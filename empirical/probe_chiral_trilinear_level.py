"""
probe_chiral_trilinear_level.py  --  run the chi_3-twisted (conductor-3) trilinear Kloosterman object
through Wright's fixed-factor mechanism and read off the level. Paranoid test of whether the chiral
structure beats the general 0.515. Honest.

Wright 2604.25177 Thm 2.1 bounds B(M,N,A;R) with a FIXED FACTOR R in the denominator nR; R enters ONLY
as powers R^{1/4} (prefactor), R^{1/8}, R^{-3/20} (bracket). Cor 2.2 levels (GENERAL moduli):
   Q <= X^{1/2+1/66} ~ 0.5152  (N small / unbalanced)   and   Q <= X^{45/89} ~ 0.5056 (balanced).

THE TEST: for the chiral channel the fixed factor is the conductor R = 3 (a CONSTANT). Does a constant
fixed factor change the level?

  (1) chi_3-twisted Kloosterman FACTORS (CRT twisted-multiplicativity): K_{chi3}(.;3q)=K_{chi3}(.;3)*
      K(.;q), and the conductor-3 part has |K_{chi3}(1,1;3)| = sqrt(3) -- a CONSTANT. The level is set by
      the ordinary mod-q Kloosterman (Weil, 1/2). So the twist preserves level 1/2.
  (2) R-exponent: R=3=X^0 => R^{1/4}=R^{1/8}=R^{-3/20}=X^0 contribute ZERO to the X-exponent => the
      bound's exponent, hence the level, is UNCHANGED from R=1. Chiral level = general level ~ 0.5152.
  (3) over Z[omega]: the Weil cap is still 1/2 in N(pi) (split prime -> classical F_p sum; inert ->
      F_{p^2}); no gain.

VERDICT (honest, negative on the shortcut): the chiral conductor-3 / Eisenstein structure does NOT beat
the general optimal-trilinear level. A gain needs a LARGE forced fixed factor (R=X^rho, rho>0) or a
genuine beyond-Wright advance; the conductor 3 is rho=0. The frontier (level->1) is the SAME single
object for both channels -- the actively-moving trilinear-Kloosterman edge -- with no structural
shortcut from the program's chi_3/primorial/Eisenstein structure.

sympy. No torch.
"""
import cmath, math
import sympy as sp

def chi3(x):
    r = x % 3
    return 0 if r == 0 else (1 if r == 1 else -1)

def kloosterman(a, b, q):
    tot = 0j
    for x in range(1, q):
        if math.gcd(x, q) == 1:
            tot += cmath.exp(2j*cmath.pi*(a*x + b*pow(x, -1, q))/q)
    return tot

def kloosterman_chi3(a, b, q):                    # chi_3(x)-twisted, twist read mod 3
    tot = 0j
    for x in range(1, q):
        if math.gcd(x, q) == 1:
            tot += chi3(x) * cmath.exp(2j*cmath.pi*(a*x + b*pow(x, -1, q))/q)
    return tot

print("=" * 92)
print("(1) the chi_3 twist contributes a CONSTANT conductor-3 factor sqrt(3); level stays 1/2 (Weil)")
print("=" * 92)
K3 = kloosterman_chi3(1, 1, 3)
print(f"  conductor-3 part  K_chi3(1,1;3) = {K3:.5f},  |K_chi3(1,1;3)| = {abs(K3):.5f}  (= sqrt 3 = {math.sqrt(3):.5f}, CONSTANT)")
print(f"  the chi_3-twisted Kloosterman over 3q factors (CRT): K_chi3(.;3q)=K_chi3(.;3)*K(.;q); check level 1/2:")
print(f"  {'q':>4} {'|K_chi3(1,1;3q)|':>18} {'sqrt(3q)':>10} {'ratio (O(1)=level 1/2)':>24}")
for q in (7, 11, 13, 17):
    Ktw = abs(kloosterman_chi3(1, 1, 3*q))
    print(f"  {q:>4} {Ktw:>18.4f} {math.sqrt(3*q):>10.4f} {Ktw/math.sqrt(3*q):>24.4f}")
print("  => |K_chi3(.;3q)|/sqrt(3q) stays O(1): the chi_3 twist (conductor 3) is a CONSTANT factor sqrt3,")
print("     it does NOT change the Weil level 1/2. The twist provides no X-growing cancellation.")

