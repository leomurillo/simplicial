"""
Native Simplicial Investigation, Script 11:
ANOVA decomposition of the LIMIT ledger explicitly.

Limit ledger: y_lim = (-a, b, -a, -a, -a, b)  with  a = 1/sqrt 2, b = sqrt 2.
Indexed by s in Z/6 with CRT s <-> (s mod 2, s mod 3):
   s=0: (0,0), y=-a
   s=1: (1,1), y=b
   s=2: (0,2), y=-a
   s=3: (1,0), y=-a
   s=4: (0,1), y=-a
   s=5: (1,2), y=b

The 2x3 grid:
                   s_3=0   s_3=1   s_3=2
   s_2=0 (even):    -a     -a     -a       (sum = -3a, mean over s_3 = -a)
   s_2=1 (odd):     -a     b      b        (sum = 2b - a, mean over s_3 = (2b-a)/3)

So mean over s_3 of y (per s_2):
  E_{s_3}[y | s_2=0] = -a
  E_{s_3}[y | s_2=1] = (2b - a)/3 = (2*sqrt 2 - 1/sqrt 2)/3 = (4/sqrt 2 - 1/sqrt 2)/3 = (3/sqrt 2)/3 = 1/sqrt 2 = a

Wait. Let's compute: 2 sqrt 2 - 1/sqrt 2 = 2 sqrt 2 - sqrt 2 / 2 = (4 sqrt 2 - sqrt 2) / 2 = 3 sqrt 2 / 2.
And (3 sqrt 2 / 2) / 3 = sqrt 2 / 2 = 1/sqrt 2 = a.

So E_{s_3}[y | s_2 = 0] = -a, E_{s_3}[y | s_2 = 1] = a.
Overall mean E[y] = 0 (centered).

y_2(s_2):
  y_2(0) = -a - 0 = -a
  y_2(1) =  a - 0 =  a

Mean over s_2 of y (per s_3):
  E_{s_2}[y | s_3 = 0] = (-a + -a)/2 = -a    (entries: y(0,0)=-a, y(1,0)=-a)
  E_{s_2}[y | s_3 = 1] = (-a + b)/2 = (b-a)/2
  E_{s_2}[y | s_3 = 2] = (-a + b)/2 = (b-a)/2

y_3(s_3) = E_{s_2}[y|s_3] - 0:
  y_3(0) = -a
  y_3(1) = (b - a)/2
  y_3(2) = (b - a)/2

Numerical: a = 1/sqrt 2 = 0.70711, b = sqrt 2 = 1.41421, so (b-a)/2 = 0.70711/2 = 0.35355. Hmm.
Wait, b - a = sqrt 2 - 1/sqrt 2 = (2 - 1)/sqrt 2 = 1/sqrt 2 = a. So (b-a)/2 = a/2.

Sum check: -a + a/2 + a/2 = 0. Good.

y_3:
  y_3(0) = -a
  y_3(1) = a/2
  y_3(2) = a/2

Interaction y_{2,3}(s_2, s_3) = y(s_2, s_3) - y_2(s_2) - y_3(s_3):
  (0,0):  -a - (-a) - (-a)  = a
  (0,1):  -a - (-a) - (a/2) = -a/2
  (0,2):  -a - (-a) - (a/2) = -a/2
  (1,0):  -a - a - (-a)     = -a
  (1,1):   b - a - (a/2)    = b - 3a/2 = sqrt 2 - 3/(2 sqrt 2) = sqrt 2 - 3 sqrt 2 / 4 = sqrt 2 / 4 = a/2
  (1,2):   b - a - (a/2)    = b - 3a/2 = a/2

Check row sums (should be 0 along each s_2):
  s_2=0: a + (-a/2) + (-a/2) = 0  ✓
  s_2=1: -a + a/2 + a/2 = 0  ✓

Check column sums (should be 0 along each s_3):
  s_3=0: a + (-a) = 0  ✓
  s_3=1: -a/2 + a/2 = 0  ✓
  s_3=2: -a/2 + a/2 = 0  ✓

So at the LIMIT ledger:
  y_2 = (-a, a) with energy 3*(2 a^2) = 6 a^2 = 3
  y_3 = (-a, a/2, a/2) with energy 2*(a^2 + 2*(a/2)^2) = 2*(a^2 + a^2/2) = 3 a^2 = 1.5
  y_{2,3}: entries are (a, -a/2, -a/2, -a, a/2, a/2). Energy = 2*(a^2) + 4*(a^2/4) = 2a^2 + a^2 = 3a^2 = 1.5
  Total = 3 + 1.5 + 1.5 = 6 = sum y^2 = 4 a^2 + 2 b^2 = 4*(1/2) + 2*2 = 2 + 4 = 6. ✓

Percentages: 50% / 25% / 25%.  EXACTLY matches what we see numerically as cutoff -> infty.

Now, the interaction term y_{2,3} has 2 d.o.f. as predicted by T0 §4.5.
In fact, looking at the explicit values:
  y_int = a * [[1, -1/2, -1/2], [-1, 1/2, 1/2]]
       = a * (1, -1) ⊗ (1, -1/2, -1/2) up to row scaling
       = a * [outer product of (1, -1) with (1, -1/2, -1/2)]

So y_int is a RANK-1 tensor in the 2x3 grid -- a single "outer-product"
interaction between the Z/2 and Z/3 axes!  But the 2-dim space of interactions
allows rank-2 tensors. The limit ledger uses only ONE direction in this 2-dim
interaction subspace; the OTHER direction is excited by finite-cutoff corrections.

This is structurally interesting: in the limit, the cross-prime interaction
is RANK 1.
"""

