"""
EXACT characterization of valid region and where detW2=0 curve sits relative to it.

Validity is monotone in C: V = {C > Cmin(B)} where
  Cmin(B) = max over primes p of ( -(p^2 + B p) ) = max_p ( -p^2 - B p ).
Because f(p)=p^2+Bp+C>0  <=>  C > -(p^2+Bp)  for that p; need it for ALL p =>
  C > max_p ( -(p^2+Bp) ) =: Cmin(B).
For each prime p, the line L_p(B) = -(p^2+Bp) = -p*B - p^2 (linear in B, slope -p).
Cmin(B) is the upper envelope of these lines. As B grows, lines with larger p (steeper
negative slope) drop faster, so for large B the binding prime is the SMALLEST (p=2).
For very negative B, the binding prime is the LARGEST... but there's no largest prime!
=> For B -> -oo the envelope is +oo (no finite Cmin)? No: for fixed B, -p*B - p^2; if B<0,
   -p*B = |B| p grows linearly, -p^2 drops quadratically, so max over p is at finite p ~ |B|/2.
Good: max_p (-pB - p^2). Treat p continuous: derivative -B-2p=0 => p=-B/2. So binding prime
near -B/2. Finite. Good.

We want exact Cmin(B) on each linear piece and compare to Cstar(B) = (B^3+38B^2+341B+988)/(B^2+15B+68).

KEY GOAL: show that on the region where detW2 >= 0 (i.e. C <= Cstar(B)) intersected with V,
we have detW3 < 0. We'll do detW3 next; here just set up the region pieces.
"""
from sympy import symbols, primerange, Rational, factor, expand, simplify, solve, Poly, S, nsimplify
import sympy as sp

B = symbols('B', real=True)
P = list(primerange(2, 200))

# Upper envelope pieces: for each prime p, line L_p(B) = -p*B - p^2.
# The envelope max_p L_p(B). Two consecutive primes p<q cross where -pB-p^2 = -qB-q^2
#  => B(q-p) = q^2 - p^2 => B = q+p.  Wait: -pB-p^2=-qB-q^2 => (q-p)B = p^2-q^2 = -(q-p)(q+p)
#  => B = -(p+q).  So line for p is on top (vs q>p) when... at B=-(p+q) they cross.
# For B > -(p+q): which is bigger? slope of L_p is -p (less steep). At B->+oo, L_p (less steep) wins.
# So for B > -(p+q), L_p > L_q (smaller prime p dominates). For B < -(p+q), larger prime q dominates.
# => The binding (max) prime p* at a given B is the one with -(p+q) crossings bracketing B.
# Envelope: between crossing B=-(p_{k}+p_{k+1}) and B=-(p_{k-1}+p_k), the binding prime is p_k.
pr = P
print("Envelope pieces (binding prime p_k on B-interval):")
print(" For B in ( -(p_k+p_{k+1}), -(p_{k-1}+p_k) ), binding prime = p_k, Cmin = -p_k*B - p_k^2")
for k in range(0, 8):
    pk = pr[k]
    left = -(pr[k]+pr[k+1])      # lower B end
    right = (-(pr[k-1]+pr[k]) if k>=1 else sp.oo)  # upper B end (for k=0, +oo)
    print(f"  p_k={pk}: B in ({left}, {right}),  Cmin = {-pk}*B - {pk**2}")

# Now: Cstar(B) - Cmin_piece(B) on each piece; find sign.
Cstar = (B**3 + 38*B**2 + 341*B + 988)/(B**2 + 15*B + 68)
print("\nCstar(B) =", Cstar)
print("\nOn each piece, compute N(B) := (Cstar - Cmin)*(B^2+15B+68); sign tells detW2 vs region.")
print("(B^2+15B+68 > 0 always.) detW2<0 <=> C>Cstar; on V we have C>Cmin; so if Cmin>=Cstar on a")
print("piece, ALL of V there has detW2<0 (D2 closes). Else need D3 on Cmin<C<=Cstar.\n")
for k in range(0, 8):
    pk = pr[k]
    Cmin_piece = -pk*B - pk**2
    num = expand((Cstar - Cmin_piece)*(B**2+15*B+68))
    numf = factor(num)
    left = -(pr[k]+pr[k+1])
    right = (-(pr[k-1]+pr[k]) if k>=1 else None)
    print(f"  p_k={pk}, B-interval=({left},{right}):")
    print(f"     (Cstar-Cmin)*(B^2+15B+68) = {numf}")
