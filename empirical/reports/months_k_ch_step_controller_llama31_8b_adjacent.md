# K^CH Local Step Controller - months / llama31_8b

## Status

- centroid source: `C:\Projects\simplicial\months\baseline\per_class_output_dists.safetensors`
- scenario: `adjacent`
- step count: `12`
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

- damped steps: `12` / `12`
- accepted-scale min / median: `0.001737` / `0.003443`
- raw cubic-fraction max / median: `56.426979` / `28.638678`
- controlled cubic-fraction max: `0.098000`

## Step Table

| step | ||s||_F | ||Kss||_F | rho=||Kss||/||s||^2 | cubic frac | scale | controlled frac | min p next | action |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| January -> February | 4.657216 | 106.630141 | 4.916174 | 11.447841 | 0.008561 | 0.098000 | 4.571e-03 | damp: cubic correction exceeds trust fraction |
| February -> March | 7.025854 | 370.728923 | 7.510315 | 26.383191 | 0.003714 | 0.098000 | 1.441e-03 | damp: cubic correction exceeds trust fraction |
| March -> April | 5.838231 | 248.955174 | 7.303963 | 21.321113 | 0.004596 | 0.098000 | 1.609e-03 | damp: cubic correction exceeds trust fraction |
| April -> May | 3.847456 | 61.088738 | 4.126803 | 7.938848 | 0.012344 | 0.098000 | 1.907e-03 | damp: cubic correction exceeds trust fraction |
| May -> June | 5.455863 | 171.692091 | 5.767976 | 15.734642 | 0.006228 | 0.098000 | 1.369e-03 | damp: cubic correction exceeds trust fraction |
| June -> July | 6.915405 | 352.016786 | 7.360853 | 25.451640 | 0.003850 | 0.098000 | 9.482e-04 | damp: cubic correction exceeds trust fraction |
| July -> August | 7.694039 | 475.401838 | 8.030675 | 30.894165 | 0.003172 | 0.098000 | 1.361e-03 | damp: cubic correction exceeds trust fraction |
| August -> September | 9.490010 | 894.689633 | 9.934341 | 47.138497 | 0.002079 | 0.098000 | 1.277e-03 | damp: cubic correction exceeds trust fraction |
| September -> October | 10.250509 | 1156.810545 | 11.009595 | 56.426979 | 0.001737 | 0.098000 | 9.940e-04 | damp: cubic correction exceeds trust fraction |
| October -> November | 10.033152 | 1052.015872 | 10.450750 | 52.426986 | 0.001869 | 0.098000 | 1.432e-03 | damp: cubic correction exceeds trust fraction |
| November -> December | 9.922106 | 1062.568391 | 10.793175 | 53.545509 | 0.001830 | 0.098000 | 1.577e-03 | damp: cubic correction exceeds trust fraction |
| December -> January | 7.426235 | 573.707735 | 10.402875 | 38.627094 | 0.002537 | 0.098000 | 1.822e-03 | damp: cubic correction exceeds trust fraction |

## Mean Conductor Packet Fractions

Fractions use the uniform cyclic character decomposition. They are packet metadata for the arithmetic audit, not the trust-region scaling rule.

| packet | step energy | K^CH response energy |
|---|---:|---:|
| conductor_12 | 0.329112 | 0.329802 |
| conductor_2 | 0.165108 | 0.164012 |
| conductor_3 | 0.244580 | 0.247438 |
| conductor_4 | 0.168029 | 0.168892 |
| conductor_6 | 0.093170 | 0.089857 |

## Highest Cubic Fractions

| step | raw cubic frac | scale | active limits | curve-corrected min p |
|---|---:|---:|---|---:|
| September -> October | 56.426979 | 0.001737 | cubic_fraction | 9.942e-04 |
| November -> December | 53.545509 | 0.001830 | cubic_fraction | 1.577e-03 |
| October -> November | 52.426986 | 0.001869 | cubic_fraction | 1.432e-03 |
| August -> September | 47.138497 | 0.002079 | cubic_fraction | 1.277e-03 |
| December -> January | 38.627094 | 0.002537 | cubic_fraction | 1.822e-03 |

## Reproduction

```powershell
python empirical/k_ch_step_controller.py --preset months --centroids "C:\Projects\simplicial\months\baseline\per_class_output_dists.safetensors" --model-tag llama31_8b --scenario adjacent --max-cubic-fraction 0.1
```
