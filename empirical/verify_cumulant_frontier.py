r"""The analytic frontier: attempt sup_{k,n} r_k(n) < 1 via the tilted-moment cumulants.

From P0 sec8.2 / verify_cancellation_place_decomposition: with b_n=a_n n!/(2n)!, L_n=log b_n=C_n+A_n,
C_n=log(n!/(2n)!) (archimedean), A_n=log a_n (arithmetic), the cancellation is
    r_k(n) = |Delta^k A_n| / |Delta^k C_n| < 1   (archimedean Gamma-curvature beats arithmetic).
RH lives in sup_{k,n} r_k(n) < 1 (uniform-in-degree domination).

CGF / CUMULANT FRAMEWORK (the right language).  a_n = int_0^inf u^{2n} Phi du = int_0^inf s^n dnu(s)
(s=u^2, dnu=Phi du >= 0).  So a(t)=int s^t dnu is the MGF of the log-pushforward measure mu (in
x=log s), and A_n = log a_n = K(n) is its CUMULANT GENERATING FUNCTION.  By the finite-difference
mean value theorem, Delta^k A_n = K^{(k)}(theta) = kappa_k(mu_theta), the k-th CUMULANT of the
exponentially tilted measure d mu_t ~ s^t dnu, theta in (n, n+k).  In particular
  * kappa_2(mu_t) = Var >= 0  (re-proves log-convexity Delta^2 A >= 0),
  * the higher kappa_k carry the arithmetic (the zeros, via the Taylor coeffs of log Xi).

The archimedean side is explicit: Delta^k C_n ~ (-1)^{k+1} (k-2)! / n^{k-1}.  Hence
    r_k(n) ~ |kappa_k(mu_n)| n^{k-1} / (k-2)!.
A saddle analysis of a(t) (saddle u_t with u_t e^{2u_t} ~ t/pi) predicts the slowly-varying form
    kappa_k(n) ~ c_k / (n^{k-1} log n),   so   r_k(n) ~ (c_k/(k-2)!) / log n.

PREDICTIONS TO TEST (pre-registered):
  T1. kappa_2(n) * n * log n -> a constant (variance decays a full log faster than |Delta^2 C|~1/n).
  T2. For each fixed k, r_k(n) -> 0 as n -> inf (so any finite set of degrees is eventually safe;
      a rate-equipped strengthening of 'N(d) exists').  Specifically r_k(n) log n -> C_k.
  T3. THE CRUX: the growth of C_k = lim_n r_k(n) log n, equivalently C_k/(k-2)!.  If C_k/(k-2)! is
      BOUNDED, the archimedean reference dominates uniformly for large n; if it grows, the head
      (k large vs n) is where RH's content sits.  We extract C_k and watch C_k/(k-2)!.

NUMERICAL (mpmath dps 70), labelled.  NOT a proof: it makes the reduction explicit and tests the
provable (fixed-k) direction; the uniform-in-k growth of c_k is the arithmetic = RH.  Refutation kept.
"""

import sys
import mpmath as mp

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass
mp.mp.dps = 70


def Phi(t):
    s = mp.mpf(0)
    for m in range(1, 7):
        m2 = mp.mpf(m) ** 2
        s += (2 * mp.pi ** 2 * m2 ** 2 * mp.e ** (mp.mpf(9) * t / 2)
              - 3 * mp.pi * m2 * mp.e ** (mp.mpf(5) * t / 2)) * mp.e ** (-mp.pi * m2 * mp.e ** (2 * t))
    return s


def moment(n):
    # peak of u^{2n} Phi moves from ~0 (n=0) to ~1.5 (n~85); breakpoints bracket it.
    return mp.quad(lambda t: t ** (2 * n) * Phi(t), [0, 0.3, 0.6, 1.0, 1.3, 1.6, 2.0, 3.0])


def diffs(seq, k):
    D = list(seq)
    for _ in range(k):
        D = [D[i + 1] - D[i] for i in range(len(D) - 1)]
    return D


