# (a) the head <-> oscillator-tail matching, made explicit and measured

**Script:** `empirical/verify_head_tail_matching.py`
**Context:** pushes on the matching itself (continues verify_jensen_turan_peaks / _hermite_archimedean).
**Nature:** numerical (mpmath moments + roots), labelled, pre-registered; gate-disciplined.

```text
(a) the head <-> oscillator-tail matching itself, made explicit and measured.

Set-up (from verify_jensen_hermite_archimedean): the Jensen tower J_{d,n}(t)=sum_k C(d,k) gamma_{n+k} t^k,
gamma_n=(-1)^n a_n n!/(2n)!, a_n=int_0^inf t^{2n} Phi dt.  RH <=> all J_{d,n} hyperbolic.
Work with b_n = a_n n!/(2n)! = |gamma_n| > 0 (sign only flips t->-t; hyperbolicity unchanged) and
the LOG-PROFILE  L_n = log b_n.

THE MATCHING MECHANISM.  Locally  b_{n+j}/b_n = exp( j*DL_n + C(j,2)*D2L_n + C(j,3)*D3L_n + ... ),
where D^k L_n is the k-th forward difference of L.  The HERMITE / oscillator template is exactly
'L_n is QUADRATIC in n':  D2L = const < 0 (the Gaussian curvature), D^{>=3}L = 0.  Then J_{d,n}
renormalizes to the Hermite polynomial H_d (GOR-Zagier).  So:
  * the OSCILLATOR TAIL is the regime where L_n has straightened to a downward parabola;
  * the ARITHMETIC HEAD is where the higher differences D^{>=3}L_n are still appreciable;
  * the MATCHING is the head's higher log-curvatures DECAYING into the oscillator quadratic.

THE PROTECTION-vs-PERTURBATION picture (the rigorous backbone of GOR-Zagier).  H_d has simple
real roots separated by a min-gap g_d > 0 (the oscillator's spectral protection).  J_{d,n} is a
perturbation of H_d of size set by the higher differences; while that perturbation stays below an
O(g_d) threshold the roots cannot collide -> J_{d,n} stays hyperbolic.  So for each d there is a
head depth n_0(d) (where the perturbation drops under the gap) beyond which hyperbolicity is FORCED
by the oscillator; the head n < n_0(d) is a finite check.  RH = the head is hyperbolic for ALL d
simultaneously -- i.e. the arithmetic head embeds in the archimedean oscillator's hyperbolic class.

PART A : the log-profile straightening.  D2L_n < 0 (Turan, the oscillator curvature) and
         D3L_n, D4L_n -> 0 (the head bending into the oscillator quadratic).  [the matching, mechanism]
PART B : protection vs perturbation.  Hermite min-gap g_d; the dimensionless perturbation
         rho_d(n)=max_{3<=k<=d}|D^k L_n|/|D2L_n|; the ACTUAL normalized min root-gap mu_d(n) of
         J_{d,n} swept head->tail; the global-min 'weld point'; head vs Hermite-tail asymptote.
PART C : the matching margin as a scalar RH-diagnostic + the structural reading (place-transfer).

NUMERICAL (mpmath moments + roots), labelled.  NOT a proof: it makes the matching explicit, names
its controlling quantities (oscillator gap g_d vs arithmetic higher-log-curvature), and localizes
RH's open content to uniform head control across all d.  Pre-registered expectations stated; any
refutation is retained (GPD gate).

Computing 32 Phi-moments (dps=50) ...
  done.

================  PART A : the log-profile L_n = log|gamma_n| straightens to the oscillator  ====
Pre-registered expectation: D2L_n < 0 (Turan / oscillator curvature), and D3L_n, D4L_n -> 0
(head bending into the oscillator quadratic).  Refutation retained.
   n     D2L_n (<0?)        D3L_n (->0?)       D4L_n (->0?)
   0   -0.0721755   0.0113216   -0.00334782
   2   -0.0528802   0.00594845   -0.0013216
   4   -0.0423049   0.00371409   -0.000658643
   8   -0.0307867   0.00188786   -0.000238483
  12   -0.0245004   0.00115952   -0.000113946
  16   -0.0204828   0.000791406   -6.37309e-5
  20   -0.0176702   0.000577824   -3.94563e-5
  24   -0.01558   0.000442135   -2.62256e-5
  27   -0.0143299   0.000370197   -1.99969e-5
  D2L_n < 0 for all n (Turan / oscillator curvature present): True
  |D3L| tail < head (straightening): True   ;  |D4L| tail < head: True
  -> the head's higher log-curvature decays: L_n bends toward the oscillator's downward
     parabola.  THAT is the matching, as a mechanism (not just an outcome).

================  PART B : oscillator protection g_d  vs  arithmetic perturbation  ===========
Hermite H_d min root-gap g_d (normalized) = the oscillator's spectral protection.
rho_d(n)=max_{3<=k<=d}|D^k L_n|/|D2L_n| = dimensionless arithmetic perturbation.
mu_d(n) = actual normalized min root-gap of J_{d,n} (>0 iff hyperbolic).  Sweep head->tail.

  d=3 : Hermite gap g_3 = 0.5   (all J_{3,n} hyperbolic in reach: True)
        mu head(n=0)=0.49122  ...  weld(n=12)=0.47922 [rho=0.04733]  ...  tail(n=28)=0.48074  -> g_3=0.5
  d=4 : Hermite gap g_4 = 0.31783724519578227   (all J_{4,n} hyperbolic in reach: True)
        mu head(n=0)=0.31388  ...  weld(n=0)=0.31388 [rho=0.1569]  ...  tail(n=27)=0.31746  -> g_4=0.31783724519578227
  d=5 : Hermite gap g_5 = 0.2372489339040398   (all J_{5,n} hyperbolic in reach: True)
        mu head(n=0)=0.22756  ...  weld(n=0)=0.22756 [rho=0.1569]  ...  tail(n=26)=0.23057  -> g_5=0.2372489339040398
  d=6 : Hermite gap g_6 = 0.18551709743297928   (all J_{6,n} hyperbolic in reach: True)
        mu head(n=0)=0.17829  ...  weld(n=0)=0.17829 [rho=0.1569]  ...  tail(n=25)=0.18107  -> g_6=0.18551709743297928

  Reading: mu_d(n) stays > 0 throughout (every tested J_{d,n} hyperbolic) and tracks toward
  the Hermite gap g_d as n grows (tail).  The 'weld point' (global-min gap) is the tightest
  Jensen polynomial = the single most marginal peak; rho there = how non-oscillator the head
  still is.  The oscillator gap g_d is the protection the arithmetic perturbation stays under.

================  PART D : the measured scalings, and the honest uniformity wall  ===========
  oscillator gap g_d  vs  head gap mu_d(0)  (is the head ~ the oscillator?):
    d=3 : g_d=0.5 , g_d*d=1.5 , mu_d(0)/g_d=0.98245
    d=4 : g_d=0.31784 , g_d*d=1.2713 , mu_d(0)/g_d=0.98756
    d=5 : g_d=0.23725 , g_d*d=1.1862 , mu_d(0)/g_d=0.95915
    d=6 : g_d=0.18552 , g_d*d=1.1131 , mu_d(0)/g_d=0.96102
  -> g_d*d = O(1): the oscillator gap shrinks like Theta(1/d).  mu_d(0)/g_d = 0.96-0.99:
     the head gap is ~the oscillator gap (the perturbation only gently tightens it).

  arithmetic perturbation rho(n)=|D3L|/|D2L| (the head straightening rate):
    n= 4 : rho=0.087793 , rho*sqrt(n)=0.17559
    n= 8 : rho=0.061321 , rho*sqrt(n)=0.17344
    n=12 : rho=0.047327 , rho*sqrt(n)=0.16394
    n=20 : rho=0.032701 , rho*sqrt(n)=0.14624
    n=27 : rho=0.025834 , rho*sqrt(n)=0.13424
  -> rho*sqrt(n) = O(1): rho(n)=Theta(1/sqrt n) -> 0.  But rho(0) is Theta(1) in d (set by
     D3, bounded below), while g_d=Theta(1/d) -> 0.

  HONEST (lesson from the prior gate catch): g_d falls like 1/d and the head perturbation
  does NOT, so a crossover MUST eventually occur -- but it is NOT witnessed for d<=6 (the gap
  reduction is only a few %%; mu_d(0)/g_d ~ 0.96-0.99).  Like the Hermite limit, uniformity-in-d
  is ASYMPTOTIC and unwitnessable in reach; claiming a numerical crossover would repeat the
  caught over-reach.  What IS named: RH = the higher log-curvatures keep mu_d > 0 for ALL d
  even as the oscillator gap g_d -> 0 -- a STRUCTURAL (cancellation/sign), not size, control of
  the arithmetic head at large degree.  This is exactly why proofs reach a finite degree (d<=8
  by GOR-Zagier & successors) and stall: beyond it, size-domination by the oscillator gap is
  lost and only arithmetic structure can carry the matching.

================  PART C : the matching margin (scalar) + what it means  ================
  MATCHING MARGIN  M := min over tested (d,n) of the normalized min root-gap mu_d(n)
                     = 0.17829   (attained at d=6, the deepest weld in reach).
  M > 0 is the peaks-side, scalar form of 'RH in reach': every Jensen polynomial up to the
  tested grid is hyperbolic by margin M.  (A de Bruijn-Newman / sigma_PI-style diagnostic.)

  STRUCTURAL READING (the matching, honestly).  The TAIL is unconditionally the archimedean
  oscillator: GOR-Zagier forces J_{d,n}->H_d, and H_d = Fourier eigenfunctions / Bargmann-Fock
  = the metaplectic-UPT selection at v=infinity (Q8vM3 Lock B).  The HEAD is the arithmetic
  (the dominant low zeros).  The matching = the arithmetic head embeds in the archimedean
  oscillator's hyperbolic class -- i.e. a TRANSFER between the finite/arithmetic places and
  the archimedean place.  That is exactly the Weil / place-completion obstruction (P0): the
  head<->tail matching is NOT lighter than RH (conservation of difficulty), now seen through
  the peaks: the tail side is no longer mysterious (it's the oscillator, forced two ways),
  so ALL of RH's weight sits in the UNIFORM head control -- bounding the head depth n_0(d)
  and verifying the finite head, for every degree d at once.  Known: d<=8 done (GOR-Zagier &
  successors); the open content is the uniformity in d.

  So the push lands here: head<->tail matching = 'does the arithmetic head join the
  archimedean-oscillator tail, uniformly in d'.  Tail forced (oscillator/UPT); head = the
  marginal low-lying zeros; matching = arithmetic->archimedean place-transfer = Weil positivity.
  Cornered to a single, sharply-named uniform-head-control statement; not crossed.
```
