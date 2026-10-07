"""
Native Simplicial Investigation, Script 03:
Hunt for the "distinguished line" in the apex generator zeros.

Strategy:
  - For real characters (c=0, c=3) the apex is real on the real axis;
    zeros come in conjugate pairs. We test whether they lie on Re beta = c_const.
  - For complex characters (c=1,2 / c=4,5), zeros are not symmetric under conjugation
    in beta (each character's set is conjugate to the OTHER character's set), so the
    natural symmetry is c <-> -c.
  - For each character we compute the mean Re(beta) of small-imag-part zeros and
    check if there's a clear "critical-line" structure.

We also probe:
  (a) Scaling/cutoff dependence: does the line stabilize as cutoff grows?
  (b) Effect of a deliberate centering shift to put the line at Re beta = 0
  (c) Whether a "natural" rescaling of y by 1/sigma(y) makes zeros land on
      a known line (e.g. Re = 1/2 of something).

Key candidate observation: zeros of mode c=3 (real character) appear to lie
ALMOST on Re beta = 0 but with a small positive offset. If the offset is
related to the "mean" structure of y, that's meaningful.
"""

import mpmath as mp
from native_simplicial_01_ledger import primorial_ledger, center
from native_simplicial_02_apex_zeros import apex, find_zeros_in_rectangle

mp.mp.dps = 40


def zero_summary(zeros, label=""):
    if not zeros:
        return f"{label}: no zeros"
    re_parts = [float(z.real) for z in zeros]
    im_parts = [float(z.imag) for z in zeros]
    abs_im = [abs(x) for x in im_parts]
    return (f"{label}: n={len(zeros)} zeros, "
            f"Re range [{min(re_parts):+.6f}, {max(re_parts):+.6f}], "
            f"mean Re = {sum(re_parts)/len(re_parts):+.6f}, "
            f"|Im| range [{min(abs_im):.4f}, {max(abs_im):.4f}]")


def main():
    print("=" * 80)
    print("Hunting for the critical line: scan over cutoffs and variants")
    print("=" * 80)

    for variant in ["prime_power", "prime_only"]:
        print(f"\n### Ledger variant: {variant}")
        for cutoff in [200, 1000, 10000]:
            y_raw = primorial_ledger(cutoff, variant=variant)
            y = center(y_raw)
            sigma_y = mp.sqrt(sum(yi**2 for yi in y) / 6)
            print(f"\n--- cutoff = {cutoff} ---  ||y||/sqrt(6) = {mp.nstr(sigma_y, 8)}")

            for c in range(6):
                zeros = find_zeros_in_rectangle(
                    c, y, x_range=(-2, 2), y_range=(-3, 3),
                    grid_x=16, grid_y=16, N=6
                )
                # Drop spurious zeros at origin (within tolerance)
                zeros = [z for z in zeros if abs(z) > 1e-10]
                print("   " + zero_summary(zeros, f"c={c}"))


if __name__ == "__main__":
    main()
