r"""STRESS-TEST of the subagent's micro-claim "RH <=> rho* < 1" on the Jensen cumulant head.

Setup (matched to verify_jensen_lp.py): Phi = Polya kernel; a_n = int_0^inf t^{2n} Phi dt (moments);
A_n = log a_n; C_n = log(n!/(2n)!) (archimedean Gamma engine); r_k(0) = |Delta^k A_0| / |Delta^k C_0|
(finite differences at the head n=0).  GOR / program frontier: RH <=> sup_{k>=3,n} r_k(n) < 1, and
R(0) := lim_{k->inf} r_k(0) is the dominant corner (the subagent extrapolated R(0) ~ 0.99972 from k<=8).
The subagent further proposed M(d) := 1 - r_d(0), rho* := lim_d M(d)/M(d-1), and claimed "RH <=> rho* < 1".

DOUBT (to test): if R(0) < 1 STRICTLY, then M(d) -> (1 - R(0)) > 0, a POSITIVE constant, so
M(d)/M(d-1) -> 1 necessarily; the rho* < 1 the subagent saw at k<=8 is just the transient while M(d)
is still falling toward its positive floor.  In that case "RH <=> rho* < 1" is INVERTED/ill-posed.
This script computes r_k(0) for k up to 30 at high precision and reads off the TRUE behavior:
  - does r_k(0) converge to a limit R(0), and is R(0) < 1, = 1, or > 1 ?
  - does M(d) -> a positive floor (=> rho* -> 1) or -> 0 ?
  - is rho* a meaningful RH separator, or an artifact ?

NUMERICAL (mpmath dps 60), honest: this CHECKS a subagent claim; it does not prove anything about RH.
"""

import sys
from math import comb
import mpmath as mp

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass
mp.mp.dps = 60

KMAX = 30
NA = KMAX + 3  # need a_0 .. a_KMAX for Delta^KMAX A_0


def Phi(t):
    s = mp.mpf(0)
    for m in range(1, 8):
        m2 = mp.mpf(m) ** 2
        s += (2 * mp.pi ** 2 * m2 ** 2 * mp.e ** (mp.mpf(9) * t / 2)
              - 3 * mp.pi * m2 * mp.e ** (mp.mpf(5) * t / 2)) * mp.e ** (-mp.pi * m2 * mp.e ** (2 * t))
    return s


def moment(n):
    return mp.quad(lambda t: t ** (2 * n) * Phi(t),
                   [0, 0.5, 0.8, 1.0, 1.1, 1.2, 1.3, 1.5, 1.8, 2.2, 2.8, 3.5])


def fd_at0(seq, k):
    # Delta^k applied, first element: sum_{j=0}^k (-1)^{k-j} C(k,j) seq[j]
    return mp.fsum((-1) ** (k - j) * mp.mpf(comb(k, j)) * seq[j] for j in range(k + 1))


def main():
    out = []

    def log(s=""):
        print(s); out.append(s)

    log(__doc__)

    log("Computing %d Phi-moments at dps=%d ..." % (NA, mp.mp.dps))
    a = [moment(n) for n in range(NA)]
    A = [mp.log(x) for x in a]
    C = [mp.loggamma(n + 1) - mp.loggamma(2 * n + 1) for n in range(NA)]
    log("  a_0..a_4 = %s" % ", ".join(mp.nstr(a[i], 6) for i in range(5)))
    # sanity: a_n > 0 (Phi-moments) and strictly log-convex tail expected
    log("  all moments positive: %s" % all(x > 0 for x in a))
    log("")

    log("================  r_k(0) = |Delta^k A_0| / |Delta^k C_0|, k = 2 .. %d  ================" % KMAX)
    log("    k     r_k(0)            M(k)=1-r_k(0)      M(k)/M(k-1)")
    rk = {}
    for k in range(2, KMAX + 1):
        dA = fd_at0(A, k)
        dC = fd_at0(C, k)
        rk[k] = abs(dA) / abs(dC)
    prevM = None
    for k in range(2, KMAX + 1):
        M = 1 - rk[k]
        ratio = "" if prevM is None or prevM == 0 else mp.nstr(M / prevM, 6)
        flag = "  <-- r_k(0) > 1 (criterion VIOLATED at this k)" if rk[k] > 1 else ""
        log("   %3d   %s     %s     %s%s" % (k, mp.nstr(rk[k], 10), mp.nstr(M, 8), ratio, flag))
        prevM = M
    log("")

    # convergence read-off
    tail = [rk[k] for k in range(KMAX - 6, KMAX + 1)]
    incr = [tail[i + 1] - tail[i] for i in range(len(tail) - 1)]
    log("================  READ-OFF  ================")
    log("  last 7 r_k(0): %s" % ", ".join(mp.nstr(v, 8) for v in tail))
    log("  last increments r_{k}(0)-r_{k-1}(0): %s" % ", ".join(mp.nstr(v, 5) for v in incr))
    if all(v > 0 for v in incr):
        trend = "still INCREASING"
    elif all(v < 0 for v in incr):
        trend = "DECREASING"
    else:
        trend = "non-monotone"
    log("  trend of r_k(0) near k=%d: %s" % (KMAX, trend))
    maxr = max(rk.values())
    argmax = max(rk, key=lambda k: rk[k])
    log("  max over k<=%d: r_%d(0) = %s   (%s 1)" % (KMAX, argmax, mp.nstr(maxr, 10), "<" if maxr < 1 else ">="))
    log("")
    log("  VERDICT on the subagent's 'RH <=> rho* < 1':")
    Mlast = [1 - rk[k] for k in range(KMAX - 6, KMAX + 1)]
    Mrat = [Mlast[i + 1] / Mlast[i] for i in range(len(Mlast) - 1) if Mlast[i] != 0]
    log("    M(k)/M(k-1) over the last few k: %s" % ", ".join(mp.nstr(v, 5) for v in Mrat))
    if all(r > 0 for r in Mlast):
        log("    M(k) = 1 - r_k(0) stays POSITIVE; if it tends to a positive floor (1 - R(0)) then")
        log("    M(k)/M(k-1) -> 1 by construction, so 'rho* < 1' is NOT an RH separator -- it is the")
        log("    transient decay of M toward its floor.  The honest invariant remains R(0) <= 1, a VALUE,")
        log("    not a rate.  (If instead r_k(0) crosses 1, RH-on-this-tower would be FALSE at finite k --")
        log("    decisive; watch the flag column above.)")
    else:
        log("    M(k) changed sign (r_k(0) crossed 1) -- see flag column; that would be the decisive event.")

    from pathlib import Path
    rep = Path(__file__).resolve().parent / "reports" / "rh_jensen_rho_star.md"
    header = [
        "# Stress-test of the 'RH <=> rho* < 1' micro-claim on the Jensen cumulant head",
        "",
        "**Script:** `empirical/verify_jensen_rho_star.py`  (extends `verify_jensen_lp.py` from k<=8 to k<=30).",
        "**Purpose:** verify or refute a subagent's proposed rate criterion rho* = lim_d M(d)/M(d-1), M(d)=1-r_d(0).",
        "**Nature:** numerical (mpmath dps 60); checks a claim, proves nothing about RH.",
        "",
        "```text",
    ]
    rep.parent.mkdir(parents=True, exist_ok=True)
    rep.write_text("\n".join(header + out + ["```", ""]), encoding="utf-8")
    print("\n[report -> %s]" % rep)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
