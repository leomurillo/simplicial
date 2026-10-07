"""
Native Simplicial Investigation, Script 05:
Test the natural rescaling beta -> beta/sigma_y.

The apex generator M_x(beta, c) = (1/6) sum_s e^{beta y_s} chi_c(s)^*.
If we rescale beta = w / sigma_y, then we examine
   N_x(w, c) := M_x(w/sigma_y, c) = (1/6) sum_s e^{w (y_s/sigma_y)} chi_c(s)^*
which uses the normalized ledger \tilde{y} = y / sigma_y with unit second moment.

Hypothesis: in w-coordinates, the zeros stabilize to a definite locus as
cutoff -> infty. The "Re w = const" lines that emerge ARE the simplicial program's
native critical lines.

This script computes the rescaled zeros across cutoffs and tests:
  (i) Do the rescaled zeros approach a limiting locus?
  (ii) What are the limit values of Re(w) for each character c?
  (iii) Is there any clean structure (e.g. Re(w) related to log of conductor)?

NOTE: Even though sigma_y diverges (with cutoff), the *centered ledger pattern*
y_s / sigma_y approaches a definite limit determined by:
  - the Mertens-type sum equidistribution of primes mod 6
  - the relative weights of r=0, 2, 3, 4 vs r=1, 5 mass
At infinite cutoff, sum_{p prime <= X} log(p)/sqrt(p) is divergent but its
RATIOS across residues 1, 5 mod 6 approach 1 (Dirichlet equidistribution).
"""

import mpmath as mp
from native_simplicial_01_ledger import primorial_ledger, center
from native_simplicial_02_apex_zeros import apex, find_zeros_in_rectangle

mp.mp.dps = 40


def rescaled_ledger(y):
    """Return y / sigma_y, where sigma_y = sqrt(mean(y^2))."""
    sigma = mp.sqrt(sum(yi**2 for yi in y) / 6)
    return [yi / sigma for yi in y]


def analyze_rescaled(y, label):
    print(f"\n  --- {label} ---")
    tilde_y = rescaled_ledger(y)
    print(f"  rescaled tilde_y:  " + " ".join(f"{mp.nstr(yi, 6):>9}" for yi in tilde_y))

    for c in range(6):
        zeros = find_zeros_in_rectangle(
            c, tilde_y, x_range=(-2, 2), y_range=(-3, 3),
            grid_x=20, grid_y=20, N=6
        )
        zeros = [z for z in zeros if abs(z) > 1e-10]
        if not zeros:
            print(f"     c={c}: no zeros found")
            continue
        re_arr = [float(z.real) for z in zeros]
        im_arr = [float(z.imag) for z in zeros]
        re_mean = sum(re_arr) / len(re_arr)
        re_min, re_max = min(re_arr), max(re_arr)
        # The "closest-to-real-axis" zero:
        closest = min(zeros, key=lambda z: abs(z.imag))
        print(f"     c={c}: n={len(zeros):3d}, Re mean={re_mean:+8.5f}, "
              f"Re range [{re_min:+8.5f}, {re_max:+8.5f}], "
              f"closest-to-real: w = {mp.nstr(closest.real, 6):>10} + {mp.nstr(closest.imag, 6):>10} i")


def main():
    print("=" * 80)
    print("Rescaled zeros: stability of limit locus under cutoff -> infty")
    print("=" * 80)

    for cutoff in [1000, 10000, 100000, 1000000]:
        print(f"\n========= cutoff = {cutoff} =========")
        y_raw = primorial_ledger(cutoff, variant="prime_power")
        y = center(y_raw)
        sigma = mp.sqrt(sum(yi**2 for yi in y) / 6)
        print(f"  sigma_y = {mp.nstr(sigma, 10)}")
        analyze_rescaled(y, "prime_power variant")


if __name__ == "__main__":
    main()
