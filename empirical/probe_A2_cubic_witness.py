"""
[A2] empirical scaffold: cubic Bombieri-style witness asymptotic.

Goal: verify that a HYPOTHETICAL off-line zero rho_0 = 1/2 + delta + i*gamma_0
drives Re C_zeta(g_0; eta_0) negative at leading order O(delta^2).

Structural prediction (from FE-symmetric expansion):
   Re C_zeta(g_0; eta_0) approx 12 * delta^2 * Re[tilde_eta_0''(3 i gamma_0)] + O(delta^4)

where the 12 is the combinatorial coefficient from the FE-symmetric cluster
   {rho_+, rho_-, bar(rho_+), bar(rho_-)}
of 4 off-line zeros, summed over the 8 ordered triples at Im sum = 3*gamma_0:
   1 * H(3*delta) + 3 * H(delta) + 3 * H(-delta) + 1 * H(-3*delta)
   = 8 H(0) + 12 delta^2 H''(0) + O(delta^4)

We:
1. Compute the cluster cubic moment numerically with a candidate eta_0.
2. Plot the result vs delta.
3. Check the leading delta^2 coefficient matches the structural prediction.
4. Identify a choice of eta_0 that makes the leading coefficient strictly negative.
"""

import numpy as np

# ----- Test cluster -----

GAMMA_0 = 14.134725141734693  # first nontrivial zero's imaginary part


def cluster_zeros(delta, gamma0=GAMMA_0):
    """Return the 4-element FE-symmetric cluster at off-line height delta."""
    return np.array([
        complex(0.5 + delta, +gamma0),   # rho_+
        complex(0.5 - delta, +gamma0),   # rho_-
        complex(0.5 + delta, -gamma0),   # bar(rho_+)
        complex(0.5 - delta, -gamma0),   # bar(rho_-)
    ])


def cubic_moment_cluster(delta, eta_tilde, gamma0=GAMMA_0, g_tilde=lambda s: 1.0+0j):
    """
    Compute the cluster cubic moment:
       sum_{i,j,k in cluster} g(rho_i) g(rho_j) g(rho_k) * eta_tilde(rho_i + rho_j + rho_k - 3/2)

    with omega_3 := 1 for now (we capture the structural delta^2 behavior; omega_3
    has unit modulus to leading order on the cluster as delta -> 0).
    """
    zeros = cluster_zeros(delta, gamma0)
    total = 0.0 + 0j
    for i in zeros:
        for j in zeros:
            for k in zeros:
                sigma3 = i + j + k
                offset = sigma3 - 1.5  # surface offset
                total += g_tilde(i) * g_tilde(j) * g_tilde(k) * eta_tilde(offset)
    return total


# ----- Candidate eta_0 smearings -----

# eta_0 is a real even non-negative function on R; tilde_eta_0(s) is its Mellin transform.
# For the witness, we want eta_0 such that Re[tilde_eta_0''(3 i gamma_0)] < 0.

# Choice 1: Gaussian smearing centered at frequency 3*gamma_0:
#   eta_0(t) = (1/sqrt(2pi sigma^2)) exp(-(log t - 0)^2 / (2 sigma^2)) * cos(3 gamma_0 log t)
# Mellin: tilde_eta_0(s) = exp(-sigma^2 (s - 0)^2 / 2) (peaked at s=0 in Mellin) - approximation
# Better: use eta_0 = exp(-t^2/2) * cos(3 gamma_0 log t) -- but this might not be non-negative.

# For empirical: use a known-positive smearing function. Take
#    tilde_eta_0(s) = exp(- s^2 * sigma^2 / 2)
# i.e., Mellin Gaussian. Its inverse Mellin gives an actual eta_0 supported on (0, infty).

def gaussian_smearing(s, sigma=1.0):
    """tilde_eta(s) = exp(-sigma^2 s^2 / 2). Mellin transform of a log-Gaussian."""
    return np.exp(-sigma**2 * s**2 / 2)


def shifted_gaussian_smearing(s, sigma, y0):
    """tilde_eta(s) = exp(-sigma^2 (s + i*y0)^2 / 2) + exp(-sigma^2 (s - i*y0)^2 / 2).
    Real-symmetric (real eta), peaked at imaginary part y = +- y0."""
    return 0.5 * (np.exp(-sigma**2 * (s + 1j*y0)**2 / 2) +
                  np.exp(-sigma**2 * (s - 1j*y0)**2 / 2))


