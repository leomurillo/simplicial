# Conservative Schur Bridge

This note records the exact condition under which the Schur term
\[
  L_{PQ}L_{QQ}^{-1}L_{QP}
\]
is dynamically connected to a conservative Bures/Nambu or variational
reduction.  It also states why the current \(Z_{30}\) projected-resolvent audit
does not yet satisfy that condition.

## Setup

Let \(z=(z_P,z_Q)\) be a linearization of a Bures/Nambu system near a regular
state, split into physical readout variables \(P\) and hidden coherent
variables \(Q\).  A conservative linearized system has the Hamiltonian form
\[
  \dot z = Lz,\qquad L=JK,
\]
where
\[
  J^*=-J,\qquad K=K^*=D^2{\mathcal H}.
\]
Here \(K\) is the Hessian of the conserved Hamiltonian/Noether functional and
\(J\) is the Bures/Nambu Poisson operator in the chosen chart.

The Feshbach identity for the resolvent is formal and always gives
\[
  P(\lambda-L)^{-1}P
  =
  \left[
    \lambda-L_{PP}
    -
    L_{PQ}(\lambda-L_{QQ})^{-1}L_{QP}
  \right]^{-1}.
\]
This identity alone is not enough to make the reduced dynamics conservative.
The extra condition is compatibility of the \(P/Q\) split with the Hamiltonian
structure.

## Lemma: Symplectic Schur Reduction

Assume the \(P/Q\) split is symplectically block-compatible:
\[
  J=
  \begin{pmatrix}
    J_P&0\\
    0&J_Q
  \end{pmatrix},
  \qquad
  K=
  \begin{pmatrix}
    K_{PP}&K_{PQ}\\
    K_{QP}&K_{QQ}
  \end{pmatrix},
\]
with \(K_{QQ}\) invertible.  Then the zero-frequency Schur reduction of the
Hamiltonian generator is again Hamiltonian:
\[
  L_{PP}-L_{PQ}L_{QQ}^{-1}L_{QP}
  =
  J_P
  \left(
    K_{PP}-K_{PQ}K_{QQ}^{-1}K_{QP}
  \right).
\]

### Proof

Since \(L=JK\),
\[
  L_{PP}=J_PK_{PP},\quad
  L_{PQ}=J_PK_{PQ},\quad
  L_{QP}=J_QK_{QP},\quad
  L_{QQ}=J_QK_{QQ}.
\]
Thus
\[
  L_{PQ}L_{QQ}^{-1}L_{QP}
  =
  J_PK_{PQ}(J_QK_{QQ})^{-1}J_QK_{QP}.
\]
Because
\[
  (J_QK_{QQ})^{-1}=K_{QQ}^{-1}J_Q^{-1},
\]
the middle \(J_Q^{-1}J_Q\) cancels, giving
\[
  L_{PQ}L_{QQ}^{-1}L_{QP}
  =
  J_PK_{PQ}K_{QQ}^{-1}K_{QP}.
\]
Therefore
\[
  L_{PP}-L_{PQ}L_{QQ}^{-1}L_{QP}
  =
  J_P
  \left(
    K_{PP}-K_{PQ}K_{QQ}^{-1}K_{QP}
  \right).
\]
The reduced stiffness
\[
  K_{\rm eff}=K_{PP}-K_{PQ}K_{QQ}^{-1}K_{QP}
\]
is symmetric because it is the Schur complement of a symmetric Hessian.  Hence
the reduced generator is Hamiltonian and conservative. \(\square\)

## Potential Interpretation

The same formula appears by stationary elimination of hidden coherences.  If
\[
  {\mathcal H}(z_P,z_Q)
  =
  {1\over2}
  \begin{pmatrix}z_P\\z_Q\end{pmatrix}^*
  \begin{pmatrix}
    K_{PP}&K_{PQ}\\
    K_{QP}&K_{QQ}
  \end{pmatrix}
  \begin{pmatrix}z_P\\z_Q\end{pmatrix},
\]
then the hidden equilibrium equation is
\[
  \partial_{z_Q}{\mathcal H}=K_{QP}z_P+K_{QQ}z_Q=0,
\]
so
\[
  z_Q=-K_{QQ}^{-1}K_{QP}z_P.
\]
Substitution gives the conservative effective Hamiltonian
\[
  {\mathcal H}_{\rm eff}(z_P)
  =
  {1\over2}z_P^*
  \left(
    K_{PP}-K_{PQ}K_{QQ}^{-1}K_{QP}
  \right)
  z_P.
\]
The Green kernel relevant to a conservative potential is therefore the inverse
of \(K_{\rm eff}\), not the inverse of an arbitrary non-self-adjoint Markov
generator.

## Consequence for Paper 28

The current \(Z_{30}\) projected-resolvent audit used
\[
  L=i[H,\cdot]+D_{\rm dephase}+D_{\rm classical}.
\]
This \(L\) is not of the form \(JK\), because the dephasing and classical
dissipator are symmetric dissipative pieces.  The audit also projected only to
diagonal readout variables, not to a full symplectic physical sector containing
coordinates and conjugate momenta.  Therefore the observed
\[
  R^2_{P(-L)^{-1}P}=0.8797
\]
is a Bures-resolvent signal, not yet a conservative force derivation.

