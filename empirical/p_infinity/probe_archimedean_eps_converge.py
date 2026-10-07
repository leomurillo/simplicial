"""
probe_archimedean_eps_converge.py — does the QW ground eps_lambda converge to a POSITIVE limit?

Last run: the fixed-n=4 mechanism eps ~ c*(1-chi_4), c~O(10)>0, holds for lambda<=2.3, but the
Fourier-truncation eps(N) does NOT visibly converge at large lambda (drift worsening with N). The
question that decides (H0') at each window: is eps(infinity) a POSITIVE limit (slow Fourier
convergence to the tiny c*(1-chi_4)), or does eps(N) -> 0 (form PSD but singular)?

Approach (robust, no oscillatory quad => no hang): fine N-sweep of the DIRECT ground eps(N) +
Aitken-Delta^2 extrapolation of the limit eps(inf). Compare to the high-precision n=4 prolate defect
(1-chi_4) via the Bouwkamp CLOSED FORM. If eps(inf) ~ c*(1-chi_4) with c>0, the ground is a genuine
positive near-kernel carried by the prolate defect (per-window H0' holds, mechanism confirmed). If
eps(inf) -> 0, the limit obligation is marginal at that window.

dps 45. Deterministic, local, no torch. Fourier-basis eps is feasible only while N resolves the tiny
ground (lambda <~ 2.5); lambda=3 (true eps~1e-48) is out of Fourier reach and flagged.
"""
import sys
import mpmath as mp

sys.stdout.reconfigure(encoding="utf-8")
mp.mp.dps = 45
PI = mp.pi


def primes_upto(xx):
    out, n = [], 2
    while n <= xx:
        if all(n % p for p in out):
            out.append(n)
        n += 1
    return out


def build_QW(lam, N):
    L = 2 * mp.log(lam)
    w = lambda k: 2 * PI * k / L
    pj = []
    for p in primes_upto(float(mp.exp(L)) + 1e-12):
        j = 1
        while j * mp.log(p) <= L + mp.mpf("1e-30"):
            pj.append((j * mp.log(p), mp.log(p) * mp.power(p, -mp.mpf(j) / 2)))
            j += 1
    pts = mp.linspace(0, L, 16)
    S = {}
    for k in range(-N, N + 1):
        wk = w(k)
        A = mp.quad(lambda y: mp.sin(wk * y) * 2 * mp.cosh(y / 2), pts)
        B = mp.quad(lambda y: mp.exp(y / 2) * mp.sin(wk * y) / (2 * mp.sinh(y)) if y != 0 else wk / 2, pts)
        P = mp.fsum(cw * mp.sin(wk * yp) for yp, cw in pj)
        S[k] = A - B - P
    tailL = mp.log(mp.tanh(L / 2)) / 2
    D = {}
    for k in range(0, N + 1):
        wk = w(k)
        qd = lambda y: 2 * (1 - y / L) * mp.cos(wk * y)
        A = mp.quad(lambda y: qd(y) * 2 * mp.cosh(y / 2), pts)
        Bint = mp.quad(lambda y: (mp.exp(y / 2) * qd(y) - 2) / (2 * mp.sinh(y)) if y != 0
                       else (mp.mpf(1) / 2 - 1 / L), pts)
        WR = (mp.log(4 * PI) + mp.euler) + Bint + 2 * tailL
        P = mp.fsum(cw * (2 * (1 - yp / L) * mp.cos(wk * yp)) for yp, cw in pj)
        D[k] = A - WR - P
    dim = 2 * N + 1
    QW = mp.matrix(dim, dim)
    for i in range(dim):
        for j in range(dim):
            n, m = i - N, j - N
            QW[i, j] = D[abs(n)] if n == m else (S[m] - S[n]) / (PI * (n - m))
    return QW, primes_upto(float(mp.exp(L)) + 1e-12)


def ground(QW, N):
    Ev = mp.matrix(N + 1, N + 1)
    for k in range(N + 1):
        for l in range(N + 1):
            a, b = QW[N + k, N + l], QW[N + k, N - l]
            Ev[k, l] = a if (k == 0 and l == 0) else (mp.sqrt(2) * a if (k == 0 or l == 0) else a + b)
    return min(mp.mpf(str(e)) for e in mp.eigsy(Ev, eigvals_only=True))


