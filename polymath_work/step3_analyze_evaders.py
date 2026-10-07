"""
Understand which polynomials make the top minors POSITIVE, and whether a SMALL SET
of minors (a disjunction) covers ALL polynomials in the bank.
Also: does the LEADING D_2 or D_3 cover the evaders? (The established result already
proves degree-1 via D_2/D_3.)
"""
from sympy import primerange, Matrix, Integer
import itertools

P = list(primerange(2, 5000))

def bvals(f, L):
    b = [Integer(1)]; a = Integer(1)
    for i in range(1, L):
        a *= f(P[i-1]); b.append(a)
    return b

def minor(b, S):
    n = len(S)
    return Matrix(n, n, lambda a, c: b[S[a]+S[c]]).det()

def poly_from_coeffs(coeffs):
    def f(x):
        v = Integer(0)
        for ccoef in coeffs:
            v = v*x + ccoef
        return v
    return f

# Rebuild the SAME bank
bank = []
for cc in range(-1, 12):
    bank.append((f"x+{cc}", [Integer(1), Integer(cc)]))
for a in range(-3, 6):
    for bb in range(-3, 12):
        bank.append((f"x^2+{a}x+{bb}", [Integer(1), Integer(a), Integer(bb)]))
for a in range(-2, 4):
    for bb in range(-2, 4):
        for d in range(-2, 6):
            bank.append((f"x^3+{a}x^2+{bb}x+{d}", [Integer(1), Integer(a), Integer(bb), Integer(d)]))
import random
random.seed(0)
for deg in (4,5,6):
    for _ in range(40):
        coeffs = [Integer(1)] + [Integer(random.randint(-3,5)) for _ in range(deg)]
        bank.append((f"deg{deg}_rand", coeffs))
for K in (100, 1000, 10**6):
    bank.append((f"x+{K}", [Integer(1), Integer(K)]))
    bank.append((f"x^2+{K}", [Integer(1), Integer(0), Integer(K)]))
    bank.append((f"x^2+x+{K}", [Integer(1), Integer(1), Integer(K)]))

NCHECK = 30
good_bank = []
for label, coeffs in bank:
    f = poly_from_coeffs(coeffs)
    if all(f(P[i]) > 0 for i in range(NCHECK)):
        good_bank.append((label, coeffs, f))

Lneed = 16
bcache = [(label, coeffs, bvals(f, Lneed)) for (label, coeffs, f) in good_bank]
total = len(bcache)

# The set of candidate minors we'll allow in a "covering set":
# leading minors D_2=(0,1,2), D_3=(0,1,2,3), D_4=(0,1,2,3,4) plus the strong shifted ones.
cand = [(0,1,2),(0,1,2,3),(0,1,2,3,4),
        (2,3,4,5),(1,2,3,4),(2,3,4,6),(2,3,4),(0,2,3,4),
        (1,2,3,5),(1,2,3,6),(1,2,3),(3,4,5,6),(0,1,2,3,4,5)]
# add all consecutive triples/quads up to index 7
for r in range(0,8):
    cand.append(tuple(range(r,r+3)))
    cand.append(tuple(range(r,r+4)))
cand = sorted(set(cand))

# For each polynomial, which candidate minors are negative?
negflags = {}  # label index -> set of minors that are negative
for k,(label,coeffs,b) in enumerate(bcache):
    s = set()
    for S in cand:
        if 2*max(S) < Lneed:
            if minor(b,S) < 0:
                s.add(S)
    negflags[k] = s

# Greedy set cover: pick minors covering all polynomials
uncovered = set(range(total))
chosen = []
allmin = [S for S in cand if 2*max(S) < Lneed]
while uncovered:
    best=None; bestcov=set()
    for S in allmin:
        cov = {k for k in uncovered if S in negflags[k]}
        if len(cov) > len(bestcov):
            bestcov = cov; best = S
    if best is None or len(bestcov)==0:
        print("CANNOT COVER remaining", len(uncovered), "polynomials")
        # show a few uncovered
        for k in list(uncovered)[:10]:
            print("   uncovered:", bcache[k][0], bcache[k][1])
        break
    chosen.append((best,len(bestcov)))
    uncovered -= bestcov

print("Greedy covering set of minors (minor, #newly covered):")
for S,n in chosen:
    print("  ", S, n)
print("Covered all?" , len(uncovered)==0, " total polys:", total)

# Now: the KEY question for a clean theorem -- is {D_2, D_3} alone enough?
# i.e. does every polynomial have D_2<0 OR D_3<0 ?
covD2D3 = 0
evaders = []
for k,(label,coeffs,b) in enumerate(bcache):
    d2 = minor(b,(0,1,2)); d3 = minor(b,(0,1,2,3))
    if d2<0 or d3<0:
        covD2D3 += 1
    else:
        evaders.append((label,coeffs,d2,d3))
print(f"\n{{D_2,D_3}} covers {covD2D3}/{total}.  Evaders: {len(evaders)}")
for label,coeffs,d2,d3 in evaders[:25]:
    print("   evade D2,D3:", label, coeffs, "D2=",d2,"D3=",d3)
