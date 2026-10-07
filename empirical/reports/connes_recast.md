# The Connes Recast: two faces of RH as one trace-positivity

**Script:** `empirical/verify_connes_recast.py`
**Context:** culmination of the Conj 8.1 / Beurling-Nyman / conditioning probes.
**Nature:** numerical (mpmath/numpy), labelled; reuses the verified explicit-formula balance.

```text
The Connes recast: the two faces of RH as one trace-positivity over the places.

Connes (1999) reads the Weil explicit formula as a TRACE FORMULA on the adele class space:
for a test function h on the idele classes,
        sum_rho h(gamma_rho)  =  Tr(h applied to the zero-operator)  =  sum_v (local term)_v,
the sum running over the places v (the primes p and the archimedean place infinity), plus the
pole. RH is then the POSITIVITY of this trace for h = f * f~ -- equivalently, the
self-adjointness (real spectrum) of the operator D whose spectrum is the zeros.

This single statement subsumes the two faces we probed separately:
  * POSITIVITY (Weil form): Tr((f*f~)(D)) >= 0.  On the line the form is a Gram matrix V*V
    (manifestly a trace of a positive operator); off the line it is NOT of the form V*V and
    goes indefinite -- the detector. So  RH <=> the form is V*V  <=>  D self-adjoint.
  * APPROXIMATION (Beurling-Nyman): 1 is cyclic / reachable -- the same operator's spectral
    measure has the support that makes d_N -> 0.
Two properties (positivity, cyclicity) of ONE operator; both <=> RH.

PART A. Exhibit the trace-positive structure Z = V*V on the line, and that an off-line zero
        breaks the V*V form (min-eig < 0). [Weil positivity, in operator/self-adjointness form.]
PART B. Decompose the trace formula by PLACE: pole + archimedean + sum over primes = sum over
        zeros, displaying each local term. Isolates the archimedean place as the dominant,
        and the one whose positivity contribution is the open step (the Connes-Consani prolate
        operator -- the archimedean 'forcing structure', the analogue of the Hodge index that
        forces the function-field RH).

NUMERICAL (mpmath/numpy), labelled. Reuses the verified explicit-formula balance (~1e-31).

================  PART A : Weil positivity = Tr(V*V), broken off the line  ============
  On the line:  Z = V* V  (V_{rho,j} = phi_j(rho)) -- manifestly a trace of a POSITIVE
    operator. min eigenvalue = -1.152e-15  (>= 0: self-adjoint / spectrum real).
  Off the line (one zero at Re=1/2+-0.2): the form is V* W with W != V, no longer V*V.
    min eigenvalue = -4.525e-01  (< 0: the operator is NOT self-adjoint).
  => RH  <=>  the Weil form is of the form V*V  <=>  the zero-operator is self-adjoint.

================  PART B : the trace formula = sum over places  ================
  spectral side:  Tr(h(D)) = sum_rho h(gamma)        = 0.0370825834626
  geometric side = sum over places (pole + arch - primes):
     place: pole (s=1)            local term = 2.01002504172
     place: infinity (archimedean) local term = -1.96812233305   <-- dominant, transcendental
     place: p = 2                   local term = -0.00481941554516
     place: p = 3                   local term = -7.09664320254e-7
     place: p = 5                   local term = -2.49022726168e-14
     place: p = 7                   local term = -8.15498499633e-21
     place: p = 11                  local term = -1.76060314747e-31
     place: p = 13                  local term = -5.46907164409e-36
     ... (remaining primes sum to 0.0)
  sum over places                            = 0.0370825834626
  residual (spectral - geometric)            = 1.787e-31

  The archimedean local term (-1.96812) dominates; the finite primes contribute -0.00482013 in total.
  RH = positivity of this trace for h=f*f~. The finite-place contribution is computable
  and (P0 sec4.3) the Gram part is free; the ARCHIMEDEAN local positivity is the open step.

================  THE SINGLE STATEMENT (the recast)  ================
RH  <=>  Tr_v( (f * f~) )  >=  0  for all test functions f,
where Tr_v is the Weil/Connes trace = sum over places (PART B), equivalently
        <=>  the zero-operator D is self-adjoint  (its Weil form is V*V, PART A)
        <=>  1 is reachable in the Beurling-Nyman space (cyclicity of the same D).

Three readings, one object. The finite places give a free Gram positivity; the open
content is the ARCHIMEDEAN local positivity -- the Connes-Consani prolate-operator
target. That archimedean term is the forcing structure to find, exactly as the Hodge
index forces the function-field RH (P0/P4). The march showed brute N cannot reach it;
this recast says what WOULD: a symmetry that makes the archimedean trace term positive
by construction, the way intersection positivity does over a curve.
```
