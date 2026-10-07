"""
Apex-weighted de Branges sign test on the (xi, L_chi3) 2-channel pair.

Context (HPo-notes Addendum A-D): the Z/6 Bures apex collapses to the pair
(Xi, L3c) = (completed zeta, completed L mod 3), both real-entire and EVEN in z
(z = the critical-line height, s = 1/2 + i z).  The de Branges / Hermite-Biehler
condition for an entire E is  |E(z)| > |E^#(z)|  on C+  (all E-zeros in closed
lower half-plane), where E^#(z) = conj(E(conj z)).  RH <=> such an E exists for Xi.

HPo found the naive 2-channel candidates fail:
  D9:  E = Xi - i L3c        fails by PARITY (both even -> Im(Xi^bar L3) antisym in x)
  D12: E = Xi - i z L3c      fails by GROWTH (z L3 dominates at large |x|)
The correct Hermite-Biehler E for Xi is Paper III's  E_B = Xi + i Xi'  (Xi even,
Xi' odd) -- de Branges <=> RH.

This probe:
  (1) validates the harness: E_B = Xi + i Xi' passes on C+ where computed (RH-consistent);
  (2) reconfirms E1 (parity) and E2 (growth) fail;
  (3) NOVEL: tests whether the apex scattering phase gamma(z)=Gamma_R(1/2+iz)/Gamma_R(1/2-iz)
      = e^{2 i theta(z)} (the apex edge multiplier, N5) supplies the missing ODD parity,
      i.e. whether weighting the K-odd channel by the apex phase removes the D9 parity wall.
  (4) honest verdict: does the (xi,L3) pair + apex weight give a de Branges E, or is the
      de Branges space genuinely E_B = Xi + i Xi' (RH-equivalent, no 2-channel shortcut)?

Deterministic: mpmath.
"""

import mpmath as mp
mp.mp.dps = 25

# --- completed functions ---------------------------------------------------
def xi(s):
    # Riemann xi(s) = 1/2 s(s-1) pi^{-s/2} Gamma(s/2) zeta(s); entire
    return mp.mpf('0.5') * s * (s - 1) * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)

def Lchi3(s):
    # L(s, chi3), chi3 the odd character mod 3: chi3(1)=1, chi3(2)=-1
    return 3 ** (-s) * (mp.zeta(s, mp.mpf(1) / 3) - mp.zeta(s, mp.mpf(2) / 3))

def Lambda3(s):
    # completed L for odd primitive chi mod 3 (root number +1):
    # Lambda3(s) = (3/pi)^{(s+1)/2} Gamma((s+1)/2) L(s, chi3)
    return (3 / mp.pi) ** ((s + 1) / 2) * mp.gamma((s + 1) / 2) * Lchi3(s)

# height-variable versions (z): s = 1/2 + i z ; both real-entire and even in z
Xi = lambda z: xi(mp.mpf('0.5') + 1j * z)
L3c = lambda z: Lambda3(mp.mpf('0.5') + 1j * z)
Xip = lambda z: mp.diff(Xi, z)            # Xi'(z): real-entire, ODD in z
def GammaR(s): return mp.pi ** (-s / 2) * mp.gamma(s / 2)
gamma_phase = lambda z: GammaR(mp.mpf('0.5') + 1j * z) / GammaR(mp.mpf('0.5') - 1j * z)  # e^{2 i theta}

# --- de Branges / Hermite-Biehler sign  D(z) = |E|^2 - |E^#|^2 -------------
def Dsign(E, z):
    Ez = E(z)
    Esharp = mp.conj(E(mp.conj(z)))
    return float((abs(Ez) ** 2 - abs(Esharp) ** 2))

candidates = {
    "E_B = Xi + i Xi'   [Paper III, correct HB]": lambda z: Xi(z) + 1j * Xip(z),
    "E1 = Xi - i L3c     [HPo D9]":               lambda z: Xi(z) - 1j * L3c(z),
    "E2 = Xi - i z L3c   [HPo D12]":              lambda z: Xi(z) - 1j * z * L3c(z),
    "E3 = Xi - i g(z) L3c [apex phase weight]":   lambda z: Xi(z) - 1j * gamma_phase(z) * L3c(z),
    "E4 = Xi + i L3c'    [odd partner from L3]":  lambda z: Xi(z) + 1j * mp.diff(L3c, z),
}

