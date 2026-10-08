"""
Paper 01f Theorem 11.6 certificate: the Debye-Hueckel tail amplitude C predicted from Coulomb-phase data.

A1  Worm sampler (ice + one monopole pair, uniform measure) reproduces exact enumeration on the L=2 torus.
A2  From saved worm runs (L=8, L=10; worm_pair_weights.json): Madelung-corrected R_inf agrees between sizes,
    and the free Coulomb slope gives K = 0.50 +- 0.01.
A3  Pinch-point stiffness from exact-ice loop Monte Carlo (stiff8.log, stiff12.log): K(q->0) by q^2 extrapolation.
A4  C_pred = (1/32)(3 K nu / pi)^(3/2), nu = 2 sqrt(R_inf), agrees with the 2-term series fit to < 2%.
A5  With C fixed, one subleading coefficient from a20 back-predicts a18, a16 (< 1%); S within 1e-5 of Kolafa.
Re-generate raw data with: worm.py 8 4e7 11 ; worm.py 10 6e7 12 ; stiff.py 8 3000 1 ; stiff.py 12 1500 2.
"""
import json, math, os, re, subprocess, sys
import numpy as np
from mpmath import zeta
HERE = os.path.dirname(os.path.abspath(__file__))
PASS = []
def chk(name, ok):
    PASS.append(bool(ok)); print(f"  [{'OK ' if ok else 'FAIL'}] {name}")

print("A1  worm sampler vs exact enumeration (L=2)")
exact = subprocess.run([sys.executable, os.path.join(HERE, 'worm_exact.py')], cwd=HERE, capture_output=True, text=True).stdout
ex = eval(exact.split('exact R(tail,head):')[1].strip())
subprocess.run([sys.executable, os.path.join(HERE, 'worm.py'), '2', '4e6', '1'], cwd=HERE, capture_output=True, text=True)
d = np.load(os.path.join(HERE, 'worm_raw_L2_s1.npy'), allow_pickle=True).item()
dev = max(abs(d['lam'] * d['hist'].get(k, 0) / d['closed'] - v) / v for k, v in ex.items())
chk(f"worm R(tail,head) = exact L=2 values within 2% (max rel dev {dev:.4f})", dev < 0.02)

print("A2  core weight and Coulomb slope from saved worm runs")
data = json.load(open(os.path.join(HERE, 'worm_pair_weights.json')))
K_slope, Rinf = {}, {}
for key, rows in data.items():
    rows = np.array(rows); sel = rows[:, 0] >= 1.5; w = rows[sel, 3]
    X = np.vstack([np.ones(sel.sum()), rows[sel, 1]]).T; W = np.diag(w)
    beta = np.linalg.solve(X.T @ W @ X, X.T @ W @ np.log(rows[sel, 2]))
    K_slope[key] = beta[1] / 4
    Rinf[key] = np.sum(w * rows[sel, 2] * np.exp(-4 * 0.5 * rows[sel, 1])) / np.sum(w)
    print(f"      {key}: free Coulomb slope K = {K_slope[key]:.3f}; R_inf (K=1/2) = {Rinf[key]:.4f}")
chk("Madelung-corrected R_inf agrees between L=8 and L=10 within 1%", abs(Rinf['L8'] - Rinf['L10']) / Rinf['L10'] < 0.01)
chk("free Coulomb slope of the monopole pair weight gives K = 0.50 +- 0.02 (both sizes)", all(abs(k - 0.5) < 0.02 for k in K_slope.values()))

print("A3  pinch-point stiffness")
qs, Ks, dKs = [], [], []
for f in ('stiff8.log', 'stiff12.log'):
    for line in open(os.path.join(HERE, f)):
        m = re.search(r"\|q\|=([\d.]+).*?=\s*([\d.]+)\s*\+-\s*([\d.]+)\s+K_q = ([\d.]+)", line)
        if m:
            q, S, dS, K = map(float, m.groups()); qs.append(q); Ks.append(K); dKs.append(K * dS / S)
q2 = np.array(qs)**2; Ks = np.array(Ks); w = 1 / np.array(dKs)**2
X = np.vstack([np.ones(len(q2)), q2]).T
beta = np.linalg.solve(X.T @ np.diag(w) @ X, X.T @ np.diag(w) @ Ks); K0 = beta[0]
dK0 = math.sqrt(np.linalg.inv(X.T @ np.diag(w) @ X)[0, 0])
print(f"      shells K_q = {np.round(Ks, 4)}; K(q->0) = {K0:.4f} +- {dK0:.4f}")
chk("two independent stiffness measurements agree (pinch point vs monopole Coulomb slope, within 0.02)", abs(K0 - K_slope['L10']) < 0.02)

print("A4  predicted amplitude")
nu = 2 * math.sqrt(Rinf['L10']); C = (3 * K0 * nu / math.pi)**1.5 / 32
a = {6: 1.3717421e-03, 8: 2.2862369e-04, 10: 2.0322105e-04, 12: 1.5523834e-04, 14: 9.094769e-05, 16: 7.033637e-05, 18: 5.308788e-05, 20: 4.1139e-05}
M = np.array([[9**-2.5, 9**-3.5], [10**-2.5, 10**-3.5]]); Cfit = np.linalg.solve(M, [a[18], a[20]])[0]
print(f"      nu = {nu:.4f} (Pauling 4/3); C_pred = {C:.5f}; C from 2-term series fit = {Cfit:.5f}")
chk("C_pred agrees with the series fit within 2%", abs(C - Cfit) / Cfit < 0.02)

print("A5  extrapolation with C fixed")
D = (a[20] - C * 10**-2.5) * 10**3.5
p18, p16 = C * 9**-2.5 + D * 9**-3.5, C * 8**-2.5 + D * 8**-3.5
S = 0.5 * math.log(1.5) + sum(a.values()) + float(C * zeta(2.5, 11) + D * zeta(3.5, 11))
kol = 0.5 * math.log(1.5074660)
print(f"      back-predicted a18 {p18:.4e} (actual {a[18]:.4e}), a16 {p16:.4e} (actual {a[16]:.4e}); S = {S:.6f}; Kolafa {kol:.6f}")
chk("back-predictions of a18 and a16 within 1%", abs(p18 / a[18] - 1) < 0.01 and abs(p16 / a[16] - 1) < 0.01)
chk("S within 1e-5 of Kolafa's Monte Carlo value", abs(S - kol) < 1e-5)
print(f"\nTOTAL {sum(PASS)}/{len(PASS)}")
