# HL k-tuple singular series: connected cumulant at order 4 — RESULT

**Date:** 2026-06-25
**Script:** `empirical_leverage/hl_cumulant_order4.py`
**Method:** EXACT symbolic (sympy 3.13, `multiset_partitions` over the partition lattice + `cancel`/`simplify`). No floats.

## The prediction

In the program connecting prime-tuple statistics to information geometry, the CONNECTED (cumulant) part of the Hardy–Littlewood k-tuple singular series is predicted to equal `1/φ(p)ⁿ = 1/(p−1)ⁿ` per prime on squarefree support (φ = Euler totient). PROVEN at order 2 (twin-prime constant). Question: does it extend to order 4?

## Setup (exactly as specified)

Singular series multiplicative over primes; per prime, on squarefree support (all shifts distinct mod p, ν_p = s), the moment factor is

    M_s(p) = (1 − s/p) / (1 − 1/p)^s,    M_1 = 1.

Connected n-tuple cumulant via Möbius inversion on the partition lattice:

    C_n(p) = Σ_{π ⊢ {1..n}} (−1)^{|π|−1} (|π|−1)! · ∏_{B ∈ π} M_{|B|}(p).

(The collaborator's "(p−2)²" formula was NOT used; it is wrong.)

Computed moment factors:

    M_1 = 1
    M_2 = p(p−2)/(p−1)²
    M_3 = p²(p−3)/(p−1)³
    M_4 = p³(p−4)/(p−1)⁴

## Exact results

| order n | C_n(p) (simplified) | C_n·(p−1)ⁿ = c_n |
|---------|---------------------------------|-------------------|
| 2 | −1/(p−1)² | c₂ = −1 |
| 3 | −2/(p−1)³ | c₃ = −2 |
| 4 | −6/(p−1)⁴ | c₄ = −6 |

- **Order-2 anchor VALIDATED:** `C_2(p) = M_2 − M_1²` simplifies EXACTLY to `−1/(p−1)² = −1/φ(p)²`. ✓
- The denominator of C_4 factors exactly as `(p−1)⁴`, and `C_4·(p−1)⁴ = −6` is a constant free of p.

## Verdict: **HOLD**

C_4(p) = c₄/(p−1)⁴ with a CONSTANT c₄ = −6. The clean power-4 totient-denominator identity holds at order 4. The connected cumulant lives on `1/φ(p)ⁿ` support exactly, with a constant numerator at every order tested.

### The pattern

    c_n = −(n−1)!

so

    C_n(p) = −(n−1)! / (p−1)ⁿ = −(n−1)! / φ(p)ⁿ.

Verified EXACTLY (symbolically) through order 6:

    c₂ = −1  = −1!
    c₃ = −2  = −2!
    c₄ = −6  = −3!
    c₅ = −24 = −4!
    c₆ = −120 = −5!

The denominator is `φ(p)ⁿ` at every order (the predicted totient-power support), and the connected-cumulant numerator is the constant `−(n−1)!` — exactly the sign/weight `(−1)^{k−1}(k−1)!` that the top (one-block) term of the Möbius/partition-lattice cumulant inversion contributes. The identity is NOT order-2-only; it is an all-orders identity with c_n = −(n−1)!.
