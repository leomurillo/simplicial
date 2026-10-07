"""
Recast the energy contraction from the RADIAL (amplitude) coordinate to the ANGULAR (phase) one,
following the Elkies max-entropy grounding (RH lives in the phase, the amplitude is its phase-blind
square).

de Branges object E_B(t) = Xi(t) + i Xi'(t).  Two coordinates:
  RADIAL   |E_B|^2 = Xi^2 + Xi'^2   (amplitude; smooth, positive; our energy metric A is this kind of
           object -- a quadratic form weighted by Omega_inf).
  ANGULAR  phi(t) = arg E_B = atan2(Xi', Xi)   (phase; winds by pi at each zero).

Three checks:
  A  ZEROS ARE PHASE EVENTS, not amplitude events: at a zero gamma (Xi=0), E_B=i Xi' so arg E_B=+-pi/2
     (phase passes through +-pi/2) while |E_B|^2 = Xi'^2 != 0 (amplitude is BLIND to the zero).
  B  the archimedean PHASE VELOCITY theta'(T) = (1/2) Omega_inf(T), Omega_inf(T)=Re psi(1/4+iT/2)-log pi
     -- i.e. OUR energy-metric weight, now as a LINEAR phase rate (radial reference of the phase).
  C  the prime PHASE FLUCTUATION S(T) = N(T) - theta(T)/pi - 1 (the angular deviation; bounded = RH-side).
     N(T)=theta/pi+1+S(T): radial (theta, archimedean, growing ~log T) + angular (S, prime, bounded).

So the contraction recast: amplitude ρ_E<=1 used Omega_inf as a QUADRATIC weight (phase-blind square,
hence marginal). The ANGULAR version uses the SAME Omega_inf as the phase velocity theta'; RH = the prime
phase fluctuation S' never overcomes theta' (phi' keeps its sign = de Branges m_B Herglotz / Laguerre) --
the prime enters LINEARLY (the arrow), not quadratically.

No torch. mpmath. Deterministic.
"""
import mpmath as mp
mp.mp.dps = 25

def xi(s): return mp.mpf(1)/2*s*(s-1)*mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s)
def Xi(t): return mp.re(xi(mp.mpf(1)/2 + 1j*mp.mpf(t)))
def dXi(t): return mp.diff(Xi, t)
def Omega(T): return mp.re(mp.digamma(mp.mpf(1)/4 + 1j*T/2)) - mp.log(mp.pi)
def theta(T): return mp.im(mp.loggamma(mp.mpf(1)/4 + 1j*T/2)) - (T/2)*mp.log(mp.pi)

GAM = [mp.im(mp.zetazero(n)) for n in range(1, 31)]    # first 30 zeros (for N(T))

print("=" * 84)
print("Recast: RH lives in the PHASE (angular), the amplitude is its phase-blind square")
print("=" * 84)

print("\nA. zeros are PHASE events, not amplitude events  (at gamma: arg E_B = +-pi/2, |E_B|^2 = Xi'^2 != 0):")
print(f"   {'zero gamma':>12} {'Xi(gamma)~0':>14} {'arg E_B (=+-pi/2)':>18} {'|E_B|^2 (=Xi'+chr(39)+'^2)':>18}")
for g in GAM[:4]:
    X = Xi(g); dX = dXi(g); EB = X + 1j*dX
    print(f"   {mp.nstr(g,8):>12} {mp.nstr(X,3):>14} {mp.nstr(mp.arg(EB),6):>18} {mp.nstr(abs(EB)**2,6):>18}")
print("   => the amplitude |E_B|^2 does NOT vanish at the zero (phase-blind); the zero is where the PHASE")
print("      passes pi/2. RH-content (the zeros) is in the angular coordinate, not the radial.")

print("\nB. archimedean PHASE VELOCITY theta'(T) = (1/2) Omega_inf(T) = (1/2) our energy-metric weight:")
print(f"   {'T':>8} {'theta'+chr(39)+'(T) [num]':>16} {'Omega_inf(T)/2':>16} {'match?':>8}")
for T in (10, 14.135, 30, 60):
    T = mp.mpf(T); tp = mp.diff(theta, T); half = Omega(T)/2
    print(f"   {mp.nstr(T,5):>8} {mp.nstr(tp,8):>16} {mp.nstr(half,8):>16} {'YES' if abs(tp-half)<mp.mpf(10)**(-6) else 'no':>8}")
print("   => the archimedean phase velocity IS Omega_inf/2 -- the SAME 2pi-hinge weight A carries, now")
print("      as a LINEAR phase rate (the radial reference of the phase), not a quadratic amplitude weight.")

print("\nC. prime PHASE FLUCTUATION S(T)=N(T)-theta(T)/pi-1 (angular deviation; bounded = RH-side):")
print(f"   {'T':>8} {'N(T)':>6} {'theta(T)/pi+1':>14} {'S(T) (angular)':>16}")
for T in (15, 20, 25, 30, 35):
    T = mp.mpf(T); N = sum(1 for g in GAM if g <= T)
    base = theta(T)/mp.pi + 1; S = N - base
    print(f"   {mp.nstr(T,4):>8} {N:>6} {mp.nstr(base,7):>14} {mp.nstr(S,4):>16}")
print("   => N(T) = theta/pi+1 (RADIAL archimedean phase, growing ~ (T/2pi)log T) + S(T) (ANGULAR prime")
print("      fluctuation, O(log T) bounded). RH = the angular S(T) stays small (Selberg O(log T/loglog T)).")

print("\n" + "=" * 84)
print("""SYNTHESIS — the recast:
  * Our energy contraction rho_E = lambda_max(A^-1/2 P A^-1/2) <= 1 lived in the RADIAL/AMPLITUDE
    coordinate: A weights by Omega_inf as a QUADRATIC form (|E_B|^2-type) -- and by the Elkies grounding
    that is the phase-BLIND square (= KL = |S_chi|^2), which is exactly WHY it was marginal/free-shaped.
  * The ANGULAR recast keeps the SAME archimedean object Omega_inf but uses it as the PHASE VELOCITY
    theta' = Omega_inf/2 (B). RH is then the phase statement: the prime phase fluctuation S(T) (C) -- the
    LINEAR (additive, arrow) prime sum -- never overcomes the archimedean phase velocity, i.e. phi'(t)
    keeps its sign = m_B=-Xi'/Xi Herglotz = the de Branges monotone clock. The prime enters LINEARLY
    (the arrow Xi'), not quadratically.
  * NET: same primes, same archimedean Omega_inf, but the RH-bearing comparison is PHASE-vs-PHASE
    (theta' vs S', linear) -- not AMPLITUDE-vs-AMPLITUDE (A vs P, quadratic, the phase-blind square that
    gave the marginal rho_E). This is the Elkies/(Z/p)^x-max-entropy reason the program's de Branges
    arrow Xi' / m_B-Herglotz / phi'>=0 is the RH-native object and the quadratic Weil/Bures form is free.
  The open inequality in the right (angular) coordinate: theta'(t) >= -pi S'(t) for all t (phi' one-signed)
  -- arch-domination as a PHASE bound on the linear prime arrow, the additive object, not the Bures square.
""")
print("=" * 84)