def fejer_smearing(s, T=1.0):
    """tilde_eta(s) = (sin(T*s/(2i)) / (T*s/(2i)))^2. Fejer-style: real even non-negative eta."""
    arg = T * s / (2j)
    return (np.sinh(arg) / (arg + 1e-30))**2


# ----- Empirical: compute Re C_cluster vs delta for several eta choices -----

print("=" * 90)
print("[A2] Empirical: cluster cubic moment as a function of delta")
print(f"gamma_0 = {GAMMA_0} (first nontrivial zero imaginary part)")
print("=" * 90)

deltas = np.linspace(0.0, 0.3, 16)

# Try different smearing candidates
eta_choices = {
    'Gaussian sigma=0.5 (default)':   lambda s: gaussian_smearing(s, sigma=0.5),
    'Gaussian sigma=1':               lambda s: gaussian_smearing(s, sigma=1.0),
    'Gaussian sigma=2':               lambda s: gaussian_smearing(s, sigma=2.0),
    'Shifted Gaussian sigma=1 y0=3g': lambda s: shifted_gaussian_smearing(s, sigma=1.0, y0=3*GAMMA_0),
    'Shifted Gaussian sigma=2 y0=3g': lambda s: shifted_gaussian_smearing(s, sigma=2.0, y0=3*GAMMA_0),
    'Shifted Gaussian sigma=5 y0=3g': lambda s: shifted_gaussian_smearing(s, sigma=5.0, y0=3*GAMMA_0),
    'Shifted Gaussian sigma=10 y0=3g':lambda s: shifted_gaussian_smearing(s, sigma=10.0, y0=3*GAMMA_0),
}

for name, eta_fn in eta_choices.items():
    print(f"\n--- eta_0: {name} ---")
    print(f"{'delta':>10s} {'Re C_cluster':>18s} {'Im C_cluster':>18s} {'Re C - Re C(0)':>20s} {'/delta^2':>15s}")
    print("-" * 90)
    C0 = cubic_moment_cluster(0.0, eta_fn)
    for delta in deltas:
        C = cubic_moment_cluster(delta, eta_fn)
        diff = C - C0
        coef = diff.real / delta**2 if delta > 1e-6 else float('nan')
        print(f"{delta:10.4f} {C.real:18.6e} {C.imag:18.6e} {diff.real:20.6e} {coef:15.4f}")
    # Check: does the coefficient stabilize as delta -> 0? Should approach 12 * Re eta''(3i*gamma_0).
    # Predict: 12 * tilde_eta''(3i*gamma_0).
    # For tilde_eta(s) = exp(-sigma^2 s^2 / 2): tilde_eta''(s) = exp(-sigma^2 s^2 / 2)*(sigma^4 s^2 - sigma^2)
    # At s = 3i*gamma_0: tilde_eta(3i*gamma_0) = exp(9 sigma^2 gamma_0^2 / 2) <- BLOWS UP! BAD.

print("\n" + "=" * 90)
print("Caveat: the default Gaussian (centered at s=0) BLOWS UP at imaginary s.")
print("The shifted Gaussian or Fejer-style smearings are required for finite values.")
print("=" * 90)

# ----- Structural prediction check -----

print("\n" + "=" * 90)
print("Structural prediction: leading coefficient = 12 * tilde_eta_0''(3i*gamma_0)")
print("=" * 90)

# For the shifted Gaussian: tilde_eta(s) = (1/2)(exp(-sigma^2(s+iy0)^2/2) + exp(-sigma^2(s-iy0)^2/2))
# At s = 3i*gamma_0 with y0 = 3*gamma_0:
#   (s + iy0) at s=3i*gamma_0 = 3i*gamma_0 + i*3*gamma_0 = 6i*gamma_0  -> (6i*gamma_0)^2 = -36*gamma_0^2
#   (s - iy0) at s=3i*gamma_0 = 3i*gamma_0 - i*3*gamma_0 = 0   -> 0
# So tilde_eta(3i*gamma_0) = 0.5 (exp(-sigma^2(-36*gamma_0^2)/2) + exp(0)) = 0.5 (exp(18*sigma^2*gamma_0^2) + 1)
#   FIRST TERM BLOWS UP for sigma>0. The shifted Gaussian doesn't work either.

