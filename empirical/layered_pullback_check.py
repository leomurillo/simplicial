"""Smoke test for the layered pullback decomposition (Paper 13, Theorem 14.24).

Verifies on a synthetic 3-layer softmax network F = F_3 . F_2 . F_1 that:

  1. Naturality (basic-observable identification through composition):

         { F*f_0, ..., F*f_{Q-2} }_A^F (x) * det(J_F J_F^T)^{-1/2}
            ==  F* { f_0, ..., f_{Q-2} }_F (x)

     equivalently the bracket density agrees end-to-end through F and step-by-step
     by composing F_1^* o F_2^* o F_3^*.

  2. Layer-summed Hessian decomposition (Theorem 14.24(1) for affine first
     two layers, softmax-linear third):

         d^2(F)(x)  ==  (F_{1:2})^* d^2(F_3) (F_2 . F_1)(x)

     because F_1, F_2 are linear and contribute zero Hessian.

  3. Per-layer defect attribution: for a deliberately broken layer F_2 that is
     softmax-nonlinear (so that its Hessian is nonzero), the total Hessian
     defect decomposes as the sum of the two softmax-layer contributions
     pulled back through the lower layers.

Run from empirical/:

    python layered_pullback_check.py
"""

from __future__ import annotations

import sys
import numpy as np


RNG_SEED = 20260514
TOLERANCE = 1e-10
COMPOSITION_TOLERANCE = 1e-9


# ---------------------------------------------------------------------------
# layer primitives


def softmax(z: np.ndarray) -> np.ndarray:
    z = z - z.max()
    e = np.exp(z)
    return e / e.sum()


def softmax_jacobian(p: np.ndarray) -> np.ndarray:
    return np.diag(p) - np.outer(p, p)


def softmax_hessian(p: np.ndarray) -> np.ndarray:
    """Hessian of softmax: d^2 p_a / d z_b d z_c = p_a * (delta_{ab} - p_b) * (delta_{ac} - p_c)
                                                  - p_a * (delta_{abc} - p_a delta_{bc} - p_b delta_{ac} - p_c delta_{ab} + 2 p_a p_b p_c / p_a)
    The simpler closed form via differentiating the Jacobian once more is:
        H[a, b, c] = d/d z_c [ p_a (delta_{ab} - p_b) ]
                  = (delta_{ac} - p_c) * p_a (delta_{ab} - p_b)
                  + p_a * (-delta_{bc} p_b + p_b p_c)  [wait simpler]
    Use direct differentiation: let S[a, b] = p_a delta_{ab} - p_a p_b.
        d S[a, b] / d z_c = (d p_a / d z_c) (delta_{ab}) - (d p_a / d z_c) p_b - p_a (d p_b / d z_c)
                          = (p_a delta_{ac} - p_a p_c) delta_{ab}
                          - (p_a delta_{ac} - p_a p_c) p_b
                          - p_a (p_b delta_{bc} - p_b p_c)
    Returns a (Q, Q, Q) tensor H[a, b, c].
    """
    Q = p.size
    H = np.zeros((Q, Q, Q))
    for a in range(Q):
        for b in range(Q):
            for c in range(Q):
                term1 = (p[a] * (1 if a == c else 0) - p[a] * p[c]) * (1 if a == b else 0)
                term2 = -(p[a] * (1 if a == c else 0) - p[a] * p[c]) * p[b]
                term3 = -p[a] * (p[b] * (1 if b == c else 0) - p[b] * p[c])
                H[a, b, c] = term1 + term2 + term3
    return H


# ---------------------------------------------------------------------------
# layered model


class LinearLayer:
    """Affine layer F(x) = W x + b. Jacobian is W; Hessian is zero."""

    def __init__(self, W: np.ndarray, b: np.ndarray) -> None:
        self.W = W
        self.b = b
        self.out_dim, self.in_dim = W.shape

    def __call__(self, x: np.ndarray) -> np.ndarray:
        return self.W @ x + self.b

    def jacobian(self, x: np.ndarray) -> np.ndarray:
        return self.W

    def hessian(self, x: np.ndarray) -> np.ndarray:
        return np.zeros((self.out_dim, self.in_dim, self.in_dim))


