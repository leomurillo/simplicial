# HPo Notes - KU-3 Hilbert-Polya on the Z/6 Bures Lift

Session date: 2026-05-22  
Workspace: `C:\Projects\simplicial`

## Executive Status

KU-3 was executed through the six requested moves. The existing Bures
K-cumulant tower probe reconfirmed the universal identity at the first five
zeta zeros. Four explicit self-adjoint finite Bures-basis Hamiltonian families
were constructed and diagonalized, with a final structural parameter sweep.

Outcome: **informative failure for finite C6 / C6 x C2 matrices as the full
Hilbert-Polya operator**. Several tuned finite spectra can approximate the
first few ordinates after affine rescaling, but none gives the zeta spectrum
structurally, and no finite matrix can have the infinite Riemann-von Mangoldt
counting law. The durable conclusion is that `Z/6` is a canonical **fiber /
carrier of the K-involution and cumulant tower**, not by itself the whole
spectral Hilbert space. A viable KU-3 continuation must use an infinite
envelope such as a direct integral, semilocal adelic/prolate space, or
Hurwitz-channel completion with `C6` as internal fiber.

No `doce.md` was created because there was no strong success.

## Move 0 - Baseline Verification

Command:

```powershell
python empirical\probe_A2_cumulant_tower.py
```

Result: confirmed

$$
\kappa_n^K(\rho)\zeta(\rho)^n = (-1)^n (n-1)! B_G(\rho)^n
$$

for `n = 2..6` at the first five nontrivial zeros. Ratios were
`1 +/- 1e-5`. The off-zero control at `s = 1/2 + 18i` was wildly non-1,
reconfirming the identity is zero-locus-specific.

## Move 1 - External Literature Survey

Modern frontier found by web/arXiv search:

