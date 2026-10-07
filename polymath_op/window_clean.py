"""
CLEAN FORM:  Q(m) = v^2 * c_m  -  u*w * c_{m+2}
where u=c_{m+1}-c_m, v=c_{m+2}-c_{m+1}, w=c_{m+3}-c_{m+2}.

3x3 principal minor {i,i+1,i+2} (m=2i+1) < 0  <=>  Q(m) > 0  <=>
       v^2 * c_m  >  u*w * c_{m+2}.

Interpretation: v=middle gap, u,w=outer gaps. The minor is NEGATIVE (kills moment)
exactly when the MIDDLE gap is large relative to the geometric-ish product of outer gaps,
weighted by the base/forward ratio values. A "prime gap that is locally a peak" triggers it.

VERIFY clean form symbolically and numerically; then study c_l=f(p_l).
"""
from sympy import symbols, expand, simplify, Integer, primerange, factor

# symbolic verify
A,u,v,w = symbols('A u v w', real=True)
B=A+u; C=A+u+v; Dd=A+u+v+w
Q = A*(B-C)**2 + C*(A-B)*(Dd-C)
clean = v**2*A - u*w*C        # c_m=A, c_{m+2}=C=A+u+v
print("Q - (v^2 c_m - u w c_{m+2}) =", simplify(Q-clean), " (should be 0)")
print()

P=list(primerange(2,200000))
print("Number of primes available:", len(P))

def gaps_and_Q(fname, f):
    print(f"\n=== f(p)={fname} :  Q(m)=v^2 c_m - u w c_{{m+2}},  c_l=f(p_l) ===")
    c=[Integer(f(p)) for p in P]
    found=[]
    for m in range(1, 60):  # 1-indexed: c_m=c[m-1]
        cm,cm1,cm2,cm3 = c[m-1],c[m],c[m+1],c[m+2]
        u=cm1-cm; v=cm2-cm1; w=cm3-cm2
        Q=v**2*cm - u*w*cm2
        if Q>0:
            found.append(m)
    print("   m with Q(m)>0:", found[:25], "..." if len(found)>25 else "")
    # the consecutive-minor ones need ODD m
    oddfound=[m for m in found if m%2==1]
    print("   ODD m (=> consecutive 3x3 principal minor {(m-1)/2,...} <0):", oddfound[:15])
    if oddfound:
        m=oddfound[0]; i=(m-1)//2
        print(f"   FIRST odd trigger m={m} -> principal minor on rows {{{i},{i+1},{i+2}}} is NEGATIVE.")
    return found

gaps_and_Q("p", lambda p:p)
gaps_and_Q("p-1", lambda p:p-1)
gaps_and_Q("p+5", lambda p:p+5)
gaps_and_Q("p^2", lambda p:p**2)
gaps_and_Q("p+10^6", lambda p:p+1000000)
gaps_and_Q("p^3-p+1", lambda p:p**3-p+1)
gaps_and_Q("(p-2)(p+100)", lambda p:(p-2)*(p+100))