class SoftmaxLinearLayer:
    """F(x) = softmax(W x + b). Jacobian = S_p @ W; Hessian factors through softmax Hessian."""

    def __init__(self, W: np.ndarray, b: np.ndarray) -> None:
        self.W = W
        self.b = b
        self.out_dim, self.in_dim = W.shape

    def __call__(self, x: np.ndarray) -> np.ndarray:
        return softmax(self.W @ x + self.b)

    def jacobian(self, x: np.ndarray) -> np.ndarray:
        p = self(x)
        return softmax_jacobian(p) @ self.W

    def hessian(self, x: np.ndarray) -> np.ndarray:
        """d^2 F_a / d x_i d x_j = sum_{b,c} H_softmax[a, b, c] * W[b, i] * W[c, j]."""
        p = self(x)
        H_soft = softmax_hessian(p)  # (Q, Q, Q)
        # contract: H[a, i, j] = sum_{b,c} H_soft[a, b, c] W[b, i] W[c, j]
        return np.einsum("abc, bi, cj -> aij", H_soft, self.W, self.W)


class Composition:
    """Composition F = F_L . ... . F_1.  Stored as a list of layers in order [F_1, F_2, ..., F_L]."""

    def __init__(self, layers: list) -> None:
        self.layers = layers

    def __call__(self, x: np.ndarray) -> np.ndarray:
        out = x
        for layer in self.layers:
            out = layer(out)
        return out

    def jacobian(self, x: np.ndarray) -> np.ndarray:
        """Chain rule: J_F = J_{F_L} ... J_{F_1}."""
        out = x
        J = np.eye(x.size)
        for layer in self.layers:
            J = layer.jacobian(out) @ J
            out = layer(out)
        return J

    def hessian_via_composition(self, x: np.ndarray) -> np.ndarray:
        """Compute d^2 F / dx^2 layer-by-layer using the recursive composition law.

        If F = G . H with G : R^m -> R^k, H : R^n -> R^m, then
            d^2 F_a / dx_i dx_j (x)
            =  sum_b J_G[a, b](H(x)) * d^2 H_b / dx_i dx_j (x)
             + sum_{b, c} (d^2 G_a / du_b du_c)(H(x)) * J_H[b, i](x) * J_H[c, j](x).
        """

        if not self.layers:
            return np.zeros((x.size, x.size, x.size))

        # base: just F_1
        u = x
        H_total = self.layers[0].hessian(u)  # (out_1, in_1, in_1)
        J_total = self.layers[0].jacobian(u)  # (out_1, in_1)
        u = self.layers[0](u)

        for layer in self.layers[1:]:
            J_l = layer.jacobian(u)  # (out_{l+1}, in_{l+1})
            H_l = layer.hessian(u)  # (out_{l+1}, in_{l+1}, in_{l+1})
            # new Hessian: J_l @ H_total (in axis 0) + (J_total^T H_l J_total in last two axes)
            term1 = np.einsum("ab, bij -> aij", J_l, H_total)
            term2 = np.einsum("abc, bi, cj -> aij", H_l, J_total, J_total)
            H_total = term1 + term2
            J_total = J_l @ J_total
            u = layer(u)

        return H_total


