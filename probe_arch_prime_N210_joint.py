"""
Joint primorial probe at N=210: archimedean vs prime decomposition of the
joint cumulants ell_k^joint(210).

Single-zeta probe (probe_arch_prime_hankel.py) showed arch and prime are
ANTAGONISTIC at every k: sign((-1)^{k+1}) vs sign((-1)^k), magnitudes ~ 2*4^k.

Question for joint primorial: does cross-character orthogonality at primorial
scale break this antagonism? Specifically, the 48 L-functions in Xi_210 contribute:

  mu_k^arch,joint = mu_k^arch,zeta  +  sum over non-zeta characters of
                                       (-1)^k zeta(2k+2, b_chi) / 2^{2k+3} * mult

where b_chi = 1/4 (even, a=0) or 3/4 (odd, a=1), and mult = 1 (self-dual) or 2 (pair).

For each L-function (Lambda(chi, s)) with character of conductor f and parity a:
  Lambda'/Lambda(s) = (1/2) log(f/pi) + (1/2) psi((s+a)/2) + L'/L(chi, s)
  archimedean part contributes: (1/2) psi((s+a)/2)  (constant absorbed)
  odd-in-t Taylor coef at s=1/2: a_{2k+1} = zeta(2k+2, b)/2^{2k+2}   [closed form]

For zeta (f=1), we have additional pole pieces 1/s + 1/(s-1) which give
the full Pass-5 §17.2 archimedean A(s) = 1/s + 1/(s-1) - log(pi)/2 + psi(s/2)/2.

The total joint cumulant comes from the LMFDB zero data (already computed in v6):
  mu_k^joint = ell_{k+1}^joint(210) = sum over all 48 L-functions of
               sum over zeros of gamma_rho^{-2(k+1)}

Then:
  mu_k^prime,joint = mu_k^joint - mu_k^arch,joint   (computed by subtraction)
"""

import sys, io, time
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from mpmath import mp, mpf, zeta, log, pi, matrix, factorial

mp.dps = 300

N_PROBE = 30
K_MAX = N_PROBE + 1   # need mu_0..mu_30 for Hankel up to n=15

# ===================================================================
# Parities of the 28 distinct primitive characters at N=210
# (counted ONCE per pair; multiplicity stored separately)
#
# Encoded as: (name, conductor, parity 'E'/'O', mult: 1=self-dual, 2=pair)
# Note: zeta (f=1) handled separately (has pole pieces).
# ===================================================================

characters = [
    # Self-dual non-zeta
    ("chi_3 (f=3)",                'O', 1),
    ("chi_5(4) (f=5)",             'E', 1),
    ("chi_7(6) (f=7)",             'O', 1),
    ("chi_15(14) (f=15)",          'O', 1),
    ("chi_21(20) (f=21)",          'E', 1),
    ("chi_35(34) (f=35)",          'O', 1),
    ("chi_105(104) (f=105)",       'E', 1),
    # Conjugate pairs (representative parity, multiplicity 2)
    ("chi_5(2,3) pair (f=5)",      'O', 2),
    ("chi_7(2,4) cubic (f=7)",     'E', 2),
    ("chi_7(3,5) sextic (f=7)",    'O', 2),
    ("chi_15(2,8) pair (f=15)",    'E', 2),
    ("chi_21(2,11) pair (f=21)",   'O', 2),
    ("chi_21(5,17) pair (f=21)",   'E', 2),
    ("chi_35(2,18) pair (f=35)",   'O', 2),
    ("chi_35(3,12) pair (f=35)",   'E', 2),
    ("chi_35(4,9) pair (f=35)",    'E', 2),
    ("chi_35(13,27) pair (f=35)",  'E', 2),
    ("chi_35(17,33) pair (f=35)",  'E', 2),
    ("chi_35(19,24) pair (f=35)",  'O', 2),
    ("chi_35(23,32) pair (f=35)",  'O', 2),
    ("chi_105(2,53) pair (f=105)", 'E', 2),
    ("chi_105(17,68) pair (f=105)",'O', 2),
    ("chi_105(23,32) pair (f=105)",'E', 2),
    ("chi_105(38,47) pair (f=105)",'O', 2),
    ("chi_105(44,74) pair (f=105)",'O', 2),
    ("chi_105(59,89) pair (f=105)",'E', 2),
    ("chi_105(62,83) pair (f=105)",'O', 2),
]

n_even_nz = sum(m for _, p, m in characters if p == 'E')
n_odd_nz  = sum(m for _, p, m in characters if p == 'O')
n_total = 1 + n_even_nz + n_odd_nz   # +1 for zeta

print("=" * 78)
print(" N=210 joint primorial arch/prime probe")
print("=" * 78)
print(f" mpmath dps = {mp.dps}")
print(f" Non-zeta even L-functions: {n_even_nz}")
print(f" Non-zeta odd L-functions:  {n_odd_nz}")
print(f" Zeta (f=1, with poles):    1")
print(f" Total L-functions:         {n_total}  (expected 48)")
assert n_total == 48
print()

# ===================================================================
# Archimedean cumulants
# ===================================================================

