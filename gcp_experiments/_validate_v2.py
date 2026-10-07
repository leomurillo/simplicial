"""Torch-free validation of the v2 metrics. Safe locally."""
import sys
import numpy as np
import kernel_probe as kp
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass
rng = np.random.default_rng(0)

print("=== centroid on independent feats (should increase toward k) ===")
for k in (2, 3, 4, 5):
    n = 2000
    Z = rng.standard_normal((n, k + 1)) + 0.5 * rng.standard_t(3, size=(n, k + 1))
    y = np.prod(np.sign(Z[:, :k]), axis=1)
    acc = {0: 0.5}
    for m in (1, 2, 3, 4, 5):
        acc[m] = kp.cv_metric(Z, y, m, "clf", lam=1e-4, n_splits=3)
    dacc = np.array([max(0.0, acc[m] - acc[m - 1]) for m in (1, 2, 3, 4, 5)])
    c = float(np.sum(np.array([1, 2, 3, 4, 5]) * dacc) / dacc.sum())
    print(f"  k={k}: centroid={c:.2f}  acc={ {m: round(acc[m],3) for m in (1,2,3,4,5)} }")

print("=== RBF vs poly2 (dark = rbf-poly2; ~0 for linear, >0 for order-3) ===")
n, d = 2000, 6
X = rng.standard_normal((n, d))
y_lin = X @ rng.standard_normal(d) + 0.3 * rng.standard_normal(n)
y_o3 = X[:, 0] * X[:, 1] * X[:, 2] + 0.3 * rng.standard_normal(n)
Xs = (X - X.mean(0)) / X.std(0)
g = kp.median_gamma(Xs)
for name, yy in [("linear", y_lin), ("order3", y_o3)]:
    p1 = kp.cv_reg_best(Xs, yy, lambda A, B: kp.poly_gram(kp.unit_normalize(A), kp.unit_normalize(B), 1))
    p2 = kp.cv_reg_best(Xs, yy, lambda A, B: kp.poly_gram(kp.unit_normalize(A), kp.unit_normalize(B), 2))
    rbf = kp.cv_reg_best(Xs, yy, lambda A, B: kp.rbf_gram(A, B, g))
    print(f"  {name}: poly1={p1:.3f} poly2={p2:.3f} rbf={rbf:.3f} dark={rbf-p2:+.3f}")
