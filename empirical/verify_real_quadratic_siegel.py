r"""Pushing the real-quadratic Siegel core, where Heegner-Stark-Baker (HSB) does NOT reach.

Setup (the GRH hard core for real characters). For a quadratic character chi_D (D a fundamental
discriminant) the gap diagnostic is L(1,chi_D); a Siegel zero is L(1,chi_D) anomalously small.
By the Dirichlet class-number formula:
   IMAGINARY (D<0):  L(1,chi_D) = 2 pi h(D) / (w_D sqrt|D|)      -- controlled by h ALONE.
   REAL      (D>0):  L(1,chi_D) = 2 h(D) R_D / sqrt(D)           -- carries the REGULATOR R_D = log eps_D.

WHY HSB reaches imaginary but not real:
  * Imaginary: small L  <=>  small h.  The tightest case h=1 saturates L ~ 1/sqrt|D|, and the h=1
    fields are PROVABLY FINITE (exactly 9, last D=-163; Heegner-Stark-Baker).  So the tightest
    near-Siegel degeneracies are an explicit finite list.
  * Real: small L  <=>  small h*R.  The regulator R_D (the log of the fundamental unit, from Pell)
    is a WILD CARD -- it ranges from ~(1/2)log D up to ~sqrt(D) -- and DECOUPLES h from L.  Worse,
    h=1 occurs for arbitrarily large D and is CONJECTURALLY INFINITE (Gauss's real class-number
    problem, OPEN).  So there is NO finite list to enumerate: HSB has no analogue here.

This probe computes L(1,chi_D) directly (digamma formula, validated against closed forms) for both
families, exhibits the regulator wild card (Pell, continued-fraction), and shows the decisive
contrast: imaginary smallest-L is pinned and finite; real smallest-L is regulator-controlled and
NOT pinned.  Then the honest residual: what STILL survives for real (Page; Deuring-Heilbronn;
Tatuzawa's EFFECTIVE at-most-one) and what does not (excluding the one exceptional D = Chowla = open).

NUMERICAL/EXACT (mpmath; Kronecker symbol + digamma; CF-Pell), labelled.  NOT a proof of GRH.
"""

import sys
import math
import mpmath as mp

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass
mp.mp.dps = 30


def jacobi(a, n):
    # n odd positive
    a %= n
    r = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                r = -r
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            r = -r
        a %= n
    return r if n == 1 else 0


def kronecker(a, n):
    # (a/n) Kronecker symbol, n >= 1
    if n == 1:
        return 1
    r = 1
    e = 0
    while n % 2 == 0:
        n //= 2; e += 1
    if e:
        if a % 2 == 0:
            return 0
        if e % 2 == 1 and (a % 8) in (3, 5):
            r = -r
    if n == 1:
        return r
    return r * jacobi(a, n)


def squarefree(n):
    n = abs(n)
    if n == 0:
        return False
    i = 2
    while i * i <= n:
        if n % (i * i) == 0:
            return False
        i += 1
    return True


def is_fund_disc(D):
    if D == 0 or D == 1:
        return False
    if D % 4 == 1:
        return squarefree(D)
    if D % 4 == 0:
        m = D // 4
        return (m % 4 in (2, 3)) and squarefree(m)
    return False


def L1(D):
    # L(1, chi_D) = -(1/|D|) sum_{a=1}^{|D|-1} chi_D(a) psi(a/|D|), chi_D(a)=kronecker(D,a)
    q = abs(D)
    s = mp.mpf(0)
    for a in range(1, q):
        c = kronecker(D, a)
        if c:
            s += c * mp.digamma(mp.mpf(a) / q)
    return -s / q


