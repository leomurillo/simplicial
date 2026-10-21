"""Paper 01g, Section 12.10 remarks (the point -1; the Syracuse law) -- certificate.

2026-10-17. Criteria fixed from an exploratory run in the same session: this script is a
reproducible re-derivation, not an out-of-sample test.

The law mu_n of Syrac(Z_3) mod 3^n is computed exactly (float64) from the stationarity
Y = 2^{-a}(1 + 3Y'), P(a) = 2^{-a} [Tao, Lemma 1.12], using the discrete logarithm base 2
(a primitive root mod 3^n), in which the sum over a is a geometric convolution on Z/(2*3^(n-1)).

S1  mu_n is a probability vector for n <= 13; its smallest atom at n = 5 equals c_5 = 4.4458e-4
    of Nikpour-Rabbani (Remark 5.4) to 4 digits.
S2  The largest atom sits at -1 mod 3^n for every n <= 13, and the ratio of consecutive values
    of (number of units) x (largest atom), i.e. max/mean, lies in [1.45, 1.55] for 6 <= n <= 13.
    [Run 1 FAILED on a mis-specified S2 that compared raw maxima (ratio 1/2 = (3/2)/3, since the
    number of units triples). Repaired to max/mean before run 2; no other change.]
S3  (number of units) x (collision probability) increases by an amount in [0.30, 0.32] at every
    step 6 <= n <= 13.
S4  The Shannon entropy in trits minus n lies in [-1.05, -0.95] for n = 12, 13.
S5  (number of units) x (smallest atom) lies in [0.03, 0.06] for 8 <= n <= 13 and is smaller at
    n = 13 than at n = 8.
[Added before run 3, Section 12.11; criteria from the exploratory probe of the same session.]
S6  Proposition 12.25: mu_n is an eigenvector, eigenvalue 1, of the averaged one-step operator at
    gamma = 1: max |L(mu_n)/mu_n - 1| < 1e-12 on live classes with mu_n > 0, for 2 <= n <= 11.
S7  Lift loss of the Syracuse law: n * l(mu_n) is increasing for 8 <= n <= 13 and lies in [2.0, 2.2];
    n * (top-digit total variation distance from uniform, weighted by mass) lies in [0.85, 0.95]
    for 10 <= n <= 13. [Run 3 FAILED S7: the band [1.3, 1.5] had been copied from the probe's
    top-digit Fourier ratio, mislabelled as total variation, and the statistic summed absolute
    deviations without the factor 1/2. Repaired to the TV distance before run 4; the manuscript
    statement was corrected at the same time.]
S8  Entropy deficit increments d_n = (H_{n-1} - (n-1)) - (H_n - n) are decreasing for 9 <= n <= 13 and
    n^1.6 d_n lies in [0.8, 1.0] there.
S9  The smallest atom lies in the class -2 mod 81 for 5 <= n <= 12.
[Added before run 5, Proposition 12.28; criteria from the exploratory probe of the same session.]
S10 The twisted top-digit recursion of Proposition 12.28 holds with max error <= 1e-12 max|Z_n| for
    3 <= n <= 13.
S11 ||Z_n||_1 is strictly decreasing for 2 <= n <= 13; n*kappa_n lies in [0.4, 1.1] for 3 <= n <= 13
    and is increasing for 7 <= n <= 13.
[Added before run 6, Propositions 12.30-12.31; criteria from the exploratory probe of the same session.]
S12 Proposition 12.30: max_j |z_n(j)| <= 1/sqrt(7) + 1e-12 for 2 <= n <= 13, with equality to 1e-12 at n = 2.
S13 Proposition 12.31: V_n = V_{n-1} - 2 Delta_n to relative error 1e-12 for 3 <= n <= 13, and
    n * (2 Delta_n / V_{n-1}) is increasing and lies in [0.8, 1.7] there.
[Added before run 7, Section 12.12 (twins and siblings); criteria from the exploratory probes
 collide.py, collide2.py, exact_sib.py of the same session.]
S14 Theorem 12.32 (float64): E_n = sum_j |Z_n(j)|^2 equals sum_{k<=40} 4^{-k} C_{n-1}(k), with
    C_m(k) = P(Y = A^k Y' mod 3^m), A(x) = 4x+1, to relative error 1e-12 for 1 <= n <= 13; and
    f_n - f_{n-1} = 2 F_n to absolute error 1e-12.
S15 Theorem 12.32 and Proposition 12.30 in exact rational arithmetic (metric trick M_3 = 3I - J),
    1 <= n <= 7: mu_n sums to 1; (1/2) sum_j x_j^T M_3 x_j equals sum_{k>=1} 4^{-k} C_{n-1}(k)
    (summed exactly over the period 3^{n-1} of A); 7 x^T M_3 x <= 2 (1^T x)^2 for every context,
    with equality attained at n = 2; f_1 = 10/9 and f_2 = 10/7.
S16 Direct Monte Carlo (seed 20261017, 4e6 histories, n = 9, collisions mod 3^8): no colliding pair
    has a_1 - a_1' odd; the shares of |a_1 - a_1'| in {0, 2, 4, 6} are within 0.002 of exact; the twin
    coherence is within 0.003 of W_8; the sibling coherences (|delta| = 2, 4, 6) lie in [-0.01, 0.01].
S17 Sibling factors c_m(k) = (2/3) 3^m C_m(k): |c_13(k) - c_12(k)| <= 5e-4 for 2 <= k <= 12;
    c_m(1) is increasing for 4 <= m <= 13 with m (c_m(1) - c_{m-1}(1)) in [0.0100, 0.0120] for
    8 <= m <= 13; n W_n = n F_n / f_{n-1} is increasing for 2 <= n <= 13 and below 1/2.
[Added before run 8, Theorem 12.38, Propositions 12.30 (hexagon form) and 12.39; criteria from the
 exploratory probe whythree.py of the same session.]
S18 Proposition 12.30, hexagon form, exact rationals, 2 <= n <= 7: every conditional top-digit
    probability lies in [2/21, 11/21]; at n = 2 the conditional laws are exactly (8,11,2)/21 and (8,2,11)/21.
S19 Proposition 12.39: for the biased laws P(a) = (1-q) q^(a-1), q in {0.35, 0.6, 0.7}, the twin/sibling
    identity K_n = w0 K_{n-1} + 2 sum_k q^(2k) w0 C_{n-1}(k), w0 = (1-q)/(1+q), holds to relative error
    1e-12 for 1 <= n <= 9; every ratio f_n/f_{n-1} is >= theta = 3 w0; at q = 0.35 (gamma > 1) the ratio
    at n = 9 lies in [theta, theta + 0.05]; at q = 0.6, 0.7 (gamma < 1) it is below 1.02.
S20 Theorem 12.38(d), multiplier 5: f_n/f_{n-1} >= 5/3 for 1 <= n <= 8, within 0.01 of 5/3 at n = 8;
    the fraction of units carrying 90% of the mass decreases over n = 4, 6, 8 and is below 0.2 at n = 8.
[Added before run 9, Section 12.14 (the comparison target); criteria from the exploratory probes
 endpoint.py, vreg.py, monotone.py, comparison.py of the same session.]
S21 Proposition 12.42: for 2 <= k <= 9 and gamma in {0.5, 0.6, 0.7, 0.8, 0.9, 0.95, 1}, the Perron vector v of the
    minimum operator satisfies Lambda(gamma) - r_k(gamma) = ((3/2)^gamma/3)(1 - rho_k(gamma)) to 1e-10, and the
    comparison ratio (1 - rho_k(gamma))/ell(mu_k) is at most 0.67, at most 0.54 for k >= 3, and increasing in gamma.
S22 Lockstep: with gamma_k computed by bisection (tolerance 1e-9) for 3 <= k <= 9, the ratio
    (1 - gamma_k)/ell(mu_k) lies in [0.69, 0.84] (the comparison would give at most 1/ln(4/3) = 3.48).
[Added before run 10, Propositions 12.46-12.48; criteria from the probes concave.py, convex2.py, general.py, cex.py.]
S23 Proposition 12.46 at fixed gamma in {0.8, 1}, 3 <= k <= 7: with c' the lift of v_k(gamma) and g = Phi^(k+1)(c') - r_k c',
    (a) g >= -1e-14 and sum g / sum c' = Lambda - r_k to 1e-10; (b) for the minimizing policy at level k+1 with left
    vector u, r_(k+1) - r_k = <u, g>/<u, c'> to 1e-8; (c) nu_k = (r_(k+1) - r_k)/(Lambda - r_k) lies in (0, 1).
    [Run 10 FAILED S23 on a mis-specified tolerance: (a) required g >= -1e-14 in absolute terms, below the
    eigenvector precision (1e-12 relative); the zero-gain entries came out at -2e-12 relative. All identities held
    to <= 3e-13. Repaired to g >= -1e-10 max g before run 11; no other change.]
S24 Proposition 12.48: for Phi(x) = (min(x0, x1), x1 + min(x0, x1)), the minimum over the four policies of the spectral
    radius is 1 (to 1e-12), while <p, Phi p>/<p, p> = 1 + sqrt(2)/4 (to 1e-12), p = (1, 1 + sqrt 2).
S25 Per-level decay: for gamma in {0.5, 0.8, 0.9} and 2 <= k <= 8, ell(v_(k+1))/ell(v_k) <= ell(mu_(k+1))/ell(mu_k).
[Added before run 12, Proposition 12.50; criteria from the probe misalign.py of the same session.]
S26 Proposition 12.50 at gamma in {0.9, 1}, k in {5, 6, 7}: the misalignment bound B_W <= G_k holds for W = 1, 2, 3, 4;
    B_2/G_k lies in [0.08, 0.20]; the fraction of odd rows with a W-aligned target is in [0.74, 0.83] for W = 2,
    in [0.27, 0.38] for W = 3, and at most 0.05 for W = 6.
[Added before run 13, Proposition 12.52; criteria from the probes hierarchy.py, anatomy.py of the same session.]
S27 Proposition 12.52: for the minimizing, a random, and the maximizing policy at modulus 3^6 (gamma in {0.9, 1}),
    the marginals of the left Perron vector satisfy rho u_j(s) = 2^-g u_j(s/2) + (3/2)^g u_(j+1)(T(s)) for
    1 <= j <= 5 to relative error 1e-11.
[Added before run 14, Section 12.15 (Argon's live-row results, with the summed form and the fence); criteria from
 the review probes argon_kl_checks.py and argon_h_check.py of the same session.]
S28 Proposition 12.54 at gamma in {0.9, 1}, k in {5, 6, 7}: every odd row x0 = 5, 8 mod 9 is 2-aligned; the fraction of
    all odd rows with a 2-aligned target equals 2/3 + p/3 to 1e-12, p the fraction among rows x0 = 2 mod 9, and
    p lies in [0.25, 0.47]; m_3(x0) = m_2(x0) on x0 = 2 mod 9 and m_3(x0) = m_2(4 x0) on x0 = 5 mod 9, pointwise to
    1e-12 max(v).
S29 Proposition 12.55, same range: delta(y) = alpha delta(2y) on units y = 1 mod 3, alpha = 2^-g / r_k, to 1e-10 max(delta);
    the opposite-orientation formula for m_2 on the rows x0 = 2 mod 9 agrees with the direct minimum to 1e-10 max(v).
S30 Proposition 12.56, same range, for the minimizing and a random policy at modulus 3^(k+1): (3/2)^g u(r(s)) =
    rho U(s) - 2^-g U(s/2) on units to 1e-10 max U; <u, g> = sum_s U(s) h(s), h = rho delta - 2^-g delta(2.), to 1e-9
    relative. For the minimizing policy, h < 0 on a fraction of units in [0.07, 0.12], and the ratio of the negative to
    the positive part of h decreases in k for each gamma.
S31 Proposition 12.57: (a) for the minimizing, a random and the maximizing policy (gamma in {0.9, 1}, k in {5, 6, 7}),
    every unit class mod 3^j, j = 1, 2, 3, carries at least (sum_{d < phi(3^j)} alpha^-d)^-1 of the occupation, and for the
    minimizing policy every unit class mod 9 carries between 0.10 and 0.20; (b) for k in {3, 4}, the vector
    U_t = sum_d alpha^d 1_{2^d t} (t a unit with delta(t) = 0) satisfies U(2s) >= alpha U(s) (relative slack >= -1e-12),
    is positive, and has |sum U_t h| <= 1e-12 sum U_t |h|.
"""
import numpy as np, math, sys, json
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8")
HERE = Path(__file__).resolve().parent
rows = []
def check(name, ok, detail=""):
    rows.append({"name": name, "pass": bool(ok), "detail": detail})
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: {detail}", flush=True)

