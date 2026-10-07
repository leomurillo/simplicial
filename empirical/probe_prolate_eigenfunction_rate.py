"""
Prolate eigenfunction rate (CCM 2511.22755 Lemma 7.2) as harmonic-oscillator perturbation theory.

CCM's prolate wave operator:  PW_lambda = -d_x((lambda^2 - x^2) d_x) + (2 pi lambda x)^2  on [-lambda, lambda].
Rescale x = lambda*u  (u in [-1,1]):  PW_lambda = -d_u((1-u^2) d_u) + (2 pi lambda^2)^2 u^2 = Slepian L_c with
BANDWIDTH c = 2 pi lambda^2.  So c ~ lambda^2, and 1/c ~ lambda^{-2}: the Lemma-7.2 rate should be the
FIRST harmonic-oscillator perturbation order.

Rescale to the oscillator variable t = sqrt(c) * u (concentration scale of the low eigenfunctions):
    L_c / c = (-d_t^2 + t^2)  +  (1/c) * W,     W = d_t(t^2 d_t) = t^2 d_t^2 + 2 t d_t   (<=0).
So  M(c) := L_c/c = H_osc + (1/c) W   is the harmonic oscillator H_osc = -d_t^2 + t^2 plus a (1/c)
perturbation.  First-order eigenvector perturbation theory => || h_{n,lambda} - h_n || = O(1/c) = O(lambda^{-2}).
This DERIVES the CCM lambda^{-2} rate (center region); the Meixner-Schaefke "Satz 9" uniform-on-[-1,1]
remainder (boundary/turning-point) is weaker, but the sup-error is center-dominated (eigenfns are
exp-small at the boundary), so the realized sup-rate should be lambda^{-2}.

This probe VERIFIES the rate exactly-numerically by comparing h_{n,lambda} (finite c) to h_n (c=inf, pure
H_osc) ON THE SAME GRID -- so the finite-difference discretization bias CANCELS and only the 1/c effect
remains.  Fit log(sup-error) vs log(lambda); expect slope ~ -2.

No torch. numpy + scipy.linalg.eigh_tridiagonal.
"""
import numpy as np
from scipy.linalg import eigh_tridiagonal

T, NGRID = 12.0, 6000           # t in [-T,T]; fine enough that same-grid comparison floor << lambda^{-2}
t = np.linspace(-T, T, NGRID + 2)[1:-1]
dt = t[1] - t[0]
tmid = (t[:-1] + t[1:]) / 2     # half-grid points for the SL weight


def operator(inv_c):
    """tridiagonal (diag, off) of M = H_osc + inv_c * W on the t-grid (symmetric SL discretization)."""
    w = tmid ** 2                                   # SL weight for W = d_t(t^2 d_t)
    # H_osc kinetic -d_t^2: diag 2/dt^2, off -1/dt^2 ; potential +t^2 on diag
    diag = 2.0 / dt**2 + t**2
    off = -np.ones(NGRID - 1) / dt**2
    # W (negative semidef): diag -(w_{j+1/2}+w_{j-1/2})/dt^2 ; off +w_{j+1/2}/dt^2
    wL = np.concatenate([[0.0], w])                 # w_{j-1/2}
    wR = np.concatenate([w, [0.0]])                 # w_{j+1/2}
    diag = diag + inv_c * (-(wL + wR) / dt**2)
    off = off + inv_c * (w / dt**2)
    return diag, off


def bottom_even_vectors(inv_c, k=5):
    d, e = operator(inv_c)
    vals, vecs = eigh_tridiagonal(d, e, select='i', select_range=(0, k - 1))
    return vals, vecs                                # columns normalized (discrete L2 = 1)


def aligned_sup_diff(v_c, v_inf):
    s = 1.0 if np.dot(v_c, v_inf) >= 0 else -1.0
    return np.max(np.abs(s * v_c - v_inf))


if __name__ == "__main__":
    print("Prolate eigenfunction rate = harmonic-oscillator 1/c perturbation (CCM Lemma 7.2)")
    print(f"  operator M(c)=H_osc+(1/c)W on t in [-{T},{T}], N={NGRID};  c=2 pi lambda^2")
    print("  comparing h_{n,lambda} (finite c) to h_n (c=inf) on the SAME grid (discretization cancels)")
    print("=" * 80)

    # reference: c = infinity (pure harmonic oscillator) on the same grid
    _, V_inf = bottom_even_vectors(0.0, k=6)
    # H_osc eigenvectors in order n=0,1,2,3,4,5; even ones are n=0,2,4 (columns 0,2,4)
    even_idx = [0, 2, 4]

    # validity of the (1/c)W expansion needs the grid inside |t| < sqrt(c): sqrt(2pi)*lambda > T,
    # i.e. lambda > T/sqrt(2pi) ~ 4.79.  Start at lambda=6 (sqrt(c) > T = 12).
    lambdas = np.array([6, 8, 10, 12, 14, 16, 20, 24, 28, 32], dtype=float)
    errs = {n: [] for n in even_idx}
    for lam in lambdas:
        c = 2 * np.pi * lam**2
        _, V = bottom_even_vectors(1.0 / c, k=6)
        for n in even_idx:
            errs[n].append(aligned_sup_diff(V[:, n], V_inf[:, n]))

    print(f"  {'lambda':>7} | {'c=2pi l^2':>10} | " + " | ".join(f'n={n} sup-err' for n in even_idx))
    print("  " + "-" * 74)
    for i, lam in enumerate(lambdas):
        c = 2 * np.pi * lam**2
        row = " | ".join(f"{errs[n][i]:.3e}" for n in even_idx)
        print(f"  {lam:>7.0f} | {c:>10.1f} | {row}")

    print("  " + "-" * 74)
    print("  fitted rate  err ~ lambda^p  (least squares on log-log; expect p ~ -2):")
    L = np.log(lambdas)
    for n in even_idx:
        p, b = np.polyfit(L, np.log(np.array(errs[n])), 1)
        # also fit vs 1/c to check the const: err ~ A/c
        c_arr = 2 * np.pi * lambdas**2
        A = np.mean(np.array(errs[n]) * c_arr)
        print(f"    n={n}:  p = {p:+.3f}   (err*c ~ const: A = {A:.3f}, std/mean = "
              f"{np.std(np.array(errs[n])*c_arr)/A:.2%})")

    print("=" * 80)
    print("VERDICT.  If p ~ -2 and err*c ~ const, the CCM Lemma-7.2 rate lambda^{-2} IS the first")
    print("harmonic-oscillator perturbation order (1/c) -- classical, derivable, verified.  The residual")
    print("CCM obstacle is NOT this rate but PROPAGATING it through the arithmetic rank-one perturbation")
    print("A_lambda to control mu_lambda -> 0 (the Davis-Kahan gap-vs-perturbation race; see writeup).")
