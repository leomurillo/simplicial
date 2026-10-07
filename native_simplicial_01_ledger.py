"""
Native Simplicial Investigation, Script 01: Construct primorial arithmetic ledgers at N=6.

For each residue r in Z/6, define the "primorial prime-power weight"
    y_raw(r) = sum_{p^k <= cutoff, p^k ≡ r mod 6} log(p) / sqrt(p^k)
then center: y(r) = y_raw(r) - (1/6) sum_s y_raw(s).

We compute this for multiple cutoffs to see how the ledger settles, and we also build
two natural variants to keep honesty:
  (V1) full prime-power ledger: all prime powers p^k <= cutoff
  (V2) prime-only ledger:       k=1 only, i.e. y_raw(r) = sum_{p prime <= cutoff, p ≡ r mod 6} log(p)/sqrt(p)
  (V3) von Mangoldt-style:      Lambda(n)/sqrt(n) summed by residue mod 6, with Lambda(n) = log p if n = p^k

Note that residues r in {0,2,3,4} for primes are degenerate:
  - r=0 mod 6: requires 6|n, only n=2^k or 3^k can have p^k composite; for prime powers p^k=6 impossible
  - r=2 mod 6: n=2, 8, 32, ... (powers of 2 with exponent giving 2 mod 6)
  - r=3 mod 6: n=3, 27, 243, ... (powers of 3 with exp giving 3 mod 6)
  - r=4 mod 6: n=4, 16, 64, ... (powers of 2 with even exponent)
  - r=1 mod 6: primes 7, 13, 19, 31, 37, 43, 61, 67, 73, ...
  - r=5 mod 6: primes 5, 11, 17, 23, 29, 41, 47, 53, 59, 71, ...

For variant V2 (prime-only): only r=1, r=2 (just p=2), r=3 (just p=3), and r=5 carry mass.
"""

import mpmath as mp
from sympy import isprime, primerange

mp.mp.dps = 30


def prime_powers_up_to(cutoff):
    """Return sorted list of (p, k, p^k) with p prime, k>=1, p^k <= cutoff."""
    out = []
    for p in primerange(2, cutoff + 1):
        pk = p
        k = 1
        while pk <= cutoff:
            out.append((p, k, pk))
            pk *= p
            k += 1
    return sorted(out, key=lambda t: t[2])


def primorial_ledger(cutoff, variant="prime_power"):
    """
    Build the raw 6-vector y_raw[r] for r in Z/6 from arithmetic data.

    variant:
      "prime_power":  y_raw[r] = sum_{p^k <= cutoff, p^k ≡ r mod 6} log(p)/sqrt(p^k)
      "prime_only":   k=1 only
      "von_mangoldt": same as prime_power; the kernel here is Lambda(n)/sqrt(n)
                       summed by n's residue mod 6.
    """
    y_raw = [mp.mpf(0) for _ in range(6)]
    pps = prime_powers_up_to(cutoff)
    for (p, k, pk) in pps:
        if variant == "prime_only" and k != 1:
            continue
        r = pk % 6
        # log(p)/sqrt(p^k); note for von_mangoldt this is exactly Lambda(n)/sqrt(n)
        w = mp.log(p) / mp.sqrt(mp.mpf(pk))
        y_raw[r] += w
    return y_raw


def center(y_raw):
    """Center a real 6-vector to live in H_0 (sum-zero)."""
    s = sum(y_raw) / 6
    return [yi - s for yi in y_raw]


def report_ledger(label, y_raw, y):
    print(f"--- {label} ---")
    print(f"raw y_raw[r] for r=0..5:")
    for r in range(6):
        print(f"   r={r}: y_raw = {mp.nstr(y_raw[r], 12)}")
    print(f"centered y[s] for s=0..5 (sum = {mp.nstr(sum(y), 4)}):")
    for s in range(6):
        print(f"   s={s}: y = {mp.nstr(y[s], 12)}")
    # report ANOVA: y(s_2, s_3) with s_2 = s mod 2, s_3 = s mod 3 via CRT mapping
    # We choose the natural CRT identification s <-> (s_2, s_3) with s mod 2, s mod 3
    print()


if __name__ == "__main__":
    print("=" * 70)
    print("Primorial arithmetic ledgers at N=6, multiple cutoffs and variants")
    print("=" * 70)

    for cutoff in [50, 200, 1000, 10000, 100000]:
        print(f"\n========== cutoff = {cutoff} ==========")
        for variant in ["prime_power", "prime_only"]:
            y_raw = primorial_ledger(cutoff, variant=variant)
            y = center(y_raw)
            report_ledger(f"variant={variant}, cutoff={cutoff}", y_raw, y)
