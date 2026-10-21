r"""Exploiting the GRH dividend: the character family as an anisotropic multi-world, and what its
anisotropy PROVABLY buys (Page, Deuring-Heilbronn) versus the one residual (the Siegel zero).

The dictionary (Beyond-CBS  <->  GRH):
  whitening (anti-collapse, E[h_i h_j]=delta_ij)        <->  CHARACTER ORTHOGONALITY / the large sieve
  anisotropy (distinct mixing rates lambda_1^(i))        <->  distinct L-functions in the family mod q
  signed-permutation identifiability (Thm 1)             <->  the chi-twist SELECTS its own L-function
                                                              (verify_multiplicative_carries_zeros: a
                                                              chi-twist moves the von Mangoldt resonance
                                                              onto L(s,chi)'s zeros -- no cross-mixing)
  slow-feature gap (G), recovery well-posed iff gap>0    <->  L(1,chi) bounded away from 0  (the "gap")
  gap (G) closing  ->  recovery ill-posed                <->  L(1,chi) -> 0  =  a SIEGEL zero (near-
                                                              collision of an L-zero with the s=1 edge)
  "anisotropy buys identifiability + a larger gap"       <->  the PROVEN family dividends:
        * Page/Landau: among all chi mod q<=Q, AT MOST ONE has a Siegel zero (>=1 degeneracy forbidden).
        * Deuring-Heilbronn: IF one chi has a near-zero gap, it REPELS all other zeros in the family
          (widens their zero-free regions) -- exactly cross-world gap interaction.
  So the family's anisotropy limits near-degeneracies to AT MOST ONE and repels the rest -- strictly
  MORE than the single-zeta case, where Lehmer near-collisions are uncontrolled in number.

GRH = every chi's phase clock phi'_chi >= 0 = every L(s,chi) has its zeros on the line = no chi's gap
ever closes (no actual Siegel zero, for any real chi).  The family structure proves "at most one
possible failure, and it repels the rest"; EXCLUDING that one is the residual = GRH's hard core.

This probe computes the gap diagnostic L(1,chi) on the cleanest family -- quadratic (real) characters,
the ones a Siegel zero attaches to -- exhibits the anisotropy, locates the near-Siegel extreme, and
shows the proven finiteness of the tightest degeneracies (the 9 class-number-one imaginary fields,
the last at d=-163: Heegner-Stark-Baker), the concrete instance of "anisotropy limits degeneracies."

NUMERICAL/EXACT (mpmath; class-number formula, validated against closed forms), labelled.  NOT a
proof of GRH: the general Siegel zero stays open; this exploits and bounds it, and closes sub-cases.
"""

import sys
import mpmath as mp

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass
mp.mp.dps = 30


def w_units(d):
    return 6 if d == -3 else (4 if d == -4 else 2)


def L1_chi(d, h):
    # imaginary quadratic, fundamental discriminant d<0, class number h:
    #   L(1, chi_d) = 2 pi h / (w_d sqrt|d|)   (Dirichlet class number formula)
    return 2 * mp.pi * h / (w_units(d) * mp.sqrt(-d))


