"""
probe_li_generating_function.py  --  the 'all rungs at once' object: the Li generating function
G(z)=sum_n lambda_n z^n, its closed form, and what its positivity/analyticity is.

CLOSED FORM. lambda_n = sum_rho [1-(1-1/rho)^n].  With w_rho = 1-1/rho,
   G(z) = sum_{n>=1} lambda_n z^n = sum_rho  z(1-w_rho) / [ (1-z)(1 - w_rho z) ],
a sum of simple-pole terms: poles at z=1 (common, the archimedean point) and at z_rho = 1/w_rho =
rho/(rho-1) (one per zero). The Bombieri-Lagarias disk map s = 1/(1-z) sends |z|<1 <-> Re s > 1/2 and
sends the pole z_rho to s = 1-rho.

KEY: |z_rho| = |rho|/|rho-1|.  ON-LINE rho=1/2+i*gamma: |rho|=|rho-1| EXACTLY -> |z_rho|=1 (pole on the
boundary circle). SUB-CRITICAL rho (Re<1/2): |rho|<|rho-1| -> |z_rho|<1 (pole INSIDE the disk). So:

   RH  <=>  G(z) is analytic in the open unit disk |z|<1  (no interior pole)
        <=>  every Li rung lambda_n >= 0  (Li's criterion)
        <=>  the Nevanlinna measure mu of m_B = -Xi'/Xi is >= 0  (= u_B>=0, N6 reading 3).

This is the 'all rungs at once' positivity: ONE analyticity / one positive-measure statement replaces
the infinitely many lambda_n>=0. The interior poles ARE the sub-critical zeros, so it is EXACTLY RH --
a unification (Li coefficients = disk analyticity = Herglotz measure = curvature holonomy), not a bypass.
The archimedean part of mu (the smooth zero density ~ (1/2pi)log(t/2pi)) is the positive dominant piece;
RH = it dominates the indefinite prime fluctuation (arch-domination, in measure form).

mpmath. No torch.
"""
import mpmath as mp
mp.mp.dps = 25

def zrho(rho):                    # pole of G in the z-plane:  z_rho = rho/(rho-1)
    rho = mp.mpc(rho)
    return rho/(rho-1)

print("=" * 92)
print("(1) the pole map |z_rho| = |rho|/|rho-1|: ON-LINE -> 1 (boundary); SUB-CRITICAL -> <1 (interior)")
print("=" * 92)
print(f"  {'zero rho':>20} {'|z_rho|=|rho|/|rho-1|':>22} {'location':>22}")
onlines = [mp.mpc(0.5, 14.1347), mp.mpc(0.5, 21.022), mp.mpc(0.5, 50.0)]
subcrit = [mp.mpc(0.3, 5.0), mp.mpc(0.45, 10.0), mp.mpc(0.1, 3.0)]
for rho in onlines:
    z = zrho(rho); print(f"  {str(rho):>20} {mp.nstr(abs(z),16):>22} {'ON boundary |z|=1':>22}")
for rho in subcrit:
    z = zrho(rho); print(f"  {str(rho):>20} {mp.nstr(abs(z),16):>22} {'INSIDE |z|<1 (sub-crit)':>22}")
print("  => on-line zeros park their pole exactly on |z|=1; a sub-critical zero (Re<1/2) drops a pole")
print("     INSIDE the disk. RH <=> no interior pole <=> G analytic on |z|<1.")

print("\n" + "=" * 92)
print("(2) true zeta: G(z)=sum lambda_n z^n converges in |z|<1 (analytic; radius 1, singular at z=1)")
print("=" * 92)
N = 150
zeros = [mp.zetazero(k) for k in range(1, N + 1)]
thetas = [mp.arg(1 - 1/r) for r in zeros]
def lam(n):                       # lambda_n partial via on-line zeros: sum 2(1-cos n theta) >= 0
    return mp.fsum(2*(1 - mp.cos(n*th)) for th in thetas)
lams = [lam(n) for n in range(1, 121)]
def G_partial(z, M):
    return mp.fsum(lams[n-1] * z**n for n in range(1, M+1))
print(f"  {'z':>8} {'G_60(z)':>16} {'G_120(z)':>16} {'converging?':>14}")
for z in (mp.mpf('0.5'), mp.mpf('0.8'), mp.mpf('0.9'), mp.mpc('0', '0.9')):
    g60, g120 = G_partial(z, 60), G_partial(z, 120)
    conv = abs(g120 - g60) < 0.05 * (abs(g120) + 1)
    print(f"  {str(z):>8} {mp.nstr(g60,7):>16} {mp.nstr(g120,7):>16} {str(conv):>14}")
