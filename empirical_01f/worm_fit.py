import numpy as np, itertools, math, sys
from scipy.special import erfc
E = np.array([[1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]]) / 4.0
A1 = np.array([E[0] - E[1], E[0] - E[2], E[0] - E[3]])

def ewald_green(L):
    R = L * A1; V = abs(np.linalg.det(R)); Gb = 2 * np.pi * np.linalg.inv(R).T
    eta = math.sqrt(math.pi) / V**(1 / 3)
    rv = [np.array(n) @ R for n in itertools.product(range(-3, 4), repeat=3)]
    gv = [np.array(m) @ Gb for m in itertools.product(range(-8, 9), repeat=3) if any(m)]
    gv = np.array(gv); g2 = np.sum(gv**2, 1); gw = np.exp(-g2 / (4 * eta**2)) / g2 / V
    def G(d):
        s = 0.0
        for r in rv:
            x = np.linalg.norm(d + r)
            if x > 1e-12: s += erfc(eta * x) / (4 * math.pi * x)
        s += np.sum(gw * np.cos(gv @ d)) - 1 / (4 * V * eta**2)
        return s
    # self term xi_L = lim_{r->0} [G(r) - 1/(4 pi r)]
    s = sum(erfc(eta * np.linalg.norm(r)) / (4 * math.pi * np.linalg.norm(r)) for r in rv if np.linalg.norm(r) > 1e-12)
    xi = s + np.sum(gw) - 1 / (4 * V * eta**2) - eta / (2 * math.pi**1.5)
    return G, xi

def analyse(files, dmin):
    rows = []
    for f in files:
        d = np.load(f, allow_pickle=True).item()
        L, lam, nc, closed = d['L'], d['lam'], d['nc'], d['closed']
        G, xi = ewald_green(L)
        for (ttype, dv), c in d['agg'].items():
            dvec = np.array(dv); r = np.linalg.norm(dvec)
            if r < dmin or c < 200: continue
            R = lam * c / (closed * nc)
            # number of tail positions of that type is nc; key aggregates over tails of that type
            rows.append((L, r, G(dvec) - xi, math.log(R), 1 / math.sqrt(c)))
    rows = np.array(rows)
    w = 1 / rows[:, 4]**2
    X = np.vstack([np.ones(len(rows)), rows[:, 2]]).T
    W = np.diag(w)
    beta = np.linalg.solve(X.T @ W @ X, X.T @ W @ rows[:, 3])
    cov = np.linalg.inv(X.T @ W @ X)
    res = rows[:, 3] - X @ beta; chi2 = np.sum(w * res**2) / (len(rows) - 2)
    lnRinf, slope = beta; K = slope / 4
    sd = np.sqrt(np.diag(cov) * max(chi2, 1))
    return dict(K=K, dK=sd[1] / 4, Rinf=math.exp(lnRinf), dRinf=math.exp(lnRinf) * sd[0], n=len(rows), chi2=chi2)

if __name__ == '__main__':
    files = sys.argv[1:]
    for dmin in (0.9, 1.2, 1.5):
        r = analyse(files, dmin)
        nu = 2 * math.sqrt(r['Rinf']); dnu = nu * 0.5 * r['dRinf'] / r['Rinf']
        C = (3 * r['K'] * nu / math.pi)**1.5 / 32
        dC = C * 1.5 * math.hypot(r['dK'] / r['K'], dnu / nu)
        print(f"dmin {dmin}: K = {r['K']:.4f} +- {r['dK']:.4f}   R_inf = {r['Rinf']:.4f} +- {r['dRinf']:.4f}   nu = {nu:.4f}   "
              f"C_pred = {C:.5f} +- {dC:.5f}   (n={r['n']}, chi2/dof={r['chi2']:.2f})")
