# K^CH Local Step Controller - weekdays / llama31_8b

## Status

- centroid source: `C:\Projects\simplicial\weekdays\baseline\per_class_output_dists.safetensors`
- scenario: `adjacent`
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
- accepted-scale min / median: `0.009516` / `0.018853`
- raw cubic-fraction max / median: `10.298255` / `5.198034`
- controlled cubic-fraction max: `0.098000`

## Step Table

| step | ||s||_F | ||Kss||_F | rho=||Kss||/||s||^2 | cubic frac | scale | controlled frac | min p next | action |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Monday -> Tuesday | 3.119476 | 35.475831 | 3.645603 | 5.686185 | 0.017235 | 0.098000 | 6.394e-03 | damp: cubic correction exceeds trust fraction |
| Tuesday -> Wednesday | 2.611260 | 21.135937 | 3.099712 | 4.047076 | 0.024215 | 0.098000 | 9.025e-03 | damp: cubic correction exceeds trust fraction |
| Wednesday -> Thursday | 2.995887 | 31.145452 | 3.470113 | 5.198034 | 0.018853 | 0.098000 | 1.774e-02 | damp: cubic correction exceeds trust fraction |
| Thursday -> Friday | 2.531800 | 16.959111 | 2.645723 | 3.349220 | 0.029261 | 0.098000 | 1.203e-02 | damp: cubic correction exceeds trust fraction |
| Friday -> Saturday | 3.245691 | 42.425795 | 4.027316 | 6.535711 | 0.014995 | 0.098000 | 5.043e-03 | damp: cubic correction exceeds trust fraction |
| Saturday -> Sunday | 2.960985 | 26.111093 | 2.978191 | 4.409190 | 0.022226 | 0.098000 | 4.434e-03 | damp: cubic correction exceeds trust fraction |
| Sunday -> Monday | 3.711436 | 76.442634 | 5.549472 | 10.298255 | 0.009516 | 0.098000 | 3.486e-03 | damp: cubic correction exceeds trust fraction |

## Mean Conductor Packet Fractions

Fractions use the uniform cyclic character decomposition. They are packet metadata for the arithmetic audit, not the trust-region scaling rule.

| packet | step energy | K^CH response energy |
|---|---:|---:|
| conductor_7 | 1.000000 | 1.000000 |

## Highest Cubic Fractions

| step | raw cubic frac | scale | active limits | curve-corrected min p |
|---|---:|---:|---|---:|
| Sunday -> Monday | 10.298255 | 0.009516 | cubic_fraction | 3.488e-03 |
| Friday -> Saturday | 6.535711 | 0.014995 | cubic_fraction | 5.049e-03 |
| Monday -> Tuesday | 5.686185 | 0.017235 | cubic_fraction | 6.403e-03 |
| Wednesday -> Thursday | 5.198034 | 0.018853 | cubic_fraction | 1.777e-02 |
| Saturday -> Sunday | 4.409190 | 0.022226 | cubic_fraction | 4.443e-03 |

## Reproduction

```powershell
python empirical/k_ch_step_controller.py --preset weekdays --centroids "C:\Projects\simplicial\weekdays\baseline\per_class_output_dists.safetensors" --model-tag llama31_8b --scenario adjacent --max-cubic-fraction 0.1
```