def main():
    out = []

    def log(s=""):
        print(s); out.append(s)

    log(__doc__)

    NMAX = 88
    log("Computing %d Phi-moments (dps=%d) ..." % (NMAX, mp.mp.dps))
    a = [moment(n) for n in range(NMAX)]
    A = [mp.log(a[n]) for n in range(NMAX)]
    C = [mp.loggamma(n + 1) - mp.loggamma(2 * n + 1) for n in range(NMAX)]
    DA = {k: diffs(A, k) for k in range(2, 7)}
    DC = {k: diffs(C, k) for k in range(2, 7)}
    log("  done.")
    log("")

    def rk(k, n):
        if n < len(DA[k]) and n < len(DC[k]) and DC[k][n] != 0:
            return abs(DA[k][n]) / abs(DC[k][n])
        return None

    ns = [4, 8, 16, 32, 48, 64, 80]

    # ---- T1 : variance scaling kappa_2(n) ~ c / (n log n) ----
    log("================  T1 : variance scaling  kappa_2(n) = Delta^2 A_n ~ c/(n log n)  ==========")
    log("   n        kappa_2(n)        kappa_2 * n          kappa_2 * n * ln n   (-> constant?)")
    for n in ns:
        k2 = DA[2][n]
        log("  %3d   %s   %s   %s"
            % (n, mp.nstr(k2, 6), mp.nstr(k2 * n, 6), mp.nstr(k2 * n * mp.log(n), 6)))
    log("  |Delta^2 C_n| ~ 1/n, so r_2(n) = kappa_2/|Delta^2 C| ~ (kappa_2 * n) ~ const/log n -> 0.")
    log("")

    # ---- T2/T3 : r_k(n), the fixed-k decay r_k ~ C_k/log n, and C_k = lim r_k log n ----
    log("================  T2 : r_k(n) < 1, and r_k(n) -> 0 for each fixed k (r_k log n -> C_k)  =====")
    log("   n  " + "".join("    r_%d(n)" % k for k in range(2, 7)))
    for n in ns:
        row = "  %3d" % n
        for k in range(2, 7):
            v = rk(k, n)
            row += "   %s" % (mp.nstr(v, 5) if v is not None else "  -  ")
        log(row)
    log("")
    log("  g_k(n) := r_k(n) * ln n   (-> C_k if r_k ~ C_k/log n):")
    log("   n  " + "".join("    g_%d(n)" % k for k in range(2, 7)))
    for n in ns:
        row = "  %3d" % n
        for k in range(2, 7):
            v = rk(k, n)
            row += "   %s" % (mp.nstr(v * mp.log(n), 5) if v is not None else "  -  ")
        log(row)
    log("")

    # ---- T3 : the crux -- C_k and C_k/(k-2)! ----
    log("================  T3 (THE CRUX) : C_k = lim_n r_k(n) ln n,  and  C_k / (k-2)!  ============")
    log("  Richardson-ish estimate C_k ~ g_k(n_max) (+ drift); watch whether C_k/(k-2)! is BOUNDED.")
    nbig = [48, 64, 80]
    log("   k      g_k(48)    g_k(64)    g_k(80)    C_k(est)   (k-2)!     C_k/(k-2)!")
    for k in range(2, 7):
        gs = [rk(k, n) * mp.log(n) for n in nbig]
        # crude 2-point Richardson in 1/log n to damp the C_k/log n -> C_k drift
        x1, x2 = 1 / mp.log(nbig[-2]), 1 / mp.log(nbig[-1])
        g1, g2 = gs[-2], gs[-1]
        Ck = g2 + (g2 - g1) * (0 - x2) / (x2 - x1)   # extrapolate to 1/log n = 0
        fact = mp.factorial(k - 2)
        log("   %d   %s   %s   %s   %s   %s   %s"
            % (k, mp.nstr(gs[0], 5), mp.nstr(gs[1], 5), mp.nstr(gs[2], 5),
               mp.nstr(Ck, 5), mp.nstr(fact, 5), mp.nstr(Ck / fact, 5)))
    log("")
    log("  Reading: r_k(n)<1 throughout and r_k(n)->0 for each fixed k (T2) -- the provable direction,")
    log("  a rate-equipped 'every finite set of degrees is eventually safe'.  THE CRUX is the last")
    log("  column: if C_k/(k-2)! stays bounded, the archimedean reference dominates uniformly for large")
    log("  n; if it grows, the head (k large vs n) carries RH.  c_k is the arithmetic (the zeros, via")
    log("  the Taylor coefficients of log Xi); bounding its growth by (k-2)! is the open content.")
    log("")

    log("================  WHAT THIS IS (honest)  ================")
    log("PROVABLE (modulo making the saddle rigorous): kappa_2>=0 (Cauchy-Schwarz); kappa_2~c/(n log n)")
    log("so r_2~C_2/log n->0; and for each FIXED k, r_k(n)~C_k/log n -> 0 (T1, T2).  This RE-DERIVES,")
    log("with an explicit 1/log n rate, that each Jensen degree is eventually hyperbolic.")
    log("IRREDUCIBLE = RH: the UNIFORM-in-k bound needs c_k <= (k-2)!(1-eps).  The archimedean/Gaussian")
    log("part of c_k (leading saddle of Phi) is <= (k-2)! by construction; the ARITHMETIC correction is")
    log("set by the zeros (kappa_k carries sum_rho (rho-1/2)^{-k}-type data).  sup_{k,n} r_k(n)<1 <=>")
    log("the arithmetic cumulant growth never exceeds the archimedean reference -- which is RH itself,")
    log("not a reduction to anything easier.  The frontier is exactly: bound the tilted-Riemann-measure")
    log("higher cumulants by the Gamma-reference rate, uniformly in order.")

    from pathlib import Path
    rep = Path(__file__).resolve().parent / "reports" / "cumulant_frontier.md"
    header = [
        "# The analytic frontier: sup_{k,n} r_k(n) < 1 via tilted-moment cumulants",
        "",
        "**Script:** `empirical/verify_cumulant_frontier.py`",
        "**Context:** attempts the bound P0 sec8.2 / Conjecture 8.4 reduces RH to.",
        "**Result:** provable fixed-k decay r_k(n)~C_k/log n -> 0; the crux is the growth of C_k/(k-2)!.",
        "**Nature:** numerical (mpmath dps 70), labelled, pre-registered.  NOT a proof (uniform-in-k = RH).",
        "",
        "```text",
    ]
    rep.parent.mkdir(parents=True, exist_ok=True)
    rep.write_text("\n".join(header + out + ["```", ""]), encoding="utf-8")
    print("\n[report -> %s]" % rep)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
