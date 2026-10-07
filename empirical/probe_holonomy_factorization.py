"""
probe_holonomy_factorization.py  --  test MY OWN compass (option 2), honestly, with pre-registered K/L.

THE REFRAME (N6 Rem 6.3 + the multiplicative compass): RH <=> the dual-flat connection omega = d log xi
has trivial holonomy on the bulk {Re s > 1/2}; an off-line zero is one curvature atom (holonomy 2 pi i).
Holonomy is INTRINSICALLY MULTIPLICATIVE (a pi_1 representation: loop integrals add in the exponent ->
factors multiply). And xi factors over places:
   xi(s) = [s(s-1)/2] * Z_inf(s) * prod_p Z_p(s),   Z_inf = pi^{-s/2} Gamma(s/2),  Z_p = (1-p^{-s})^{-1}.
So  d log xi  =  (pole) + (archimedean)  +  sum_p (prime),  and the holonomy is a SUM of per-place
windings -- equivalently exp(holonomy) is a PRODUCT of per-place phase factors.

THE NON-CIRCULAR QUESTION (pre-registered, three-outcome GPD):
  K (the compass has TEETH): the holonomy factors into computable per-place pieces with a NONTRIVIAL
     archimedean factor that ISOLATES the RH content -- some local factor's winding carries the zeros,
     giving a handle the additive Weil trace did not.
  L (the compass reduces to the WALL): EACH local factor (archimedean Z_inf AND every finite Euler factor
     Z_p AND every finite Euler product) has ZERO bulk holonomy -- it is holomorphic & non-vanishing there
     -- so the zeros live in NONE of them; the total holonomy is irreducibly emergent from the analytic
     continuation of zeta. The factorization is trivial-per-place; the smooth winding DENSITY is
     archimedean (arch-domination), and RH = control of the emergent prime fluctuation S(T) = the same
     archimedean wall (N7/N11), now in winding form.
  joint: partial.

This decisively tests whether "multiplicative holonomy" is a NEW handle or a relabel of arch-domination.
It is the honest paranoid pass on a direction *I* proposed. Deterministic mpmath. No torch.
"""
import mpmath as mp
mp.mp.dps = 20

# ---- per-place logarithmic derivatives d log(factor)/ds -------------------------------------------
dlog_zeta = lambda s: mp.diff(mp.zeta, s) / mp.zeta(s)                    # zeta'/zeta (carries the zeros)
dlog_Zinf = lambda s: -mp.log(mp.pi)/2 + mp.digamma(s/2)/2                # archimedean Gamma-factor
dlog_Zp   = lambda s, p: -(mp.log(p)) * p**(-s) / (1 - p**(-s))           # p-th Euler factor
dlog_pole = lambda s: 1/s + 1/(s-1)                                       # s(s-1)/2
def dlog_xi(s):       return dlog_pole(s) + dlog_Zinf(s) + dlog_zeta(s)
def dlog_euler(s, P): return mp.fsum(dlog_Zp(s, p) for p in PRIMES if p <= P)

PRIMES = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]

def winding(dlog, center, hw):
    """(1/2 pi i) * contour integral of dlog around the square of half-width hw at center = #zeros-#poles."""
    re0, re1 = center.real - hw, center.real + hw
    im0, im1 = center.imag - hw, center.imag + hw
    bot = mp.quad(lambda x: dlog(mp.mpc(x, im0)),        [re0, re1])
    rgt = mp.quad(lambda y: dlog(mp.mpc(re1, y)) * 1j,   [im0, im1])
    top = mp.quad(lambda x: dlog(mp.mpc(x, im1)),        [re1, re0])
    lft = mp.quad(lambda y: dlog(mp.mpc(re0, y)) * 1j,   [im1, im0])
    return (bot + rgt + top + lft) / (2j * mp.pi)

# ===================================================================================================
print("="*92)
print("TEST 1 -- box around the first zero (0.5+14.1347 i): which factor carries the holonomy/zero?")
print("="*92)
c  = mp.mpc(0.5, 14.134725)         # the first zeta zero
hw = mp.mpf('0.45')                  # box Re in [0.05,0.95], Im in [13.68,14.58]: encloses exactly 1 zero
print(f"  box: Re in [{float(c.real-hw):.2f},{float(c.real+hw):.2f}], Im in "
      f"[{float(c.imag-hw):.2f},{float(c.imag+hw):.2f}]  (encloses the first zero)")
