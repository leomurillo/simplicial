# Collatz Mixed Gauge Holonomy Theorem Note

## Local Object

Let

```text
D(x) = 2x,        U(x) = (x - 1)/3.
```

Fix a finite quotient

```text
M = 2^a 3^b,      a >= 1,
```

and let `W` be a branch word with `d` occurrences of `D` and `u` occurrences of `U`, with `u <= b`.

The correct finite object is not a same-level map `R/M -> R/M`.  It is the filtered relation

```text
R/(3^u M) -> R/M.
```

The extra digit

```text
q mod 3^u,        x = r + qM mod 3^u M
```

is the gauge coordinate.

## Theorem

For every branch word `W` with `d` `D`-steps and `u` `U`-steps, and every coarse source residue `r mod M`, exactly one of the following occurs.

1. No lift `r + qM mod 3^u M` is an honest inverse-Collatz path because some `U` parity gate fails.
2. Every lift is honest, and the final targets form a single principal `Z/(3^u)` gauge orbit modulo `M`.

In the second case, if `G = M/3^u`, then the final target phase obeys

```text
phase(q) = phase(0) + 2^d q mod 3^u.
```

Thus the word-level gauge holonomy is the unit

```text
2^d in (Z/3^u)^*.
```

## Proof

The formal composition of `W` has affine form

```text
F_W(x) = (2^d x + B_W) / 3^u
```

for some integer `B_W`; this follows by induction from the two branch rules.  Therefore two source lifts differing by `qM` have final formal targets differing by

```text
F_W(x + qM) - F_W(x) = 2^d q M / 3^u = 2^d q G.
```

Modulo `M`, this is exactly a phase shift by `2^d q mod 3^u`.

It remains to justify that honesty is all-or-nothing over the gauge fiber.  Before the `j`th `U` step, two lifts differ by

```text
2^e q M / 3^j
```

for some `e >= 0` and with `j < u`.  Since `u <= b`, this difference is still divisible by `2 * 3`, so it is `0 mod 6`.  Hence the gate condition `x = 4 mod 6` at that `U` step is independent of `q`.  Either every lift passes every `U` gate, or no lift does.

Combining this all-or-nothing gate property with the affine difference formula gives the claimed principal gauge orbit and holonomy multiplier.

## Computational Check

The finite audit

```powershell
python empirical/collatz_gauge_holonomy.py --max-word-length 8 --two-bits 4 --three-depth 4
```

verified this theorem on all branch words in that window:

```text
audited words: 380
honest-source words: 141
finite parity-defect words: 239
gauge orbit violations: 0
phase-law violations: 0
gauge-law failures: 0
```

## Collatz Consequence

The local closure problem is now separated from the global conjecture.

Same-level `U` closure deficit is a section artifact.  After adding the missing `3`-adic lift digit, the local filtered path algebra closes exactly.  The remaining global obstructions are therefore not hidden inside the finite quotient gauge:

```text
Cycle side:   primitive carry-necklace divisibility.
Descent side: q_w >= 0 for contracting carry words.
Escape side:  control of infinite admissible carry words.
```

This note proves only the local algebraic closure statement.  It does not prove Collatz.