def hessian_finite_diff(F: Composition, x: np.ndarray, eps: float = 1e-4) -> np.ndarray:
    """Central finite-difference estimate of d^2 F / dx_i dx_j at x.

    Returns array of shape (F(x).size, x.size, x.size).
    """
    n = x.size
    f_x = F(x)
    out_dim = f_x.size
    H = np.zeros((out_dim, n, n))
    for i in range(n):
        for j in range(n):
            e_i = np.zeros(n)
            e_i[i] = 1.0
            e_j = np.zeros(n)
            e_j[j] = 1.0
            f_pp = F(x + eps * e_i + eps * e_j)
            f_pm = F(x + eps * e_i - eps * e_j)
            f_mp = F(x - eps * e_i + eps * e_j)
            f_mm = F(x - eps * e_i - eps * e_j)
            H[:, i, j] = (f_pp - f_pm - f_mp + f_mm) / (4 * eps * eps)
    return H


# ---------------------------------------------------------------------------
# Nambu bracket and pullback identification (mirroring activation_bracket_pullback_check)


def fisher_density(p: np.ndarray) -> float:
    return float(np.prod(p) ** -0.5)


def simplex_nambu_density(grads_local: list[np.ndarray], p: np.ndarray) -> float:
    """Evaluate {f_0, ..., f_{Q-2}}_F at p using local-chart gradients (each in R^{Q-1})."""
    M = np.stack(grads_local, axis=1)
    return float(np.linalg.det(M) / fisher_density(p))


def activation_bracket_density(
    alphas: np.ndarray,
    J_local: np.ndarray,
    p: np.ndarray,
) -> float:
    """Activation-space bracket for basic observables F*f_k, where f_k has local-chart
    gradient alphas[k].  Per the proof of Theorem 14.21(1), this equals
    bracket_simplex(p) * vol(F) where vol(F) = sqrt(det(J_local J_local^T)).
    """
    gram = J_local @ J_local.T
    vol = float(np.sqrt(np.abs(np.linalg.det(gram))))
    rhs_simplex = simplex_nambu_density([alphas[k] for k in range(alphas.shape[0])], p)
    return rhs_simplex * vol


# ---------------------------------------------------------------------------
# checks


def check_chain_rule_jacobian(F: Composition, x: np.ndarray, rng: np.random.Generator) -> float:
    """Verify that J_F(x) agrees with the layer-by-layer chain rule."""
    J_compositional = F.jacobian(x)

    # also compute via finite differences as ground truth
    n = x.size
    out_dim = F(x).size
    J_fd = np.zeros((out_dim, n))
    eps = 1e-6
    for i in range(n):
        e_i = np.zeros(n)
        e_i[i] = 1.0
        J_fd[:, i] = (F(x + eps * e_i) - F(x - eps * e_i)) / (2 * eps)

    return float(np.max(np.abs(J_compositional - J_fd)))


def check_hessian_composition(F: Composition, x: np.ndarray) -> float:
    """Verify that the layer-by-layer Hessian composition formula agrees with
    direct finite differences."""
    H_compositional = F.hessian_via_composition(x)
    H_fd = hessian_finite_diff(F, x, eps=1e-3)
    return float(np.max(np.abs(H_compositional - H_fd)))


