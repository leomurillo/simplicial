"""
THE N=2 WINDOW CRITERION (a 3x3 principal-minor test, applied at every window s):

  NON-MOMENT  if  EXISTS s>=1 :  c_s g_{s+1}^2 > c_{s+2} g_s g_{s+2}.     (*)
  where c_l=f(p_l), g_l=c_{l+1}-c_l.

Equivalently  R(s) := g_{s+1}^2 / (g_s g_{s+2})  >  c_{s+2}/c_s.

(A) AP control: c_l = A+B l => g_l=B => g_{s+1}^2/(g_s g_{s+2}) = 1, and c_{s+2}/c_s>1.
    So (*) NEVER holds for AP. GOOD (AP is moment).

(B) Prime/monic: does (*) hold for SOME s, for EVERY monic f? Let's scan.
    For each f, find smallest s with (*) true (=> a negative 3x3 minor, => non-moment),
    OR report none found up to s_max.

This is the discriminating, degree-independent criterion requested.
"""
from sympy import primerange, Integer

P = list(primerange(2, 200000))

def scan(ff, smax=400):
    def c(l): return Integer(ff(P[l-1]))
    cv = [None]+[c(l) for l in range(1, smax+5)]  # cv[l]
    g = [None]+[cv[l+1]-cv[l] for l in range(1, smax+4)]
    for s in range(1, smax+1):
        lhs = cv[s]*g[s+1]**2
        rhs = cv[s+2]*g[s]*g[s+2]
        if lhs > rhs:
            return s, cv[s], g[s], g[s+1], g[s+2]
    return None

tests = {
  "p": lambda p: p, "p+1": lambda p: p+1, "p+5": lambda p:p+5, "p+10": lambda p:p+10,
  "p+10^6": lambda p:p+10**6,
  "p^2": lambda p: p**2, "p^2+1": lambda p: p**2+1, "p^2+10^6": lambda p:p**2+10**6,
  "p^3+1": lambda p: p**3+1, "p^3-p+5": lambda p: p**3-p+5,
  "p^4+1": lambda p: p**4+1, "p^5+1": lambda p:p**5+1,
  "p^6+1": lambda p:p**6+1, "p^7+1": lambda p:p**7+1,
  "p^10+1": lambda p:p**10+1,
  "p^2+p+1": lambda p:p**2+p+1, "2p^3+3p+7": lambda p:2*p**3+3*p+7,
}
print(f"{'f':14s} {'smallest s with (*)':>20s}   (window primes p_s..p_{{s+3}})")
for name, ff in tests.items():
    r = scan(ff, 500)
    if r is None:
        print(f"{name:14s} {'NONE up to 500':>20s}")
    else:
        s = r[0]
        print(f"{name:14s} {s:>20d}   primes p_{s}={P[s-1]} .. p_{s+3}={P[s+2]}")
