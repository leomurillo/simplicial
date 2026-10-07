"""
ASYMPTOTIC trigger for a general degree-d polynomial f.

Window primes: q0 = x, q1 = x+a, q2 = x+a+b, q3 = x+a+b+e
  (a = g_left, b = g_mid, e = g_right are the prime gaps; x -> oo along primes).

f monic degree d (leading coeff 1; lower terms fixed). Then as x->oo:
  f(q_{l+1})-f(q_l) = f(x+...) differences. Compute the forward differences.
  u = f(q1)-f(q0),  v = f(q2)-f(q1),  w = f(q3)-f(q2).
By MVT / Taylor: f(x+s)-f(x+t) = f'(x)(s-t) + O(x^{d-2})*(...).
  u ~ f'(x)*a,  v ~ f'(x)*b,  w ~ f'(x)*e   (leading order f'(x)~ d x^{d-1}).
  c_m=f(q0)~x^d, c_{m+2}=f(q2)~x^d.
So  Q = v^2 c_m - u w c_{m+2} ~ f'(x)^2 [ b^2 - a e ] * x^d   (leading order).
=> sign(Q) -> sign(b^2 - a e)  as x->oo, for ANY fixed monic f and fixed gap pattern (a,b,e)!

THIS IS THE UNIVERSAL MECHANISM:
  If a window of 4 primes at large x has middle prime-gap b with b^2 > a*e (outer gaps),
  then Q>0 for EVERY polynomial f once x is large enough.

Verify this limit symbolically with sympy (treat x symbolic, expand leading order).
"""
from sympy import symbols, expand, Poly, factor, simplify, Rational, O, series, limit, oo

x = symbols('x', positive=True)
a,b,e = symbols('a b e', positive=True)   # prime gaps
# general monic degree d: do d=1,2,3,4,5 with generic lower coeffs
def fgen(d, t):
    # f(t)=t^d + sum_{k<d} A_k t^k
    coeffs = symbols(f'A0:{d}')
    return t**d + sum(coeffs[k]*t**k for k in range(d)), coeffs

for d in [1,2,3,4,5]:
    f_, A = fgen(d, x)  # placeholder; we need f at shifted args
    # define f as a lambda in its argument with same coeffs
    Acoef = A
    def F(t, Ac=Acoef, dd=d):
        return t**dd + sum(Ac[k]*t**k for k in range(dd))
    q0=x; q1=x+a; q2=x+a+b; q3=x+a+b+e
    u=F(q1)-F(q0); v=F(q2)-F(q1); w=F(q3)-F(q2)
    cm=F(q0); cm2=F(q2)
    Q=expand(v**2*cm - u*w*cm2)
    # leading term in x: total degree of Q in x is (d-1)*2 + d = 3d-2
    pQ=Poly(Q, x)
    lead_deg=pQ.degree()
    lead_coeff=pQ.LC()
    print(f"d={d}: deg_x(Q)={lead_deg} (expect 3d-2={3*d-2}), leading coeff in x:")
    print("      ", factor(lead_coeff))
    # this leading coeff should be d^2*(b^2-a e) (since f'~ d x^{d-1}, f'^2~d^2 x^{2d-2}, times x^d)
    expected = d**2*(b**2-a*e)
    print("      leading/(d^2*(b^2-ae)) =", simplify(lead_coeff/expected))
    print()
