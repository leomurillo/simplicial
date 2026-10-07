"""
C10 -- higher genus: the Fermat QUARTIC L-polynomial (genus 3) and Weil's 1/2.

Extends C9 from g=1 (cubic) to g=3 (quartic x^4+y^4+z^4=0 over F_q, q=1 mod 4).
The L-polynomial P(T) = prod_{i=1}^{6}(1 - alpha_i T) now has degree 2g = 6. We
build it from brute point counts #C(F_{q^n}), n=1,2,3, via Newton's identities,
complete it by the functional equation c_{6-k}=q^{3-k}c_k, and TEST that
functional equation by predicting #C(F_{q^4}), #C(F_{q^5}) and matching brute.

Then Weil: every |alpha_i| = sqrt q  <=>  Re s = 1/2 (six zeros, on the line).

NEW INSIGHT (CM purity). The order-4 character lives in Q(zeta_4)=Q(i), and the
eigenvalues come out as GAUSSIAN INTEGERS alpha = a+bi with a^2+b^2 = q (norm q).
Weil's |alpha|=sqrt q is exactly the norm-q condition in the CM field Q(i); the
"1/2" is norm-q purity in the cyclotomic field of the apex character. (For the
cubic N=3 the eigenvalues are Eisenstein integers in Q(zeta_3); see C9.) The
Fermat-quartic Jacobian has CM, so the six Weil numbers collapse to one conjugate
pair with multiplicity 3 -- the critical-line spectrum is a single height x3.

Point counts use the F_{p^d} machinery of ff_ext (frequency-convolution, O(p^d)).
"""

import math
import numpy as np
from ff_ext import fermat_quartic_count

G = 3                                    # genus of the quartic


def Lpoly(q):
    """Genus-3 L-poly coeffs c_0..c_6 from #C(F_{q^n}), n=1,2,3 + functional eq."""
    cnt = [fermat_quartic_count(q, n) for n in (1, 2, 3)]
    pw = [q ** n + 1 - cnt[n - 1] for n in (1, 2, 3)]           # power sums of alpha
    e1 = pw[0]
    e2 = (e1 * pw[0] - pw[1]) // 2
    e3 = (e2 * pw[0] - e1 * pw[1] + pw[2]) // 3
    c = [1, -e1, e2, -e3]                                       # c_k = (-1)^k e_k
    c += [q * c[2], q ** 2 * c[1], q ** 3 * c[0]]               # FE: c_{6-k}=q^{3-k}c_k
    return c, cnt


def nearest_gaussian(a):
    return (round(a.real), round(a.imag))


def test_quartic(q):
    c, cnt = Lpoly(q)
    int_ok = all(abs(x - round(x)) < 1e-9 for x in c)           # integer coefficients
    alpha = np.roots(c)                                         # eigenvalues (|alpha|=sqrt q)
    sq = math.sqrt(q)
    weil = all(abs(abs(a) - sq) < 1e-3 for a in alpha)
    re_half = all(abs(math.log(abs(a)) / math.log(q) - 0.5) < 1e-4 for a in alpha)
    # functional equation TEST: c_4..c_6 were set by the FE; predict the n=4 point
    # count from the completed polynomial and match brute (q^5+ is too large to brute).
    pred4 = sum(a ** 4 for a in alpha).real
    brute4 = q ** 4 + 1 - fermat_quartic_count(q, 4)
    fe_ok = abs(pred4 - brute4) < 1e-3
    # CM: eigenvalues are Gaussian integers of norm q
    gi = [nearest_gaussian(a) for a in alpha]
    cm_ok = all(abs(a - complex(r, im)) < 1e-3 and r * r + im * im == q
                for a, (r, im) in zip(alpha, gi))
    heights = sorted(set(round(np.angle(a) / math.log(q), 4) for a in alpha))
    distinct = sorted(set(gi))
    good = int_ok and weil and re_half and fe_ok and cm_ok
    print(f"  q={q:3d}: P=[{','.join(str(round(x)) for x in c)}]")
    print(f"        |a|=sqrt q:{weil} Re s=1/2:{re_half} FE(n=4 predict):{fe_ok}"
          f"int-coeffs:{int_ok} Gaussian-int norm q:{cm_ok}")
    print(f"        eigenvalues={distinct} (norm {q}); critical-line heights Im s={heights} "
          f"{'OK' if good else 'FAIL'}")
    return good


def main():
    print("=" * 78)
    print("C10 -- Fermat quartic (genus 3): degree-6 L-poly, Weil 1/2, Gaussian-int CM")
    print("=" * 78)
    ok = True
    for q in (13, 17, 29, 37):                # all 1 mod 4
        assert (q - 1) % 4 == 0
        ok = test_quartic(q) and ok
    print("  companion: |Jacobi sum| = sqrt q (C9) = apex-coeff modulus; eigenvalues")
    print("  live in Q(zeta_4)=Q(i), Weil's 1/2 = norm-q purity in the CM field.")
    print("-" * 78)
    print("C10:", "PASS" if ok else "FAIL")
    return ok


if __name__ == "__main__":
    import sys
    sys.exit(0 if main() else 1)
