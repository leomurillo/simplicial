# Collatz Domain-Constrained Transfer

## Status

This report couples the two-cocycle `(H(w), B_w)` to the exact carry-domain cylinder `n = r_w mod 2^(S+1)`.  The goal is to test whether rare high-intercept corridors line up with actual positive integers cheaply enough to matter.

- long corridor length: `120`
- exact validation length: `10`
- barriers: `[0.0, 2.0, 4.0, 8.0]`
- log2(3): `1.584962500721`

## Exact Domain Formula

```text
U_w(n) = (3^m n + C_w) / 2^S
3^m r_w + C_w == 2^S mod 2^(S+1)
n = r_w + t 2^(S+1)
```

If `2^S > 3^m`, the word is contracting for all sufficiently large representatives in its cylinder.  The exact finite nondecrease exceptions are the `t` for which

```text
r_w + t 2^(S+1) <= floor(C_w / (2^S - 3^m)).
```

## Long Witness Corridors

| barrier | corridor | S | H | log2 B | log2 n0 | log2 U(n0) | log2 gain | log2 cap | nondec reps | word |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 0.0 | all-ones expansion corridor | 120 | -70.195500 | 70.195500 | 121.000000 | 191.195500 | 70.195500 | - | infinite | `(1^120)` |
| 2.0 | all-ones expansion corridor | 120 | -70.195500 | 70.195500 | 121.000000 | 191.195500 | 70.195500 | - | infinite | `(1^120)` |
| 2.0 | final-window earliest contracting cap | 191 | 0.804500 | 69.610538 | 191.415037 | 190.610538 | -0.804500 | 70.836745 | 0 | `(72 1^119)` |
| 2.0 | prefix-barrier earliest contracting cap | 191 | 0.804500 | 6.045360 | 191.707069 | 190.902569 | -0.804500 | 7.271568 | 0 | `(3 2 1 2 1 2^2 1 ... 1 2^2 1 2 1 2^2 1^2)` |
| 4.0 | all-ones expansion corridor | 120 | -70.195500 | 70.195500 | 121.000000 | 191.195500 | 70.195500 | - | infinite | `(1^120)` |
| 4.0 | final-window earliest contracting cap | 191 | 0.804500 | 69.610538 | 191.415037 | 190.610538 | -0.804500 | 70.836745 | 0 | `(72 1^119)` |
| 4.0 | prefix-barrier earliest contracting cap | 191 | 0.804500 | 8.015299 | 189.695762 | 188.891262 | -0.804500 | 9.241507 | 0 | `(5 2 1 2 1 2^2 1 ... 1 2 1 2^2 1 2 1^5)` |
| 8.0 | all-ones expansion corridor | 120 | -70.195500 | 70.195500 | 121.000000 | 191.195500 | 70.195500 | - | infinite | `(1^120)` |
| 8.0 | final-window earliest contracting cap | 191 | 0.804500 | 69.610538 | 191.415037 | 190.610538 | -0.804500 | 70.836745 | 0 | `(72 1^119)` |
| 8.0 | prefix-barrier earliest contracting cap | 191 | 0.804500 | 11.934350 | 190.850897 | 190.046397 | -0.804500 | 13.160558 | 0 | `(9 2 1 2 1 2^2 1 ... 1 2 1 2^2 1 2 1^12)` |

The all-ones corridor creates the largest visible intercept tail, but its first admissible positive integer is also enormous because the exact cylinder is `-1 mod 2^(m+1)`.  The contracting-cap corridors sit just past the height boundary; they are the finite words where additive lift has the best chance to delay descent.

## Exact Final-Window Validation

These exact rows enumerate every carry word at the validation length whose final height satisfies `H(w) <= barrier`.

| barrier | words | mass | log2 mass | expanding % | contracting words | all-decrease words | finite exception reps |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0.0 | 3003 | 0.15087890625 | -2.728537 | 100.0000 | 0 | 0 | 0 |
| 2.0 | 19448 | 0.314529418945 | -1.668733 | 47.9697 | 16445 | 16445 | 0 |
| 4.0 | 92378 | 0.5 | -1.000000 | 30.1758 | 89375 | 89375 | 0 |
| 8.0 | 1144066 | 0.797563552856 | -0.326329 | 18.9175 | 1141063 | 1141062 | 1 |

### Final-Window Max Contracting Caps

| window | barrier | score | S | H | log2 B | log2 n0 | log2 gain | reps | word |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| exact-final-window | 0.0 | - | - | - | - | - | - | - | - |
| exact-final-window | 2.0 | 8.574828 | 16 | 0.150375 | 5.238164 | 16.999527 | -0.149914 | 0 | `(7 1^9)` |
| exact-final-window | 4.0 | 8.574828 | 16 | 0.150375 | 5.238164 | 16.999527 | -0.149914 | 0 | `(7 1^9)` |
| exact-final-window | 8.0 | 8.574828 | 16 | 0.150375 | 5.238164 | 16.999527 | -0.149914 | 0 | `(7 1^9)` |