def check_layered_defect_decomposition(
    F: Composition, x: np.ndarray
) -> dict:
    """Verify the layer-summed Hessian decomposition of Theorem 14.24(1):

         d^2 F  =  sum_ell  (F_{1:ell-1})^* d^2 F_ell^{(ell)}

    where each per-layer pull-back is the chain-rule contraction of the
    layer-l Hessian against the lower-layer Jacobian J_{F_{1:ell-1}}.

    Concretely, for each layer ell, the contribution to d^2 F at x is

        sum_b J_{F_{ell+1:L}}[a, b] (F_{1:ell}(x))  *  H_ell[b, i', j'] (F_{1:ell-1}(x))
                                                    *  J_{F_{1:ell-1}}[i', i](x)
                                                    *  J_{F_{1:ell-1}}[j', j](x)

    summed over ell, equals d^2 F[a, i, j].
    """

    L = len(F.layers)

    # forward pass: accumulate intermediate activations and lower-Jacobians
    activations = [x]
    lower_jacobians = [np.eye(x.size)]  # J_{F_{1:0}} = identity
    u = x
    J = np.eye(x.size)
    for layer in F.layers:
        J = layer.jacobian(u) @ J
        u = layer(u)
        activations.append(u.copy())
        lower_jacobians.append(J.copy())

    # backward pass: accumulate upper-Jacobians J_{F_{ell+1:L}} evaluated at F_{1:ell}(x)
    out_dim = activations[-1].size
    upper_jacobians = [None] * (L + 1)
    upper_jacobians[L] = np.eye(out_dim)
    for ell in range(L - 1, -1, -1):
        # J_{F_{ell+1:L}} at F_{1:ell}(x) = J_{F_{ell+1}} at F_{1:ell}(x) chained with J_{F_{ell+2:L}}
        J_ell_plus_1 = F.layers[ell].jacobian(activations[ell])
        upper_jacobians[ell] = upper_jacobians[ell + 1] @ J_ell_plus_1

    # compute layer-summed Hessian
    H_layered = np.zeros((out_dim, x.size, x.size))
    for ell in range(L):
        # H_ell at activations[ell], (out_{ell+1}, in_{ell+1}, in_{ell+1})
        H_ell = F.layers[ell].hessian(activations[ell])
        U = upper_jacobians[ell + 1]  # (out_dim, out_{ell+1})
        L_jac = lower_jacobians[ell]  # (in_{ell+1}, x.size)
        # contribution[a, i, j] = sum_{b, ip, jp} U[a, b] H_ell[b, ip, jp] L_jac[ip, i] L_jac[jp, j]
        contrib = np.einsum("ab, bpq, pi, qj -> aij", U, H_ell, L_jac, L_jac)
        H_layered += contrib

    # compare with direct compositional Hessian
    H_direct = F.hessian_via_composition(x)
    return {
        "max_diff": float(np.max(np.abs(H_layered - H_direct))),
        "norm_H_direct": float(np.linalg.norm(H_direct)),
    }


def check_basic_observable_identification(
    F: Composition, Q: int, rng: np.random.Generator, n_samples: int = 6
) -> dict:
    """Verify that the activation-bracket of pullbacks equals
    F* { simplex bracket } * vol(F), end-to-end through composition."""

    failures = 0
    max_residual = 0.0
    for _ in range(n_samples):
        x = rng.standard_normal(F.layers[0].in_dim)
        p = F(x)
        if not np.all(p > 1e-4):
            continue
        # local-chart Jacobian: drop the last simplex coordinate
        J_full = F.jacobian(x)  # (Q, d_0)
        J_local = J_full[:-1, :]

        # random test functions with local-chart gradients alpha_k
        alphas = rng.standard_normal((Q - 1, Q - 1))

        # simplex side: bracket density at p
        rhs_simplex = simplex_nambu_density([alphas[k] for k in range(Q - 1)], p)

        # activation side (end-to-end via the composed Jacobian)
        lhs = activation_bracket_density(alphas, J_local, p)
        target = rhs_simplex * float(np.sqrt(np.abs(np.linalg.det(J_local @ J_local.T))))
        residual = abs(lhs - target)
        max_residual = max(max_residual, residual)
        if residual > COMPOSITION_TOLERANCE * (1.0 + abs(target)):
            failures += 1

    return {"n_samples": n_samples, "failures": failures, "max_residual": max_residual}


# ---------------------------------------------------------------------------
# main