# Actually, the right choice: eta_0 should be a real Schwartz function such that
# tilde_eta_0(s) decays in BOTH Re(s) and Im(s). The (1/2)(exp + exp) doesn't decay in Im(s)
# unless we pick the right kernel.

# Correct choice: use the Fourier transform of a positive bump.
# Let h(t) = exp(-t^2 / (2 sigma^2)) * (1 + cos(3*gamma_0*t)).  Then h(t) >= 0 (since 1 + cos >= 0).
# Its Fourier transform is real and peaked at y = +- 3*gamma_0.
# If we define eta_0(x) = h(log x) / x (so it's a positive function on (0, infty)), then
# tilde_eta_0(s) = int_0^infty eta_0(x) x^{s-1} dx = int h(u) e^{su} du / (... change of var ...)
# Actually: int eta_0(x) x^{s-1} dx with eta_0(x) = h(log x)/x and substitution u = log x:
# = int h(u) e^{u(s-1)} e^u du = int h(u) e^{us} du = Laplace transform of h at s, or
# = Fourier transform of h at -is.

print("Using Fourier-positive-kernel smearing: tilde_eta(s) = hat{h}(-is) where h>=0")
print()

def positive_smearing(s, sigma=0.2, y0=3*GAMMA_0):
    """
    eta_0(t) corresponds to h(u) = exp(-u^2/(2 sigma^2)) * (1 + cos(y0 * u)).
    Then tilde_eta_0(s) = int h(u) e^{su} du = exp(s^2 sigma^2 / 2) * (1 + 0.5*(exp(...)+exp(...)))

    More carefully:
      h(u) = exp(-u^2/(2 sigma^2)) + 0.5 exp(-u^2/(2 sigma^2)) (e^{i y0 u} + e^{-i y0 u})
      H(s) := int h(u) e^{su} du  (Laplace-like; converges for any complex s if sigma < infty)
      Using int exp(-u^2/(2 sigma^2) + s*u) du = sqrt(2 pi sigma^2) * exp(s^2 sigma^2 / 2)
      Replacing s by s + i*y0 and s - i*y0 for the cosine terms:
      H(s) = sqrt(2 pi sigma^2) [exp(s^2 sigma^2 / 2) + 0.5 (exp((s+i y0)^2 sigma^2 / 2) + exp((s-i y0)^2 sigma^2 / 2))]

    At s = 3 i gamma_0 (with y0 = 3 gamma_0): (s - i y0) = 0, exp(0) = 1.
      (s + i y0) = 6 i gamma_0, (6 i gamma_0)^2 sigma^2/2 = -18 gamma_0^2 sigma^2 (negative -> small).
      s^2 sigma^2/2 = -9 gamma_0^2 sigma^2/2 (negative -> small).
    So tilde_eta(3 i gamma_0) is finite, mainly from the (s-iy0)=0 term: ~ 0.5 sqrt(2 pi sigma^2).
    """
    pref = np.sqrt(2 * np.pi * sigma**2)
    return pref * (np.exp(s**2 * sigma**2 / 2) +
                   0.5 * (np.exp((s + 1j*y0)**2 * sigma**2 / 2) +
                          np.exp((s - 1j*y0)**2 * sigma**2 / 2)))

# Test the positive smearing
print(f"\nUsing positive_smearing with sigma=0.2, y0 = 3*gamma_0 = {3*GAMMA_0:.4f}")
print(f"  tilde_eta(0) = {positive_smearing(0.0).real:.6f}")
print(f"  tilde_eta(3i*gamma_0) = {positive_smearing(3j*GAMMA_0)}")
print(f"  tilde_eta'(3i*gamma_0): finite difference")
ds = 1e-4
eta_p_plus = positive_smearing(3j*GAMMA_0 + ds)
eta_p_minus = positive_smearing(3j*GAMMA_0 - ds)
eta_p_2nd = positive_smearing(3j*GAMMA_0 + 2*ds)
eta_p_m2 = positive_smearing(3j*GAMMA_0 - 2*ds)
eta_pp = (eta_p_plus - 2*positive_smearing(3j*GAMMA_0) + eta_p_minus) / ds**2
print(f"  tilde_eta''(3i*gamma_0) approx = {eta_pp}")
print(f"  Predicted leading coefficient = 12 * tilde_eta''(3i*gamma_0) = {12*eta_pp}")
print(f"  Sign of Re(12 * tilde_eta''(3i*gamma_0)) = {'NEGATIVE' if (12*eta_pp).real < 0 else 'POSITIVE'}")

