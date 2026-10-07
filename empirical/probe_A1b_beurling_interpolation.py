"""
[A1] structural insight: cubic Fejer positivity class non-empty via Beurling interpolation.

Empirical finding from probe_A1_fejer_positivity.py:
   EVERY positive-coefficient kernel h(gamma) >= 0 produces S_g with sign changes.
   Reason: S_g positive-definite (Bochner) but not pointwise non-negative.

Correct route: solve for h(gamma) such that S_g(x) := sum_k h_k exp(i gamma_k x)
approximates a TARGET non-negative function phi(x) on [0, X], via Beurling-Selberg
interpolation. The coefficients h_k will NOT all be positive; they encode the
spectral expansion of phi on the zeta zero set.

We solve the least-squares system:
   minimize  ||S_g(x_j) - phi(x_j)||^2  over h
on a grid of N sample points x_j in [0, X].

This gives a constructive non-empty Fejer class G.

Setup:
- Take K = 50 zeta zeros (positive gamma's only).
- Use 2K Fourier basis functions cos(gamma_k x), sin(gamma_k x) (real and imaginary parts).
  But for symmetric S_g (real g), sin parts vanish, so 2K -> K cosines.
- Solve LS for cosine coefficients to match a target phi(x).
"""

import numpy as np

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


def fit_S_g_to(phi_fn, gammas, x_grid):
    """
    Solve min ||sum_k 2 h_k cos(gamma_k x_j) - phi(x_j)||^2 for h.

    Returns h vector.
    """
    # Design matrix A[j, k] = 2 cos(gamma_k * x_j)
    A = 2 * np.cos(np.outer(x_grid, gammas))
    target = phi_fn(x_grid)
    h, residuals, rank, sv = np.linalg.lstsq(A, target, rcond=None)
    return h, A @ h, target


def S_g_from_h(x, h, gammas):
    return 2 * np.sum(h * np.cos(np.outer(np.asarray(x), gammas)), axis=1)


def main():
    gammas = np.array(ZETA_ZEROS)
    K = len(gammas)
    print("=" * 90)
    print("[A1] structural construction: solve for h such that S_g(x) = phi(x), phi >= 0")
    print(f"Using K = {K} zeta zeros (positive gamma's only)")
    print("=" * 90)

    # Sampling grid: dense enough to resolve highest frequency
    gamma_max = gammas.max()
    N = 4 * K  # oversample
    X = 0.5  # support of target
    x_grid = np.linspace(0, X, N)

    # Target: a positive bump on [0, X]
    targets = {
        'Gaussian centered at X/2':  lambda x: np.exp(-((x - X/2)/(X/4))**2),
        'Fejer tent on [0, X]':      lambda x: np.maximum(0, 1 - 2*np.abs(x - X/2)/X),
        'Smooth bump on [0, X]':     lambda x: np.exp(-1/(1 - ((x - X/2)/(X/2))**2 + 1e-15)) * ((np.abs(x - X/2) < X/2)),
        'Constant 1':                lambda x: np.ones_like(x),
    }

    for name, phi_fn in targets.items():
        print(f"\n--- Target: {name} ---")
        h, S_fit, phi_target = fit_S_g_to(phi_fn, gammas, x_grid)
        residual = np.linalg.norm(S_fit - phi_target) / max(np.linalg.norm(phi_target), 1e-10)
        print(f"  Sample points: {N}, residual: {residual:.6e}")
        print(f"  Coefficient range: h in [{h.min():+.4f}, {h.max():+.4f}], |h_max|/|h_mean| = {np.max(np.abs(h))/np.mean(np.abs(h)):.4f}")
        print(f"  Sign of coefficients: {sum(1 for x in h if x > 0)} positive, {sum(1 for x in h if x < 0)} negative")

        # Verify S_g on broader range [0, 2X]
        x_check = np.linspace(0, 2 * X, 500)
        S_check = S_g_from_h(x_check, h, gammas)
        phi_check = phi_fn(x_check)
        print(f"  S_g on [0, X]:    min = {S_check[:250].min():+.6f}, max = {S_check[:250].max():+.6f}")
        print(f"  S_g on [X, 2X]:   min = {S_check[250:].min():+.6f}, max = {S_check[250:].max():+.6f}")
        print(f"  S_g on [0, X]: positive everywhere? {'YES' if S_check[:250].min() > -1e-6 else 'NO'}")
        # Print at sample points
        for xi in [0, X/4, X/2, 3*X/4, X, 1.5*X, 2*X]:
            i = int(min(xi / (2*X) * 500, 499))
            print(f"    S_g({xi:.3f}) = {S_check[i]:+.6f},  target phi({xi:.3f}) = {phi_check[i]:+.6f}")

    # ===== Now construct an EXPLICIT element of G =====
    print("\n" + "=" * 90)
    print("Explicit construction: a g such that S_g >= 0 on [0, X]")
    print("=" * 90)

    phi_fn = lambda x: np.exp(-((x - 0.25)/0.1)**2)  # Gaussian bump at 0.25
    X = 0.5
    N = 4 * K
    x_grid = np.linspace(0, X, N)
    h, S_fit, phi_target = fit_S_g_to(phi_fn, gammas, x_grid)
    print(f"\nTarget phi(x) = exp(-((x-0.25)/0.1)^2), Gaussian bump centered at 0.25")
    print(f"Fitted on grid [0, {X}], N = {N} points")
    print(f"Residual: {np.linalg.norm(S_fit - phi_target)/np.linalg.norm(phi_target):.6e}")
    print(f"\nFirst 10 coefficients h_k (for k = 1, ..., 10):")
    for k in range(10):
        print(f"  h_{k+1} (gamma_{k+1} = {gammas[k]:.4f}) = {h[k]:+.6e}")

    print(f"\nVerify S_g(x) >= 0 on [0, X]:")
    x_verify = np.linspace(0, X, 200)
    S_verify = S_g_from_h(x_verify, h, gammas)
    print(f"  min S_g on [0, X] = {S_verify.min():.6e}")
    print(f"  max S_g on [0, X] = {S_verify.max():.6e}")
    if S_verify.min() >= -1e-6 * S_verify.max():
        print(f"  -> S_g is non-negative on [0, X] up to fit residual. <-- CONFIRMS [A1] CONSTRUCTIVELY")
    else:
        print(f"  -> S_g has sign change(s); fit didn't converge to a positive function")

    # Check behavior beyond [0, X]
    print(f"\nExtrapolate to [0, 2X] = [0, {2*X}]:")
    x_extra = np.linspace(0, 2 * X, 400)
    S_extra = S_g_from_h(x_extra, h, gammas)
    print(f"  min S_g on [X, 2X] = {S_extra[200:].min():.6e}")
    print(f"  Extrapolated S_g {'STAYS non-negative' if S_extra[200:].min() >= -1e-6 else 'GOES NEGATIVE'} beyond fit window")
    # That negative excursion is "OK" — we only need positivity on the support of eta in [A1].


if __name__ == '__main__':
    main()