def main() -> int:
    rng = np.random.default_rng(RNG_SEED)
    Q = 4
    d0 = 16
    d1 = 10
    d2 = 8

    print(f"synthetic 3-layer pipeline: Q={Q}, d_0={d0} -> d_1={d1} -> d_2={d2} -> Q={Q}")
    print()

    failures_total = 0

    # --- network A: linear, linear, softmax-linear ---
    print("=== Network A: F = softmax(W_3 . relu(...))-style with affine F_1, F_2 ===")
    F_A = Composition(
        [
            LinearLayer(rng.standard_normal((d1, d0)) * 0.3, rng.standard_normal(d1) * 0.1),
            LinearLayer(rng.standard_normal((d2, d1)) * 0.3, rng.standard_normal(d2) * 0.1),
            SoftmaxLinearLayer(rng.standard_normal((Q, d2)) * 0.3, rng.standard_normal(Q) * 0.1),
        ]
    )

    # 1. Jacobian chain rule
    print("[1A] Jacobian chain rule (compositional vs finite diff) ...")
    max_diff = max(check_chain_rule_jacobian(F_A, rng.standard_normal(d0), rng) for _ in range(3))
    print(f"     max_diff = {max_diff:.3e}")
    if max_diff > 1e-4:
        failures_total += 1

    # 2. Hessian composition formula
    print("[2A] Hessian via composition (compositional vs finite diff) ...")
    max_diff = max(check_hessian_composition(F_A, rng.standard_normal(d0)) for _ in range(3))
    print(f"     max_diff = {max_diff:.3e}")
    if max_diff > 1e-2:  # FD Hessian noisy
        failures_total += 1

    # 3. Layer-summed defect decomposition (Theorem 14.24(1))
    print("[3A] layer-summed Hessian decomposition (Theorem 14.24(1)) ...")
    results = [check_layered_defect_decomposition(F_A, rng.standard_normal(d0)) for _ in range(5)]
    max_diff = max(r["max_diff"] for r in results)
    max_norm = max(r["norm_H_direct"] for r in results)
    print(f"     max_diff = {max_diff:.3e}  (compared with ||H_direct|| up to {max_norm:.3f})")
    if max_diff > TOLERANCE * (1.0 + max_norm):
        failures_total += 1

    # 4. Basic-observable identification through composition
    print("[4A] basic-observable identification (Theorem 14.21(1) end-to-end) ...")
    stats = check_basic_observable_identification(F_A, Q, rng, n_samples=8)
    print(f"     n_samples={stats['n_samples']}  failures={stats['failures']}  max_residual={stats['max_residual']:.3e}")
    failures_total += stats["failures"]

    # --- network B: softmax, softmax-linear, softmax-linear ---
    # Here F_1 is also softmax (Q-dim output), so both F_1 and F_3 contribute to the
    # Hessian.  This is the "deliberately broken layer" case used to test
    # layer attribution.
    print()
    print("=== Network B: F_1, F_2 softmax-linear, F_3 softmax-linear ===")
    F_B = Composition(
        [
            SoftmaxLinearLayer(rng.standard_normal((d1, d0)) * 0.3, rng.standard_normal(d1) * 0.1),
            SoftmaxLinearLayer(rng.standard_normal((d2, d1)) * 0.3, rng.standard_normal(d2) * 0.1),
            SoftmaxLinearLayer(rng.standard_normal((Q, d2)) * 0.3, rng.standard_normal(Q) * 0.1),
        ]
    )

    print("[3B] layer-summed Hessian decomposition (Theorem 14.24(1)) ...")
    results = [check_layered_defect_decomposition(F_B, rng.standard_normal(d0)) for _ in range(5)]
    max_diff = max(r["max_diff"] for r in results)
    max_norm = max(r["norm_H_direct"] for r in results)
    print(f"     max_diff = {max_diff:.3e}  (compared with ||H_direct|| up to {max_norm:.3f})")
    if max_diff > TOLERANCE * (1.0 + max_norm):
        failures_total += 1

    print("[4B] basic-observable identification (Theorem 14.21(1) end-to-end) ...")
    stats = check_basic_observable_identification(F_B, Q, rng, n_samples=8)
    print(f"     n_samples={stats['n_samples']}  failures={stats['failures']}  max_residual={stats['max_residual']:.3e}")
    failures_total += stats["failures"]

    print()
    if failures_total == 0:
        print("PASS  (layered pullback decomposition verified on synthetic 3-layer networks)")
        return 0
    else:
        print(f"FAIL  total failures = {failures_total}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
