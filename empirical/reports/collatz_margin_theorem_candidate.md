# Collatz Margin Theorem Candidate

## Theorem Split

Candidate:

```text
For every nontrivial contracting carry word w, q_w > 0.
```

The old research notes force a sharper split.  The equality case `q_w = 0` is exactly the positive periodic/cycle obstruction: `U_w(r_w)=r_w`, equivalently `2^S-3^m` divides `C_w`.  That is the cycle-side zero-orbit problem from the notes.  The new descent-side theorem candidate is therefore:

```text
For every contracting carry word w, q_w >= 0.
Equality occurs only on the trivial (2)^m family if the positive cycle conjecture holds.
```

## Exact Identities

Let `D=2^S-3^m`, `M=2^(S+1)`, and choose the exact domain residue `r_w` by

```text
3^m r_w + C_w == 2^S mod M.
```

For contracting words `D>0`, define `y_w=U_w(r_w)`.  Then

```text
D r_w - C_w = M q_w
q_w = (r_w - y_w) / 2
```

So the sign of `q_w` is not an approximation.  It is exactly the sign of descent at the first positive integer in the carry cylinder.

## Heavy Census Imported

- source: `empirical\reports\collatz_margin_lattice_L12_S25_K8.json`
- settings: `{'max_length': 12, 'max_total_depth': 25, 'max_carry': 8, 'top_limit': 16}`
- contracting words: `15641778`
- positive q: `15641766`
- zero q: `12`
- trivial zero q: `12`
- nontrivial zero q: `0`
- negative q: `0`
- primitive negative q: `0`

## Random Stress

- samples: `500000`
- contracting samples seen: `499877`
- max length: `120`
- max carry: `12`
- seed: `20260513`
- bad nontrivial q<=0 sample: `False`

Smallest positive `q` seen in random stress:

- word: `(1 4)`
- length/depth: `2, 5`
- q: `1`

## Lower-Envelope Family

The visible `q=1` lower envelope is not mysterious.  The word

```text
(1, 4, 2, 2, ..., 2)
```

maps `3 -> 5 -> 1 -> 1 -> ... -> 1`, so `q=(3-1)/2=1` for every length at least 2.  This gives an infinite positive-margin family exactly on the lower edge.

| word | m | S | q | n0 | image | descent |
|---|---:|---:|---:|---:|---:|---:|
| `(1 4)` | 2 | 5 | 1 | 3 | 1 | 2 |
| `(1 4 2)` | 3 | 7 | 1 | 3 | 1 | 2 |
| `(1 4 2^2)` | 4 | 9 | 1 | 3 | 1 | 2 |
| `(1 4 2^3)` | 5 | 11 | 1 | 3 | 1 | 2 |
| `(1 4 2^4)` | 6 | 13 | 1 | 3 | 1 | 2 |
| `(1 4 2^5)` | 7 | 15 | 1 | 3 | 1 | 2 |
| `(1 4 2^6)` | 8 | 17 | 1 | 3 | 1 | 2 |
| `(1 4 2^7)` | 9 | 19 | 1 | 3 | 1 | 2 |
| `(1 4 2^8)` | 10 | 21 | 1 | 3 | 1 | 2 |
| `(1 4 2^9)` | 11 | 23 | 1 | 3 | 1 | 2 |
| `(1 4 2^10)` | 12 | 25 | 1 | 3 | 1 | 2 |
| `(1 4 2^11)` | 13 | 27 | 1 | 3 | 1 | 2 |

Verified through length `120`; last row has `q=1`.

## Equality Family

The trivial equality family is `(2)^m`, where the first representative is `1` and the image is also `1`.

| word | m | S | q | n0 | image | descent |
|---|---:|---:|---:|---:|---:|---:|
| `(2)` | 1 | 2 | 0 | 1 | 1 | 0 |
| `(2^2)` | 2 | 4 | 0 | 1 | 1 | 0 |
| `(2^3)` | 3 | 6 | 0 | 1 | 1 | 0 |
| `(2^4)` | 4 | 8 | 0 | 1 | 1 | 0 |
| `(2^5)` | 5 | 10 | 0 | 1 | 1 | 0 |
| `(2^6)` | 6 | 12 | 0 | 1 | 1 | 0 |
| `(2^7)` | 7 | 14 | 0 | 1 | 1 | 0 |
| `(2^8)` | 8 | 16 | 0 | 1 | 1 | 0 |
| `(2^9)` | 9 | 18 | 0 | 1 | 1 | 0 |
| `(2^10)` | 10 | 20 | 0 | 1 | 1 | 0 |
| `(2^11)` | 11 | 22 | 0 | 1 | 1 | 0 |
| `(2^12)` | 12 | 24 | 0 | 1 | 1 | 0 |

Verified through length `120`; last row has `q=0`.

## Proof Target

A proof of the full candidate naturally decomposes into two lemmas:

```text
Descent-margin lemma: q_w >= 0 for every contracting carry word.
Cycle-zero lemma: q_w = 0 only for the trivial (2)^m positive cycle.
```

The second lemma is exactly the old notes' cycle-side divisibility problem.  The first lemma is the new thing we can attack directly with the domain-cylinder algebra.

## Reproduction

```powershell
python empirical/collatz_margin_theorem_candidate.py --samples 500000 --max-length 120 --max-carry 12 --family-length 120
```
