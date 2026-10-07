r"""Attempting the arithmetic clock: build phi'(x) >= 0 from the primes, and pin the exact obstruction.

This IS RH (phi' >= 0 <=> the de Branges phase clock is monotone <=> self-adjointness of H = N_inf +
V_arith).  We do NOT fabricate a proof.  We (1) write the clock's explicit-formula decomposition into
an archimedean drift + an arithmetic (von Mangoldt) fluctuation, (2) exhibit the precise obstruction --
the prime sum converges only OFF the critical line; on it, its continuation IS the zeros (circular),
(3) record the ONE genuinely non-circular partial positivity available (de Bruijn-Newman / Rodgers-Tao:
the heat-flowed clock is provably monotone for t > Lambda >= 0), so RH = the t->0 closure, and (4) show
the drift and the fluctuation are the SAME ORDER (~log T) -- the analytic face of RH's marginality.

The clock's log-derivative is m = -xi'/xi, and exactly (Re s > 1):
   -xi'/xi(s) = [ -1/s - 1/(s-1) + (1/2)log(pi) - (1/2)psi(s/2) ]  +  [ sum_n Lambda(n) n^{-s} ],
                \________________ archimedean (Gamma) drift ________/    \___ arithmetic (primes) ___/
the arithmetic part being -zeta'/zeta(s) = sum Lambda(n) n^{-s}.  On s = 1/2 + i z this is the von
Mangoldt sum sum Lambda(n) n^{-1/2 - i z} (the multiplicative basis that CARRIES the zeros).

NUMERICAL/EXACT (mpmath), labelled.  NOT a proof.
"""

import sys
import mpmath as mp

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass
mp.mp.dps = 25


def xi(s):
    return mp.mpf(1) / 2 * s * (s - 1) * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)


def mangoldt_upto(N):
    Lam = [mp.mpf(0)] * (N + 1)
    sieve = list(range(N + 1))
    for p in range(2, N + 1):
        if sieve[p] == p:  # p prime
            pk = p
            while pk <= N:
                Lam[pk] = mp.log(p)
                pk *= p
            for m in range(2 * p, N + 1, p):
                if sieve[m] == m:
                    sieve[m] = p
    return Lam


