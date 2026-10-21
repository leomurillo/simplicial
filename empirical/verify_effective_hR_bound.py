r"""Effective lower bounds on hR (= the real-quadratic Siegel problem): the honest, layered state.

GOAL asked: an effective lower bound on h(D)*R(D) for real quadratic D, where R=log eps_D is the
regulator.  Since L(1,chi_D) = 2 h R / sqrt(D), this is an effective lower bound on L(1,chi_D).
A *no-exception* such bound (L >> 1/polylog for ALL real D) is equivalent to no real-quadratic
Siegel zero = Chowla's conjecture = OPEN.  This certificate lays out the THREE layers honestly.

LAYER 1 -- ELEMENTARY, holds for ALL D, but WEAK.  The fundamental unit satisfies eps_D >= (1+sqrt D)/2
  (sharp at D=5, the golden ratio), so R_D >= log((1+sqrt D)/2) ~ (1/2)log D, and with h>=1:
        h R >= log((1+sqrt D)/2),   i.e.   L(1,chi_D) >= 2 log((1+sqrt D)/2)/sqrt(D) ~ (log D)/sqrt(D).
  Effective, unconditional, for every D -- but it -> 0, far weaker than the GRH-strength target.

LAYER 2 -- TATUZAWA (1951), holds for ALL BUT <=1 D, and is STRONG.  Siegel's L(1,chi_D) >>_eps D^{-eps}
  is made EFFECTIVE with at most one exceptional discriminant.  This is the genuine effective bound on
  hR (>> D^{1/2-eps}) -- the family/anisotropy (large-sieve = whitening) dividend delivering an
  effective Siegel for all but one D.

LAYER 3 -- THE ONE EXCEPTIONAL D (no-exception bound) -- OPEN.  Excluding the single possible exceptional
  discriminant = a no-exception effective L >> 1/polylog = no real Siegel zero (Chowla).  The imaginary
  analogue was cracked (Goldfeld 1976 + Gross-Zagier 1986: h(-D) >> (log D)^{1-eps}, effective, via an
  L-function with a triple central zero / a Heegner-point height); that mechanism is IMAGINARY-specific
  and has NO real-quadratic analogue.  This layer is the open core.

This probe VERIFIES Layer 1 (the elementary bound, sharp at D=5), measures the gap to the GRH target,
confirms no near-Siegel discriminant in range, and states Layers 2-3 with their status.  NOT a proof
of Layer 3; that is Chowla/Siegel.

NUMERICAL/EXACT (mpmath; Kronecker + digamma), labelled.
"""

import sys
import mpmath as mp

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass
mp.mp.dps = 30


def jacobi(a, n):
    a %= n; r = 1
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
    if n == 1:
        return 1
    r = 1; e = 0
    while n % 2 == 0:
        n //= 2; e += 1
    if e:
        if a % 2 == 0:
            return 0
        if e % 2 == 1 and (a % 8) in (3, 5):
            r = -r
    return r if n == 1 else r * jacobi(a, n)


def squarefree(n):
    n = abs(n)
    i = 2
    while i * i <= n:
        if n % (i * i) == 0:
            return False
        i += 1
    return n > 0


def is_fund_disc(D):
    if D in (0, 1):
        return False
    if D % 4 == 1:
        return squarefree(D)
    if D % 4 == 0:
        m = D // 4
        return (m % 4 in (2, 3)) and squarefree(m)
    return False


def L1(D):
    q = abs(D); s = mp.mpf(0)
    for a in range(1, q):
        c = kronecker(D, a)
        if c:
            s += c * mp.digamma(mp.mpf(a) / q)
    return -s / q


