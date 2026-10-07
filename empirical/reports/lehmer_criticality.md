# Forcing the displacement: zero repulsion, Lehmer pairs, and the Lambda=0 knife-edge

**Script:** `empirical/verify_lehmer_criticality.py`
**Context:** attempting the unified open step (P0 Conj 8.5) on the de Bruijn-Newman (t->0) face.
**Finding:** repulsion is the forcing mechanism (= GUE/oscillator); close (Lehmer) pairs prove
Lambda>=0 from below; Lambda<=0 (no actual collision) is RH; Lambda=0 = knife-edge, margin 0.
**Nature:** numerical (mpmath), labelled.  NOT a proof (the upper side IS RH).

```text
Forcing the displacement away: the t->0 face, the repulsion mechanism, and why Lambda=0 is a knife-edge.

The unified open step (P0 sec8.3, Conj 8.5): force the additive/phase object to FORBID a zero's off-axis
displacement.  On the de Bruijn-Newman face this is: the heat-flow Xi_t(z)=int e^{tu^2}Phi cos(uz) du is
real-rooted for t>Lambda; RH = Lambda<=0 (real-rooted down to t=0).  As t DECREASES, a complex pair can
only appear via a COLLISION of two real roots (a real double root) -- "phase leakage."  The mechanism
that RESISTS collision is the zeros' mutual REPULSION: under the heat/Dyson flow the roots obey
x_j' = -2 sum_{k!=j} 1/(x_j - x_k) (repulsive), so real roots push apart; a collision is the repulsion
losing.  This repulsion IS the GUE / Montgomery pair-correlation = the archimedean oscillator (front a):
the SAME object three faces over.

So "force the additive/phase object to forbid the displacement" = "the repulsion never loses, down to t=0"
= Lambda<=0 = RH.  And the marginality is concrete and famous:
  * CLOSE PAIRS (Lehmer pairs) = near-collisions.  A pair of zeros far closer than the mean spacing is a
    pair the backward flow would collide quickly -- so it forces Lambda BOUNDED BELOW (Lehmer; Csordas-
    Smith-Varga): tighter pair => Lambda forced closer to 0 from BELOW.  Rodgers-Tao (2018) closed this:
    Lambda >= 0 unconditionally.  RH = Lambda <= 0.  So Lambda = 0 is the KNIFE-EDGE: close pairs exist
    (forcing Lambda>=0) yet none actually collides at t=0 (RH).  The repulsion wins -- but only just.

This probe makes the criticality concrete: (1) the closest normalized zero-pair in reach (live demo that
near-collisions occur); (2) the famous Lehmer pair near T~7005 (cited) as the extreme; (3) the honest
verdict: the forcing mechanism (repulsion) is real and PROVABLY critical from below (Lambda>=0), but the
upper side (Lambda<=0, "no pair EVER collides") needs the INDIVIDUAL (not statistical) guarantee -- which
is RH.  NOT a proof; the marginality is now a named arithmetic phenomenon.

NUMERICAL (mpmath), labelled.

Computing the first 100 nontrivial zeros (ordinates) ...
  done.

================  PART 1 : the closest normalized zero-pair in reach (a near-collision)  ====
  normalized gap = (gap) x (local density); GUE mean = 1, and P(small) ~ (gap)^2 (repulsion).
  The 4 closest consecutive pairs among the first 100 zeros:
     n     gamma_n        gamma_{n+1}      gap        normalized gap
     34   111.02954   111.87466   0.84512    0.38629
     71   184.87447   185.59878   0.72432    0.38985
     91   220.71492   221.43071   0.71579    0.40544
     97   231.25019   231.98724   0.73705    0.42296
  pairs with normalized gap < 0.6 (notably close): 13 of 99  -- repulsion suppresses but does
  NOT forbid close pairs; each is a near-collision the backward heat flow would tighten.

================  PART 2 : the Lehmer pair near T ~ 7005 (the extreme near-collision)  ======
  (cited; Lehmer 1956) gamma ~ 7005.062866 and 7005.100564, gap ~ 0.0377,
  normalized gap ~ 0.0421  -- about 23.8x tighter than the mean: a celebrated near-collision.
  Such pairs are exactly what gives RIGOROUS LOWER bounds on the de Bruijn-Newman constant
  (Csordas-Smith-Varga 'Lehmer pair' criterion): the tighter the pair, the closer Lambda is
  pushed to 0 FROM BELOW.  The historical chain of Lehmer pairs drove Lambda > -(tiny), and
  Rodgers-Tao (2018) then proved Lambda >= 0 outright.

================  PART 3 : Lambda = 0 is a knife-edge; the forcing, honestly  ================
THE MECHANISM (real): zero repulsion (x_j' = -2 sum 1/(x_j-x_k)) resists collision; it is the
GUE/Montgomery pair-correlation = the archimedean oscillator (front a) -- the SAME object as the
phase clock phi' (front b's count) and the Kubo-Mori curvature current.  Forcing the additive/
phase object to forbid the off-axis displacement = the repulsion never losing, down to t=0.

WHAT IS PROVEN (non-circular): Lambda >= 0 (Rodgers-Tao), driven from below by close (Lehmer)
pairs -- near-collisions that exist and pin Lambda up against 0.  So the displacement is
PERPETUALLY ATTEMPTED (close pairs) and the lower side is settled.
WHAT IS OPEN (= RH): Lambda <= 0 -- that NO pair EVER actually collides at t=0.  The repulsion
is STATISTICALLY sufficient (GUE: P(gap->0) ~ gap^2), but RH needs the INDIVIDUAL guarantee for
every pair at every height -- the same average->individual gap as the Siegel core, the same
'soft bound is the wrong instrument' as the Born/Bures/CRT blindness.  Lambda = 0 is the knife-
edge: the repulsion wins at t=0 (RH) by exactly zero margin (the Weil margin 0 / R(0)~0.9999).

HONEST VERDICT: the forcing mechanism is named and provably critical from one side; the other
side is RH and is NOT crossed.  The marginality is no longer abstract -- it is the existence of
Lehmer pairs (proven near-collisions) against the absence of an actual collision (RH).  The one
missing ingredient remains the individual/integrality guarantee that the statistical repulsion
does not supply: self-adjointness of H = phi'>=0 from arithmetic = Lambda<=0 = L(1,chi) bound.
```
