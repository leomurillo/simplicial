"""
probe_fusion_closure_nogo.py   --  certificate for N9.

Claim under test: the property separating the RH-respecting class from RH-violating Dirichlet
series with a functional equation is CROSS-PRIME MULTIPLICATIVITY  a_{mn}=a_m a_n (coprime m,n),
i.e. the EULER PRODUCT, i.e. cross-prime fusion closure (T8 sec 3.4 / T11).

We certify:
  (1) zeta (a_n=1) and L(.,chi_3) (a_n=chi_3(n)) are cross-prime fusion-closed: defect 0 exactly.
  (2) the Davenport-Heilbronn function f = (1-i k)/2 L(s,chi) + (1+i k)/2 L(s,conj chi),
      chi the order-4 character mod 5 (chi(2)=i), k = DH constant -- has a FUNCTIONAL EQUATION
      (Davenport-Heilbronn 1936) and zeros OFF the critical line, yet is NOT cross-prime
      fusion-closed: defect != 0. So functional equation =/=> RH; cross-prime fusion closure is the
      structural invariant the counterexamples violate.
  (3) cubic = pairwise: for fusion-closed series a_{pqr}=a_p a_q a_r follows from pairwise closure,
      so the order-3 vertex adds no constraint beyond order-2.

a_DH(n) = Re(chi(n)) + k*Im(chi(n))  (real).  numpy. No torch.
"""
import numpy as np

# order-4 character mod 5 with chi(2)=i:  chi(1)=1, chi(2)=i, chi(3)=-i, chi(4)=-1
CHI5 = {0:0+0j, 1:1+0j, 2:1j, 3:-1j, 4:-1+0j}
def chi5(n):  return CHI5[n % 5]
def chi3(n):
    m = n % 3
    return 0.0 if m == 0 else (1.0 if m == 1 else -1.0)

# Davenport-Heilbronn constant (functional-equation value)
KAPPA = (np.sqrt(10 - 2*np.sqrt(5)) - 2) / (np.sqrt(5) - 1)     # ~ 0.2841
def a_zeta(n):  return 1.0
def a_Lchi3(n): return chi3(n)
def a_DH(n):    z = chi5(n); return z.real + KAPPA*z.imag        # real coefficients

print("="*82)
print(f"N9 certificate -- cross-prime fusion closure as the RH-respecting invariant   (DH kappa={KAPPA:.4f})")
print("="*82)

print("\n(1)+(2)  cross-prime multiplicativity defect  |a_pq - a_p a_q|  (=0 iff Euler/fusion-closed)")
print(f"  {'(p,q)':>9} {'zeta':>8} {'L(chi3)':>9} {'DH':>10}")
pairs = [(2,3),(3,7),(2,7),(7,13),(3,13),(2,13),(7,11),(3,11)]
maxz = maxl = 0.0; dh_any = 0.0
for (p,q) in pairs:
    dz = abs(a_zeta(p*q)-a_zeta(p)*a_zeta(q))
    dl = abs(a_Lchi3(p*q)-a_Lchi3(p)*a_Lchi3(q))
    dh = abs(a_DH(p*q)-a_DH(p)*a_DH(q))
    maxz = max(maxz, dz); maxl = max(maxl, dl); dh_any = max(dh_any, dh)
    print(f"  {str((p,q)):>9} {dz:>8.4f} {dl:>9.4f} {dh:>10.4f}")
print(f"  max defect:  zeta={maxz:.1e}  L(chi3)={maxl:.1e}  DH(max)={dh_any:.4f}")
print(f"  => zeta, L(chi3) fusion-closed (defect 0 EXACTLY); DH NOT (defect up to {dh_any:.3f}).")

print("\n(3)  order-3 adds nothing past order-2:  triple defect  a_pqr - a_p a_q a_r")
print("     (logically, a_pqr = a_p a_q a_r is IMPLIED by pairwise closure applied twice:")
print("      a_pqr = a_{(pq)r} = a_pq a_r = (a_p a_q) a_r; so the cubic vertex is downstream of order-2.)")
print(f"  {'(p,q,r)':>13} {'zeta':>9} {'L(chi3)':>10} {'DH':>9}")
for (p,q,r) in [(2,3,7),(3,7,13),(2,3,13),(7,13,17)]:
    tz = abs(a_zeta(p*q*r)-a_zeta(p)*a_zeta(q)*a_zeta(r))
    tl = abs(a_Lchi3(p*q*r)-a_Lchi3(p)*a_Lchi3(q)*a_Lchi3(r))
    td = abs(a_DH(p*q*r)-a_DH(p)*a_DH(q)*a_DH(r))
    print(f"  {str((p,q,r)):>13} {tz:>9.1e} {tl:>10.1e} {td:>9.4f}")
print("  => fusion-closed (zeta,L): triple defect 0. DH: nonzero, but only because PAIRWISE")
print("     already fails -- the order-3 vertex imposes no constraint absent at order-2.")

print("\n" + "="*82)
print("VERDICT")
print("="*82)
print("""  The invariant separating RH-respecting from RH-violating (functional-equation) Dirichlet
  series is CROSS-PRIME MULTIPLICATIVITY = the EULER PRODUCT = cross-prime fusion closure.
  zeta and primitive L respect it (defect 0, exact); Davenport-Heilbronn violates it (defect != 0)
  and indeed has off-line zeros (DH 1936). The order-3 vertex adds nothing past order-2.

  NECESSARY, NOT SUFFICIENT. This is the Selberg-class Euler axiom. It cleanly EXCLUDES the
  known counterexamples (a genuine No-Go) but does not prove RH: 'Euler product + functional
  equation => RH' is Selberg's conjecture, open. Operator-theoretically, fusion closure is the
  tensor factorization H = (x)_p H_p (multiplicative skeleton); self-adjointness -- eigenvalues
  on the line -- is the residual ARCHIMEDEAN positivity (N5; Connes-Consani), which fusion
  closure does not supply. Conclusion: N9 characterizes the class and discharges DH; the residue
  is archimedean, not multiplicative.""")
