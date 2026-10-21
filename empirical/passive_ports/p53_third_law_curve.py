"""The third-law curve of the finite zeta port (Paper 53 §4.7).

For a height window W = [t0, t0 + 20] and a resolution X, the finite port of §4.6 is
    F_X(s) = A_X(s) + G(s) A_X^#(1 - s).
Measured per (W, X):
    off(X)  = zeros of F_X in 1/2 < sigma < 1, t in W   (argument principle, adaptive phase steps < 0.4)
    on(X)   = zeros of F_X on the line in W              (sign changes of the real Z-function)
    err(X)  = mean |gamma_port - gamma_true| / (mean spacing), when on(X) equals the true count
The curve: X_pass(W) = largest X before the first resolution with off(X) > 0, and err at X_pass.

Ports:
    zeta   : A = exp(L_X)                    (plain truncated free energy)
    zeta_c : A = exp(L_X + E_1((s-1) log X)) (Hagedorn tail carried along, Prop 4.9)
    DH     : A = c1 exp(L_X(chi)) + c2 exp(L_X(chibar)), G = chi_5   (no pole: nothing to compensate)
"""
import numpy as np
import mpmath as mp
from scipy.special import loggamma, exp1

SQ5 = np.sqrt(5.0)
KAPPA = (np.sqrt(10 - 2 * SQ5) - 2) / (SQ5 - 1)
C1, C2 = (1 - 1j * KAPPA) / 2, (1 + 1j * KAPPA) / 2
CHI = {0: 0, 1: 1, 2: 1j, 3: -1j, 4: -1}


def prime_powers(X):
    sieve = np.ones(X + 1, bool); sieve[:2] = False
    for i in range(2, int(X**0.5) + 1):
        if sieve[i]:
            sieve[i * i::i] = False
    out = []
    for p in np.nonzero(sieve)[0]:
        k, pk = 1, int(p)
        while pk <= X:
            out.append((pk, int(p), k)); k += 1; pk *= int(p)
    return out


class Gas:
    """Truncated free energy L_X(s; c) = sum_{p^k <= X} c(p)^k / (k p^{ks}), evaluated in chunks."""
    def __init__(self, X, char=None):
        pp = prime_powers(X)
        self.logn = np.array([np.log(n) for n, p, k in pp])
        self.w = np.array([(1.0 if char is None else char(p) ** k) / k for n, p, k in pp], dtype=complex)
        keep = self.w != 0
        self.logn, self.w = self.logn[keep], self.w[keep]

    def __call__(self, s):
        s = np.asarray(s, dtype=complex)
        flat, out = s.ravel(), np.empty(s.size, dtype=complex)
        for i in range(0, flat.size, 2048):
            blk = flat[i:i + 2048]
            out[i:i + 2048] = np.exp(-np.outer(blk, self.logn)) @ self.w
        return out.reshape(s.shape)


chi_zeta = lambda s: np.pi ** (s - 0.5) * np.exp(loggamma((1 - s) / 2) - loggamma(s / 2))
chi_5 = lambda s: (5 / np.pi) ** (0.5 - s) * np.exp(loggamma(1 - s / 2) - loggamma((1 + s) / 2))


def make(name, X):
    if name in ("zeta", "zeta_c"):
        L = Gas(X)
        lx = np.log(X)
        if name == "zeta":
            A = lambda s: np.exp(L(s))
        else:
            A = lambda s: np.exp(L(s) + exp1((np.asarray(s, complex) - 1) * lx))
        return (lambda s: A(s) + chi_zeta(s) * A(1 - np.asarray(s, complex))), chi_zeta
    if name == "DH":
        La, Lb = Gas(X, lambda p: CHI[p % 5]), Gas(X, lambda p: np.conj(CHI[p % 5]))
        D = lambda s: C1 * np.exp(La(s)) + C2 * np.exp(Lb(s))
        return (lambda s: D(s) + chi_5(s) * D(1 - np.asarray(s, complex))), chi_5
    raise ValueError(name)


def zero_crossings(t, z):
    sc = np.nonzero(np.sign(z[:-1]) * np.sign(z[1:]) < 0)[0]
    return t[sc] - z[sc] * (t[sc + 1] - t[sc]) / (z[sc + 1] - z[sc])


def online(F, arch, t):
    s = 0.5 + 1j * t
    beta = np.unwrap(np.angle(arch(s)))
    z = np.exp(-0.5j * beta) * F(s)
    return zero_crossings(t, z.real)


