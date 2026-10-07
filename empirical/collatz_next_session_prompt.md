# New Session Prompt: Reverse Engineering Collatz via Mixed 2/3 Path Algebra

You are continuing a research/programming thread in `C:\Projects\simplicial`.

Goal: reverse engineer the Collatz conjecture as a finite/inverse arithmetic skeleton problem, not as a continuous dynamical approximation. Keep the work empirical-theorem-facing: make definitions computable, stress-check them, and revise if the algebra points somewhere better.

Core context to keep:

- The 2-adic forward carry program found an exact descent-margin quotient
  `q_w = (r_w(2^S - 3^m) - C_w) / 2^(S+1)`.
  See:
  - `C:\Projects\simplicial\empirical\collatz_margin_theorem_candidate.py`
  - `C:\Projects\simplicial\empirical\reports\collatz_margin_theorem_candidate.md`
  - `C:\Projects\simplicial\empirical\collatz_margin_lattice_miner.py`
  - `C:\Projects\simplicial\empirical\reports\collatz_margin_lattice_L12_S25_K8.md`

- The second-half/no-descent language showed that support-level counting is not enough. The finite bad sets shrink in mass, but the infinite 2-adic support language is nonempty.
  See:
  - `C:\Projects\simplicial\empirical\collatz_no_descent_language.py`
  - `C:\Projects\simplicial\empirical\reports\collatz_no_descent_language_L300.md`
  - `C:\Projects\simplicial\empirical\collatz_closure_deficit_ledger.py`
  - `C:\Projects\simplicial\empirical\reports\collatz_closure_deficit_L120_B14.md`

- The key correction was to flip to the inverse tree. Formal branches
  `D(x)=2x` and `U(x)=(x-1)/3` live naturally in `Z[1/3]`. Honest integer inverse paths require a 3-adic integrality gate and a 2-adic parity gate.
  See:
  - `C:\Projects\simplicial\empirical\collatz_inverse_tree_3adic_audit.py`
  - `C:\Projects\simplicial\empirical\reports\collatz_inverse_tree_3adic_L20.md`
  - `C:\Projects\simplicial\empirical\collatz_mixed_inverse_path_algebra.py`
  - `C:\Projects\simplicial\empirical\reports\collatz_mixed_inverse_path_seed_1_L20.md`
  - `C:\Projects\simplicial\empirical\reports\collatz_mixed_inverse_path_seed_2_L20.md`

- The mixed inverse algebra exposed a gauge: modulo `M=2^a 3^b`, `U` is not same-level closed. A coarse source `r mod M` has three lifts `r`, `r+M`, `r+2M mod 3M`, giving a `Z/3` torsor:
  ```text
  U_t(r) = (r + tM - 1)/3 mod M
  U_{t+delta}(r) = U_t(r) + delta*M/3 mod M
  ```
  Raw `U` closure deficit is `2/3`; gauge-reduced deficit is `0`. The next likely object is gauge holonomy along branch words.

Background papers that motivated the closure/gauge viewpoint:

- `C:\Projects\simplicial\11.quotient_character_adjacency_algebras.md`
  Important ideas: operator-valued adjacency, path algebra, filtered local algebra, support-level vs full-block closure, closure-deficit ledger.
- `C:\Projects\simplicial\12.discrete_fisher_skeletons_for_ai_optimization.md`
  Important ideas: quadratic blindspot, off-centroid finite arithmetic channels, macrovariable closure.
- Old notes for cycle/path-sum sanity checks:
  `C:\Projects\collatz-loops\RESEARCH_NOTES.md`

Known calibration facts:

- In all `Z`, include the five known cycles: `0`, positive `1 -> 4 -> 2 -> 1`, and the three negative cycles. Any global inverse-tree theorem must keep these components separate.
- Do not claim Collatz is proved. Current evidence sharpens the algebra and theorem candidates only.

Suggested milestones, but adjust freely if the math points elsewhere:

1. Formalize the mixed 2/3 inverse path algebra.
   Make the state object explicit: support word, current quotient `2^a3^b`, 3-adic lift phase/gauge, integer gate, parity gate, and relation to the forward carry word.

2. Compute gauge holonomy.
   For branch words, compose gauged `D` and `U_t` operators and record accumulated `Z/3` phase. Compare holonomy signatures against the five integer cycles and against forward carry-cycle sieves.

3. Look for the next theorem candidate.
   Possible shape:
   ```text
   Every infinite honest positive-integer inverse path either lies in the
   inverse basin of the positive 1-4-2 cycle or eventually develops a
   finite 3-adic denominator defect / 2-adic parity defect / nontrivial
   gauge holonomy.
   ```
   This wording is provisional. Improve it if the computations reveal a cleaner invariant.

Operating style:

- Prefer small computable definitions and reports over broad speculation.
- Keep old scripts as evidence, but do not be trapped by them.
- Use Papers 11/12 as conceptual scaffolding, not as a requirement to force terminology.
- Work backwards from “what algebra would make Collatz’s legal paths closed?”
- If a scalar count disagrees with filtered residue/gauge data, trust the filtered data.