mu = np.array([1.0]); stats = {}; Zs = {}; OMEGA = np.exp(2j*np.pi/3); MUS = {0: mu.copy()}
for n in range(1, 14):
    M = 3**n; L = 2*3**(n-1)
    g = np.empty(L, dtype=np.int64); g[0] = 1
    for i in range(1, L): g[i] = (g[i-1]*2) % M
    f = np.zeros(M); f[(1 + 3*np.arange(3**(n-1))) % M] = mu
    F = f[g]; G = np.zeros(L); a = np.arange(1, L+1)
    G[L-1] = np.sum(2.0**(-a)*F[(L-1+a) % L])/(1 - 2.0**(-L))
    for j in range(L-2, -1, -1): G[j] = 0.5*F[j+1] + 0.5*G[j+1]
    mu = np.zeros(M); mu[g] = G
    p = mu[np.arange(M) % 3 != 0]; U = p.size
    if n >= 2:
        rr = np.arange(M); qq = ((2*rr - 1)//3) % (M//3); lf = np.stack([(qq + j*(M//3)) % M for j in range(3)], 1)
        Lmu = np.where(rr % 3 != 0, 0.5*mu[(2*rr) % M] + np.where(rr % 3 == 2, 1.5*mu[lf].mean(1), 0.0), 0.0)
        ok_live = (rr % 3 != 0) & (mu > 0); eig_err = float(np.abs(Lmu[ok_live]/mu[ok_live] - 1).max())
        T = mu.reshape(3, M//3); avg = T.mean(0); mn = T.min(0); lv = avg > 0
        lift_loss = float(3*(avg - mn)[lv].sum()/mu.sum())
        tv_top = float(0.5*np.abs(T - avg).sum()/mu.sum())
    else:
        eig_err = lift_loss = tv_top = float('nan')
    um = np.where(np.arange(M) % 3 != 0, mu, np.inf); amin = int(np.argmin(um))
    stats_extra = dict(eig_err=eig_err, lift_loss=lift_loss, tv_top=tv_top, argmin_mod81=amin % 81 if n >= 4 else -1)
    stats[n] = dict(total=mu.sum(), argmax_is_minus1=int(np.argmax(mu)) == M-1, max=p.max(), min=p.min(),
                    coll_units=(p**2).sum()*U, H_minus_n=-(p*np.log(p)).sum()/math.log(3) - n, min_units=p.min()*U)
    stats[n].update(stats_extra)
    if n >= 2:
        T3 = mu.reshape(3, M//3); Zs[n] = T3[0] + OMEGA*T3[1] + OMEGA**2*T3[2]
    MUS[n] = mu.copy()
    print(f"  n={n}: " + ", ".join(f"{k}={v:.6g}" if isinstance(v, float) else f"{k}={v}" for k, v in stats[n].items()), flush=True)

check("S1 probability vectors; c_5", all(abs(s['total'] - 1) < 1e-12 for s in stats.values()) and abs(stats[5]['min'] - 4.4458e-4) < 5e-8,
      f"c_5 = {stats[5]['min']:.6e}")
r = [3*stats[n]['max']/stats[n-1]['max'] for n in range(6, 14)]   # max/mean ratio: units triple
check("S2 largest atom at -1, growing like 3/2", all(s['argmax_is_minus1'] for s in stats.values()) and all(1.45 <= x <= 1.55 for x in r),
      f"ratios {[round(x, 4) for x in r]}")
d = [stats[n]['coll_units'] - stats[n-1]['coll_units'] for n in range(6, 14)]
check("S3 collision grows linearly", all(0.30 <= x <= 0.32 for x in d), f"increments {[round(x, 4) for x in d]}")
check("S4 full Shannon dimension", all(-1.05 <= stats[n]['H_minus_n'] <= -0.95 for n in (12, 13)),
      f"H-n = {stats[12]['H_minus_n']:.4f}, {stats[13]['H_minus_n']:.4f}")
mu_ = [stats[n]['min_units'] for n in range(8, 14)]
check("S5 smallest atom", all(0.03 <= x <= 0.06 for x in mu_) and mu_[-1] < mu_[0], f"{[round(x, 4) for x in mu_]}")
check("S6 Proposition 12.25 (averaged Perron vector)", all(stats[n]['eig_err'] < 1e-12 for n in range(2, 12)),
      f"max errors {[f'{stats[n]['eig_err']:.1e}' for n in range(2, 12)]}")
nl = [n*stats[n]['lift_loss'] for n in range(8, 14)]; nt = [n*stats[n]['tv_top'] for n in range(10, 14)]
check("S7 Syracuse lift loss ~ 1/n", all(b > a for a, b in zip(nl, nl[1:])) and all(2.0 <= x <= 2.2 for x in nl) and all(0.85 <= x <= 0.95 for x in nt),
      f"n*l = {[round(x, 3) for x in nl]}; n*TV_top = {[round(x, 3) for x in nt]}")
dd = {n: stats[n-1]['H_minus_n'] - stats[n]['H_minus_n'] for n in range(9, 14)}
check("S8 entropy deficit increments", all(dd[n+1] < dd[n] for n in range(9, 13)) and all(0.8 <= n**1.6*dd[n] <= 1.0 for n in dd),
      f"n^1.6 d_n = {[round(n**1.6*dd[n], 3) for n in dd]}")
check("S9 smallest atom near -2", all(stats[n]['argmin_mod81'] == 79 for n in range(5, 13)), f"argmin mod 81 = {[stats[n]['argmin_mod81'] for n in range(5, 14)]}")
errs = []
for n in range(3, 14):
    K = 3**(n-1); J = np.arange(K); c = (2*J >= K).astype(int); tau = ((2*J - 1)//3) % (K//3)
    rhs = 0.5*OMEGA**c*np.conj(Zs[n][(2*J) % K]) + 0.5*np.where(J % 3 == 2, OMEGA**c*np.conj(Zs[n-1][tau]), 0)
    errs.append(float(np.abs(Zs[n] - rhs).max()/np.abs(Zs[n]).max()))
check("S10 Proposition 12.28 (twisted top-digit recursion)", max(errs) <= 1e-12, f"max relative error {max(errs):.1e}")
nz = {n: float(np.abs(Zs[n]).sum()) for n in range(2, 14)}
nk = {n: n*(1 - nz[n]/nz[n-1]) for n in range(3, 14)}
check("S11 alignment defect", all(nz[n] < nz[n-1] for n in range(3, 14)) and all(0.4 <= nk[n] <= 1.1 for n in nk)
      and all(nk[n] > nk[n-1] for n in range(8, 14)), f"n*kappa_n = {[round(nk[n], 3) for n in nk]}")
def rel_z(n):
    m = MUS[n-1]; pos = m > 0
    return np.where(pos, Zs[n]/np.where(pos, m, 1), 0), m, pos
caps = {n: float(np.abs(rel_z(n)[0]).max()) for n in range(2, 14)}
check("S12 Proposition 12.30 (cap 1/sqrt7)", all(caps[n] <= 1/np.sqrt(7) + 1e-12 for n in caps) and abs(caps[2] - 1/np.sqrt(7)) < 1e-12,
      f"max|z_n| = {[round(caps[n], 6) for n in caps]}")
Vn = {}; ok13 = True; rn = {}
for n in range(2, 14):
    z, m, pos = rel_z(n); Vn[n] = float(np.sum(m[pos]*np.abs(z[pos])**2))
for n in range(3, 14):
    z, m, pos = rel_z(n); zp, mp, posp = rel_z(n-1)
    K = 3**(n-1); J = np.arange(K); tau = ((2*J - 1)//3) % (K//3); sel = (J % 3 == 2) & pos
    alpha = np.where(pos, m[(2*J) % K]/(2*np.where(pos, m, 1)), 0)
    Delta = float(np.sum((m*alpha*(1 - alpha)*np.abs(z[(2*J) % K] - zp[tau])**2)[sel]))
    ok13 &= abs(Vn[n-1] - 2*Delta - Vn[n]) <= 1e-12*Vn[n]
    rn[n] = n*2*Delta/Vn[n-1]
ok13 &= all(rn[n] > rn[n-1] for n in range(4, 14)) and all(0.8 <= rn[n] <= 1.7 for n in rn)
check("S13 Proposition 12.31 (chi-square energy identity)", ok13, f"n*r_n = {[round(rn[n], 3) for n in rn]}")

# --- Section 12.12: twins and siblings ---
def C_sib(m, k):
    if m == 0: return 1.0
    Mm = 3**m; y = np.arange(Mm, dtype=np.int64)
    return float(np.dot(MUS[m], MUS[m][(pow(4, k, Mm)*y + ((4**k - 1)//3) % Mm) % Mm]))
KK = {m: float(np.dot(MUS[m], MUS[m])) for m in range(14)}
ff = {m: (2/3)*3**m*KK[m] for m in range(14)}
cc = {m: {k: (2/3)*3**m*C_sib(m, k) for k in range(1, 41)} for m in range(13)}
FF = {n: sum(4.0**(-k)*cc[n-1][k] for k in range(1, 41)) for n in range(1, 14)}
ok14 = True; e14 = []
for n in range(1, 14):
    if n == 1: E = abs(MUS[1][0] + OMEGA*MUS[1][1] + OMEGA**2*MUS[1][2])**2
    else: E = float(np.sum(np.abs(Zs[n])**2))
    S = sum(4.0**(-k)*C_sib(n-1, k) for k in range(1, 41))
    e14.append(abs(E - S)/E); ok14 &= abs(E - S) <= 1e-12*E and abs(ff[n] - ff[n-1] - 2*FF[n]) <= 1e-12
check("S14 Theorem 12.32 (sibling identity, float64)", ok14, f"max relative error {max(e14):.1e}; 2F_13 = {2*FF[13]:.4f}")

from fractions import Fraction as Fr
def exact_laws(N):
    out = {0: [Fr(1)]}; m_ = [Fr(1)]
    for n in range(1, N+1):
        M = 3**n; L = 2*3**(n-1)
        g = [1]*L
        for i in range(1, L): g[i] = g[i-1]*2 % M
        f = [Fr(0)]*M
        for y in range(3**(n-1)): f[(1 + 3*y) % M] = m_[y]
        F = [f[x] for x in g]; G = [Fr(0)]*L
        G[L-1] = sum((Fr(1, 2**a)*F[(L-1+a) % L] for a in range(1, L+1)), Fr(0))/(1 - Fr(1, 2**L))
        for j in range(L-2, -1, -1): G[j] = (F[j+1] + G[j+1])/2
        m_ = [Fr(0)]*M
        for i, x in enumerate(g): m_[x] = G[i]
        out[n] = m_
    return out
EX = exact_laws(7)
def qM3(x): return 3*sum(v*v for v in x) - sum(x)**2
ok15 = True; eq2 = False
for n in range(1, 8):
    m_ = EX[n]; K = 3**(n-1); mp = EX[n-1]; Mm = 3**(n-1)
    ok15 &= sum(m_) == 1
    E = sum(qM3([m_[j], m_[j+K], m_[j+2*K]]) for j in range(K))/2
    def Cx(k):
        u = pow(4, k, Mm); b = ((4**k - 1)//3) % Mm
        return sum(mp[y]*mp[(u*y + b) % Mm] for y in range(Mm))
    S = sum((Fr(1, 4**k)*Cx(k) for k in range(1, Mm+1)), Fr(0))/(1 - Fr(1, 4**Mm))
    ok15 &= E == S
    if n >= 2:
        for j in range(K):
            x = [m_[j], m_[j+K], m_[j+2*K]]; t = sum(x); q = qM3(x)
            ok15 &= 7*q <= 2*t*t
            if n == 2 and t > 0 and 7*q == 2*t*t: eq2 = True
fx = {n: Fr(2, 3)*3**n*sum(v*v for v in EX[n]) for n in (1, 2)}
ok15 &= eq2 and fx[1] == Fr(10, 9) and fx[2] == Fr(10, 7)
check("S15 Theorem 12.32 and Proposition 12.30, exact rationals (metric trick)", ok15, f"n <= 7; f_1 = {fx[1]}, f_2 = {fx[2]}; cap equality at n = 2: {eq2}")

rng = np.random.default_rng(20261017)
n_ = 9; M = 3**n_; Mc = 3**(n_-1); S_ = 4_000_000; AM = 40
a_ = rng.geometric(0.5, size=(S_, n_)).astype(np.int64); A_ = np.cumsum(a_, axis=1)
Lp = 2*3**(n_-1); inv2 = pow(2, -1, M); tab = np.array([pow(inv2, i, M) for i in range(Lp)], dtype=np.int64)
Y = np.zeros(S_, dtype=np.int64); p3 = 1
for mm in range(n_):
    Y = (Y + p3*tab[A_[:, mm] % Lp]) % M; p3 *= 3
ctx = Y % Mc; ph = np.exp(2j*np.pi*(Y // Mc)/3); key = ctx*(AM+1) + np.minimum(a_[:, 0], AM)
cnt = np.bincount(key, minlength=Mc*(AM+1)).reshape(Mc, AM+1).astype(float)
Sp = (np.bincount(key, weights=ph.real, minlength=Mc*(AM+1)) + 1j*np.bincount(key, weights=ph.imag, minlength=Mc*(AM+1))).reshape(Mc, AM+1)
tot = (cnt.sum(1)**2).sum() - S_
ok16 = True; det16 = []
for d in range(0, 7):
    if d == 0:
        pr = (cnt**2).sum() - S_; coh = ((np.abs(Sp)**2).sum() - S_)/pr
        sh_ex = ff[n_-2]/ff[n_-1]; coh_ex = (ff[n_-1]/ff[n_-2] - 1)/2
        ok16 &= abs(pr/tot - sh_ex) <= 0.002 and abs(coh - coh_ex) <= 0.003
    else:
        pr = 2*(cnt[:, d:]*cnt[:, :-d]).sum()
        if d % 2:
            ok16 &= pr == 0; det16.append(f"d={d}: {int(pr)} pairs"); continue
        coh = 2*np.real((Sp[:, d:]*np.conj(Sp[:, :-d])).sum())/pr; kk = d//2
        sh_ex = 2*4.0**(-kk)*cc[n_-2][kk]/ff[n_-1]
        ok16 &= abs(pr/tot - sh_ex) <= 0.002 and -0.01 <= coh <= 0.01
    det16.append(f"d={d}: share {pr/tot:.4f} (exact {sh_ex:.4f}), coherence {coh:+.4f}")
check("S16 direct Monte Carlo of colliding pairs (twins and siblings)", ok16, "; ".join(det16))

ok17 = all(abs(cc[12][k] - (2/3)*3**13*C_sib(13, k)) <= 5e-4 for k in range(2, 13))
c1 = {m: (2/3)*3**m*C_sib(m, 1) for m in range(3, 14)}
ok17 &= all(c1[m] > c1[m-1] for m in range(4, 14)) and all(0.0100 <= m*(c1[m] - c1[m-1]) <= 0.0120 for m in range(8, 14))
nW = {n: n*FF[n]/ff[n-1] for n in range(2, 14)}
ok17 &= all(nW[n] > nW[n-1] for n in range(3, 14)) and all(v < 0.5 for v in nW.values())
check("S17 sibling factors converge, c_m(1) creeps, n W_n -> 1/2 from below", ok17,
      f"c_13(2..4) = {[round((2/3)*3**13*C_sib(13, k), 5) for k in (2, 3, 4)]}; c_13(1) = {c1[13]:.5f}; "
      f"m dc_m(1) = {[round(m*(c1[m] - c1[m-1]), 4) for m in range(8, 14)]}; n W_n = {[round(nW[n], 3) for n in nW]}")
# --- Theorem 12.38, Propositions 12.30 (hexagon) and 12.39 ---
ok18 = True; lo = Fr(2, 21); hi = Fr(11, 21); n2laws = set()
for n in range(2, 8):
    m_ = EX[n]; K = 3**(n-1)
    for j in range(K):
        x = [m_[j], m_[j+K], m_[j+2*K]]; t = sum(x)
        if t == 0: continue
        cond = [v/t for v in x]
        ok18 &= all(lo <= c <= hi for c in cond)
        if n == 2: n2laws.add(tuple(cond))
ok18 &= n2laws == {(Fr(8, 21), Fr(11, 21), Fr(2, 21)), (Fr(8, 21), Fr(2, 21), Fr(11, 21))}
check("S18 Proposition 12.30, hexagon form (exact)", ok18, f"conditional laws at n = 2: {sorted(tuple(str(c) for c in l) for l in n2laws)}")

def biased_law(base, N, q):
    out = {0: np.array([1.0])}; m_ = np.array([1.0])
    for n in range(1, N+1):
        M = base**n; L = (base-1)*base**(n-1)
        g = np.empty(L, dtype=np.int64); g[0] = 1
        for i in range(1, L): g[i] = (g[i-1]*2) % M
        f = np.zeros(M); f[(1 + base*np.arange(base**(n-1))) % M] = m_
        F = f[g]; G = np.zeros(L); a = np.arange(1, L+1)
        G[L-1] = np.sum((1-q)*q**(a-1)*F[(L-1+a) % L])/(1 - q**L)
        for j in range(L-2, -1, -1): G[j] = (1-q)*F[j+1] + q*G[j+1]
        m_ = np.zeros(M); m_[g] = G; out[n] = m_
    return out
ok19 = True; det19 = []
for q in (0.35, 0.6, 0.7):
    B = biased_law(3, 9, q); w0 = (1-q)/(1+q); th = 3*w0; err = 0.0
    for n in range(1, 10):
        Kn = float(B[n] @ B[n]); Km = float(B[n-1] @ B[n-1]); Mm = 3**(n-1); y = np.arange(Mm, dtype=np.int64)
        S = sum(q**(2*k)*w0*(float(B[n-1] @ B[n-1][(pow(4, k, Mm)*y + ((4**k-1)//3) % Mm) % Mm]) if n > 1 else 1.0) for k in range(1, 80))
        err = max(err, abs(Kn - (w0*Km + 2*S))/Kn)
    fq = [3**n*float(B[n] @ B[n]) for n in range(10)]
    rat = [fq[n]/fq[n-1] for n in range(1, 10)]
    ok19 &= err <= 1e-12 and all(r >= th - 1e-12 for r in rat)
    ok19 &= (th <= rat[-1] <= th + 0.05) if q < 0.5 else (rat[-1] < 1.02)
    det19.append(f"q={q}: theta={th:.4f}, ratio_9={rat[-1]:.4f}, err={err:.1e}")
check("S19 Proposition 12.39 (biased twin/sibling identity, L2 transition)", ok19, "; ".join(det19))

B5 = biased_law(5, 8, 0.5)
f5 = [5**n*float(B5[n] @ B5[n]) for n in range(9)]
r5 = [f5[n]/f5[n-1] for n in range(1, 9)]
fr90 = []
for n in (4, 6, 8):
    pp = np.sort(B5[n][B5[n] > 0])[::-1]; k90 = int(np.searchsorted(np.cumsum(pp), 0.9)) + 1; fr90.append(k90/(4*5**(n-1)))
ok20 = all(r >= 5/3 - 1e-12 for r in r5) and abs(r5[-1] - 5/3) <= 0.01 and fr90[0] > fr90[1] > fr90[2] and fr90[2] < 0.2
check("S20 Theorem 12.38(d), multiplier 5 (collision growth, concentration)", ok20,
      f"ratios {[round(r, 4) for r in r5]}; 90%-mass unit fractions {[round(v, 4) for v in fr90]}")

# --- Section 12.14: deficit = lift loss at every exponent; comparison with the Syracuse law ---
def kl_build(k):
    Mk = 3**k; rr = np.arange(Mk, dtype=np.int64); qq = ((2*rr - 1)//3) % (Mk//3)
    return dict(k=k, M=Mk, even=(2*rr) % Mk, live=(rr % 3 != 0), odd=(rr % 3 == 2),
                lifts=np.stack([(qq + j*(Mk//3)) % Mk for j in range(3)], axis=1))
def kl_phi(Bk, c, g):
    return np.where(Bk['live'], 2**(-g)*c[Bk['even']] + np.where(Bk['odd'], 1.5**g*c[Bk['lifts']].min(1), 0.0), 0.0)
def kl_perron(Bk, g, c0, iters=400000):
    c = c0/c0.sum(); lam = 0.0
    for it in range(iters):
        nw = kl_phi(Bk, c, g); s = nw.sum(); nw = nw/s
        if it > 30 and abs(s - lam) < 1e-14 and np.abs(nw - c).max() < 1e-12*nw.max(): return s, nw
        lam, c = s, nw
    return lam, c
def lift_loss(x, k):
    T = x.reshape(3, 3**(k-1)); return float(3*(T.mean(0) - T.min(0)).sum()/x.sum())
GAM = [0.5, 0.6, 0.7, 0.8, 0.9, 0.95, 1.0]
ok21 = True; ratios21 = {}; maxerr21 = 0.0
for k in range(2, 10):
    Bk = kl_build(k); c = Bk['live'].astype(float); lm = lift_loss(MUS[k], k); rk_row = []
    for g in GAM:
        lam, c = kl_perron(Bk, g, c)
        Lam = 2**(-g) + 1.5**g/3; loss = lift_loss(c, k)
        maxerr21 = max(maxerr21, abs((Lam - lam) - 1.5**g/3*loss)); rk_row.append(loss/lm)
    ratios21[k] = rk_row
    ok21 &= max(rk_row) <= 0.67 and (k < 3 or max(rk_row) <= 0.54) and all(b_ > a_ for a_, b_ in zip(rk_row, rk_row[1:]))
ok21 &= maxerr21 <= 1e-10
check("S21 Proposition 12.42 and the comparison ratio", ok21,
      f"identity error {maxerr21:.1e}; ratio at gamma=1: {[round(ratios21[k][-1], 3) for k in ratios21]}; at gamma=0.5: {[round(ratios21[k][0], 3) for k in ratios21]}")

def kl_gamma(k):
    Bk = kl_build(k); c = Bk['live'].astype(float); lo, hi = 0.3, 1.0
    while hi - lo > 1e-9:
        mid = (lo + hi)/2; lam, c2 = kl_perron(Bk, mid, c)
        if lam >= 1: lo, c = mid, c2
        else: hi = mid
    return lo
lock = {k: (1 - kl_gamma(k))/lift_loss(MUS[k], k) for k in range(3, 10)}
check("S22 lockstep of 1 - gamma_k with the Syracuse lift loss", all(0.69 <= v_ <= 0.84 for v_ in lock.values()),
      f"(1-gamma_k)/ell(mu_k) = {[round(v_, 3) for v_ in lock.values()]}")

# --- Propositions 12.46-12.48 ---
def kl_left(Bk, pol, g, iters=400000):
    Mk = Bk['M']; live = Bk['live']; odd = Bk['odd']
    se = np.nonzero(live)[0]; de = Bk['even'][se]; so = np.nonzero(odd)[0]; do_ = pol[so]; keep = do_ % 3 != 0; so, do_ = so[keep], do_[keep]
    u = live.astype(float); u /= u.sum(); lam = 0.0
    for it in range(iters):
        nw = np.bincount(de, weights=2**(-g)*u[se], minlength=Mk) + np.bincount(do_, weights=1.5**g*u[so], minlength=Mk)
        s = nw.sum(); nw /= s
        if it > 30 and abs(s - lam) < 1e-15 and np.abs(nw - u).max() < 1e-13*nw.max(): return s, nw
        lam, u = s, nw
    return lam, u
ok23 = True; nus = []
for g in (0.8, 1.0):
    Lam = 2**(-g) + 1.5**g/3
    for k in range(3, 8):
        Bk = kl_build(k); rk, vk = kl_perron(Bk, g, Bk['live'].astype(float))
        B1 = kl_build(k+1); cl = vk[np.arange(3**(k+1)) % 3**k]
        gg = kl_phi(B1, cl, g) - rk*cl
        ok23 &= gg.min() >= -1e-10*gg.max() and abs(gg.sum()/cl.sum() - (Lam - rk)) <= 1e-10
        rk1, vk1 = kl_perron(B1, g, cl)
        li = B1['lifts']; pol = li[np.arange(3**(k+1)), vk1[li].argmin(1)]
        lam_u, u = kl_left(B1, pol, g)
        Gk = float(u @ gg)/float(u @ cl)
        ok23 &= abs((rk1 - rk) - Gk) <= 1e-8 and 0 < Gk/(Lam - rk) < 1
        nus.append(round(Gk/(Lam - rk), 3))
check("S23 Proposition 12.46 (level recursion at fixed gamma)", ok23, f"nu_k for gamma=0.8 then 1, k=3..7: {nus}")

Phi2 = lambda x: np.array([min(x[0], x[1]), x[1] + min(x[0], x[1])])
pols = [np.array([[0, 1], [0, 2]], float), np.array([[0, 1], [1, 1]], float), np.array([[1, 0], [0, 2]], float), np.array([[1, 0], [1, 1]], float)]
rmin = min(max(abs(np.linalg.eigvals(P_))) for P_ in pols)
p2 = np.array([1.0, 1 + np.sqrt(2)]); tang2 = float(p2 @ Phi2(p2))/float(p2 @ p2)
A2 = np.array([[0.5, 0.5], [0.5, 1.5]]); ok24 = abs(rmin - 1) <= 1e-12 and abs(tang2 - (1 + np.sqrt(2)/4)) <= 1e-12 and np.allclose(A2 @ p2, (1 + 1/np.sqrt(2))*p2)
check("S24 Proposition 12.48 (minimality alone is not enough: 2x2 counterexample)", ok24, f"min rho = {rmin:.12f}, tangent = {tang2:.12f}")

ok25 = True; det25 = []
for g in (0.5, 0.8, 0.9):
    ellv = {}
    c = None
    for k in range(2, 10):
        Bk = kl_build(k); c0 = Bk['live'].astype(float)
        lam, vk = kl_perron(Bk, g, c0); ellv[k] = lift_loss(vk, k)
    for k in range(2, 9):
        rv = ellv[k+1]/ellv[k]; rm = lift_loss(MUS[k+1], k+1)/lift_loss(MUS[k], k)
        ok25 &= rv <= rm + 1e-12
    det25.append(f"gamma={g}: v ratios {[round(ellv[k+1]/ellv[k], 3) for k in range(2, 9)]}")
check("S25 per-level decay of the KL lift loss vs the Syracuse law", ok25, "; ".join(det25))

# --- Proposition 12.50: misalignment along A(x) = 4x+1 ---
ok26 = True; det26 = []
for g in (0.9, 1.0):
    a_, b_ = 2.0**(-g), 1.5**g
    for k in (5, 6, 7):
        Bk = kl_build(k); rk, vv = kl_perron(Bk, g, Bk['live'].astype(float)); Mk = 3**k
        B1 = kl_build(k+1); cl = vv[np.arange(3**(k+1)) % Mk]
        gg = np.maximum(kl_phi(B1, cl, g) - rk*cl, 0.0)
        rk1, v1 = kl_perron(B1, g, cl); li = B1['lifts']; pol = li[np.arange(3**(k+1)), v1[li].argmin(1)]
        rho_, uu = kl_left(B1, pol, g)
        G = float(uu @ gg)/float(uu @ cl); U = uu.reshape(3, Mk).sum(0)
        Tv = vv.reshape(3, Mk//3); delta = (Tv - Tv.min(0)).reshape(-1)
        yy = np.arange(Mk, dtype=np.int64); Aidx = (4*yy + 1) % Mk; oddk = (yy % 3 == 2); qk = ((2*yy - 1)//3) % (Mk//3)
        Lk = np.stack([(qk + j*(Mk//3)) % Mk for j in range(3)], axis=1)
        fr = {}
        for W in (1, 2, 3, 4, 6):
            S_ = np.zeros(Mk); cur = yy.copy()
            for i in range(W): S_ += delta[cur]; cur = Aidx[cur]
            mW = np.where(oddk, b_*S_[Lk].min(1), 0.0)
            BW = ((a_/rho_)**(2*(W-1))/W)*float((U*mW).sum())/float(uu @ cl)
            fr[W] = float(np.mean(mW[oddk] <= 1e-12*b_*vv[oddk].max()))
            if W <= 4: ok26 &= BW <= G*(1 + 1e-9)
            if W == 2: ok26 &= 0.08 <= BW/G <= 0.20; b2 = BW/G
        ok26 &= 0.74 <= fr[2] <= 0.83 and 0.27 <= fr[3] <= 0.38 and fr[6] <= 0.05
        det26.append(f"g={g},k={k}: B2/G={b2:.3f}, aligned W=2,3,4,6: {fr[2]:.3f},{fr[3]:.3f},{fr[4]:.3f},{fr[6]:.3f}")
check("S26 Proposition 12.50 (misalignment bound and alignment persistence)", ok26, "; ".join(det26))

# --- Proposition 12.52: the occupation below the top digit is adversary-free ---
ok27 = True; worst27 = 0.0; rng27 = np.random.default_rng(3)
for g in (0.9, 1.0):
    a_, b_ = 2.0**(-g), 1.5**g; k = 5
    B1 = kl_build(k+1); M1 = 3**(k+1); li = B1['lifts']
    _, v1 = kl_perron(B1, g, B1['live'].astype(float))
    for pol in (li[np.arange(M1), v1[li].argmin(1)], li[np.arange(M1), rng27.integers(0, 3, M1)], li[np.arange(M1), v1[li].argmax(1)]):
        rho_, uu = kl_left(B1, pol, g)
        for j in range(1, k+1):
            Mj = 3**j; uj = uu.reshape(-1, Mj).sum(0); uj1 = uu.reshape(-1, 3*Mj).sum(0)
            s_ = np.arange(Mj, dtype=np.int64); live_ = s_ % 3 != 0
            Ts = ((3*s_ + 1)*pow(2, -1, 3*Mj)) % (3*Mj)
            err = np.abs(rho_*uj - (a_*uj[(s_*pow(2, -1, Mj)) % Mj] + b_*uj1[Ts]))[live_].max()/uj[live_].max()
            worst27 = max(worst27, err)
ok27 = worst27 <= 1e-11
check("S27 Proposition 12.52 (adversary-free marginal hierarchy)", ok27, f"max relative error {worst27:.1e} over 3 policies x 2 exponents x 5 levels")

# --- Section 12.15: the gain on live rows (Argon), the summed form and the fence ---
def live_setup(g, k):
    Bk = kl_build(k); Mk = 3**k; K1 = Mk//3
    rk, vv = kl_perron(Bk, g, Bk['live'].astype(float))
    Tv = vv.reshape(3, K1); delta = (Tv - Tv.min(0)).reshape(-1)
    yy = np.arange(Mk, dtype=np.int64); Aidx = (4*yy + 1) % Mk
    qk = ((2*yy - 1)//3) % K1; Lk = np.stack([(qk + j*K1) % Mk for j in range(3)], axis=1)
    return Bk, Mk, K1, rk, vv, delta, yy, Aidx, Lk
def m_window(W, delta, yy, Aidx, Lk, b_):
    S_ = np.zeros(len(yy)); cur = yy.copy()
    for i in range(W): S_ += delta[cur]; cur = Aidx[cur]
    return np.where(yy % 3 == 2, b_*S_[Lk].min(1), 0.0)
ok28 = ok29 = ok30 = ok31 = True; det28 = []; det30 = []; det31 = []; negratio = {}
rng28 = np.random.default_rng(1215)
for g in (0.9, 1.0):
    a_, b_ = 2.0**(-g), 1.5**g
    for k in (5, 6, 7):
        Bk, Mk, K1, rk, vv, delta, yy, Aidx, Lk = live_setup(g, k)
        tol = 1e-12*vv.max(); oddk = yy % 3 == 2
        m2 = m_window(2, delta, yy, Aidx, Lk, b_); m3 = m_window(3, delta, yy, Aidx, Lk, b_)
        s2, s5, s8 = oddk & (yy % 9 == 2), oddk & (yy % 9 == 5), oddk & (yy % 9 == 8)
        al = m2 <= tol; p = float(al[s2].mean())
        ok28 &= bool(al[s5].all() and al[s8].all()) and abs(float(al[oddk].mean()) - (2/3 + p/3)) <= 1e-12 and 0.25 <= p <= 0.47
        ok28 &= np.abs(m3[s2] - m2[s2]).max() <= tol and np.abs(m3[s5] - m2[(4*yy[s5]) % Mk]).max() <= tol
        det28.append(f"g={g},k={k}: p={p:.3f}, W=3 on x0=8: {float((m3 <= tol)[s8].mean()):.3f}")
        # S29: Proposition 12.55
        alpha = a_/rk; one = yy % 3 == 1
        ok29 &= np.abs(delta[one] - alpha*delta[(2*yy[one]) % Mk]).max() <= 1e-10*delta.max()
        x0 = yy[s2]; t0 = ((2*x0 - 1)//3) % K1; z1 = (2*t0) % K1; z2 = (4*t0 + 1) % K1
        cc = (2*t0 >= K1).astype(np.int64); qq = (4*t0)//K1
        form = b_*np.min(np.stack([alpha*delta[z1 + ((cc - i) % 3)*K1] + delta[z2 + ((qq + i) % 3)*K1] for i in range(3)]), axis=0)
        ok29 &= np.abs(form - m2[s2]).max() <= 1e-10*vv.max()
        # S30-S31: level k+1 policies
        B1 = kl_build(k+1); M1 = 3**(k+1); cl = vv[np.arange(M1) % Mk]; li = B1['lifts']
        gg = np.maximum(kl_phi(B1, cl, g) - rk*cl, 0.0)
        _, v1 = kl_perron(B1, g, cl)
        pols = {'min': li[np.arange(M1), v1[li].argmin(1)], 'rand': li[np.arange(M1), rng28.integers(0, 3, M1)],
                'max': li[np.arange(M1), v1[li].argmax(1)]}
        live = yy % 3 != 0; inv2 = pow(2, -1, Mk); rs = ((3*yy + 1)*pow(2, -1, M1)) % M1
        for name, pol in pols.items():
            rho, uu = kl_left(B1, pol, g); U = uu.reshape(3, Mk).sum(0)
            if name in ('min', 'rand'):
                lhs = b_*uu[rs]; rhs = rho*U - a_*U[(yy*inv2) % Mk]
                ok30 &= np.abs(lhs - rhs)[live].max() <= 1e-10*U.max()
                h = rho*delta - a_*delta[(2*yy) % Mk]
                ok30 &= abs(float(uu @ gg) - float(U @ h)) <= 1e-9*float(uu @ gg)
                if name == 'min':
                    neg = live & (h < -1e-14*np.abs(h).max()); fneg = float(neg.sum()/live.sum())
                    ok30 &= 0.07 <= fneg <= 0.12
                    negratio[(g, k)] = float(-h[neg].sum()/h[h > 0].sum())
                    det30.append(f"g={g},k={k}: h<0 on {fneg:.3f}, neg/pos {negratio[(g, k)]:.3f}, U on h<0 {float(U[neg].sum()):.3f}")
            al_ = a_/rho
            for j in (1, 2, 3):
                Mj = 3**j; uj = uu.reshape(-1, Mj).sum(0)/uu.sum(); sj = np.arange(Mj)
                bound = 1.0/sum(al_**(-d) for d in range(2*3**(j-1)))
                ok31 &= bool((uj[sj % 3 != 0] >= bound*(1 - 1e-12)).all())
            if name == 'min':
                U9 = (uu.reshape(-1, 9).sum(0)/uu.sum())[np.array([1, 2, 4, 5, 7, 8])]
                ok31 &= bool(((U9 >= 0.10) & (U9 <= 0.20)).all())
                det31.append(f"g={g},k={k}: U(mod 9) in [{U9.min():.3f},{U9.max():.3f}], bound {1.0/sum(al_**(-d) for d in range(6)):.4f}")
    for k in (5, 6):
        ok30 &= negratio[(g, k+1)] < negratio[(g, k)]
for g in (0.9, 1.0):
    a_ = 2.0**(-g)
    for k in (3, 4):
        Bk, Mk, K1, rk, vv, delta, yy, Aidx, Lk = live_setup(g, k)
        B1 = kl_build(k+1); M1 = 3**(k+1); cl = vv[np.arange(M1) % Mk]; li = B1['lifts']
        _, v1 = kl_perron(B1, g, cl); rho, _ = kl_left(B1, li[np.arange(M1), v1[li].argmin(1)], g)
        al_ = a_/rho; Lu = 2*3**(k-1); h = rho*delta - a_*delta[(2*yy) % Mk]
        t = int(next(y for y in yy if y % 3 != 0 and delta[y] <= 1e-15*delta.max()))
        Ut = np.zeros(Mk); x = t
        for d in range(Lu): Ut[x] = al_**d; x = (2*x) % Mk
        live = yy % 3 != 0
        ok31 &= bool((Ut[live] > 0).all()) and bool(((Ut[(2*yy) % Mk] - al_*Ut)[live] >= -1e-12*Ut.max()).all())
        ok31 &= abs(float(Ut @ h)) <= 1e-12*float(Ut @ np.abs(h))
check("S28 Proposition 12.54 (dead targets; live rows carry all W=2 misalignment)", ok28, "; ".join(det28))
check("S29 Proposition 12.55 (doubling lock and opposite orientations on live rows)", ok29, "identities hold on k=5,6,7, gamma in {0.9,1}")
check("S30 Proposition 12.56 (the gain is a pairing with the coarse occupation)", ok30, "; ".join(det30))
check("S31 Proposition 12.57 (low digits occupied for free; the doubling cone has zero-gain vectors)", ok31, "; ".join(det31))

npass = sum(r_['pass'] for r_ in rows)
print(f"\n{npass}/{len(rows)} passed")
(HERE / "cert_syracuse_law_results.json").write_text(json.dumps({"rows": rows, "stats": {str(k): v for k, v in stats.items()}}, indent=2, default=float))
sys.exit(0 if npass == len(rows) else 1)
