"""
TWO threads:
  A (side thought)  "prove any three zeros are collinear" -- is it easier than RH?
  B (main)          the q->1 spectral-completion datum: what controls how finitely-many function-field
                    zeros DENSIFY into zeta_Q's spectrum?  Answer-candidate: the archimedean Gamma-factor.

A. COLLINEARITY.  Three points are collinear <=> the triangle area (a 2x2 determinant) vanishes.
   Claim: (every triple of zeros collinear)  <=>  RH.  Two ingredients:
     (i)  if every 3 points of a set are collinear, ALL are on one line (pick 2, the rest join them);
     (ii) the zero set is invariant under conjugation (rho<->rho_bar, Re-axis reflection) AND the FE
          (rho<->1-rho, reflection across Re=1/2).  A line invariant under BOTH is Re=1/2 or Im=0.
          The nontrivial zeros are not real -> Re=1/2 = RH.
   So collinearity <=> RH (NOT easier); concretely, an OFF-line zero's symmetric orbit
   {rho,1-rho,rho_bar,1-rho_bar} is a 2D RECTANGLE (non-collinear); on the line it degenerates to a
   vertical segment.  RH <=> every orbit degenerate.  The FE is what upgrades "collinear" to "on 1/2".

B. DENSIFICATION DATUM.  Riemann-von Mangoldt:  N(T) = theta(T)/pi + 1 + S(T),
   theta(T) = Im log Gamma(1/4 + iT/2) - (T/2) log pi   (the ARCHIMEDEAN Gamma-factor phase),
   S(T) = (1/pi) arg zeta(1/2+iT)   (the prime-side fluctuation).
   The MAIN term theta/pi+1 ~ (T/2pi) log(T/2pi) is the Gamma-factor; its derivative
   theta'(T)/pi = (1/2pi) log(T/2pi)  IS the zero DENSITY (Stirling).  A function field has NO
   archimedean place -> NO Gamma-factor -> a FIXED finite spectrum (2g zeros).  As q->1 the Gamma-factor
   "switches on" and supplies the log-T densification.  We test: does the Gamma-factor control the
   COUNT (yes) and/or the LOCATION/real-parts (no)?  -> the completion datum is the COUNT, RH is the
   location (S(T)), beyond it.

No torch. mpmath. Deterministic.
"""
import mpmath as mp
mp.mp.dps = 25

print("=" * 90)
print("A. Collinearity of zeros  <=>  RH  (the FE upgrades 'collinear' to 'on Re=1/2')")
print("=" * 90)
def area(P, Q, R):  # signed triangle area; ==0 iff collinear
    return ((Q[0]-P[0])*(R[1]-P[1]) - (R[0]-P[0])*(Q[1]-P[1]))/2
G = [mp.im(mp.zetazero(k)) for k in (1, 2, 3, 4)]
onl = [(mp.mpf('0.5'), g) for g in G]                      # zeros ON the line
print(f"  on-line zeros (Re=1/2): area of triples ~ 0 (collinear):")
print(f"     area(z1,z2,z3) = {mp.nstr(area(onl[0],onl[1],onl[2]),3)}   "
      f"area(z1,z2,z4) = {mp.nstr(area(onl[0],onl[1],onl[3]),3)}")
print(f"  a single OFF-line zero rho=0.6+i*14.13 has symmetric orbit {{rho,1-rho,rho_bar,1-rho_bar}}:")
orb = [(mp.mpf('0.6'), G[0]), (mp.mpf('0.4'), G[0]), (mp.mpf('0.6'), -G[0]), (mp.mpf('0.4'), -G[0])]
print(f"     points: (0.6,{mp.nstr(G[0],4)}),(0.4,{mp.nstr(G[0],4)}),(0.6,{mp.nstr(-G[0],4)}),(0.4,{mp.nstr(-G[0],4)})")
print(f"     area of three of them = {mp.nstr(area(orb[0],orb[1],orb[2]),4)}  != 0  => a 2D RECTANGLE, NON-collinear.")
print(f"  on the line the same orbit is {{0.5+14.13i, 0.5-14.13i}} -- a vertical SEGMENT (degenerate).")
print("""  => (every triple collinear) <=> (all on one line); symmetry (conjugation + FE) forces that line
     to be Re=1/2 (or Im=0, excluded). So COLLINEARITY <=> RH -- a clean geometric equivalent, but
     NOT easier: 'some triple collinear' is trivial; 'every triple' is exactly RH. The content the FE
     supplies is 'collinear => vertical'; the missing content is the flatness (zero area) itself = RH.""")