# Per-L-function archimedean cumulant (excluding zeta), closed form:
#   mu_k^arch,chi = (-1)^k * zeta(2k+2, b_chi) / 2^{2k+3}
# with b_chi = 1/4 (even) or 3/4 (odd)

def mu_arch_per_L(k, parity):
    b = mpf(1)/4 if parity == 'E' else mpf(3)/4
    return (-1)**k * zeta(2*k+2, b) / mpf(2)**(2*k+3)

# Zeta's archimedean cumulant from single-zeta probe formula:
#   A_zeta(s) = 1/s + 1/(s-1) - log(pi)/2 + psi(s/2)/2
# Taylor coefs at s=1/2+t for n=2k+1 odd:
#   pole part: -2^{n+2}  (for n odd)
#   psi part: zeta(n+1, 1/4)/2^{n+1}  (for n >= 1)
# mu_k^arch,zeta = (-1)^k a_{2k+1}/2 = (-1)^k [-2^{2k+3} + zeta(2k+2, 1/4)/2^{2k+2}] / 2

def mu_arch_zeta(k):
    pole = -mpf(2)**(2*k+3)
    psi_part = zeta(2*k+2, mpf(1)/4) / mpf(2)**(2*k+2)
    return (-1)**k * (pole + psi_part) / 2

print("Computing archimedean cumulants ...")
t0 = time.time()
mu_arch_joint = []
for k in range(K_MAX):
    val = mu_arch_zeta(k)
    for _, parity, mult in characters:
        val += mult * mu_arch_per_L(k, parity)
    mu_arch_joint.append(val)
print(f"  Done in {time.time()-t0:.1f}s")

# Sanity at k=0: zeta archimedean has -1.85 contribution alone.
# Other 47 L-functions each contribute (-1)^0 * zeta(2, 1/4 or 3/4) / 8 ~ +2 to +5 per L-function.
# So mu_0^arch,joint should be ~ -1.85 + 47*(average ~3) ~ +100 ish?
print()
print(f"mu_0^arch,joint = {mp.nstr(mu_arch_joint[0], 10)}")
print(f"mu_0^arch,zeta only = {mp.nstr(mu_arch_zeta(0), 10)}")
print(f"Per even L-function at k=0: {mp.nstr(mu_arch_per_L(0, 'E'), 6)}")
print(f"Per odd L-function at k=0:  {mp.nstr(mu_arch_per_L(0, 'O'), 6)}")
print(f"Total non-zeta arch at k=0: {mp.nstr(mu_arch_joint[0] - mu_arch_zeta(0), 6)}")

# ===================================================================
# Total joint cumulants from LMFDB zero data
# ===================================================================

print()
print("Loading zero data and computing total joint cumulants ...")
t0 = time.time()
from zero_data_N210 import self_dual_all as sd, non_self_dual_all as nsd

# ell_m^joint(210) = sum over chars of (sum over zeros of gamma^{-2m})
# mu_k = ell_{k+1}
def joint_cumulant(m):
    total = mpf(0)
    for zs in sd.values():
        total += 2 * sum(z ** (-2 * m) for z in zs)
    for zs in nsd.values():
        total += 2 * sum(z ** (-2 * m) for z in zs)
    return total

mu_total = [joint_cumulant(k+1) for k in range(K_MAX)]
print(f"  Done in {time.time()-t0:.1f}s")
print(f"mu_0^total = {mp.nstr(mu_total[0], 10)} (= ell_1^joint(210), expected ~159.77)")

# ===================================================================
# Prime cumulants by subtraction
# ===================================================================

mu_prime_joint = [mu_total[k] - mu_arch_joint[k] for k in range(K_MAX)]

print()
print("=" * 78)
print(" Joint cumulant decomposition at N=210")
print("=" * 78)
print(f"  {'k':>3} {'mu_k^arch,joint':>22} {'mu_k^prime,joint':>22} {'mu_k^joint':>22}")
print("  " + "-" * 71)
for k in [0, 1, 2, 3, 4, 5, 8, 10, 15, 20, 25, 30]:
    print(f"  {k:>3} {mp.nstr(mu_arch_joint[k], 6):>22} "
          f"{mp.nstr(mu_prime_joint[k], 6):>22} {mp.nstr(mu_total[k], 6):>22}")

def sign_pat(seq, K):
    return "".join("+" if s > 0 else ("-" if s < 0 else "0") for s in seq[:K])

print()
print(f"Sign patterns (k=0..{N_PROBE}):")
print(f"  mu_k^arch,joint : {sign_pat(mu_arch_joint, K_MAX)}")
print(f"  mu_k^prime,joint: {sign_pat(mu_prime_joint, K_MAX)}")
print(f"  mu_k^joint      : {sign_pat(mu_total, K_MAX)}")

print()
print("Cancellation tightness |mu_k^joint| / max(|arch|, |prime|):")
print(f"  {'k':>3} {'|mu_k^joint|':>16} {'max indiv':>16} {'ratio':>16}")
for k in [0, 1, 2, 5, 10, 20, 30]:
    a, p, m = abs(mu_arch_joint[k]), abs(mu_prime_joint[k]), abs(mu_total[k])
    ratio = m / max(a, p) if max(a, p) > 0 else mpf(0)
    print(f"  {k:>3} {mp.nstr(m, 6):>16} {mp.nstr(max(a, p), 6):>16} {mp.nstr(ratio, 6):>16}")