def main():
    out = []

    def log(s=""):
        print(s); out.append(s)

    log(__doc__)

    # ---- PART 1 : the clock = archimedean drift + arithmetic (von Mangoldt) fluctuation ----
    log("================  PART 1 : explicit-formula decomposition of the clock (at s=2, Re>1)  ======")
    s = mp.mpf(2)
    direct = -mp.diff(xi, s) / xi(s)
    arch = -1 / s - 1 / (s - 1) + mp.log(mp.pi) / 2 - mp.psi(0, s / 2) / 2
    arith_exact = -mp.zeta(s, derivative=1) / mp.zeta(s)      # = -zeta'/zeta(2), the prime part (exact)
    log("  -xi'/xi(2)  (direct)                 = %s" % mp.nstr(direct, 16))
    log("  archimedean(2) + (-zeta'/zeta(2))    = %s" % mp.nstr(arch + arith_exact, 16))
    log("    archimedean (Gamma) drift          = %s" % mp.nstr(arch, 12))
    log("    arithmetic (primes) -zeta'/zeta(2) = %s" % mp.nstr(arith_exact, 12))
    log("  identity match to %s   -> the clock is EXACTLY arch drift + prime part (Lambda(n) >= 0)."
        % mp.nstr(abs(direct - (arch + arith_exact)), 3))
    Lam = mangoldt_upto(20000)
    log("  prime interpretation: sum_{n<=N} Lambda(n)/n^2 converges to -zeta'/zeta(2) (slow ~(logN)/N tail):")
    for N in (100, 2000, 20000):
        ps = mp.fsum(Lam[n] * mp.mpf(n) ** (-s) for n in range(2, N + 1))
        log("     N=%6d : %s   (gap to limit = %s)" % (N, mp.nstr(ps, 10), mp.nstr(arith_exact - ps, 3)))
    log("")

    # ---- PART 2 : the obstruction -- primes converge OFF the line; ON it the continuation = zeros ----
    log("================  PART 2 : the convergence boundary (why it is not direct)  ================")
    log("  sum_{n<=N} Lambda(n) n^{-s} partial sums:")
    for sval, tag in [(mp.mpf(2), "Re s=2 (>1: converges)"), (mp.mpf("1.2"), "Re s=1.2 (slow)")]:
        ps = []
        for N in (100, 1000, 10000):
            ps.append(mp.fsum(Lam[n] * mp.mpf(n) ** (-sval) for n in range(2, N + 1)))
        lim = -mp.diff(mp.zeta, sval) / mp.zeta(sval)
        log("    %-24s N=100:%s  N=1e3:%s  N=1e4:%s   (-zeta'/zeta=%s)"
            % (tag, mp.nstr(ps[0], 7), mp.nstr(ps[1], 7), mp.nstr(ps[2], 7), mp.nstr(lim, 7)))
    log("  ON the line (Re s = 1/2) the prime sum DIVERGES; its continuation -zeta'/zeta(1/2+iT) has")
    log("  POLES at the zeros (residue = multiplicity).  |zeta'/zeta(1/2+iT)| near gamma_1=14.1347:")
    for T in [mp.mpf(t) for t in ["13.5", "14.0", "14.10", "14.134"]]:
        s2 = mp.mpf(1) / 2 + 1j * T
        val = abs(mp.zeta(s2, derivative=1) / mp.zeta(s2))
        log("     T=%6s   |zeta'/zeta| = %s" % (mp.nstr(T, 6), mp.nstr(val, 8)))
    log("  -> the convergent (non-circular) prime data lives at Re s>1; on the line it becomes the")
    log("     zeros themselves.  Transferring the prime positivity (Lambda>=0) ACROSS the strip to the")
    log("     line is exactly the open step -- it cannot be done by the prime sum alone.")
    log("")

    # ---- PART 3 : drift vs fluctuation -- the same order (RH's marginality, analytic face) ----
    log("================  PART 3 : archimedean drift vs arithmetic fluctuation -- SAME ORDER  =======")
    log("  drift density d(T)=(1/2)log(T/2pi)  vs  fluctuation S(T)=(1/pi)arg zeta(1/2+iT)  (both ~log T)")
    log("      T        d(T)=(1/2)log(T/2pi)     S(T)        log T")
    for T in [30, 100, 500, 1000, 5000]:
        d = mp.log(mp.mpf(T) / (2 * mp.pi)) / 2
        S = mp.nzeros(T) - mp.siegeltheta(T) / mp.pi - 1
        log("   %5d        %s          %s     %s"
            % (T, mp.nstr(d, 7), mp.nstr(S, 5), mp.nstr(mp.log(T), 6)))
    log("  -> drift density d(T)=(1/2)log(T/2pi) and the unconditional bound |S(T)| <= c log T are BOTH")
    log("     Theta(log T) -- the same order.  S(T) is small here (zeros track the smooth count), but the")
    log("     worst-case excursion PERMITTED is the size of the drift itself, so no soft bound forces")
    log("     phi' >= 0; RH is exactly that the actual excursion never reverses the drift.  (Same")
    log("     marginality as R(0)~0.9999, Weil margin 0, Lambda=0.)")
    log("")

    # ---- PART 4 : the one genuinely non-circular partial positivity, and what is open ----
    log("================  PART 4 : the non-circular partial result, and the exact open step  ========")
    log("GENUINELY NON-CIRCULAR (de Bruijn 1950 + Rodgers-Tao 2018): the heat-flowed Xi_t(z) =")
    log("int e^{t u^2} Phi(u) cos(uz) du is REAL-ROOTED for t > Lambda, with Lambda >= 0 PROVEN")
    log("unconditionally.  So for t > Lambda the heat-flowed clock phi'_t >= 0 PROVABLY -- a monotone")
    log("arithmetic clock EXISTS after enough smoothing, with no circular use of RH.  RH = Lambda <= 0")
    log("= pushing t -> 0^+ in the Born cone (program: RH-Pass4/5).  And Lambda = 0 exactly = RH 'barely")
    log("true' -- the same marginality, now as the heat constant sitting at the boundary.")
    log("")
    log("THE EXACT OPEN STEP (three faces, one thing):")
    log("  (i)  self-adjointness of H = N_inf + V_arith in the Kubo-Mori geometry;")
    log("  (ii) the archimedean local positivity (Connes trace term >= 0), the analogue of the Hodge")
    log("       index over a curve;")
    log("  (iii) Lambda <= 0, i.e. the heat flow reaches t=0 without leaving the Born cone.")
    log("All three = phi'(x) >= 0 from the arithmetic, non-circularly = RH.  The prime positivity")
    log("Lambda(n) >= 0 gives the half-plane Re s > 1 (the EASY half); FE reflects to Re s < 0; the open")
    log("content is the strip-crossing to Re s = 1/2.  NOT crossed.  But the clock is now explicit, its")
    log("decomposition is arch-drift + prime-fluctuation, it is PROVABLY monotone after heat-smoothing")
    log("(t > Lambda >= 0), and the gap is the single, sharply-named t -> 0 / strip-crossing closure.")

    from pathlib import Path
    rep = Path(__file__).resolve().parent / "reports" / "arithmetic_clock.md"
    header = [
        "# Attempting the arithmetic clock phi'(x) >= 0 from the primes (= RH); the exact obstruction",
        "",
        "**Script:** `empirical/verify_arithmetic_clock.py`",
        "**Context:** the irreducible step -- construct the de Branges clock from arithmetic, non-circularly.",
        "**Finding:** clock = archimedean Gamma-drift + von Mangoldt prime-fluctuation; primes converge only",
        "off the line (on it the continuation = the zeros); drift ~ fluctuation ~ log T (marginal); the clock",
        "is PROVABLY monotone after heat-smoothing (t>Lambda>=0, Rodgers-Tao); RH = the t->0 / strip-crossing.",
        "**Nature:** numerical/exact (mpmath), labelled.  NOT a proof (this step IS RH).",
        "",
        "```text",
    ]
    rep.parent.mkdir(parents=True, exist_ok=True)
    rep.write_text("\n".join(header + out + ["```", ""]), encoding="utf-8")
    print("\n[report -> %s]" % rep)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