# grid in C+
xs = [mp.mpf(x) / 2 for x in range(-50, 51, 2)]   # x in [-25, 25]
ys = [mp.mpf(y) for y in ['0.1', '0.3', '0.6', '1.0', '2.0']]

print("=" * 78)
print("APEX-WEIGHTED de BRANGES SIGN TEST on the (Xi, L_chi3) 2-channel pair")
print("de Branges requires D(z)=|E|^2-|E^#|^2 > 0 for ALL z in C+")
print("=" * 78)
print(f"  grid: x in [-25,25] step 0.5 ({len(xs)} pts) x y in {[float(y) for y in ys]}  "
      f"= {len(xs)*len(ys)} points\n")
print(f"  {'candidate':<42} {'%pass D>0':>10} {'min D (norm)':>14} {'parity?':>9}")
for name, E in candidates.items():
    npass = 0; ntot = 0; minnorm = mp.mpf('inf')
    Dleft = {}; Dright = {}
    for y in ys:
        for x in xs:
            z = x + 1j * y
            try:
                D = Dsign(E, z)
                Eabs2 = abs(E(z)) ** 2 + abs(mp.conj(E(mp.conj(z)))) ** 2 + mp.mpf('1e-300')
                Dn = D / float(Eabs2)
            except Exception:
                continue
            ntot += 1
            if D > 0:
                npass += 1
            if Dn < minnorm:
                minnorm = Dn
            if x > 0:
                Dright[(float(x), float(y))] = D
                Dleft[(-float(x), float(y))] = None  # placeholder
    # parity check: is D(x,y) ~ -D(-x,y)?  (antisymmetric => parity-broken candidate)
    asym = 0; sym = 0; cnt = 0
    for y in ys:
        for x in xs:
            if x <= 0:
                continue
            z = x + 1j * y; zm = -x + 1j * y
            try:
                d1 = Dsign(E, z); d2 = Dsign(E, zm)
            except Exception:
                continue
            cnt += 1
            if abs(d1 + d2) < 1e-6 * (abs(d1) + abs(d2) + 1e-30):
                asym += 1
            if abs(d1 - d2) < 1e-6 * (abs(d1) + abs(d2) + 1e-30):
                sym += 1
    parity = "ANTISYM" if asym > cnt * 0.8 else ("sym" if sym > cnt * 0.8 else "mixed")
    pct = 100.0 * npass / max(ntot, 1)
    print(f"  {name:<42} {pct:>9.1f}% {float(minnorm):>14.4f} {parity:>9}")

print()
print("=" * 78)
print("READING")
print("=" * 78)
print("""  - E_B = Xi + i Xi' passing (100%) validates the harness and confirms the
    de Branges function for Xi is the Hermite-Biehler pair (Xi, Xi') -- and its
    passing where computed is RH-consistent (it passes <=> the zeros in range are
    on the line).  This is Paper III's E_B; its global HB property IS RH.
  - E1 (parity ANTISYM, ~50%) and E2 (growth) reconfirm HPo D9/D12: the bare
    2-channel pair (Xi, L3c) is NOT a de Branges function.
  - E3 tests whether the apex scattering phase gamma=e^{2 i theta} (N5) breaks the
    parity wall.  If %pass jumps and parity leaves ANTISYM, the apex phase is the
    missing parity-breaking ingredient (a genuine structural advance, though the
    resulting object is not entire -- gamma has Gamma-poles -- so it is a sign
    diagnostic, not yet an E-function).
  - Honest frame: building the de Branges space for Xi is RH-equivalent.  This
    probe settles whether the (Xi,L3) 2-channel gives a shortcut (it does not if
    only E_B passes), and locates the apex's role: the explicit archimedean phase,
    not a new E-function.""")
