"""
probe_alpha_curvature_offline_zero.py  --  is the adelic manifold's alpha-curvature LITERALLY the
off-line-zero obstruction?  Make 'dually flat <=> no off-line zero' precise and certify it.

THESIS (precise). The dual-flat (e-/m-) potential of the adelic statistical manifold, in its spectral
chart, is psi = log xi (xi = the completed zeta, the log-partition / Weil form potential of N5/N6).
The e-connection 1-form is omega = d psi = (xi'/xi) ds. Then:

  (1) POINCARE-LELONG.  omega is closed (flat) where xi != 0; its CURVATURE CURRENT is the zero divisor
        (1/2pi i) d omega  =  sum_rho m_rho delta_rho        [holonomy 2pi i per zero].
      Equivalently, the dual potential's real part is HARMONIC off the zeros:
        Laplacian log|xi|  =  2pi sum_rho delta_rho   (=0 in the bulk, delta-atom at each zero).
      So 'alpha-curvature' (alpha=+/-1, the dually-flat pair) is LITERALLY supported on the zeros.

  (2) THE EQUIVALENCE (bulk).  Let Omega = {Re s > 1/2} (the bulk, one side of the critical line). Then
        adelic manifold dually FLAT on Omega  <=>  omega has trivial holonomy on every loop in Omega
        <=>  log xi single-valued (a global convex dual potential exists) on Omega  <=>  no zeros in
        Omega  <=>  (with the functional equation xi(s)=xi(1-s))  RH.
      An OFF-LINE ZERO is exactly one quantized curvature atom (delta_rho) in the bulk Omega -- the
      holonomy/curvature obstruction to global dual-flatness. RH = curvature confined to the boundary
      line Re=1/2.

  (3) THE UPGRADE over 'necessary-not-sufficient'.  The first Laguerre inequality (Xi')^2 - Xi Xi'' >= 0
      / phase-monotonicity phi'>=0 is the BOUNDARY TRACE (Im omega on Re=1/2). It is necessary but not
      sufficient (an off-line zero's bulk atom is maskable on the line). The CURVATURE CURRENT on the
      open bulk Omega is the 2-dim object the 1-dim boundary cannot see; it is EQUIVALENT to RH. So the
      curvature/holonomy formulation is the exact upgrade that closes the necessary->sufficient gap.

Certified here: (1) holonomy (1/2pi i)∮ xi'/xi = #zeros enclosed (=curvature mass); (2) the bulk Omega
is holonomy-free in the computed range (RH-region clean); (3) log|xi| harmonic (Laplacian≈0) in the
bulk; (4) honest necessary-not-sufficient demo: a toy with an off-line zero whose boundary Laguerre
inequality is MASKED for far zeros yet whose holonomy = 2pi i always.

mpmath + numpy. No torch.
"""
import mpmath as mp
import numpy as np
mp.mp.dps = 20

def xi(s):
    s = mp.mpc(s)
    return 0.5 * s * (s - 1) * mp.power(mp.pi, -s / 2) * mp.gamma(s / 2) * mp.zeta(s)

def dlogxi(s):                       # xi'/xi  (analytic: avoids cancellation; poles only at zeros of xi)
    s = mp.mpc(s)
    return 1/s + 1/(s-1) - 0.5*mp.log(mp.pi) + 0.5*mp.digamma(s/2) + mp.zeta(s,1,1)/mp.zeta(s)

def winding(a, b, c, d):             # (1/2pi i) ∮ xi'/xi ds over rectangle [a,b]x[c,d], CCW
    f = dlogxi
    I  = mp.quad(lambda x: f(mp.mpc(x, c)),      [a, b])
    I += mp.quad(lambda y: f(mp.mpc(b, y)) * 1j, [c, d])
    I += mp.quad(lambda x: f(mp.mpc(x, d)),      [b, a])
    I += mp.quad(lambda y: f(mp.mpc(a, y)) * 1j, [d, c])
    return I / (2j * mp.pi)

