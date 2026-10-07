"""Probe the convolution-square form of Poisson-window recovery.

The script works on finite cyclic grids, standing in for primorial CRT rows.
Given a nonnegative K-even spectral window phi, it forms a square root in the
dual variable and takes a finite inverse FFT.  The cyclic autocorrelation then
has spectral transform exactly phi.
"""

import numpy as np


def fake_m(z, gamma=14.134725141734693, beta=2.0):
    return -(
        2 * (z - gamma) / ((z - gamma) ** 2 + beta**2)
        + 2 * (z + gamma) / ((z + gamma) ** 2 + beta**2)
    )


def boundary_m(z, gamma=14.134725141734693):
    return -(1 / (z - gamma) + 1 / (z + gamma))


def spectral_window(x, gamma=14.134725141734693, sigma=0.55):
    return np.exp(-0.5 * ((x - gamma) / sigma) ** 2) + np.exp(
        -0.5 * ((x + gamma) / sigma) ** 2
    )


def convolution_square_from_spectral_phi(phi):
    """Return f and F=f*f^* with fft(F)=phi under numpy conventions."""

    sqrt_phi = np.sqrt(np.maximum(phi, 0.0))
    f = np.fft.ifft(sqrt_phi)
    F = np.fft.ifft(np.abs(np.fft.fft(f)) ** 2)
    return f, F


def window_integral(xs, phi, mfun, y):
    vals = np.array([mfun(complex(float(x), y)).imag for x in xs])
    return np.trapezoid(phi * vals, xs), np.trapezoid(phi, xs)


def run_row(n, t_max=80.0):
    xs = np.linspace(-t_max, t_max, n, endpoint=False)
    phi = spectral_window(xs)
    f, F = convolution_square_from_spectral_phi(phi)
    recovered_phi = np.fft.fft(F).real

    spectral_error = np.max(np.abs(recovered_phi - phi))
    imag_error = np.max(np.abs(F.imag))
    k_error = np.max(np.abs(phi - phi[::-1]))

    fake_num, mass = window_integral(xs, phi, fake_m, y=1.55)
    boundary_num, _ = window_integral(xs, phi, boundary_m, y=1.55)

    return {
        "N": n,
        "dx": 2 * t_max / n,
        "spectral_error": spectral_error,
        "imag_error": imag_error,
        "k_error": k_error,
        "fake_avg": fake_num / mass,
        "boundary_avg": boundary_num / mass,
        "f_l2": float(np.linalg.norm(f)),
        "F_l1": float(np.sum(np.abs(F.real))),
    }


def main():
    print("Convolution-square Poisson recovery probe")
    print("Rows are primorial-like CRT grid sizes.")
    print()
    print(
        "N, dx, max|fft(F)-phi|, max|Im F|, fake window avg, boundary window avg, ||f||2"
    )
    for n in [210, 2310, 30030]:
        row = run_row(n)
        print(
            f"{row['N']:6d} {row['dx']: .6e} {row['spectral_error']: .3e} "
            f"{row['imag_error']: .3e} {row['fake_avg']: .12e} "
            f"{row['boundary_avg']: .12e} {row['f_l2']: .12e}"
        )


if __name__ == "__main__":
    main()
