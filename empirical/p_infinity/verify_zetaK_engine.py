"""verify_zetaK_engine.py — fast gate for the chiral (Dedekind) pairing engine.
zeta_K = zeta * L(s,chi_D).  Pole pair = xi_zeta's (coeff 1, xi_K entire).  Engine:
  prime weight  Lambda(n)(1+chi_D(n))/sqrt n ;  arch  Om_K(r)=Re psi(1/4+ir/2)+Re psi(1/4+a/2+ir/2)
  -2 log pi + log|D|.  GATE: self-pairing local (poles+primes+arch) == zeros-side (poles - sum over
  zeta-zeros U L-zeros |ghat|^2), D=-3 (odd/chiral) & D=5 (even).  Wide bump s=0.55 => gamma<=9 only,
  L-zeros via seeded findroot."""
import mpmath as mp
from sympy import primerange
mp.mp.dps = 20

def kron(a, n):
    if n == 0: return 1 if abs(a) == 1 else 0
    res = 1
    if n % 2 == 0:
        if a % 2 == 0: return 0
        while n % 2 == 0:
            n //= 2
            if a % 8 in (3, 5): res = -res
    a %= n
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5): res = -res
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3: res = -res
        a %= n
    return res if n == 1 else 0

def Lfun(D, s):
    q = abs(D)
    return q**(-s)*mp.fsum(kron(D, a)*mp.zeta(s, mp.mpf(a)/q) for a in range(1, q+1) if kron(D, a) != 0)

def Lzeros(D, seeds):
    zs = []
    for t0 in seeds:
        try:
            z = mp.findroot(lambda t: Lfun(D, mp.mpf('0.5') + 1j*t), mp.mpf(t0), maxsteps=20)
            zr = float(mp.re(z))
            if zr > 1 and abs(Lfun(D, mp.mpf('0.5') + 1j*mp.mpf(zr))) < 1e-7 and all(abs(zr - q) > 1e-3 for q in zs):
                zs.append(zr)
        except Exception: pass
    return sorted(zs)

def m(b, z):
    a, s = b
    return s*mp.sqrt(2*mp.pi)*mp.e**(z*a + s*s*z*z/2)
def poles(b): return 2*(m(b, mp.mpf('0.5'))*m(b, mp.mpf('-0.5'))).real
def arch_local(D, a_par, b):
    Ls = lambda r: (mp.re(mp.digamma(mp.mpf('0.25') + 1j*r/2))
                    + mp.re(mp.digamma(mp.mpf('0.25') + a_par/mp.mpf(2) + 1j*r/2))
                    - 2*mp.log(mp.pi) + mp.log(abs(D)))
    return -(1/mp.pi)*mp.quad(lambda r: (m(b, 1j*r)*m(b, -1j*r)).real*Ls(r), [0, 4, 12, 30])
def primes_local(D, b):
    a, s = b
    kc = lambda v: s*mp.sqrt(mp.pi)*mp.e**(-v*v/(4*s*s))
    tot = mp.mpf(0)
    for p in primerange(2, 80):
        lp = mp.log(p); k = 1; pk = p
        while k*lp <= 30:
            w = lp*(1 + kron(D, pk))/mp.sqrt(pk)
            if w != 0: tot += w*(kc(k*lp) + kc(-k*lp))
            k += 1; pk *= p
    return tot

print("gate: zeta_K = zeta * L(s,chi_D) self-pairing, local == zeros-side  (bump s=0.55)\n")
bump = (mp.mpf('1.4'), mp.mpf('0.55'))
zz = [float(mp.im(mp.zetazero(k))) for k in range(1, 4)]      # 14.13, 21.02, 25.01
print(f"zeta zeros: {[round(g,3) for g in zz]}")
for D, a_par, seeds, label in [(-3, 1, [8.0, 11.2, 15.7], "odd/chiral"), (5, 0, [6.6, 9.8, 13.0], "even")]:
    lz = Lzeros(D, seeds)
    loc = primes_local(D, bump) + arch_local(D, a_par, bump)        # local side = primes + arch (no poles)
    zer = poles(bump) - mp.fsum(abs(m(bump, 1j*mp.mpf(g)))**2 for g in zz) \
                      - mp.fsum(abs(m(bump, 1j*mp.mpf(g)))**2 for g in lz)
    rel = abs(loc - zer)/abs(zer)
    print(f"D={D:>3} ({label}, a={a_par}): L-zeros={[round(z,3) for z in lz]}")
    print(f"        local={float(loc):.9f}  zeros-side={float(zer):.9f}  reldiff={float(rel):.2e}"
          f"   {'PASS' if rel < 1e-5 else 'FAIL'}\n")
