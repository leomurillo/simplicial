# (GBP) cleanest form: Szego spectral factorization of the Weil field u_B = |Sigma|^2 <=> u_B>=0 <=> RH

**Script:** `empirical/verify_weil_spectral_factorization.py`  (builds on the (GBP) Fourier-support correction).
**Finding:** since u_B and |Sigma|^2 share the log-rational lattice with matched (explicit-formula) amplitudes,
(GBP) [|Sigma|^2=u_B] is exactly 'the Weil-Poisson field u_B is a perfect square' -- which by Szego/Fejer-Riesz
holds iff u_B>=0 iff RH. The program's |Sigma|^2 is the spectral OUTER factor; the residual is purely u_B>=0.
Sign distinction: |Sigma|^2>=0 is free (a square); RH is the converse on the FIXED prime amplitudes. Computed:
the inter-zero margin min u_B(.,y) ~ c*y -> 0 (the factorization knife-edge), unifying with de Branges phi'
and R(0)~0.9997. Replaces the audit's 'disjoint lattices' with 'shared lattice, square-factorization=positivity'.
**Nature:** numerical (mpmath) + spectral-factorization structure. NO RH claim; the cleanest classical form of the wall.

```text
(GBP), cleanest form: the Weil-Poisson field u_B is a SQUARE |Sigma|^2 iff u_B>=0 iff RH
(Szego/Fejer-Riesz spectral factorization on the log-rational lattice), and the positivity is marginal.

Corrected picture (verify_gbp_fourier_support.py): u_B(xi,y)=Im[-Xi'/Xi(xi+iy)] and |Sigma|^2 share the
LOG-RATIONAL Fourier lattice {log n}; their amplitudes are the Guinand-Weil prime-power weights
Lambda(n)/sqrt n (the explicit formula, TRUE unconditionally).  So (GBP) [|Sigma|^2 = u_B] is NOT a
coincidence of disjoint measures; it is the statement that the Weil field u_B is a perfect square.

SZEGO / FEJER-RIESZ.  A function with one-sided (log-rational, n>=1) Fourier support factors as
|Sigma|^2 for a Hardy/Dirichlet OUTER function Sigma(xi)=sum_n a_n n^{i xi}  IFF it is >= 0 (and
log-integrable, Szego).  Hence
   (GBP) [u_B = |Sigma|^2]  <=>  u_B >= 0  <=>  m_B Herglotz  <=>  no off-axis zero  <=>  RH.
The program's |Sigma|^2 IS the spectral (outer) factor; the residual is exactly the POSITIVITY of u_B.
This is why Paper III sec 8.5a's three structural moves all reduce to 'u_B>=0 = RH': it is Fejer-Riesz.

THE SIGN DISTINCTION (why the program's free positivity is not RH).  |Sigma|^2 >= 0 is automatic for ANY
coefficient sequence (a square is nonnegative -- Fejer-Riesz forward).  RH is the converse on the FIXED
arithmetic data: the SPECIFIC Weil distribution (arch + Lambda(n)/sqrt n at log n) admits a square
factorization.  The amplitudes are not free -- they are the primes -- and whether THOSE form a positive
(factorizable) field is RH, not a choice.

MARGINALITY.  u_B(xi,y) = sum_rho y/((xi-gamma_rho)^2 + y^2) >= 0 (Poisson field).  Between consecutive
zeros it DIPS toward 0 as y->0 (the field grazes its floor); an off-axis zero would push the dip BELOW 0.
So RH is the knife-edge 'u_B barely stays >= 0', the same marginality as R(0)~0.9997 / phi'>=0 / Lambda=0.

PART A states the spectral-factorization form.  PART B computes the inter-zero MARGIN min u_B(.,y) and its
y->0 decay (the factorization's delicacy).  PART C: the sign distinction + the unification + honest scope.
NUMERICAL (mpmath); NO RH claim -- it gives (GBP) its cleanest classical form (Szego factorization = RH).

================  PART A: (GBP) = Szego factorization of u_B = |Sigma|^2  <=>  u_B>=0 = RH  ===
  u_B(xi,y) sampled at the first two zeros and the gap midpoint (Poisson field, should be >=0):
     u_B(14.13472, 0.5) = 2.033773
     u_B(17.57838, 0.5) = 0.1134056
     u_B(21.02204, 0.5) = 2.068874
  The amplitudes of u_B on {log n} are the Guinand-Weil weights Lambda(n)/sqrt n (the explicit
  formula, unconditional).  (GBP) asks: is this FIXED arithmetic field a perfect square |Sigma|^2?
  By Szego/Fejer-Riesz, YES iff u_B>=0 -- i.e. (GBP) <=> u_B>=0 <=> RH.  |Sigma| is the outer factor.

================  PART B: the marginal positivity -- min u_B between zeros, y->0  ============
  min_{xi in (gamma_1, gamma_2)} u_B(xi,y) as y->0 (the field grazes its floor; an off-axis zero
  would push it < 0 -- the only way (GBP)/RH fails):
     y         min u_B on (g1,g2)      argmin xi        min u_B / y
      1.0      0.2165303              17.47636        0.21653
      0.5      0.11325532             17.49284        0.226511
     0.25      0.057298872            17.49667        0.229195
      0.1      0.022996198            17.49772        0.229962
     0.05      0.011503601            17.49787        0.230072
  => min u_B stays > 0 (RH-consistent) but DECAYS ~ linearly in y (min u_B / y -> const): the field
  grazes 0 between the zeros as y->0.  RH = 'this grazing never crosses 0, at every gap, every y' =
  the knife-edge.  An off-line zero z0 makes u_B(xi,y) ~ ... - y/((xi-Re z0)^2 - (y-Im z0)^2+..) DIP
  BELOW 0 near z0 -- the unique failure mode.  Marginal positivity = R(0)~0.9997 = phi'>=0 = Lambda=0.

================  PART C: the sign distinction, the unification, and the honest scope  ========
THE SIGN DISTINCTION (why the program's unconditional positivity is not RH):
  * |Sigma|^2 >= 0 is FREE -- a square is nonnegative for ANY coefficients (Fejer-Riesz forward).
    The program HAS this (the Gram-Bochner density d nu_y >= 0, unconditional).
  * RH is the CONVERSE on FIXED data: the SPECIFIC Weil field u_B (arch + Lambda(n)/sqrt n at log n)
    is a square. The coefficients are the PRIMES, not a free choice; their positive-definiteness
    (= square-factorizability = Szego) is RH. So (GBP) = 'the arithmetic field is the program's
    free square' = the Szego factorization closes on the ARITHMETIC weights = RH.

THE UNIFICATION (the program's one wall, now in its cleanest classical form):
  (GBP) = u_B is a square = u_B >= 0 = m_B Herglotz = E_B Hermite-Biehler = phi' >= 0 (de Branges)
        = Weil explicit-formula positivity = Apex Lemma_HJ Hankel >= 0 = uniform no-Siegel mod P_n
        = front (a) statistical->individual = the marginal R(0)~0.9997 knife-edge = GRH_N = RH.
  The Szego/Fejer-Riesz reading is the cleanest: the SAME prime-power amplitudes that make the
  Gram side a (free) square must make the Weil field a square -- and that is exactly RH.

WHAT THE PUSH ADDS (honest):
  [P/computed] u_B's prime-power Fourier support (last probe) + the inter-zero margin min u_B ~ c*y
    -> 0 (the factorization knife-edge), unifying (GBP) with the de Branges/phi' and R(0) marginality.
  [structural, correct] (GBP) = Szego spectral factorization of the Weil field; the program's
    |Sigma|^2 is the outer factor; the residual is u_B>=0 = RH. This REPLACES the audit's 'disjoint
    lattices, integrated identity' with the correct 'shared lattice, square-factorization = positivity'.
  [open == RH] the factorization exists <=> u_B>=0 <=> RH. Conservation holds: the cleanest classical
    form of the wall is Szego/Weil positivity on the log-rational lattice -- it IS RH, no shortcut.

VERDICT: pushing the cleaner form gives (GBP) its sharpest classical identity -- the spectral (Szego/
Fejer-Riesz) factorization of the Weil-Poisson field into the program's Gram square, equivalent to the
field's positivity, equivalent to RH -- with the positivity shown MARGINAL (grazes 0 between zeros).
This is the maximal honest localization: not a closure, but the wall named in its cleanest form, and
unified with every other route. The program reduces RH to Weil/Szego positivity; that reduction is real.
```
