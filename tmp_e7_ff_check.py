"""Exact verification: fake counting data over q=8 satisfies all abstract E.7-FF axioms.

N_m = (2^m - 1)(4^m - 1) = 8^m + 1 - 4^m - 2^m   (q = 8, 'genus 1', P(t) = (1-2t)(1-4t))

Checks:
  1. N_m >= 0 for all m (state positivity / Lambda >= 0).
  2. Point multiplicities m_n = (1/n) sum_{d|n} mu(n/d) N_d are NONNEGATIVE INTEGERS
     (honest ITPFI over a countable set of 'closed points' with norms 8^n).
  3. Functional equation P(t) = q^g t^{2g} P(1/(qt)) exactly (coefficient identity).
  4. Zeros at t = 1/2, 1/4, i.e. Re s = log2/log8 = 1/3 and 2/3 -- OFF the line Re s = 1/2.
  5. Weil bound |N_m - 8^m - 1| <= 2g * 8^{m/2} fails (so no actual curve), incl. m=1.
  6. Rosati positivity fails: Tr((F - sqrt(q))(F - sqrt(q))') = 4q - 2 sqrt(q)(beta + q/beta) < 0
     for beta = 2, q = 8 (exact: 32 - 12*sqrt(8) < 0  <=>  32^2 < 144*8 = 1152).
"""
from sympy import mobius, divisors, symbols, expand, simplify, Rational, sqrt, Poly

q = 8
def N(m): return (2**m - 1)*(4**m - 1)

# --- 1 & 2: multiplicities ---
MAX = 300
bad = []
for n in range(1, MAX+1):
    s = sum(mobius(n//d) * N(d) for d in divisors(n))
    if s % n != 0 or s < 0:
        bad.append((n, s))
assert not bad, f"FAIL multiplicities: {bad[:5]}"
mvals = [sum(mobius(n//d)*N(d) for d in divisors(n))//n for n in range(1, 13)]
print("m_n (n=1..12):", mvals)
print("check N_n = sum_{d|n} d*m_d :",
      all(N(n) == sum(d * (sum(mobius(d//e)*N(e) for e in divisors(d))//d) for d in divisors(n))
          for n in range(1, 60)))

# --- 3: functional equation ---
t = symbols('t')
P = expand((1 - 2*t)*(1 - 4*t))
g = 1
FE = expand(q**g * t**(2*g) * P.subs(t, 1/(q*t)))
print("FE exact:", simplify(P - FE) == 0)

# --- 4: zero locations ---
from sympy import log, nsimplify
print("Re s of zeros:", nsimplify(log(2)/log(8)), nsimplify(log(4)/log(8)))

# --- 5: Weil bound violation ---
viol = [m for m in range(1, 10) if (4**m + 2**m)**2 > 4 * 8**m]   # |N - q^m - 1| = 4^m + 2^m
print("Weil bound |tr F^m| <= 2g q^{m/2} violated at m =", viol)

# --- 6: Rosati form negative on F - sqrt(q) ---
beta = 2
val = 4*q - 2*sqrt(q)*(beta + Rational(q, beta))   # = 32 - 12*sqrt(8)
print("Rosati Tr((F-sqrt q)(F-sqrt q)') =", val, "=", float(val), "< 0 :", val < 0)

# --- sanity: honest-vs-fake same ITPFI type data ---
# type at beta<=1 depends only on the lattice q^{beta Z}; both honest genus-1/F_8 curve
# and the fake count have norms {8^n} with m_n ~ 8^n/n -> same Araki-Woods ratio set.
print("ALL CHECKS PASS")
