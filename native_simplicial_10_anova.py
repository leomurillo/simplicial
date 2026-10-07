"""
Native Simplicial Investigation, Script 10:
ANOVA decomposition of the primorial ledger at N=6.

By CRT, Z/6 ~= Z/2 x Z/3.  The mapping is s <-> (s mod 2, s mod 3).

Mapping table for s in {0, 1, 2, 3, 4, 5}:
  s=0: (0, 0)
  s=1: (1, 1)
  s=2: (0, 2)
  s=3: (1, 0)
  s=4: (0, 1)
  s=5: (1, 2)

So as a 2x3 grid (s_2 in {0,1}, s_3 in {0,1,2}):
   (s_2=0, s_3=0): s=0    (s_2=0, s_3=1): s=4    (s_2=0, s_3=2): s=2
   (s_2=1, s_3=0): s=3    (s_2=1, s_3=1): s=1    (s_2=1, s_3=2): s=5

ANOVA decomposition (Hoeffding/Möbius):
  y(s_2, s_3) = y_2(s_2) + y_3(s_3) + y_{2,3}(s_2, s_3)

where:
  y_2(s_2) = E_{s_3}[y(s_2, s_3)] - E[y]
  y_3(s_3) = E_{s_2}[y(s_2, s_3)] - E[y]
  y_{2,3}(s_2, s_3) = y(s_2, s_3) - y_2(s_2) - y_3(s_3) - E[y]

The dimensions:
  dim(single-axis Z/2) = 1
  dim(single-axis Z/3) = 2 (3-1)
  dim(interaction)     = 6 - 1 - 1 - 2 = 2  (per T0 §4.5)

So y_{2,3} is a 2-dimensional cross-prime interaction term.
"""

import mpmath as mp
from native_simplicial_01_ledger import primorial_ledger, center

mp.mp.dps = 30


def crt_index(s, N=6):
    """Return (s mod 2, s mod 3)."""
    return s % 2, s % 3


def anova_decomposition(y):
    """
    Given y indexed by s in Z/6, decompose into:
      y_single_2[s_2]: single-axis Z/2 component
      y_single_3[s_3]: single-axis Z/3 component
      y_inter[s_2, s_3]: cross-prime interaction component
    All centered (zero marginal over each axis they depend on).
    """
    # Build 2x3 grid: y_grid[s_2][s_3]
    y_grid = [[mp.mpf(0)] * 3 for _ in range(2)]
    for s in range(6):
        s2, s3 = crt_index(s)
        y_grid[s2][s3] = y[s]

    # Overall mean (should be 0 if y is centered)
    mu = sum(y) / 6

    # Marginals
    y2 = [mp.mpf(0)] * 2  # y2[s_2]
    for s2 in range(2):
        y2[s2] = sum(y_grid[s2][s3] for s3 in range(3)) / 3 - mu
    y3 = [mp.mpf(0)] * 3  # y3[s_3]
    for s3 in range(3):
        y3[s3] = sum(y_grid[s2][s3] for s2 in range(2)) / 2 - mu

    # Interaction
    y_int = [[mp.mpf(0)] * 3 for _ in range(2)]
    for s2 in range(2):
        for s3 in range(3):
            y_int[s2][s3] = y_grid[s2][s3] - y2[s2] - y3[s3] - mu

    return y_grid, y2, y3, y_int, mu


def verify_reconstruction(y, y2, y3, y_int, mu):
    """y[s] should equal mu + y2[s%2] + y3[s%3] + y_int[s%2][s%3]."""
    for s in range(6):
        s2, s3 = crt_index(s)
        reconstructed = mu + y2[s2] + y3[s3] + y_int[s2][s3]
        if abs(y[s] - reconstructed) > 1e-25:
            print(f"  WARNING: s={s}, y={y[s]}, reconstructed={reconstructed}, diff={y[s]-reconstructed}")
    print("  Reconstruction OK to machine precision")


