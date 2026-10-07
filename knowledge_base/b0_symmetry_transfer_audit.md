# B4 Symmetry-Premium Transfer Criterion

Created: 2026-05-14

B4 connects B3 to an A0-style policy decision: when should a prediction engine
pay for symmetry-complete support rather than minimal subgroup support?

## Criterion

Let \(S\) be the source reciprocal support and let held-out tasks be drawn from
a normalizer-transfer distribution on \(\Gamma.S\).  Let

```text
D(S)       = <S> \ {0}
D^Gamma(S) = <Gamma.S> \ {0}
```

B3 is worth its symmetry premium exactly when

```text
E[ structural_cost(D(S), target) - structural_cost(D^Gamma(S), target) ]
>
lambda_resource * ( resource(D^Gamma(S)) - resource(D(S)) ).
```

Equivalently: pay for symmetry completion when expected transfer gain exceeds
the resource-weighted symmetry premium.

## Exact Audit

Implemented:

- `empirical/normalizer_transfer_audit.py`
- `empirical/reports/normalizer_transfer_audit.md`
- `empirical/reports/normalizer_transfer_audit.json`

The audit fixes a source support, samples held-out supports from its normalizer
orbit, and compares:

- `source_minimal`: B2 subgroup closure of the source support;
- `source_normalizer`: B3 normalizer saturation of the source support;
- `oracle_minimal`: B2 subgroup closure of the held-out target support;
- `full`: buy everything.

## First Results

Cyclic rows have zero symmetry premium, so B2 and B3 coincide.

Local rows show the real policy split:

| row | B3 beats B2 rate | mean structural gain | mean premium | mean net gain |
|---|---:|---:|---:|---:|
| `F4[u]/(u^2)` | `0.812` | `1.498377` | `0.167708` | `1.330668` |
| `F2[u]/(u^4)` | `0.799` | `1.398391` | `0.168229` | `1.230162` |

For these transfer distributions, B3 easily pays for itself.  On fixed tasks,
B2 remains cheaper.  This is the first concrete A0 policy rule:

> choose minimal subgroup descent for fixed-support prediction; choose
> normalizer saturation when the deployment distribution ranges over symmetry
> equivalents and the expected transfer gain exceeds the symmetry premium.

## A0 Reading

This is where information investment becomes conditional rather than absolute.
The "optimal discretization" depends on the deployment distribution:

- fixed task: minimize closure support;
- symmetric transfer family: buy symmetry saturation;
- unknown family: estimate the premium/gain frontier.

That is the shape of universal information-investment modeling: not one basis
for everything, but a rule for when additional structure is worth its cost.