def pell_regulator(D):
    # log of fundamental Pell unit for x^2 - D y^2 = 1 (illustrative regulator), via CF of sqrt(D)
    a0 = math.isqrt(D)
    if a0 * a0 == D:
        return None
    m, dd, a = 0, 1, a0
    num1, num = 1, a0
    den1, den = 0, 1
    steps = 0
    while num * num - D * den * den != 1:
        m = dd * a - m
        dd = (D - m * m) // dd
        a = (a0 + m) // dd
        num1, num = num, a * num + num1
        den1, den = den, a * den + den1
        steps += 1
        if steps > 100000:
            return None
    return mp.log(num + den * mp.sqrt(D))


def main():
    out = []

    def log(s=""):
        print(s); out.append(s)

    log(__doc__)

    log("================  validation (digamma L vs closed forms)  ================")
    phi = (1 + mp.sqrt(5)) / 2
    log("  L(1,chi_{-4}) = %s  vs pi/4 = %s" % (mp.nstr(L1(-4), 10), mp.nstr(mp.pi / 4, 10)))
    log("  L(1,chi_{-3}) = %s  vs pi/3sqrt3 = %s" % (mp.nstr(L1(-3), 10), mp.nstr(mp.pi / (3 * mp.sqrt(3)), 10)))
    log("  L(1,chi_5)   = %s  vs 2log(phi)/sqrt5 = %s" % (mp.nstr(L1(5), 10), mp.nstr(2 * mp.log(phi) / mp.sqrt(5), 10)))
    log("  L(1,chi_8)   = %s  vs 2log(1+sqrt2)/sqrt8 = %s"
        % (mp.nstr(L1(8), 10), mp.nstr(2 * mp.log(1 + mp.sqrt(2)) / mp.sqrt(8), 10)))
    log("")

    # ---- PART 1 : real quadratic -- L(1,chi_D), and the wild regulator ----
    log("================  PART 1 : REAL quadratic L(1,chi_D) and the regulator wild card  ==========")
    reals = [D for D in range(5, 205) if is_fund_disc(D)]
    log("     D     L(1,chi_D)    Pell regulator R_D=log(eps)   L*sqrt(D)/2 = h*R (the 'gap quantum')")
    rmin = (None, mp.inf); rmax = (None, mp.mpf(0)); lmin = (None, mp.inf)
    sample = [5, 8, 12, 13, 24, 29, 44, 56, 61, 76, 89, 124, 136, 173, 197]
    for D in reals:
        L = L1(D); R = pell_regulator(D); hR = L * mp.sqrt(D) / 2
        if R is not None:
            if R < rmin[1]: rmin = (D, R)
            if R > rmax[1]: rmax = (D, R)
        if L < lmin[1]: lmin = (D, L)
        if D in sample:
            log("   %4d   %s     %s          %s"
                % (D, mp.nstr(L, 7), mp.nstr(R, 7) if R is not None else "  -  ", mp.nstr(hR, 6)))
    log("  ...(%d real fundamental discriminants in [5,200] computed)" % len(reals))
    log("  regulator RANGE: min R=%s at D=%d ; max R=%s at D=%d  -- the wild card (orders of magnitude)."
        % (mp.nstr(rmin[1], 5), rmin[0], mp.nstr(rmax[1], 5), rmax[0]))
    log("  smallest L(1,chi_D) in range: %s at D=%d." % (mp.nstr(lmin[1], 6), lmin[0]))
    log("  -> L = 2 h R / sqrt(D): the regulator R decouples h from L.  Large-D fields can have")
    log("     L = O(1) (large unit) OR small L (small unit) -- L does NOT track 1/sqrt(D).")
    log("")

    # ---- PART 2 : imaginary contrast -- L pinned by h, HSB-finite ----
    log("================  PART 2 : IMAGINARY contrast -- L pinned by h, the tightest are FINITE  ====")
    imags = [D for D in range(-200, -2) if is_fund_disc(D)]
    log("  L(1,chi_D) = 2 pi h /(w sqrt|D|): NO regulator; small L <=> small h.  Smallest L in range:")
    ilmin = min(((D, L1(D)) for D in imags), key=lambda t: t[1])
    log("     smallest L(1,chi_D) = %s at D=%d  (= -163 if range reaches it: the h=1 extreme)."
        % (mp.nstr(ilmin[1], 6), ilmin[0]))
    log("  L(1,chi_{-163}) = %s ~ pi/sqrt163 (h=1, the tightest); and the h=1 fields are EXACTLY 9"
        % mp.nstr(L1(-163), 6))
    log("  (D=-3,-4,-7,-8,-11,-19,-43,-67,-163; Heegner-Stark-Baker) -- a FINITE near-Siegel list.")
    log("")

    # ---- PART 3 : what survives for real, and what does not ----
    log("================  PART 3 : the real-quadratic residual, honestly  ================")
    log("WHY HSB DOES NOT REACH REAL: the regulator R_D decouples h from L, and h=1 occurs for")
    log("arbitrarily large D -- conjecturally INFINITELY often (Gauss's real class-number problem,")
    log("OPEN).  There is no finite list of tightest fields to enumerate; the imaginary HSB miracle")
    log("(h=1 finite) has no real-quadratic analogue.")
    log("")
    log("WHAT STILL SURVIVES (the family dividend, effective):")
    log("  * Page/Landau: at most ONE exceptional real character per range (orthogonality = large")
    log("    sieve = whitening).  Applies to real quadratic unchanged.")
    log("  * Deuring-Heilbronn: the one near-degeneracy REPELS all other zeros in the family.")
    log("  * Tatuzawa (1951): Siegel's bound L(1,chi_D) >> D^{-eps} is EFFECTIVE with AT MOST ONE")
    log("    exceptional D.  So even effectively, the real-quadratic Siegel zero is cornered to a")
    log("    SINGLE possible exceptional discriminant.")
    log("")
    log("WHAT DOES NOT (= GRH's hard core): excluding that ONE exceptional D -- i.e. an effective")
    log("L(1,chi_D) >> 1/polylog(D) for ALL real D, equivalently no real-quadratic Siegel zero")
    log("(Chowla's conjecture).  This is OPEN, and it is exactly where the regulator wild card lives:")
    log("the one D where h*R could conspire to be anomalously small, with R uncontrolled.  The family")
    log("structure limits (Page), repels (Deuring-Heilbronn), and effectivizes-to-one (Tatuzawa) --")
    log("but does not exclude the one.  That residual = RH-for-L(s,chi_D) for the lone exceptional D.")
    log("Not crossed; GRH's real-quadratic core is pinned to a single discriminant, with the regulator")
    log("as the precise obstruction HSB cannot touch.")

    from pathlib import Path
    rep = Path(__file__).resolve().parent / "reports" / "real_quadratic_siegel.md"
    header = [
        "# The real-quadratic Siegel core, where Heegner-Stark-Baker does not reach",
        "",
        "**Script:** `empirical/verify_real_quadratic_siegel.py`",
        "**Context:** pushes the GRH hard core for real characters (the regulator wild card).",
        "**Finding:** imaginary L pinned by h (HSB-finite, 9 fields); real L=2hR/sqrt(D) carries the",
        "regulator R (wild card), h=1 conjecturally infinite (Gauss) -- no HSB analogue; survives: Page,",
        "Deuring-Heilbronn, Tatuzawa (effective <=1); residual = the one exceptional D = Chowla = open.",
        "**Nature:** numerical/exact (mpmath; Kronecker+digamma; CF-Pell), validated.  NOT a proof.",
        "",
        "```text",
    ]
    rep.parent.mkdir(parents=True, exist_ok=True)
    rep.write_text("\n".join(header + out + ["```", ""]) + ADDENDUM_2026_10_07, encoding="utf-8")
    print("\n[report -> %s]" % rep)
    return 0



