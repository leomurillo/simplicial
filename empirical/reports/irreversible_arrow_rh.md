# The irreversible blind spot, transported to RH: the off-line zero is an ARROW

**Script:** `empirical/verify_irreversible_arrow_rh.py`  (uses IrreversibleBlindSpot.md insights).
**Finding:** front (a)'s statistical->individual gap is blind on TWO orthogonal axes -- cumulant
(2nd-order, the moment thermometer) AND reversibility (symmetric, the arrow). The off-line
displacement is the ANTISYMMETRIC arrow, in the kernel of every symmetric/quadratic form by parity
(Lemma 1) -- NOT a rare event. The de Branges arrow-numerator Xi'^2-XiXi'' carries the sign (phi');
the Bures magnitude |E_B|^2>0 is sign-blind (= the Kubo-Mori/Bures fork, T24, named). RH <=> phi'>=0
<=> irreversibility gap Delta=0 <=> detailed balance. The lift is the asymmetric predictor/phase object.
**Nature:** numerical (numpy operator toy + mpmath de Branges) + structural transport. NO claim RH proved.

```text
The IRREVERSIBLE blind spot, transported to RH: the off-line displacement is an ARROW, and every
SYMMETRIC instrument has it in its kernel by parity.  (Third reading of front (a).)

The Irreversible Blind Spot (sibling paper) proves: the single-encoder/SYMMETRIC objective is a
functional of the symmetric part S=(T+T*)/2 ALONE; the antisymmetric part A=(T-T*)/2 -- the probability
CURRENT, the arrow of time -- is in the KERNEL of every real quadratic form (Lemma 1: <h,Ah>=0). The
PREDICTOR (asymmetric, two-encoder) probes <f,Tg> with f!=g, recovers the SVD, and reads A. The
irreversibility gap Delta = sum sigma_i(T) - sum lambda_i(S) >= 0 measures it; =0 iff detailed balance.

RH READING (the unification this script makes concrete):
  * The de Branges clock: E_B = Xi + i Xi', phase phi = -arg E_B, phi(T)/pi = N(T), and
        phi'(t) = (Xi'^2 - Xi Xi'') / (Xi^2 + Xi'^2),     RH <=> phi'(t) >= 0 for all t.
  * The NUMERATOR  Xi'^2 - Xi Xi''  is the ADDITIVE/Kubo-Mori "arrow" object: its SIGN is the arrow
    (phi increasing = forward). A zero leaving the critical line is exactly phi' changing sign
    (de Bruijn-Newman / Lehmer): the arrow REVERSES.
  * The DENOMINATOR  Xi^2 + Xi'^2 = |E_B|^2  is the BURES (quadratic, symmetric) magnitude. It is
    ALWAYS > 0 -- so it is SIGN-BLIND: it cannot see whether phi' > 0 or < 0. The Bures magnitude is
    the arrow-blind symmetric instrument; the phase phi' is the predictor that carries the arrow. This
    IS the program's Kubo-Mori-vs-Bures fork (T24), now NAMED by the irreversibility axis.
  * So front (a)'s "symmetric/averaged statistics (2nd moment, pair correlation, Bures) are blind to
    the off-line zero" is not "averages miss rare events" -- it is the EXACT parity fact: the off-line
    displacement is the ANTISYMMETRIC (arrow) content, in the kernel of every symmetric form. Lifting
    it needs an ASYMMETRIC instrument: the phase clock phi' / m_B = -Xi'/Xi / the predictor.
  * RH  <=>  phi' >= 0 (no arrow reversal)  <=>  Delta = 0 (detailed balance)  <=>  every zero is fixed
    by the reflection about the critical line (on the line), no antisymmetric displacement.

This probe: (A) operator-level -- a toy reversible vs irreversible operator: S has REAL spectrum (a
"line of zeros"), adding A pushes it OFF (complex), the symmetric form <h,Th>=<h,Sh> is blind, the
predictor/SVD sees A, and Delta>0 iff off-line; (B) the RH instance -- compute Xi, Xi', Xi'' and the
arrow-numerator vs Bures-denominator near the first zeros, show phi' carries the sign (arrow) the Bures
magnitude discards; (C) synthesis + honest residual.  NUMERICAL; NO claim RH is proved.

================  PART A: on-line = reversible (real spectrum); off-line = the arrow (A!=0)  ===
  detailed balance q=b  : max|Im eig(T)|=0.0000 (ON line) ; <h,Th>-<h,Sh> max=0.0e+00 (BLIND) ; Delta(top-3)=-0.0000 ; |A|=0.0000
  drift q>b (arrow)     : max|Im eig(T)|=0.4000 (OFF line: arrow!) ; <h,Th>-<h,Sh> max=3.6e-15 (BLIND) ; Delta(top-3)=0.0430 ; |A|=0.9798
  => detailed balance (q=b): spectrum REAL = 'zeros on the line', A=0, Delta=0 -- no arrow.
     drift (q!=b): spectrum COMPLEX = 'zeros off the line', the symmetric form is BLIND to it
     (<h,Th>=<h,Sh> to 1e-15); only the predictor/SVD (Delta>0) sees the arrow. Delta=0 switches
     the blind spot OFF exactly at detailed balance -- the operator-level RH<=>no-arrow picture.

================  PART B: RH -- phi' numerator (arrow) vs Bures denominator (sign-blind)  =====
  Xi(t)=xi(1/2+it) is real; E_B=Xi+iXi'; phi'(t)=(Xi'^2 - Xi Xi'')/(Xi^2+Xi'^2).
  arrow numerator N(t)=Xi'^2 - Xi Xi''  (additive/Kubo-Mori; its SIGN = the arrow);
  Bures denominator D(t)=Xi^2 + Xi'^2 = |E_B|^2  (quadratic/symmetric; ALWAYS > 0 = sign-blind).

     t        Xi(t)         N(t)=Xi'^2-XiXi''   D(t)=|E_B|^2     phi'=N/D     arrow
       8.0        0.1033     0.000751176      0.012565   0.0597831  fwd (phi'>0)
   14.1347    1.9598e-10      1.91191e-6    1.91191e-6         1.0  fwd (phi'>0) <- zero
      17.0   -0.00054338      7.13482e-8    3.63808e-7    0.196115  fwd (phi'>0)
    21.022    6.4117e-12     3.15054e-10   3.15054e-10         1.0  fwd (phi'>0) <- zero
      23.0     5.6218e-6     1.84373e-11   4.48969e-11    0.410658  fwd (phi'>0)
   25.0109    -5.312e-13     1.60074e-12   1.60074e-12         1.0  fwd (phi'>0) <- zero
      30.0    -1.5017e-8     1.30304e-15   2.53467e-15    0.514087  fwd (phi'>0)

  min phi' over tested t = 0.0597831  (>=0: RH-consistent, arrow always forward).  At each zero Xi=0 so
  N=Xi'^2 and phi'=1 exactly -- the clock ticks one unit per zero (phi(T)/pi = N(T)).
  KEY: D=|E_B|^2 is POSITIVE at every t -- the Bures magnitude cannot see the SIGN of phi'.  An
  off-line zero is exactly N(t)<0 (phi' reverses); D stays >0 and is BLIND to it.  The arrow lives
  in the numerator N (additive/Kubo-Mori), in the KERNEL of the Bures quadratic -- Irreversible
  Blind Spot Lemma 1, on zeta: the symmetric/quadratic instrument cannot carry the antisymmetric arrow.

================  PART C: synthesis -- front (a) is blind on TWO axes  ================
Front (a)'s statistical->individual gap is now explained at the structural level, and it is blind
on BOTH of the program's blind-spot axes at once:
  * CUMULANT axis (CBS / parent): the averaged instrument is 2nd-ORDER -- it misses the higher
    moments (the two-tower thermometer; 2nd moment Levinson-Conrey ~42%, needs the 4th).
  * REVERSIBILITY axis (this sibling): the averaged instrument is SYMMETRIC -- the off-line
    displacement is the ANTISYMMETRIC arrow, in the KERNEL by parity (Lemma 1), NOT merely a
    rare event. The Bures magnitude |E_B|^2 is sign-blind; the phase phi' (Kubo-Mori/m_B) carries it.
These two axes are ORTHOGONAL (Irreversible paper E14: zero cross-talk). So the 'individual
guarantee' RH needs is doubly out of reach of symmetric 2nd-moment statistics: it requires an
instrument that is BOTH higher-order AND asymmetric -- which is exactly the additive/phase object
the program kept arriving at (phi', m_B=-Xi'/Xi, the integer count N(T), the predictor).

THE UNIFIED STATEMENT (tiered):
  [P] computed: symmetric forms are blind to the antisymmetric part (A in kernel), exact to 1e-15;
      the de Branges arrow-numerator N=Xi'^2-XiXi'' carries the sign phi'; the Bures denominator
      |E_B|^2>0 is sign-blind; phi'>=0 at all tested t (RH-consistent); phi'=1 at each zero.
  [A] structural: off-line zero = antisymmetric arrow = phi'<0 = irreversibility gap Delta>0;
      RH <=> phi'>=0 <=> Delta=0 <=> detailed balance <=> no zero off the reflection axis. The
      Kubo-Mori-vs-Bures fork (T24) IS the symmetric-vs-predictor split of the irreversibility axis.
  [open == RH] forcing phi'>=0 (Delta=0) from the arithmetic = building the asymmetric (predictor)
      object whose self-adjointness is detailed balance -- the Hilbert-Polya H = N_inf + V_arith,
      whose self-adjointness IS RH. Difficulty conserved; the unification names WHY every symmetric
      instrument fails and WHICH object (asymmetric/additive/phase) is forced.

NET: the Irreversible Blind Spot upgrades front (a) from 'averages are blind' to the exact parity
reason -- the arrow is antisymmetric, the symmetric instruments' kernel -- and identifies the lift
as the predictor/phase object, unifying the statistical->individual gap, the Kubo-Mori/Bures fork,
and the 'one obstruction, three names' into ONE: the off-line displacement is the arrow of time of
the zero-dynamics, and RH is its detailed balance.
```
