# Projection-Strength Pareto Sweep

## Verdict

The conductor tax curve is sharp on this synthetic F4[u]/(u^2) row.
Fractional projection reduces leakage smoothly, and the sweep separates
the useful closure mechanism from unnecessary projection strength.  In
this run, the best KL setting is reported below rather than assumed.

- no projection KL / K^CH leakage: `0.036156` / `0.557145`
- full projection KL / K^CH leakage: `0.023031` / `4.141e-33`
- best KL setting: gradient `0%`, update `100%`, KL `0.014998`
- best nonzero-leak KL setting: gradient `0%`, update `75%`, K^CH leakage `0.158571`

## Target Control

- target logit leakage: `4.272e-33`
- target probability leakage: `4.407e-33`
- mean target conductor `u` energy: `0.517811`
- mean target conductor `u^2` energy: `0.482189`

## Setup

- contexts: `64`
- online steps: `2500`
- batch size: `128`
- closed Adam-style learning rate: `0.08`
- JSON payload: `C:\Projects\simplicial\empirical\reports\conductor_projection_pareto_f4_u2.json`

Projection is applied fractionally as

```text
x <- (1-rho) x + rho P_closed x
```

separately for the stochastic gradient and the Adam-style update.  Logits
are not hard-projected after partial steps, so the intermediate rows are
real leakage/accuracy tradeoffs rather than hidden 100% projections.

## Symmetric Tax Curve

| projection | true KL mean | final probability leakage | applied update leakage | K^CH carry leakage |
|---:|---:|---:|---:|---:|
| 0% | 0.036156 +/- 0.002221 | 4.392630e-02 | 5.281936e-01 | 5.571452e-01 |
| 25% | 0.031080 +/- 0.001437 | 2.976707e-02 | 2.612556e-01 | 4.702883e-01 |
| 50% | 0.026869 +/- 0.001406 | 1.614337e-02 | 6.563269e-02 | 1.938763e-01 |
| 75% | 0.024039 +/- 0.001645 | 5.119562e-03 | 4.490698e-03 | 1.897822e-02 |
| 100% | 0.023031 +/- 0.001791 | 4.144935e-33 | 4.103962e-33 | 4.140837e-33 |

## Full Gradient/Update Grid

| gradient projection | update projection | true KL mean | final probability leakage | K^CH carry leakage |
|---:|---:|---:|---:|---:|
| 0% | 0% | 0.036156 | 4.392630e-02 | 5.571452e-01 |
| 0% | 25% | 0.030856 | 3.306252e-02 | 5.340435e-01 |
| 0% | 50% | 0.025559 | 2.209036e-02 | 4.052387e-01 |
| 0% | 75% | 0.020295 | 1.129854e-02 | 1.585710e-01 |
| 0% | 100% | 0.014998 | 4.177920e-33 | 4.145553e-33 |
| 25% | 0% | 0.035726 | 3.969136e-02 | 5.516738e-01 |
| 25% | 25% | 0.031080 | 2.976707e-02 | 4.702883e-01 |
| 25% | 50% | 0.026438 | 1.986156e-02 | 3.078214e-01 |
| 25% | 75% | 0.021841 | 1.018496e-02 | 1.045400e-01 |
| 25% | 100% | 0.017221 | 4.290347e-33 | 4.081090e-33 |
| 50% | 0% | 0.034125 | 3.237960e-02 | 4.652277e-01 |
| 50% | 25% | 0.030478 | 2.414328e-02 | 3.437559e-01 |
| 50% | 50% | 0.026869 | 1.614337e-02 | 1.938763e-01 |
| 50% | 75% | 0.023308 | 8.314584e-03 | 5.878731e-02 |
| 50% | 100% | 0.019737 | 4.269968e-33 | 4.181400e-33 |
| 75% | 0% | 0.030177 | 1.961166e-02 | 2.194760e-01 |
| 75% | 25% | 0.028108 | 1.472549e-02 | 1.373810e-01 |
| 75% | 50% | 0.026081 | 1.001959e-02 | 6.736615e-02 |
| 75% | 75% | 0.024039 | 5.119562e-03 | 1.897822e-02 |
| 75% | 100% | 0.022023 | 4.260273e-33 | 4.115395e-33 |
| 100% | 0% | 0.023031 | 4.200104e-33 | 4.146132e-33 |
| 100% | 25% | 0.023031 | 4.143659e-33 | 4.089125e-33 |
| 100% | 50% | 0.023031 | 4.170569e-33 | 4.126383e-33 |
| 100% | 75% | 0.023031 | 4.220536e-33 | 4.145847e-33 |
| 100% | 100% | 0.023031 | 4.144935e-33 | 4.140837e-33 |

## Reading

Both projection sites matter, but they do different engineering jobs.
Update-side projection gives a direct monotone closure control even when
the gradient is left noisy.  Gradient-side projection changes the internal
Adam moments and can itself close this particular row when taken to 100%.
The practical primitive suggested by the sweep is therefore not automatic
'project everything'; it is a tunable conductor filter whose best setting
should be selected against the KL/leakage Pareto curve.

## Reproduction

```powershell
python empirical/conductor_closed_optimizer.py --pareto-sweep
```
