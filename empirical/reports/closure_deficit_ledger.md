# Rosas Closure-Deficit Ledger

This report normalizes the finite coboundary residuals already computed
for the local Ext_CH rows.  For a chosen section-change model, the
closure deficit is

\[
\delta=\frac{\text{residual support}}{\text{raw carry support}}.
\]

Thus \(\delta=0\) means the raw carry is section-trivial in that
model, while \(\delta=1\) means every raw carry atom survives.  The
full-block and support-projection columns are deliberately separated:
support closure alone can miss the filtered adjacency-algebra class.

| row | raw atoms | raw pairs | pair orbits | full field | full residual dim | full delta | support delta | reading |
|---|---:|---:|---:|---|---:|---:|---:|---|
| F_4[u]/(u^2) | 1569 | 369 | 20 | Q | 73116 | 1.000 | n/a | full-block residual survives |
| F_2[u]/(u^5) | 19140 | 2516 | 81 | Q | 728381 | 1.000 | 0.000 | full-block survives; support projection closes |
| F_8[u]/(u^2) | 158081 | 7105 | 49 | F_1000003 | 25752440 | 1.000 | 0.000 | full-block survives; support projection closes |

## Paper-facing use

The ledger turns the Rosas closure audit into a quantitative task.
The F4[u]/(u^2), F2[u]/(u^5), and F8[u]/(u^2) full-block rows
all have delta 1, so their carries are not artifacts of the chosen
filtered section.  The F2[u]/(u^5) and F8[u]/(u^2)
support-projection rows have delta 0, showing that support-level
compression is too coarse to certify filtered closure.