### Final-Window Smallest Domain Charge

`domain charge = log2(first admissible n) - log2(B_w)`.  Smaller means the intercept tail is cheaper in actual integer size.

| window | barrier | score | S | H | log2 B | log2 n0 | log2 gain | reps | word |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| exact-final-window | 0.0 | 1.699002 | 13 | -2.849625 | 3.255195 | 4.954196 | 2.909990 | infinite | `(1^4 2^2 1 2 1^2)` |
| exact-final-window | 2.0 | 1.699002 | 13 | -2.849625 | 3.255195 | 4.954196 | 2.909990 | infinite | `(1^4 2^2 1 2 1^2)` |
| exact-final-window | 4.0 | 1.699002 | 13 | -2.849625 | 3.255195 | 4.954196 | 2.909990 | infinite | `(1^4 2^2 1 2 1^2)` |
| exact-final-window | 8.0 | 0.083620 | 20 | 4.150375 | -0.083620 | 0.000000 | 0.000000 | 1 | `(2^10)` |

## Exact Prefix-Barrier Validation

These exact rows enumerate every validation-length word whose every prefix stays under the same height barrier.

| barrier | words | mass | log2 mass | expanding % | contracting words | all-decrease words | finite exception reps |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0.0 | 961 | 0.0645141601562 | -3.954240 | 100.0000 | 0 | 0 | 0 |
| 2.0 | 12279 | 0.243927001953 | -2.035479 | 58.4261 | 9525 | 9525 | 0 |
| 4.0 | 71719 | 0.451429367065 | -1.147428 | 33.4157 | 68717 | 68717 | 0 |
| 8.0 | 1028570 | 0.781611442566 | -0.355477 | 19.3036 | 1025567 | 1025566 | 1 |

### Prefix-Barrier Max Contracting Caps

| window | barrier | score | S | H | log2 B | log2 n0 | log2 gain | reps | word |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| exact-prefix-window | 0.0 | - | - | - | - | - | - | - | - |
| exact-prefix-window | 2.0 | 6.278110 | 16 | 0.150375 | 2.941446 | 15.906444 | -0.150175 | 0 | `(3 2 1 2 1 2^2 1^3)` |
| exact-prefix-window | 4.0 | 7.729924 | 16 | 0.150375 | 4.393260 | 16.085908 | -0.149891 | 0 | `(5 2 1 2 1^6)` |
| exact-prefix-window | 8.0 | 8.574828 | 16 | 0.150375 | 5.238164 | 16.999527 | -0.149914 | 0 | `(7 1^9)` |

### Prefix-Barrier Smallest Domain Charge

| window | barrier | score | S | H | log2 B | log2 n0 | log2 gain | reps | word |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| exact-prefix-window | 0.0 | 1.699002 | 13 | -2.849625 | 3.255195 | 4.954196 | 2.909990 | infinite | `(1^4 2^2 1 2 1^2)` |
| exact-prefix-window | 2.0 | 1.699002 | 13 | -2.849625 | 3.255195 | 4.954196 | 2.909990 | infinite | `(1^4 2^2 1 2 1^2)` |
| exact-prefix-window | 4.0 | 1.699002 | 13 | -2.849625 | 3.255195 | 4.954196 | 2.909990 | infinite | `(1^4 2^2 1 2 1^2)` |
| exact-prefix-window | 8.0 | 0.083620 | 20 | 4.150375 | -0.083620 | 0.000000 | 0.000000 | 1 | `(2^10)` |

## Witness Validation

The long witnesses are generated by an early-depth rule: put the extra carry depth as early as the constraints allow.  This table checks that rule against the exact validation window.

| barrier | positive S | final witness exact? | prefix witness exact? | final signatures | prefix signatures |
|---:|---:|---|---|---|---|
| 0.0 | 16 | no contracting S | no contracting S | - | - |
| 2.0 | 16 | True | True | `(7 1^9)` / `(7 1^9)` | `(3 2 1 2 1 2^2 1^3)` / `(3 2 1 2 1 2^2 1^3)` |
| 4.0 | 16 | True | True | `(7 1^9)` / `(7 1^9)` | `(5 2 1 2 1^6)` / `(5 2 1 2 1^6)` |
| 8.0 | 16 | True | True | `(7 1^9)` / `(7 1^9)` | `(7 1^9)` / `(7 1^9)` |

## Interpretation

This is the arithmetic version of the blindspot.  Height pressure sees contraction, and intercept pressure sees a large rare tail.  The exact domain cylinder adds the missing cost: high-intercept words usually demand very large first admissible integers, and contracting words have an exact finite exception budget.

The next proof-facing object is therefore a domain-constrained transfer operator: states should carry `(H, log2 B, log2 r_w or cylinder scale, exception budget)`, with exact residue updates rather than source-blind averaging.  In deep-learning language, this is the conductor packet layer that the quadratic metric averages away.

## Reproduction

```powershell
python empirical/collatz_domain_constrained_transfer.py --long-length 120 --exact-length 10 --barriers "0.0,2.0,4.0,8.0"
```
