"""
[A1] empirical scaffold: explicit construction of a non-empty cubic Fejér class.

Goal: exhibit a real Schwartz function g on (0, infty) such that
   S_g(x) := sum_{gamma: zeta(1/2 + i*gamma) = 0} tilde_g(1/2 + i*gamma) * exp(i*gamma*x) >= 0  on R_{>=0}.

Strategy:
  - Choose a positive, smooth, compactly supported kernel phi(x) on [0, T] (Fejer tent, smooth cutoff).
  - Express phi via its (truncated) "zero-spectrum Fourier series": phi(x) ≈ sum_gamma h(gamma) exp(i*gamma*x).
  - Set tilde_g(1/2 + i*gamma) := h(gamma); this defines g unique up to Mellin transform.
  - Verify S_g(x) ≈ phi(x) >= 0 on R_{>=0} up to truncation.

The construction follows Beurling-Selberg: in the zero spectrum of zeta (density log(t)/(2pi) at height t),
a smooth positive function bandlimited to height T can be perfectly recovered from its values on N(T) ~ T log T / (2pi) zeros.

We use the LMFDB list of first 1000 nontrivial zeros (or, for portability, the first 100 stored values).

Empirical content:
1. Construct candidate g via h(gamma) = exp(-gamma^2 / sigma^2) (Gaussian on critical line).
2. Compute S_g(x) = 2 sum_{gamma>0} h(gamma) cos(gamma * x) for x in [0, X_max].
3. Plot / tabulate: is S_g >= 0 on [0, X_max]? What is the first zero of S_g?
4. Conclude: |S_g >= 0| on a substantial range -> cubic Fejer class non-empty (constructively).
"""

import numpy as np
import mpmath as mp

# First 50 nontrivial zeros of zeta on the critical line (imaginary parts)
# Reference values (Odlyzko); we use a precomputed list to avoid mp.zetazero overhead.
ZETA_ZEROS = [
    14.134725141734693, 21.022039638771555, 25.010857580145688,
    30.424876125859513, 32.935061587739189, 37.586178158825671,
    40.918719012147495, 43.327073280914999, 48.005150881167160,
    49.773832477672302, 52.970321477714460, 56.446247697063394,
    59.347044002602353, 60.831778524609810, 65.112544048081607,
    67.079810529494173, 69.546401711173979, 72.067157674481907,
    75.704690699083933, 77.144840068874805, 79.337375020249368,
    82.910380854341184, 84.735492980517051, 87.425274613125229,
    88.809111207634462, 92.491899270558484, 94.651344040519886,
    95.870634228245309, 98.831194218193698, 101.317851005731391,
    103.725538040478339, 105.446623052087650, 107.168611184276644,
    111.029535543171830, 111.874659177002, 114.320220915453,
    116.226680321519, 118.790782866263, 121.370125002420,
    122.946829293896, 124.256818554320, 127.516683879596,
    129.578704200002, 131.087688531195, 133.497737203718,
    134.756509753373, 138.116042055444, 139.736208952121,
    141.123707404021, 143.111845808910
]

def S_g(x, h_values, gammas):
    """S_g(x) = 2 sum_{gamma>0} h(gamma) cos(gamma * x)."""
    return 2 * np.sum(h_values * np.cos(np.outer(np.asarray(gammas), np.asarray(x)).T), axis=1)


