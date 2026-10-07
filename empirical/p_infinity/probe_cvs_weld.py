"""
probe_cvs_weld.py — weld the CCM matrix QW_lambda to Connes-van Suijlekom [CS] 2511.23257.

[CS] Thm `finmain`: for a real symmetric Q of the FORM
    q_{ii}=a_i,  q_{ij}=(b_i-b_j)/(i-j) (i!=j),   a_{-j}=a_j, b_{-j}=-b_j,
with D=diag(j), gamma the reflection, eta=sum e_j (even), beta=sum b_j e_j (odd):
   [D,Q] = DQ-QD = |beta><eta| - |eta><beta|   (the RANK-2 commutator = the two pole terms),
and IF Q>=0 with 1-dim kernel ker Q=<xi> (xi even), then
   D' := D - |D xi><eta|  is self-adjoint w.r.t. Q,  and  the zeros of xi-hat are all REAL.
D' is exactly CCM's rank-one-perturbed D~; finmain(ii) is CCM Thm 1.1.

This script verifies, on the ACTUAL CCM matrix:
  (W1) QW_lambda IS a [CS] (form) matrix with b_n = -S_n/pi  (off-diagonal exact).
  (W2) the rank-2 commutator [D,QW] = |beta><eta| - |eta><beta|  (machine-exact).
  (W3) the [CS] Lemma `key` relations on the ground xi: exact identity QD xi = -beta + eps*D xi,
       D' xi = 0, and the Q-self-adjointness DEFECT of D' scales with eps_lambda (= (H0')).
  (W4) the finmain determinant identity Det(D'-s) = -s prod(j-s) sum_j xi_j/(j-s).
  (W5) the zeros (eigenvalues of D') are REAL; and WHY (ground xi nodeless => interlacing).

mpmath dps 40, deterministic, local. No torch.
"""

import mpmath as mp
import numpy as np

mp.mp.dps = 40


def primes_upto(x):
    out, n = [], 2
    while n <= x:
        if all(n % p for p in out):
            out.append(n)
        n += 1
    return out


def build_QW_full(lam, N):
    """Full CCM matrix QW on V_n (n=-N..N) + the per-frequency scalars S_n."""
    L = 2 * mp.log(lam)
    w = lambda k: 2 * mp.pi * k / L
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
    cgamma = mp.euler
    tailL = mp.log(mp.tanh(L / 2)) / 2
    D = {}
    for k in range(0, N + 1):
        wk = w(k)
        qd = lambda y: 2 * (1 - y / L) * mp.cos(wk * y)
        A = mp.quad(lambda y: qd(y) * 2 * mp.cosh(y / 2), pts)
        Bint = mp.quad(lambda y: (mp.exp(y / 2) * qd(y) - 2) / (2 * mp.sinh(y)) if y != 0
                       else (mp.mpf(1) / 2 - 1 / L), pts)
        WR = (mp.log(4 * mp.pi) + cgamma) / 2 * 2 + Bint + 2 * tailL
        P = mp.fsum(cw * (2 * (1 - yp / L) * mp.cos(wk * yp)) for yp, cw in pj)
        D[k] = A - WR - P
    dim = 2 * N + 1
    QW = mp.matrix(dim, dim)
    for i in range(dim):
        for j in range(dim):
            n, m = i - N, j - N
            QW[i, j] = D[abs(n)] if n == m else (S[m] - S[n]) / (mp.pi * (n - m))
    return QW, S, L


