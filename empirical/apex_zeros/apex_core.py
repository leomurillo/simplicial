"""
Core routines for the apex zero-variety probe suite (T0 6.6 / T7 7.4).

The apex generator, for a centered log-ledger y in C^N and character index c:

    M(beta, c) = (1/N) sum_s exp(beta * y_s) * conj(chi_c(s)),
    chi_c(s) = exp(2 pi i c s / N),  so conj(chi_c(s)) = exp(-2 pi i c s / N).

This is a finite exponential sum in beta -> entire of exponential type. We
locate its zeros in a complex rectangle by:
  (1) the argument principle (rigorous count = completeness certificate), and
  (2) grid-seeded Newton iteration (location),
then assert the two agree.

Strip bound (provable): for a sum of N unit-modulus-coefficient exponentials
with real frequencies sorted y_(1) < ... < y_(N), every zero has

    -log(N-1)/(y_(2) - y_(1))  <=  Re beta  <=  log(N-1)/(y_(N) - y_(N-1)).

Note this half-width VANISHES at N=2 (log 1 = 0): the cosh case is the unique
exactly-on-the-imaginary-axis case (Theorem 4, the no-go mechanism).

No torch, no network: deterministic numpy/mpmath gate.
"""

import numpy as np
import mpmath as mp

mp.mp.dps = 30  # ~30 significant digits


# ----------------------------------------------------------------------------
# Ledgers
# ----------------------------------------------------------------------------
def centered_log_ledger(x):
    """y_s = log x_s - mean_j log x_j, for a positive real ledger x. Sum y = 0."""
    lx = [mp.log(mp.mpf(xi)) for xi in x]
    m = sum(lx) / len(lx)
    return [li - m for li in lx]


def centered_complex_ledger(z):
    """Complex centered log-ledger y_s = log z_s - mean_j log z_j (principal branch)."""
    lz = [mp.log(mp.mpc(zi)) for zi in z]
    m = sum(lz) / len(lz)
    return [li - m for li in lz]


def spread(y):
    """Delta_y = max Re y - min Re y  (the tropical width / |dom K*_y|)."""
    rs = [mp.re(v) for v in y]
    return max(rs) - min(rs)


def strip_bound(y, N):
    """(R_minus, R_plus): provable real-part envelope of the zeros (real ledger)."""
    rs = sorted(mp.re(v) for v in y)
    if N < 3:
        return mp.mpf(0), mp.mpf(0)
    gap_top = rs[-1] - rs[-2]
    gap_bot = rs[1] - rs[0]
    lg = mp.log(N - 1)
    return lg / gap_bot, lg / gap_top


# ----------------------------------------------------------------------------
# The generator and its derivative
# ----------------------------------------------------------------------------
def M(beta, c, y):
    N = len(y)
    beta = mp.mpc(beta)
    acc = mp.mpc(0)
    for s in range(N):
        acc += mp.e ** (beta * y[s]) * mp.e ** (-2j * mp.pi * c * s / N)
    return acc / N


def Mprime(beta, c, y):
    N = len(y)
    beta = mp.mpc(beta)
    acc = mp.mpc(0)
    for s in range(N):
        acc += y[s] * mp.e ** (beta * y[s]) * mp.e ** (-2j * mp.pi * c * s / N)
    return acc / N


# ----------------------------------------------------------------------------
# Zero finding
# ----------------------------------------------------------------------------
# ---- fast numpy evaluation (counting only; needs ~2 digits to round) -------
def _np_y(y):
    return np.array([complex(mp.re(v), mp.im(v)) for v in y], dtype=np.complex128)


def _np_coeff(c, N):
    s = np.arange(N)
    return np.exp(-2j * np.pi * c * s / N)


def M_np(B, c, y_np):
    """Vectorised M over complex128 array B. y_np: complex128 frequencies."""
    N = len(y_np)
    coeff = _np_coeff(c, N)
    E = np.exp(np.outer(B, y_np))            # (n, N)
    return (E * coeff).sum(axis=1) / N


def Mp_np(B, c, y_np):
    N = len(y_np)
    coeff = _np_coeff(c, N) * y_np
    E = np.exp(np.outer(B, y_np))
    return (E * coeff).sum(axis=1) / N


_GL_DEG = 48
_GL_X, _GL_W = np.polynomial.legendre.leggauss(_GL_DEG)
_SEG_MAX = 4.0           # composite-GL panel length (keeps accuracy T-independent)


