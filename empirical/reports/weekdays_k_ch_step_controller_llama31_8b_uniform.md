# K^CH Local Step Controller - weekdays / llama31_8b

## Status

- centroid source: `C:\Projects\simplicial\weekdays\baseline\per_class_output_dists.safetensors`
- scenario: `uniform`
- step count: `7`
- max cubic fraction: `0.100000`
- max Fisher norm: `none`
- min probability: `1.000e-09`
- cyclic conductor packet audit: `on`

The controller accepts a proposed output-simplex step `s`, computes

```text
K^CH_p(s)s = s*s/p - <s,s>_p p
cubic_fraction = 0.5 ||K^CH_p(s)s||_p / ||s||_p
```

and shrinks the step when the cubic fraction exceeds the configured trust target. The optional curve-correction vector is reported but not applied as the default optimizer action.

## Summary

- damped steps: `7` / `7`
- accepted-scale min / median: `0.044644` / `0.056232`
- raw cubic-fraction max / median: `2.195129` / `1.742771`
- controlled cubic-fraction max: `0.098000`

## Step Table

| step | ||s||_F | ||Kss||_F | rho=||Kss||/||s||^2 | cubic frac | scale | controlled frac | min p next | action |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| uniform -> Monday | 1.538150 | 3.894512 | 1.646098 | 1.265973 | 0.077411 | 0.098000 | 1.323e-01 | damp: cubic correction exceeds trust fraction |
| uniform -> Tuesday | 1.750098 | 6.100042 | 1.991627 | 1.742771 | 0.056232 | 0.098000 | 1.353e-01 | damp: cubic correction exceeds trust fraction |
| uniform -> Wednesday | 1.712557 | 5.878533 | 2.004374 | 1.716303 | 0.057099 | 0.098000 | 1.357e-01 | damp: cubic correction exceeds trust fraction |
| uniform -> Thursday | 1.813828 | 6.611193 | 2.009499 | 1.822443 | 0.053774 | 0.098000 | 1.358e-01 | damp: cubic correction exceeds trust fraction |
| uniform -> Friday | 1.978130 | 7.929679 | 2.026497 | 2.004337 | 0.048894 | 0.098000 | 1.361e-01 | damp: cubic correction exceeds trust fraction |
| uniform -> Saturday | 1.763144 | 6.060847 | 1.949656 | 1.718762 | 0.057018 | 0.098000 | 1.350e-01 | damp: cubic correction exceeds trust fraction |
| uniform -> Sunday | 2.157222 | 9.470762 | 2.035145 | 2.195129 | 0.044644 | 0.098000 | 1.366e-01 | damp: cubic correction exceeds trust fraction |

## Mean Conductor Packet Fractions

Fractions use the uniform cyclic character decomposition. They are packet metadata for the arithmetic audit, not the trust-region scaling rule.

| packet | step energy | K^CH response energy |
|---|---:|---:|
| conductor_7 | 1.000000 | 1.000000 |

## Highest Cubic Fractions

| step | raw cubic frac | scale | active limits | curve-corrected min p |
|---|---:|---:|---|---:|
| uniform -> Sunday | 2.195129 | 0.044644 | cubic_fraction | 1.372e-01 |
| uniform -> Friday | 2.004337 | 0.048894 | cubic_fraction | 1.366e-01 |
| uniform -> Thursday | 1.822443 | 0.053774 | cubic_fraction | 1.363e-01 |
| uniform -> Tuesday | 1.742771 | 0.056232 | cubic_fraction | 1.358e-01 |
| uniform -> Saturday | 1.718762 | 0.057018 | cubic_fraction | 1.355e-01 |

## Reproduction

```powershell
python empirical/k_ch_step_controller.py --preset weekdays --centroids "C:\Projects\simplicial\weekdays\baseline\per_class_output_dists.safetensors" --model-tag llama31_8b --scenario uniform --max-cubic-fraction 0.1
```
