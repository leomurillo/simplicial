# Collatz Inverse Tree 3-Adic Audit

## Meaning

The forward carry audits were mostly 2-adic because the accelerated map divides by powers of 2.  The flipped inverse tree exposes the missing prime: unrestricted inverse words live in `Z[1/3]`, and returning to `Z` is a 3-adic divisibility condition.

For the unrestricted inverse branches

```text
D(x) = 2x
U(x) = (x - 1)/3
```

a binary word with `k` uses of `U` lands at `N / 3^k`.  It is an integer exactly when `v_3(N) >= k`.  That is the 3-adic closure test.

The shifted branch system is also audited:

```text
A(x) = 2x - 1
B(x) = 2x/3
```

## Branch Audits

### inverse D/U from seed 1

- seed: `1`
- max length: `20`
- final integer words: `268` / `1048576`
- final integer density: `0.000255584717`

| L | words | integer words | integer density | distinct integer endpoints | dominant reduced denominator exponents (inverse D/U from seed 1) |
|---:|---:|---:|---:|---:|---|
| 1 | 2 | 2 | 1.000000000000 | 2 | 3^-0:2 |
| 2 | 4 | 2 | 0.500000000000 | 2 | 3^-0:2, 3^-1:2 |
| 3 | 8 | 3 | 0.375000000000 | 3 | 3^-0:3, 3^-1:3, 3^-2:2 |
| 4 | 16 | 4 | 0.250000000000 | 3 | 3^-1:5, 3^-2:5, 3^-0:4, 3^-3:2 |
| 5 | 32 | 5 | 0.156250000000 | 4 | 3^-2:10, 3^-1:8, 3^-3:7, 3^-0:5, 3^-4:2 |
| 8 | 256 | 10 | 0.039062500000 | 8 | 3^-3:65, 3^-4:61, 3^-2:45, 3^-5:37, 3^-1:23 |
| 10 | 1024 | 18 | 0.017578125000 | 15 | 3^-4:236, 3^-5:224, 3^-3:178, 3^-6:148, 3^-2:98 |
| 12 | 4096 | 29 | 0.007080078125 | 25 | 3^-5:874, 3^-6:832, 3^-4:690, 3^-7:585, 3^-3:412 |
| 14 | 16384 | 51 | 0.003112792969 | 44 | 3^-6:3270, 3^-7:3123, 3^-5:2666, 3^-8:2297, 3^-4:1701 |
| 16 | 65536 | 88 | 0.001342773438 | 76 | 3^-7:12329, 3^-8:11813, 3^-6:10303, 3^-9:8993, 3^-5:6922 |
| 18 | 262144 | 154 | 0.000587463379 | 127 | 3^-8:46774, 3^-9:44948, 3^-7:39857, 3^-10:35166, 3^-6:27897 |
| 20 | 1048576 | 268 | 0.000255584717 | 215 | 3^-9:178353, 3^-10:171836, 3^-8:154385, 3^-11:137464, 3^-7:111724 |

### inverse D/U from seed 2

- seed: `2`
- max length: `20`
- final integer words: `355` / `1048576`
- final integer density: `0.000338554382`

| L | words | integer words | integer density | distinct integer endpoints | dominant reduced denominator exponents (inverse D/U from seed 2) |
|---:|---:|---:|---:|---:|---|
| 1 | 2 | 1 | 0.500000000000 | 1 | 3^-0:1, 3^-1:1 |
| 2 | 4 | 2 | 0.500000000000 | 2 | 3^-0:2, 3^-1:1, 3^-2:1 |
| 3 | 8 | 3 | 0.375000000000 | 3 | 3^-0:3, 3^-1:2, 3^-2:2, 3^-3:1 |
| 4 | 16 | 4 | 0.250000000000 | 4 | 3^-0:4, 3^-1:4, 3^-2:4, 3^-3:3, 3^-4:1 |
| 5 | 32 | 5 | 0.156250000000 | 5 | 3^-2:8, 3^-1:7, 3^-3:7, 3^-0:5, 3^-4:4 |
| 8 | 256 | 12 | 0.046875000000 | 11 | 3^-4:56, 3^-3:54, 3^-5:42, 3^-2:40, 3^-1:22 |
| 10 | 1024 | 22 | 0.021484375000 | 20 | 3^-5:208, 3^-4:204, 3^-6:162, 3^-3:156, 3^-7:93 |
| 12 | 4096 | 39 | 0.009521484375 | 34 | 3^-6:782, 3^-5:772, 3^-7:625, 3^-4:607, 3^-8:385 |
| 14 | 16384 | 66 | 0.004028320312 | 58 | 3^-7:2961, 3^-6:2933, 3^-8:2417, 3^-5:2365, 3^-9:1571 |
| 16 | 65536 | 115 | 0.001754760742 | 98 | 3^-8:11272, 3^-7:11192, 3^-9:9366, 3^-6:9217, 3^-10:6352 |
| 18 | 262144 | 200 | 0.000762939453 | 166 | 3^-9:43102, 3^-8:42873, 3^-10:36356, 3^-7:35930, 3^-11:25526 |
| 20 | 1048576 | 355 | 0.000338554382 | 278 | 3^-10:165433, 3^-9:164778, 3^-11:141340, 3^-8:140139, 3^-12:102142 |

