"""
probe_helmert_fourier_fusion_metric.py  --  the S-D fusion-contingent metric, three riders, exact frame.

Frame B: exact rank & trace (sympy, kappa as a radical) anchor each matrix; the SIGNATURE is read from
40-digit eigenvalues (certain -- nonzero eigenvalues are O(1), separated from the exact zeros). Reads
SIGNATURE, not conditioning. Question (Leo): does cross-prime fusion-closure (N9: zeta and primitive L
fusion-closed; Davenport-Heilbronn NOT) appear in the Helmert-Fourier frame as a SIGNATURE, and which
of three riders for the L-data carries it?

DATA on (Z/5)^x = {1,2,3,4} (DH's conductor). chi = order-4 char, chi(2)=i. a_DH = Re chi + kappa Im chi:
   zeta : a = (1, 1, 1, 1)            fusion-closed (trivial char)
   chi  : a = (1, i, -i, -1)          fusion-closed (order-4, primitive, complex)
   DH   : a = (1, kappa, -kappa, -1)  NOT fusion-closed (cross defect 1+kappa^2)
kappa = (sqrt(10 - 2 sqrt5) - 2)/(sqrt5 - 1) ~ 0.2841 (exact algebraic real).

(i)  cross-prime: Phi[m,n] = a(mn mod 5)           (ii) intra-prime: Hankel of a(p^k)
(iii) archimedean apex: positive weight congruence Phi -> W Phi W  (Sylvester -> inertia-neutral)
"""
import sympy as sp
import numpy as np

kappa = (sp.sqrt(10 - 2 * sp.sqrt(5)) - 2) / (sp.sqrt(5) - 1)
I = sp.I
G = [1, 2, 3, 4]
dlog = {1: 0, 2: 1, 4: 2, 3: 3}
A = {
    "zeta": {g: sp.Integer(1) for g in G},
    "chi ": {g: I**dlog[g] for g in G},
    "DH  ": {1: sp.Integer(1), 2: kappa, 3: -kappa, 4: sp.Integer(-1)},
}


def npmat(P):
    return np.array([[complex(sp.N(P[i, j], 40)) for j in range(P.cols)] for i in range(P.rows)])


def signature(P):
    """(n+, n-, n0) from 40-digit eigenvalues; None if not Hermitian."""
    M = npmat(P)
    if not np.allclose(M, M.conj().T, atol=1e-15):
        return None
    ev = np.linalg.eigvalsh(M)
    tol = 1e-13 * max(1.0, np.max(np.abs(ev)))
    return (int(np.sum(ev > tol)), int(np.sum(ev < -tol)), int(np.sum(np.abs(ev) <= tol)))


def report(name, P):
    rk = P.rank()
    tr = sp.simplify(sp.trace(P))
    sg = signature(P)
    print(f"  {name}:  exact rank = {rk},  exact trace = {tr},  signature (n+,n-,n0) = {sg}")


print("=" * 92)
print("RIDER (i)   cross-prime fusion matrix  Phi[m,n] = a(m*n mod 5)")
print("=" * 92)
for name, a in A.items():
    Phi = sp.Matrix(4, 4, lambda i, j: a[(G[i] * G[j]) % 5])
    report(name, Phi)
print("  (chi: complex-symmetric, not Hermitian -> signature n/a; rank is the fusion invariant there)")

print("\n" + "=" * 92)
print("RIDER (ii)  intra-prime local Hankel  H[i,j] = a(2^(i+j) mod 5)")
print("=" * 92)
chi2 = {1: sp.Integer(1), 4: sp.Integer(1), 2: sp.Integer(-1), 3: sp.Integer(-1)}  # real order-2 char
locals_ = {"zeta (a=1)         ": A["zeta"], "chi2 (real L-local)": chi2, "DH  (Re chi+k Im) ": A["DH  "]}
nloc = 4
for name, a in locals_.items():
    b = [a[pow(2, k, 5)] for k in range(2 * nloc - 1)]
    H = sp.Matrix(nloc, nloc, lambda i, j: b[i + j])
    seq = [sp.N(x, 3) for x in b[:4]]
    print(f"  {name}: a(2^k)={seq} -> exact rank={H.rank()}, signature={signature(H)}")

print("\n" + "=" * 92)
print("RIDER (iii) archimedean apex weight as a congruence  Phi -> W Phi W,  W=diag>0 (Sylvester)")
print("=" * 92)
W = sp.diag(sp.Rational(7, 3), sp.Rational(5, 2), sp.Rational(11, 4), sp.Rational(9, 5))
for name in ("zeta", "DH  "):
    a = A[name]
    Phi = sp.Matrix(4, 4, lambda i, j: a[(G[i] * G[j]) % 5])
    print(f"  {name}: signature(Phi)={signature(Phi)}  ->  signature(W Phi W)={signature(W * Phi * W)}  "
          f"(W alone PSD: {signature(W * W)})")

print("\n" + "=" * 92)
print("FACTS (for interpretation)")
print("=" * 92)
print("  rider (i): fusion-closed data -> Phi rank 1 (single sign); non-fusion-closed (DH) -> ?")
print("  rider (ii): single prime = no cross-prime; intra-prime recurrence holds for DH (N9).")
print("  rider (iii): positive congruence preserves inertia exactly (Sylvester).")
