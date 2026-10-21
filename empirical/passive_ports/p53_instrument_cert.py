"""Certificate K6 for Theorem 4.10 (the instrument identity), Paper 53 §4.8.

For a window W = [T1, T2] and resolution X:
    N_bal(X; W)  = Delta_W(theta)/pi + Delta_W(S_X),   S_X(t) = Im L_X(1/2 + it)/pi   (Selberg's short sum)
    N_line(W)    = zeros of the target on the line in W (sign changes)
    R_W          = N_bal - N_line,      E_W = Delta_W(S_X - S),   S(t) = arg f(1/2 + it)/pi from sigma = 4
Theorem 4.10:  R_W - E_W = 2 N_off(W)   (zeros right of the line, counted once per pair).
The readout  round(R_W / 2)  equals N_off(W) whenever |E_W| < 1.

S is computed by tracking arg f along the horizontal from sigma = 4 (no zero counting is used), so the identity
check is independent of the zero count; a missed or spurious zero on the line would show as a nonzero residual.
"""
import numpy as np
import mpmath as mp
from scipy.special import loggamma
from p53_third_law_curve import Gas, KAPPA, true_dh_online

# ---------------------------------------------------------------- zeta by Euler-Maclaurin (numpy)
B2K = [1 / 6, -1 / 30, 1 / 42, -1 / 30, 5 / 66, -691 / 2730, 7 / 6, -3617 / 510, 43867 / 798, -174611 / 330]


def zeta_em(s, N):
    s = np.asarray(s, dtype=complex)
    n = np.arange(1, N, dtype=float)
    head = np.exp(-np.outer(s, np.log(n))).sum(axis=1)
    lN = np.log(N)
    tail = np.exp((1 - s) * lN) / (s - 1) + 0.5 * np.exp(-s * lN)
    fac, poch = 1.0, s.copy()
    term_pow = np.exp(-(s + 1) * lN)  # N^{-s-1}
    for k, b in enumerate(B2K, start=1):
        fac *= (2 * k) * (2 * k - 1) if k > 1 else 2
        tail += b / fac * poch * term_pow
        poch = poch * (s + 2 * k - 1) * (s + 2 * k)
        term_pow = term_pow / N**2
    return head + tail


def theta_zeta(t):
    return np.imag(loggamma(0.25 + 0.5j * t)) - 0.5 * t * np.log(np.pi)


def theta_5(t):
    return 0.5 * t * np.log(5 / np.pi) + np.imag(loggamma(0.75 + 0.5j * t))


def track_arg(f_of_sigma, h=0.005, s_hi=4.0):
    """Continuous arg along sigma from s_hi down to 1/2, refined until no step exceeds 0.4 rad."""
    while True:
        sg = np.linspace(s_hi, 0.5, int((s_hi - 0.5) / h) + 1)
        v = f_of_sigma(sg)
        jumps = np.abs(np.angle(v[1:] / v[:-1]))
        if jumps.max() < 0.4 or h < 1e-5:
            return np.angle(v[0]) + np.sum(np.angle(v[1:] / v[:-1]))
        h /= 4


def S_zeta(T):
    N = int(T) + 20
    return track_arg(lambda sg: zeta_em(sg + 1j * T, N)) / np.pi


def Z_rs(t):
    """Riemann-Siegel Z with the first correction term (sign changes only)."""
    a = np.sqrt(t / (2 * np.pi))
    m = np.floor(a).astype(int)
    th = theta_zeta(t)
    out = np.zeros_like(t)
    for n in range(1, int(m.max()) + 1):
        mask = m >= n
        out[mask] += 2 * np.cos(th[mask] - t[mask] * np.log(n)) / np.sqrt(n)
    p = a - m
    c0 = np.cos(2 * np.pi * (p * p - p - 1 / 16)) / np.cos(2 * np.pi * p)
    return out + (-1.0) ** (m - 1) * (t / (2 * np.pi)) ** -0.25 * c0


def S_X_of(X, t):
    return np.imag(Gas(X)(0.5 + 1j * np.atleast_1d(t))) / np.pi


# ---------------------------------------------------------------- DH
DH_A = [1, KAPPA, -KAPPA, -1]