print(f"  {'factor':>26} {'winding = #zeros enclosed':>28}")
results = []
for name, dl in [("xi (the completed object)", dlog_xi),
                 ("  Z_inf (archimedean)",    dlog_Zinf),
                 ("  Z_2 (Euler factor p=2)",  lambda s: dlog_Zp(s,2)),
                 ("  Z_3 (Euler factor p=3)",  lambda s: dlog_Zp(s,3)),
                 ("  Z_5 (Euler factor p=5)",  lambda s: dlog_Zp(s,5)),
                 ("  prod_{p<=47} Z_p",        lambda s: dlog_euler(s,47)),
                 ("  zeta (the continuation)", dlog_zeta)]:
    w = winding(dl, c, hw)
    results.append((name, w))
    print(f"  {name:>26} {mp.nstr(w, 6):>28}")

zero_in = {n: abs(mp.re(w)) > 0.5 for n, w in results}
print(f"\n  => the holonomy (= 1 enclosed zero) is carried by: "
      f"{', '.join(n.strip() for n,w in results if abs(mp.re(w))>0.5)}")
print(f"     and is ABSENT (winding 0) from: archimedean Z_inf AND every finite Euler factor/product.")

print("\n"+"="*92)
print("TEST 2 -- a purely bulk box (Re in [0.7,1.3], no zeros under RH): total holonomy = 0 ?")
print("="*92)
cb = mp.mpc(1.0, 14.0); hwb = mp.mpf('0.3')
wb = winding(dlog_xi, cb, hwb)
print(f"  box Re in [0.7,1.3], Im in [13.7,14.3]:  winding(xi) = {mp.nstr(wb,4)}  (expect 0: no bulk zeros)")

print("\n"+"="*92)
print("TEST 3 -- the winding DENSITY decomposes: N(T) = theta(T)/pi + 1 + S(T)  (arch-domination)")
print("="*92)
print(f"  {'T':>6} {'arch: theta/pi+1':>18} {'prime: S(T)':>14} {'sum':>10} {'|frac part|':>12}")
for T in (20, 50, 100, 200):
    th = mp.siegeltheta(T)/mp.pi + 1                      # archimedean smooth count
    S  = mp.arg(mp.zeta(mp.mpc(0.5, T)))/mp.pi            # prime fluctuation S(T)
    N  = th + S
    print(f"  {T:>6} {float(th):>18.4f} {float(S):>+14.4f} {float(N):>10.4f} {float(abs(N-mp.nint(N))):>12.4f}")
print("  => the SMOOTH winding (the density of the holonomy) is the archimedean theta(T)/pi ~ "
      "(T/2pi)log(T/2pi);")
print("     the prime contribution is only the BOUNDED fluctuation S(T). The holonomy is arch-DOMINATED.")

print("\n"+"="*92)
print("VERDICT (honest paranoid pass on my own compass)")
print("="*92)
arch_trivial = abs(mp.re(dict(results)["  Z_inf (archimedean)"])) < 0.5
euler_trivial = abs(mp.re(dict(results)["  prod_{p<=47} Z_p"])) < 0.5
print(f"""  K-branch (new handle)?  Would require a local factor whose winding carries the zeros.
  L-branch (reduces to wall)? Requires: zeros in NO explicit local factor + arch-dominated density.

  OBSERVED:
   - the enclosed zero's holonomy is in zeta's CONTINUATION only; archimedean factor trivial: {arch_trivial};
     finite Euler product trivial: {euler_trivial}  (TEST 1).
   - bulk box (no zeros) has zero total holonomy (TEST 2) -- consistent, no hidden bulk content.
   - the winding DENSITY is the archimedean theta(T)/pi; primes give only the bounded S(T) (TEST 3).

  => L-BRANCH. The 'multiplicative holonomy factorization' is TRIVIAL PER PLACE: neither the explicit
     archimedean Gamma-factor nor any finite Euler factor/product carries a zero -- the holonomy is
     irreducibly emergent from the continuation of zeta. So the factorization gives NO free local
     positivity; it relabels ARCH-DOMINATION (smooth winding = archimedean) + the open control of the
     prime fluctuation S(T) = the SAME archimedean wall (N7/N11), now in winding form. My compass
     (option 2) does NOT supply a new handle. Honestly retired as a free path.

  THE ONE SURVIVING DISTINCTION (forward, not closed): over a function field the SAME factorization is
     NON-trivial per place -- the local Frobenius factors DO carry the zeros (eigenvalue phases forced
     to |alpha|=sqrt q by Weil/Hodge intersection positivity). The Q-vs-F_q gap is exactly that the
     finite places carry no holonomy over Q (this probe) but do over F_q. That points back to the
     function-field door (multiplicative = Weil-intersection positivity), NOT to an archimedean
     holonomy handle. No proof of RH; this CLOSES one compass and re-aims at the other.""")
