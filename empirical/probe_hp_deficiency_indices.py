"""
probe_hp_deficiency_indices.py   --  operator-build, task (2): deficiency indices / self-adjoint
extensions of the Hilbert-Polya dilation operator, honestly.

OPERATOR. The HP / Berry-Keating base (HPo Move 6) is the dilation generator
        D = -i(x d/dx + 1/2)   on  L^2(R_+, dx)   (equivalently -i d/du on L^2 in u=log x).
von Neumann: deficiency indices n_pm = dim ker(D* -+ i I) in L^2; D is essentially self-adjoint iff
(n_+,n_-)=(0,0); otherwise an (n,n)-parameter family of self-adjoint extensions.

THREE REGIMES (each settles something):
  (1) BARE D on (0,infinity).  Solve D* psi = +-i psi: psi = x^{-3/2} (for +i), x^{1/2} (for -i).
      Neither is L^2 (x^{-3/2} blows up at 0, x^{1/2} at infinity) -> (0,0): ESSENTIALLY SELF-ADJOINT,
      but spectrum is CONTINUOUS (= R, via Mellin -> momentum). Rigid, but not a discrete HP operator.
  (2) CUTOFF D = -i d/du on a finite log-box [0,L] (the Connes-type regularization).
      Deficiency solutions e^{+-u} are BOTH L^2 on [0,L] -> (1,1): a U(1) family of self-adjoint
      extensions D_theta with domain psi(L)=e^{i theta}psi(0), eigenvalues
          lambda_n(theta) = (2 pi n + theta)/L,   n in Z   -- an ARITHMETIC PROGRESSION (spacing 2pi/L).
  (3) Compare the extension spectra to the actual zeta zeros. The zeros' spacing SHRINKS (Weyl law
      N(T) ~ (T/2pi) log(T/2pi): density grows like log). No arithmetic progression (any L, any theta)
      can track them -> the boundary phase is the WRONG knob; the zeros' density must come from a
      POTENTIAL (the archimedean Gamma-curvature), not a boundary condition.

VERDICT (honest, either way): deficiency indices settle SELF-ADJOINTNESS (achievable -- (0,0) bare,
or a clean (1,1) extension family with the cutoff), but NOT spectrum = zeros. The extension freedom is
a U(1) phase that only SHIFTS an arithmetic ladder; the zeros' increasing density lives in the
potential = the archimedean data. So the rigidity that matters is the DRESSED operator's, and
'self-adjoint' is necessary-not-sufficient: real discrete spectrum is free for a confining potential,
but spectrum = the zeros is the explicit-formula / archimedean identification = RH. Task 2 rules out
the boundary-condition shortcut concretely and returns to the archimedean potential (the wall).

mpmath + numpy. No torch.
"""
import numpy as np
import mpmath as mp
mp.mp.dps = 20

print("="*84)
print("(1) BARE dilation D = -i(x d/dx + 1/2) on L^2(R_+, dx):  deficiency via L^2-membership")
print("="*84)
# deficiency solutions: D* psi = +i psi -> psi=x^{-3/2};  D* psi = -i psi -> psi=x^{1/2}
def l2norm_sq(power, a, b):    # integral_a^b |x^power|^2 dx = integral x^{2 power} dx
    p = 2*power
    if abs(p+1) < 1e-12: return np.log(b/a)
    return (b**(p+1)-a**(p+1))/(p+1)
print("  D* psi = +i psi  =>  psi = x^{-3/2}:")
for (a,b) in [(1e-3,1.0),(1e-6,1.0),(1e-9,1.0)]:
    print(f"     ||psi||^2 on [{a:.0e},{b:.0f}] = {l2norm_sq(-1.5,a,b):.3e}  (-> infinity as a->0: NOT L^2)")
print("  D* psi = -i psi  =>  psi = x^{1/2}:")
for (a,b) in [(1.0,1e3),(1.0,1e6),(1.0,1e9)]:
    print(f"     ||psi||^2 on [{a:.0f},{b:.0e}] = {l2norm_sq(0.5,a,b):.3e}  (-> infinity as b->inf: NOT L^2)")
print("  => neither deficiency solution is L^2  ::  (n_+, n_-) = (0,0)  ::  ESSENTIALLY SELF-ADJOINT.")
print("     But the spectrum is CONTINUOUS (= R, momentum on the log-line): rigid, NOT a discrete HP operator.")