def main():
    out = []

    def log(s=""):
        print(s); out.append(s)

    log(__doc__)

    reals = [D for D in range(5, 1001) if is_fund_disc(D)]

    # ---- LAYER 1 : the elementary effective bound, verified + sharpness ----
    log("================  LAYER 1 : hR >= log((1+sqrt D)/2)  (elementary, ALL D, weak)  ============")
    log("  hR = L(1,chi_D) sqrt(D)/2  (computed from L); bound B(D)=log((1+sqrt D)/2) (from eps_D>=(1+sqrtD)/2).")
    holds = True
    minratio = (None, mp.inf)
    minL = (None, mp.inf)
    for D in reals:
        L = L1(D)
        hR = L * mp.sqrt(D) / 2
        B = mp.log((1 + mp.sqrt(D)) / 2)
        ratio = hR / B
        if hR < B - mp.mpf(10) ** -12:
            holds = False
        if ratio < minratio[1]:
            minratio = (D, ratio)
        if L < minL[1]:
            minL = (D, L)
    log("  hR >= B(D) for ALL %d real fundamental discriminants in [5,1000]: %s" % (len(reals), holds))
    log("  tightest (min hR/B): ratio %s at D=%d  (=1 exactly at D=5: hR=B=log(golden ratio))"
        % (mp.nstr(minratio[1], 6), minratio[0]))
    log("  smallest L(1,chi_D) in range: %s at D=%d (no near-Siegel: bounded well away from 0)."
        % (mp.nstr(minL[1], 6), minL[0]))
    log("  => unconditional effective bound, ALL D:  L(1,chi_D) >= 2 log((1+sqrtD)/2)/sqrt(D) ~ (log D)/sqrt(D).")
    log("")

    # ---- the gap to the GRH-strength target ----
    log("================  THE GAP : effective (Layer 1) vs GRH-strength target  ================")
    log("  GRH-strength target (no Siegel zero): L(1,chi_D) >> 1/log D.  Compare the two at sample D:")
    log("     D        L (actual)     Layer-1 bound 2B/sqrtD     target ~1/log D     gap factor sqrtD/(logD)^2")
    for D in [5, 101, 1000, 10 ** 4, 10 ** 6, 10 ** 9]:
        Bb = 2 * mp.log((1 + mp.sqrt(D)) / 2) / mp.sqrt(D)
        tgt = 1 / mp.log(D)
        gap = mp.sqrt(D) / mp.log(D) ** 2
        actual = mp.nstr(L1(D), 6) if D <= 1000 and is_fund_disc(D) else "(—)"
        log("   %9d   %s        %s              %s            %s"
            % (D, actual, mp.nstr(Bb, 4), mp.nstr(tgt, 4), mp.nstr(gap, 5)))
    log("  the Layer-1 bound is weaker than the target by a factor ~ sqrt(D)/(log D)^2 -> infinity:")
    log("  the elementary regulator bound is SHARP (saturated at D=5) and cannot be improved")
    log("  elementarily; closing the gap needs analytic control of h (or the product) -- Layers 2-3.")
    log("")

    # ---- Layers 2-3 : the real effective result, and the open core ----
    log("================  LAYER 2 (Tatuzawa) and LAYER 3 (the open core)  ================")
    log("LAYER 2 -- EFFECTIVE for ALL BUT <=1 D (Tatuzawa 1951): hR >>_eps D^{1/2-eps}, effective,")
    log("  with at most one exceptional discriminant.  This is the genuine effective lower bound on hR;")
    log("  it is the family/large-sieve (= whitening) dividend made effective.  So an effective bound")
    log("  DOES exist -- up to a single possible exception per range.")
    log("")
    log("LAYER 3 -- THE ONE EXCEPTIONAL D (no-exception bound) -- OPEN = Chowla/Siegel.  Excluding that")
    log("  one discriminant is a no-exception effective L >> 1/polylog = no real-quadratic Siegel zero.")
    log("  The imaginary analogue (Gauss class-number problem) WAS solved effectively (Goldfeld +")
    log("  Gross-Zagier: a triple central zero / Heegner-point height gives h(-D) >> (log D)^{1-eps});")
    log("  that construction is IMAGINARY-specific (central L-value of a weight-2 form; Heegner points")
    log("  on X_0(N)) and has NO real-quadratic analogue.  This is exactly where the regulator wild card")
    log("  lives: the one D where h*R could conspire small, with R uncontrolled.")
    log("")
    log("================  HONEST VERDICT  ================")
    log("An effective lower bound on hR EXISTS for all but at most one real discriminant (Tatuzawa,")
    log(">> D^{1/2-eps}); the unconditional all-D bound is elementary and sharp (hR >= log((1+sqrtD)/2),")
    log("L >> (log D)/sqrt D) and provably too weak by ~sqrt(D)/(log D)^2.  A NO-EXCEPTION effective")
    log("bound -- closing the single exceptional discriminant -- IS the real-quadratic Siegel/Chowla")
    log("problem, OPEN, with the imaginary-only Goldfeld-Gross-Zagier mechanism not transferring.")
    log("I do not solve Layer 3; the regulator is the named obstruction, and fabricating a bound there")
    log("would be the fluent-but-false failure the discipline forbids.  GRH's real-quadratic core is")
    log("pinned to that one discriminant; Layers 1-2 are the honest, real effective state around it.")

    from pathlib import Path
    rep = Path(__file__).resolve().parent / "reports" / "effective_hR_bound.md"
    header = [
        "# Effective lower bounds on hR for real quadratic fields: the honest layered state",
        "",
        "**Script:** `empirical/verify_effective_hR_bound.py`",
        "**Context:** the asked 'effective lower bound on hR' = the real-quadratic Siegel/Chowla problem.",
        "**Result:** Layer 1 elementary (all D, hR>=log((1+sqrtD)/2), sharp at D=5, too weak by sqrtD/(logD)^2);",
        "Layer 2 Tatuzawa (effective for all but <=1 D, >>D^{1/2-eps}); Layer 3 (the one exceptional D) = OPEN",
        "(Chowla; Goldfeld-Gross-Zagier is imaginary-only).  NOT a proof of Layer 3.",
        "",
        "```text",
    ]
    rep.parent.mkdir(parents=True, exist_ok=True)
    rep.write_text("\n".join(header + out + ["```", ""]) + ADDENDUM_2026_10_07, encoding="utf-8")
    print("\n[report -> %s]" % rep)
    return 0



