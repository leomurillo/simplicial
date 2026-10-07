# Conductor-Closed Optimizer Prototype

## Verdict

On this synthetic mixed-output task, the conductor-closed optimizer keeps
the learned logits and the applied K^CH carry response inside the declared
mixed conductor closure up to floating-point noise.  Adam and plain natural
gradient both leak substantial energy into the eight off-closure character
modes created by online one-hot sampling noise.

- final probability leakage reduction vs Adam: `inf`
- final probability leakage reduction vs plain natural gradient: `inf`
- K^CH carry-response leakage reduction vs Adam: `inf`
- K^CH carry-response leakage reduction vs plain natural gradient: `inf`

## Algebra

- label algebra: `F4[u]/(u^2)`, `F4 = F2[w]/(w^2+w+1)`
- output labels: `16`
- closed generators: `1`, `u`, `wu`
- nontrivial closed modes: `u`, `wu`, `(w+1)u`, `1`, `1+u`, `1+wu`, `1+(w+1)u`
- closed nontrivial modes: `7`
- leakage nontrivial modes: `8`

The target natural parameters use both conductor packets:

- mean target logit energy in conductor `u`: `0.517811`
- mean target logit energy in conductor `u^2`: `0.482189`
- target logit leakage: `4.272e-33`
- target probability leakage: `4.407e-33`

## Setup

- seeds: `6`
- contexts: `64`
- online steps per seed: `2500`
- batch size: `128`
- signal scale: `2.4`
- JSON payload: `C:\Projects\simplicial\empirical\reports\conductor_closed_optimizer_f4_u2.json`

The model is a free 16-logit table per context.  Since the population
target is conductor-closed, off-closure Fourier energy measures optimizer
leakage rather than target complexity.  The stochastic labels are one-hot
samples from the closed target distributions.

## Summary

| optimizer | true KL mean | true KL std | final logit leakage | final probability leakage | applied update leakage | K^CH carry leakage |
|---|---:|---:|---:|---:|---:|---:|
| Adam | 0.036156 | 0.002221 | 3.932819e-02 +/- 2.2e-03 | 4.392630e-02 +/- 5.3e-03 | 5.281936e-01 | 5.571452e-01 |
| plain natural gradient | 0.057886 | 0.001652 | 3.580474e-03 +/- 1.4e-04 | 2.805547e-03 +/- 1.5e-04 | 5.239528e-01 | 5.040191e-01 |
| conductor-closed optimizer | 0.023031 | 0.001791 | 4.274725e-33 +/- 3.5e-34 | 4.144935e-33 +/- 4.5e-34 | 4.103962e-33 | 4.140837e-33 |

## Per-Seed Results

| seed | optimizer | true KL | final probability leakage | K^CH carry leakage |
|---:|---|---:|---:|---:|
| 3107 | Adam | 0.038587 | 4.568920e-02 | 5.534302e-01 |
| 3107 | plain natural gradient | 0.059254 | 2.829996e-03 | 5.037288e-01 |
| 3107 | conductor-closed optimizer | 0.025752 | 4.253861e-33 | 4.249431e-33 |
| 3108 | Adam | 0.035225 | 4.992886e-02 | 5.430770e-01 |
| 3108 | plain natural gradient | 0.055594 | 2.957592e-03 | 5.029513e-01 |
| 3108 | conductor-closed optimizer | 0.021095 | 5.007694e-33 | 4.164576e-33 |
| 3109 | Adam | 0.035593 | 4.392031e-02 | 5.653744e-01 |
| 3109 | plain natural gradient | 0.057944 | 2.994200e-03 | 5.054226e-01 |
| 3109 | conductor-closed optimizer | 0.022061 | 3.976069e-33 | 4.158427e-33 |
| 3110 | Adam | 0.033125 | 3.786869e-02 | 5.636493e-01 |
| 3110 | plain natural gradient | 0.060618 | 2.756302e-03 | 5.086483e-01 |
| 3110 | conductor-closed optimizer | 0.022378 | 4.109809e-33 | 4.103470e-33 |
| 3111 | Adam | 0.039563 | 4.989755e-02 | 5.555282e-01 |
| 3111 | plain natural gradient | 0.056804 | 2.531683e-03 | 5.016310e-01 |
| 3111 | conductor-closed optimizer | 0.021664 | 3.997484e-33 | 4.092963e-33 |
| 3112 | Adam | 0.034846 | 3.625317e-02 | 5.618124e-01 |
| 3112 | plain natural gradient | 0.057103 | 2.763509e-03 | 5.017328e-01 |
| 3112 | conductor-closed optimizer | 0.025237 | 3.524697e-33 | 4.076152e-33 |

## Interpretation

This is a prototype, not yet a general optimizer package.  The positive
result is that the conductor projection is doing real work on a mixed local
row: it suppresses both final off-closure probability energy and the
second-order K^CH carry response while remaining competitive on population
KL in this finite-sample regime.

The important control is that the target itself has essentially zero
off-closure leakage while using both tame and wild packets.  Plain Adam
and plain natural gradient therefore leak because of their update rule
under stochastic labels, not because the task secretly requires those
modes.

## Reproduction

```powershell
python empirical/conductor_closed_optimizer.py
```
