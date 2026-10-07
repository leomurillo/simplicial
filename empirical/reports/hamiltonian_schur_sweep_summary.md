# Hamiltonian Schur Sweep Summary

The Hamiltonian audit constructs a finite conservative system
\[
  \dot z=Lz,\qquad L=JK,\qquad J^T=-J,\qquad K=K^T,
\]
with a physical coordinate block \(P\) and hidden coordinate block \(Q\).  It
chooses \(K_{PQ}\) by spectral factorization of \(K_{PP}-K_{\rm target}\), so
the stiffness Schur complement satisfies
\[
  K_{\rm eff}
  =
  K_{PP}-K_{PQ}K_{QQ}^{-1}K_{QP}
  =
  K_{\rm target}
\]
to numerical precision.

| row | h scale | target components | target pairs | complete R2 | Schur R2 | relative Schur error | Hamiltonian defect |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 30 | 4.0 | 2 | 44 | -0.351598 | 0.702735 | 2.71e-15 | 0 |
| 30 | 7.0 | 1 | 169 | 0.200676 | 0.678263 | 1.65e-15 | 0 |
| 30 | 8.0 | 1 | 281 | -0.043614 | 0.249277 | 1.07e-15 | 0 |
| 210 | 6.0 | 1 | 2437 | -0.019893 | 0.311886 | 2.16e-15 | 0 |
| 210 | 7.0 | 1 | 3617 | -0.080825 | 0.747328 | 2.32e-15 | 0 |
| 210 | 7.5 | 1 | 5457 | -0.066235 | 0.772276 | 2.38e-15 | 0 |
| 210 | 8.0 | 1 | 5841 | -0.000327 | 0.734242 | 2.52e-15 | 0 |

Interpretation: the conservative Schur bridge is algebraically viable.  The
uneliminated physical stiffness \(K_{PP}\) is mean-field and has a flat
off-source Green kernel, while the hidden-coordinate Schur complement can
recover a target-local stiffness with a substantially more \(1/r\)-like Green
kernel.  The \(Z_{210}\), `h_scale=7.5` run is the cleanest connected-row
signal in this sweep.

Caveat: this is a finite conservative existence construction.  It does not
derive \(K_{PQ}\) from CRT/Bures structure, \(K^{CH}(D\eta v,D\eta v)\), or
\(\Pi_{\rm EL}\).  The next task is to replace spectral completion with a
structured Bures/Nambu Hessian whose Schur complement has the same behavior.