print("\n" + "=" * 90)
print("B. The densification datum: the archimedean Gamma-factor controls the COUNT, not the LOCATION")
print("=" * 90)
def theta(T): return mp.im(mp.loggamma(mp.mpf('0.25') + 1j*T/2)) - (T/2)*mp.log(mp.pi)  # RS theta
def Nmain(T): return theta(T)/mp.pi + 1                          # archimedean main term
print(f"  the Gamma-factor main term N_main(T)=theta(T)/pi+1 vs the true count n at the n-th zero gamma_n:")
print(f"   {'n':>3} {'gamma_n':>12} {'N_main(gamma_n)':>16} {'S=n-1/2-N_main':>16} {'density dtheta/pi':>19}")
for n in range(1, 13):
    g = mp.im(mp.zetazero(n))
    nm = Nmain(g)
    S = (n - mp.mpf('0.5')) - nm                                 # the prime-side fluctuation S(gamma_n)
    dens = mp.diff(theta, g)/mp.pi                               # = (1/2pi) log(T/2pi)
    print(f"   {n:>3} {mp.nstr(g,7):>12} {mp.nstr(nm,7):>16} {mp.nstr(S,3):>16} {mp.nstr(dens,5):>16}")
print(f"""  => N_main (the Gamma-factor) tracks the COUNT n to within S(T) ~ O(1) (Stirling density
     (1/2pi)log(T/2pi), growing -- the rising column). This IS the q->1 completion datum: the archimedean
     Gamma-factor is what densifies a finite function-field spectrum into zeta_Q's log-T spectrum.
     BUT N_main depends ONLY on T (the height) -- it has NO information about the real parts. It fixes
     HOW MANY zeros lie below height T; it says NOTHING about WHETHER they are on Re=1/2. That location
     is carried by S(T)=(1/pi)arg zeta(1/2+iT) -- the PRIME-side fluctuation, beyond the Gamma-factor.""")

print("\n" + "=" * 90)
print("""SYNTHESIS -- the densification datum, identified and bounded:
  * The q->1 spectral-completion datum is the archimedean Gamma-factor: theta(T)~ (T/2)log(T/2pi),
    density (1/2pi)log(T/2pi). A function field has no archimedean place, hence a finite fixed spectrum;
    the Gamma-factor 'switches on' the log-T densification that turns it into zeta_Q's spectrum. EXPLICIT,
    KNOWN (Stirling), and exactly the object 'not finitely-prime-generable'.
  * BUT it controls the COUNT only, not the LOCATION. N_main(T) is a function of height alone -- it
    prescribes how many zeros, never their real parts. RH is the location (S(T) small / zeros on 1/2 /
    every-orbit-collinear, thread A) -- the prime-side residue beyond the Gamma-factor.
  CONCLUSION: the densification is fully understood and explicit (Gamma-factor = the count), which is why
  it is NOT where RH lives. RH = the location given the count = the same archimedean-completion residue
  (S(T) bounded / Weil positivity / the apex spectrum on Re=1/2). The lift identifies the completion
  datum cleanly and confirms RH is the orthogonal (location) half. Conservation of difficulty, sharpened:
  COUNT = Gamma-factor (free, archimedean, explicit);  LOCATION = RH (the wall).
""")
print("=" * 90)
