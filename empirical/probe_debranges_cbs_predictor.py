"""
(2) Pin the de Branges <-> CBS-predictor identification for the zeta operator.

CLAIM. The de Branges function E_B(z) = Xi(z) + i Xi'(z) IS the CBS predictor block
for zeta, with the 2x2 real block
        B(z) = Xi(z) I + Xi'(z) J,     J = [[0,1],[-1,0]],
whose eigenvalues are Xi +/- i Xi' = E_B, E_B^*.  In CBS language (T = S + A):
   - Xi   = the SYMMETRIC part S  (even in z; what the single-encoder / Hankel / (GBP)
            quadratic form can read);
   - Xi'  = the ANTISYMMETRIC part A = the CURRENT / arrow of time (odd in z; in the
            kernel of every real quadratic form -- CBS Lemma 1);
   - m_B = -Xi'/Xi Herglotz  <=>  RH  =  "the arrow is correctly phased", a reading
            available only to the predictor (the full block B), not to v^T B v.

Four certificates:
  A. SKEW VANISHES: v^T B v = Xi |v|^2 exactly -- the quadratic form is BLIND to the
     arrow Xi'.  (CBS Lemma 1 / the Irreversible Blind Spot, for zeta.)
  B. FUNCTIONAL EQUATION = TIME REVERSAL: Xi even, Xi' odd  =>  E_B(-z) = conj(E_B(z))
     = E_B^*(z).  The map z -> -z (i.e. s -> 1-s) is the CBS time-reversal B -> B^T,
     which flips the arrow Xi' -> -Xi'.
  C. m_B HERGLOTZ (RH-consistent): Im m_B(x+iy) > 0 throughout the sampled upper half
     plane; at a true zero gamma the pole has the Herglotz sign (residue of m_B = -1,
     i.e. m_B ~ +1/(gamma - z) with positive weight).
  D. THE BLIND SPOT, stated: the symmetric reading Xi is reversal-invariant while the
     arrow Xi' flips -- zeta and its time-reverse share a loss landscape; the arrow is
     unrecoverable by the symmetric quadratic, recoverable by the predictor.

Deterministic: mpmath only. No torch.
"""

import mpmath as mp
mp.mp.dps = 30

def xi(s):
    return mp.mpf(1) / 2 * s * (s - 1) * mp.pi**(-s / 2) * mp.gamma(s / 2) * mp.zeta(s)
def Xi(z):
    return xi(mp.mpf(1) / 2 + 1j * z)
def dXi(z):
    return mp.diff(Xi, z)

J = mp.matrix([[0, 1], [-1, 0]])

# ============================================================================
print("=" * 78)
print("A. SKEW VANISHES -- the quadratic form reads Xi, is BLIND to the arrow Xi'")
print("=" * 78)
for zr in ['6.0', '10.0', '12.0']:
    z = mp.mpf(zr)
    a = mp.re(Xi(z)); b = mp.re(dXi(z))          # Xi real, Xi' real on the line
    B = mp.matrix([[a, b], [-b, a]])
    for v0, v1 in [(mp.mpf('0.7'), mp.mpf('-1.3')), (mp.mpf('1.0'), mp.mpf('2.0'))]:
        vTBv = v0 * (a * v0 + b * v1) + v1 * (-b * v0 + a * v1)
        target = a * (v0**2 + v1**2)
        print(f"  z={zr:>5}: Xi={float(a):+.6e}  arrow Xi'={float(b):+.6e}  "
              f"|v^TBv - Xi|v|^2|={float(abs(vTBv - target)):.1e}")
    ev = mp.eig(B, left=False, right=False)
    eb = a + 1j * b
    print(f"          eig(B) = {complex(ev[0]):.5f}, {complex(ev[1]):.5f}   "
          f"E_B = Xi+iXi' = {complex(eb):.5f}")
print("  >>> v^T B v = Xi|v|^2 to machine precision: the arrow Xi' is in the kernel of")
print("      the quadratic form (CBS Lemma 1). eig(B) = Xi +/- i Xi' = E_B, E_B^*.")

# ============================================================================
print()
print("=" * 78)
print("B. FUNCTIONAL EQUATION s->1-s  ==  z->-z  ==  CBS time-reversal B -> B^T")
print("=" * 78)
for zr in ['8.3', '14.7', '23.1']:
    z = mp.mpf(zr)
    even_err = abs(Xi(-z) - Xi(z))
    odd_err = abs(dXi(-z) + dXi(z))
    EB = Xi(z) + 1j * dXi(z)
    EBflip = Xi(-z) + 1j * dXi(-z)
    rev_err = abs(EBflip - mp.conj(EB))
    print(f"  z={zr:>5}: |Xi(-z)-Xi(z)|={float(even_err):.1e}  "
          f"|Xi'(-z)+Xi'(z)|={float(odd_err):.1e}  |E_B(-z)-conj E_B(z)|={float(rev_err):.1e}")
print("  >>> Xi even, Xi' odd  =>  E_B(-z) = conj E_B(z) = E_B^*.  The arrow flips under")
print("      the functional equation: it IS the CBS time-reversal that swaps the charts.")

# ============================================================================
print()
print("=" * 78)
print("C. m_B = -Xi'/Xi HERGLOTZ (RH-consistent): Im m_B > 0 on C+, Herglotz pole sign")
print("=" * 78)
def mB(z):
    return -dXi(z) / Xi(z)
ok = True
print(f"  {'x':>6} {'y':>5} {'Im m_B':>16}")
for x in ['5', '10', '17', '21', '25']:
    for y in ['0.4', '1.0', '3.0']:
        z = mp.mpf(x) + 1j * mp.mpf(y)
        im = mp.im(mB(z))
        if im <= 0:
            ok = False
        print(f"  {x:>6} {y:>5} {float(im):>16.6e}")
print(f"  >>> Im m_B > 0 at every sampled point: {'OK (Herglotz / RH-consistent)' if ok else 'CHECK'}")
g1 = mp.im(mp.zetazero(1))
eps = mp.mpf('1e-8')
res = (mp.mpf('0') + eps) * 0  # placeholder
res = eps * mB(g1 + eps)       # (z-g1)*m_B  ->  residue
print(f"  zero gamma_1={float(g1):.6f}: Xi(gamma_1)={float(abs(Xi(g1))):.1e} (~0); "
      f"residue of m_B = {float(mp.re(res)):+.4f} (= -1 => m_B ~ +1/(gamma-z), Herglotz sign)")

# ============================================================================
print()
print("=" * 78)
print("D. THE BLIND SPOT FOR ZETA (summary)")
print("=" * 78)
print("""  Xi  (symmetric S, even)  is reversal-invariant: zeta and its time-reverse give
  the SAME symmetric reading -- the Hankel / (GBP) / single-encoder quadratic v^TBv=Xi|v|^2
  cannot tell them apart.  Xi' (antisymmetric A = the current/arrow, odd) FLIPS under
  s->1-s.  So the arrow is in the kernel of the quadratic instrument and is read only by
  the predictor (the full block B / the SVD / E_B).  RH = m_B=-Xi'/Xi Herglotz = the
  arrow is purely phased.  This is the Irreversible Blind Spot, for the zeta operator.""")
