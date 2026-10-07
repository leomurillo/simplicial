# Bures Off-Diagonal Generator Audit

- Claim tested: honest off-diagonal Bures generator on target-local pairs
- Status: EXPLICIT_BUILT
- Row: 30
- State count: 30
- xi labels: `['p5:res', 'p3:res', 'p2:res']`
- target radius: 2.574638e+00
- target pair count: 281
- classical shadow anisotropy: 1.689008e-01
- classical shadow q4: 6.637604e-02
- classical unit-symbol fourth ratio: 1.649076e+00

## Explicit Bures Checks

- Bures derivation q4: 7.375115e-05
- Bures unit-symbol fourth ratio: 1.649076e+00
- max |derivation second - edge formula|: 2.469136e-13
- max |Hamiltonian symmetric form|: 0.000000e+00
- max |Lindblad - 1/2 derivation|: 1.818989e-12

## Interpretation

For diagonal physical observables at the maximally mixed state, the
off-diagonal SLD/Bures derivation norm is exactly the edge-weight
shadow with weights |H_ij|^2. The pure Hamiltonian commutator is
skew-adjoint and contributes zero symmetric Dirichlet form. The
Hermitian Lindblad dissipator gives one half of the derivation
quadratic form. The raw q4 changes under the global Bures scale,
so the scale-invariant comparison is the unit-symbol fourth ratio;
there the off-diagonal realization matches the diagonal edge
shadow rather than reducing its locality cost.
