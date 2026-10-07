"""

Port Principle — auxiliary check: probes vs interventions (NOT used by PortPrinciple.md).
Exact arithmetic for every decision marked [exact]; floats only in labelled [witness] checks.

PRE-REGISTERED FALSIFIERS (written before the first run; every branch reportable)

SPLIT NOTE (2026-09-29): split verbatim from p5_headline_candidates.py when v3 of PortPrinciple.md was
written. Falsifier text, code, and run logs are preserved unchanged; only this header was added.

H1  PROBES MEASURE TILTS, PATCHING MEASURES TRANSLATIONS (static FDT = Stein).
    For activations x ~ p and a readout f: probe = Sigma^-1 Cov(x,f) = response to an exponential
    TILT of p (thermodynamic push); patch = E[grad f] = response to a TRANSLATION (mechanical push).
    K1a [exact]: 1-D gap(f=x^k) := E[f'] - Cov(x,f)/Var(x) contains ONLY cumulants of order >= 3
         (every monomial has some kappa_j, j>=3), k = 2..6; gap(x^2) = -kappa3/kappa2 exactly.
    K1b [exact]: gap(x^k) = -kappa_{k+1}/kappa2 + (terms in lower cumulants of order >= 3), so
         "probe == patch for every polynomial readout"  <=>  all kappa_{>=3} = 0 (Gaussian).
    K1c [witness]: d=4, Gaussian-mixture activations, random tanh-MLP readout: gap == -E[f (s - s_G)]
         (score identity) within Monte Carlo error; gap ~ 0 when the mixture collapses to a Gaussian;
         |gap| grows with mixture separation.
    L1: any fails.
"""
from fractions import Fraction as F
from itertools import product
import math
import numpy as np
import sympy as sp

res = []
def check(name, ok, detail=""):
    res.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")

# ================================================================ H1
print("== H1 probes measure tilts, patching measures translations ==")
k1, k2, k3, k4, k5, k6, k7 = sp.symbols('kappa1:8')
kap = [k1, k2, k3, k4, k5, k6, k7]
t_ = sp.symbols('t')
K = sum(kap[j] * t_ ** (j + 1) / sp.factorial(j + 1) for j in range(7))
M = sp.series(sp.exp(K), t_, 0, 8).removeO()
mom = [sp.expand(sp.factorial(j) * M.coeff(t_, j)) for j in range(8)]      # mom[j] = E[x^j]
def gap(kpow):
    Ef1 = kpow * mom[kpow - 1]
    probe = (mom[kpow + 1] - mom[1] * mom[kpow]) / k2
    return sp.expand(sp.simplify(Ef1 - probe))
ok_a = sp.simplify(gap(2) + k3 / k2) == 0
high = {k3, k4, k5, k6, k7}
for kp in range(2, 7):
    g = sp.expand(gap(kp) * k2)
    for term in sp.Add.make_args(g):
        if not (term.free_symbols & high): ok_a = False
check("H1.K1a [exact] probe-patch gap for x^k (k=2..6) lives only in cumulants >= 3; gap(x^2) = -kappa3/kappa2", ok_a,
      f"gap(x^3) = {sp.factor(gap(3))}")
ok_b = True
for kp in range(2, 7):
    g = sp.expand(gap(kp) * k2)
    lead = g.coeff(kap[kp])          # coefficient of kappa_{k+1}
    ok_b &= (lead == -1)
    rest = sp.expand(g + kap[kp])
    ok_b &= not (rest.free_symbols & {kap[j] for j in range(kp, 7)})
check("H1.K1b [exact] gap(x^k) = -kappa_{k+1}/kappa2 + lower: probe==patch for all polynomial readouts <=> Gaussian", ok_b)

rng = np.random.default_rng(11)
d, Nmc = 4, 400_000
W1 = rng.normal(size=(8, d)) / np.sqrt(d); b1 = rng.normal(size=8) * 0.3; w2 = rng.normal(size=8)
def f_and_grad(X):
    Hh = np.tanh(X @ W1.T + b1)
    f = Hh @ w2
    g = ((1 - Hh ** 2) * w2) @ W1
    return f, g