def winding(F, s0, s1, t0, t1, h=0.005):
    def edge(a, b):
        n = max(2, int(abs(b - a) / h))
        return a + (b - a) * np.linspace(0, 1, n, endpoint=False)
    path = np.concatenate([edge(s0 + 1j * t0, s1 + 1j * t0), edge(s1 + 1j * t0, s1 + 1j * t1),
                           edge(s1 + 1j * t1, s0 + 1j * t1), edge(s0 + 1j * t1, s0 + 1j * t0)])
    path = np.append(path, path[0])
    v = F(path)
    for _ in range(14):
        bad = np.nonzero(np.abs(np.angle(v[1:] / v[:-1])) > 0.4)[0]
        if len(bad) == 0:
            break
        mids = (path[bad] + path[bad + 1]) / 2
        path = np.insert(path, bad + 1, mids)
        v = np.insert(v, bad + 1, F(mids))
    return np.sum(np.angle(v[1:] / v[:-1])) / (2 * np.pi)


def true_zeta_zeros(t0, t1):
    mp.mp.dps = 20
    n = max(1, int(mp.siegeltheta(t0) / mp.pi) - 3)
    out = []
    while True:
        g = float(mp.zetazero(n).imag)
        if g > t1:
            break
        if g >= t0:
            out.append(g)
        n += 1
    return np.array(out)


def true_dh_online(t0, t1, dt=0.01):
    mp.mp.dps = 15
    a = [1, KAPPA, -KAPPA, -1]
    t = np.arange(t0, t1, dt)
    f = np.array([complex(mp.power(5, -(0.5 + 1j * x)) *
                          sum(a[j] * mp.zeta(0.5 + 1j * x, (j + 1) / 5.0) for j in range(4))) for x in t])
    beta = np.unwrap(np.angle(chi_5(0.5 + 1j * t)))
    return zero_crossings(t, (np.exp(-0.5j * beta) * f).real)


XGRID = [2, 3, 5, 7, 11, 13, 17, 23, 31, 41, 53, 71, 97, 127, 167, 223, 293, 389, 509, 673, 887,
         1171, 1543, 2039, 2689, 3547, 4679, 6173, 8147]
ETA = 0.002


SIG_BULK = 0.75


def scan(name, t0, truth, t1=None):
    """Rows (X, count difference in the core, bulk off-line, edge off-line, err in mean spacings).
    err: each true zero in W matched to its nearest port zero (port zeros searched in W widened by 2)."""
    t1 = t0 + 20.0 if t1 is None else t1
    tgrid = np.arange(t0 - 2.0, t1 + 2.0, 0.002)
    spacing = 2 * np.pi / np.log((5 if name == "DH" else 1) * max(t0, 7.0) / (2 * np.pi))
    core = lambda z: z[(z >= t0 + 0.5) & (z <= t1 - 0.5)]
    rows = []
    for X in XGRID:
        F, arch = make(name, X)
        on = online(F, arch, tgrid)
        dcount = len(core(on)) - len(core(truth))
        bulk = round(winding(F, 0.5 + ETA, SIG_BULK, t0, t1))
        edge = round(winding(F, SIG_BULK, 1.0, t0, t1))
        idx = np.array([np.argmin(np.abs(on - g)) for g in truth])
        err = np.mean(np.abs(on[idx] - truth)) / spacing if len(set(idx)) == len(idx) else None
        rows.append((X, dcount, bulk, edge, err))
    return rows


def summarize(name, t0, truth, rows):
    fmt = lambda e: "--" if e is None else f"{e:.4f}"
    passive = [r for r in rows if r[2] == 0 and r[3] == 0]
    bulk_passive = [r for r in rows if r[2] == 0]
    first_bad = next((i for i, r in enumerate(rows) if r[2] + r[3] > 0), len(rows))
    xp = passive[-1] if passive else None
    xb = bulk_passive[-1] if bulk_passive else None
    line = (f"{name:6s} W=[{t0:5.0f},{t0 + 20:5.0f}] true {len(truth):3d} | first active X "
            f"{rows[first_bad][0] if first_bad < len(rows) else '>8147':>5} | X_pass {xp[0] if xp else '--':>5} "
            f"err {fmt(xp[4]) if xp else '--'} dcount {xp[1] if xp else '--'} | X_bulk {xb[0] if xb else '--':>5} "
            f"err {fmt(xb[4]) if xb else '--'} | err at X=8147 {fmt(rows[-1][4])}")
    detail = " ".join(f"{X}:{dc:+d}/{b}+{e}/{fmt(er)}" for X, dc, b, e, er in rows)
    return line, detail


if __name__ == "__main__":
    print("detail columns  X : count difference (port - true, core of W) / off-line bulk (1/2,3/4) + edge [3/4,1)"
          " / err in mean spacings\n")
    for t0 in (20, 50, 100, 200, 400, 800, 1600, 3200):
        truth = true_zeta_zeros(t0, t0 + 20)
        for name in ("zeta", "zeta_c"):
            rows = scan(name, t0, truth)
            line, detail = summarize(name, t0, truth, rows)
            print(line); print("    ", detail, flush=True)
    print()
    for t0 in (20, 50, 80, 110, 160):
        truth = true_dh_online(t0, t0 + 20)
        rows = scan("DH", t0, truth)
        line, detail = summarize("DH", t0, truth, rows)
        print(line); print("    ", detail, flush=True)