| Line | Operator Type | Domain | Frontier / Breakdown |
|---|---|---|---|
| Bender-Brody-Muller 2017, [arXiv:1608.03679](https://arxiv.org/abs/1608.03679) | PT-symmetric Hamiltonian, classical limit `2xp` | Infinite-dimensional differential operator | Eigenvalues correspond to zeros if boundary conditions hold; operator not conventionally Hermitian; self-adjoint metric/domain remains the load-bearing gap. |
| Yakaboylu 2022, [arXiv:2211.01899](https://arxiv.org/abs/2211.01899) | Formally self-adjoint Hamiltonian coupling Berry-Keating to number operator | Two-dimensional/half-line limit | Formal self-adjointness under a boundary condition; rigor of boundary/domain preservation is open. |
| Yakaboylu 2024, [arXiv:2309.00405](https://arxiv.org/abs/2309.00405) | Hamiltonian whose eigenfunctions vanish by zeta zeros | Positive half-line | If self-adjoint/real-spectrum, RH follows; proof hinges on similarity transform and boundary-condition domain. |
| Yakaboylu 2024-2026, [arXiv:2408.15135](https://arxiv.org/abs/2408.15135) | Non-symmetric operator `R`, compressed zero subspace, positive intertwiner `W` | `L^2([0,infty))` | Moves toward pseudo-Hermitian/self-adjoint operator via positivity condition; uses zero-defined spectral subspace, so circularity/domain issues must be watched. |
| Connes-Consani-Moscovici 2024, [Zeta zeros and prolate wave operators](https://alainconnes.org/2024/02/from-rings-of-operators-to-noncommutative-geometry/) | Semilocal prolate operator in trace-formula framework | Semilocal/adelic Hilbert spaces | Spectral realization of low zeros and UV behavior; not a finite matrix, and framed as trace/prolate spectral realization rather than a direct elementary HP proof. |
| Hateley 2025, [arXiv:2511.18309](https://arxiv.org/abs/2511.18309) | Chiral adelic Dirac operator with prime-indexed mass deformation | Idele class space / Floquet background | Zeros appear as spectral-shift discontinuities rather than raw eigenvalues; finite-prime truncations are computable but distributional. |
| Anukool et al. 2026, [INSPIRE record](https://inspirehep.net/literature/3103567) | Acceleration-dependent Hamiltonian `H_BK + beta H_a` | Extended phase-space differential operator | Studies spectral discreteness/self-adjoint realizations; no exact zeta spectrum established. |
| Karazoupis 2025, [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5196327) | Finite-dimensional deterministic matrix model with prime data | Finite matrices | Statistical/random-matrix style approximation; not an exact Hilbert-Polya operator and not Bures/cyclic `Z/6`. |

Negative search result: I found no modern paper using Bures geometry, cyclic
group quotients, or a finite-dimensional `Z/6` carrier to produce an exact
Hilbert-Polya operator. Finite-dimensional proposals are statistical models,
not exact spectrum identities.

## Moves 2-3 - Internal Knowledge and Log Grep

Important internal hints:

- `nueve.md` Section 6 gives the Bures lift on `Z/6`, K-involution
  `r -> -r mod 6` plus conjugation, Bures amplitude `B_G(s)`, and the
  universal K-cumulant tower.
- `nueve.md` Sections 6.5-6.6 explicitly warn that the identity holds at every
  nontrivial zero, on-line or hypothetically off-line; finite-`Q` cumulant
  data alone does not discriminate RH.
- `05.simplicial_cyclotomic_riemann_interfaces.md` already states the
  Hilbert-Polya gap correctly: one must specify a Hilbert space, an operator
  with controlled trace/determinant, a limiting procedure, and FE-compatible
  spectral symmetry.
- `27.finite_to_archimedean_noether_limits_and_canonical_involution.md`
  supplies the canonical Bures anti-unitary involution on
  `C^2 tensor C^3 ~= C^6`, implementing finite spectral inversion.
- `44_quantization_forced_cubic_to_bures_bridge.md` supplies the explicit
  Bures metric/cubic tensor and `su(2) + su(3)` generator layer on `C^6`.
- The `.claude/worktrees/musing-pascal-4e9c9d` log layer largely duplicated
  the promoted manuscripts and added no stronger hidden HP operator. It did
  reinforce the `N=4` wedge-Hodge identity `K(u)^3=-K(u)` and the finite
  Fourier/cyclic spectral toolkit.

Internal synthesis: the corpus has all ingredients for a **fiberwise
anti-unitary symmetry** but not an existing construction of the infinite
spectral direction needed to carry all ordinates.

## Move 4 - Candidate Hamiltonians

All matrices below are in the Bures basis
`|0>, |1>, |2>, |3>, |4>, |5>` unless explicitly doubled.

Common definitions:

- `P_K |r> = |-r mod 6>`, and antiunitary `K = P_K C`.
- `F_6` is the unitary DFT.
- `P_6 = F_6 diag(0,1,2,-3,-2,-1) F_6^*`, the finite cyclic momentum.
- `X_6 = diag(r - 5/2) / sqrt(mean((r - 5/2)^2))`.
- `G_bal` is the canonical Hermitian observable used in `probe_A2`:

$$
G_{00}=1,\quad G_{11}=-1,\quad G_{22}=1/2,\quad G_{33}=-1/2,
$$

with off-diagonal entries
`G_{01}=G_{10}=0.3`, `G_{23}=G_{32}=0.2`, `G_{02}=G_{20}=0.1`.

### Family A - Berry-Keating xp

Finite cyclic compression:

$$
H_{A,circ}=\frac12(X_6P_6+P_6X_6).
$$

Hurwitz-channel compression:

Use channels

$$
f_0(t)=6^{-s},\qquad f_r(t)=6^{-s}\zeta(s,r/6),\quad s=1/2+it,
$$

and least-squares project multiplication by `t` and `-i d/dt` onto their
six-dimensional span on `t in [7,62]`. Then

$$
H_{A,Hurwitz}=\frac12(X_tP_t+P_tX_t).
$$

### Family B - K-Hermitian / BBM-style

Finite commutator candidate:

$$
H_B(\lambda)= i[G_{bal},P_6]+\lambda\,\frac{G_{bal}+G_{bal}^K}{2}.
$$

Hurwitz Bures-amplitude candidate:

Project multiplication by `B_G(t)` and `d_s=-i d/dt` onto the same Hurwitz
channel span:

$$
H_{B,Hurwitz}=
\operatorname{Herm}\{i(B_G d_s-d_sB_G)\}
\lambda\,\frac{G_{bal}+G_{bal}^K}{2}.
$$

Control:

$$
A_{Kodd}=\operatorname{diag}(0,1,1,0,-1,-1),\qquad
H_{B,ctrl}=i[A_{Kodd},P_6].
$$

### Family C - Cumulant-Tower Generator

Linear K-mark shadow:

$$
A_K(G)=\frac12(P_KG+GP_K).
$$

Finite cumulant generator:

$$
H_C(\alpha,\beta)
=\alpha\,\frac12(P_6A_K(G_{bal})+A_K(G_{bal})P_6)
\beta\,\frac12(P_6A_K(A_{Kodd})+A_K(A_{Kodd})P_6).
$$

Hurwitz version replaces `P_6` by projected `P_t`.

Rate-shadow control:

$$
H_{C,rate}=\operatorname{Herm}\left(\frac{G^KG+GG^K}{2}\right).
$$

### Family D - Stella-Octangula / Janus Doubling

On `C^6 tensor C^2`, with Pauli matrices `sigma_x,sigma_y,sigma_z`,

$$
H_D(\alpha,\beta,\mu)
=\alpha\,H_B^{(0)}\otimes\sigma_z
\beta\,(A_K(G_{bal})+A_K(A_{Kodd}))\otimes\sigma_x
\mu\,P_6\otimes\sigma_y,
$$

where `H_B^(0)=i[G_bal,P_6]`. The intended Janus time reversal is
`K_J=(P_K tensor sigma_x) C`.

## Move 5 - Numerical Verification

Scripts added:

- `empirical/hpo_common.py`
- `empirical/probe_HPo_FamilyA_berry_keating.py`
- `empirical/probe_HPo_FamilyB_K_hermitian.py`
- `empirical/probe_HPo_FamilyC_cumulant_generator.py`
- `empirical/probe_HPo_FamilyD_stella_octangula.py`
- `empirical/probe_HPo_parameter_sweep.py`

### Projection Residuals

The literal Hurwitz-channel projections are not closed:

| Projected operation | Relative residual |
|---|---:|
| `d/dt` | `4.379829e-01` |
| multiplication by `t` | `3.957107e-01` |
| multiplication by `B_G(t)` | `4.908962e-01` |

This is a major structural obstruction for Families A/B in finite channel
form: the requested differential operators leak out of the six-channel span.

### Raw Candidate Results

| Family | Dim | Self-adjoint? | Best raw/structural comparison |
|---|---:|---:|---|
| A.1 cyclic BK | 6 | yes | Eigenvalues `+-2.0403, +-0.8657, +-0.2575`; best affine full-spectrum rms `1.1467`. |
| A.2 Hurwitz BK | 6 | yes | Projection residuals large; all eigenvalues negative; best affine rms `1.9224`. |
| B.1 finite K-Hermitian | 6 | yes | Best positive-branch affine rms `1.0592`; not exact. |
| B.2 Hurwitz Bures commutator | 6 | yes | Best positive-branch affine rms `0.8650`; projection residuals large. |
| B.3 K-odd diagonal control | 6 | yes, K-Hermitian defect `6.7e-15` | Symmetric finite spectrum; best full affine rms `1.7062`. |
| C.1 finite cumulant generator | 6 | yes, K-Hermitian defect `3.6e-15` | Best full affine rms `1.3782`. |
| C.2 Hurwitz cumulant generator | 6 | yes | Best full affine rms `0.6168`; projection residuals large. |
| C.3 rate shadow | 6 | yes, K-Hermitian exact | Two positive eigenvalues can be fit exactly to two zeros only; no spectrum. |
| D.1 Janus doubled | 12 | yes | Best positive-branch affine rms `2.4344`; Janus defect large. |
| D.2 doubled block | 12 | yes | Best positive-branch affine rms `1.7875`; finite doubled symmetry only. |

### Free-Coefficient Sweep

The sweep sampled 5000 random normalized structural coefficient vectors for
Families B-D and then applied the best affine map `gamma ~= a lambda + b`.

| Family | Best branch | Coefficients | Fit count | RMS | Max error | Interpretation |
|---|---|---|---:|---:|---:|---|
| B | full | `(-0.482794, +0.871526, +0.085749)` | 6 | `0.0555915` | `0.0934791` | Good six-point numerical fit after 3 structural coefficients plus affine scale/shift; not structural/no-tuning and cannot extend past 6 eigenvalues. |
| C | full | `(+0.882029, -0.137292, -0.450750)` | 6 | `1.04694` | `1.76325` | No good fit. |
| D | full | `(-0.190294, -0.869116, -0.456537)` | 12 | `0.417762` | `0.850578` | Moderate finite fit after tuning; not exact and no density. |

The Family B sweep is the most interesting numerical trace. It is still
classified as a tuning artifact: with a 6-dimensional matrix, three structural
coefficients plus affine rescaling can shape six ordered eigenvalues. It does
not produce the remaining zeros, the Riemann-von Mangoldt law, or an analytic
eigenvalue equation.

### Counting Law Check

Every finite matrix saturates:

$$
N_H(T) \leq \dim H.
$$

But the zeta ordinates obey

$$
N_\zeta(T)=\frac{T}{2\pi}\log\frac{T}{2\pi}-\frac{T}{2\pi}+O(\log T),
$$

which is unbounded. Thus a bare self-adjoint operator on `C^6` or
`C^6 tensor C^2` cannot have spectrum `{gamma_n}_{n>=1}`. The only viable
reading of "Bures envelope of C6" is an infinite Hilbert space with a `C6`
internal Bures fiber.

## Move 6 - Proof Status

Self-adjointness:

- Families A-D are self-adjoint by Hermitian symmetrization or by `i` times a
  commutator of Hermitian matrices.
- Some controls are also exactly K-Hermitian/pseudo-Hermitian under `K`.

Spectrum identity:

- No candidate satisfies
  `H psi_rho = gamma_rho psi_rho` for every zero.
- The cumulant-tower identity supplies a fiberwise exponential cgf at zeros,
  but it does not determine the global spectral counting direction.
- The finite-dimensional candidates cannot satisfy the infinite spectrum
  identity for dimensional reasons.

Conclusion: KU-3 closes **negatively for the finite-matrix interpretation** and
redirects to an infinite Bures-fiber Hilbert space. This is not a rejection of
the `Z/6` carrier; it clarifies its role.

## Next KU-3 Attack Surface

The next serious candidate should be:

$$
\mathcal H = L^2(\mathbb R_+, dx/x)\otimes \mathbb C^6
$$

or a semilocal/adelic prolate space with `C6` Bures fiber. The operator should
look like a Berry-Keating/Connes/prolate dilation generator on the base, with
the `Z/6` K-involution acting fiberwise:

$$
\widehat H =
\frac12(xp+px)\otimes I_6
+ \text{prime/Bures fiber potential}
$$

where the fiber potential is built from `B_G`, `P_K`, and the
K-cumulant tower. The target is then not a `6 x 6` matrix spectrum, but a
trace formula or spectral determinant:

$$
\det(\widehat H - t) \sim \xi(1/2+it).
$$

That is where the internal `Z/6` structure can plausibly meet the unbounded
Riemann-von Mangoldt density.