def main():
    out = []

    def log(s=""):
        print(s); out.append(s)

    log(__doc__)

    # (d, h) for imaginary quadratic fundamental discriminants; h = class number (standard tables).
    fam = [(-3, 1), (-4, 1), (-7, 1), (-8, 1), (-11, 1), (-15, 2), (-19, 1), (-23, 3),
           (-24, 2), (-43, 1), (-47, 5), (-67, 1), (-71, 7), (-163, 1)]

    # ---- validation against closed forms ----
    log("================  validation (closed forms)  ================")
    log("  L(1,chi_{-4}) = %s   vs  pi/4 = %s" % (mp.nstr(L1_chi(-4, 1), 12), mp.nstr(mp.pi / 4, 12)))
    log("  L(1,chi_{-3}) = %s   vs  pi/(3 sqrt3) = %s"
        % (mp.nstr(L1_chi(-3, 1), 12), mp.nstr(mp.pi / (3 * mp.sqrt(3)), 12)))
    log("")

    # ---- PART 1 : the family is anisotropic; the gap L(1,chi); the near-Siegel extreme ----
    log("================  PART 1 : L(1,chi) across the family -- the 'gap', and its extreme  ========")
    log("  L(1,chi) bounded away from 0 = the slow-feature gap (G) is open = no Siegel zero.")
    log("  smaller L(1,chi) = nearer a Siegel degeneracy (an L-zero approaching the s=1 edge).")
    log("     d     h    L(1,chi_d)     normalized  L*sqrt|d| = 2*pi*h/w")
    rows = []
    for d, h in fam:
        L = L1_chi(d, h)
        norm = L * mp.sqrt(-d)
        rows.append((d, h, L, norm))
    for d, h, L, norm in rows:
        log("   %5d   %d    %s     %s" % (d, h, mp.nstr(L, 8), mp.nstr(norm, 8)))
    mn = min(rows, key=lambda r: r[2])
    spread = max(r[2] for r in rows) / min(r[2] for r in rows)
    log("  anisotropy: L(1,chi) spans a factor %s across the family (distinct 'mixing rates')."
        % mp.nstr(spread, 5))
    log("  near-Siegel extreme (smallest gap in range): d=%d, h=%d, L(1,chi)=%s -- the tightest"
        % (mn[0], mn[1], mp.nstr(mn[2], 6)))
    log("  near-degeneracy (class number 1 saturates the lower bound L ~ 1/sqrt|d|).")
    log("")

    # ---- PART 2 : the PROVEN family dividends (anisotropy limits + repels degeneracies) ----
    log("================  PART 2 : what the anisotropy PROVABLY buys  ================")
    cn1 = [d for d, h in fam if h == 1]
    log("  (a) FINITENESS of the tightest degeneracies.  Class-number-one imaginary fields (h=1,")
    log("      smallest L) in range: d = %s." % ", ".join(str(d) for d in cn1))
    log("      There are EXACTLY NINE class-number-one fields, the last at d=-163 (Heegner-Stark-")
    log("      Baker).  So the tightest near-Siegel degeneracies are PROVABLY FINITE -- a closed")
    log("      sub-case of 'anisotropy limits degeneracies', settled by deep methods.")
    log("  (b) AT-MOST-ONE (Page/Landau).  Among all primitive chi mod q <= Q, at most ONE -- a real")
    log("      character -- can carry a Siegel zero.  The family's orthogonality (the large sieve =")
    log("      the WHITENING) forbids two simultaneous near-degeneracies.  This is the genuine large-")
    log("      sieve-flavored dividend, and it has NO analogue in the single-zeta case (Lehmer pairs")
    log("      are uncontrolled in number).")
    log("  (c) REPULSION (Deuring-Heilbronn).  IF the one exceptional chi has gap ~ lambda/log q, all")
    log("      other zeros in the family are pushed to Re < 1 - c log(1/lambda)/log q -- a wider zero-")
    log("      free region.  The near-degeneracy of one world REPELS the others: cross-world gap")
    log("      interaction, exactly the Beyond-CBS anisotropy/gap coupling.")
    log("")

    # ---- PART 3 : the residual, honestly ----
    log("================  PART 3 : the residual (= GRH's hard core), honestly  ================")
    log("GRH = no chi's gap EVER closes = no actual Siegel zero for ANY real character (incl. large-d")
    log("real quadratic, where finiteness like (a) is NOT available).  The family dividend:")
    log("  * LIMITS near-degeneracies to <= 1 in any range (Page) -- PROVEN;")
    log("  * REPELS the rest if one is near (Deuring-Heilbronn) -- PROVEN;")
    log("  * CLOSES the tightest sub-case (h=1, finite) -- PROVEN (Heegner-Stark-Baker).")
    log("It does NOT exclude the one possible exceptional real character in general: that is")
    log("L(1,chi) >> 1/sqrt(q) effectively (Siegel: ineffective) or 1/polylog (GRH-strength: open).")
    log("")
    log("So the GRH dividend, exploited: the anisotropy of the character family (= large-sieve")
    log("whitening) provably corners GRH to a SINGLE possible exceptional real character per range,")
    log("repels everything else, and settles the tightest degeneracies outright -- strictly more than")
    log("the single-zeta corner (Lehmer pairs uncontrolled).  The residual is exactly that one")
    log("character's gap staying open = its phase clock phi'_chi >= 0 = RH-for-L(s,chi).  Not crossed;")
    log("but GRH is now pinned to one object, with the family structure doing provable work around it.")

    from pathlib import Path
    rep = Path(__file__).resolve().parent / "reports" / "grh_anisotropy_dividend.md"
    header = [
        "# Exploiting the GRH dividend: the character family as an anisotropic multi-world",
        "",
        "**Script:** `empirical/verify_grh_anisotropy_dividend.py`",
        "**Context:** the Beyond-CBS anisotropy/identifiability theorem, mapped to the GRH character family.",
        "**Finding:** large sieve = whitening, orthogonality = anisotropy; the family PROVABLY limits Siegel",
        "degeneracies to <=1 (Page), repels the rest (Deuring-Heilbronn), and closes h=1 (Heegner-Stark-Baker);",
        "the residual is the one possible exceptional real character = RH-for-L(s,chi).",
        "**Nature:** numerical (mpmath, class-number formula, validated); cited theorems labelled.  NOT a proof.",
        "",
        "```text",
    ]
    rep.parent.mkdir(parents=True, exist_ok=True)
    rep.write_text("\n".join(header + out + ["```", ""]) + ADDENDUM_2026_10_07, encoding="utf-8")
    print("\n[report -> %s]" % rep)
    return 0



