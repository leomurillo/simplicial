"""Finite-resolution zeta port: balance is free, passivity is the test (matched pair zeta / L(chi) / DH).

Truncate the multiplicative crystal N = (+)_p N to its X-smooth part and keep the free energy of the
truncated primon gas:  log P_X(s; c) = sum_{p^k <= X} c(p)^k / (k p^{ks}).  P_X is entire and zero-free.
The balanced (lossless) port at resolution X is

    F_X(s) = A_X(s) + (archimedean factor)(s) * A_X(1 - s),

with the functional equation built in, so |reflection| = 1 on Re s = 1/2 (balance).  Zeros of F_X are the
points where the reflection S_X = (arch)(s) A_X(1-s)/A_X(s) equals -1.

  zeta  : A = P_X(s; 1),                         arch = chi_zeta(s)
  L(chi): A = P_X(s; chi), mirror P_X(1-s; chibar), arch = W chi_5(s)      (chi mod 5, chi(2) = i)
  DH    : A = c1 P_X(s; chi) + c2 P_X(s; chibar), arch = chi_5(s)          (interference of two free gases)

Counts on-line zeros (sign changes of the real Z-function) and off-line zeros in 1/2 < sigma < 1 (grid
minima of |F| refined by Newton, cross-checked by the argument principle), per height window.
"""
import numpy as np
from scipy.special import loggamma

SQ5 = np.sqrt(5.0)
KAPPA = (np.sqrt(10 - 2 * SQ5) - 2) / (SQ5 - 1)
C1, C2 = (1 - 1j * KAPPA) / 2, (1 + 1j * KAPPA) / 2
CHI = {0: 0, 1: 1, 2: 1j, 3: -1j, 4: -1}
TAU = sum(CHI[a] * np.exp(2j * np.pi * a / 5) for a in range(1, 5))
W = TAU / (1j * SQ5)


def prime_powers(X):
    ps = [p for p in range(2, X + 1) if all(p % q for q in range(2, int(p**0.5) + 1))]
    out = []
    for p in ps:
        k, pk = 1, p
        while pk <= X:
            out.append((pk, p, k)); k += 1; pk *= p
    return out


def logP(s, pp, char):
    acc = np.zeros_like(s, dtype=complex)
    for n, p, k in pp:
        c = 1.0 if char is None else char(p) ** k
        if c != 0:
            acc += c / k * np.exp(-s * np.log(n))
    return acc


chi_mod5 = lambda p: CHI[p % 5]
chibar_mod5 = lambda p: np.conj(CHI[p % 5])
chi_zeta = lambda s: np.pi ** (s - 0.5) * np.exp(loggamma((1 - s) / 2) - loggamma(s / 2))
chi_5 = lambda s: (5 / np.pi) ** (0.5 - s) * np.exp(loggamma(1 - s / 2) - loggamma((1 + s) / 2))


def make(name, X):
    pp = prime_powers(X)
    if name == "zeta":
        A = lambda s: np.exp(logP(s, pp, None))
        Am = A
        arch = chi_zeta
    elif name == "L(chi)":
        A = lambda s: np.exp(logP(s, pp, chi_mod5))
        Am = lambda s: np.exp(logP(s, pp, chibar_mod5))
        arch = lambda s: W * chi_5(s)
    elif name == "DH":
        A = lambda s: C1 * np.exp(logP(s, pp, chi_mod5)) + C2 * np.exp(logP(s, pp, chibar_mod5))
        Am = A
        arch = chi_5
    F = lambda s: A(s) + arch(s) * Am(1 - s)
    return F, A, arch


def online_zeros(F, arch, t):
    s = 0.5 + 1j * t
    beta = np.unwrap(np.angle(arch(s)))
    z = np.exp(-0.5j * beta) * F(s)
    assert np.max(np.abs(z.imag)) < 1e-8 * (1 + np.max(np.abs(z.real))), "Z not real on the line"
    sc = np.nonzero(np.sign(z.real[:-1]) * np.sign(z.real[1:]) < 0)[0]
    return t[sc] - z.real[sc] * (t[sc + 1] - t[sc]) / (z.real[sc + 1] - z.real[sc])