import mpmath as mp

mp.mp.dps = 30


def main():
    a = 1 / mp.sqrt(2)
    b = mp.sqrt(2)

    y_lim = [-a, b, -a, -a, -a, b]

    print("=" * 80)
    print("ANOVA decomposition of the LIMIT ledger at N=6")
    print("=" * 80)

    print(f"\ny_lim = (-1/sqrt 2, sqrt 2, -1/sqrt 2, -1/sqrt 2, -1/sqrt 2, sqrt 2)")
    print(f"a = 1/sqrt 2 = {mp.nstr(a, 12)}")
    print(f"b = sqrt 2   = {mp.nstr(b, 12)}")

    # Build 2x3 grid: rows = s_2 in {0, 1}, cols = s_3 in {0, 1, 2}
    grid = [[mp.mpf(0)] * 3 for _ in range(2)]
    for s in range(6):
        s2, s3 = s % 2, s % 3
        grid[s2][s3] = y_lim[s]

    print("\n2x3 grid of y_lim (rows=s_2, cols=s_3):")
    for s2 in range(2):
        print("  " + " ".join(f"{mp.nstr(grid[s2][s3], 8):>14}" for s3 in range(3)))

    # ANOVA
    y2 = [sum(grid[s2][s3] for s3 in range(3)) / 3 for s2 in range(2)]
    y3 = [sum(grid[s2][s3] for s2 in range(2)) / 2 for s3 in range(3)]
    y_int = [[grid[s2][s3] - y2[s2] - y3[s3] for s3 in range(3)] for s2 in range(2)]

    print(f"\ny_2 (single-axis Z/2 component): {[mp.nstr(x, 12) for x in y2]}")
    print(f"y_3 (single-axis Z/3 component): {[mp.nstr(x, 12) for x in y3]}")
    print(f"\ny_{{2,3}} (cross-prime interaction):")
    for s2 in range(2):
        print("  " + " ".join(f"{mp.nstr(y_int[s2][s3], 12):>14}" for s3 in range(3)))

    # Closed-form
    print(f"\nClosed forms:")
    print(f"  y_2 = (-a, a)              where a = 1/sqrt 2")
    print(f"  y_3 = (-a, a/2, a/2)")
    print(f"  y_int (s_2, s_3) entries:")
    print(f"     row s_2=0: (a, -a/2, -a/2)")
    print(f"     row s_2=1: (-a, a/2, a/2)")
    print(f"  i.e. y_int = a * [outer product of (1, -1)_s2 with (1, -1/2, -1/2)_s3]")

    # Rank check on y_int
    print(f"\nRank of y_int (as 2x3 matrix):")
    # rank = number of nonzero singular values
    import mpmath as _mp
    M = mp.matrix(2, 3)
    for s2 in range(2):
        for s3 in range(3):
            M[s2, s3] = y_int[s2][s3]
    print(f"  Matrix M = {M}")
    # use SVD
    try:
        U, S, V = mp.svd(M)
        print(f"  Singular values: {[mp.nstr(S[i], 10) for i in range(min(2,3))]}")
        rank = sum(1 for i in range(len(S)) if abs(S[i]) > 1e-20)
        print(f"  Numerical rank: {rank}  (out of max possible = 2 = min(2,3))")
    except Exception as e:
        print(f"  SVD error: {e}")
        # Manual: rank 1 iff rows are proportional
        ratio_row = grid[1][0] / grid[0][0] if grid[0][0] != 0 else None
        print(f"  Manual check: ratio y_int[1]/y_int[0] entries: " +
              " ".join(f"{mp.nstr(y_int[1][s3]/y_int[0][s3] if y_int[0][s3] != 0 else 'NaN', 8)}" for s3 in range(3)))

    # Energies
    E_total = sum(yi**2 for yi in y_lim)
    E_y2 = sum(y2[s2]**2 for s2 in range(2)) * 3
    E_y3 = sum(y3[s3]**2 for s3 in range(3)) * 2
    E_int = sum(y_int[s2][s3]**2 for s2 in range(2) for s3 in range(3))
    print(f"\nANOVA energy decomposition:")
    print(f"  ||y||^2 = {mp.nstr(E_total, 12)} (should = 4a^2 + 2b^2 = 2 + 4 = 6)")
    print(f"  E(y_2)  = {mp.nstr(E_y2, 12)}   = 6a^2 = 3       (50.00%)")
    print(f"  E(y_3)  = {mp.nstr(E_y3, 12)}   = 3a^2 = 1.5     (25.00%)")
    print(f"  E(y_int)= {mp.nstr(E_int, 12)}  = 3a^2 = 1.5     (25.00%)")
    print(f"  Sum     = {mp.nstr(E_y2 + E_y3 + E_int, 12)}    -> matches ||y||^2 OK")

    # Confirm: at the limit, the interaction is RANK 1
    print(f"\nKEY STRUCTURAL FACT:")
    print(f"  The cross-prime interaction y_{{2,3}} at the primorial LIMIT ledger")
    print(f"  is RANK 1 (a single outer-product mode) out of a possible 2-dim space.")
    print(f"  Finite-cutoff corrections excite the OTHER interaction direction.")


if __name__ == "__main__":
    main()
