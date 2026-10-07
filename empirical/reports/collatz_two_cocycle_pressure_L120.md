# Collatz Two-Cocycle Pressure

## Status

This report couples the escape-side height cocycle to the normalized affine intercept.  It asks how much additive lift remains inside the same low-height carry windows measured by the height-pressure audit.

- max prefix length: `120`
- barriers: `[0.0, 2.0, 4.0, 8.0]`
- log2(3): `1.584962500721`

## Affine Cocycle

For a carry word `w=(s_1,...,s_m)`,

```text
U_w(n) = 2^{-H(w)} n + B_w
H(w)   = S(w) - m log2(3)
B_{w,s}= (3 B_w + 1) / 2^s
```

The polynomial moment algebra is triangular.  The leading degree-`r` pressure mode is

```text
lambda_r(theta) = sum_s 2^-s 2^{-theta(s-log2(3))} (3/2^s)^r
                = 3^{theta+r} / (2^{1+theta+r}-1)
```

The height pressure minimizer is `theta=0.438032659282`.

| degree r | log2 lambda_r(0) | lambda_r(0) | log2 lambda_r(theta*) | lambda_r(theta*) |
|---:|---:|---:|---:|---:|
| 0 | 0.000000 | 1.000000000 | -0.079319 | 0.946504577 |
| 1 | 0.000000 | 1.000000000 | 0.135501 | 1.098473858 |
| 2 | 0.362570 | 1.285714286 | 0.565819 | 1.480227231 |
| 3 | 0.847997 | 1.800000000 | 1.079261 | 2.112953966 |
| 4 | 1.385654 | 2.612903226 | 1.629751 | 3.094595818 |

The degree-1 intercept mode is neutral at theta zero: `lambda_1(0)=1`.  The degree-2 mode is already expansive, so intercept variance grows even though typical height contracts.

## Unrestricted Intercept Moments

At length `120`, the unrestricted carry shift has:

- mean `B_w`: `40`
- rms `B_w`: `7074539.26213`
- rms/mean: `176863.481553`

This is the first concrete sign that the escape algebra is not scalar: average additive lift is mild, but higher moments are controlled by rare low-carry branches.

## Final Low-Height Windows

These rows select all words whose final height satisfies `H(w) <= barrier`, without requiring earlier prefixes to stay below the barrier.

| barrier | mass | log2 mass | mean H | mean B | rms B | max log2 B | expansion % | max cap log2 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0.0 | 0.00017617055343 | -12.470740 | -2.632725 | 90819.109974 | 533002684.012547 | 70.195500 | 100.0000 | - |
| 2.0 | 0.000327515174901 | -11.576151 | -0.780919 | 51903.750546 | 390913887.963625 | 70.195500 | 53.7900 | 70.836745 |
| 4.0 | 0.000588969956144 | -10.729518 | 1.061966 | 30559.469950 | 291508167.792468 | 70.195500 | 29.9116 | 70.836745 |
| 8.0 | 0.00173299304178 | -9.172518 | 4.718017 | 11538.184456 | 169941480.873452 | 70.195500 | 10.1657 | 70.836745 |

### Max Final-Window Intercepts

| barrier | depth | log2 value | witness carry signature |
|---:|---:|---:|---|
| 0.0 | 120 | 70.195500 | `(1^120)` |
| 2.0 | 120 | 70.195500 | `(1^120)` |
| 4.0 | 120 | 70.195500 | `(1^120)` |
| 8.0 | 120 | 70.195500 | `(1^120)` |

### Max Final-Window Contracting Caps

For `H>0`, a branch has real cap `B_w / (1 - 2^{-H})`; above that cap the branch decreases after the whole word.

| barrier | depth | log2 value | witness carry signature |
|---:|---:|---:|---|
| 0.0 | - | - | - |
| 2.0 | 191 | 70.836745 | `(72 1^119)` |
| 4.0 | 191 | 70.836745 | `(72 1^119)` |
| 8.0 | 191 | 70.836745 | `(72 1^119)` |

## Prefix-Barrier Windows

These rows are stricter: every prefix must satisfy `H(prefix) <= barrier`.  They are the finite analogue of a persistently low-height escape corridor.

| barrier | mass | log2 mass | mean H | mean B | rms B | max log2 B | expansion % | max cap log2 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0.0 | 9.3061361718e-06 | -16.713386 | -5.062436 | 88129.338748 | 1304715628.432503 | 70.195500 | 100.0000 | - |
| 2.0 | 4.80750978531e-05 | -14.344351 | -3.092728 | 50268.999492 | 817707691.883980 | 70.195500 | 84.0314 | 7.271568 |
| 4.0 | 0.000135739095461 | -12.846876 | -1.141298 | 29616.653554 | 544737610.933181 | 70.195500 | 58.9438 | 9.241507 |
| 8.0 | 0.000643859048005 | -10.600967 | 2.708263 | 11228.605291 | 270445089.698736 | 70.195500 | 22.4260 | 13.160558 |

### Max Prefix-Barrier Intercepts

| barrier | depth | log2 value | witness carry signature |
|---:|---:|---:|---|
| 0.0 | 120 | 70.195500 | `(1^120)` |
| 2.0 | 120 | 70.195500 | `(1^120)` |
| 4.0 | 120 | 70.195500 | `(1^120)` |
| 8.0 | 120 | 70.195500 | `(1^120)` |

### Max Prefix-Barrier Contracting Caps

| barrier | depth | log2 value | witness carry signature |
|---:|---:|---:|---|
| 0.0 | - | - | - |
| 2.0 | 191 | 7.271568 | `(3 2 1 2 1 2^2 ... 2^2 1 2 1 2^2 1^2)` |
| 4.0 | 191 | 9.241507 | `(5 2 1 2 1 2^2 ... 2 1 2^2 1 2 1^5)` |
| 8.0 | 191 | 13.160558 | `(9 2 1 2 1 2^2 ... 2 1 2^2 1 2 1^12)` |

## Interpretation

The algebra needed for Collatz is a finite quotient carry algebra lifted to a triangular affine cocycle.  The quotient/carry layer supplies exact branch labels; the height layer supplies contraction pressure; the intercept layer supplies the additive carry memory that scalar pressure cannot see.

The important obstruction is now sharper.  Low-height corridors are exponentially small in 2-adic mass, but inside them the intercept cocycle has neutral and expanding polynomial modes.  A proof-facing escape argument has to dominate this intercept growth against the height pressure and the exact domain cylinders.

Next computational target: build the transfer operator on binned `(H, log2 B)` states and compare its leading spectral radius against the exact domain-cylinder constraints modulo `2^S`.

## Reproduction

```powershell
python empirical/collatz_two_cocycle_pressure.py --max-length 120 --barriers "0.0,2.0,4.0,8.0"
```