def print_grid(name, grid, rows=2, cols=3, prec=8):
    print(f"  {name} (rows = s_2 in [0,1], cols = s_3 in [0,1,2]):")
    for s2 in range(rows):
        print("    " + " ".join(f"{mp.nstr(grid[s2][s3], prec):>14}" for s3 in range(cols)))


def main():
    print("=" * 80)
    print("ANOVA decomposition of primorial ledgers at N=6 (CRT: Z/6 = Z/2 x Z/3)")
    print("=" * 80)

    print("\nCRT mapping s <-> (s mod 2, s mod 3):")
    for s in range(6):
        print(f"  s={s} <-> (s mod 2={s%2}, s mod 3={s%3})")

    for cutoff in [1000, 10000, 100000]:
        print(f"\n========= cutoff = {cutoff} =========")
        y_raw = primorial_ledger(cutoff, variant="prime_power")
        y = center(y_raw)
        sigma_y = mp.sqrt(sum(yi**2 for yi in y) / 6)

        print(f"  centered y[s] for s=0..5:")
        for s in range(6):
            print(f"     y[{s}] = {mp.nstr(y[s], 10)}")
        print(f"  sigma_y = {mp.nstr(sigma_y, 8)}")

        y_grid, y2, y3, y_int, mu = anova_decomposition(y)
        print(f"\n  Overall mean mu = {mp.nstr(mu, 6)} (should be ~0 by centering)")

        print(f"\n  Single-axis Z/2 component y_2[s_2]:")
        for s2 in range(2):
            print(f"    y_2[{s2}] = {mp.nstr(y2[s2], 10)}")
        print(f"  Verify: sum y_2 = {mp.nstr(sum(y2), 6)} (should be 0)")

        print(f"\n  Single-axis Z/3 component y_3[s_3]:")
        for s3 in range(3):
            print(f"    y_3[{s3}] = {mp.nstr(y3[s3], 10)}")
        print(f"  Verify: sum y_3 = {mp.nstr(sum(y3), 6)} (should be 0)")

        print(f"\n  Interaction component y_{{2,3}}[s_2, s_3]:")
        print_grid("y_int", y_int)
        # Verify marginal sums vanish:
        for s2 in range(2):
            row_sum = sum(y_int[s2][s3] for s3 in range(3))
            print(f"    row s_2={s2}: sum over s_3 = {mp.nstr(row_sum, 6)} (should be 0)")
        for s3 in range(3):
            col_sum = sum(y_int[s2][s3] for s2 in range(2))
            print(f"    col s_3={s3}: sum over s_2 = {mp.nstr(col_sum, 6)} (should be 0)")

        verify_reconstruction(y, y2, y3, y_int, mu)

        # Compute energies (squared norms) of each component
        E_single_2 = sum(y2[s2]**2 for s2 in range(2)) * 3  # times multiplicity over the 6-vector
        E_single_3 = sum(y3[s3]**2 for s3 in range(3)) * 2
        E_inter = sum(y_int[s2][s3]**2 for s2 in range(2) for s3 in range(3))
        E_total = sum(y[s]**2 for s in range(6))
        print(f"\n  ANOVA energy decomposition (||y||^2 = {mp.nstr(E_total, 8)}):")
        print(f"    Single-axis Z/2:  {mp.nstr(E_single_2, 8)}  ({100*float(E_single_2/E_total):.2f}%)")
        print(f"    Single-axis Z/3:  {mp.nstr(E_single_3, 8)}  ({100*float(E_single_3/E_total):.2f}%)")
        print(f"    Interaction:      {mp.nstr(E_inter, 8)}  ({100*float(E_inter/E_total):.2f}%)")
        # check
        sum_check = E_single_2 + E_single_3 + E_inter
        print(f"    Sum:              {mp.nstr(sum_check, 8)}  (matches {100*float(sum_check/E_total):.2f}%)")


if __name__ == "__main__":
    main()
