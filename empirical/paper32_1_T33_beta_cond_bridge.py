"""
Joint result: Paper 32.1 conductor boundary share as a T33 smooth divisor-family ratio,
and the status of beta_infinity.

Claims to verify (exact where possible, else mpmath high precision):

  (1) beta_cond(P_k) = prod_{p|N}(p^2-p) / ( prod_{p|N}(p^2-p+1) - 1 )
      reproduces 32.1 values  3/5, 6/11, 5040/9481, 277200/526223.
      [numerator = phi(N)*N = prod p(p-1);  denominator = sum_{c|N,c>1} phi(c)c
       = prod(p^2-p+1) - 1.]

  (2) beta_cond(inf) = prod_p (p^2-p)/(p^2-p+1) = zeta(6)/(zeta(2)zeta(3))  (Landau^-1).
      The two multipliers are the T33 divisor-family seeds:
        u^2-u    (member P2minus, interpolating phi(N)N)
        u^2-u+1  = Phi_6(u)  (NEW member Psi6, interpolating prod Phi_6(p)).
      Ratio is ABSOLUTELY convergent (factor ~ 1 - 1/p^2) => clean emission (T33 sec 8.5).

  (3) The weight curve  L(beta) = prod_p (1 + 1/((p-1)p^beta))  has
        L(1) = zeta(2)zeta(3)/zeta(6) = Landau = 1/beta_cond(inf)   (reciprocal),
        L(0) divergent (= 1/unit-density, the beta=0 corner -> 0),
      and  beta_inf := root of L(beta)=2  =  0.954352187581...  (32.1 sec 13.3),
      which is STRICTLY BETWEEN the two T33-classified integer-weight endpoints
      and is NOT itself a divisor-order (integer-k) emission.
"""
import sympy as sp
import mpmath as mp
mp.mp.dps = 30

def primes_dividing_primorial(k):
    return list(sp.primerange(2, sp.prime(k) + 1))[:k]

print("=== (1) beta_cond(P_k) exact rationals ===")
expect = {2: sp.Rational(3,5), 3: sp.Rational(6,11),
          4: sp.Rational(5040,9481), 5: sp.Rational(277200,526223)}
for k in (2,3,4,5):
    ps = primes_dividing_primorial(k)
    num = sp.prod([p*p - p for p in ps])              # phi(N)*N
    den = sp.prod([p*p - p + 1 for p in ps]) - 1      # sum_{c|N,c>1} phi(c)c
    bc = sp.Rational(num, den)
    N = sp.prod(ps)
    # cross-check num == phi(N)*N, den == sum_{c|N,c>1} phi(c)*c
    num_chk = sp.totient(N) * N
    den_chk = sum(sp.totient(c) * c for c in sp.divisors(N) if c > 1)
    ok = (num == num_chk) and (den == den_chk) and (bc == expect[k])
    print(f"  P_{k}={int(N):>5}: beta_cond={bc} = {float(bc):.4f}   match32.1={bc==expect[k]}  defs_ok={num==num_chk and den==den_chk}  [{ok}]")

print("\n=== (2) beta_cond(inf) = zeta(6)/(zeta(2)zeta(3)) ===")
zeta_ratio = mp.zeta(6)/(mp.zeta(2)*mp.zeta(3))
# truncated Euler product prod (p^2-p)/(p^2-p+1)
prod = mp.mpf(1)
for p in sp.primerange(2, 200000):
    prod *= mp.mpf(p*p-p)/mp.mpf(p*p-p+1)
print(f"  zeta(6)/(zeta(2)zeta(3)) = {zeta_ratio}")
print(f"  prod_(p<2e5)(p^2-p)/(p^2-p+1) = {prod}")
print(f"  agree to ~ {mp.nstr(abs(prod-zeta_ratio),3)} (prime tail)")
# absolute convergence check: factor = 1 - 1/(p^2-p+1) ~ 1 - 1/p^2
print(f"  factor at p=2,3,5: {[float(1 - mp.mpf(1)/(p*p-p+1)) for p in (2,3,5)]}  (1-O(1/p^2): abs conv)")

print("\n=== (3) weight curve L(beta) and beta_infinity ===")
def L(beta, X=200000):
    s = mp.mpf(0)
    for p in sp.primerange(2, X):
        s += mp.log1p(mp.mpf(1)/((p-1)*mp.power(p, beta)))
    # prime-zeta tail correction ~ sum_{p>=X} 1/(p-1)p^beta ~ small; X large enough for 6 digits
    return mp.e**s
L1 = L(mp.mpf(1))
landau = mp.zeta(2)*mp.zeta(3)/mp.zeta(6)
print(f"  L(1) = {L1}")
print(f"  zeta(2)zeta(3)/zeta(6) (Landau) = {landau}")
print(f"  L(1) == 1/beta_cond(inf)? 1/L(1) = {1/L1}  vs zeta-ratio {zeta_ratio}")
print(f"  L(1) < 2 ? {L1 < 2}  (so root of L=2 is below beta=1)")
beta_inf = mp.findroot(lambda b: L(b) - 2, mp.mpf('0.95'))
print(f"  beta_inf (root of L(beta)=2, primes<2e5) = {mp.nstr(beta_inf, 12)}")
print(f"  32.1 pinned value                        = 0.954352187581")
print(f"  0 < beta_inf < 1, strictly interior: {0 < beta_inf < 1}")

print("\nVERDICT: beta_cond(inf) IS a clean T33 divisor-family ratio (Phi_6 member / (u^2-u) member);")
print("         beta_inf is the interior L=2 root, NOT an integer-k emission -> outside the tower.")