# ===================================================================
# Hankel positivity tests
# ===================================================================

def ldl(M):
    n = M.rows
    A_ = matrix(n, n)
    for i in range(n):
        for j in range(n):
            A_[i, j] = M[i, j]
    diags = []
    for k in range(n):
        d = A_[k, k]
        diags.append(d)
        if d <= 0:
            return False, k, diags
        for i in range(k+1, n):
            f = A_[i, k] / d
            for j in range(k+1, n):
                A_[i, j] -= f * A_[k, j]
    return True, n, diags

def hankel(seq, n):
    M = matrix(n+1, n+1)
    for i in range(n+1):
        for j in range(n+1):
            M[i, j] = seq[i+j]
    return M

def hankel_shifted(seq, n):
    """J_n: shifted-Hankel, J_{ij} = mu_{i+j+1}."""
    M = matrix(n+1, n+1)
    for i in range(n+1):
        for j in range(n+1):
            M[i, j] = seq[i+j+1]
    return M

print()
print("=" * 78)
print(" H_n (Hankel) positivity at N=210: arch-joint, prime-joint, total")
print("=" * 78)
print(f"  {'n':>3}  {'arch':>6} {'prime':>6} {'total':>6}   "
      f"{'arch_minD':>14} {'prime_minD':>14} {'total_minD':>14}")
print("  " + "-" * 88)

for n in [0, 1, 2, 3, 5, 8, 10, 12, 14]:
    if 2*n >= K_MAX:
        break
    Ha = hankel(mu_arch_joint, n)
    Hp = hankel(mu_prime_joint, n)
    Ht = hankel(mu_total, n)
    pa, _, da = ldl(Ha); pp, _, dp = ldl(Hp); pt, _, dt = ldl(Ht)
    sa = "PSD" if pa else "FAIL"
    sp = "PSD" if pp else "FAIL"
    st = "PSD" if pt else "FAIL"
    print(f"  {n:>3}  {sa:>6} {sp:>6} {st:>6}   "
          f"{mp.nstr(min(da), 4):>14} {mp.nstr(min(dp), 4):>14} {mp.nstr(min(dt), 4):>14}")

print()
print("=" * 78)
print(" J_n (shifted Hankel) positivity at N=210: arch-joint, prime-joint, total")
print("=" * 78)
print(f"  {'n':>3}  {'arch':>6} {'prime':>6} {'total':>6}   "
      f"{'arch_minD':>14} {'prime_minD':>14} {'total_minD':>14}")
print("  " + "-" * 88)

for n in [0, 1, 2, 3, 5, 8, 10, 12, 14]:
    if 2*n + 1 >= K_MAX:
        break
    Ja = hankel_shifted(mu_arch_joint, n)
    Jp = hankel_shifted(mu_prime_joint, n)
    Jt = hankel_shifted(mu_total, n)
    pa, _, da = ldl(Ja); pp, _, dp = ldl(Jp); pt, _, dt = ldl(Jt)
    sa = "PSD" if pa else "FAIL"
    sp = "PSD" if pp else "FAIL"
    st = "PSD" if pt else "FAIL"
    print(f"  {n:>3}  {sa:>6} {sp:>6} {st:>6}   "
          f"{mp.nstr(min(da), 4):>14} {mp.nstr(min(dp), 4):>14} {mp.nstr(min(dt), 4):>14}")

# ===================================================================
# Compare to single-zeta probe results
# ===================================================================

print()
print("=" * 78)
print(" Comparison: single-zeta vs N=210-joint arch/prime split")
print("=" * 78)
print()
print("Single-zeta probe:")
print("  mu_0^arch  = -1.85 (NEG)")
print("  mu_0^prime = +1.87 (pos)")
print("  H_n^arch FAILS at every n (mu_0^arch < 0)")
print("  H_n^prime FAILS at every n >= 1")
print("  Antagonism: opposite signs alternating, |arch| ~ |prime| ~ 2*4^k")
print()
print("N=210 joint probe (this script):")
print(f"  mu_0^arch,joint  = {mp.nstr(mu_arch_joint[0], 6)} "
      f"({'pos' if mu_arch_joint[0] > 0 else 'NEG'})")
print(f"  mu_0^prime,joint = {mp.nstr(mu_prime_joint[0], 6)} "
      f"({'pos' if mu_prime_joint[0] > 0 else 'NEG'})")
print()
print("Diagnostic Q: did cross-character orthogonality break the antagonism?")
arch_indef_at_0 = mu_arch_joint[0] <= 0
prime_indef_at_0 = mu_prime_joint[0] <= 0
total_pos = mu_total[0] > 0
print(f"  arch indefinite at H_0?  {'YES' if arch_indef_at_0 else 'no'}")
print(f"  prime indefinite at H_0? {'YES' if prime_indef_at_0 else 'no'}")
print(f"  total PSD at H_0?        {'YES' if total_pos else 'NO'}")
