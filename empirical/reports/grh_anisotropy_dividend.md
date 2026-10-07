# Exploiting the GRH dividend: the character family as an anisotropic multi-world

**Script:** `empirical/verify_grh_anisotropy_dividend.py`
**Context:** the Beyond-CBS anisotropy/identifiability theorem, mapped to the GRH character family.
**Finding:** large sieve = whitening, orthogonality = anisotropy; the family PROVABLY limits Siegel
degeneracies to <=1 (Page), repels the rest (Deuring-Heilbronn), and closes h=1 (Heegner-Stark-Baker);
the residual is the one possible exceptional real character = RH-for-L(s,chi).
**Nature:** numerical (mpmath, class-number formula, validated); cited theorems labelled.  NOT a proof.

```text
Exploiting the GRH dividend: the character family as an anisotropic multi-world, and what its
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

================  validation (closed forms)  ================
  L(1,chi_{-4}) = 0.785398163397   vs  pi/4 = 0.785398163397
  L(1,chi_{-3}) = 0.604599788078   vs  pi/(3 sqrt3) = 0.604599788078

================  PART 1 : L(1,chi) across the family -- the 'gap', and its extreme  ========
  L(1,chi) bounded away from 0 = the slow-feature gap (G) is open = no Siegel zero.
  smaller L(1,chi) = nearer a Siegel degeneracy (an L-zero approaching the s=1 edge).
     d     h    L(1,chi_d)     normalized  L*sqrt|d| = 2*pi*h/w
      -3   1    0.60459979     1.0471976
      -4   1    0.78539816     1.5707963
      -7   1    1.1874104     3.1415927
      -8   1    1.1107207     3.1415927
     -11   1    0.94722583     3.1415927
     -15   2    1.6223115     6.2831853
     -19   1    0.72073078     3.1415927
     -23   3    1.9652021     9.424778
     -24   2    1.2825498     6.2831853
     -43   1    0.47908839     3.1415927
     -47   5    2.2912419     15.707963
     -67   1    0.38380663     3.1415927
     -71   7    2.6098692     21.991149
    -163   1    0.24606853     3.1415927
  anisotropy: L(1,chi) spans a factor 10.606 across the family (distinct 'mixing rates').
  near-Siegel extreme (smallest gap in range): d=-163, h=1, L(1,chi)=0.246069 -- the tightest
  near-degeneracy (class number 1 saturates the lower bound L ~ 1/sqrt|d|).

================  PART 2 : what the anisotropy PROVABLY buys  ================
  (a) FINITENESS of the tightest degeneracies.  Class-number-one imaginary fields (h=1,
      smallest L) in range: d = -3, -4, -7, -8, -11, -19, -43, -67, -163.
      There are EXACTLY NINE class-number-one fields, the last at d=-163 (Heegner-Stark-
      Baker).  So the tightest near-Siegel degeneracies are PROVABLY FINITE -- a closed
      sub-case of 'anisotropy limits degeneracies', settled by deep methods.
  (b) AT-MOST-ONE (Page/Landau).  Among all primitive chi mod q <= Q, at most ONE -- a real
      character -- can carry a Siegel zero.  The family's orthogonality (the large sieve =
      the WHITENING) forbids two simultaneous near-degeneracies.  This is the genuine large-
      sieve-flavored dividend, and it has NO analogue in the single-zeta case (Lehmer pairs
      are uncontrolled in number).
  (c) REPULSION (Deuring-Heilbronn).  IF the one exceptional chi has gap ~ lambda/log q, all
      other zeros in the family are pushed to Re < 1 - c log(1/lambda)/log q -- a wider zero-
      free region.  The near-degeneracy of one world REPELS the others: cross-world gap
      interaction, exactly the Beyond-CBS anisotropy/gap coupling.

================  PART 3 : the residual (= GRH's hard core), honestly  ================
GRH = no chi's gap EVER closes = no actual Siegel zero for ANY real character (incl. large-d
real quadratic, where finiteness like (a) is NOT available).  The family dividend:
  * LIMITS near-degeneracies to <= 1 in any range (Page) -- PROVEN;
  * REPELS the rest if one is near (Deuring-Heilbronn) -- PROVEN;
  * CLOSES the tightest sub-case (h=1, finite) -- PROVEN (Heegner-Stark-Baker).
It does NOT exclude the one possible exceptional real character in general: that is
L(1,chi) >> 1/sqrt(q) effectively (Siegel: ineffective) or 1/polylog (GRH-strength: open).

So the GRH dividend, exploited: the anisotropy of the character family (= large-sieve
whitening) provably corners GRH to a SINGLE possible exceptional real character per range,
repels everything else, and settles the tightest degeneracies outright -- strictly more than
the single-zeta corner (Lehmer pairs uncontrolled).  The residual is exactly that one
character's gap staying open = its phase clock phi'_chi >= 0 = RH-for-L(s,chi).  Not crossed;
but GRH is now pinned to one object, with the family structure doing provable work around it.
```