def f_dh(s):
    return complex(mp.power(5, -s) * sum(DH_A[j] * mp.zeta(s, (j + 1) / 5.0) for j in range(4)))


def S_dh(T):
    mp.mp.dps = 15
    return track_arg(lambda sg: np.array([f_dh(mp.mpc(x, T)) for x in sg])) / np.pi


def D5_arg(T):
    La = Gas(5, lambda p: {1: 1, 2: 1j, 3: -1j, 4: -1, 0: 0}[p % 5])
    Lb = Gas(5, lambda p: np.conj({1: 1, 2: 1j, 3: -1j, 4: -1, 0: 0}[p % 5]))
    c1, c2 = (1 - 1j * KAPPA) / 2, (1 + 1j * KAPPA) / 2
    return track_arg(lambda sg: c1 * np.exp(La(sg + 1j * T)) + c2 * np.exp(Lb(sg + 1j * T))) / np.pi


if __name__ == "__main__":
    mp.mp.dps = 20
    for s in (0.5 + 100j, 0.7 + 1000j, 2 + 5000j, 0.5 + 5000.3j):
        ref = complex(mp.zeta(s))
        got = zeta_em(np.array([s]), int(s.imag) + 20)[0]
        print(f"zeta_em check at {s}: |rel err| = {abs(got - ref) / abs(ref):.1e}")

    # zeta: 250 contiguous windows of width 20 on [100, 5100]
    T = 100.0 + 20.0 * np.arange(251)
    S = np.array([S_zeta(x) for x in T])
    th = theta_zeta(T)
    tg = np.arange(100.0, 5100.0, 0.004)
    z = Z_rs(tg)
    sc = tg[np.nonzero(np.sign(z[:-1]) * np.sign(z[1:]) < 0)[0]]
    nline = np.histogram(sc, bins=T)[0]
    backlund = np.diff(th) / np.pi + np.diff(S) - nline          # = 2 N_off by Theorem 4.10
    print(f"\nzeta, 250 windows on [100, 5100]: {nline.sum()} zeros on the line;"
          f" max |Delta theta/pi + Delta S - N_line| = {np.abs(backlund).max():.2e}  (=> N_off = 0 in every window)")
    print("readout error E_W = Delta_W(S_X - S); the instrument misreads iff |E_W| >= 1")
    rules = {"X = 13": lambda t: 13, "X = 1000": lambda t: 1000, "X = t^(1/2)": lambda t: int(t ** 0.5),
             "X = t": lambda t: int(t)}
    for name, rule in rules.items():
        # one resolution per window, chosen at the window's start
        E = np.array([np.diff(S_X_of(max(2, rule(T[j])), T[j:j + 2]))[0] - (S[j + 1] - S[j]) for j in range(250)])
        R = np.array([np.diff(th[j:j + 2])[0] / np.pi + np.diff(S_X_of(max(2, rule(T[j])), T[j:j + 2]))[0] - nline[j]
                      for j in range(250)])
        mis = np.sum(np.round(R / 2) != 0)
        print(f"  {name:12s}: residual max|R - E - 0| = {np.abs(R - E).max():.1e} | max|E| = {np.abs(E).max():.3f}"
              f" | rms E = {np.sqrt(np.mean(E**2)):.3f} | misreads {mis}/250")

    # DH: five windows, passive port X = 5, known off-line zeros 0, 0, 1, 1, 2
    print("\nDH, passive port X = 5 (theta_5, S_DH tracked from sigma = 4, S_X = arg D_5 / pi tracked the same way)")
    for (a, b), noff in zip([(20, 40), (50, 70), (80, 100), (110, 130), (160, 180)], [0, 0, 1, 1, 2]):
        nl = len(true_dh_online(a, b))
        dth = (theta_5(np.array([b]))[0] - theta_5(np.array([a]))[0]) / np.pi
        dS, dSX = S_dh(b) - S_dh(a), D5_arg(b) - D5_arg(a)
        R, E = dth + dSX - nl, dSX - dS
        print(f"  W=[{a},{b}]: N_line {nl:2d} | R = {R:+.4f} | E = {E:+.4f} | R - E = {R - E:+.4f}"
              f" (2 N_off = {2 * noff}) | readout round(R/2) = {int(np.round(R / 2))}")
