"""
Paper 54, section 4.2 -- EXPLORATORY probe of Open Problem 4.6 (frequency-wise positivity of the total FDT violation).
NOT BLIND, NOT A CERTIFICATE: written after p54hs_harada_sasa_cert.py run 3 returned 8/8, to test whether the
finite-arrow positivity seen there (H6) survives strong, non-normal arrows.  float64 throughout; a negative value
below the stated tolerance would be a counterexample to the conjecture and would be verified exactly before use.

Probe A: random Lindbladians on C^d, d = 2, 3 (Ginibre jumps, GUE Hamiltonians scaled by kappa in {0,1,5,25}),
         metrics SLD and BKM in the eigenbasis of the numerically computed stationary state.
         Quantity: Delta_tot(omega) = -Im Tr[(i omega + Lt_f)^-1 A_f] on 801 log-spaced omega in [1e-4, 1e4].
Probe B: the bare matrix statement.  For real P with P + P^T <= 0 and spectrum in Re < 0,
         F(omega) = omega Tr[(P^2 + omega^2)^-1 (P^T - P)/2], n = 2..12, 300 trials each (1 in 5 with a rank-deficient
         symmetric part, i.e. hypocoercive), antisymmetric part scaled up to 100 x.
Results (2026-10-01, seeds 20261001 and 7):  A: 1600 cases, 0 negative; worst min/||A||^2 = 7.8e-15 (high-omega edge).
                                             B: ~3300 cases, 0 negative; worst normalized min = 2.9e-19 (omega edge).
Outcome (2026-10-02): the conjecture was PROVED (Paper 54 Lemma 4.6 / Theorem 4.7; p54hs_op46_proof_cert.py).
"""
import numpy as np

def probe_A(seed=20261001):
    rng = np.random.default_rng(seed)
    def lindblad_super(Ls_list, H, d):
        S = np.zeros((d * d, d * d), complex)
        for k in range(d * d):
            E = np.zeros(d * d, complex); E[k] = 1; E = E.reshape(d, d)
            out = -1j * (H @ E - E @ H)
            for L in Ls_list:
                out += L @ E @ L.conj().T - 0.5 * (L.conj().T @ L @ E + E @ L.conj().T @ L)
            S[:, k] = out.reshape(-1)
        return S
    def analyse(Ls, d, kind):
        w, V = np.linalg.eig(Ls)
        sig = V[:, np.argmin(abs(w))].reshape(d, d); sig = sig / np.trace(sig); sig = (sig + sig.conj().T) / 2
        p, U = np.linalg.eigh(sig)
        if p.min() <= 1e-9: return None
        T = np.zeros((d * d, d * d), complex)
        for k in range(d * d):
            E = np.zeros(d * d, complex); E[k] = 1; E = E.reshape(d, d)
            T[:, k] = (U.conj().T @ E @ U).reshape(-1)
        Lsr = T @ Ls @ np.linalg.inv(T)
        c = []
        for i in range(d):
            for j in range(d):
                if kind == "SLD": c.append((p[i] + p[j]) / 2)
                else: c.append(p[i] if abs(p[i] - p[j]) < 1e-14 else (p[i] - p[j]) / (np.log(p[i]) - np.log(p[j])))
        C = np.diag(c); Lh = Lsr.conj().T; Lt = np.linalg.inv(C) @ Lsr @ C; A = (Lh - Lt) / 2
        ws = np.logspace(-4, 4, 801)
        vals = np.array([-np.imag(np.trace(np.linalg.solve(1j * x * np.eye(d * d) + Lt, A))) for x in ws])
        return vals.min() / max(np.linalg.norm(A) ** 2, 1e-300)
    count = neg = 0; worst = np.inf
    for d in (2, 3):
        for trial in range(400):
            kappa = [0.0, 1.0, 5.0, 25.0][trial % 4]; nj = 1 + trial % 3
            Ls_list = [(rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))) / np.sqrt(2) for _ in range(nj)]
            G = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d)); H = kappa * (G + G.conj().T) / 2
            Ls = lindblad_super(Ls_list, H, d)
            for kind in ("SLD", "BKM"):
                m = analyse(Ls, d, kind)
                if m is None: continue
                count += 1; neg += m < -1e-10; worst = min(worst, m)
    return count, neg, worst

def probe_B(seed=7):
    rng = np.random.default_rng(seed); ws = np.logspace(-3, 3, 601)
    count = neg = 0; worst = np.inf
    for n in range(2, 13):
        for t in range(300):
            G = rng.normal(size=(n, n)); S = -(G @ G.T) * rng.choice([0.01, 0.1, 1.0])
            if t % 5 == 0:
                k = max(1, n // 3); Gk = rng.normal(size=(n, k)); S = -(Gk @ Gk.T)
            Ar = rng.normal(size=(n, n)); A = (Ar - Ar.T) / 2 * rng.choice([0.1, 1, 10, 100])
            P = S - A
            if np.max(np.linalg.eigvals(P).real) > -1e-9: continue
            v = np.array([w * np.trace(np.linalg.solve(P @ P + w * w * np.eye(n), (P.T - P) / 2)) for w in ws])
            count += 1; neg += v.min() < -1e-12 * max(1, np.abs(v).max())
            worst = min(worst, v.min() / max(np.linalg.norm(A) ** 2, 1e-300))
    return count, neg, worst

if __name__ == "__main__":
    a = probe_A(); print(f"Probe A (Lindblad): cases {a[0]}, negative {a[1]}, worst normalized min {a[2]:.3e}")
    b = probe_B(); print(f"Probe B (dissipative matrices): cases {b[0]}, negative {b[1]}, worst normalized min {b[2]:.3e}")