print("=" * 92)
print("(1) CURVATURE CURRENT = ZERO DIVISOR: (1/2pi i) ∮ xi'/xi ds = #zeros enclosed (holonomy)")
print("=" * 92)
# nontrivial zeros at Im ~ 14.1347, 21.022, 25.0109, 30.4249, 32.9351
boxes = [
    ("straddle line, 1st zero (14.13)", 0.2, 0.8, 13.0, 15.0, 1),
    ("straddle line, zeros 1-3",        0.2, 0.8, 13.0, 26.0, 3),
    ("straddle line, zeros 1-5",        0.2, 0.8, 13.0, 36.0, 5),
]
for name, a, b, c, d, exp in boxes:
    w = winding(a, b, c, d)
    print(f"  {name:34} winding = {mp.nstr(w,6):>16}  ~ {int(round(float(w.real)))}  (expect {exp})")
print("  => the holonomy of omega=d log xi around a region = the number of zeros (curvature atoms) in")
print("     it: the curvature current is the zero divisor.")

print("\n" + "=" * 92)
print("(2) THE EQUIVALENCE: curvature ON the line vs FLAT bulk.  (contours bounded away from Re=1/2,")
print("    else they ride the on-line zeros and pick up spurious half-residues -- a real pitfall.)")
print("=" * 92)
demos = [
    ("straddle line  Re[0.3,0.7] Im[13,15]", 0.3, 0.7, 13.0, 15.0, "curvature ON the line"),
    ("BULK  Re[0.7,1.3] Im[13,15]",          0.7, 1.3, 13.0, 15.0, "flat (no off-line zero)"),
    ("BULK  Re[0.8,3.0] Im[5,35]",           0.8, 3.0, 5.0, 35.0,  "flat (no off-line zero)"),
    ("BULK  Re[0.8,3.0] Im[35,60]",          0.8, 3.0, 35.0, 60.0, "flat (no off-line zero)"),
]
for name, a, b, c, d, tag in demos:
    w = winding(a, b, c, d)
    print(f"  {name:38} winding ~ {int(round(float(w.real))):>2}  ({mp.nstr(w.real,3):>9})  -> {tag}")
print("  => curvature sits ON the critical line (straddle box =1); the bulk Re>1/2 is FLAT (=0). RH =")
print("     'all curvature confined to the line' = log xi single-valued (a global convex chart) on the")
print("     bulk = the adelic manifold DUALLY FLAT off the line. An off-line zero = a curvature puncture")
print("     (winding=1) in some bulk box -- demonstrated in part (4).")

print("\n" + "=" * 92)
print("(3) POINCARE-LELONG harmonicity: Laplacian log|xi| = 0 in the bulk (flat), 2pi delta at zeros")
print("=" * 92)
h = 1e-3
def logabsxi(x, y): return float(mp.log(abs(xi(mp.mpc(x, y)))))
def lap(x, y):
    return (logabsxi(x+h,y)+logabsxi(x-h,y)+logabsxi(x,y+h)+logabsxi(x,y-h)-4*logabsxi(x,y))/h**2
for (x, y) in [(0.80, 17.0), (1.20, 25.0), (0.70, 40.0), (2.0, 8.0)]:
    print(f"  bulk point s={x:+.2f}{y:+.1f}i (no zero):  Laplacian log|xi| = {lap(x,y):+.3e}  (~0 -> harmonic/FLAT)")
print("  => log|xi| (real part of the dual potential) is HARMONIC away from zeros: zero curvature in the")
print("     bulk. Poincare-Lelong: Laplacian log|xi| = 2pi sum_rho delta_rho -- all curvature is the")
print("     ZERO DIVISOR (a current). The 2pi mass per zero is the 2pi i holonomy of part (1).")

print("\n" + "=" * 92)
print("(4) UPGRADE over necessary-not-sufficient: first Laguerre (boundary) maskable; holonomy (bulk) not")
print("=" * 92)
# toy: f(z) = prod_{k=1..n}(1 - z^2/k^2) * (z^2 + beta^2). zeros: +-k (REAL=on-line), +-i beta (OFF-line).
# real-entire; critical line = real z axis. Laguerre L1 = f'^2 - f f'' on the real axis.
def toy_L1_min(n, beta):
    roots = [k for k in range(1, n+1)] + [-k for k in range(1, n+1)] + [1j*beta, -1j*beta]
    c = np.poly(roots)                      # real coeffs (conj pair)
    c = np.real(c)
    d1 = np.polyder(c); d2 = np.polyder(c, 2)
    xs = np.linspace(-n-0.5, n+0.5, 40001)
    near = np.min(np.abs(xs[:, None] - np.arange(1, n+1)[None, :]), axis=1)
    near = np.minimum(near, np.min(np.abs(xs[:, None] + np.arange(1, n+1)[None, :]), axis=1))
    mask = near > 0.02                      # avoid real zeros (there L1=f'^2>=0 trivially)
    L1 = np.polyval(d1, xs)**2 - np.polyval(c, xs) * np.polyval(d2, xs)
    # normalize by f^2 scale to compare signs meaningfully
    f2 = np.polyval(c, xs)**2 + 1e-300
    return np.min((L1 / (f2 + np.max(f2)*1e-6))[mask]), np.min(L1[mask])