def _edge_integral(c, y_np, a, b):
    """Composite Gauss-Legendre integral of M'/M along the segment a->b."""
    L = abs(b - a)
    npan = max(1, int(np.ceil(L / _SEG_MAX)))
    # panel midpoints/halfwidths along the segment, then all nodes at once
    edges = np.linspace(0.0, 1.0, npan + 1)
    mids = (edges[:-1] + edges[1:]) / 2.0
    half = (edges[1] - edges[0]) / 2.0
    # parametrize a->b by t in [0,1]; node t-values:
    tnodes = (mids[:, None] + half * _GL_X[None, :]).ravel()
    wts = np.tile(_GL_W * half, npan)
    nodes = a + (b - a) * tnodes
    g = Mp_np(nodes, c, y_np) / M_np(nodes, c, y_np)
    return (b - a) * np.sum(wts * g)


def count_zeros_rect_fast(c, y, re_lo, re_hi, im_lo, im_hi):
    """Fast argument-principle count (float128-free, Gauss-Legendre per edge)."""
    y_np = _np_y(y)
    re_lo, re_hi = float(re_lo), float(re_hi)
    im_lo, im_hi = float(im_lo), float(im_hi)
    c0 = complex(re_lo, im_lo); c1 = complex(re_hi, im_lo)
    c2 = complex(re_hi, im_hi); c3 = complex(re_lo, im_hi)
    total = (_edge_integral(c, y_np, c0, c1) + _edge_integral(c, y_np, c1, c2)
             + _edge_integral(c, y_np, c2, c3) + _edge_integral(c, y_np, c3, c0))
    return total / (2j * np.pi)


def count_zeros_rect(c, y, re_lo, re_hi, im_lo, im_hi):
    """Argument-principle count of zeros strictly inside the rectangle (CCW)."""
    def g(b):
        return Mprime(b, c, y) / M(b, c, y)

    re_lo, re_hi = mp.mpf(re_lo), mp.mpf(re_hi)
    im_lo, im_hi = mp.mpf(im_lo), mp.mpf(im_hi)
    total = mp.mpc(0)
    total += mp.quad(lambda t: g(mp.mpc(t, im_lo)), [re_lo, re_hi])         # bottom L->R
    total += mp.quad(lambda t: g(mp.mpc(re_hi, t)) * 1j, [im_lo, im_hi])    # right  B->T
    total += mp.quad(lambda t: g(mp.mpc(t, im_hi)), [re_hi, re_lo])         # top    R->L
    total += mp.quad(lambda t: g(mp.mpc(re_lo, t)) * 1j, [im_hi, im_lo])    # left   T->B
    return total / (2j * mp.pi)


def _newton(seed, c, y, iters=80, tol=mp.mpf(10) ** (-26)):
    b = mp.mpc(seed)
    for _ in range(iters):
        d = Mprime(b, c, y)
        if abs(d) < mp.mpf(10) ** (-40):
            break
        step = M(b, c, y) / d
        b = b - step
        if abs(step) < tol:
            break
    return b


def find_zeros_rect(c, y, re_lo, re_hi, im_lo, im_hi,
                    im_seeds_per_period=4, re_seeds=7, dedupe=mp.mpf(10) ** (-6),
                    resid=mp.mpf(10) ** (-18)):
    """Grid-seeded Newton; return zeros (mpc) found strictly inside the rectangle."""
    Dy = spread(y)
    period = 2 * mp.pi / Dy if Dy > 0 else (im_hi - im_lo)
    n_im = max(4, int(mp.ceil((im_hi - im_lo) / period * im_seeds_per_period)))
    found = []
    for ii in range(n_im + 1):
        im0 = im_lo + (im_hi - im_lo) * ii / n_im
        for ri in range(re_seeds):
            re0 = re_lo + (re_hi - re_lo) * ri / (re_seeds - 1)
            b = _newton(mp.mpc(re0, im0), c, y)
            if abs(M(b, c, y)) > resid:
                continue
            if not (re_lo <= mp.re(b) <= re_hi and im_lo <= mp.im(b) <= im_hi):
                continue
            if any(abs(b - f) < dedupe for f in found):
                continue
            found.append(b)
    found.sort(key=lambda b: (float(mp.im(b)), float(mp.re(b))))
    return found
