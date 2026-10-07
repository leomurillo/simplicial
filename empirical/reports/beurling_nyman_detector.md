# Beurling-Nyman Detector + the Approximation Face of RH

**Script:** `empirical/verify_beurling_nyman_detector.py`
**Context:** P0 Conj 8.1 follow-up. Weil positivity (prior probe) <-> Beurling-Nyman
approximation, both <=> RH, both governed by sum_rho 1/|rho|^2 = 2+gamma-log4pi.
**Nature:** numerical (mpmath/numpy); labelled.

```text
Beurling-Nyman detector: a second, independent RH-equivalent, and its bridge to the zeros.

Nyman-Beurling / Baez-Duarte criterion (classical): RH <=> the constant 1 lies in the
L^2(0,1)-closure of the span of the dilated fractional parts rho_{1/n}, equivalently the
least-squares distance d_N = dist(1, span{rho_{1/n} : 2<=n<=N+1}) -> 0 as N -> infinity.

Clean computability. With u = 1/t, on each unit interval u in [k,k+1) one finds
        rho_{1/n}(t) = {floor(1/t)/n} = {k/n}   (a STEP function),
so the Gram matrix and target vector are pure arithmetic sums (no oscillatory integration):
        G_{mn} = sum_{k>=1} {k/m}{k/n} / (k(k+1)),     v_n = sum_{k>=1} {k/n} / (k(k+1)),
and ||1||^2 = 1, so   d_N^2 = 1 - v^T G^{-1} v   over the chosen index set.
Sanity: for N=1 (n=2 only) this gives d_1^2 = 1 - log 2 exactly.

This is the APPROXIMATION face of RH (1 is reachable) -- dual to the POSITIVITY face probed in
verify_conj81_positivity.py (the Weil form stays PSD). Both <=> RH; both are governed by the
SAME zeros: under RH the Baez-Duarte-Balazard-Landreau-Saias asymptotic is
        d_N^2 * log N  ->  sum_rho 1/|rho|^2  =  2 + gamma - log(4 pi)  ~  0.0461914,
a sum over the zeros. We (A) extract the Weil-form DETECTOR test function that witnesses an
off-line zero, (B) compute d_N from scratch and watch it decrease, (C) verify the zero-rate
constant two ways. NUMERICAL probe (labelled); the conclusions (a sign, a monotone decrease,
a constant match) are robust.

================  PART A : the detector test function (Weil side)  ================
  basis frequencies (zero #1 neighborhood): ['12.13', '13.13', '14.13', '15.13', '16.13']
  detector f* = eigenvector of min eigenvalue of the OFF-line Weil form (delta=0.2):
     |c*_j| = ['0.283', '0.648', '0.000', '0.648', '0.283']
     arg c*_j = ['+3.14', '-3.14', '-0.00', '+0.00', '+0.00']  (the PHASE profile -- the direction a real basis is blind to)
  Weil energy of this same f*:
     on  the line :  W(f*) = +2.179566e-11   (>= 0)
     off the line :  W(f*) = -4.524760e-01   (<  0  -> detects the off-line zero)

================  PART B : Beurling-Nyman distance d_N = dist(1, span rho_{1/n})  =====
  arithmetic Gram from {k/m}{k/n}/(k(k+1)), K=200000 terms; ||1||^2 = 1.
  N (functions n=2..N+1) |   d_N^2     |   d_N    | d_N^2 * log N
  -----------------------+-------------+----------+--------------
             1           |   0.3068553 | 0.553945 |   0.212696
             2           |   0.0957513 | 0.309437 |   0.105194
             3           |   0.0659555 | 0.256818 |   0.091434
             4           |   0.0363231 | 0.190586 |   0.058460
             5           |   0.0362121 | 0.190295 |   0.064883
             6           |   0.0243926 | 0.156181 |   0.047466
             7           |   0.0242487 | 0.155720 |   0.050424
             8           |   0.0240993 | 0.155239 |   0.052952
             9           |   0.0238568 | 0.154456 |   0.054932
            10           |   0.0205038 | 0.143191 |   0.049166
            11           |   0.0205023 | 0.143186 |   0.050946
            12           |   0.0198785 | 0.140991 |   0.050987
            13           |   0.0185360 | 0.136147 |   0.048917
            14           |   0.0183844 | 0.135589 |   0.049786

  sanity: d_1^2 = 0.3068553 vs exact 1 - log2 = 0.3068528  (match: True)
  d_N^2 is monotone decreasing in N: True   (RH <=> d_N -> 0)

================  PART C : the BN rate is a sum over the zeros  ================
  sum_rho 1/|rho|^2  =  2 + gamma - log(4 pi)  =  0.04619141793   (closed form, exact)
  partial sum over first 200 zeros 2*sum 1/(1/4+gamma^2) = 0.042069721  (slow tail; trending up to it)
  BDBLS asymptotic: d_N^2 * log N  ->  this constant. Our d_N^2 log N column is in its
  basin (slow ~1/log N convergence; small N is far from the limit, as expected).

================  WHERE THIS CORNERS RH  ================
Two independent faces of the SAME wall, both computed, both pointing at the zeros:
  - POSITIVITY (Weil form, prior probe): PSD exactly on the line; an off-line zero
    drives min-eig < 0. PART A gives the explicit DETECTOR f* -- a phase-profiled test
    function with W(f*) >= 0 on-line and < 0 off-line. RH <=> this form stays PSD.
  - APPROXIMATION (Beurling-Nyman, PART B): d_N = dist(1, span rho_{1/n}) decreases
    monotonically; RH <=> d_N -> 0. Computed from scratch (d_1^2 = 1 - log2 exactly).
  - BRIDGE (PART C): both rates are set by sum_rho 1/|rho|^2 = 2+gamma-log4pi. The
    same zeros govern positivity AND approximation.

Cornered further: RH now sits at the meeting of two computable, zero-controlled
conditions -- a positivity (stays PSD in the limit) and an approximation (d_N -> 0).
Neither crossed; both sharply localized, and now cross-checked against each other.
```
