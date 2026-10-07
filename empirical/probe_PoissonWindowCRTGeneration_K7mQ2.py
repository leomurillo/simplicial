"""Probe finite CRT/Fejer generation of Poisson-Gaussian windows.

This is a harmonic-analysis probe only.  It shows that primorial-size Fourier
blocks can approximate local K-even Poisson-window detectors on a fixed height
interval.  It does not test RH and does not test the arithmetic divisor
weights.
"""

import numpy as np


def primorials():
    return [6, 30, 210, 2310, 30030]


def poisson_gaussian_window(x, x0=14.134725141734693, y=0.55, sigma=2.0):
    def one(center):
        return (y / ((x - center) ** 2 + y**2)) * np.exp(-0.5 * ((x - center) / sigma) ** 2)

    return one(x0) + one(-x0)


def fejer_reconstruct(samples, keep_modes):
    coeffs = np.fft.fft(samples)
    n = len(samples)
    modes = np.fft.fftfreq(n) * n
    weights = np.zeros(n)
    mask = np.abs(modes) <= keep_modes
    weights[mask] = 1.0 - np.abs(modes[mask]) / (keep_modes + 1.0)
    return np.fft.ifft(coeffs * weights).real


def main():
    t_max = 80.0
    n_grid = 16384
    xs = np.linspace(-t_max, t_max, n_grid, endpoint=False)
    target = poisson_gaussian_window(xs)
    target = target / target.max()

    print("CRT/Fejer approximation of a K-even Poisson-Gaussian detector")
    print(f"interval=[{-t_max:.1f},{t_max:.1f}], grid={n_grid}, target max normalized to 1")
    print()
    print("P_n, keep_modes, rel_L2_error, Linf_error, min_reconstruction")

    for p in primorials():
        keep = min((p - 1) // 2, n_grid // 2 - 1)
        recon = fejer_reconstruct(target, keep)
        rel_l2 = np.linalg.norm(recon - target) / np.linalg.norm(target)
        linf = np.max(np.abs(recon - target))
        print(f"{p:5d} {keep:10d} {rel_l2: .12e} {linf: .12e} {recon.min(): .12e}")

    # A non-primorial mode count with the same size as 210 is included only as
    # a sanity check that the phenomenon is Fourier resolution, while the
    # primorial rows supply the arithmetic carrier for that resolution.
    for keep in [20, 50, 100, 200, 500, 1000]:
        recon = fejer_reconstruct(target, keep)
        rel_l2 = np.linalg.norm(recon - target) / np.linalg.norm(target)
        linf = np.max(np.abs(recon - target))
        print(f"modes {keep:4d} {rel_l2: .12e} {linf: .12e} {recon.min(): .12e}")


if __name__ == "__main__":
    main()
