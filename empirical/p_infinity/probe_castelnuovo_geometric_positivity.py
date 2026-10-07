"""probe_castelnuovo_geometric_positivity.py — pillar (III) of the Castelnuovo map (P-infinity-C).

On the surface C x C over F_q, Castelnuovo's argument rests on: two DISTINCT irreducible curves meet
non-negatively.  The zeta-side counterpart: for positive test profiles g, h (classes of effective
scaling correspondences) with DISJOINT supports (no common component with each other; correlation
supported away from the diagonal v=0), the intersection pairing

   <g,h> := ghat(0)hhat(1) + ghat(1)hhat(0) - sum_rho ghat(rho) hhat(1-rho)         (zeros side)
         =  sum_n (Lambda(n)/sqrt n) [rho_c(log n) + rho_c(-log n)]  +  ARCH(g,h)   (local side)

is a sum of POSITIVE local terms at EVERY place:
  - finite places: Lambda(n) >= 0 against the positive correlation rho_c(v) = int G(x)H(x-v)dx;
  - archimedean place: density  k_inf(v) = e^{-|v|/2}/(1 - e^{-2|v|})  > 0 away from v=0
    (= the trivial-zero ladder sum_{k>=0} e^{-(2k+1/2)|v|}; same universal e^{-v/2} envelope as the
    prime atoms log p * p^{-k/2} at v = k log p — every place carries the critical-line envelope).

CERTIFIES (exact targets):
  (1) the archimedean kernel: -(1/pi) int_0^inf cos(rv) [Re psi(1/4+ir/2) - log pi] dr
      equals e^{-v/2}/(1-e^{-2v}) for v in {0.4, 0.9, 1.5, 2.3}   [quadosc vs closed form]
  (2) pairing identity zeros-side == local-side (the pairing-level W1) for 3 disjoint bump pairs
  (3) POSITIVITY of all three pairings, including a "prime desert" pair where the archimedean
      place alone carries the positivity
  (4) frequency-space arch == int rho_c k_inf  (kernel <-> symbol consistency, disjoint case)
  (5) overlap control: identical bumps (self-intersection) — identity still holds (frequency-space
      arch handles the diagonal PV); positivity NOT claimed there (common components, as on a surface)
No torch.  Deterministic.  GREEN iff all pass.
"""
import sys
import mpmath as mp
from sympy import factorint

mp.mp.dps = 30
PASS = True
def check(label, ok, detail=""):
    global PASS
    print(("  PASS " if ok else "  FAIL ") + label + (("  " + detail) if detail else ""))
    if not ok: PASS = False

# bump = (a, s):  G(x) = exp(-(x-a)^2 / 2s^2);   m(z) = int G(x) e^{zx} dx  (entire)
def m(b, z):
    a, s = b
    return s*mp.sqrt(2*mp.pi)*mp.e**(z*a + s*s*z*z/2)

print("[zeros] loading 80 zeta zeros ...")
ZN = 80
zeros = [mp.im(mp.zetazero(k)) for k in range(1, ZN+1)]

def pair_zeros(b1, b2):
    poles = m(b1, mp.mpf(-1)/2)*m(b2, mp.mpf(1)/2) + m(b1, mp.mpf(1)/2)*m(b2, mp.mpf(-1)/2)
    zsum = mp.fsum(2*mp.re(m(b1, 1j*g)*m(b2, -1j*g)) for g in zeros)
    return poles - zsum

def Lsym(r):
    return mp.re(mp.digamma(mp.mpf('0.25') + 1j*r/2)) - mp.log(mp.pi)

def pair_local(b1, b2, nmax=600):
    a1, s1 = b1; a2, s2 = b2
    S2 = s1*s1 + s2*s2
    def rho_c(v):                                  # int G1(x) G2(x - v) dx : center a1-a2, var S2
        return s1*s2*mp.sqrt(2*mp.pi/S2)*mp.e**(-(a1 - a2 - v)**2/(2*S2))
    ps = mp.mpf(0)
    for n in range(2, nmax+1):
        f = factorint(n)
        if len(f) == 1:
            ((p, k),) = f.items()
            ln = mp.log(n)
            ps += (mp.log(p)/mp.sqrt(n))*(rho_c(ln) + rho_c(-ln))
    arch = -(1/mp.pi)*mp.quad(lambda r: mp.re(m(b1, 1j*r)*m(b2, -1j*r))*Lsym(r), [0, 4, 12, 40])
    return ps + arch, ps, arch

# ---------------- (1) the archimedean kernel: numeric vs closed form ----------------
print("== (1) archimedean intersection kernel  k_inf(v) = e^{-v/2}/(1-e^{-2v}) ==")
def k_num(v):
    Lp = lambda r: -mp.im(mp.psi(1, mp.mpf('0.25') + 1j*r/2))/2          # d/dr Lsym(r)
    I = mp.quadosc(lambda r: mp.sin(r*v)*Lp(r), [0, mp.inf], period=2*mp.pi/v)
    return I/(mp.pi*v)                       # = -(1/pi) int_0^inf cos(rv) Lsym(r) dr  (one IBP)
