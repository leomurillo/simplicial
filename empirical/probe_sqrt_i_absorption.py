"""
probe_sqrt_i_absorption.py  --  is the apex 'sqrt(i) = 1/8 turn' arrow algebraically ABSORBABLE
(finite, like Andy Thomson's sqrt(3) in M = 4I - J), leaving ONLY the Gamma-envelope as the wall?

sqrt(i) = zeta_8 = e^{i pi/4} = (1+i)/sqrt(2),  zeta_8 in Q(zeta_8) = Q(i, sqrt2), degree 4.
The sqrt(2) is EXACTLY the T4 Helmert rung-1 (first prime) normalizer sqrt(1*2). Andy absorbs sqrt(3)
into M = 4I - J (tetrahedral / prime-3); the apex sqrt(i) should absorb into the prime-2 cyclotomic
metric the same way -- the surd cancels into the lattice, leaving exact integer entries.

PART 1  sqrt(i) = zeta_8 = (1+i)/sqrt2; sqrt2 = zeta_8 + zeta_8^{-1} = the prime-2 rung; deg Q(zeta_8)=4.
PART 2  EXACT ABSORPTION in Z[zeta_8] (companion C of Phi_8 = x^4+1): C = mult-by-zeta_8 is an INTEGER
        ORTHOGONAL matrix; C^2 = 'i', C^4 = -I, C^8 = I; sqrt2 = C + C^7 is an INTEGER matrix with
        (C+C^7)^2 = 2I; the trace-form metric is M = 4I (integer). No surd anywhere -- sqrt(i) and
        sqrt(2) are both absorbed into the lattice/metric. (The exact analog of Andy's sqrt3 -> rational.)
PART 3  what is NOT absorbable: the off-axis modulus. At s = 1/2 + it the apex phase is zeta_8 * e^{-pi t/2}
        and |Gamma(1/2+it)| = sqrt(pi / cosh(pi t)); the non-normality ratio is e^{pi t} -- TRANSCENDENTAL.
PART 4  verdict.

sympy (exact) + mpmath (the transcendental envelope). No torch.
"""
import sympy as sp
import mpmath as mp

x = sp.symbols('x')
I = sp.I

print("=" * 90)
print("PART 1  sqrt(i) = zeta_8 = (1+i)/sqrt2;  sqrt2 = zeta_8 + zeta_8^{-1} = T4 rung-1 (prime 2)")
print("=" * 90)
z8 = sp.exp(I * sp.pi / 4)
print(f"  sqrt(i)            = {sp.simplify(sp.sqrt(I))}   (principal)")
print(f"  zeta_8             = {sp.nsimplify(z8)} = {sp.simplify(z8)}")
print(f"  zeta_8 - (1+i)/√2  = {sp.simplify(z8 - (1 + I) / sp.sqrt(2))}   (==0 confirms sqrt(i)=(1+i)/√2)")
print(f"  zeta_8^2           = {sp.simplify(z8**2)}   (== i: zeta_8 is a square root of i)")
print(f"  zeta_8 + 1/zeta_8  = {sp.simplify(z8 + 1 / z8)}   (== √2 : the prime-2 / rung-1 normalizer √(1·2))")
print(f"  minimal poly of zeta_8 = Phi_8 = {sp.cyclotomic_poly(8, x)} ;  [Q(zeta_8):Q] = {sp.totient(8)}")
print("  => sqrt(i) is the order-8 cyclotomic landmark; its only surd is the rung-1 prime-2 √2.")

print("\n" + "=" * 90)
print("PART 2  EXACT ABSORPTION: in Z[zeta_8] (companion of x^4+1), sqrt(i) AND sqrt2 are INTEGER matrices")
print("=" * 90)
C = sp.Matrix([[0, 0, 0, -1],
               [1, 0, 0, 0],
               [0, 1, 0, 0],
               [0, 0, 1, 0]])                      # companion of Phi_8 = x^4 + 1  =  mult-by-zeta_8
