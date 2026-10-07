# Collatz Remaining Margin Channels

## Meaning

Suffix monotonicity handles every appended carry `s >= 2` after a contracting prefix.  This report audits the two channels still capable of containing a minimal negative-margin word: trailing append-1 chains and first-contraction boundary words.

## Settings

- max length: `12`
- max total carry depth: `25`
- carry alphabet: `1..8`

## Totals

- words scanned: `15710500`
- contracting words: `15641778`
- negative q words: `0`
- zero q words: `12`
- trivial zero words: `12`
- positive q words: `15641766`

## Append-One Chains

| trailing ones | words | negative q | zero q | positive q | min q | max drop from anchor | min-q word |
|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | 3909061 | 0 | 0 | 3909061 | 1 | 88572 | `(1 3 1)` |
| 2 | 1609560 | 0 | 0 | 1609560 | 2 | 73805 | `(2^3 1^2)` |
| 3 | 632621 | 0 | 0 | 632621 | 1 | 46740 | `(3 2 1^3)` |
| 4 | 234717 | 0 | 0 | 234717 | 2 | 26585 | `(4 1^4)` |
| 5 | 80980 | 0 | 0 | 80980 | 48 | 14348 | `(1 2^2 4 2 1^5)` |
| 6 | 25431 | 0 | 0 | 25431 | 72 | 6650 | `(2^2 4 2 1^6)` |
| 7 | 7037 | 0 | 0 | 7037 | 471 | -247 | `(2 1 6 1^7)` |
| 8 | 1625 | 0 | 0 | 1625 | 706 | -611 | `(4^2 1^8)` |
| 9 | 282 | 0 | 0 | 282 | 6466 | -6362 | `(7 1^9)` |
| 10 | 28 | 0 | 0 | 28 | 28290 | -28248 | `(8 1^10)` |

Largest observed q drop along a trailing-one chain:

- word: `(1^2 2 1 2^2 1 4 3 1 3 1)`
- m, S: `12, 22`
- q: `1831392`
- height: `2.980450`
- anchor: `(1^2 2 1 2^2 1 4 3 1 3)`
- anchor q: `1919964`
- drop from anchor: `88572`

## First-Contraction Boundary

| final carry | boundary words | negative q | zero q | positive q | min q | min-q word |
|---:|---:|---:|---:|---:|---:|---|
| 2 | 1509 | 0 | 0 | 1509 | 2 | `(1 2^2 1 2)` |
| 3 | 12508 | 0 | 0 | 12508 | 1 | `(1^2 2 3)` |
| 4 | 16567 | 0 | 0 | 16567 | 1 | `(1 4)` |
| 5 | 17883 | 0 | 0 | 17883 | 5 | `(1^3 5)` |
| 6 | 18243 | 0 | 0 | 18243 | 25 | `(1^7 6)` |
| 7 | 18321 | 0 | 0 | 18321 | 169 | `(1^8 2^2 7)` |
| 8 | 18333 | 0 | 0 | 18333 | 37 | `(1 2 8)` |

Smallest observed boundary q:

- word: `(1^2 2 3)`
- m, S: `4, 7`
- q: `1`
- height: `0.660150`
- noncontracting prefix: `(1^2 2)`

## Irreducible After Suffix Monotonicity

An irreducible word here means: root, append-1 final carry, or first-contraction boundary.  Any minimal counterexample must appear in this reduced list.

- irreducible words: `6604713`
- negative q: `0`
- zero q: `1`
- positive q: `6604712`
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
python empirical/collatz_margin_remaining_channels.py --max-length 12 --max-total-depth 25 --max-carry 8
```
