"""
Native Simplicial Investigation, Script 04:
Rigorous check of the critical-line hypothesis.

Hypothesis: For the primorial ledger at N=6, as cutoff X -> infty, the zeros
of M_x(beta, c) accumulate on the imaginary axis Re(beta) = 0.

We test this by:
  (a) Computing zeros at multiple cutoffs and tracking Re(beta) statistics
  (b) Rescaling beta by the natural scale sigma_y to see if the shape stabilizes
  (c) Checking what happens if we use a "Mertens-balanced" ledger where the
      r=1 and r=5 entries are equal (i.e., the actual prime asymmetry is removed)

The third test isolates whether the small positive offset of zeros is due
to the FINITE asymmetry between primes ≡ 1 mod 6 vs primes ≡ 5 mod 6.
By Dirichlet, primes are EQUIDISTRIBUTED in the long run, but finite cutoffs
give Chebyshev-bias-style asymmetries.

The Chebyshev bias: primes ≡ 5 mod 6 outnumber primes ≡ 1 mod 6 for "most" X
(famous result; primes ≡ 5 mod 6 lead in a Cesàro sense, though "race" reverses
infinitely often by Littlewood). So y_raw(5) - y_raw(1) is generically positive.
This asymmetry could be precisely what's pushing the real parts off zero.
"""

import mpmath as mp
from native_simplicial_01_ledger import primorial_ledger, center
from native_simplicial_02_apex_zeros import apex, find_zeros_in_rectangle

mp.mp.dps = 40


def make_symmetric_ledger(y, kind="r1_r5_avg"):
    """Symmetrize ledger to kill the prime-race asymmetry."""
    y2 = list(y)
    if kind == "r1_r5_avg":
        # average y[1] and y[5] (both contain "primes coprime to 6" mass)
        avg = (y[1] + y[5]) / 2
        y2[1] = avg
        y2[5] = avg
    elif kind == "r1_r5_zero":
        # set y[1] = y[5] = 0 (purely r=2,3,4 ledger)
        y2[1] = mp.mpf(0)
        y2[5] = mp.mpf(0)
    elif kind == "centered_again":
        # re-center after operations
        pass
    s = sum(y2) / 6
    y2 = [yi - s for yi in y2]
    return y2


def analyze_modes(y, label):
    print(f"\n  --- {label} ---")
    print(f"  centered y: " + " ".join(f"{mp.nstr(yi, 6):>10}" for yi in y))
    sigma = mp.sqrt(sum(yi**2 for yi in y) / 6)
    print(f"  sigma_y = {mp.nstr(sigma, 8)}")
    for c in range(6):
        zeros = find_zeros_in_rectangle(
            c, y, x_range=(-1, 1), y_range=(-2.5, 2.5),
            grid_x=14, grid_y=14, N=6
        )
        zeros = [z for z in zeros if abs(z) > 1e-10]
        if not zeros:
            print(f"     c={c}: no zeros found")
            continue
        re_arr = [float(z.real) for z in zeros]
        im_arr = [float(z.imag) for z in zeros]
        re_mean = sum(re_arr) / len(re_arr)
        re_min, re_max = min(re_arr), max(re_arr)
        print(f"     c={c}: n={len(zeros):3d}, Re mean={re_mean:+9.6f}, "
              f"Re range [{re_min:+9.6f}, {re_max:+9.6f}], "
              f"|Re|*sigma mean={abs(re_mean)*float(sigma):.5f}")


def main():
    print("=" * 80)
    print("Critical-line check: zeros vs cutoff, with symmetrized variants")
    print("=" * 80)

    for cutoff in [1000, 10000, 100000]:
        print(f"\n========= cutoff = {cutoff} =========")
        y_raw = primorial_ledger(cutoff, variant="prime_power")
        y = center(y_raw)
        analyze_modes(y, f"natural primorial ledger (prime_power)")

        y_sym = make_symmetric_ledger(y, kind="r1_r5_avg")
        analyze_modes(y_sym, "symmetrized: r=1 and r=5 averaged")


if __name__ == "__main__":
    main()