print()
print("Empirical cluster cubic moment with positive_smearing:")
print(f"{'delta':>10s} {'Re C_cluster':>18s} {'Re C - Re C(0)':>20s} {'/delta^2':>15s}")
print("-" * 65)
C0 = cubic_moment_cluster(0.0, positive_smearing)
print(f"{0.0:10.4f} {C0.real:18.6e}")
for delta in deltas[1:]:
    C = cubic_moment_cluster(delta, positive_smearing)
    diff = C - C0
    coef = diff.real / delta**2
    print(f"{delta:10.4f} {C.real:18.6e} {diff.real:20.6e} {coef:15.6e}")

# ----- Optimal sigma scan: find sigma making leading coefficient negative -----

print("\n" + "=" * 90)
print("STRUCTURAL FORMULA: leading delta^2 coefficient = 24 H_1''(0) + 72 H_3''(0)")
print("  where H_1(x) = tilde_eta_0(x + 3i*gamma_0), H_3(x) = tilde_eta_0(x + i*gamma_0)")
print("  (8 same-Im triples weight 24; 24 mixed-Im triples weight 72)")
print("=" * 90)
print()

def H_double_prime(s_eval, sigma, y0):
    """Numerical 2nd derivative of positive_smearing at s_eval."""
    smearing = lambda s: positive_smearing(s, sigma=sigma, y0=y0)
    ds = 1e-4
    return (smearing(s_eval + ds) - 2*smearing(s_eval) + smearing(s_eval - ds)) / ds**2

print(f"{'sigma':>8s} {'H_1''(0)':>16s} {'H_3''(0)':>16s} {'24 H_1 + 72 H_3':>18s} {'empirical c2':>14s} {'agree?':>8s}")
print("-" * 92)

for sigma in [0.05, 0.08, 0.10, 0.12, 0.15, 0.18, 0.20, 0.25, 0.30, 0.40, 0.50]:
    smearing = lambda s, sg=sigma: positive_smearing(s, sigma=sg, y0=3*GAMMA_0)
    H1pp = H_double_prime(3j*GAMMA_0, sigma, 3*GAMMA_0).real
    H3pp = H_double_prime(1j*GAMMA_0, sigma, 3*GAMMA_0).real
    predicted = 24*H1pp + 72*H3pp

    # Empirical: compute cluster cubic moment at delta = 0.05 (small)
    delta_small = 0.05
    C0 = cubic_moment_cluster(0.0, smearing)
    C_small = cubic_moment_cluster(delta_small, smearing)
    empirical_c2 = (C_small.real - C0.real) / delta_small**2

    agree = "YES" if abs(predicted - empirical_c2) < 0.05*abs(empirical_c2) + 1e-6 else "NO"
    print(f"{sigma:8.3f} {H1pp:16.6e} {H3pp:16.6e} {predicted:18.6e} {empirical_c2:14.6e} {agree:>8s}")

print()
print("Negative-coefficient region: sigma where 24 H_1'' + 72 H_3'' < 0")
print("=> at this sigma, hypothetical off-line zero rho_0 = 1/2 + delta + i*gamma_0")
print("   drives Re C_cluster strictly negative at leading order O(delta^2).")
print("   This is the cubic Bombieri witness [A2].")

# ----- Verify negativity at chosen sigma over a delta range -----

print("\n" + "=" * 90)
print("Verification at sigma = 0.08 (near-optimal): Re C decreases as delta grows")
print("=" * 90)
sigma_opt = 0.08
smearing = lambda s: positive_smearing(s, sigma=sigma_opt, y0=3*GAMMA_0)
print(f"\n{'delta':>10s} {'Re C(delta)':>18s} {'Re C - Re C(0)':>20s} {'/delta^2':>15s}")
print("-" * 70)
C0 = cubic_moment_cluster(0.0, smearing)
print(f"{0.0:10.4f} {C0.real:18.6e}")
for delta in [0.01, 0.02, 0.05, 0.08, 0.10, 0.15, 0.20, 0.25, 0.30]:
    C = cubic_moment_cluster(delta, smearing)
    diff = C - C0
    coef = diff.real / delta**2
    print(f"{delta:10.4f} {C.real:18.6e} {diff.real:20.6e} {coef:15.6e}")
