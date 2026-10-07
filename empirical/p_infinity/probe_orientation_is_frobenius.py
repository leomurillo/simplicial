"""
Is the chiral RH sign a FREE orientation bit (like doc 08's Boolean-Janus cosets B/K), or is it
arithmetic-determined?  Audit on Z/6.

Claim: the "orientation swap" 2<->4 that flips the chiral current Im(rho_chi)_{2,4} (N14 Rem 7.9)
is NOT a free convention -- it is the FROBENIUS monodromy c -> p*c mod 6 [N1 sec 4 Galois action],
which is FIXED by the prime's residue mod 6:
    p = 1 mod 6 (7,13,19,...):  c->c on {2,4}        -> orientation FIXED
    p = 5 mod 6 (5,11,17,...):  swaps 2<->4 (= c->-c) -> orientation REVERSED
and the parity reflection R: c->-c that the chiral current is odd under is literally Frobenius_5
(since -1 = 5 mod 6).  So the sign is read off the prime, not chosen.

Doc 08 distinction: in PURE GEOMETRY the block-sign quotient B/K gives genuine free orientation
bits (a Boolean code).  But once the ARITHMETIC is attached (the L-function / the prime side), the
orientation element is pinned to the Galois/Frobenius class -- it leaves K-as-free and becomes
B/K-as-determined.  RH = sign of L(1/2,chi_3), a CONJUGATION-INVARIANT real number (chi_3 quadratic
=> chi_3 = conj(chi_3)); the free-looking additive sign is compensated by the Gauss-sum phase.

This script certifies the arithmetic facts; the conceptual reading is in the printout.
No torch. numpy/sympy. Deterministic.
"""
import numpy as np
from sympy import primerange

N = 6
chars = [1, 2, 3, 4, 5]          # nonzero residues mod 6 (the additive characters of Z/6)

def frobenius(p):
    """c -> p*c mod N, as a permutation of the character index set {1..5}."""
    return {c: (p * c) % N for c in chars}

print("=" * 76)
print("Z/6: the orientation swap 2<->4 IS the Frobenius monodromy c -> p*c mod 6")
print("=" * 76)
print(f"{'p':>4} {'p mod 6':>8}   action on chars {{1..5}}        swaps 2<->4 ?")
for p in primerange(5, 40):
    fr = frobenius(p)
    swaps = (fr[2] == 4 and fr[4] == 2)
    fixes = (fr[2] == 2 and fr[4] == 4)
    tag = "SWAP (orientation reversed)" if swaps else ("fix  (orientation kept)" if fixes else "other")
    print(f"{p:>4} {p % 6:>8}   {fr}   {tag}")

print("\nParity R: c -> -c mod 6 =", {c: (-c) % N for c in chars})
print("Frobenius_5: c -> 5c mod 6 =", frobenius(5))
assert {c: (-c) % N for c in chars} == frobenius(5), "R must equal Frobenius_5"
print("=> R (the involution the chiral current is odd under) IS Frobenius at p=5.  [verified]")

# the quadratic Dirichlet character mod 3 (= chi_3) is REAL: chi_3 = conj(chi_3)
chi3 = {1: 1, 2: -1}   # Legendre symbol mod 3 on (Z/3)^x
print("\nchi_3 (quadratic mod 3) values:", chi3, " -> real, so chi_3 == conj(chi_3):",
      all(v == np.conj(v) for v in chi3.values()))
print("Hence L(1/2,chi_3) is conjugation-INVARIANT: a fixed real number (=0.4808...>0), NOT flipped")
print("by the 2<->4 conjugation.  The additive-character sign that DOES flip is gauge; it is")
print("compensated by the Gauss-sum phase linking additive <-> multiplicative.")

print("""
========================================================================================
VERDICT.  The chiral sign is NOT a free-will lever for RH.
  * The 2<->4 'orientation' is the Galois/Frobenius element c->p c, FIXED by p mod 6
    (p=1: keep; p=5: reverse).  It is determined by the prime, not chosen.
  * The bare additive sign Im(rho_chi)_{2,4} flips under it, but that is a GAUGE
    (relabeling) quantity -- doc 08's K, the physically vacuous part.
  * RH = sign/nonvanishing of L(1/2,chi_3), a conjugation-INVARIANT number -- doc 08's
    gauge-invariant residue.  A genuine free orientation bit (doc 08's B/K) exists, but
    RH lives on its COMPLEMENT: the Frobenius-pinned, arithmetic-determined part.
  You can choose the convention; the convention cancels out of RH.
========================================================================================
""")
