"""
probe_archimedean_edge_rung.py — the MATCHED-RUNG refinement of the edge-law test.

The fixed-n=4 test (probe_archimedean_edge_law_hp) showed eps/(1-chi_4) is a positive O(10)
constant for lambda <= 2.3 (through the 5-joining), then BLOWS UP (113, 1100, ...). Two candidate
causes, disentangled here:
  (b) RESOLUTION: eps at large lambda may be N-under-resolved (artificially large) -> N-sweep.
  (a) WRONG RUNG: the fixed n=4 prolate defect plunges faster than the true ground; the ground may
      track a HIGHER, lambda-dependent prolate rung -> compute the concentration CHAIN 1-chi_{2m}
      (m=0..7) and find the rung m* whose defect matches eps_lambda. Does m* climb smoothly?

Decisive readings:
  * if eps is NOT N-converged and drops to ~ (1-chi_4) once resolved  -> blowup was resolution;
    the fixed-n=4 mechanism holds and (H0') stays "eps = c (1-chi_4), c>0 bounded".
  * if eps IS N-converged and a HIGHER rung m*(lambda) matches it with eps/(1-chi_{2m*}) ~ O(1)
    and m* climbs smoothly  -> the ground rides a MOVING prolate rung, still sign-supplied.
  * if no rung matches eps's decay  -> the prolate picture is incomplete; difficulty elsewhere.

Phase 1 (dps 45): N-sweep eps (QW even-sector ground).  Phase 2 (dps 70): Bouwkamp concentration
chain via the eigenfunction-ratio closed form chi_{2m} = lambda sqrt(2) beta0 / psi(0), validated
by eigenfunction constancy.  Deterministic, local, no torch.
"""
import sys
import mpmath as mp

sys.stdout.reconfigure(encoding="utf-8")
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


def _psi_factory(beta, ks, K):
    def Psi(u):
        return mp.fsum(beta[i] * mp.sqrt(ks[i] + mp.mpf(1) / 2) * mp.legendre(ks[i], u) for i in range(K))
    return Psi


def concentration_chain(lam, mmax):
    """1 - chi_{2m} for m=0..mmax via the eigenfunction-ratio CLOSED FORM (fast, no quad).
    Returns (chain, Q, ks, K, c) so specific rungs can be validated on demand."""
    c = 2 * PI * lam ** 2
    K = max(mmax + 6, int(float(c) / 2) + 30)
    E, Q = bouwkamp_even(c, K)
    ks = [2 * i for i in range(K)]
    chain = []
    for m in range(mmax + 1):
        beta = [Q[i, m] for i in range(K)]
        Psi = _psi_factory(beta, ks, K)
        chi0 = lam * mp.sqrt(2) * beta[0] / Psi(0)
        chain.append(dict(m=m, n=2 * m, defect=1 - chi0))
    return chain, Q, ks, K, c


def validate_rung(lam, Q, ks, K, c, m):
    """eigenfunction constancy: chi(x=0) closed form vs chi(x=0.31 lam) oscillatory quad."""
    beta = [Q[i, m] for i in range(K)]
    Psi = _psi_factory(beta, ks, K)
    chi0 = lam * mp.sqrt(2) * beta[0] / Psi(0)
    xi = mp.mpf("0.31")
    pts = mp.linspace(-1, 1, max(48, int(float(c))))
    chi_xi = lam * mp.quad(lambda u: mp.cos(c * xi * u) * Psi(u), pts) / Psi(xi)
    return abs(chi0 - chi_xi)


def ns(x, n=5):
    return mp.nstr(mp.mpf(x), n)


def main():
    print("=" * 104)
    print("MATCHED-RUNG refinement: which prolate rung does the QW ground eps_lambda actually track?")
    print("=" * 104)

    lambdas = [2.0, 2.3, 2.5, 2.7, 3.0]

    # ---- Phase 1: N-sweep eps (dps 45) ----
    mp.mp.dps = 45
    print("\nPHASE 1 — N-convergence of eps (resolution confound check):")
    print(f"  {'lambda':>7} {'primes':>12} {'eps(N=14)':>14} {'eps(N=16)':>14} {'eps(N=18)':>14} {'rel 16->18':>11}")
    eps_conv = {}
    for lf in lambdas:
        lam = mp.mpf(str(lf))
        evals = {}
        primes = None
        for N in (14, 16, 18):
            QW, primes = build_QW(lam, N)
            evals[N] = ground(QW, N)
        rel = abs(evals[18] - evals[16]) / abs(evals[16])
        eps_conv[lf] = evals[18]
        conv = "OK" if rel < mp.mpf("0.05") else "DRIFT"
        print(f"  {lf:>7.2f} {str(primes):>12} {ns(evals[14],5):>14} {ns(evals[16],5):>14} "
              f"{ns(evals[18],5):>14} {float(rel):>10.2%} {conv}")

    # ---- Phase 2: prolate concentration chain + matched rung (dps 70) ----
    mp.mp.dps = 70
    print("\nPHASE 2 — prolate concentration chain 1-chi_{2m} and the rung matching eps (dps 70):")
    for lf in lambdas:
        lam = mp.mpf(str(lf))
        eps = mp.mpf(mp.nstr(eps_conv[lf], 40))     # converged eps (N=18)
        chain, Q, ks, K, c = concentration_chain(lam, mmax=7)
        # matched rung: m minimizing |log(defect) - log(eps)|
        leps = mp.log(eps)
        best = min(chain, key=lambda d: abs(mp.log(d["defect"]) - leps) if d["defect"] > 0 else mp.inf)
        d4 = next(d for d in chain if d["m"] == 2)
        r4 = validate_rung(lam, Q, ks, K, c, 2)
        rstar = validate_rung(lam, Q, ks, K, c, best["m"])
        print(f"\n  lambda={lf}  eps={ns(eps,5)}  (4 lambda^2 = {4*lf*lf:.1f}, edge index ~ that)")
        print(f"     chain 1-chi_2m: " + "  ".join(
            f"n{d['n']}:{ns(d['defect'],2)}" for d in chain))
        print(f"     fixed n=4 : 1-chi_4={ns(d4['defect'],4)}  eps/(1-chi_4)={float(eps/d4['defect']):.3g}  "
              f"(resid {ns(r4,2)})")
        print(f"     MATCHED n*={best['n']}: 1-chi_{best['n']}={ns(best['defect'],4)}  "
              f"eps/(1-chi_n*)={float(eps/best['defect']):.4f}  (resid {ns(rstar,2)})")

    print("\n" + "=" * 104)
    print("READING: Phase 1 — if eps keeps dropping with N at large lambda, the fixed-n4 blowup was")
    print("resolution; if eps is N-stable, the blowup is real. Phase 2 — if a higher rung n*(lambda)")
    print("matches eps with eps/(1-chi_n*) ~ O(1) and n* climbs smoothly, the ground rides a MOVING")
    print("prolate rung (still sign-supplied); the matched-rung ratio is the refined (H0') quantity.")
    print("=" * 104)


if __name__ == "__main__":
    main()