Sig0 = np.eye(d) * 0.5 + 0.2
Si0 = np.linalg.inv(Sig0)
def run(sep):
    mu = np.zeros(d); mu[0] = sep; mu[1] = -0.5 * sep
    z = rng.random(Nmc) < 0.3
    L = np.linalg.cholesky(Sig0)
    X = (rng.normal(size=(Nmc, d)) @ L.T) + np.where(z[:, None], mu, -0.3 / 0.7 * mu)
    m1, m2 = mu, -0.3 / 0.7 * mu
    # exact mixture score s(x) = grad log p
    def logN(Xc): return -0.5 * np.einsum('ij,jk,ik->i', Xc, Si0, Xc)
    l1, l2 = np.log(0.3) + logN(X - m1), np.log(0.7) + logN(X - m2)
    mx = np.maximum(l1, l2); r1 = np.exp(l1 - mx); r2 = np.exp(l2 - mx); g1 = r1 / (r1 + r2)
    s = -(g1[:, None] * ((X - m1) @ Si0) + (1 - g1)[:, None] * ((X - m2) @ Si0))
    f, g = f_and_grad(X)
    mean = X.mean(0); Sig = np.cov(X.T)
    probe = np.linalg.solve(Sig, ((X - mean) * (f - f.mean())[:, None]).mean(0))
    patch = g.mean(0)
    sG = -(X - mean) @ np.linalg.inv(Sig)
    formula = -((f - f.mean())[:, None] * (s - sG)).mean(0)
    return patch - probe, formula, np.linalg.norm(patch)
gaps = []
okc = True
for sep in [0.0, 1.0, 2.0, 3.0]:
    gp, fm, npch = run(sep)
    gaps.append(np.linalg.norm(gp) / npch)
    okc &= np.linalg.norm(gp - fm) < 0.02 * npch + 0.01
okc &= gaps[0] < 0.02 and gaps[1] < gaps[2] < gaps[3] and gaps[3] > 0.1
check("H1.K1c [witness] d=4 mixture + MLP: gap == -E[f(s - s_G)]; ~0 when Gaussian; grows with separation", okc,
      f"relative gap by separation 0,1,2,3: {[round(x,4) for x in gaps]}")
# RUN LOG (2026-09-29): K1c FAILS as pre-registered (magnitude clause: gap 2.5% < 10% at sep 3). Diagnosis:
# the small-weight tanh MLP is nearly LINEAR, and for linear f probe == patch under ANY distribution
# (E[x s^T] = E[x s_G^T] = -I). The gap is a PRODUCT: readout curvature x representation non-Gaussianity.
# At a 0.1-2% gap the Monte Carlo identity check is noise-dominated. Retained; superseded by K1d.
# K1d is POST-DIAGNOSIS (not blind): a curved readout f = x0^2 + 0.5 x1 on the same mixtures.
def run_quad(sep):
    mu = np.zeros(d); mu[0] = sep; mu[1] = -0.5 * sep
    z = rng.random(Nmc) < 0.3; L = np.linalg.cholesky(Sig0)
    m1, m2 = mu, -0.3 / 0.7 * mu
    X = (rng.normal(size=(Nmc, d)) @ L.T) + np.where(z[:, None], m1, m2)
    def logN(Xc): return -0.5 * np.einsum('ij,jk,ik->i', Xc, Si0, Xc)
    l1, l2 = np.log(0.3) + logN(X - m1), np.log(0.7) + logN(X - m2)
    mx = np.maximum(l1, l2); r1 = np.exp(l1 - mx); r2 = np.exp(l2 - mx); g1 = r1 / (r1 + r2)
    s = -(g1[:, None] * ((X - m1) @ Si0) + (1 - g1)[:, None] * ((X - m2) @ Si0))
    f = X[:, 0] ** 2 + 0.5 * X[:, 1]; g = np.zeros_like(X); g[:, 0] = 2 * X[:, 0]; g[:, 1] = 0.5
    mean = X.mean(0); Sig = np.cov(X.T)
    probe = np.linalg.solve(Sig, ((X - mean) * (f - f.mean())[:, None]).mean(0))
    patch = g.mean(0); sG = -(X - mean) @ np.linalg.inv(Sig)
    formula = -((f - f.mean())[:, None] * (s - sG)).mean(0)
    gp = patch - probe
    return (np.linalg.norm(gp) / np.linalg.norm(patch), np.linalg.norm(gp - formula) / np.linalg.norm(gp),
            float(probe @ patch / np.linalg.norm(probe) / np.linalg.norm(patch)))
qd = [run_quad(sep) for sep in [1.0, 2.0, 3.0]]
check("H1.K1d [witness, post-diagnosis] curved readout: identity holds (<5%), gap >30%, probe ANTI-aligned with causal effect at sep 3",
      all(r[1] < 0.05 for r in qd) and all(r[0] > 0.3 for r in qd) and qd[-1][2] < 0,
      f"(rel gap, identity err, cos) = {[tuple(round(v,3) for v in r) for r in qd]}")

print(f"\n{sum(res)}/{len(res)} GREEN  (K1c: pre-registered failure retained; superseded by post-diagnosis K1d)")