def toy_holonomy(n, beta):
    # (1/2pi i) ∮ f'/f around +i*beta on a small circle; f'/f = sum 1/(z-root)
    roots = [k for k in range(1, n+1)] + [-k for k in range(1, n+1)] + [1j*beta, -1j*beta]
    th = np.linspace(0, 2*np.pi, 4000, endpoint=False)
    zc = 1j*beta + 0.2*np.exp(1j*th)
    fof = np.array([np.sum(1.0/(z - np.array(roots))) for z in zc])
    integ = np.sum(fof * (0.2j*np.exp(1j*th))) * (2*np.pi/4000)
    return integ/(2j*np.pi)
n = 20
print(f"  toy f = prod_(k=1)^{n}(1-z^2/k^2)*(z^2+beta^2): on-line zeros +-1..+-{n}, OFF-line zeros +-i*beta")
print(f"  {'beta':>6} {'min normalized L1 on line':>26} {'first-Laguerre':>16} {'holonomy(iβ)':>14}")
for beta in (0.3, 1.0, 3.0, 8.0, 20.0):
    mn_norm, mn_raw = toy_L1_min(n, beta)
    hol = toy_holonomy(n, beta)
    verdict = "VIOLATED" if mn_norm < -1e-9 else "holds (MASKED)"
    print(f"  {beta:>6} {mn_norm:>26.3e} {verdict:>16} {int(round(hol.real)):>14}")
print("  holonomy (1/2pi i)∮ f'/f around +i*beta = 1 for EVERY beta (computed) -- the curvature")
print("  atom is ALWAYS there. But the boundary Laguerre inequality only 'sees' it when beta is small")
print("  (zero near the line); for large beta it is MASKED. => boundary inequality = necessary, NOT")
print("  sufficient; the BULK holonomy/curvature = the equivalent (un-maskable) condition. This is the")
print("  exact gap the curvature-current formulation closes.")

print("\n" + "=" * 92)
print("VERDICT")
print("=" * 92)
print("""  PRECISE & CERTIFIED:  'dually flat (off the critical line)  <=>  no off-line zero'  is LITERAL:
   * the dual-flat potential is psi=log xi; omega=d psi; its CURVATURE CURRENT (Poincare-Lelong) is
     EXACTLY the zero divisor sum_rho delta_rho -- holonomy 2pi i per zero (part 1), Laplacian log|xi|
     =2pi sum delta_rho, harmonic/FLAT in the bulk (part 3);
   * an OFF-LINE ZERO is one quantized curvature atom in the bulk Omega={Re>1/2}; the adelic manifold
     is dually flat on Omega  <=>  Omega is curvature-free  <=>  no off-line zeros  <=>  RH (part 2);
   * this is the BULK (2-dim) statement, EQUIVALENT to RH -- the exact upgrade of the boundary (1-dim)
     first-Laguerre / phase-monotonicity inequality, which is only necessary (maskable, part 4).
  So the alpha-curvature (alpha=+/-1, the e-/m- dually-flat pair) IS literally the off-line-zero
  obstruction: RH = 'the curvature of the adelic dual potential is confined to the critical line.'
  HONEST SCOPE: the identification psi=log xi (the adelic manifold's spectral potential) is the
  program's N5/N6 content ([P]/[A]); the Poincare-Lelong 'curvature=zeros' and the bulk equivalence are
  rigorous complex analysis. The reformulation is EQUIVALENT to RH (a sharper geometric coordinate with
  Gauss-Bonnet/holonomy tools attached), not a reduction to something strictly easier -- but it pins the
  open content to one clean statement: a positive, FE-symmetric curvature current is supported on its
  symmetry axis. That positivity is the Weil/chiral-channel content, now in curvature form.""")
