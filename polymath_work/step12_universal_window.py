"""
For each consecutive prime quadruple at base r, determine whether R<0 (minor negative)
for a HUGE bank of monic polynomials. A window that works for ALL of them is a 'universal
window' candidate. Report, per r, how many monic f FAIL (R>=0).
Also: as a function of f, characterize R at fixed window -- is the SUP over monic f
achieved by f=x (d=1) or by high degree? (Determines worst case.)
"""
from sympy import primerange, Integer, Rational
import random

P = list(primerange(2, 2_000_000))

def poly(coeffs):
    def f(x):
        v=Integer(0)
        for cf in coeffs: v=v*x+cf
        return v
    return f

def Rval(f,r):
    q1,q2,q3,q4=P[2*r],P[2*r+1],P[2*r+2],P[2*r+3]
    u=Rational(f(q2),f(q1)); v=Rational(f(q3),f(q2)); s=Rational(f(q4),f(q3))
    a=u-1;b=v-1;e=s-1
    return a*e-b**2+2*a*b*e+a*b**2*e

# bank of monic polys
random.seed(3)
bank=[]
for cc in range(0,12): bank.append([Integer(1),Integer(cc)])
for a in range(-5,6):
    for bb in range(-5,12):
        bank.append([Integer(1),Integer(a),Integer(bb)])
for deg in range(3,13):
    for _ in range(80):
        bank.append([Integer(1)]+[Integer(random.randint(-6,12)) for _ in range(deg)])
# slow growers
for deg in range(2,13):
    for a in range(-1,-7,-1):
        bank.append([Integer(1),Integer(a)]+[Integer(0)]*(deg-2))
# pure x^d
for d in range(1,13): bank.append([Integer(1)]+[Integer(0)]*d)

def ok(coeffs,npr=400):
    f=poly(coeffs)
    return all(f(P[i])>0 for i in range(npr))
bankf=[poly(c) for c in bank if ok(c)]
print("bank size:", len(bankf))

print("\nPer-window r: number of monic f with R>=0 (i.e. minor NOT negative):")
universal=[]
for r in range(0,30):
    fails=0
    for f in bankf:
        if Rval(f,r) >= 0:
            fails+=1
    q1,q2,q3,q4=P[2*r],P[2*r+1],P[2*r+2],P[2*r+3]
    g=(q2-q1,q3-q2,q4-q3)
    tag=" <-- UNIVERSAL (0 fails)" if fails==0 else ""
    print(f"  r={r:2d} primes=({q1},{q2},{q3},{q4}) gaps={g}: fails={fails}{tag}")
    if fails==0: universal.append(r)
print("\nUniversal windows (R<0 for ALL tested monic f):", universal)
