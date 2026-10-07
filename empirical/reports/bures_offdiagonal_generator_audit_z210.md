# Bures Off-Diagonal Generator Audit

- Claim tested: honest off-diagonal Bures generator on target-local pairs
- Status: EXPLICIT_BUILT
- Row: 210
- State count: 210
- xi labels: `['p7:res', 'p5:res', 'p3:res']`
- target radius: 1.695744e+00
- target pair count: 5841
- classical shadow anisotropy: 1.088986e-01
- classical shadow q4: 2.180711e-02
- classical unit-symbol fourth ratio: 6.691668e-01

## Explicit Bures Checks

- Bures derivation q4: 4.944924e-07
- Bures unit-symbol fourth ratio: 6.691668e-01
- max |derivation second - edge formula|: 5.743850e-12
- max |Hamiltonian symmetric form|: 0.000000e+00
- max |Lindblad - 1/2 derivation|: 1.164153e-10

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