print("  => partial sums of G stabilize inside |z|<1 (lambda_n ~ (n/2)log n, radius of convergence 1):")
print("     G is analytic in the disk for true zeta -- consistent with RH (no interior pole).")

print("\n" + "=" * 92)
print("(3) a SUB-CRITICAL zero puts an interior pole: G blows up at z_rho inside the disk")
print("=" * 92)
def G_closed(zeroset, z):         # exact closed form sum_rho z(1-w)/((1-z)(1-w z)), w=1-1/rho
    z = mp.mpc(z); tot = mp.mpc(0)
    for rho in zeroset:
        w = 1 - 1/mp.mpc(rho)
        tot += z*(1-w) / ((1-z)*(1 - w*z))
    return tot
# toy: a few on-line zeros (+conjugates) plus ONE sub-critical zero rho0 and its conjugate
rho0 = mp.mpc(0.3, 5.0)
toy = [mp.mpc(0.5, 14.13), mp.mpc(0.5,-14.13), mp.mpc(0.5,21.0), mp.mpc(0.5,-21.0), rho0, mp.conj(rho0)]
zp = zrho(rho0)
print(f"  sub-critical zero rho0={rho0}; its pole z_rho0 = {mp.nstr(zp,6)}, |z_rho0|={mp.nstr(abs(zp),6)} (<1, INSIDE)")
print(f"  {'z (approaching z_rho0)':>26} {'|G_toy(z)|':>18}")
for t in (mp.mpf('0.7'), mp.mpf('0.9'), mp.mpf('0.97'), mp.mpf('0.995')):
    z = t * zp                    # march toward the interior pole along the ray
    print(f"  {'t='+mp.nstr(t,4)+' * z_rho0':>26} {mp.nstr(abs(G_closed(toy, z)),8):>18}")
print("  => |G_toy| blows up as z -> z_rho0 INSIDE the disk: the sub-critical (off-line) zero is an")
print("     interior pole of the generating function. That is the single obstruction to 'G analytic in")
print("     |z|<1' = the obstruction to all lambda_n>=0.")

print("\n" + "=" * 92)
print("(4) the all-at-once positivity = the Nevanlinna measure of m_B >= 0  (= u_B>=0, N6)")
print("=" * 92)
print("""  m_B(z) = -Xi'/Xi is Herglotz on C+  <=>  it has a Nevanlinna representation with a POSITIVE measure
  mu;  under RH, mu = sum_n delta_{gamma_n} (point masses at the real zero-heights, all positive), and
  u_B = Im m_B is its Poisson integral.  lambda_n >= 0 for all n  <=>  mu >= 0  <=>  G analytic in the
  disk  <=>  RH.  The 'all rungs at once' object IS this single measure mu.  Its archimedean part is the
  smooth zero density ~ (1/2pi)log(t/2pi) (positive, growing); the prime part is the indefinite
  fluctuation.  mu >= 0  =  the archimedean density dominates the fluctuation  =  arch-domination.""")

print("\n" + "=" * 92)
print("VERDICT  --  the all-rungs-at-once positivity, found and placed (honest)")
print("=" * 92)
print("""  FOUND: the single object that closes all rungs at once is the Li generating function
  G(z)=sum lambda_n z^n (closed form: poles at z=1 and z_rho=rho/(rho-1)).  RH  <=>  G is ANALYTIC in
  the open unit disk |z|<1  <=>  no interior pole  <=>  every lambda_n>=0  <=>  the Nevanlinna measure
  mu of m_B is >=0  <=>  u_B>=0 (N6 reading 3).  ONE analyticity / one positive measure replaces the
  infinitely many rung checks.
  UNIFICATION (the genuine gain): the Li ladder (coefficients), the curvature/holonomy (interior poles
  = sub-critical zeros, exactly the curvature atoms of N6 Rem 6.3 transported by the disk map), and the
  Herglotz/Bures field (measure mu, N6 reading 3) are now ONE statement about G.  The archimedean part
  of mu is the explicit positive dominant piece.
  HONEST: this is NOT a bypass.  The interior poles ARE the off-line zeros, so 'G analytic in the disk'
  is RH by definition; establishing it = proving mu>=0 = arch-domination, the same content.  No
  checkable shortcut emerges -- a generating function cannot manufacture positivity its coefficients
  don't have.  What IS delivered: the all-at-once object is identified and maximally explicit (one
  positive measure, archimedean part known), and four readings are unified.  Closing it is RH.""")