### shifted A/B from seed 2

- seed: `2`
- max length: `20`
- final integer words: `488` / `1048576`
- final integer density: `0.000465393066`

| L | words | integer words | integer density | distinct integer endpoints | dominant reduced denominator exponents (shifted A/B from seed 2) |
|---:|---:|---:|---:|---:|---|
| 1 | 2 | 1 | 0.500000000000 | 1 | 3^-0:1, 3^-1:1 |
| 2 | 4 | 2 | 0.500000000000 | 2 | 3^-0:2, 3^-1:1, 3^-2:1 |
| 3 | 8 | 2 | 0.250000000000 | 2 | 3^-1:3, 3^-0:2, 3^-2:2, 3^-3:1 |
| 4 | 16 | 4 | 0.250000000000 | 4 | 3^-2:5, 3^-0:4, 3^-1:3, 3^-3:3, 3^-4:1 |
| 5 | 32 | 5 | 0.156250000000 | 5 | 3^-2:8, 3^-3:8, 3^-1:6, 3^-0:5, 3^-4:4 |
| 8 | 256 | 14 | 0.054687500000 | 14 | 3^-4:58, 3^-3:52, 3^-5:45, 3^-2:36, 3^-6:23 |
| 10 | 1024 | 26 | 0.025390625000 | 26 | 3^-5:213, 3^-4:198, 3^-6:171, 3^-3:144, 3^-7:98 |
| 12 | 4096 | 50 | 0.012207031250 | 50 | 3^-6:795, 3^-5:753, 3^-7:653, 3^-4:572, 3^-8:405 |
| 14 | 16384 | 89 | 0.005432128906 | 89 | 3^-7:2996, 3^-6:2873, 3^-8:2506, 3^-5:2253, 3^-9:1646 |
| 16 | 65536 | 157 | 0.002395629883 | 157 | 3^-8:11371, 3^-7:10995, 3^-9:9654, 3^-6:8845, 3^-10:6626 |
| 18 | 262144 | 277 | 0.001056671143 | 277 | 3^-9:43391, 3^-8:42206, 3^-10:37305, 3^-7:34668, 3^-11:26516 |
| 20 | 1048576 | 488 | 0.000465393066 | 488 | 3^-10:166293, 3^-9:162471, 3^-11:144517, 3^-8:135786, 3^-12:105707 |

## Integer Cycles In All Z

These are included as a calibration row for the flipped picture.  A correct global story has to keep the positive, zero, and negative basins separate.

| cycle | length | verified |
|---|---:|---|
| `0` | 1 | True |
| `1, 4, 2` | 3 | True |
| `-1, -2` | 2 | True |
| `-5, -14, -7, -20, -10` | 5 | True |
| `-17, -50, -25, -74, -37, -110, -55, -164, -82, -41, -122, -61, -182, -91, -272, -136, -68, -34` | 18 | True |

## Interpretation

The flip is worth doing.  The binary branch support is huge, but integrality is a thin 3-adic condition.  That means our previous 2-adic residue/carry ledger was only half of the filtered algebra.  The natural object is a mixed `2`/`3` path algebra:

- `2`-adic data controls forward carry depth and descent margins.
- `3`-adic data controls which inverse binary words are honest integer nodes rather than `Z[1/3]` shadows.
- the five integer cycles are boundary components of the all-`Z` dynamics, not noise.

The next useful theorem form is therefore not purely 2-adic:

```text
Every infinite support path in the inverse 2/3 branch algebra either
falls into one of the five integer cycle components or has a
nonzero 3-adic denominator defect at some finite stage.
```

That is the flipped version of the closure-deficit question: support paths are easy; integer paths require simultaneous 2-adic and 3-adic closure.

## Reproduction

```powershell
python empirical/collatz_inverse_tree_3adic_audit.py --max-length 20
```
