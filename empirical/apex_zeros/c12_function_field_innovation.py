"""
C12 -- the function-field innovation chain: the provable template for d(s) > 0.

Ports P infinity-F section 19's Gohberg-Krein innovation chain to the place where
positivity is a THEOREM (Weil). For a curve C/F_q the Weil form is the real
symmetric TOEPLITZ matrix of the normalized point counts
    a_k = (q^k + 1 - N_k) / q^{k/2}  =  sum_i (alpha_i / sqrt q)^k,
and the dictionary is exact:

  * innovation d(s)              = Levinson-Durbin prediction error E_m
  * Gohberg-Krein/Schur params   = reflection coefficients k_m
  * "factorizes outer, no inner" = |k_m| <= 1 for all m   (Schur/Szego)
  * d(s) > 0 for all s           = Toeplitz PSD = (a_k) positive-definite
                                 = normalized Frobenius UNITARY = |alpha_i|=sqrt q
                                 = WEIL PURITY (the curve RH).
  * "Weil process asympt. det."  = E_m -> 0 (finite 2g sinusoids, perfectly
                                   predictable at order 2g) -- from ABOVE, by purity.

So the open archimedean step "d(s)>0 for all s" is, in the solvable place, exactly
Herglotz/Szego positive-definiteness of the point-count sequence, which Frobenius
hands over for free (it is unitary after the sqrt q rescale). The fake-curve test
(an eigenvalue pushed OFF the circle, FE preserved) makes a_k grow, drives a
reflection coefficient past 1, and a prediction error NEGATIVE -- the innovation
chain detecting a zero leaving the critical circle. That is (H0') failing,
made literal in the place where it cannot.
"""

import math
import numpy as np
from ff_core import make_chars, fermat_count_Fp
from c10_higher_genus import Lpoly as quartic_Lpoly


def cubic_eigs(q):
    a = q + 1 - fermat_count_Fp(q, 3)
    return np.roots([1.0, -a, q])                 # 2 eigenvalues, |.|=sqrt q (Hasse)


def quartic_eigs(q):
    c, _ = quartic_Lpoly(q)
    return np.roots(c)                            # 6 eigenvalues, |.|=sqrt q (Weil)


def normalized_traces(eigs, q, M):
    """a_k = sum_i (alpha_i/sqrt q)^k  (= (q^k+1-N_k)/q^{k/2}, the geometric data)."""
    sq = math.sqrt(q)
    return np.array([float(np.real(sum((al / sq) ** k for al in eigs))) for k in range(M + 1)])


def levinson_durbin(a, rtol=1e-9):
    """
    Real symmetric Toeplitz T[i,j]=a[|i-j|]. Returns (errors E_0..E_r, reflections k_1..k_r),
    STOPPING at rank saturation (E <= rtol*a_0): a curve has 2g Frobenius sinusoids, so the
    Weil process is perfectly predictable at order 2g and the innovation hits 0 -- the tail
    is deterministic (0/0), not informative. PSD (valid autocorrelation) <=> |k_m|<=1 and
    E_m>=0. The E_m ARE section 19's innovation/prediction-error rates d(s); k_m are the
    Gohberg-Krein/Schur reflection coefficients.
    """
    M = len(a) - 1
    A = np.zeros(M + 1); A[0] = 1.0
    E = a[0]
    errs = [E]; refl = []
    for m in range(1, M + 1):
        if E <= rtol * abs(a[0]):                 # rank reached (process deterministic)
            break
        acc = a[m] + sum(A[i] * a[m - i] for i in range(1, m))
        k = -acc / E
        Anew = A.copy()
        for i in range(1, m):
            Anew[i] = A[i] + k * A[m - i]
        Anew[m] = k
        A = Anew
        E = E * (1.0 - k * k)
        refl.append(k); errs.append(E)
    return errs, refl


def report(eigs, q, label, M, fake=False):
    a = normalized_traces(eigs, q, M)
    twog = len(eigs)
    rtol = 1e-6 * max(1.0, a[0])
    Tz = np.array([[a[abs(i - j)] for j in range(M + 1)] for i in range(M + 1)])
    min_eig = float(np.linalg.eigvalsh(Tz).min())          # PSD verdict (rank-noise robust)
    errs, refl = levinson_durbin(a)                        # innovations to rank saturation
    max_refl = max((abs(k) for k in refl), default=0.0)    # meaningful Schur params only
    min_err = min(errs)
    bounded = max(abs(x) for x in a) <= twog + 1e-6        # |a_k| <= 2g iff on the circle
    psd = (min_eig > -rtol) and bounded and (max_refl <= 1 + 1e-6) and (min_err > -rtol)
    verdict_ok = (psd != fake)                             # pure -> PSD; fake -> indefinite
    tag = "FAKE off-circle" if fake else "real curve"
    print(f"  [{label}] {tag}, q={q}, 2g={twog}:")
    print(f"       |a_k|<=2g: {bounded} (max|a_k|={max(abs(x) for x in a):.3f}); "
          f"Toeplitz min-eig={min_eig:+.2e}; max|Schur k_m|={max_refl:.3f}")
    print(f"       innovations d(s)=E_m (to rank 2g): "
          f"{['%.3f' % e for e in errs]}  -> 0 (determinism)")
    print(f"       => purity/PSD={psd}  [d(s)>0 for all s <=> |alpha|=sqrt q]  "
          f"{'OK' if verdict_ok else 'FAIL'}")
    return verdict_ok


def fake_cubic(q, scale=1.4):
    """RH-false g=1 spectrum: real FE pair {beta, q/beta}, |beta|!=sqrt q (off the circle)."""
    beta = math.sqrt(q) * scale
    return np.array([beta, q / beta])


def fake_quartic(q, scale=1.5):
    """Push one conjugate pair of the genuine sextic off the circle, keep FE alpha<->q/alpha."""
    eigs = list(quartic_eigs(q))
    eigs.sort(key=lambda z: (round(z.real, 6), z.imag))
    # replace the top conjugate pair by a real FE pair off the circle
    b = math.sqrt(q) * scale
    eigs[-1] = b; eigs[-2] = q / b
    return np.array(eigs)


def main():
    print("=" * 80)
    print("C12 -- function-field innovation chain: Levinson on the point-count Toeplitz")
    print("       d(s)>0 (innovation positive) <=> Weil purity |alpha|=sqrt q")
    print("=" * 80)
    ok = True
    print("  REAL CURVES (Weil purity => innovations positive, then -> 0 = determinism):")
    for q in (7, 13, 19, 31, 61):
        ok = report(cubic_eigs(q), q, f"Fermat cubic g=1", M=6) and ok
    for q in (13, 17, 29):
        ok = report(quartic_eigs(q), q, f"Fermat quartic g=3", M=10) and ok
    print("  FAKE OFF-CIRCLE SPECTRA (RH-false => a reflection passes 1, an innovation < 0):")
    ok = report(fake_cubic(13), 13, "cubic, beta off-circle", M=6, fake=True) and ok
    ok = report(fake_cubic(31), 31, "cubic, beta off-circle", M=6, fake=True) and ok
    ok = report(fake_quartic(17), 17, "quartic, pair off-circle", M=10, fake=True) and ok
    print("-" * 80)
    print("C12:", "PASS" if ok else "FAIL")
    return ok


if __name__ == "__main__":
    import sys
    sys.exit(0 if main() else 1)
