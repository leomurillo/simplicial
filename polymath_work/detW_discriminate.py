"""
TEST the N=2 criterion's discriminating power, then derive N=3 clean form.

N=2 criterion (det W_2 < 0):  c1 g2^2 > c3 g1 g3,  g_l = c_{l+1}-c_l.

Equivalently  Phi_2 := c1 g2^2 - c3 g1 g3 > 0.

(A) AP case c_l = A+B l: g_l = B constant. Then Phi_2 = c1 B^2 - c3 B^2 = B^2(c1-c3) < 0
    (since c3>c1). So AP => Phi_2<0 => det W_2>0 => MOMENT-COMPATIBLE at N=2. GOOD: matches.

(B) Prime/monic: g_l = f(p_{l+1})-f(p_l). The gaps g_l are NOT constant; for monic f of
    degree d, g_l ~ f'(p_l)*(p_{l+1}-p_l). The prime gaps p_{l+1}-p_l are IRREGULAR.
    We need g2^2 > (c3/c1) g1 g3, i.e. the middle gap is large relative to neighbors,
    AMPLIFIED enough to beat the factor c3/c1>1.

Let me COMPUTE Phi_2 for monic f(p)=p+c (degree 1) over the FIRST primes and see sign vs c.
Primes: p1=2,p2=3,p3=5,p4=7. c_l = p_l + c.
g1 = 3-2=1... wait g_l = c_{l+1}-c_l = (p_{l+1}+c)-(p_l+c) = p_{l+1}-p_l = prime gap! (c cancels)
So for f(p)=p+c: g1=1, g2=2, g3=2. (gaps 2->3 is 1, 3->5 is 2, 5->7 is 2).
Phi_2 = c1 g2^2 - c3 g1 g3 = (2+c)*4 - (5+c)*1*2 = 8+4c - 10-2c = 2c-2 = 2(c-1).
=> det W_2 < 0  <=>  Phi_2>0  <=>  c>1.   MATCHES established D_2(c)=-2(c-1)(...)<0 for c>1!
"""
from sympy import symbols, simplify, factor, expand, primerange, Integer

P = list(primerange(2, 100))
c = symbols('c', real=True)

# f(p)=p+c degree 1
def cl(l): return Integer(P[l-1]) + c   # l=1.. uses p_l
g1 = cl(2)-cl(1); g2 = cl(3)-cl(2); g3 = cl(4)-cl(3)
Phi2 = cl(1)*g2**2 - cl(3)*g1*g3
print("deg1 f(p)=p+c:  g1,g2,g3 =", g1, g2, g3)
print("Phi_2 =", expand(Phi2), " (det W_2<0 iff Phi_2>0)")
print("  => det W_2<0  <=>  c>1   [matches established D_2=-2(c-1)(...)]")
print()

# Now degree 2 monic f(p)=p^2 + c (just to see the gaps amplify)
def cl2(l): return Integer(P[l-1])**2 + c
g1=cl2(2)-cl2(1); g2=cl2(3)-cl2(2); g3=cl2(4)-cl2(3)
Phi2b = cl2(1)*g2**2 - cl2(3)*g1*g3
print("deg2 f(p)=p^2+c: gaps g1,g2,g3 =", g1,g2,g3, " (=9-4,25-9,49-25 =5,16,24)")
print("Phi_2 =", expand(Phi2b))
print("  det W_2<0 iff Phi_2>0; solve:", factor(Phi2b))
# find sign for c>=0
from sympy import solve
print("  Phi_2=0 at c =", solve(Phi2b, c))
