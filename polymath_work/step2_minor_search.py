"""
Search for a UNIFORM negative principal minor of the Hankel matrix (b_{i+j}),
across a large bank of monic non-constant polynomials f with f(p)>0 on primes.

Key reduction: sign(D_N) depends only on ratio sequence c_i = f(p_i).
A principal minor on index set S = {s_0<s_1<...} of the Hankel matrix is
   M_S = det( b_{s_a + s_b} )_{a,b}.
Factor b_{min index appearing}? No -- principal minor rows/cols share index set.
We just compute det of the submatrix b_{i+j}, i,j in S, with exact integers.

We want: an index set S (|S|=3 or 4) such that M_S < 0 for EVERY f in the bank.
"""
from sympy import primerange, Matrix, Integer
import itertools

P = list(primerange(2, 5000))

def bvals(f, L):
    b = [Integer(1)]
    a = Integer(1)
    for i in range(1, L):
        a *= f(P[i-1])
        b.append(a)
    return b

def minor(b, S):
    n = len(S)
    return Matrix(n, n, lambda a, c: b[S[a]+S[c]]).det()

# ---- Build a bank of monic non-constant polynomials with f(p)>0 on all primes ----
# Represent f by coefficient list (leading=1). We ensure f(p)>0 for p in our prime range
# (and ideally for ALL primes; since leading coeff>0 and degree>=1, f(p)>0 for large p
#  automatically; we just check on the primes we use).
def poly_from_coeffs(coeffs):
    # coeffs: highest degree first, leading = 1
    def f(x):
        v = Integer(0)
        for ccoef in coeffs:
            v = v*x + ccoef
        return v
    return f

bank = []  # list of (label, coeffs)

# Degree 1: x + c, c in a range (valid c > -2)
for cc in range(-1, 12):
    bank.append((f"x+{cc}", [Integer(1), Integer(cc)]))

# Degree 2: x^2 + a x + b, choose so positive on primes
for a in range(-3, 6):
    for bb in range(-3, 12):
        coeffs = [Integer(1), Integer(a), Integer(bb)]
        bank.append((f"x^2+{a}x+{bb}", coeffs))

# Degree 3: x^3 + a x^2 + b x + d
for a in range(-2, 4):
    for bb in range(-2, 4):
        for d in range(-2, 6):
            bank.append((f"x^3+{a}x^2+{bb}x+{d}", [Integer(1), Integer(a), Integer(bb), Integer(d)]))

# Degree 4,5,6 a few
import random
random.seed(0)
for deg in (4,5,6):
    for _ in range(40):
        coeffs = [Integer(1)] + [Integer(random.randint(-3,5)) for _ in range(deg)]
        bank.append((f"deg{deg}_rand", coeffs))

# big additive constants
for K in (100, 1000, 10**6):
    bank.append((f"x+{K}", [Integer(1), Integer(K)]))
    bank.append((f"x^2+{K}", [Integer(1), Integer(0), Integer(K)]))
    bank.append((f"x^2+x+{K}", [Integer(1), Integer(1), Integer(K)]))

# Filter bank: keep only f with f(p)>0 for the first ~30 primes (need positivity)
NCHECK = 30
good_bank = []
for label, coeffs in bank:
    f = poly_from_coeffs(coeffs)
    if all(f(P[i]) > 0 for i in range(NCHECK)):
        good_bank.append((label, coeffs, f))

print(f"Bank size after positivity filter: {len(good_bank)}")

# ---- Candidate index sets S, |S| in {3,4}, indices up to MAXIDX ----
MAXIDX = 6  # indices 0..6 -> need b up to 12
Lneed = 2*MAXIDX + 2
candidatesS = []
for size in (3,4):
    for S in itertools.combinations(range(MAXIDX+1), size):
        candidatesS.append(tuple(S))

print(f"Number of candidate index sets: {len(candidatesS)}")

# Precompute b-values for each f
bcache = []
for label, coeffs, f in good_bank:
    bcache.append(bvals(f, Lneed))

# For each candidate S, count how many f give M_S < 0, =0, >0
results = {}
for S in candidatesS:
    neg = 0; zero = 0; pos = 0
    for b in bcache:
        m = minor(b, S)
        if m < 0: neg += 1
        elif m == 0: zero += 1
        else: pos += 1
    results[S] = (neg, zero, pos)

# Print index sets that are ALWAYS negative (neg==total, zero==0, pos==0)
total = len(good_bank)
print(f"\nTotal polynomials tested: {total}")
print("\n=== Index sets that are ALWAYS strictly negative ===")
always_neg = []
for S, (neg, zero, pos) in sorted(results.items()):
    if neg == total:
        always_neg.append(S)
        print(f"  S={S}: ALWAYS NEG ({neg}/{total})")
if not always_neg:
    print("  (none strictly always-negative)")

print("\n=== Index sets that are negative-or-zero (>=0 never) ===")
for S, (neg, zero, pos) in sorted(results.items()):
    if pos == 0 and neg > 0:
        print(f"  S={S}: neg={neg} zero={zero} pos={pos}")

print("\n=== Most-negative index sets (by neg fraction) top 20 ===")
ranked = sorted(results.items(), key=lambda kv: -kv[1][0])
for S, (neg, zero, pos) in ranked[:20]:
    print(f"  S={S}: neg={neg} zero={zero} pos={pos}")