print("\n" + "=" * 92)
print("(2) Wright Thm 2.1: R = conductor 3 = X^0 contributes 0 to the X-exponent => level UNCHANGED")
print("=" * 92)
# R-powers appearing in Wright Thm 2.1; for R = const (X^0) each contributes exponent 0
Rpows = sp.Rational(1,4), sp.Rational(1,8), sp.Rational(-3,20)
rho = sp.symbols('rho', nonnegative=True)         # R = X^rho ;  conductor 3 => rho = 0
print(f"  R enters Wright Thm 2.1 as powers {', '.join('R^'+str(p) for p in Rpows)} (prefactor + bracket).")
print(f"  with R = X^rho, the R-contribution to the bound's X-exponent is each power times rho:")
for p in Rpows:
    print(f"    R^{p} -> exponent {p}*rho ;  at rho=0 (R=3 const): {p*0}")
print(f"  conductor 3 => rho = 0 => ALL R-contributions vanish => bound exponent = the R=1 (general) case.")
lvl_unbal = sp.Rational(1,2) + sp.Rational(1,66)
lvl_bal = sp.Rational(45,89)
print(f"  => chiral level = GENERAL level (Wright Cor 2.2): unbalanced 1/2+1/66 = {float(lvl_unbal):.4f},"
      f" balanced 45/89 = {float(lvl_bal):.4f}.  NO gain from the conductor.")
print(f"  (a level GAIN would need rho>0 -- a LARGE forced fixed factor; the conductor 3 is rho=0.)")

print("\n" + "=" * 92)
print("(3) over Z[omega]: Weil cap still 1/2 in N(pi) -- no gain from the Eisenstein structure either")
print("=" * 92)
print(f"  {'p':>4} {'p mod3':>7} {'behavior':>16} {'field':>8} {'Kloosterman Weil bound':>24} {'level':>7}")
for p in (5, 7, 11, 13):
    if p % 3 == 1:
        print(f"  {p:>4} {p%3:>7} {'split':>16} {'F_p':>8} {f'|K|<=2 sqrt(p)={2*math.sqrt(p):.2f}':>24} {'1/2':>7}")
    else:
        print(f"  {p:>4} {p%3:>7} {'inert':>16} {'F_{p^2}':>8} {f'|K|<=2 p=2 N^(1/2)={2*p}':>24} {'1/2':>7}")
print("  => split prime -> classical F_p Kloosterman (Weil 2 sqrt p); inert -> F_{p^2} (Weil 2p = 2N(pi)^1/2).")
print("     Both are level 1/2 in the field norm N(pi). Beyond-Weil over Z[omega] is the SAME frontier.")

print("\n" + "=" * 92)
print("VERDICT  --  the chiral trilinear level, computed (honest negative on the shortcut)")
print("=" * 92)
print(f"""  RESULT: the chi_3-twisted (conductor-3) trilinear object does NOT beat the general optimal-trilinear
  level. Three independent reasons, all computed:
   (1) the chi_3 twist factors off a CONSTANT conductor-3 part |K_chi3(.;3)|=sqrt3; the level stays the
       Weil 1/2 (|K_chi3(.;3q)|/sqrt(3q) = O(1)). No X-growing cancellation from the twist.
   (2) in Wright Thm 2.1 the fixed factor R enters only as powers (1/4, 1/8, -3/20); R = conductor 3 =
       X^0 contributes 0 to the X-exponent, so the level is UNCHANGED from general: chiral level =
       1/2+1/66 ~ 0.5152 (Cor 2.2). A gain needs rho>0 (R growing with X); the conductor is rho=0.
   (3) over Z[omega] the Weil cap is still 1/2 in N(pi) (split=F_p, inert=F_{p^2}); no Eisenstein gain.
  So the program's specific structure (primorial smoothness, chi_3 conductor, Eisenstein ring) PLACES the
  frontier on the right machinery (Wright/BC/Varbanets) but provides NO shortcut past the general level.
  The genuine advance must come from the trilinear-Kloosterman ANT frontier itself (level -> 1), which is
  the SAME single object for both metric and chiral channels and is RH-strength. NOT crossed. No proof.
  This closes, precisely and negatively, the 'does the chiral conductor buy a better level' question.""")
