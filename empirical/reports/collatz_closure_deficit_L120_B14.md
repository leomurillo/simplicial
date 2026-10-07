# Collatz Closure-Deficit Ledger

## Meaning

Papers 11 and 12 say that support closure is not enough: the visible conductor macrovariable can close while the full filtered adjacency algebra still carries hidden data.  This is the Collatz version of that audit.

The visible macrovariable is the no-descent support language:

```text
S_j <= floor(j log2(3)) for every prefix j.
```

The filtered data is the exact 2-adic residue packet of the initial odd integer.  At finite depth this report projects those packets modulo `2^B` and compares them with the support-only language.

## Projection Audit

| bits | stable from | final states | depths | residues | residue density | residue deficit | max v2(n+1) | contains -1 |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 8 | 5 | 1319 | 71 | 19 | 0.148438 | 0.851562 | 8 | True |
| 10 | 6 | 4396 | 71 | 64 | 0.125000 | 0.875000 | 10 | True |
| 12 | 7 | 15348 | 71 | 226 | 0.110352 | 0.889648 | 12 | True |
| 14 | 8 | 49353 | 71 | 734 | 0.089600 | 0.910400 | 14 | True |

Selected rows for the largest quotient, `2^14`:

| m | states mod 2^14 | depths | residues | density | mean v2(n+1) |
|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 1 | 4096 | 0.500000 | 2.999756 |
| 2 | 2 | 2 | 3072 | 0.375000 | 3.333008 |
| 3 | 3 | 2 | 2048 | 0.250000 | 3.749512 |
| 4 | 7 | 3 | 1664 | 0.203125 | 3.922476 |
| 5 | 12 | 3 | 1216 | 0.148438 | 4.157072 |
| 8 | 173 | 5 | 734 | 0.089600 | 4.431880 |
| 10 | 961 | 6 | 734 | 0.089600 | 4.431880 |
| 12 | 3031 | 8 | 734 | 0.089600 | 4.431880 |
| 16 | 4579 | 10 | 734 | 0.089600 | 4.431880 |
| 20 | 6047 | 12 | 734 | 0.089600 | 4.431880 |
| 30 | 10451 | 18 | 734 | 0.089600 | 4.431880 |
| 40 | 14855 | 24 | 734 | 0.089600 | 4.431880 |
| 60 | 23663 | 36 | 734 | 0.089600 | 4.431880 |
| 80 | 31737 | 47 | 734 | 0.089600 | 4.431880 |
| 100 | 40545 | 59 | 734 | 0.089600 | 4.431880 |
| 120 | 49353 | 71 | 734 | 0.089600 | 4.431880 |

## Positive Integer Stress

Directly tested positive odd integers below `2^B`, excluding the fixed point `1`, against the no-descent condition through `120` accelerated odd steps.

| bits | odds tested | survivors to M | best n | survived prefixes | failure length | failure S/cap |
|---:|---:|---:|---:|---:|---:|---|
| 8 | 127 | 0 | 27 | 36 | 37 | 59/58 |
| 10 | 511 | 0 | 703 | 50 | 51 | 83/80 |
| 12 | 2047 | 0 | 703 | 50 | 51 | 83/80 |
| 14 | 8191 | 0 | 10087 | 65 | 66 | 108/104 |
| 16 | 32767 | 0 | 35655 | 84 | 85 | 135/134 |
| 18 | 131071 | 0 | 35655 | 84 | 85 | 135/134 |
| 20 | 524287 | 0 | 1027431 | 114 | 115 | 183/182 |

## Interpretation

This is the blindspot made concrete.  The support language remains alive and the finite residue projections stabilize to nonempty 2-adic survivor sets, including the all-ones class `-1`.  But bounded positive integers disappear in the direct stress test.  So the second-half theorem is not a mass/counting theorem; it is a closure theorem separating the inverse-limit 2-adic survivor set from the embedded positive odd integers.

The next theorem target should therefore be:

```text
The infinite no-descent residue inverse limit contains no positive odd integer.
```

In the papers' language: height support is the associated graded; exact residue packets are the filtered block; the missing proof is that support-level closure does not lift to a positive-integer full-block path.

## Reproduction

```powershell
python empirical/collatz_closure_deficit_ledger.py --max-length 120 --projection-bits 8 10 12 14 --positive-bits 8 10 12 14 16 18 20
```