Id = sp.eye(4)
print("  C = mult-by-zeta_8 (companion of x^4+1):")
sp.pprint(C)
print(f"  C integer?            {all(e.is_integer for e in C)}")
print(f"  C^2 (='i' rotation):  C^2 squares to -I?   {sp.simplify(C**2 * C**2 + Id) == sp.zeros(4)}")
print(f"  C^4 = -I ?            {C**4 == -Id}        C^8 = I ?   {C**8 == Id}")
print(f"  C orthogonal (C^T C = I)?   {C.T * C == Id}    => C is an EXACT integer rotation (no surd)")
S = C + C**7                                        # zeta_8 + zeta_8^{-1} = sqrt2
print("  sqrt2 = C + C^7 (= zeta_8 + zeta_8^{-1}):")
sp.pprint(S)
print(f"  S integer?  {all(e.is_integer for e in S)}    (C+C^7)^2 = 2I ?  {S * S == 2 * Id}   => √2 is an INTEGER matrix")
# trace-form metric M_jk = Tr(zeta^{j-k}) on basis 1,zeta,zeta^2,zeta^3
M = sp.Matrix(4, 4, lambda j, k: sp.simplify(sp.trace(C**((j - k) % 8)) if (j - k) % 8 != 0 else sp.Integer(4)))
print("  cyclotomic trace-form metric M (basis 1,ζ,ζ²,ζ³):")
sp.pprint(M)
print(f"  M = 4I (integer)?  {M == 4 * Id}    C^T M C = M ?  {C.T * M * C == M}   (C is M-orthogonal, exact)")
print("  => BOTH sqrt(i)=C and sqrt2=C+C^7 are exact integer matrices, M=4I-orthogonal. The surd is")
print("     absorbed into the prime-2 cyclotomic lattice -- the exact analog of Andy's sqrt3 in M=4I-J.")

print("\n" + "=" * 90)
print("PART 3  what is NOT absorbable: the transcendental Gamma-envelope (the actual non-normality)")
print("=" * 90)
mp.mp.dps = 25
print(f"  {'t':>5} {'|Gamma(1/2+it)|':>20} {'sqrt(pi/cosh(pi t))':>22} {'ratio |k~(1/2-it)|/|k~(1/2+it)|':>32}")
for t in (0.5, 1.0, 2.0):
    g = abs(mp.gamma(mp.mpf(1) / 2 + 1j * t))
    closed = mp.sqrt(mp.pi / mp.cosh(mp.pi * t))
    ratio = mp.e**(mp.pi * t)                       # = e^{pi t}, from |e^{i pi s/2}| = e^{-pi t/2}
    print(f"  {t:>5} {mp.nstr(g, 12):>20} {mp.nstr(closed, 12):>22} {mp.nstr(ratio, 12):>32}")
print("  => the off-axis modulus is sqrt(pi/cosh(pi t)) and the non-normality ratio is e^{pi t}:")
print("     transcendental (pi, cosh, exp) -- NOT in any Z[zeta_N]. This is the irreducible residue.")

print("\n" + "=" * 90)
print("VERDICT")
print("=" * 90)
print("""  The apex 'sqrt(i) = 1/8 turn' ARROW is a FINITE cyclotomic landmark: sqrt(i)=zeta_8 and its only
  surd, sqrt2 = the prime-2 / Helmert rung-1 normalizer, are BOTH exact integer matrices in Z[zeta_8]
  with the M=4I trace-form metric -- absorbed exactly, the same mechanism by which Andy's M=4I-J makes
  the tetrahedral (sqrt3) rotations rational. So sqrt(i) is NOT the obstruction; it is algebraically
  absorbable into the prime-2 conductor metric. The IRREDUCIBLE wall is the off-axis modulus alone --
  the transcendental Gamma-envelope sqrt(pi/cosh(pi t)) / the e^{pi t} non-normality ratio -- i.e. the
  archimedean L-factor positivity (Connes-Consani). Just as the exact-signature probe removed
  'marginality' from the wall, this removes 'sqrt(i)' from the wall: the residue is purely the
  transcendental Gamma-factor.""")