print("\n" + "="*84)
print("(2) CUTOFF dilation -i d/du on [0,L] (Connes-type regularization): deficiency + extensions")
print("="*84)
L = 10.0
# deficiency solutions e^{+-u} are both L^2 on [0,L]:
print(f"  deficiency solutions on [0,{L:.0f}]:  ||e^{{+u}}||^2 = {(np.exp(2*L)-1)/2:.3e},  ||e^{{-u}}||^2 = {(1-np.exp(-2*L))/2:.3f}")
print("  both finite (L^2)  ::  (n_+, n_-) = (1,1)  ::  a U(1) family of self-adjoint extensions D_theta.")
# extension eigenvalues lambda_n(theta) = (2 pi n + theta)/L
print(f"  {'theta':>7} {'first few eigenvalues (2 pi n + theta)/L':>46} {'spacing':>10}")
for theta in (0.0, np.pi/2, np.pi):
    ev = [(2*np.pi*n + theta)/L for n in range(-1,4)]
    print(f"  {theta:>7.3f} {str([round(e,4) for e in ev]):>46} {2*np.pi/L:>10.4f}")
print("  => every extension's spectrum is an ARITHMETIC PROGRESSION, spacing 2pi/L = const. theta only SHIFTS it.")

print("\n" + "="*84)
print("(3) DO ANY EXTENSION SPECTRA TRACK THE ZEROS?  (zeros have INCREASING density -> no)")
print("="*84)
NZ = 40
gam = np.array([float(mp.im(mp.zetazero(n))) for n in range(1, NZ+1)])
gaps = np.diff(gam)
# best arithmetic fit gamma_n ~ a n + b (least squares); residual measures departure from a ladder
nidx = np.arange(1, NZ+1)
Acoef = np.vstack([nidx, np.ones_like(nidx)]).T
(a_fit, b_fit), res, *_ = np.linalg.lstsq(Acoef, gam, rcond=None)
fit = a_fit*nidx + b_fit
rms = np.sqrt(np.mean((gam-fit)**2))
print(f"  first/last zero: {gam[0]:.3f} ... {gam[-1]:.3f}")
print(f"  consecutive gaps: first={gaps[0]:.3f}  median={np.median(gaps):.3f}  last={gaps[-1]:.3f}  (SHRINKING)")
print(f"  Weyl density (1/2pi)log(gamma/2pi):  at gamma={gam[5]:.1f}: {np.log(gam[5]/(2*np.pi))/(2*np.pi):.4f}/unit, "
      f"at gamma={gam[-1]:.1f}: {np.log(gam[-1]/(2*np.pi))/(2*np.pi):.4f}/unit  (GROWS)")
print(f"  best arithmetic-progression fit gamma_n ~ {a_fit:.3f} n + {b_fit:.3f}:  RMS residual = {rms:.3f}")
print(f"     (a pure ladder would have residual ~0; {rms:.2f} is large -> the zeros are NOT an arithmetic progression)")
print("  => no boundary-phase extension D_theta (any L, theta) reproduces the zeros: the increasing")
print("     density is a POTENTIAL effect (Weyl law), not a boundary-condition effect.")

print("\n" + "="*84)
print("VERDICT (task 2)")
print("="*84)
print("""  Deficiency indices, computed honestly:
    - bare dilation: (0,0) -- essentially self-adjoint, but CONTINUOUS spectrum (not a discrete HP op);
    - cutoff dilation: (1,1) -- a clean U(1) family of self-adjoint extensions, every one with an
      ARITHMETIC-PROGRESSION spectrum (theta merely shifts the ladder).
  Neither tracks the zeros: the zeros' density GROWS like (1/2pi)log(gamma/2pi), so no arithmetic
  ladder fits (RMS residual large). The zeros' density is carried by the POTENTIAL (the archimedean
  Gamma-curvature / the Weyl law), NOT by the self-adjoint-extension boundary phase.

  So the self-adjoint-EXTENSION freedom is the WRONG knob -- it is ruled out, concretely, as the lever.
  The rigidity that matters is the DRESSED operator's self-adjointness, and that is necessary-not-
  sufficient: a confining apex/archimedean potential gives a self-adjoint operator with real discrete
  spectrum FOR FREE (essential self-adjointness at infinity), but whether that spectrum IS the zeros is
  the explicit-formula / archimedean-positivity identification = RH. Task 2 settles: deficiency/extension
  is concrete and gives self-adjointness, but not spectrum=zeros; the lever is the archimedean potential,
  i.e. the same wall -- now with the boundary-condition shortcut explicitly closed.""")
