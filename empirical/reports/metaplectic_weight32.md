# L(1,chi_D) as a weight-3/2 (metaplectic) coefficient, tied to N_inf

**Script:** `empirical/verify_metaplectic_weight32.py`
**Context:** develops the divergent metaplectic/Selberg lens on the real-quadratic Siegel core.
**Result:** L(1,chi_{-D})=pi H(D)/sqrt(D), H=Hurwitz class number = weight-3/2 coefficient (certified
exact by Hurwitz-Kronecker); weight-3/2 = metaplectic = N_inf archimedean; imaginary=holomorphic/CM
(GGZ-controllable) vs real=geodesic-period/regulator (spectral-only; Selberg, Kim-Sarnak 0.238/0.25).
**Nature:** exact (fractions) + mpmath, validated.  NOT a proof.

```text
Developing the metaplectic/Selberg lens: L(1,chi_D) as a weight-3/2 coefficient, tied to N_inf.

The divergence (the exceptional real-quadratic D is NOT irreducible) routes through the metaplectic /
half-integral-weight world -- which is the program's OWN apparatus (the UPT Bargmann-Fock at v=inf is
the Weil representation = the archimedean component of Mp_2, where weight-3/2 forms live).  Concretely:

  IMAGINARY D (fundamental):  L(1,chi_{-D}) = pi * H(D) / sqrt(D),   H = Hurwitz class number.
  And {H(n)} are the Fourier coefficients of a WEIGHT-3/2 modular form (Zagier's Eisenstein series),
  certified by the HURWITZ-KRONECKER class-number relation:
       sum_{r in Z} H(4n - r^2)  =  2 sigma_1(n) - sum_{d|n} min(d, n/d).
  This relation IS the modularity (the Hecke/theta-trace identity); we verify it in exact arithmetic.

So L(1,chi_{-D}) is literally a coefficient of an N_inf-form (weight 3/2; archimedean = the oscillator
the program already selected).  The asymmetry that makes REAL D the hard core, sharpened:
  * IMAGINARY D <-> a HOLOMORPHIC weight-3/2 coefficient = a CM point on the modular curve (0-dim,
    rigid).  Controllable: Goldfeld-Gross-Zagier (Heegner points) gives effective h(-D) >> (log D)^{1-eps};
    h=1 finite (HSB, 9 fields).
  * REAL D <-> a GEODESIC-CYCLE period (1-dim closed geodesic of length = the regulator R_D).  The
    regulator is the geodesic length; the family is the length spectrum (Selberg trace formula's
    geometric side).  No holomorphic CM point -> GGZ does not apply.  Control is SPECTRAL: the Siegel
    zero <-> an exceptional small Laplacian eigenvalue (Selberg lambda_1 >= 1/4), where the proven
    partial result Kim-Sarnak lambda_1 >= 975/4096 ~ 0.238 is EFFECTIVE -- teeth the arithmetic lens lacks.

This probe VERIFIES the exact chain (H via reduced forms; Hurwitz-Kronecker modularity; L=pi H/sqrt D),
and states the holomorphic-imaginary / geodesic-real asymmetry with the spectral residual.  NOT a proof.

EXACT (fractions) + mpmath, labelled.

================  Hurwitz class numbers H(N) (reduced-form count)  ================
  H(3..24) match known values: True
  H = {3:1/3, 4:1/2, 7:1, 8:1, 11:1, 12:4/3, 15:2, 16:3/2, 19:1, 20:2, 23:3, 24:2}

================  Hurwitz-Kronecker relation (the weight-3/2 MODULARITY), exact  ===========
  sum_{r} H(4n-r^2) = 2 sigma_1(n) - sum_{d|n} min(d, n/d) :
    n     LHS (sum_r H)      RHS (2 sigma_1 - min-div)     equal?
    1     1                  1                          OK
    2     4                  4                          OK
    3     6                  6                          OK
    4     10                 10                         OK
    5     10                 10                         OK
    6     18                 18                         OK
    7     14                 14                         OK
    8     24                 24                         OK
    9     21                 21                         OK
   10     30                 30                         OK
  Hurwitz-Kronecker holds for n=1..10 (exact): True  -> {H(n)} IS a weight-3/2 modular form.

================  L(1,chi_{-D}) = pi H(D)/sqrt(D)  (the metaplectic-coefficient realization)  =
     D     H(D)      pi H(D)/sqrt(D)      class-number formula 2 pi h/(w sqrtD)    match?
      3   1/3      0.604599788      0.604599788      True
      4   1/2      0.785398163      0.785398163      True
      7   1        1.18741041      1.18741041      True
      8   1        1.11072073      1.11072073      True
     11   1        0.947225825      0.947225825      True
     15   2        1.62231147      1.62231147      True
     19   1        0.720730784      0.720730784      True
     20   2        1.40496295      1.40496295      True
     23   3        1.96520205      1.96520205      True
     24   2        1.28254983      1.28254983      True
    163   1        0.246068528      0.246068528      True
  (H(D) = 2 h(-D)/w, so pi H/sqrtD = 2 pi h/(w sqrtD) = L(1,chi_{-D}) exactly; e.g. D=4 -> pi/4.)

================  the holomorphic-imaginary / geodesic-real asymmetry (the lens)  ===========
IMAGINARY D: H(D) is a HOLOMORPHIC weight-3/2 coefficient = a CM point (0-dim, rigid) on the
  modular curve.  Controllable: Goldfeld + Gross-Zagier (Heegner-point height of a triple-zero
  L-function) => effective h(-D) >> (log D)^{1-eps}; the tightest (h=1) are the FINITE 9 fields
  (HSB, last D=-163; here H(163)=1, L(1,chi_{-163})=pi/sqrt163).
REAL D: the analogue is a GEODESIC-CYCLE period -- a closed geodesic of length = the regulator
  R_D, a 1-dimensional cycle, NOT a rigid CM point.  No Heegner point -> GGZ does not transfer.
  The regulator IS the geodesic length; the family {(R_D,h_D)} is the length spectrum (Selberg
  trace formula, geometric side).  Control is SPECTRAL: a real Siegel zero <-> an exceptional
  small Laplacian eigenvalue (Selberg lambda_1 >= 1/4), where Kim-Sarnak's PROVEN lambda_1 >=
  975/4096 ~ 0.238 is EFFECTIVE -- the teeth the ineffective arithmetic (Siegel) lens lacks.

PAYOFF: L(1,chi_D) lives natively as a coefficient of a weight-3/2 (metaplectic) form whose
archimedean component IS the program's N_inf.  The exceptional real D is the geodesic-period /
exceptional-eigenvalue shadow -- over-determined, NOT irreducible; softest on the spectral side
(Kim-Sarnak 0.238 -> 0.25) and the metaplectic side (our UPT).  Not a proof; a route with teeth.
```