# Re-scope after OpenAI 2026 (family 003); appended to the report on every run.
ADDENDUM_2026_10_07 = '\n## Addendum (2026-10-07): re-scope after the quasi-GRH half-plane (OpenAI 2026)\n\n**Input, tier [A].**  OpenAI, *The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane Re(s) > 7/8*\n(30 Sep 2026, github.com/openai/math, family 003, Thm 1.1).  Every Dirichlet L(s,chi), for every modulus\nand character, has no zero in Re s > 7/8.  The result is model-generated.  OpenAI reports that the\ncore statement is Lean-formalized (lean/docs/003.md).  We have not refereed it.  Everything below rests\non it and is [A], never [P].  The functional equation then gives 1/8 <= beta <= 7/8 for every nontrivial\nzero.  In particular every real character has beta <= 7/8, with no exceptional modulus.\n\n**Effective L(1,chi) (derivation, [A] on 003 + classical).**  The zero-free-rectangle lemma\n(Granville-Soundararajan 2003, GAFA, Lemma 2.2; the Littlewood 1928 argument with 1/2 replaced by\nsigma_0) takes sigma_0 = 7/8, s = 1, sigma_1 = 7/8 + 1/log y.  It gives\n    log L(1,chi) = sum_{n<=y} Lambda(n) chi(n) / (n log n) + O( log q * y^(-1/8) * log^2 y ).\nTake y = (log q)^B with B > 8.  The error is o(1), and\n    |sum_{n<=y} Lambda(n) chi(n)/(n log n)| <= log log y + gamma + o(1) = log log log q + log B + gamma + o(1).\nHence, for every primitive real chi mod q and q >= q_0,\n    c / log log q  <=  L(1,chi)  <=  C log log q,\nwith c and q_0 EFFECTIVE (any c < e^(-gamma)/8 and C > 8 e^gamma for q large).  This is the Littlewood\nshape, with constants weaker than GRH\'s.  It needs no Siegel-zero hypothesis, because 003 excludes\nthat zero for every q at once.\n\n**Consequences, each [A] on 003.**\n- Imaginary quadratic: h(-d) = w sqrt(d) L(1,chi_{-d}) / (2 pi) >> sqrt(d)/log log d, EFFECTIVE.\n  The previous effective record is Goldfeld-Gross-Zagier, h(-d) >> log d.\n- Real quadratic: h(D) log eps_D = sqrt(D) L(1,chi_D) >> sqrt(D)/log log D, EFFECTIVE, no exceptional D.\n  It does NOT separate h(D) from the regulator, and Gauss\'s real class-number questions stay open.\n- PNT in APs: psi(x;q,a) = psi-main + O(x^(7/8) log^2(qx)), EFFECTIVE, uniform for q <= x^(1/8-eps).\n  This replaces the ineffective Siegel-Walfisz range q <= (log x)^A.\n- Linnik: p(q,a) << q^(8+eps) effectively.  This is NO gain: Xylouris\'s L = 5 is already effective.\n- Euler\'s idoneal numbers (Weinberger 1973): the effective h(-4n) lower bound beats the genus count\n  2^(omega(n)-1).  So "the 65 are complete" reduces to an EXPLICIT form of c, q_0 plus a finite search.\n  That explicit bound and search are NOT done here.  Status: reduced to computation, not settled.\n- NOT gained: GRH.  Complex zeros may still lie anywhere in 1/8 <= beta <= 7/8, and nothing here touches\n  Re rho = 1/2.  "No Siegel zero << GRH" remains true and correct.  Only the "OPEN" labels on the\n  Siegel / exceptional-zero items move, from open to [A].\n\n**This report.**  The residual "the one exceptional D = Chowla = open" is re-scoped to **[A], closed on\nOpenAI 2026**.  There is still no finite list to enumerate (no HSB analogue).  That structural point stands.\nBut the analytic residual L(1,chi_D) >> 1/polylog(D) for ALL real D now holds, with 1/log log D in fact.\nThe "regulator wild card" survives only as the open question of splitting hR into h and R.\n'

if __name__ == "__main__":
    raise SystemExit(main())
