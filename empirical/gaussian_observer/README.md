# Gaussian observer reproducibility package

Standalone author calculations, October 10, 2026. This directory supports the
Gaussian-observer derivation note; it does not modify Paper 60 or other papers.

## Reproduce

From `C:\Projects\simplicial`, with Python 3.12 and the pinned dependencies:

```powershell
python empirical\gaussian_observer\verify.py
python empirical\gaussian_observer\optimize.py --case all --seeds 7 23
```

The verifier is the quick reproduction path. It validates archived candidates,
checks independent ODE and direct Gaussian calculations, and audits the blanket
condition. The optimization command is slower and repeats stochastic numerical
searches. Different BLAS implementations or library versions may change their
last digits or search paths. Neither optimizer success nor agreement between
seeds establishes global optimality.

Dependencies were available in the working Python environment. No installation
or global environment changes were performed for this package.

## Files and outputs

- `model.py`: exact covariance, work, visibility, port, and rotation-frontier
  formulas; full-precision candidate parameters recovered from the chat.
- `verify.py`: ten check groups with stated tolerances. Independent covariance
  ODE integration and a Van Loan block exponential supplement formula replay.
- `optimize.py`: bounded differential evolution followed by constrained local
  polishing. Settings, feasibility, and optimizer status are saved.
- `runs/<UTC timestamp>/`: immutable-per-invocation audit log and JSON results,
  including source hashes and software versions. Failures are preserved.
- `optimization_runs/<UTC timestamp>/`: search settings and per-seed candidates.

## Scope that must accompany the numbers

1. The three-coordinate initial law is `N(0,T K^-1)`, not an exactly reset memory.
2. The inferred target is the initial residual `sqrt(3/T)*(e0+4*b0/3)`.
3. The physical model uses overdamped, equal-temperature independent baths.
4. Active covariance evolves; it is not replaced by a thermal covariance.
5. Work is reference-averaged mechanical actuation, excluding actuator and
   mobility-switch hardware and initial signal preparation.
6. The fixed acquisition/search windows, deadline, stiffness budget, and drive
   limit are part of each comparison. Gated systems have a prescheduled control.
7. Check C09 verifies that the selected active witness does **not** preserve the
   passive static Markov blanket. This is a scope correction, not a failed test.
8. The rotational frontier concerns an already available input register and
   deterministic rotation schedules. It is not the original observer's total
   acquisition/work frontier.
9. A sampled inequality check is evidence for implementation consistency; the
   proof in the derivation note establishes the mathematical statement.
10. All numbers are model calculations, not experimental observations or an
    independent peer review.

See the standalone derivation note and claim contract in the repository root
for proofs, provenance, limitations, and the proposed next research question.

## Recorded runs

- First audit: `runs/20261010T174925_244752Z/`, 10/10 check groups passed
  without checker repair. The active blanket diagnostic is part of the result.
- Repeat optimization: `optimization_runs/20261010T175019_508844Z/`, seven
  cases with seeds 7 and 23, 250 differential-evolution iterations allowed per
  seed. All fourteen candidates met the numerical work-budget tolerance.
