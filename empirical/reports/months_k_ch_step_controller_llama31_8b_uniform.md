# K^CH Local Step Controller - months / llama31_8b

## Status

- centroid source: `C:\Projects\simplicial\months\baseline\per_class_output_dists.safetensors`
- scenario: `uniform`
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
- accepted-scale min / median: `0.020698` / `0.021637`
- raw cubic-fraction max / median: `4.734695` / `4.529383`
- controlled cubic-fraction max: `0.098000`

## Step Table

| step | ||s||_F | ||Kss||_F | rho=||Kss||/||s||^2 | cubic frac | scale | controlled frac | min p next | action |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| uniform -> January | 2.166095 | 13.402505 | 2.856478 | 3.093701 | 0.031677 | 0.098000 | 8.084e-02 | damp: cubic correction exceeds trust fraction |
| uniform -> February | 3.000822 | 27.126430 | 3.012397 | 4.519834 | 0.021682 | 0.098000 | 8.156e-02 | damp: cubic correction exceeds trust fraction |
| uniform -> March | 3.025101 | 27.558337 | 3.011432 | 4.554944 | 0.021515 | 0.098000 | 8.157e-02 | damp: cubic correction exceeds trust fraction |
| uniform -> April | 2.497912 | 18.368932 | 2.943945 | 3.676857 | 0.026653 | 0.098000 | 8.116e-02 | damp: cubic correction exceeds trust fraction |
| uniform -> May | 2.823413 | 23.951557 | 3.004589 | 4.241597 | 0.023105 | 0.098000 | 8.144e-02 | damp: cubic correction exceeds trust fraction |
| uniform -> June | 2.986004 | 26.845916 | 3.010909 | 4.495292 | 0.021801 | 0.098000 | 8.154e-02 | damp: cubic correction exceeds trust fraction |
| uniform -> July | 3.013361 | 27.354878 | 3.012538 | 4.538932 | 0.021591 | 0.098000 | 8.156e-02 | damp: cubic correction exceeds trust fraction |
| uniform -> August | 3.113703 | 29.223259 | 3.014216 | 4.692686 | 0.020884 | 0.098000 | 8.162e-02 | damp: cubic correction exceeds trust fraction |
| uniform -> September | 3.120625 | 29.351562 | 3.014034 | 4.702834 | 0.020838 | 0.098000 | 8.162e-02 | damp: cubic correction exceeds trust fraction |
| uniform -> October | 3.039157 | 27.829695 | 3.013020 | 4.578521 | 0.021404 | 0.098000 | 8.158e-02 | damp: cubic correction exceeds trust fraction |
| uniform -> November | 3.140970 | 29.743071 | 3.014798 | 4.734695 | 0.020698 | 0.098000 | 8.164e-02 | damp: cubic correction exceeds trust fraction |
| uniform -> December | 2.998924 | 27.046658 | 3.007342 | 4.509394 | 0.021732 | 0.098000 | 8.156e-02 | damp: cubic correction exceeds trust fraction |

## Mean Conductor Packet Fractions

Fractions use the uniform cyclic character decomposition. They are packet metadata for the arithmetic audit, not the trust-region scaling rule.

| packet | step energy | K^CH response energy |
|---|---:|---:|
| conductor_12 | 0.380412 | 0.360948 |
| conductor_2 | 0.085581 | 0.091035 |
| conductor_3 | 0.168923 | 0.183575 |
| conductor_4 | 0.172981 | 0.183764 |
| conductor_6 | 0.192102 | 0.180678 |

## Highest Cubic Fractions

| step | raw cubic frac | scale | active limits | curve-corrected min p |
|---|---:|---:|---|---:|
| uniform -> November | 4.734695 | 0.020698 | cubic_fraction | 8.180e-02 |
| uniform -> September | 4.702834 | 0.020838 | cubic_fraction | 8.178e-02 |
| uniform -> August | 4.692686 | 0.020884 | cubic_fraction | 8.178e-02 |
| uniform -> October | 4.578521 | 0.021404 | cubic_fraction | 8.174e-02 |
| uniform -> March | 4.554944 | 0.021515 | cubic_fraction | 8.173e-02 |

## Reproduction

```powershell
python empirical/k_ch_step_controller.py --preset months --centroids "C:\Projects\simplicial\months\baseline\per_class_output_dists.safetensors" --model-tag llama31_8b --scenario uniform --max-cubic-fraction 0.1
```