def strip_zeros(F, sig_lo, sig_hi, t_lo, t_hi, dsig=0.01, dt=0.02):
    sg = np.arange(sig_lo, sig_hi + dsig / 2, dsig)
    tg = np.arange(t_lo, t_hi + dt / 2, dt)
    S = sg[:, None] + 1j * tg[None, :]
    L = np.log(np.abs(F(S)) + 1e-300)
    core = L[1:-1, 1:-1]
    nb = np.stack([L[1 + a:L.shape[0] - 1 + a, 1 + b:L.shape[1] - 1 + b]
                   for a in (-1, 0, 1) for b in (-1, 0, 1) if (a, b) != (0, 0)])
    cand = S[1:-1, 1:-1][(core < nb.min(axis=0))]
    found = []
    for z in cand:
        for _ in range(60):
            h = 1e-6
            f = F(np.array([z]))[0]
            d = (F(np.array([z + h]))[0] - F(np.array([z - h]))[0]) / (2 * h)
            if d == 0:
                break
            step = f / d
            z = z - step
            if abs(step) < 1e-13:
                break
        if abs(step) < 1e-10 and sig_lo - 1e-3 < z.real < sig_hi + 1e-3 and t_lo <= z.imag <= t_hi:
            if all(abs(z - w) > 1e-6 for w in found):
                found.append(z)
    return np.array(found)


def winding(F, s0, s1, t0, t1, h=0.005):
    def edge(a, b):
        n = max(2, int(abs(b - a) / h))
        return a + (b - a) * np.linspace(0, 1, n, endpoint=False)
    path = np.concatenate([edge(s0 + 1j * t0, s1 + 1j * t0), edge(s1 + 1j * t0, s1 + 1j * t1),
                           edge(s1 + 1j * t1, s0 + 1j * t1), edge(s0 + 1j * t1, s0 + 1j * t0)])
    path = np.append(path, path[0])
    for _ in range(12):  # adaptive refinement where the phase jumps
        v = F(path)
        dphi = np.angle(v[1:] / v[:-1])
        bad = np.nonzero(np.abs(dphi) > 0.4)[0]
        if len(bad) == 0:
            break
        mids = (path[bad] + path[bad + 1]) / 2
        path = np.insert(path, bad + 1, mids)
    v = F(path)
    return np.sum(np.angle(v[1:] / v[:-1])) / (2 * np.pi)


if __name__ == "__main__":
    ETA = 0.002
    # K4(a) the DH functional equation, exactly where the construction needs it
    print(f"K4(a) W(chi) = {W:.12f};  c2/c1 = {C2 / C1:.12f};  |diff| = {abs(W - C2 / C1):.1e}")

    # K4(b) matched pair at one resolution, t <= 1000: on-line counts and off-line counts per window
    print("\nK4(b) resolution X = 13, 1 <= t <= 1000 (off-line = zeros in 1/2 < sigma < 1, argument principle)")
    for name in ("zeta", "L(chi)", "DH"):
        F, A, arch = make(name, 13)
        on = online_zeros(F, arch, np.arange(1.0, 1000.0, 0.001))
        offw = [round(winding(F, 0.5 + ETA, 1.0, max(a, 1.0) + 1e-3, a + 200 - 1e-3)) for a in range(0, 1000, 200)]
        nA = len([z for z in strip_zeros(A, 0.5 + ETA, 1.0, 1.0, 300.0) if z.real > 0.5001])
        print(f"  {name:7s} on-line {len(on):4d} | off-line per 200-window {offw} (total {sum(offw)}) "
              f"| zeros of the amplitude A_X in (1/2,1), t<=300: {nA}")

    # K4(c) resolution sweep, t <= 300: where the extra zeros of high-resolution ports sit
    print("\nK4(c) resolution sweep, 1 <= t <= 300; sigma-bins of off-line zeros [.5,.6,.7,.8,.9,1)")
    for X in (5, 13, 50, 200):
        for name in ("zeta", "L(chi)", "DH"):
            F, A, arch = make(name, X)
            on = online_zeros(F, arch, np.arange(1.0, 300.0, 0.001))
            off = strip_zeros(F, 0.5 + ETA, 1.0, 1.0, 300.0)
            off = off[off.real > 0.5001]
            wn = winding(F, 0.5 + ETA, 1.0, 1.0 + 1e-3, 300.0 - 1e-3)
            bins = np.histogram(off.real, bins=[0.5, 0.6, 0.7, 0.8, 0.9, 1.0])[0].tolist()
            print(f"  X={X:3d} {name:7s} on-line {len(on):4d} | off-line {round(wn):4d} (located {len(off)}) {bins}")

    # K4(d) precursors: on-line zeros of the zeta port against the zeros of zeta, 10 <= t <= 100
    print("\nK4(d) zeta-port on-line zeros vs zeta zeros, 10 <= t <= 100")
    g = np.sort(np.load(r"C:\Projects\simplicial\empirical\zeros_cache.npy").real)
    g = g[g < 100]
    for X in (2, 5, 13, 50, 200, 1000, 5000):
        F, A, arch = make("zeta", X)
        on = online_zeros(F, arch, np.arange(10.0, 101.0, 0.0005))
        msg = f"count {len(on)} vs {len(g)}"
        if len(on) == len(g):
            e = np.abs(on - g)
            msg += f" | mean |err| {e.mean():.4f}  max |err| {e.max():.4f}"
        print(f"  X={X:5d}: {msg}")
