"""
Native Simplicial Investigation, Script 06:
Compute the LIMITING zero locus in rescaled w-coordinates.

In the limit X -> infty, the rescaled ledger tilde_y = y / sigma_y approaches
a definite vector (the "Mertens-equidistribution limit") given by Dirichlet's
theorem on primes in arithmetic progressions. We compute that limit explicitly
and find ALL zeros of the limiting apex in a generous box.

LIMIT LEDGER:
  At cutoff infty, both r=1 and r=5 residues capture half the prime mass each
  (Dirichlet equidistribution), and the r=2, 3, 4 contributions are FINITE
  (only finitely many prime powers: r=2 has 2, 2^7=128 (=2 mod 6); wait,
  more carefully: 2^k mod 6 = 2 if k=1, 4 if k=2, 2 if k=3, 4 if k=4 ...
  Actually 2 mod 6 = 2, 4 mod 6 = 4, 8 mod 6 = 2, 16 mod 6 = 4, ...
  So 2^k mod 6: cycles {2, 4, 2, 4, ...} from k=1. Mass = sum_{k>=1} log 2 / sqrt(2^k)
  = log 2 * sum_{k>=1} 2^{-k/2} = log 2 * sqrt(2)/(sqrt(2)-1) = log 2 * (sqrt(2)+sqrt(2)/(sqrt(2)-1))
  Let me just compute: log 2 * 1/(sqrt(2)-1) by geometric series sum_{k>=1} (1/sqrt(2))^k = (1/sqrt(2))/(1-1/sqrt(2)) = 1/(sqrt(2)-1).
  And this splits equally between r=2 and r=4 over the cycle.

  3^k mod 6: 3, 3, 3, ... (always 3). Mass = log 3 * sum_{k>=1} 3^{-k/2}
  = log 3 * (1/sqrt(3))/(1-1/sqrt(3)) = log 3 / (sqrt(3) - 1).

  r=0: nothing (no prime power is 0 mod 6).

  r=1 and r=5: each gets HALF of sum_{p>3 prime} log p / sqrt(p), which DIVERGES.

So the dominant entries are y_raw[1] and y_raw[5], each ~ (1/2) * sum_{p<=X} log p / sqrt(p).
Their RATIO -> 1 as X -> infty. After centering and rescaling by sigma_y,
y_1 and y_5 each approach +sqrt(2), other entries approach 0... wait,
let me compute the centered/rescaled limit carefully.

If y_raw[1] = y_raw[5] = D (large, X-dependent) and y_raw[r] = c_r (finite)
for r in {0,2,3,4}, then after centering:
  mean = (2D + c_0 + c_2 + c_3 + c_4) / 6 ~ D/3
  y_centered[r] for r in {0,2,3,4}: c_r - D/3 ~ -D/3
  y_centered[r] for r in {1,5}: D - D/3 = 2D/3
sigma_y^2 = (1/6) sum y_centered^2
         ~ (1/6) [4 * (D/3)^2 + 2 * (2D/3)^2]
         = (1/6) * (4 D^2/9 + 8 D^2/9)
         = (1/6) * (12 D^2/9) = (12/54) D^2 = (2/9) D^2
so sigma_y ~ D * sqrt(2)/3.

Rescaled tilde_y:
  tilde_y[r] for r in {0,2,3,4}: -D/3 / (D sqrt(2)/3) = -1/sqrt(2)
  tilde_y[r] for r in {1,5}:     +2D/3 / (D sqrt(2)/3) = 2/sqrt(2) = sqrt(2)

So the LIMITING tilde_y = (-1/sqrt(2), sqrt(2), -1/sqrt(2), -1/sqrt(2), -1/sqrt(2), sqrt(2)).

This is the "primorial equidistribution limit" ledger. It has SYMMETRY: invariant
under s <-> s + 2 mod 6 (the cyclic shift by 2 permutes {0,2,4} and fixes the
"prime" pattern: actually s=1 and s=5 are both "prime" residues; s+2: 1->3, 5->1.
Let's check: shift by 2 sends (s=0)->(s=2), (s=1)->(s=3), ..., (s=5)->(s=1).
Under this shift y -> y_shift. y=(-a, b, -a, -a, -a, b) with a=1/sqrt(2), b=sqrt(2).
y_shift[s] = y[s-2]:
  y_shift[0] = y[4] = -a
  y_shift[1] = y[5] = b
  y_shift[2] = y[0] = -a
  y_shift[3] = y[1] = b
  y_shift[4] = y[2] = -a
  y_shift[5] = y[3] = -a
Hmm, that's NOT the same. So the limit ledger does NOT have a shift-by-2 symmetry.
But under s <-> -s (i.e., s <-> 6-s, which is the "reversal"):
  y_rev[s] = y[-s mod 6] = y[6-s mod 6]
  y_rev[0] = y[0] = -a
  y_rev[1] = y[5] = b
  y_rev[2] = y[4] = -a
  y_rev[3] = y[3] = -a
  y_rev[4] = y[2] = -a
  y_rev[5] = y[1] = b
Yes! y_rev = y. So the limit ledger is REAL ( = symmetric under reversal),
which makes M_x(beta, c) real for real beta and the conjugation rule
M_x(beta, c)^* = M_x(beta^*, -c) hold.

That's the structure we expected from a real-valued primorial ledger.
"""

