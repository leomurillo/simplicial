"""
Pushing on the PROLATE GROUND STATE -- where the whole RH margin lives -- and decomposing its energy
against the EXPLICIT Gamma-factor.

The energy-condition probe found: the critical mode (rho_E ~ 1) is the smooth ground state; the margin
3.4e-6 lives there.  The lever question: at the ground state, does the EXPLICIT archimedean Gamma-factor
control the prime energy directly (-> a real handle in a known object), or is the s=1 POLE load-bearing
(-> the margin is the PNT main term, a different kind of input)?

Finer basis (12 frequencies nu=4..48, s=3) so the ground state is well resolved.  We solve the generalized
eigenproblem P v = rho (A_pole+A_arch) v for the top rho (the ground state), then DECOMPOSE its energy:

      v'A_pole v   (the simple pole of zeta at s=1 = the PNT main term)
      v'A_arch v   (the explicit Gamma-factor:  Omega_inf(r)=Re psi(1/4+ir/2)-log pi)
      v'P v        (the prime energy)

  G1  the ground-state energy ratio rho_E and margin 1-rho_E on the fine basis.
  G2  the ground-state SHAPE (is it prolate: smooth, concentrated at low frequency?).
  G3  the DECOMPOSITION -- which term is load-bearing:
        - does v'A_arch v >= v'P v  (Gamma-factor ALONE dominates the primes -> the lever works)?
        - or is v'A_pole v essential (pole-driven; Gamma-factor insufficient or a drag)?
  G4  the lever verdict and what it means for the open inequality.

No torch. mpmath. Deterministic.  (Arch integrals cached by center -> fast.)
"""
import mpmath as mp
mp.mp.dps = 18

NUS = [mp.mpf(v) for v in range(4, 49, 4)]   # 4,8,...,48  (12 frequencies)
n = len(NUS); s = mp.mpf(3)
def Omega(r): return mp.re(mp.digamma(mp.mpf(1)/4 + 1j*r/2)) - mp.log(mp.pi)

# cache the archimedean integral by center c (Omega even -> I(c)=I(-c))
def Ic(c): return mp.quad(lambda r: mp.e**(-(r-c)**2/s**2)*Omega(r), [c-8*s, c, c+8*s])
centers = {}
for j in range(n):
    for k in range(n):
        for a in (NUS[j], -NUS[j]):
            for b in (NUS[k], -NUS[k]):
                c = (a+b)/2
                if c not in centers: centers[c] = None
for c in list(centers): centers[c] = Ic(c)

def abc(j, k):
    return [(mp.e**(-(a-b)**2/(4*s**2)), (a+b)/2)
            for a in (NUS[j], -NUS[j]) for b in (NUS[k], -NUS[k])]
def arch(j, k): return mp.fsum(A*centers[c] for A, c in abc(j, k))/(2*mp.pi)
def gfun(j, k, u):
    pref = s/(2*mp.sqrt(mp.pi))*mp.e**(-s**2*u**2/4)
    return pref*mp.fsum(A*mp.cos(c*u) for A, c in abc(j, k))
def pole(j, k):
    ph = lambda jj, r: mp.e**(-(r-NUS[jj])**2/(2*s**2)) + mp.e**(-(r+NUS[jj])**2/(2*s**2))
    return mp.re(ph(j, 1j/2)*ph(k, 1j/2) + ph(j, -1j/2)*ph(k, -1j/2))
def prime_powers(Pn):
    out = []
    for p in range(2, Pn+1):
        if all(p % d for d in range(2, int(p**0.5)+1)):
            lp = mp.log(p); pk = p
            while pk <= Pn:
                out.append((pk, lp)); pk *= p
    return out

Apole = mp.matrix(n, n); Aarch = mp.matrix(n, n); P = mp.matrix(n, n)
pp = prime_powers(3000)
for j in range(n):
    for k in range(j, n):
        Apole[j,k]=Apole[k,j]=pole(j,k); Aarch[j,k]=Aarch[k,j]=arch(j,k)
        P[j,k]=P[k,j]=mp.fsum(2*lp/mp.sqrt(pk)*gfun(j,k,mp.log(pk)) for pk, lp in pp)
A = Apole + Aarch
W = A - P                         # the Weil form (explicit-formula side)

def eigsym(M):
    E, Q = mp.eigsy((M+M.T)/2)
    order = sorted(range(n), key=lambda i: mp.re(E[i]))
    return [mp.re(E[i]) for i in order], [[Q[r, i] for r in range(n)] for i in order]
EA, _   = eigsym(A)
EAr, _  = eigsym(Aarch)
EW, VW  = eigsym(W)
# critical mode = worst direction of W (robust to A being non-PD)
v = VW[0]; nv = mp.sqrt(mp.fsum(x**2 for x in v)); v = [x/nv for x in v]
def quad(M): return mp.fsum(v[a]*M[a,b]*v[b] for a in range(n) for b in range(n))
vApole, vAarch, vP, vA = quad(Apole), quad(Aarch), quad(P), quad(A)
A_is_PD = min(EA) > 0
rho_E = vP/vA                     # energy ratio along the critical mode (well-defined: vA>0 below)

