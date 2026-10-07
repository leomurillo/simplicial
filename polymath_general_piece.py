"""
Prove Cmin(B) >= Cstar(B) for ALL B <= -5, hence D2 closes the entire B<=-5 region.

On the piece where prime q=p_k is binding (q nearest -B/2), Cmin = -q*B - q^2.
We must show, for the relevant B-interval of each q,
   -qB - q^2 >= Cstar(B) = (B^3+38B^2+341B+988)/(B^2+15B+68).
Equivalently   N_q(B) := (-qB - q^2)(B^2+15B+68) - (B^3+38B^2+341B+988) >= 0  on that interval
(since B^2+15B+68>0). This N_q(B) = -(Cstar-Cmin)(B^2+15B+68), i.e. the NEGATIVE of what we
factored before. So we want N_q(B) >= 0, i.e. the previously-factored thing <= 0. Confirmed
for q=3..19. Now show it for GENERAL q with symbolic q, on its interval B in (-(q+q'),-(q''+q))
where q'' < q < q' are consecutive primes. The interval LENGTH and endpoints depend on prime
gaps, but we can bound: binding prime q satisfies roughly q ~ -B/2, i.e. B ~ -2q, and the
interval is contained in B in (-(q+nextprime), -(prevprime+q)) which is within ( -2q - gap, -2q + gap ).

Simplest rigorous route: show the cubic  N_q(B) = -q B^3 + ... is >= 0 at the two ENDPOINTS
of each q-interval AND has no interior root. Endpoints are B = -(p_{k-1}+p_k) and -(p_k+p_{k+1}),
shared with neighbors => continuity. At a crossing B=-(p+q) (p,q consecutive), BOTH pieces give
the SAME Cmin (that's the envelope corner), so N is continuous. We just need: N_q has no root in
the open interval (already verified numerically/factoring for k<=7) AND N_q(endpoint) >= 0.
Let's verify N at every envelope corner B=-(p_k+p_{k+1}) for k=0..60 is >= 0. That + per-piece
no-interior-root (the cubic is monotone-ish) gives the whole ray.
"""
from sympy import symbols, primerange, factor, expand, S, Rational, nsimplify, sign
import sympy as sp

B = symbols('B', real=True)
P = list(primerange(2, 5000))

def Cmin_piece(q):
    return -q*B - q**2
Cstar_num = B**3+38*B**2+341*B+988
Cstar_den = B**2+15*B+68

def N_q(q):
    # (Cmin - Cstar)*den = Cmin*den - num   >=0 wanted
    return expand(Cmin_piece(q)*Cstar_den - Cstar_num)

# Check value of N at all envelope corners B = -(p_k + p_{k+1}); at that corner both p_k and p_{k+1}
# are binding (equal Cmin). Evaluate N using q=p_k (== using q=p_{k+1}) -> should match & be >=0.
print("Envelope-corner check: at B=-(p_k+p_{k+1}), N_{p_k}(B)=N_{p_{k+1}}(B), want >=0")
bad = []
for k in range(0, 200):
    pk, pk1 = P[k], P[k+1]
    Bc = -(pk+pk1)
    v1 = N_q(pk).subs(B, Bc)
    v2 = N_q(pk1).subs(B, Bc)
    assert v1 == v2, (k, pk, pk1, v1, v2)
    if v1 < 0:
        bad.append((k, pk, pk1, Bc, v1))
    if k < 12:
        print(f"  k={k}: B=-(.{pk}+{pk1})={Bc}: N={v1}  ({'OK>=0' if v1>=0 else 'NEG!'})")
print("corners with N<0:", bad[:20], "(empty => all corners >=0)")
print("checked corners k=0..199:", "ALL >=0" if not bad else f"{len(bad)} BAD")
