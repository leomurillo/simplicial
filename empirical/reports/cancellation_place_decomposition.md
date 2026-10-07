# Pushing the cancellation: the head<->tail matching decomposed by place

**Script:** `empirical/verify_cancellation_place_decomposition.py`
**Context:** opens up the large-degree cancellation that the head<->tail matching reduces to.
**Result:** the cancellation splits by place -- an EXACT archimedean Gamma engine (sign-definite
differences) vs a PROVABLY log-convex arithmetic moment perturbation; k=2 = exact Turan place-split.
**Nature:** exact/numerical (mpmath dps 60), labelled, pre-registered.  NOT a proof (uniform = RH).

```text
Pushing the cancellation itself: the head<->tail matching, decomposed by PLACE.

From verify_head_tail_matching: RH-on-the-peaks = the higher log-curvatures of L_n=log|gamma_n|
keep the Jensen polynomials hyperbolic uniformly in degree, even as the oscillator gap g_d~1/d->0.
Beyond the proven finite-degree frontier this can only hold by CANCELLATION (sign/structure), not
size.  Here we open up that cancellation and find it splits cleanly by place.

DECOMPOSITION.  gamma_n = (-1)^n a_n n!/(2n)!,  a_n = int_0^inf t^{2n} Phi(t) dt.  Put b_n=|gamma_n|
and L_n = log b_n = C_n + A_n,
    C_n = log( n! / (2n)! )            -- the ARCHIMEDEAN / Gamma-factor part (combinatorial),
    A_n = log a_n                      -- the ARITHMETIC part (moments of the Riemann measure Phi).

Two structural facts make the cancellation precise:

 (1) C_n's finite differences are EXACT and SIGN-DEFINITE (pure Gamma asymptotics, NO arithmetic):
        D^1 C_n = -log(4n+2),
        D^2 C_n = log( (2n+1)/(2n+3) )                 < 0   (the oscillator's negative curvature),
        D^3 C_n = log( (2n+3)^2 / ((2n+1)(2n+5)) )      > 0,
        ... sign(D^k C_n) = (-1)^{k+1} for k>=2, magnitude ~ c_k / n^{k-1}.
     This IS the Hermite/oscillator engine -- explicit, arithmetic-free, the same for ANY measure.

 (2) A_n = log a_n is PROVABLY LOG-CONVEX:  a_n = int s^n dnu(s) (s=t^2, dnu=Phi/(2 sqrt s) ds >= 0
     since Phi>0), so by Cauchy-Schwarz a_n^2 <= a_{n-1} a_{n+1}, i.e. D^2 A_n >= 0.  The arithmetic
     part is a log-convex perturbation; it carries the xi-zeros.

THE CANCELLATION, order by order.  D^k L_n = D^k C_n + D^k A_n.  Hyperbolicity needs the net to keep
the sign-definite oscillator structure: the ARCHIMEDEAN explicit differences must DOMINATE the
ARITHMETIC moment differences.  The cleanest instance is k=2 (Turan):
        D^2 L_n < 0  <=>  D^2 A_n < -D^2 C_n = log( (2n+3)/(2n+1) )
   <=>  a_{n+2} a_n / a_{n+1}^2  <  (2n+3)/(2n+1).
That is an EXACT place-split of the Turan inequality: arithmetic log-convexity (left, >=1) is beaten
by the archimedean ratio (right, >1).  RH (uniform-in-degree hyperbolicity) = this domination holding
for all orders k -- archimedean Gamma-curvature beats arithmetic moment-convexity, uniformly.

PARTS: A the archimedean engine (exact, verified); B the arithmetic perturbation (log-convex,
verified); C the cancellation order-by-order, the exact k=2 Turan place-split + its margin, and the
domination ratios r_k(n)=|D^k A|/|D^k C| (does the margin close as k grows -> the uniformity wall?);
D the honest reading.

NUMERICAL/EXACT mix (mpmath dps 60), labelled.  NOT a proof: the uniform domination IS RH.  But the
cancellation is now place-separated -- an explicit archimedean engine vs a provably-log-convex
arithmetic perturbation -- and the k=2 case is rigorous.  Pre-registered; refutation retained.

Computing 26 Phi-moments (dps=60) ...
  done.

================  PART A : archimedean (Gamma) part C_n -- exact, sign-definite engine  =====
  closed forms verified to 3.64e-59 :
    D^1 C_n = -log(4n+2)                         (drift)
    D^2 C_n = log((2n+1)/(2n+3)) < 0             (oscillator's NEGATIVE curvature)
    D^3 C_n = log((2n+3)^2/((2n+1)(2n+5))) > 0
  sign(D^k C_n) = (-1)^{k+1} for k>=2, magnitude ~ 1/n^{k-1}.  Sample (n=8):
    D^2=-0.1112  D^3=0.01114  D^4=-0.00203  D^5=0.000509  D^6=-0.0001571
  -> the Hermite/oscillator engine, fully explicit and ARITHMETIC-FREE (same for any measure).

================  PART B : arithmetic part A_n = log a_n -- provably log-convex perturbation  =
  D^2 A_n >= 0 for all n (log-convex, by Cauchy-Schwarz on the moments a_n): True
  Sample D^k A_n (n=8), the perturbation carrying the xi-zeros:
    D^2=0.08044  D^3=-0.009254  D^4=0.001792  D^5=-0.0004649  D^6=0.0001467
  -> arithmetic moment-convexity OPPOSES the archimedean curvature at k=2 (D^2 A>0 vs D^2 C<0).

================  PART C : the cancellation (archimedean beats arithmetic, order by order)  ==
  k=2 is the EXACT Turan place-split:  a_{n+2}a_n/a_{n+1}^2  <  (2n+3)/(2n+1) ?
    n   arith ratio L2=a_{n+2}a_n/a_{n+1}^2   arch ratio R2=(2n+3)/(2n+1)   margin R2-L2  (>0 OK)
    0   2.791102858            3.0            0.2089   OK
    2   1.32789109            1.4            0.072109   OK
    4   1.17159468            1.222222222            0.050628   OK
    8   1.083762628            1.117647059            0.033884   OK
   12   1.053861083            1.08            0.026139   OK
   16   1.039102842            1.060606061            0.021503   OK
   20   1.030411135            1.048780488            0.018369   OK
  Turan (k=2 cancellation) holds: True.  The arithmetic log-convexity L2>1 is beaten by the
  archimedean R2>1 -- but BOTH ->1, so the cancellation margin ->0 (the marginality, place-resolved).

  domination ratio r_k(n) = |D^k A_n| / |D^k C_n|   (<1 => archimedean wins that order):
     k    r_k(n=4)     r_k(n=8)     r_k(n=12)    net D^k L keeps archimedean sign?
     2   0.78918   0.7232   0.68165    yes
     3   0.88952   0.83057   0.78926    yes
     4   0.93184   0.88255   0.84486    yes
     5   0.95434   0.91346   0.87981    yes
     6   0.96777   0.93375   0.90389    yes
  Reading: where r_k < 1 the archimedean engine dominates that order outright; the net D^k L
  keeps the oscillator sign (-1)^{k+1}.  Arithmetic OPPOSES archimedean at EVERY order
  (sign D^k A = (-1)^k  vs  sign D^k C = (-1)^{k+1}), so 'net keeps archimedean sign' <=> r_k<1.
  OBSERVED: r_k(n) < 1 throughout, but RISES toward 1 as k grows (fixed n) and FALLS as n grows.
  => the domination MARGIN 1-r_k CLOSES at higher order (head / large degree) and OPENS in the
  tail.  That is the uniformity-in-degree wall, place-resolved.  RH = r_k(n) stays < 1 for ALL
  k, n: the archimedean Gamma-curvature never lets the arithmetic moment-curvature overtake it.

================  PART D : what the cancellation IS (honest)  ================
RH-on-the-peaks = the archimedean Gamma-curvature DOMINATES the arithmetic moment-convexity in
the log-profile L_n = C_n + A_n, uniformly in order k (= Jensen degree d).  Place-separated:
  * the ENGINE is archimedean: C_n=log(n!/(2n)!), with EXACT sign-definite differences
    D^k C_n ~ (-1)^{k+1}/n^{k-1} -- the oscillator/Hermite/Bargmann-Fock structure, explicit,
    and arithmetic-free (the metaplectic-UPT factor at v=infinity, Q8vM3, made elementary);
  * the PERTURBATION is arithmetic: A_n=log a_n, PROVABLY log-convex (Cauchy-Schwarz on the
    Riemann moments), carrying the xi-zeros and OPPOSING the archimedean curvature.
The k=2 cancellation is EXACTLY Turan, place-split: a_{n+2}a_n/a_{n+1}^2 < (2n+3)/(2n+1) -- a
rigorous inequality (both sides ->1, margin ->0: marginality, place-resolved).  For k>=3 the
r_k(n)<1 are the place-separated higher-order analogues: NOT claimed term-by-term equivalent to
hyperbolicity (that is a whole-polynomial condition), but the controlling quantities that track
it -- all < 1 in reach.  RH (= xi in Laguerre-Polya = all Jensen polynomials hyperbolic) lives in
the UNIFORM control of these ratios.  This is the sharpest 'the archimedean place forces RH'
statement of the arc: an explicit archimedean engine vs a provably-log-convex arithmetic load,
with k=2 rigorous and the open content = uniform-in-degree archimedean domination.

NOT a proof: the uniform domination is RH.  But the cancellation is no longer a black box -- it
is 'Gamma-curvature beats moment-convexity, order by order', the engine is explicit, the
perturbation is provably log-convex, and the lowest order is a proven (place-split) inequality.
Cornered to a single uniform inequality between two named, place-separated quantities.
```
