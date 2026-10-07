# Collatz Remaining Margin Channels

## Meaning

Suffix monotonicity handles every appended carry `s >= 2` after a contracting prefix.  This report audits the two channels still capable of containing a minimal negative-margin word: trailing append-1 chains and first-contraction boundary words.

## Settings

- max length: `8`
- max total carry depth: `21`
- carry alphabet: `1..8`

## Totals

- words scanned: `359083`
- contracting words: `358130`
- negative q words: `0`
- zero q words: `8`
- trivial zero words: `8`
- positive q words: `358122`

## Append-One Chains

| trailing ones | words | negative q | zero q | positive q | min q | max drop from anchor | min-q word |
|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | 83151 | 0 | 0 | 83151 | 1 | 1092 | `(1 3 1)` |
| 2 | 26563 | 0 | 0 | 26563 | 2 | 905 | `(2^3 1^2)` |
| 3 | 7573 | 0 | 0 | 7573 | 1 | 570 | `(3 2 1^3)` |
| 4 | 1848 | 0 | 0 | 1848 | 2 | 260 | `(4 1^4)` |
| 5 | 359 | 0 | 0 | 359 | 115 | -36 | `(2 4 2 1^5)` |
| 6 | 48 | 0 | 0 | 48 | 174 | -168 | `(3 4 1^6)` |
| 7 | 3 | 0 | 0 | 3 | 1077 | -1067 | `(6 1^7)` |

Largest observed q drop along a trailing-one chain:

- word: `(2 1^4 7 3 1)`
- m, S: `8, 17`
- q: `62153`
- height: `4.320300`
- anchor: `(2 1^4 7 3)`
- anchor q: `63245`
- drop from anchor: `1092`

## First-Contraction Boundary

| final carry | boundary words | negative q | zero q | positive q | min q | min-q word |
|---:|---:|---:|---:|---:|---:|---|
| 2 | 222 | 0 | 0 | 222 | 2 | `(1 2^2 1 2)` |
| 3 | 386 | 0 | 0 | 386 | 1 | `(1^2 2 3)` |
| 4 | 442 | 0 | 0 | 442 | 1 | `(1 4)` |
| 5 | 456 | 0 | 0 | 456 | 5 | `(1^3 5)` |
| 6 | 458 | 0 | 0 | 458 | 25 | `(1^7 6)` |
| 7 | 458 | 0 | 0 | 458 | 233 | `(1 7)` |
| 8 | 458 | 0 | 0 | 458 | 37 | `(1 2 8)` |

Smallest observed boundary q:

- word: `(1^2 2 3)`
- m, S: `4, 7`
- q: `1`
- height: `0.660150`
- noncontracting prefix: `(1^2 2)`

## Irreducible After Suffix Monotonicity

An irreducible word here means: root, append-1 final carry, or first-contraction boundary.  Any minimal counterexample must appear in this reduced list.

- irreducible words: `122432`
- negative q: `0`
- zero q: `1`
- positive q: `122431`
- min q: `0`

Smallest irreducible q:

- word: `(2)`
- m, S: `1, 2`
- q: `0`
- height: `0.415037`
- reason: `root`

## Next Proof Targets

The remaining theorem work is now concentrated in two statements:

```text
Append-one positivity:
A contracting append-1 chain cannot push q below zero.

Boundary positivity:
Every first-contraction boundary word has q >= 0.
```

The finite window shows no negative q in either channel.  This is not yet a proof; it is the narrowed target list after the suffix-monotonicity lemma.

## Reproduction

```powershell
python empirical/collatz_margin_remaining_channels.py --max-length 8 --max-total-depth 21 --max-carry 8
```
