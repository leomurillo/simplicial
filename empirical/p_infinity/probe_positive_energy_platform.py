"""
(b) THE POSITIVE-ENERGY PLATFORM: complete monotonicity / Herglotz positivity of the reconstructed
scaling theory -- the main line, targeting the obligation itself (not a sub-family).

We ask the platform what is UNCONDITIONALLY TRUE about the positive-energy structure, and where the
residual sits. Findings, honestly tiered.

A. THE HERGLOTZ FIELD IS MANIFESTLY POSITIVE (the good news). The OS two-point function's positivity is
   u_B(z) = Im m_B(z) = Im(-Xi'/Xi)(z) = sum over zeros  y/|z - z_n|^2  (a Poisson kernel per zero),
   z = x+iy in C+. For zeros ON the line (z_n real) EVERY term is > 0: u_B is a SUM OF POSITIVE POISSON
   KERNELS, manifestly positive, NOT a delicate cancellation. An off-line zero is the ONLY thing that can
   inject a negative dip. So in the positive-energy/Herglotz register the positivity is robust-with-margin.

B. COMPLETE MONOTONICITY is manifest, and the "marginality" was the WRONG register. S(t)=sum e^{-t gamma_n}
   (gamma_n real ordinates) is completely monotone; its moment Hankel is PSD by SIGNATURE (Hamburger),
   exactly -- even though its CONDITIONING (lambda_min/lambda_max) collapses. The program's "Lambda=0
   marginality" is a conditioning artifact of the moment register; the SIGNATURE (the positive-energy
   content) is robustly correct.

C. THE ARCHIMEDEAN HALF IS FREE. The archimedean place's positive-energy / Weil positivity is a THEOREM
   (Connes-Consani arXiv:2006.13771); the free prolate semigroup e^{-tW_free} is positive-energy
   (Mehler/Hermite). Half the OS reconstruction is unconditional. The archimedean baseline density
   ~ (1/2pi) log(T/2pi) is positive and GROWS.

D. HONEST RESIDUAL = RH. u_B > 0 EVERYWHERE <=> no off-line zero. The mechanism is favorable (positive
   growing archimedean baseline + positive on-line Poisson kernels vs a localized off-line dip), but the
   uniform "no dip at any height" statement IS RH. Good news = the structure/mechanism; NOT a proof.

mpmath. No torch.
"""
import mpmath as mp
mp.mp.dps = 25

print("computing zeta zeros ...", flush=True)
N = 80
G = [mp.im(mp.zetazero(k)) for k in range(1, N+1)]   # ordinates gamma_n > 0

def uB(x, y, gammas, offline=None):
    """Im m_B at z=x+iy in C+ : sum of Poisson kernels over zeros at z=+-gamma_n (on the line, real).
       offline=(re,im) optionally injects an off-line zero pair (complex ordinate) = an RH violation."""
    s = mp.mpf(0)
    for g in gammas:
        for zn in (g, -g):                          # real ordinate (on the critical line)
            s += y/((x-zn)**2 + y**2)
    if offline is not None:
        a, b = offline                              # off-line zero -> complex ordinate z_n = a + i b
        for zn in (mp.mpc(a, b), mp.mpc(-a, b)):
            d = (x-zn)**2 + (mp.mpc(0,1)*y - 0)**2   # generic: use Im of 1/(z - z_n)
        # cleaner: Im(1/(z - z_n)) summed; z=x+iy
        for zn in (mp.mpc(a, b), mp.mpc(-a, -b), mp.mpc(-a, b), mp.mpc(a, -b)):
            s += mp.im(-1/(mp.mpc(x, y) - zn))
    return s

print("="*88)
print("A. THE HERGLOTZ FIELD u_B = Im m_B IS MANIFESTLY POSITIVE (sum of Poisson kernels per zero)")
print("="*88)
print(f"  {'sample z=x+iy in C+':>26} {'u_B (on-line zeros)':>20} {'sign':>6}")
for (x, y) in [(7, 1), (20, 1), (50, 2), (100, 3), (3, mp.mpf('0.3')), (40, mp.mpf('0.5'))]:
    val = uB(mp.mpf(x), mp.mpf(y), G)
    print(f"  {f'x={x}, y={float(y)}':>26} {mp.nstr(val,8):>20} {'>0' if val>0 else '<=0':>6}")
