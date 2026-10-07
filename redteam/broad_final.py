"""Final broad confirmation via EXACT contiguous-3x3 obstruction.
For a wide net of monic f (f(p)>0), find the smallest contiguous 3x3 principal
minor {m,m+1,m+2} of the Hankel matrix that is exactly negative. If EVERY
candidate has such a finite m, none is a moment sequence. Exact integer arithmetic."""
import sys; sys.set_int_max_str_digits(2000000)
from sympy import primerange, Integer, Symbol, Poly, expand
P=list(primerange(2,100000))
p=Symbol('p')

def fvals(coeffs, M):
    out=[]
    for i in range(1,M+1):
        pr=P[i-1]; v=Integer(0)
        for c in coeffs: v=v*pr+c
        if v<=0: return None
        out.append(v)
    return out

def b_from_vals(vals, L):
    out=[Integer(1)]; a=Integer(1)
    for i in range(1,L):
        a*=vals[i-1]; out.append(a)
    return out

def minor3(b,m):
    I=[m,m+1,m+2]
    M=[[b[I[i]+I[j]] for j in range(3)] for i in range(3)]
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
           -M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
           +M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))

def smallest_neg_contig3(coeffs, mmax):
    vals=fvals(coeffs, 2*(mmax+3)+2)
    if vals is None: return 'invalid'
    b=b_from_vals(vals, 2*(mmax+3)+2)
    for m in range(0,mmax+1):
        if minor3(b,m) < 0:
            return m
    return None  # no contiguous-3x3 failure up to mmax

# Broad net: powers, products, shifted, rational-ish (cleared denominators), mixed.
tests=[]
# pure powers p^d
for d in [1,2,3,4,6,8,12,16,24,32]:
    c=[int(x) for x in Poly(expand(p**d),p).all_coeffs()]; tests.append((f'p^{d}',c))
# (p+r)^d
for r in [-1,1,2,5]:
    for d in [2,4,8,16]:
        c=[int(x) for x in Poly(expand((p+r)**d),p).all_coeffs()]; tests.append((f'(p+{r})^{d}',c))
# products of distinct quadratics
for (a,b2) in [(0,1),(1,2),(0,2),(-1,3),(3,5)]:
    c=[int(x) for x in Poly(expand((p**2+a)*(p**2+b2)),p).all_coeffs()]
    tests.append((f'(p^2+{a})(p^2+{b2})',c))
# polynomials with large additive constant + high degree
for d in [4,8,16]:
    c=[int(x) for x in Poly(expand(p**d+1000000),p).all_coeffs()]; tests.append((f'p^{d}+1e6',c))
# near-geometric: f tuned so f(2),f(3),f(5).. ~ ratio? use p^d * small
# big-degree to push m
for d in [48,64]:
    c=[int(x) for x in Poly(expand(p**d),p).all_coeffs()]; tests.append((f'p^{d}',c))

mmax=200
print("smallest contiguous-3x3 NEGATIVE principal minor (exact). None=no fail <= %d"%mmax)
worst=[]
for name,coeffs in tests:
    m=smallest_neg_contig3(coeffs, mmax)
    print(f"  {name:18s}: m={m}", flush=True)
    if m is None:
        worst.append(name)
if worst:
    print("CANDIDATE SURVIVORS (no 3x3 contig fail):", worst)
else:
    print("ALL candidates have a finite negative contiguous 3x3 minor => NONE is a moment sequence.")
