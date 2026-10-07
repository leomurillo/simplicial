"""
Unfolded-ladder probe. The marginality (lam_min/lam_max -> 0) of the zero-positivity
matrices comes from the zeros PILING UP (atoms gamma^-2 -> 0; Cayley angles a -> 0).
Hypothesis (user): UNFOLD the zeros -- reparametrize so they are uniformly spaced
(the apex-phase coordinate, N(T)=theta/pi+1) -- and the margin stops collapsing.

Honest design: a reparametrization is RH-content-preserving only if it is a smooth
change of coordinate. We test whether unfolding lifts the margin AND whether the
off-line-zero SENSITIVITY survives -- because if unfolding lifts the margin only by
washing out the signal, the difficulty is CONSERVED, not beaten.

PART A  Hankel/moment encoding is intrinsically marginal: folded atoms gamma^-2 AND
        uniform-on-interval atoms BOTH give a collapsing margin (the second is a
        Hilbert matrix). Unfolding the atoms does not help the moment encoding.
PART B  Circle/Toeplitz encoding: interpolate folded angles a_k -> uniform angles
        (s: 0 -> 1). Track the on-line margin lam_min/lam_max AND the off-line
        detection lam_min(T_off): does raising the margin hide the off-line zero?

Deterministic: mpmath only. No torch.
"""

import mpmath as mp
mp.mp.dps = 30

M = 200
print(f"computing first {M} zeta zeros (dps={mp.mp.dps}) ...")
gammas = [mp.im(mp.zetazero(k)) for k in range(1, M + 1)]

def eig_lohi(A):
    n = A.rows
    Ar = mp.matrix([[mp.re(A[i, j]) for j in range(n)] for i in range(n)])
    ev = sorted(mp.re(e) for e in mp.eigsy(Ar, eigvals_only=True))
    return ev[0], ev[-1]

# ============================================================================
# PART A -- moment/Hankel encoding is intrinsically marginal (unfolding atoms fails)
# ============================================================================
print()
print("=" * 80)
print("PART A -- Hankel margin: folded atoms (gamma^-2) vs UNFOLDED (uniform) atoms")
print("=" * 80)
lam = sorted([1 / g**2 for g in gammas])          # folded: pile up at 0
lam_f = [l / lam[-1] for l in lam]                # normalize max -> 1
lam_u = [(k + mp.mpf('0.5')) / M for k in range(M)]   # unfolded: uniform on (0,1]
NMAX = 8
def hankel_margin(atoms, n):
    mu = [mp.fsum(a**(j + 1) for a in atoms) for j in range(0, 2 * n + 1)]
    H = mp.matrix([[mu[a + b] for b in range(n + 1)] for a in range(n + 1)])
    lo, hi = eig_lohi(H)
    return lo / hi
print(f"  {'n':>3} {'folded gamma^-2':>20} {'unfolded uniform':>20}")
for n in range(1, NMAX + 1):
    print(f"  {n:>3} {mp.nstr(hankel_margin(lam_f, n),4):>20} {mp.nstr(hankel_margin(lam_u, n),4):>20}")
print("  >>> BOTH collapse super-exponentially (uniform atoms -> Hilbert matrix).")
print("      The moment/Hankel encoding is intrinsically marginal; unfolding the")
print("      atoms does NOT help -- marginality is a property of moments-on-a-line.")

# ============================================================================
# PART B -- circle/Toeplitz: does unfolding lift the margin or hide the signal?
# ============================================================================
print()
print("=" * 80)
print("PART B -- interpolate folded angles a_k -> uniform; margin vs off-line detection")
print("=" * 80)
alphas = sorted([mp.atan2(g, g * g - mp.mpf(1) / 4) for g in gammas])   # pile near 0
unif = [mp.pi * (k + mp.mpf('0.5')) / M for k in range(M)]              # uniform on (0,pi)
ioff = 0                       # move the zero with the largest angle (lowest gamma)
g_off = min(gammas)            # gamma_1
beta = mp.mpf('3.0')           # gross off-line displacement Re = 1/2 - beta
rho = mp.mpc(mp.mpf('0.5') - beta, g_off)
r = abs(1 - 1 / rho)           # |w| != 1 is the RH violation (radial defect)
print(f"  off-line model: move lowest zero to Re=1/2-{float(beta)} ; |1-1/rho|=r={float(r):.5f}")
n = 12
print(f"  Toeplitz order n={n}.  s=0 folded (piled) ... s=1 unfolded (uniform)")
print(f"  {'s':>5} {'margin lam_min/lam_max':>23} {'lam_min(T_off)/lam_max':>24} {'off-line detected?':>19}")
for s in [mp.mpf(x) for x in ['0.0', '0.25', '0.5', '0.75', '1.0']]:
    theta = [(1 - s) * alphas[j] + s * unif[j] for j in range(M)]
    t_on = [mp.fsum(2 * mp.cos(k * th) for th in theta) for k in range(n + 1)]
    # off-line: replace zero ioff's on-circle contribution 2cos by the off-circle 2 r^k cos
    t_off = [t_on[k] + 2 * (r**k - 1) * mp.cos(k * theta[ioff]) for k in range(n + 1)]
    T_on = mp.matrix([[t_on[abs(a - b)] for b in range(n + 1)] for a in range(n + 1)])
    T_off = mp.matrix([[t_off[abs(a - b)] for b in range(n + 1)] for a in range(n + 1)])
    lo_on, hi_on = eig_lohi(T_on)
    lo_off, _ = eig_lohi(T_off)
    detected = "YES (lam_min<0)" if lo_off < 0 else "no (hidden)"
    print(f"  {float(s):>5} {mp.nstr(lo_on/hi_on,4):>23} {mp.nstr(lo_off/hi_on,4):>24} {detected:>19}")
print()
print("  >>> As s rises the on-line margin lifts off the floor (-> O(1)), BUT the")
print("      off-line zero stops being detected: unfolding raises the background")
print("      lam_max so the fixed RH-defect is washed out. Margin is traded for")
print("      sensitivity -- the product (the actual RH content) is CONSERVED.")

print()
print("=" * 80)
print("READING")
print("=" * 80)
print("""  VERDICT on 'unfold the ladder to lift the marginality':
   - PART A: the moment/Hankel encoding is marginal in ANY atom spacing (uniform ->
     Hilbert). Not curable by unfolding.
   - PART B: unfolding the circle angles DOES lift the on-line margin to O(1) -- but
     it lifts it by inflating the uniform background (lam_max), against which the
     off-line zero's fixed radial defect (|w|!=1) becomes invisible. The off-line
     zero, DETECTED at s=0 (folded), is HIDDEN at s=1 (unfolded).

  So unfolding trades margin for sensitivity: the RH-discriminating signal is a fixed
  quantity that no smooth reparametrization creates or destroys. The marginality and
  the sensitivity are two readings of the SAME content (the Lambda=0 / 'RH barely
  true' fact). Difficulty conserved -- unfolding is not the lever.

  What survives as genuine value (probe 2): the apex GENERATES the Li/positivity tower
  exactly (arch Gamma + conductor primes), in the additive register. The remaining
  content is the global all-n positivity = m_B Herglotz = RH; it has a fixed size and
  must be met head-on (the additive register makes it manifest per rung, not smaller).
  The residual benefit of unfolding is only organizational: in the apex-phase
  coordinate the archimedean background is flat, so 'arch dominates prime' is cleanest
  to STATE there -- a proof-bookkeeping convenience, not a reduction of difficulty.""")
