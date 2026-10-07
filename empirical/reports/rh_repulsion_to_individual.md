# Front (a): the statistical->individual repulsion gap, attacked directly

**Script:** `empirical/verify_repulsion_to_individual.py`
**Finding:** the gap is bridged, partially, by three rigorous routes -- proportion ON the line
(Levinson-Conrey 2nd-moment mollifier, now 5/12=41.67%), number OFF the line (zero-density,
Guth-Maynard 2024 breaking Ingham), region AVOIDED (Vinogradov-Korobov). The program-native
contribution: %-on-line is a THERMOMETER for distance past the conductor blind spot (2nd-moment
diagonal = CBS floor; off-diagonal/trilinear = beyond-2nd-order). Residual 41.67%->100% = RH.
**Nature:** numerical (Part A, GUE statistics of first 300 zeros) + literature-exact catalog (B) +
tiered program analysis (C/D). NO claim RH is proved.

```text
FRONT (a): the statistical -> individual repulsion gap, attacked directly.

The unified missing ingredient of RH (from the four-front synthesis): GUE-type repulsion of the zeros
holds ON AVERAGE (pair correlation, gap^2 law) but RH needs the INDIVIDUAL guarantee (every zero on
the line; in its weakest form, no two zeros collide = simplicity).  This probe does three things.

PART A  -- the STATISTICAL side, computed from the actual zeros: nearest-neighbor spacing (Wigner/GUE,
   s^2 repulsion at small s), pair correlation R_2(u)=1-(sin pi u/pi u)^2 (the gap^2 dip), and the
   smallest gap among the first N (GUE extreme-value scaling ~ N^{-1/3}).  These are AVERAGES: a single
   off-line zero is invisible to all of them.  This is exactly why "RH from statistics" stalls.

PART B  -- the three RIGOROUS bridges where statistical control IS converted to individual control,
   with exact constants (verified against the literature, June 2026):
   (B1) proportion ON the line, Levinson-Conrey mollifier (a SECOND-MOMENT method):
        Levinson 1974: 0.3474;  Conrey 1989: 0.4077 (>2/5);  Feng 2012: 0.4128;
        Pratt-Robles-Zaharescu-Zeindler 2020: 5/12 = 0.41667 (current record).  Limiter: mollifier
        length theta (Conrey theta<4/7 via Weil/Kloosterman; longer theta needs off-diagonal/trilinear
        bounds -- Bettin-Chandee-Radziwill, the program's cited anchors).
   (B2) number OFF the line, zero-density estimates:
        Ingham 1940: N(sigma,T) << T^{3(1-sigma)/(2-sigma)+o(1)};  density hypothesis T^{2(1-sigma)+o(1)};
        Guth-Maynard 2024 (arXiv:2405.20552): N(sigma,T) << T^{30(1-sigma)/13+o(1)} (first improvement on
        Ingham's exponent in ~80 yr, via Dirichlet-polynomial large values) => primes in short intervals
        [x, x+x^{17/30+o(1)}] (improving 7/12).
   (B3) region AVOIDED, zero-free region: classical 1-c/log T; Vinogradov-Korobov 1-c/(log T)^{2/3}(loglog)^{1/3}.

PART C  -- the PROGRAM angle (the genuine contribution).  The proportion-on-line is set by the moment
   ORDER controllable.  Levinson-Conrey is a 2nd-moment method => its diagonal main term is the
   second-order (Gaussian) contribution = the CONDUCTOR BLIND SPOT floor; pushing theta past 4/7 needs
   the OFF-DIAGONAL (trilinear/Kloosterman) arithmetic = genuinely beyond-second-order information.
   So % of zeros provably on the line is a THERMOMETER for how far past the conductor blind spot the
   moment machinery reaches: 5/12 = the second-order ceiling now; 100% = all orders = RH.

PART D  -- honest residual + the concrete next step.

NUMERICAL (mpmath) for Part A; literature-exact catalog for B; tiered analysis for C/D.  NO claim that
RH is proved; this LOCATES and QUANTIFIES the statistical->individual gap and gives it a program-native
coordinate (the cumulant/CBS order).

================  PART A: the GUE repulsion of the actual zeros (an AVERAGE)  ================
  computing the first 300 ordinates gamma_n (mpmath zetazero)...
  unfolded nearest-neighbor gaps: count 299, mean 0.998562 (target ~1.0)

  (A1) nearest-neighbor spacing P(s): GUE Wigner surmise p(s)=(32/pi^2) s^2 exp(-4 s^2/pi).
       small-s REPULSION ~ s^2 (NOT flat=Poisson).  Empirical CDF vs GUE CDF:
       s<0.3 : empirical 0.006689   GUE 0.02725   (Poisson 1-e^-x = 0.2592)
       s<0.5 : empirical 0.0602   GUE 0.112   (Poisson 1-e^-x = 0.3935)
       s<0.7 : empirical 0.2341   GUE 0.2584   (Poisson 1-e^-x = 0.5034)
       s<1.0 : empirical 0.5652   GUE 0.5331   (Poisson 1-e^-x = 0.6321)
       => empirical small-gap fraction 0.006689 tracks the GUE s^2 law, NOT Poisson -- repulsion confirmed.

  (A2) pair correlation R_2(u): GUE 1-(sin pi u/pi u)^2 ~ pi^2 u^2/3 at small u (the gap^2 dip).
       binned empirical pair density vs GUE R_2 (normalized to 1 far from 0):
       u in [0.0,0.25): empirical 0.0   GUE R_2(0.125)=0.05036
       u in [0.25,0.5): empirical 0.2424   GUE R_2(0.375)=0.385
       u in [0.5,0.75): empirical 0.9562   GUE R_2(0.625)=0.7786
       u in [0.75,1.0): empirical 1.077   GUE R_2(0.875)=0.9806
       u in [1.0,1.5): empirical 0.9091   GUE R_2(1.25)=0.9676
       u in [1.5,2.0): empirical 0.9697   GUE R_2(1.75)=0.9835
       u in [2.0,3.0): empirical 1.0   GUE R_2(2.5)=0.9838
       => the [0,0.25) bin is DEPRESSED (repulsion); R_2(u)->0 like u^2 as u->0.

  (A3) smallest unfolded gap among the first N (GUE extreme value ~ c N^{-1/3}):
       N=100 : min unfolded gap = 0.3868   (N^{-1/3} = 0.21544)
       N=200 : min unfolded gap = 0.32444   (N^{-1/3} = 0.171)
       N=300 : min unfolded gap = 0.29109   (N^{-1/3} = 0.14938)
       => the tightest pair shrinks ~N^{-1/3}: small gaps are GUARANTEED to recur (statistical),
          but NO lower bound 'gap>0 always' (simplicity) follows -- the individual guarantee is absent.

  KEY: every statistic above is an AVERAGE over zeros.  A single off-line zero (a measure-zero
  event) leaves all of them unchanged.  This is the precise reason 'RH from spectral statistics'
  cannot close: averaged repulsion is blind to the individual exception RH forbids.

================  PART B: where statistical control IS converted to individual (exact)  ======

  (B1) proportion ON the line -- Levinson-Conrey mollifier (a SECOND-MOMENT method) [P, cited]:
        Levinson                         0.3474           (1974)
        Conrey                           0.4077  (>2/5)   (1989)
        Feng                             0.4128           (2012)
        Pratt-Robles-Zaharescu-Zeindler  5/12 = 0.41667   (2020)
        mechanism: count sign changes of a mollified zeta via the mollified 2nd moment
          int_0^T |zeta M|^2 dt and int |(zeta)' M|^2 dt; proportion rises with mollifier length theta.
        LIMITER: theta < 4/7 (Conrey, via Weil bound for Kloosterman sums in the twisted 2nd-moment
          error term); longer theta needs OFF-DIAGONAL / trilinear character-sum bounds (Bettin-Chandee,
          Fouvry-Radziwill-Michel) -- the program's own cited anchors (theta_0 ~ 0.515 on primorial moduli).

  (B2) number OFF the line -- zero-density estimates N(sigma,T)=#{rho: Re>=sigma, |Im|<=T} [P, cited]:
        Ingham 1940     : N(sigma,T) << T^{3(1-sigma)/(2-sigma)+o(1)}   (sigma=3/4 -> exponent 0.600)
        Guth-Maynard 24 : N(sigma,T) << T^{30(1-sigma)/13+o(1)}         (sigma=3/4 -> exponent 0.577)
        density hypoth. : N(sigma,T) << T^{2(1-sigma)+o(1)}             (sigma=3/4 -> exponent 0.500)
        at sigma=3/4: Ingham 0.6,  Guth-Maynard 0.5769,  DH 0.5  (GM closes ~23.1% of the Ingham->DH gap)
        PAYOFF (individual, unconditional): primes in short intervals [x, x+x^theta] asymptotic for
          theta > 17/30 ~ 0.5667 (Guth-Maynard), improving 7/12 ~ 0.5833 (Huxley/Heath-Brown).
        This is genuine statistical->individual: large-VALUE STATISTICS of Dirichlet polynomials
        (how often sum a_n n^{it} is big) => a COUNT of possible off-line zeros.

  (B3) region AVOIDED -- zero-free region (the strongest UNCONDITIONAL individual statement) [P]:
        classical (de la Vallee Poussin): no rho with Re(rho) > 1 - c/log(|Im|+2);
        Vinogradov-Korobov: no rho with Re(rho) > 1 - c/((log T)^{2/3}(loglog T)^{1/3}).
        Individual (every zero avoids the region) and unconditional -- but far from Re=1/2.

================  PART C: the conductor-blind-spot THERMOMETER (program contribution)  =======

  The three bridges all extract 'individual' from 'statistical' via a MOMENT of zeta -- and the
  reach of each is set by the moment ORDER / mollifier length one can asymptotically evaluate:

    * Levinson-Conrey (B1) is a SECOND-MOMENT method.  Its DIAGONAL main term is the second-order
      (Gaussian) contribution -- exactly the CONDUCTOR BLIND SPOT floor (T0/CBS: 2nd order is
      structureless/Gaussian, blind to the higher cumulants).  Each gain in theta past 4/7 is an
      OFF-DIAGONAL term, controlled only by genuinely-higher-order arithmetic (Kloosterman/trilinear,
      Bettin-Chandee).  So the proportion-on-line is, structurally, a measure of how far past the
      second-order (diagonal/Gaussian) approximation the off-diagonal arithmetic is controlled.
    * Guth-Maynard (B2) is a LARGE-VALUE (high-moment) estimate on Dirichlet polynomials -- it wins
      precisely by going beyond the 2nd-moment (mean-square) bound to control the rare large values,
      i.e. beyond the Gaussian/second-order envelope.  Same theme.

  THERMOMETER (the program-native coordinate for the statistical->individual gap):
        proportion on line     reach
        5/12 = 41.67%%          current (2nd-moment, theta<4/7 + off-diagonal nibbles)
        -> 100%% = RH           ALL orders / full off-diagonal control = transcending the CBS
  i.e. the 41.67%% -> 100%% gap is the SAME object as the cumulant frontier R(0)->1 and the CBS:
  the unconditional %%-on-line is one minus a residual that lives entirely in the >2nd-order arithmetic.
  This gives the 'individual guarantee' a concrete address in the program: it is the order at which
  the mollified moment stops being diagonal -- the conductor blind spot, measured in zeros.

  STAGNATION SIGNATURE (data-supported, the sharp claim).  Proportion gains per era:
       1974->1989 (15 yr): +0.0603  (0.00402/yr)
       1989->2012 (23 yr): +0.0051  (0.000222/yr)
       2012->2020 ( 8 yr): +0.00387  (0.000484/yr)
       => gains DECELERATE ~15x (+0.060 -> +0.005 -> +0.004) despite heroic mollifier engineering:
          the 2nd-moment well is nearly dry near ~42%.  CBS PREDICTION (falsifiable): no incremental
          2nd-moment mollifier reaches 50%; breaking ~45% needs a genuinely HIGHER-ORDER (>=4th
          moment) method -- the move past the conductor blind spot.  The 4th moment of zeta IS known
          (Ingham/Heath-Brown), but the MOLLIFIED 4th moment with a long mollifier (the object that
          would raise the thermometer) is open -- that is the exact analytic frontier.

================  PART D: honest residual + the concrete next step  ================
RESIDUAL (tiered):
  [P] statistical repulsion (GUE pair-correlation/spacing/gap^2) -- confirmed above, but an AVERAGE;
  [P] individual reach today: 41.67%% ON the line, N(sigma,T) off-line bound (Guth-Maynard), VK zero-free;
  [open == RH] 41.67%% -> 100%%; even SIMPLICITY (no collision, the weakest individual repulsion) is NOT
      known unconditionally for all zeros -- only a positive proportion (via the same 2nd-moment method).
  Difficulty conserved: closing the thermometer to 100%% = controlling all moment orders = RH.  The gain
  vs the four equivalent fronts is that the gap now has a MOVABLE, fundable coordinate (theta / moment
  order), where the field is ACTIVELY progressing (Conrey 4/7 -> trilinear; Ingham -> Guth-Maynard).

CONCRETE NEXT STEP (where the program can actually push):
  The mollifier-length frontier theta is governed by the TWISTED moment / trilinear character-sum
  bounds (Bettin-Chandee theta_0~0.515, Fouvry-Radziwill-Michel) the program ALREADY cites for its
  primorial-moduli RH direction.  The targeted question: does the program's cumulant/CBS machinery
  (which quantifies the 2nd-order diagonal vs the higher-order off-diagonal) give a NEW handle on the
  mollified 4th moment, or on extending theta past 4/7 on primorial moduli -- i.e. raise the
  thermometer?  That is a finite, fundable analytic-number-theory target (unlike RH), and it is the
  honest realization of 'attack the statistical->individual gap directly': push theta / the moment
  order, equivalently push past the conductor blind spot, equivalently raise the %%-on-line.
```