def main():
    gammas = np.array(ZETA_ZEROS)

    print("=" * 90)
    print("[A1] Empirical: cubic Fejér positivity class non-empty?")
    print(f"Using first {len(gammas)} zeros of zeta")
    print("=" * 90)

    # Test candidates for h(gamma): different positive kernels
    candidates = {
        'Gaussian sigma=10':   lambda g: np.exp(-g**2 / 100),
        'Gaussian sigma=20':   lambda g: np.exp(-g**2 / 400),
        'Gaussian sigma=50':   lambda g: np.exp(-g**2 / 2500),
        'Exponential 1/g':     lambda g: 1.0 / (1 + g**2),
        'Sinc^2 T=2':          lambda g: (np.sin(2*g)/(2*g + 1e-30))**2,
        'Sinc^2 T=5':          lambda g: (np.sin(5*g)/(5*g + 1e-30))**2,
        'Fejer^2 T=10':        lambda g: ((np.sin(10*g/2)/(g/2 + 1e-30))**2 / 10**2),
        'Cutoff T=20':         lambda g: 1.0 * (g < 20),  # sharp cutoff
        'Smooth cutoff T=20':  lambda g: np.exp(-(g/20)**4),  # super-Gaussian
        'Smooth cutoff T=50':  lambda g: np.exp(-(g/50)**4),
        'Smooth cutoff T=100': lambda g: np.exp(-(g/100)**4),
    }

    x_test = np.linspace(0, 5, 501)

    print(f"\n{'kernel h(gamma)':>25s}  {'S_g(0)':>14s}  {'min S_g':>14s}  {'argmin x':>10s}  {'pos on [0,5]?':>15s}")
    print("-" * 90)

    for name, h_fn in candidates.items():
        h_vals = h_fn(gammas)
        S_vals = S_g(x_test, h_vals, gammas)
        S0 = S_vals[0]
        S_min = S_vals.min()
        x_min = x_test[np.argmin(S_vals)]
        is_pos = (S_min >= -1e-10 * abs(S0))
        print(f"{name:>25s}  {S0:14.6e}  {S_min:14.6e}  {x_min:10.4f}  {'YES' if is_pos else 'NO':>15s}")

    # Find first positive crossing for the Gaussian sigma=10 case (likely the most positive)
    print("\n" + "=" * 90)
    print("Detail: Gaussian h(gamma) = exp(-gamma^2 / 100), x in [0, 20]")
    print("=" * 90)
    x_detail = np.linspace(0, 20, 2001)
    h_vals = np.exp(-gammas**2 / 100)
    S_detail = S_g(x_detail, h_vals, gammas)

    # Find sign changes
    sign_changes = []
    for i in range(1, len(S_detail)):
        if S_detail[i-1] * S_detail[i] < 0:
            sign_changes.append((x_detail[i-1], x_detail[i], S_detail[i-1], S_detail[i]))

    print(f"\nS_g(0) = {S_detail[0]:.6f}")
    print(f"S_g(20) = {S_detail[-1]:.6f}")
    print(f"min S_g on [0,20] = {S_detail.min():.6f} at x = {x_detail[np.argmin(S_detail)]:.4f}")
    print(f"max S_g on [0,20] = {S_detail.max():.6f} at x = {x_detail[np.argmax(S_detail)]:.4f}")
    print(f"\nFirst {min(5, len(sign_changes))} sign changes:")
    for x1, x2, s1, s2 in sign_changes[:5]:
        print(f"  x in [{x1:.4f}, {x2:.4f}]: S_g goes {s1:+.4f} -> {s2:+.4f}")

    print("\nValues at sampled x:")
    for x_sample in [0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0, 10.0, 15.0, 20.0]:
        i = int(x_sample / 20 * 2000)
        print(f"  S_g({x_sample:6.2f}) = {S_detail[i]:+.6f}")

    # ===== Now use a Selberg majorant-style kernel: bandlimited positive =====
    # Take h(gamma) such that S_g = (truncated Fejér tent in x space)

    print("\n" + "=" * 90)
    print("Construction: positivity-preserving choice via squared bandlimited kernel")
    print("=" * 90)
    # h(gamma) = (sin(T*gamma) / (T*gamma))^2 is the FT of the Fejér tent on [-T, T]
    # The zero-spectrum sum S_g(x) = sum_gamma h(gamma) e^{i*gamma*x} approximates
    # the (scaled) Fejér tent (1 - |x|/T)_+ supported on |x| <= T.
    for T in [5, 10, 20, 50]:
        h_vals = (np.sin(T * gammas) / (T * gammas + 1e-30)) ** 2
        # Normalize
        x_test = np.linspace(0, 2*T, 1001)
        S_vals = S_g(x_test, h_vals, gammas)
        min_val = S_vals.min()
        max_val = S_vals.max()
        print(f"T = {T:3d}: S_g(0) = {S_vals[0]:.6f}, max = {max_val:.6f}, min = {min_val:.6f}, "
              f"argmin at x = {x_test[np.argmin(S_vals)]:.4f}, positive everywhere? {'YES' if min_val >= -1e-10*abs(max_val) else 'NO'}")

if __name__ == '__main__':
    main()