def k_cf(v):
    return mp.e**(-v/2)/(1 - mp.e**(-2*v))
for v in (mp.mpf('0.4'), mp.mpf('0.9'), mp.mpf('1.5'), mp.mpf('2.3')):
    kn, kc = k_num(v), k_cf(v)
    check(f"v={float(v):.1f}: kernel num {float(kn):+.10f} == closed form {float(kc):+.10f}",
          abs(kn - kc) < mp.mpf('1e-10'))
check("kernel positive away from diagonal (trivial-zero ladder sum_k e^{-(2k+1/2)v})",
      all(k_cf(mp.mpf(v)) > 0 for v in ('0.1', '0.5', '1', '2', '4')))

# ---------------- (2,3) pairing identity + positivity, disjoint pairs ----------------
print("== (2,3) <g,h> zeros-side == local-side; positivity at every tested disjoint pair ==")
pairs = [
    ("prime-rich  (diff 1.30 ~ log 3.7)", (mp.mpf('0.90'), mp.mpf('0.18')), (mp.mpf('2.20'), mp.mpf('0.18'))),
    ("prime desert(diff 0.55 ~ log 1.73)", (mp.mpf('0.50'), mp.mpf('0.18')), (mp.mpf('1.05'), mp.mpf('0.18'))),
    ("near 7      (diff 1.90 ~ log 6.7)", (mp.mpf('1.20'), mp.mpf('0.18')), (mp.mpf('3.10'), mp.mpf('0.18'))),
]
for label, b1, b2 in pairs:
    pz = pair_zeros(b1, b2)
    pl, ps, ar = pair_local(b1, b2)
    rel = abs(pz - pl)/abs(pz)
    check(f"{label}: identity (reldiff {float(rel):.1e})", rel < mp.mpf('1e-10'))
    check(f"{label}: POSITIVE  <g,h> = {float(pz):+.6f}  (primes {float(ps):+.6f}, arch {float(ar):+.6f})",
          pz > 0)
pdz = pair_zeros(*[p[1] for p in pairs[1:2]][0:1][0:1] ) if False else None
# prime-desert pair: arch must carry the positivity
_, ps_d, ar_d = pair_local(pairs[1][1], pairs[1][2])
check("prime desert: archimedean place alone carries the positivity (arch > primes)", ar_d > ps_d,
      f"arch {float(ar_d):.6f} vs primes {float(ps_d):.6f}")

# ---------------- (4) kernel <-> symbol consistency on a disjoint pair ----------------
# narrow bumps (s=0.12) so the correlation tail through the diagonal (where the closed form omits
# the PV counterterms) is e^{-29} — i.e., a genuinely disjoint pair, as the surface statement requires
print("== (4) frequency-space arch == int rho_c(v) k_inf(|v|) dv  (disjoint pair, s=0.12) ==")
b1, b2 = (mp.mpf('0.90'), mp.mpf('0.12')), (mp.mpf('2.20'), mp.mpf('0.12'))
a1, s1 = b1; a2, s2 = b2; S2 = s1*s1 + s2*s2
rho_c = lambda v: s1*s2*mp.sqrt(2*mp.pi/S2)*mp.e**(-(a1 - a2 - v)**2/(2*S2))
arch_kernel = mp.quad(lambda v: rho_c(v)*k_cf(abs(v)), [-5, a1 - a2, mp.mpf('-0.05')])
_, _, arch_freq = pair_local(b1, b2)
check(f"arch via kernel {float(arch_kernel):+.10f} == via symbol {float(arch_freq):+.10f}",
      abs(arch_kernel - arch_freq) < mp.mpf('1e-9'))

# ---------------- (5) overlap control: self-intersection ----------------
print("== (5) overlap control (identical bumps; the 'common component' case) ==")
bs = (mp.mpf('1.40'), mp.mpf('0.18'))
pz = pair_zeros(bs, bs)
pl, ps, ar = pair_local(bs, bs)
rel = abs(pz - pl)/abs(pz)
check(f"identity STILL holds at full overlap (reldiff {float(rel):.1e})", rel < mp.mpf('1e-10'))
print(f"        self-intersection <g,g> = {float(pz):+.6f} (primes {float(ps):+.6f}, arch {float(ar):+.6f})"
      f" — sign NOT claimed (diagonal PV / adjunction, as on a surface)")

print()
print("RESULT: " + ("GREEN — geometric positivity certified at every place, off-diagonal"
                    if PASS else "RED — failures above"))
sys.exit(0 if PASS else 1)
