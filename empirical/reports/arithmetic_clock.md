# Attempting the arithmetic clock phi'(x) >= 0 from the primes (= RH); the exact obstruction

**Script:** `empirical/verify_arithmetic_clock.py`
**Context:** the irreducible step -- construct the de Branges clock from arithmetic, non-circularly.
**Finding:** clock = archimedean Gamma-drift + von Mangoldt prime-fluctuation; primes converge only
off the line (on it the continuation = the zeros); drift ~ fluctuation ~ log T (marginal); the clock
is PROVABLY monotone after heat-smoothing (t>Lambda>=0, Rodgers-Tao); RH = the t->0 / strip-crossing.
**Nature:** numerical/exact (mpmath), labelled.  NOT a proof (this step IS RH).

```text
Attempting the arithmetic clock: build phi'(x) >= 0 from the primes, and pin the exact obstruction.

This IS RH (phi' >= 0 <=> the de Branges phase clock is monotone <=> self-adjointness of H = N_inf +
V_arith).  We do NOT fabricate a proof.  We (1) write the clock's explicit-formula decomposition into
an archimedean drift + an arithmetic (von Mangoldt) fluctuation, (2) exhibit the precise obstruction --
the prime sum converges only OFF the critical line; on it, its continuation IS the zeros (circular),
(3) record the ONE genuinely non-circular partial positivity available (de Bruijn-Newman / Rodgers-Tao:
the heat-flowed clock is provably monotone for t > Lambda >= 0), so RH = the t->0 closure, and (4) show
the drift and the fluctuation are the SAME ORDER (~log T) -- the analytic face of RH's marginality.

The clock's log-derivative is m = -xi'/xi, and exactly (Re s > 1):
   -xi'/xi(s) = [ -1/s - 1/(s-1) + (1/2)log(pi) - (1/2)psi(s/2) ]  +  [ sum_n Lambda(n) n^{-s} ],
                \________________ archimedean (Gamma) drift ________/    \___ arithmetic (primes) ___/
the arithmetic part being -zeta'/zeta(s) = sum Lambda(n) n^{-s}.  On s = 1/2 + i z this is the von
Mangoldt sum sum Lambda(n) n^{-1/2 - i z} (the multiplicative basis that CARRIES the zeros).

NUMERICAL/EXACT (mpmath), labelled.  NOT a proof.

================  PART 1 : explicit-formula decomposition of the clock (at s=2, Re>1)  ======
  -xi'/xi(2)  (direct)                 = -0.06906623153000068
  archimedean(2) + (-zeta'/zeta(2))    = -0.06906623153000068
    archimedean (Gamma) drift          = -0.639027224625
    arithmetic (primes) -zeta'/zeta(2) = 0.569960993095
  identity match to 6.46e-27   -> the clock is EXACTLY arch drift + prime part (Lambda(n) >= 0).
  prime interpretation: sum_{n<=N} Lambda(n)/n^2 converges to -zeta'/zeta(2) (slow ~(logN)/N tail):
     N=   100 : 0.5595279169   (gap to limit = 0.0104)
     N=  2000 : 0.5694601166   (gap to limit = 0.000501)
     N= 20000 : 0.5699109381   (gap to limit = 5.01e-5)

================  PART 2 : the convergence boundary (why it is not direct)  ================
  sum_{n<=N} Lambda(n) n^{-s} partial sums:
    Re s=2 (>1: converges)   N=100:0.5595279  N=1e3:0.5689589  N=1e4:0.5698611   (-zeta'/zeta=0.569961)
    Re s=1.2 (slow)          N=100:2.450866  N=1e3:3.20193  N=1e4:3.66613   (-zeta'/zeta=4.458337)
  ON the line (Re s = 1/2) the prime sum DIVERGES; its continuation -zeta'/zeta(1/2+iT) has
  POLES at the zeros (residue = multiplicity).  |zeta'/zeta(1/2+iT)| near gamma_1=14.1347:
     T=  13.5   |zeta'/zeta| = 1.5070927
     T=  14.0   |zeta'/zeta| = 7.3434356
     T=  14.1   |zeta'/zeta| = 28.716222
     T=14.134   |zeta'/zeta| = 1378.9586
  -> the convergent (non-circular) prime data lives at Re s>1; on the line it becomes the
     zeros themselves.  Transferring the prime positivity (Lambda>=0) ACROSS the strip to the
     line is exactly the open step -- it cannot be done by the prime sum alone.

================  PART 3 : archimedean drift vs arithmetic fluctuation -- SAME ORDER  =======
  drift density d(T)=(1/2)log(T/2pi)  vs  fluctuation S(T)=(1/pi)arg zeta(1/2+iT)  (both ~log T)
      T        d(T)=(1/2)log(T/2pi)     S(T)        log T
      30        0.7816602          -0.56488     3.4012
     100        1.383647          -0.0024099     4.60517
     500        2.188366          -0.58673     6.21461
    1000        2.534939          0.38376     6.90776
    5000        3.339658          -0.33117     8.51719
  -> drift density d(T)=(1/2)log(T/2pi) and the unconditional bound |S(T)| <= c log T are BOTH
     Theta(log T) -- the same order.  S(T) is small here (zeros track the smooth count), but the
     worst-case excursion PERMITTED is the size of the drift itself, so no soft bound forces
     phi' >= 0; RH is exactly that the actual excursion never reverses the drift.  (Same
     marginality as R(0)~0.9999, Weil margin 0, Lambda=0.)

================  PART 4 : the non-circular partial result, and the exact open step  ========
GENUINELY NON-CIRCULAR (de Bruijn 1950 + Rodgers-Tao 2018): the heat-flowed Xi_t(z) =
int e^{t u^2} Phi(u) cos(uz) du is REAL-ROOTED for t > Lambda, with Lambda >= 0 PROVEN
unconditionally.  So for t > Lambda the heat-flowed clock phi'_t >= 0 PROVABLY -- a monotone
arithmetic clock EXISTS after enough smoothing, with no circular use of RH.  RH = Lambda <= 0
= pushing t -> 0^+ in the Born cone (program: RH-Pass4/5).  And Lambda = 0 exactly = RH 'barely
true' -- the same marginality, now as the heat constant sitting at the boundary.

THE EXACT OPEN STEP (three faces, one thing):
  (i)  self-adjointness of H = N_inf + V_arith in the Kubo-Mori geometry;
  (ii) the archimedean local positivity (Connes trace term >= 0), the analogue of the Hodge
       index over a curve;
  (iii) Lambda <= 0, i.e. the heat flow reaches t=0 without leaving the Born cone.
All three = phi'(x) >= 0 from the arithmetic, non-circularly = RH.  The prime positivity
Lambda(n) >= 0 gives the half-plane Re s > 1 (the EASY half); FE reflects to Re s < 0; the open
content is the strip-crossing to Re s = 1/2.  NOT crossed.  But the clock is now explicit, its
decomposition is arch-drift + prime-fluctuation, it is PROVABLY monotone after heat-smoothing
(t > Lambda >= 0), and the gap is the single, sharply-named t -> 0 / strip-crossing closure.
```
