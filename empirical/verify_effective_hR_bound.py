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
    rep.write_text("\n".join(header + out + ["```", ""]), encoding="utf-8")
    print("\n[report -> %s]" % rep)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
