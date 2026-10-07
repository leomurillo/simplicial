# Conjecture 8.1 Positivity Probe (RH direction)

**Script:** `empirical/verify_conj81_positivity.py`
**Context:** P0 Conjecture 8.1 -- RH = Weil positivity surviving the archimedean adjunction.
**Nature:** high-precision NUMERICAL (mpmath); the archimedean term is transcendental.

```text
Probe of Conjecture 8.1 (P0): does the Weil quadratic form's positivity track RH?

RH-direction step. We corner the open step P0 isolates -- "positivity survives once the
archimedean Gamma-factor is adjoined" -- by testing the Weil/explicit-formula quadratic form
directly. Number-field analogue of the function-field circle probe
(verify_finite_global_positivity.py): there RH <=> Frobenius eigenvalues on the CIRCLE <=> a
Toeplitz form PSD, and pushing an eigenvalue off the circle broke PSD. Here the "circle" is the
critical LINE; the archimedean term is what sets that geometry.

NUMERICAL (mpmath/numpy), not exact-integer: the archimedean term (digamma psi(1/4+ir/2)) and
the prime weights (log p / sqrt p) are transcendental -- exactly P0/P6's point that the
archimedean place is not finitely generable. Floats are the medium, labelled; the conclusions
(sign of a min-eigenvalue; a balance to many digits) are robust.

RETAINED CORRECTION (the gate on this probe). A first formulation used
B_ij = sum_rho h_i(gamma_rho) conj(h_j(gamma_rho)) -- a sum of v v*, hence PSD BY CONSTRUCTION,
unable to test anything (min-eig ~ 0 for every offset). The correct Weil pairing is
        B_ij = sum_rho  fhat_i(rho) * conj( fhat_j(1 - conj(rho)) ),
since for g = f_i (convolved with) f_j-tilde the explicit-formula summand is
fhat_i(rho) conj(fhat_j(1-conj rho)). On the line 1-conj(rho)=rho, so B is a Gram matrix => PSD
(P0 sec 4.3, "finite positivity is free"). OFF the line 1-conj(rho) != rho, the pairing is
between DIFFERENT points and B becomes indefinite. That asymmetry is the whole content.

PART A (core). fhat_j(s) = transform of an even modulated Gaussian f_j(u)=e^{-u^2/2tau^2}cos(w_j u):
        fhat_j(s) = (1/2) sqrt(2pi) tau [ e^{tau^2 (c+i w_j)^2/2} + e^{tau^2 (c-i w_j)^2/2} ],  c=s-1/2,
peaked at frequency w_j. Build B for the true zeros (on the line) and after pushing ONE zero to
Re = 1/2 +- delta (its functional-equation + conjugate QUADRUPLE). Scan delta; watch min-eig cross 0.
  K : min-eig(B) >= 0 at delta=0 and < 0 once delta>0 -> Weil positivity <=> RH, and SENSITIVE.
  L : insensitive to delta.

PART B (assembly). Validate the Riemann-Weil explicit formula numerically for a Gaussian:
(sum over zeros) =?= (pole) + (archimedean digamma term) - (prime sum). A clean balance shows the
archimedean Gamma-term is the piece that completes the finite prime data (the Place-Completion).

================  PART A : Weil positivity tracks the critical line  ================
  first zeros gamma_k : 14.135, 21.022, 25.011, 30.425, 32.935, 37.586, ...
  basis: 5 complex-modulated Gaussians focused at zero #1 (gamma_1=14.135), tau=1.0
  Weil form B_ij = sum_rho fhat_i(rho) conj(fhat_j(1-conj rho)) over the first 15 zeros;
  zero #1 pushed to Re = 1/2 +- delta (its functional-equation quadruple).

  delta (off-line offset of zero #1) |   min eigenvalue of B   | positive?
  -----------------------------------+-------------------------+-----------------
            0.00                      |          -1.151773e-15 | yes (PSD)
            0.02                      |          -4.435731e-03 | NO  (indefinite)
            0.05                      |          -2.775248e-02 | NO  (indefinite)
            0.10                      |          -1.114278e-01 | NO  (indefinite)
            0.15                      |          -2.522894e-01 | NO  (indefinite)
            0.20                      |          -4.524760e-01 | NO  (indefinite)
            0.30                      |          -1.044081e+00 | NO  (indefinite)

  [A] on the line (delta=0): PSD = True ;  off-line breaks positivity = True (first at delta=0.02)

================  PART B : the archimedean term completes the prime side  ===========
  test function h(r)=exp(-r^2/2 sigma^2), sigma=5.0
  zero side   sum_rho h(gamma)        = 0.037082583462639
  pole  2 h(i/2)                      = 2.0100250417188
  archimedean (digamma) term          = -1.9681223330467
  prime side  2 sum L(n) n^-.5 g       = 0.0048201252095084
  pole + archimedean - prime          = 0.037082583462639
  residual (zero side - RHS)          = 1.787e-31

  [B] explicit formula balances to ~1.8e-31. The archimedean term (-1.96812) dominates the completion
      of the tiny prime side (-0.00482) into the zero side (0.0370826).

================  WHERE THIS CORNERS RH  ================
PART A realized K. The Weil quadratic form is PSD exactly on the critical line, and a
single off-line zero (its functional-equation quadruple) drives the minimum eigenvalue
negative. So 'Weil positivity' is EQUIVALENT to RH and SENSITIVE to off-line zeros -- the
exact number-field mirror of the function-field circle test (where RH is Weil's theorem).
Conjecture 8.1's open step is therefore correctly and sharply stated: prove this one
explicit form stays PSD in the projective limit.

PART B: the explicit formula balances (residual ~1.8e-31). The archimedean digamma term is the
completing factor turning the finite prime data into the object whose positivity is RH --
P0's Place-Completion, numerically concrete, and P6's point that this term is the one the
finite primes cannot supply.

Cornered (not crossed): RH = positivity of this one computable form; finite part free;
archimedean part the completing piece; off-line sensitivity demonstrated. Remaining target:
uniform positivity of the archimedean-adjoined limit -- the Connes/self-adjointness step,
now sharply localized.
```