# Re-scope after OpenAI 2026 (family 003); appended to the report on every run.
ADDENDUM_2026_10_07 = '\n## Addendum (2026-10-07): re-scope after the quasi-GRH half-plane (OpenAI 2026)\n\n**Input, tier [A].**  OpenAI, *The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane Re(s) > 7/8*\n(30 Sep 2026, github.com/openai/math, family 003, Thm 1.1).  Every Dirichlet L(s,chi), for every modulus\nand character, has no zero in Re s > 7/8.  The result is model-generated.  OpenAI reports that the\ncore statement is Lean-formalized (lean/docs/003.md).  We have not refereed it.  Everything below rests\non it and is [A], never [P].  The functional equation then gives 1/8 <= beta <= 7/8 for every nontrivial\nzero.  In particular every real character has beta <= 7/8, with no exceptional modulus.\n\n**Effective L(1,chi) (derivation, [A] on 003 + classical).**  The zero-free-rectangle lemma\n(Granville-Soundararajan 2003, GAFA, Lemma 2.2; the Littlewood 1928 argument with 1/2 replaced by\nsigma_0) takes sigma_0 = 7/8, s = 1, sigma_1 = 7/8 + 1/log y.  It gives\n    log L(1,chi) = sum_{n<=y} Lambda(n) chi(n) / (n log n) + O( log q * y^(-1/8) * log^2 y ).\nTake y = (log q)^B with B > 8.  The error is o(1), and\n    |sum_{n<=y} Lambda(n) chi(n)/(n log n)| <= log log y + gamma + o(1) = log log log q + log B + gamma + o(1).\nHence, for every primitive real chi mod q and q >= q_0,\n    c / log log q  <=  L(1,chi)  <=  C log log q,\nwith c and q_0 EFFECTIVE (any c < e^(-gamma)/8 and C > 8 e^gamma for q large).  This is the Littlewood\nshape, with constants weaker than GRH\'s.  It needs no Siegel-zero hypothesis, because 003 excludes\nthat zero for every q at once.\n\n**Consequences, each [A] on 003.**\n- Imaginary quadratic: h(-d) = w sqrt(d) L(1,chi_{-d}) / (2 pi) >> sqrt(d)/log log d, EFFECTIVE.\n  The previous effective record is Goldfeld-Gross-Zagier, h(-d) >> log d.\n- Real quadratic: h(D) log eps_D = sqrt(D) L(1,chi_D) >> sqrt(D)/log log D, EFFECTIVE, no exceptional D.\n  It does NOT separate h(D) from the regulator, and Gauss\'s real class-number questions stay open.\n- PNT in APs: psi(x;q,a) = psi-main + O(x^(7/8) log^2(qx)), EFFECTIVE, uniform for q <= x^(1/8-eps).\n  This replaces the ineffective Siegel-Walfisz range q <= (log x)^A.\n- Linnik: p(q,a) << q^(8+eps) effectively.  This is NO gain: Xylouris\'s L = 5 is already effective.\n- Euler\'s idoneal numbers (Weinberger 1973): the effective h(-4n) lower bound beats the genus count\n  2^(omega(n)-1).  So "the 65 are complete" reduces to an EXPLICIT form of c, q_0 plus a finite search.\n  That explicit bound and search are NOT done here.  Status: reduced to computation, not settled.\n- NOT gained: GRH.  Complex zeros may still lie anywhere in 1/8 <= beta <= 7/8, and nothing here touches\n  Re rho = 1/2.  "No Siegel zero << GRH" remains true and correct.  Only the "OPEN" labels on the\n  Siegel / exceptional-zero items move, from open to [A].\n\n**This report.**  "the general Siegel zero stays open" and "1/polylog (GRH-strength: open)" are\nre-scoped to **[A] on OpenAI 2026**.  No real character\'s gap (G) closes, and L(1,chi) >> 1/log log q\nholds effectively.  What the anisotropy argument itself proves (Page, Deuring-Heilbronn, the sub-cases) is\nunchanged.  The phase-clock statement phi\'_chi >= 0 = RH-for-L(s,chi) is NOT touched and remains open.\n'

if __name__ == "__main__":
    raise SystemExit(main())