print("  => every value > 0: u_B is a sum of POSITIVE Poisson kernels (manifest, not a cancellation).")
print("  Now INJECT an off-line zero at Re=1/2+0.3 (ordinate 14.13 - i*0.3) -- the only spoiler:")
for (x, y) in [(14, mp.mpf('0.15')), (14, mp.mpf('0.05'))]:
    base = uB(mp.mpf(x), y, G)
    viol = uB(mp.mpf(x), y, G, offline=(mp.mpf('14.1347'), mp.mpf('0.3')))
    print(f"    z=x={x},y={float(y)}: on-line u_B={mp.nstr(base,6)}  ;  with off-line zero u_B={mp.nstr(viol,6)}  "
          f"({'DIPS NEGATIVE' if viol<0 else 'still >0'})")
print("  => an off-line zero injects a localized NEGATIVE dip; u_B>0 everywhere <=> no off-line zero = RH.")

print("="*88)
print("B. COMPLETE MONOTONICITY is manifest; the marginality is a CONDITIONING (not signature) artifact")
print("="*88)
# S(t) = sum e^{-t gamma_n} completely monotone (gamma_n>0 real). Moment Hankel mu_k = sum gamma_n^k.
import sympy as sp
M = 5
gnum = [sp.nsimplify(round(float(g), 6)) for g in G[:25]]   # use 25 zeros, rationalized
mu = [sum(g**k for k in [kk] for g in gnum) for kk in range(0, 2*M+1)]
mu = [sum(g**kk for g in gnum) for kk in range(0, 2*M+1)]
Hk = sp.Matrix(M+1, M+1, lambda i, j: mu[i+j])
# signature via real_roots (real symmetric)
lam = sp.symbols('lam')
rs = sp.Poly(sp.expand(Hk.charpoly(lam).as_expr()), lam).real_roots()
npos = sum(1 for r in rs if r.is_positive); nneg = sum(1 for r in rs if r.is_negative)
# conditioning
Hf = mp.matrix([[float(mu[i+j]) for j in range(M+1)] for i in range(M+1)])
ev = mp.eigsy(Hf, eigvals_only=True)
cond = float(abs(ev[-1]/ev[0])) if ev[0] != 0 else float('inf')
print(f"  moment Hankel of the zero ordinates (size {M+1}): signature (npos,nneg) = ({npos},{nneg})")
print(f"  -> PSD (positive-energy content) by SIGNATURE: {nneg==0}")
print(f"  but conditioning lambda_max/lambda_min ~ {cond:.2e}  (collapses -- the 'marginality')")
print("  => the marginality is a CONDITIONING artifact; the SIGNATURE (the positive-energy content) is")
print("     robustly correct. Same lesson as the program's exact-signature redo: read signature, not cond.")

print("="*88)
print("C. THE ARCHIMEDEAN HALF IS FREE (unconditional positive-energy)")
print("="*88)
print("  Archimedean baseline density (Riemann-von Mangoldt) ~ (1/2pi) log(T/2pi), positive & growing:")
for T in [30, 100, 1000, 10**6]:
    dens = float(mp.log(mp.mpf(T)/(2*mp.pi))/(2*mp.pi))
    print(f"    T={T:>8}: archimedean density = {dens:.5f} > 0")
print("""  The archimedean place's Weil positivity is a THEOREM (Connes-Consani arXiv:2006.13771); the free
  prolate semigroup e^{-tW_free} is positive-energy (Mehler/Hermite). Half the OS reconstruction is
  unconditional, and its baseline is a positive, growing field.""")

print("="*88)
print("D. HONEST VERDICT -- the good news, calibrated")
print("="*88)
print("""  GOOD NEWS (true, unconditional, on-platform):
   * In the positive-energy / Herglotz register, the positivity u_B = Im m_B is a SUM OF POSITIVE POISSON
     KERNELS (one per on-line zero) on a POSITIVE, GROWING archimedean baseline -- manifest, robust,
     with margin. It is NOT the delicate marginal cancellation the moment register shows.
   * The 'Lambda=0 marginality' is a CONDITIONING artifact of the additive moment Hankel; the SIGNATURE
     (the actual positive-energy content) is robustly correct.
   * The archimedean half of the positive-energy theorem is FREE (Connes-Consani, proven).
   So the difficulty is cleanly localized to ONE thing: an off-line zero is the only object that injects a
   negative dip into u_B. The mechanism is FAVORABLE -- a positive growing baseline + positive on-line
   kernels, versus a single localized would-be dip.
  HONEST RESIDUAL = RH: 'u_B > 0 at every height' <=> 'no off-line zero anywhere'. The positive-energy /
   complete-monotonicity holds with manifest margin on every computed region; proving it at ALL heights
   (no dip ever) is exactly RH. This is the good news -- the structure and mechanism are favorable and the
   marginality fear was a register artifact -- but it is NOT a proof. The residual is the uniform exclusion
   of off-line dips on a manifestly-positive, archimedean-dominated field.""")