import mpmath as mp
from native_simplicial_02_apex_zeros import apex, find_zeros_in_rectangle

mp.mp.dps = 40


def limit_ledger():
    a = 1 / mp.sqrt(2)
    b = mp.sqrt(2)
    # y = (-a, b, -a, -a, -a, b) -- check: sum = -4a + 2b = -4/sqrt(2) + 2 sqrt(2) = -2sqrt(2) + 2 sqrt(2) = 0. Good.
    # mean square = (1/6)(4 a^2 + 2 b^2) = (1/6)(4*0.5 + 2*2) = (1/6)(2 + 4) = 1. Good.
    return [-a, b, -a, -a, -a, b]


def main():
    print("=" * 80)
    print("Limiting zero locus in rescaled w-coordinates")
    print("Primorial equidistribution limit ledger:")
    print("   y_lim = (-1/sqrt 2, sqrt 2, -1/sqrt 2, -1/sqrt 2, -1/sqrt 2, sqrt 2)")
    print("=" * 80)

    y = limit_ledger()
    print(f"\ny_lim = {[mp.nstr(yi, 12) for yi in y]}")
    print(f"sum    = {mp.nstr(sum(y), 8)}")
    print(f"mean^2 = {mp.nstr(sum(yi**2 for yi in y)/6, 8)}")
    print()

    print("Symmetry checks:")
    yrev = [y[(-s) % 6] for s in range(6)]
    print(f"  y_rev (s -> -s) == y: {all(abs(yrev[i]-y[i])<1e-30 for i in range(6))}")
    yshift = [y[(s - 2) % 6] for s in range(6)]
    print(f"  y_shift (s -> s+2) == y: {all(abs(yshift[i]-y[i])<1e-30 for i in range(6))}")
    print()

    print("Zero hunt in w-plane, generous box [-3, 3] x [-10, 10]:")
    for c in range(6):
        zeros = find_zeros_in_rectangle(
            c, y, x_range=(-3, 3), y_range=(-10, 10),
            grid_x=40, grid_y=60, N=6
        )
        zeros = [z for z in zeros if abs(z) > 1e-10]
        print(f"\n  c={c} ({len(zeros)} zeros found):")
        for z in zeros[:25]:  # show first 25
            print(f"    w = {mp.nstr(z.real, 12):>16} + {mp.nstr(z.imag, 12):>16} i"
                  f"   |M| = {mp.nstr(abs(apex(z, c, y)), 4)}")


if __name__ == "__main__":
    main()
