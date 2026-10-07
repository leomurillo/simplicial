# Selberg trace formula: sum_D h_D (kernel of R_D) geometric side vs the spectral side

**Script:** `empirical/verify_selberg_geodesic_spectral.py`
**Context:** makes the geodesic (geometric) side and the 'Siegel zero = exceptional eigenvalue'
correspondence concrete for the real-quadratic Siegel core.
**Finding:** geodesic length spectrum ell_D=2 log eps_D^+ (ell_min=2acosh(3/2)=1.9248 at D=5),
weighted by h_D, IS the trace-formula geometric side; spectral side has lambda_1~91>>1/4 at level 1
(no exceptional eigenvalue); Siegel zero <-> exceptional eigenvalue at congruence level, Kim-Sarnak 0.238/0.25.
**Nature:** numerical (geometric side computed/validated) + cited (eigenvalues, Kim-Sarnak).  NOT a full balance.

```text
Selberg trace formula: the geometric (geodesic) side sum_D h_D (kernel of R_D) vs the spectral side,
and the 'Siegel zero = exceptional eigenvalue' correspondence -- made concrete, honestly scoped.

On the modular surface X = SL(2,Z)\H, the Selberg trace formula reads (schematically)
   sum_j h(r_j)  +  (continuous/Eisenstein, involves zeta)   [SPECTRAL: eigenvalues lambda_j = 1/4 + r_j^2]
   =  (Area/4pi) int h(r) r tanh(pi r) dr                    [identity / Weyl]
      + (elliptic, orders 2,3)
      + SUM OVER CLOSED GEODESICS:  sum_{prim gamma} sum_{k>=1} ( ell_gamma / (2 sinh(k ell_gamma/2)) ) g(k ell_gamma)
The geodesic sum is EXACTLY the user's sum_D h_D (kernel of R_D): primitive closed geodesics <-> primitive
indefinite binary quadratic forms <-> real quadratic discriminants D, with
   length ell_D = 2 log eps_D^+   (eps_D^+ = the norm-+1 fundamental unit; (t+u sqrt D)/2, t^2 - D u^2 = 4),
and multiplicity h_D (the form class number).  So the ARITHMETIC of real quadratic fields (regulators,
class numbers) IS the geometric side; the Laplacian eigenvalues are the spectral side; the trace formula
is the bridge.

THE CORRESPONDENCE (Siegel zero <-> exceptional eigenvalue): an eigenvalue lambda < 1/4 (r = i t imaginary,
'exceptional') is the spectral shadow of a Landau-Siegel zero of the relevant L-function -- AT CONGRUENCE
LEVEL Gamma_0(q) (the theta/metaplectic level where the weight-1/2 forms live).  Selberg's conjecture
lambda_1 >= 1/4 <=> no exceptional eigenvalue; the PROVEN partial bound Kim-Sarnak lambda_1 >= 975/4096
~ 0.238 is EFFECTIVE.  For SL(2,Z) ITSELF (level 1) the smallest eigenvalue is lambda_1 ~ 91.14 (r_1 ~
9.534) >> 1/4 -- NO exceptional eigenvalue, so no Siegel-analogue at level 1; the action is at the level.

This probe: (1) computes the geodesic length spectrum {(ell_D, h_D)} (geometric data; validates ell_min);
(2) evaluates the geodesic sum sum_D h_D (kernel) for a test function (short-geodesic dominated);
(3) lists the spectral side (cited Maass eigenvalues; lambda_1 >> 1/4); (4) states the correspondence.
NOT a full numerical trace-formula balance (the continuous/zeta term is not implemented) and NOT a search
for exceptional eigenvalues -- it makes the geometric side and the dictionary concrete.  Labelled.

================  (1) geodesic length spectrum {(ell_D, h_D)} -- the GEOMETRIC side data  ====
   length ell_D    D    h_D    automorph (t,u): t^2-Du^2=4    eps_D^+=(t+u sqrt D)/2
   1.9248473       5   1     (3,1)                  2.618034
   2.6339158      12   1     (4,1)                  3.732051
   3.1335985      21   1     (5,1)                  4.791288
   3.5254943       8   1     (6,2)                  5.828427
   4.1268741      60   2     (8,1)                  7.872983
   4.5848633      24   1     (10,2)                  9.898979
   4.7790529      13   1     (11,3)                  10.90833
   5.5373188      28   1     (16,3)                  15.93725
   5.9864457      44   1     (20,3)                  19.94987
   6.4345439      69   ?     (25,3)                  24.95994
   6.5889246      29   1     (27,5)                  26.96291
   6.8001688      56   1     (30,4)                  29.96663
  shortest geodesic: ell_min = 1.9248473 at D=5  (known value 2*acosh(3/2) = 1.9248473)  match: True
  (ell_D = 2 log eps_D^+; for D=5, eps_5^+ = phi^2, so ell_5 = 4 log phi = 4 R_5.)

================  (2) the geodesic sum  G = sum_D h_D sum_k ell_D/(2 sinh(k ell_D/2)) g(k ell_D)  =
  test function g(u) = exp(-u^2/(2*2.0^2)); contributions by discriminant (k=1 primitive):
     D=  5 : 0.588417   (40.7% of G)
     D= 12 : 0.325388   (22.5% of G)
     D= 21 : 0.201395   (13.9% of G)
     D=  8 : 0.132006   (9.1% of G)
     D= 60 : 0.126795   (8.8% of G)
     D= 24 : 0.03381   (2.3% of G)
  geodesic-side total G = 1.4466948   -- a convergent sum DOMINATED by the shortest geodesic (D=5).
  This is literally sum_D h_D (kernel of R_D): the real-quadratic arithmetic, as the geometric side.

================  (3) the SPECTRAL side: Laplacian eigenvalues lambda_j = 1/4 + r_j^2  ========
  first SL(2,Z) Maass cusp-form spectral parameters r_j (cited; Hejhal/LMFDB):
    9.533695, 12.17301, 13.77975, 14.35851, 16.13807, 16.64426
  lambda_1 = 1/4 + r_1^2 = 91.14134  >>  1/4 = 0.25.
  => SL(2,Z) (level 1) has NO exceptional eigenvalue (lambda < 1/4): Selberg holds trivially
     here; there is no Siegel-zero analogue at level 1.
  Weyl law: N(lambda) ~ (Area/4pi) lambda = lambda/12  (Area = pi/3); the smooth eigenvalue count.

================  (4) 'Siegel zero = exceptional eigenvalue', made concrete  ================
The trace formula equates the GEOMETRIC side -- (Weyl) + (elliptic) + the geodesic sum sum_D h_D
(kernel of R_D), i.e. the REAL-QUADRATIC ARITHMETIC of step (2) -- to the SPECTRAL side, the
Laplacian eigenvalues of step (3) (plus the zeta-laden continuous term).  An EXCEPTIONAL
eigenvalue lambda = 1/4 - s^2 (0<s<1/2; r = i s) is the spectral shadow of a Landau-Siegel zero
beta = 1/2 + s of the associated real L-function -- at CONGRUENCE LEVEL Gamma_0(q) (the theta /
metaplectic level, weight 1/2, Kohnen plus space; Shimura-Waldspurger).  As beta -> 1 (s -> 1/2)
the eigenvalue lambda -> 0.  Selberg's lambda_1 >= 1/4 <=> no exceptional eigenvalue <=> (via the
theta lift) control of the Siegel zero; the PROVEN Kim-Sarnak lambda_1 >= 975/4096 ~ 0.238 is the
effective partial result -- 0.238 of the 0.250 wall, the teeth the ineffective Siegel bound lacks.

HONEST SCOPE: computed -- the geodesic length spectrum (geometric data, validated) and the
geodesic sum sum_D h_D (kernel); cited -- the SL(2,Z) Maass eigenvalues and Kim-Sarnak; NOT done
-- a full geometric=spectral balance (needs the zeta-scattering continuous term) and a search for
exceptional eigenvalues (none at level 1; at congruence level it is the open Selberg problem).
The payoff: the real-quadratic arithmetic (regulators R_D, class numbers h_D) IS the geometric
side of a Laplace spectrum; the Siegel zero is an exceptional eigenvalue; and the spectral side
carries proven effective traction (Kim-Sarnak) the arithmetic side does not.
```
