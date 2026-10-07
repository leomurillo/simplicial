# Bures Off-Diagonal Generator Audit

- Claim tested: off-diagonal Bures generator diagonal-shadow identity check
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
- thermal rho condition: 1.380457e+01
- thermal max |Gamma_H|: 2.220446e-16
- thermal max |Gamma cross|: 1.776357e-15
- thermal full-image unit-symbol fourth ratio: 7.384398e+01
- thermal max |SLD image cross second|: 3.786778e+03

## Interpretation

This is a diagonal-shadow consistency check, not a
coherent-sector no-go.  The observables are
X_mu=diag(xi_mu), so the Markov carre-du-champ is evaluated
only on a commuting subalgebra.

For diagonal physical observables at the maximally mixed state, the
off-diagonal SLD/Bures derivation norm is exactly the edge-weight
shadow with weights |H_ij|^2. The pure Hamiltonian commutator is
skew-adjoint and contributes zero symmetric Dirichlet form. The
Hermitian Lindblad dissipator gives one half of the derivation
quadratic form. The raw q4 changes under the global Bures scale,
so the scale-invariant comparison is the unit-symbol fourth ratio;
there the off-diagonal realization matches the diagonal edge
shadow rather than reducing its locality cost.

For non-maximally mixed diagonal rho, the reported Gamma cross
term is a residual of three evaluations of a linear map:
Gamma_{H+D}-Gamma_H-Gamma_D. It is therefore algebraically zero,
with the displayed value only measuring floating-point noise. The
Hamiltonian derivation also cancels from Gamma on these observables
by the Leibniz rule. The SLD norm of the generator image can have a
Hamiltonian/dissipative cross term, but that is a different
diagnostic from the symmetric Dirichlet form used for reversible
Green-kernel recovery.

The live coherent-route question is not addressed here: compute
the Green kernel from the non-symmetric resolvent of a genuinely
non-reversible quantum generator on the relevant quotient/full
algebra, without replacing that resolvent by Gamma on the diagonal
subalgebra.
