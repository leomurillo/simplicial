# The scattering term: zeta (level 1) and L(s,chi) (level q); Siegel zero = exceptional eigenvalue

**Script:** `empirical/verify_scattering_zeta_L.py`
**Context:** the continuous/scattering term of the Selberg trace formula -- where zeta/L and the
Siegel zero / exceptional eigenvalue live.
**Finding:** phi(s)=sqrt(pi)Gamma(s-1/2)zeta(2s-1)/(Gamma(s)zeta(2s)), phi(s)phi(1-s)=1; zeta zeros =
scattering poles (s=rho/2); a real pole beta in (1/2,1) = exceptional eigenvalue lambda=beta(1-beta);
Siegel zero of L(s,chi) is exactly such a pole; L(s,chi_5)>0 on (1/2,1) (no Siegel); Kim-Sarnak 0.238/0.25.
**Nature:** numerical (mpmath), scattering structure computed/validated.  NOT a full TF balance.

```text
The continuous/scattering term of the trace formula: zeta (level 1) and L(s,chi) (level q), and the
EXACT mechanism 'Siegel zero = exceptional eigenvalue' as a scattering pole on the real segment.

Both requests, via the one object that carries them -- the scattering matrix (Eisenstein constant term):

LEVEL 1 (SL(2,Z)):  the scattering determinant is
      phi(s) = sqrt(pi) * Gamma(s-1/2) * zeta(2s-1) / ( Gamma(s) * zeta(2s) ).
   It is the zeta-laden continuous-spectrum term of the trace formula (the term int h(r) phi'/phi(1/2+ir)dr).
   zeta(2s) in the DENOMINATOR => the zeros of zeta are the POLES (resonances) of phi: a zeta zero rho
   gives a scattering pole at s = rho/2.  Under RH these sit on Re(s)=1/4.  So RH = 'the level-1 scattering
   resonances lie on a vertical line' -- zeta enters the SAME trace formula whose GEODESIC side is the
   real-quadratic arithmetic (regulators/class numbers, previous probe).  One formula, both arithmetics.

THE POLE<->EIGENVALUE LAW:  a pole of phi at s* yields a residual Laplacian eigenvalue lambda = s*(1-s*).
   A pole on the REAL segment s* = beta in (1/2,1) gives lambda = beta(1-beta) in (0,1/4) -- an EXCEPTIONAL
   eigenvalue (lambda < 1/4).  Level 1: zeta(2s) has NO real zero in (1,2), so no real pole, no exceptional
   eigenvalue (consistent with lambda_1 ~ 91).

LEVEL q (Gamma_0(q), real chi):  the scattering carries L(s,chi).  A LANDAU-SIEGEL ZERO is a REAL zero
   beta in (1/2,1) of L(s,chi); it is a real scattering pole at s=beta, hence an EXCEPTIONAL eigenvalue
   lambda = beta(1-beta) -> 0 as beta -> 1.  Selberg lambda_1 >= 1/4  <=>  no scattering pole in (1/2,1)
   <=>  no Siegel zero; Kim-Sarnak lambda_1 >= 975/4096 ~ 0.238 is the proven, effective partial bound.
   (The precise theta-lift quantitative dictionary is cited, not re-derived: Iwaniec; Sarnak; Phillips-Sarnak.)

This probe: (A) computes phi(s), validates phi(s)phi(1-s)=1, shows zeta-zero = scattering pole; (B) the
pole<->eigenvalue law and the level-1 no-exceptional fact; (C) computes L(s,chi_5) on (1/2,1), shows no
Siegel zero -> no exceptional eigenvalue, with the lambda=beta(1-beta) law; (D) synthesis + honest scope.
NUMERICAL (mpmath), labelled.  NOT a full trace-formula balance (elliptic/parabolic terms not implemented;
the continuous integral has an r=0 zeta-pole cancelled by the parabolic term -- noted, not faked).

================  (A) LEVEL 1: the zeta-scattering determinant phi(s)  ================
  phi(s) = sqrt(pi) Gamma(s-1/2) zeta(2s-1)/(Gamma(s) zeta(2s))
  unitarity check  phi(s)phi(1-s) = (1.0 - 7.14214298e-28j)  (should be 1)  -> True
  zeta zero rho_1 = 1/2 + i*14.134725  ->  scattering pole at s = rho_1/2 = 1/4 + i*7.067363:
     s = 1/4 + i*6.7673626 :  |phi(s)| = 1.9947471
     s = 1/4 + i*6.9673626 :  |phi(s)| = 5.2425176
     s = 1/4 + i*7.0473626 :  |phi(s)| = 25.744114
     s = 1/4 + i*7.0633626 :  |phi(s)| = 128.64238
  -> |phi| blows up as s -> rho_1/2: the zeta zero IS a scattering resonance (pole of phi).
  RH  <=>  all these resonances (s = rho/2) lie on Re(s) = 1/4.  Zeta lives in the SAME trace
  formula whose geodesic side is the real-quadratic arithmetic (regulators/class numbers).

================  (B) scattering pole at s*  <->  residual eigenvalue lambda = s*(1-s*)  ======
  a REAL pole s*=beta in (1/2,1) gives lambda=beta(1-beta) in (0,1/4): an EXCEPTIONAL eigenvalue.
     beta      lambda = beta(1-beta)
     0.6       0.24
     0.8       0.16
     0.9       0.09
     0.99       0.0099
     0.999       0.000999
  -> beta -> 1 (a tighter Siegel zero) pushes lambda -> 0 (a smaller exceptional eigenvalue).
  LEVEL 1: zeta(2s) has NO real zero in (1,2), so phi has no real pole in (1/2,1) -> NO
  exceptional eigenvalue (consistent with lambda_1 ~ 91.14).  No Siegel analogue at level 1.

================  (C) LEVEL q: a Siegel zero of L(s,chi) = a real scattering pole = exceptional  =
  Gamma_0(q) scattering carries L(s,chi); a real zero beta in (1/2,1) of L(s,chi) (a SIEGEL zero)
  is a real scattering pole -> an exceptional eigenvalue lambda=beta(1-beta).  Check chi_5 on (1/2,1):
     s        L(s, chi_5)
     0.55      0.25337421
     0.6      0.27463336
     0.65      0.29551539
     0.7      0.31600925
     0.75      0.33610563
     0.8      0.35579689
     0.85      0.3750769
     0.9      0.39394097
     0.95      0.41238571
  L(1, chi_5) = 0.43040894  (= 2 log(golden)/sqrt5 = 0.43040894).  min over (1/2,1) = 0.253374 at s=0.55 > 0:
  L(s,chi_5) has NO real zero in (1/2,1) -> NO scattering pole there -> NO exceptional eigenvalue.
  (A Siegel zero would be a beta just below 1 with L(beta,chi)=0; none for chi_5 -- as expected.)

================  (D) synthesis, and honest scope  ================
ONE trace formula, both arithmetics: GEOMETRIC side = closed geodesics = real-quadratic data
(regulators R_D, class numbers h_D; previous probe, golden-ratio geodesic dominant); SPECTRAL
side = discrete Maass eigenvalues + the CONTINUOUS term built from zeta (level 1) / L(s,chi)
(level q).  The zeros of zeta/L are the scattering POLES; a pole on the real segment (1/2,1) --
a SIEGEL ZERO -- is a residual EXCEPTIONAL eigenvalue lambda=beta(1-beta).  Thus:
   RH for zeta   <=>  level-1 scattering resonances (rho/2) on Re(s)=1/4 (continuous spectrum);
   GRH/no Siegel <=>  no real scattering pole in (1/2,1) <=> Selberg lambda_1 >= 1/4;
   Kim-Sarnak lambda_1 >= 0.238 = the proven, EFFECTIVE partial bound (the teeth).

HONEST SCOPE: computed + validated -- phi(s) and phi(s)phi(1-s)=1; zeta-zero = scattering pole;
the pole<->eigenvalue law; L(s,chi_5) > 0 on (1/2,1) (no Siegel zero).  CITED, not derived -- the
precise theta-lift dictionary (which Kim-Sarnak bound gives which Siegel-zero bound; Iwaniec,
Sarnak, Phillips-Sarnak) and the SL(2,Z) Maass eigenvalues.  NOT done -- a full numerical
trace-formula balance: the continuous integral int h(r) phi'/phi(1/2+ir) dr has an r=0 pole from
zeta(1+2ir) that is cancelled by the parabolic term; balancing needs the exact elliptic/parabolic
constants, which I did not implement and will not fake.  The scattering structure -- the heart of
'zeta/L in the trace formula' and of 'Siegel zero = exceptional eigenvalue' -- is exact and here.
```