To make the Schur route load-bearing for Paper 28, one must construct a
Hamiltonian/Bures-Nambu finite-row generator satisfying:

1. \(L=JK\) with \(K=D^2{\mathcal H}\) from the cubic Noether/Bures action;
2. a symplectically compatible \(P/Q\) split;
3. \(K_{\rm eff}=K_{PP}-K_{PQ}K_{QQ}^{-1}K_{QP}\) has target-local elliptic
   principal symbol on the physical quotient;
4. the resulting force is
   \[
     F_{\rm eff}=-\nabla{\mathcal H}_{\rm eff},
   \]
   so the dynamics remain conservative.

If these conditions can be met, the Schur localization route becomes
compatible with the conservation theorems.  If not, the \(Z_{30}\) signal
belongs to a neighboring Bures-to-Laplacian program rather than to the proof
spine of Paper 28.

## Finite Hamiltonian Audit

The audit `empirical/hamiltonian_schur_audit.py` now tests the conservative
bridge directly.  It constructs a finite Hamiltonian linear system
\[
  \dot z=Lz,\qquad L=JK,\qquad J^T=-J,\qquad K=K^T,
\]
with physical coordinates \(P\) and hidden coordinates \(Q\).  The physical
block \(K_{PP}\) is chosen to be mean-field/complete, while \(K_{PQ}\) is
chosen by spectral factorization of \(K_{PP}-K_{\rm target}\).  Consequently
\[
  K_{PP}-K_{PQ}K_{QQ}^{-1}K_{QP}
  =
  K_{\rm target}
\]
to numerical precision.

The cleanest connected-row run so far is
`empirical/reports/hamiltonian_schur_audit_z210_hscale75.md`:

| row | target pairs | components | \(R^2(K_{PP}^{-1})\) | \(R^2(K_{\rm eff}^{-1})\) | Hamiltonian defect |
|---:|---:|---:|---:|---:|---:|
| \(210\) | \(5457\) | \(1\) | \(-0.066235\) | \(0.772276\) | \(0\) |

The Schur consistency error is \(2.38\times10^{-15}\), and
\[
  \max |L^TK+KL|=0.
\]
Thus the finite Hamiltonian algebra does **not** obstruct Schur localization:
hidden conservative coordinates can turn a mean-field physical block into a
target-local effective stiffness.

The caveat remains decisive.  This audit proves conservative realizability by
spectral completion.  It does not derive the hidden coupling \(K_{PQ}\) from
CRT/Bures structure, the cubic Noether Hessian, \(K^{CH}(D\eta v,D\eta v)\), or
\(\Pi_{\rm EL}\).  The next bridge is therefore the structured-Hessian problem:
replace the spectral factorization with a conductor-compatible Bures/Nambu
Hessian and test whether its Schur complement retains the target-local
principal symbol.

## Bures Hamiltonian Split Gate

The audit `empirical/bures_hamiltonian_split_audit.py` now tests the missing
\(G_{\rm split}\) gate against the actual Bures/unitary leaf geometry, using
the same `build_xi`, `target_radius`, and target-local pair machinery as the
localization audits.  It constructs a faithful diagonal reference state
\(\rho_*\), verifies the diagonal equilibrium condition, builds the real
off-diagonal unitary-orbit tangent basis, and forms the KKS/Bures Poisson
tensor \(J\) in matrix-unit quadrature blocks.

The default \(Z_{30}\) run reports:

| gate | value |
|---|---:|
| unitary orbit dimension | \(870\) |
| target-local pairs | \(169\) |
| \(\operatorname{cond}(\rho_*)\) | \(14.33825\) |
| \(\|-i[H_{\rm eq},\rho_*]\|\) | \(0\) |
| \(\max|J+J^T|\) | \(0\) |
| \(\operatorname{rank}J\) | \(870\) |

The candidate split outcomes are:

| split | status | \(\dim P\) | \(\operatorname{rank}J_{PP}\) | cross/J | invariance defect |
|---|---|---:|---:|---:|---:|
| diagonal readout | invalid | \(0\) | \(0\) | n/a | n/a |
| target \(q\)-only | fail | \(169\) | \(0\) | \(0.478158\) | \(1\) |
| target symplectic pairs | pass | \(338\) | \(338\) | \(0\) | \(0\) |
| \(\xi\) \(q\)-readout | fail | \(3\) | \(0\) | \(0.064156\) | \(1\) |
| \(\operatorname{span}\{\xi,J\xi\}\) one-step closure | fail | \(6\) | \(6\) | \(0.077499\) | \(0.64949\) |

Thus the clean Hamiltonian Schur identity is **not** available for diagonal
population readout, \(q\)-only target edges, or the naive three-coordinate
\(\xi\) sector.  The only passing finite split is a sector made of complete
matrix-unit quadrature pairs.  This does not prove localization or canonicity;
it only says that the Schur stiffness audit is well-defined on that Darboux
sector.  The next structured-Hessian test must therefore either work in the
passing target-symplectic-pair sector and then define the physical quotient
there, or construct a genuine Darboux physical sector whose observables push
down to the desired \(\xi\) coordinates.  A diagonal shape readout cannot carry
the Hamiltonian Schur bridge by itself.