# Re-scope after OpenAI 2026 (family 003); appended to the report on every run.
ADDENDUM_2026_10_07 = '\n## Addendum (2026-10-07): re-scope after the quasi-GRH half-plane (OpenAI 2026)\n\n**Input, tier [A].**  OpenAI, *The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane Re(s) > 7/8*\n(30 Sep 2026, github.com/openai/math, family 003, Thm 1.1).  Every Dirichlet L(s,chi), for every modulus\nand character, has no zero in Re s > 7/8.  The result is model-generated.  OpenAI reports that the\ncore statement is Lean-formalized (lean/docs/003.md).  We have not refereed it.  Everything below rests\non it and is [A], never [P].  The functional equation then gives 1/8 <= beta <= 7/8 for every nontrivial\nzero.  In particular every real character has beta <= 7/8, with no exceptional modulus.\n\n**Effective L(1,chi) (derivation, [A] on 003 + classical).**  The zero-free-rectangle lemma\n(Granville-Soundararajan 2003, GAFA, Lemma 2.2; the Littlewood 1928 argument with 1/2 replaced by\nsigma_0) takes sigma_0 = 7/8, s = 1, sigma_1 = 7/8 + 1/log y.  It gives\n    log L(1,chi) = sum_{n<=y} Lambda(n) chi(n) / (n log n) + O( log q * y^(-1/8) * log^2 y ).\nTake y = (log q)^B with B > 8.  The error is o(1), and\n    |sum_{n<=y} Lambda(n) chi(n)/(n log n)| <= log log y + gamma + o(1) = log log log q + log B + gamma + o(1).\nHence, for every primitive real chi mod q and q >= q_0,\n    c / log log q  <=  L(1,chi)  <=  C log log q,\nwith c and q_0 EFFECTIVE (any c < e^(-gamma)/8 and C > 8 e^gamma for q large).  This is the Littlewood\nshape, with constants weaker than GRH\'s.  It needs no Siegel-zero hypothesis, because 003 excludes\nthat zero for every q at once.\n\n**Consequences, each [A] on 003.**\n- Imaginary quadratic: h(-d) = w sqrt(d) L(1,chi_{-d}) / (2 pi) >> sqrt(d)/log log d, EFFECTIVE.\n  The previous effective record is Goldfeld-Gross-Zagier, h(-d) >> log d.\n- Real quadratic: h(D) log eps_D = sqrt(D) L(1,chi_D) >> sqrt(D)/log log D, EFFECTIVE, no exceptional D.\n  It does NOT separate h(D) from the regulator, and Gauss\'s real class-number questions stay open.\n- PNT in APs: psi(x;q,a) = psi-main + O(x^(7/8) log^2(qx)), EFFECTIVE, uniform for q <= x^(1/8-eps).\n  This replaces the ineffective Siegel-Walfisz range q <= (log x)^A.\n- Linnik: p(q,a) << q^(8+eps) effectively.  This is NO gain: Xylouris\'s L = 5 is already effective.\n- Euler\'s idoneal numbers (Weinberger 1973): the effective h(-4n) lower bound beats the genus count\n  2^(omega(n)-1).  So "the 65 are complete" reduces to an EXPLICIT form of c, q_0 plus a finite search.\n  That explicit bound and search are NOT done here.  Status: reduced to computation, not settled.\n- NOT gained: GRH.  Complex zeros may still lie anywhere in 1/8 <= beta <= 7/8, and nothing here touches\n  Re rho = 1/2.  "No Siegel zero << GRH" remains true and correct.  Only the "OPEN" labels on the\n  Siegel / exceptional-zero items move, from open to [A].\n\n**This report.**  LAYER 3 ("the one exceptional D = Chowla = OPEN") is re-scoped to **[A], closed on\nOpenAI 2026**.  The effective bound h(D) log eps_D >> sqrt(D)/log log D now holds for EVERY D, with no\nTatuzawa exception.  Layers 1-2 are unchanged and still correct.  The remark that Goldfeld-Gross-Zagier is\nimaginary-only stays true.  The closure comes from a zero-free half-plane, not from any regulator mechanism.\n'

if __name__ == "__main__":
    raise SystemExit(main())