def main():
    print("=" * 84)
    print("CvS weld: QW_lambda  ==  [CS] 2511.23257 (form) matrix; D' = CCM D~; zeros real")
    print("=" * 84)
    ok = True
    for lam, N in [(mp.mpf("1.5"), 10), (mp.mpf("2.0"), 12)]:
        dim = 2 * N + 1
        QW, S, L = build_QW_full(lam, N)
        idx = list(range(-N, N + 1))
        # b_n = -S_n/pi
        b = mp.matrix(dim, 1)
        for i, n in enumerate(idx):
            b[i] = -S[n] / mp.pi
        # (W1) form check: QW[i,j] == (b_i - b_j)/(n_i - n_j) off-diagonal
        w1 = mp.mpf(0)
        for i in range(dim):
            for j in range(dim):
                if i != j:
                    pred = (b[i] - b[j]) / (idx[i] - idx[j])
                    w1 = max(w1, abs(QW[i, j] - pred))
        # b odd, a even
        bodd = max(abs(b[i] + b[dim - 1 - i]) for i in range(dim))
        aeven = max(abs(QW[i, i] - QW[dim - 1 - i, dim - 1 - i]) for i in range(dim))
        # (W2) rank-2 commutator [D,QW] = |beta><eta| - |eta><beta|
        Dm = mp.matrix(dim, dim)
        for i in range(dim):
            Dm[i, i] = idx[i]
        comm = Dm * QW - QW * Dm
        eta = mp.matrix([mp.mpf(1)] * dim)
        w2 = mp.mpf(0)
        for i in range(dim):
            for j in range(dim):
                rk2 = b[i] * eta[j] - eta[i] * b[j]
                w2 = max(w2, abs(comm[i, j] - rk2))
        # ground eigenvector xi (even sector ground = global ground)
        E, V = mp.eigsy(QW)
        gi = min(range(dim), key=lambda k: E[k])
        eps = E[gi]
        xi = mp.matrix([V[i, gi] for i in range(dim)])
        s_eta = mp.fsum(xi[i] for i in range(dim))          # <eta|xi>
        xi = xi / s_eta                                      # normalize <eta|xi>=1
        even_def = max(abs(xi[i] - xi[dim - 1 - i]) for i in range(dim))
        beta_xi = mp.fsum(b[i] * xi[i] for i in range(dim))  # <beta|xi> ~ 0 (parity)
        # (W3) Lemma key: QD xi = -beta + eps*D xi ; D' xi = 0; self-adjointness defect ~ eps
        Dxi = mp.matrix([idx[i] * xi[i] for i in range(dim)])
        QDxi = QW * Dxi
        keyi = max(abs(QDxi[i] + b[i] - eps * Dxi[i]) for i in range(dim))   # exact relation
        naive = max(abs(QDxi[i] + b[i]) for i in range(dim))                 # the eps-defect
        Dp = Dm - Dxi * eta.T                                # D' = D - |D xi><eta|
        Dpxi = Dp * xi
        dpxi = max(abs(Dpxi[i]) for i in range(dim))         # should be 0 exactly
        M = QW * Dp
        sa_def = max(abs(M[i, j] - M[j, i]) for i in range(dim) for j in range(dim))
        # (W4) determinant identity at a sample complex s
        s0 = mp.mpc("0.37", "0.21")
        lhs = mp.det(Dp - s0 * mp.eye(dim))
        prodj = mp.fprod([(idx[j] - s0) for j in range(dim)])
        sm = mp.fsum(xi[j] / (idx[j] - s0) for j in range(dim))
        rhs = -s0 * prodj * sm
        w4 = abs(lhs - rhs) / abs(rhs)
        # (W5) zeros real + WHY: nodeless xi => interlacing. Count sign changes of xi; find roots of g(s).
        signs = [mp.sign(mp.re(xi[i])) for i in range(dim) if abs(xi[i]) > mp.mpf("1e-30")]
        sign_changes = sum(1 for a, b_ in zip(signs, signs[1:]) if a != b_)
        g = lambda s: mp.fsum(xi[j] / (s - idx[j]) for j in range(dim))
        real_roots = 0
        for j in range(dim - 1):
            lo, hi = idx[j] + mp.mpf("1e-6"), idx[j + 1] - mp.mpf("1e-6")
            if mp.re(g(lo)) * mp.re(g(hi)) < 0:
                real_roots += 1
        # (W6) eigenvalues of D' are REAL, and (scaled by 2pi/L) reproduce gamma_1
        Dpn = np.array([[complex(Dp[i, j]) for j in range(dim)] for i in range(dim)], dtype=complex)
        ev = np.linalg.eigvals(Dpn)
        maxim = max(abs(e.imag) for e in ev)
        pos = sorted(e.real for e in ev if abs(e.imag) < 1e-9 and e.real > 1e-6)
        gamma1 = float(2 * mp.pi / L) * pos[0] if pos else float("nan")
        good = (w1 < 1e-30 and w2 < 1e-30 and bodd < 1e-30 and even_def < 1e-25
                and keyi < 1e-25 and dpxi < 1e-25 and w4 < 1e-25 and maxim < 1e-9)
        ok = ok and good
        print(f"\n  lambda={float(lam):.2f}  N={N}  (eps_lambda={mp.nstr(eps,4)}):")
        print(f"   W1 form |QW-(b_i-b_j)/(i-j)|={mp.nstr(w1,2)}; b odd={mp.nstr(bodd,2)}; a even={mp.nstr(aeven,2)}")
        print(f"   W2 rank-2 commutator [D,QW]=|b><eta|-|eta><b| defect={mp.nstr(w2,2)}")
        print(f"   W3 Lemma key: |QDxi+beta-eps*Dxi|={mp.nstr(keyi,2)} (exact); naive |QDxi+beta|={mp.nstr(naive,2)} (~eps)")
        print(f"      D'xi={mp.nstr(dpxi,2)} (=0); Q-self-adj defect of D' = {mp.nstr(sa_def,3)}  vs eps={mp.nstr(eps,3)}")
        print(f"   W4 finmain det identity Det(D'-s)=-s prod(j-s) sum xi_j/(j-s): rel-err={mp.nstr(w4,2)}")
        print(f"   W5 xi sign-changes={sign_changes} (NOT nodeless); interlacing-protected roots={real_roots}/{dim-1}")
        print(f"      => {dim-1-real_roots} zeros NOT interlacing-protected -> real ONLY by Q>=0 (this is (H0'))")
        print(f"   W6 eig(D') max|Im|={maxim:.1e} (all REAL); smallest pos eig*2pi/L={gamma1:.5f} (gamma_1=14.13472)")
        print(f"   => weld {'OK' if good else 'FAIL'}")
    print("-" * 84)
    print("RESULT:", "GREEN" if ok else "RED")
    return ok


if __name__ == "__main__":
    import sys
    sys.exit(0 if main() else 1)
