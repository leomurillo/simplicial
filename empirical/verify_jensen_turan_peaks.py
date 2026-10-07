r"""(a) on the peaks side: the Jensen / Turan / Laguerre-Polya characterization of RH.

User's lens: in a sin wave we over-regard the ZEROS and treat the PEAKS as 'just amplitude',
but the peaks (extrema, f'=0) carry the reconstruction, and the derivative hierarchy
(f=0 zeros, f'=0 peaks, f''=0 inflections, ...) is the real structure.

That crystallizes into the classical PEAKS-side characterization of RH:
  RH  <=>  the Riemann xi is in the Laguerre-Polya class (a real-rooted entire limit)
       <=>  every Jensen polynomial J_{d,n} is HYPERBOLIC (all roots real)
       <=>  the Turan inequalities hold (coefficient log-concavity).
Real-rootedness is exactly 'f and f' interlace' -- peaks and zeros alternate (Rolle + reality),
the derivative hierarchy. This is the de Bruijn-Newman heat-flow's LP class (Pass-4's Phi), and
it is STRICTLY STRONGER than the moment/Hankel positivity (which is automatic, because the
Riemann kernel Phi(t) > 0): moments = amplitude (free); Jensen hyperbolicity = peaks (the RH content).

Setup. Phi(t) = sum_{m>=1} (2 pi^2 m^4 e^{9t/2} - 3 pi m^2 e^{5t/2}) e^{-pi m^2 e^{2t}}  (Phi>0, Polya).
xi-hat(z) = int_0^inf Phi(t) cos(zt) dt = sum_n (-1)^n a_n/(2n)! z^{2n},  a_n = int_0^inf t^{2n} Phi dt.
As a function of w=z^2:  G(w) = sum_n (gamma_n/n!) w^n,  gamma_n = (-1)^n a_n n!/(2n)!.
Jensen polynomial:  J_{d,n}(t) = sum_{k=0}^d C(d,k) gamma_{n+k} t^k.   RH <=> all J_{d,n} hyperbolic.
d=2 hyperbolicity = Turan: gamma_{n+1}^2 >= gamma_n gamma_{n+2}.

PART 1 (amplitude, automatic): a_n are Stieltjes moments of Phi>0 => Hankel(a) >= 0. NOT RH.
PART 2 (peaks, the RH content): Turan (d=2) and Jensen hyperbolicity (d=2,3,4) for low n.
        Known unconditional at low degree (Csordas-Norfolk-Varga d=2; Dimitrov-Lucas d=3;
        Griffin-Ono-Rolen-Zagier: each d hyperbolic for n large). We confirm + frame.

NUMERICAL (mpmath moments + numpy root-reality), labelled.
"""

import sys
from math import comb, factorial
import mpmath as mp
import numpy as np

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass
mp.mp.dps = 30


def Phi(t):
    s = mp.mpf(0)
    for m in range(1, 7):
        m2 = mp.mpf(m) ** 2
        s += (2 * mp.pi ** 2 * m2 ** 2 * mp.e ** (mp.mpf(9) * t / 2)
              - 3 * mp.pi * m2 * mp.e ** (mp.mpf(5) * t / 2)) * mp.e ** (-mp.pi * m2 * mp.e ** (2 * t))
    return s


def moment(n):
    return mp.quad(lambda t: t ** (2 * n) * Phi(t), [0, 1, 2, 3])  # Phi negligible past t~2.5


def det_mp(M):
    M = [[mp.mpf(x) for x in row] for row in M]
    n = len(M); d = mp.mpf(1)
    for i in range(n):
        p = next((r for r in range(i, n) if M[r][i] != 0), None)
        if p is None:
            return mp.mpf(0)
        if p != i:
            M[i], M[p] = M[p], M[i]; d = -d
        d *= M[i][i]
        for r in range(i + 1, n):
            f = M[r][i] / M[i][i]
            for c in range(i, n):
                M[r][c] -= f * M[i][c]
    return d