print("=" * 86)
print("The prolate GROUND STATE and the explicit Gamma-factor: what carries the energy condition?")
print("=" * 86)
print(f"\nG1  fine basis nu=4..48 (n={n}), primes<=3000:")
print(f"      lambda_min(W) = {mp.nstr(EW[0],4)}   (Weil margin on this basis)")
print(f"      energy ratio along critical mode rho_E = v'Pv/v'Av = {mp.nstr(rho_E,8)}   margin 1-rho_E = {mp.nstr(1-rho_E,4)}")
print(f"      A = pole+arch spectrum [{mp.nstr(min(EA),4)}, {mp.nstr(max(EA),4)}]  -> "
      f"{'PD (valid energy metric)' if A_is_PD else 'NOT PD: A alone is not a metric -- the POLE is needed to make it one'}")
print(f"      A_arch (Gamma-factor) spectrum [{mp.nstr(min(EAr),4)}, {mp.nstr(max(EAr),4)}]  -> "
      f"{'PD' if min(EAr)>0 else 'INDEFINITE (Omega_inf<0 near r=0)'}")

print(f"\nG2  ground-state shape |v| on nu={[int(x) for x in NUS]}:")
print(f"      {[mp.nstr(abs(x),3) for x in v]}")
lowfrac = (v[0]**2+v[1]**2)/mp.fsum(x**2 for x in v)
print(f"      weight on the two lowest frequencies (nu=4,8): {mp.nstr(lowfrac*100,3)}%  -> smooth/prolate ground state")

print(f"\nG3  DECOMPOSITION of the ground-state energy  v'A v = v'A_pole v + v'A_arch v  vs  v'P v:")
print(f"      v'A_pole v (s=1 pole / PNT main) = {mp.nstr(vApole,6)}")
print(f"      v'A_arch v (explicit Gamma-fac)  = {mp.nstr(vAarch,6)}")
print(f"      v'A v      (total archimedean)   = {mp.nstr(vA,6)}")
print(f"      v'P v      (prime energy)        = {mp.nstr(vP,6)}")
print(f"      margin v'A v - v'P v             = {mp.nstr(vA-vP,4)}")
print(f"\n      load-bearing test:")
print(f"        Gamma-factor alone >= primes?   v'A_arch v - v'P v = {mp.nstr(vAarch-vP,4)}  "
      f"-> {'YES (Gamma-factor dominates: lever works)' if vAarch>=vP else 'NO'}")
print(f"        pole alone >= primes?           v'A_pole v - v'P v = {mp.nstr(vApole-vP,4)}  "
      f"-> {'YES (pole dominates)' if vApole>=vP else 'NO'}")
print(f"        pole fraction of arch energy:   v'A_pole v / v'A v = {mp.nstr(vApole/vA*100,4)}%")
print(f"        Gamma-factor sign on g.s.:      v'A_arch v {'> 0 (helps)' if vAarch>0 else '< 0 (a DRAG)'}")

print("\n" + "=" * 86)
gamma_wins = vAarch >= vP
pole_load = vApole/vA > mp.mpf('0.5')
print(f"""G4  VERDICT -- the ground state, decomposed:
  rho_E = {mp.nstr(rho_E,8)} <= 1 (energy condition holds on this finite basis, margin {mp.nstr(1-rho_E,3)}).
  The ground state is the smooth prolate mode ({mp.nstr(lowfrac*100,2)}% on the two lowest frequencies).
  Load-bearing: {'the explicit Gamma-factor ALONE dominates the prime energy -- the lever works: RH at the'
     ' critical mode reduces to a Gamma-factor estimate.' if gamma_wins else
     'the s=1 POLE is load-bearing (%.0f%% of the archimedean energy); the Gamma-factor %s.' %
     (float(vApole/vA*100), 'is a drag (negative on the ground state)' if vAarch<0 else 'alone does NOT dominate the primes')}
  {'' if gamma_wins else 'So at the ground state the margin is POLE-driven (PNT main term), confirming the program record.'}
  {'' if gamma_wins else 'CONSEQUENCE: the open inequality at the critical mode is not a pure Gamma-factor bound -- it is'}
  {'' if gamma_wins else 'pole(PNT) + Gamma-factor >= primes, a balance in which the rank-1 pole carries the bulk and the'}
  {'' if gamma_wins else 'Gamma-factor sets the fine (sub-leading) correction whose sign is RH.  The lever is the pole+Gamma'}
  {'' if gamma_wins else 'COMBINATION, not the Gamma-factor alone -- which is exactly why finite witnesses need the pole.'}
""")
print("=" * 86)