def bouwkamp_even(c, K):
    M = mp.zeros(K, K)
    for i in range(K):
        k = 2 * i
        M[i, i] = k * (k + 1) + c ** 2 * mp.mpf(2 * k * k + 2 * k - 1) / ((2 * k - 1) * (2 * k + 3))
        if i + 1 < K:
            off = c ** 2 * mp.mpf((k + 1) * (k + 2)) / ((2 * k + 3) * mp.sqrt((2 * k + 1) * (2 * k + 5)))
            M[i, i + 1] = off
            M[i + 1, i] = off
    return mp.eigsy(M)


def chi4_defect(lam):
    """1 - chi_4 via the Bouwkamp eigenfunction-ratio CLOSED FORM (no quad)."""
    c = 2 * PI * lam ** 2
    K = max(30, int(float(c) / 2) + 25)
    E, Q = bouwkamp_even(c, K)
    beta = [Q[i, 2] for i in range(K)]                      # n=4 mode (3rd even, col 2)
    psi0 = mp.fsum(beta[i] * mp.sqrt(2 * i + mp.mpf(1) / 2) * mp.legendre(2 * i, 0) for i in range(K))
    chi = lam * mp.sqrt(2) * beta[0] / psi0
    return 1 - chi


def aitken(seq):
    """Aitken Delta^2 on the last 3 entries: extrapolated limit of a geometrically-convergent seq."""
    if len(seq) < 3:
        return None
    x0, x1, x2 = seq[-3], seq[-2], seq[-1]
    denom = (x2 - x1) - (x1 - x0)
    if denom == 0:
        return x2
    return x2 - (x2 - x1) ** 2 / denom


def ns(x, n=5):
    return mp.nstr(mp.mpf(x), n)


def main():
    print("=" * 100)
    print("Convergence of the QW ground eps_lambda — does it reach a POSITIVE limit ~ c*(1-chi_4)?")
    print("=" * 100)

    for lf in (2.0, 2.3, 2.5):
        lam = mp.mpf(str(lf))
        d4 = chi4_defect(lam)
        print(f"\nlambda={lf}   1-chi_4(hp) = {ns(d4,6)}")
        Ns = list(range(16, 41, 4))                        # 16,20,...,40
        seq, primes = [], None
        print(f"  {'N':>4} {'eps(N)':>16} {'rel prev':>10} {'eps/(1-chi4)':>14}")
        for N in Ns:
            QW, primes = build_QW(lam, N)
            e = ground(QW, N)
            rel = abs(e - seq[-1]) / abs(seq[-1]) if seq else None
            seq.append(e)
            print(f"  {N:>4} {ns(e,7):>16} {(f'{float(rel):.2%}' if rel is not None else '--'):>10} "
                  f"{float(e / d4):>14.4f}")
            if rel is not None and rel < mp.mpf("0.005"):
                print(f"       (converged: rel < 0.5%)")
                break
        ext = aitken(seq)
        print(f"  primes in window: {primes}")
        if ext is not None:
            print(f"  Aitken-extrapolated eps(inf) = {ns(ext,6)}   sign = {'+' if ext > 0 else ('0' if ext==0 else '-')}")
            print(f"  eps(inf)/(1-chi_4) = {float(ext / d4):.4f}   "
                  f"(positive & O(10) => prolate defect carries the ground; H0' holds at this window)")

    print("\n" + "=" * 100)
    print("READING: if eps(N) flattens to a positive value tracking c*(1-chi_4) (c>0, O(10)), the")
    print("ground is a genuine positive near-kernel (per-window H0' confirmed, fixed-n4 mechanism).")
    print("If eps(N) keeps decaying toward 0 with no flattening, eps(inf) is marginal -- the limit")
    print("obligation. (Fourier eps is resolvable only while N reaches the tiny true ground; large")
    print("lambda needs a prolate-adapted Weil-matrix re-derivation, scoped separately.)")
    print("=" * 100)


if __name__ == "__main__":
    main()