def main():
    out = []

    def log(s=""):
        print(s); out.append(s)

    log(__doc__)

    NMAX = 9
    a = [moment(n) for n in range(NMAX)]
    log("Phi-moments a_n = int t^{2n} Phi dt (all > 0 since Phi > 0):")
    log("  " + ", ".join("a_%d=%s" % (n, mp.nstr(a[n], 6)) for n in range(NMAX)))
    log("")

    # PART 1 : amplitude / moment positivity (automatic, Phi>0) -- NOT RH
    log("================  PART 1 : amplitude = moment/Hankel positivity (automatic)  ========")
    Ds = []
    for k in range(4):
        H = [[a[i + j] for j in range(k + 1)] for i in range(k + 1)]
        Dk = det_mp(H)
        Ds.append(Dk)
        log("  Hankel det D_%d = %s   (>0)" % (k, mp.nstr(Dk, 6)))
    log("  All Hankel dets > 0: %s  -- a_n is a Stieltjes moment sequence. This is the 'amplitude'"
        % all(D > 0 for D in Ds))
    log("  condition; it is FREE (Phi>0) and is NOT RH.")
    log("")

    # PART 2 : peaks = Jensen hyperbolicity / Turan (the RH content)
    log("================  PART 2 : peaks = Jensen hyperbolicity / Turan (the RH content)  ====")
    gamma = [(mp.mpf(-1) ** n) * a[n] * mp.factorial(n) / mp.factorial(2 * n) for n in range(NMAX)]

    log("  Turan (d=2, log-concavity): gamma_{n+1}^2 >= gamma_n gamma_{n+2}  <=>  J_{2,n} hyperbolic")
    turan_ok = True
    for n in range(NMAX - 2):
        lhs = gamma[n + 1] ** 2
        rhs = gamma[n] * gamma[n + 2]
        ratio = lhs / rhs if rhs != 0 else mp.inf
        ok = lhs >= rhs
        turan_ok = turan_ok and ok
        log("    n=%d : gamma_{n+1}^2 / (gamma_n gamma_{n+2}) = %s  %s"
            % (n, mp.nstr(ratio, 8), "OK" if ok else "FAIL"))
    log("  Turan holds for all tested n: %s   (known unconditional, Csordas-Norfolk-Varga 1986)"
        % turan_ok)
    log("")

    log("  Jensen hyperbolicity J_{d,n}(t) = sum_k C(d,k) gamma_{n+k} t^k  (all roots real?):")

    def hyperbolic(d, n):
        coeffs = [float(comb(d, k) * gamma[n + k]) for k in range(d + 1)]  # low..high
        scale = max(abs(c) for c in coeffs) or 1.0
        coeffs = [c / scale for c in coeffs]
        roots = np.roots(coeffs[::-1])                # numpy wants high..low
        if len(roots) == 0:
            return True, 0.0
        maximag = max(abs(r.imag) / (abs(r) + 1e-30) for r in roots)
        return maximag < 1e-6, maximag

    all_hyp = True
    for d in (2, 3, 4):
        row = []
        for n in range(0, NMAX - d):
            hyp, mi = hyperbolic(d, n)
            all_hyp = all_hyp and hyp
            row.append("n%d:%s" % (n, "R" if hyp else "C(%.0e)" % mi))
        log("    d=%d : %s" % (d, "  ".join(row)))
    log("  (R = real-rooted/hyperbolic = peaks and zeros interlace; C = complex root present.)")
    log("  All tested Jensen polynomials hyperbolic: %s" % all_hyp)
    log("")

    log("================  WHAT THIS IS  ================")
    log("Amplitude (moments/Hankel) is FREE: Phi>0 makes a_n a moment sequence, automatically.")
    log("The PEAKS (Jensen hyperbolicity / Turan log-concavity) are the RH content -- strictly")
    log("stronger, and exactly 'f and f' interlace' (the derivative hierarchy). Low-degree holds")
    log("unconditionally (CNV d=2, Dimitrov-Lucas d=3); RH = ALL degrees, and Griffin-Ono-Rolen-")
    log("Zagier force each degree d for n large -- the residual is LOW n, i.e. the DOMINANT")
    log("low-lying zeros = the biggest peaks. The de Bruijn-Newman heat flow (kernel Phi) preserves")
    log("the Laguerre-Polya/hyperbolic property; RH is whether it survives to t=0 (Pass-4).")
    log("")
    log("So (a) on the peaks side: RH = forcing Jensen hyperbolicity (the peaks) at every degree,")
    log("with the moment/amplitude floor free and the residual concentrated at the dominant low")
    log("peaks. This is the archimedean object (xi) read through the derivative hierarchy, not the")
    log("zeros -- exactly the reframe: the peaks carry it.")

    from pathlib import Path
    rep = Path(__file__).resolve().parent / "reports" / "jensen_turan_peaks.md"
    header = [
        "# (a) peaks side: Jensen / Turan / Laguerre-Polya for the Riemann xi",
        "",
        "**Script:** `empirical/verify_jensen_turan_peaks.py`",
        "**Context:** the peaks insight; (a) the archimedean forcing structure; ties dBN heat flow + moment work.",
        "**Nature:** numerical (mpmath moments + numpy roots), labelled.",
        "",
        "```text",
    ]
    rep.parent.mkdir(parents=True, exist_ok=True)
    rep.write_text("\n".join(header + out + ["```", ""]), encoding="utf-8")
    print("\n[report -> %s]" % rep)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
