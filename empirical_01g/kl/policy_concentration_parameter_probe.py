"""Exploratory float64 policy concentration and labelled-edge entropy.

Not a rigorous interval certificate or an asymptotic test.
"""
import json
from pathlib import Path
import numpy as np
from scipy.sparse import coo_matrix
from visibility_potential_probe import build, eigen


def law(k):
    previous = np.ones(1)
    for n in range(1, k+1):
        m = 3**n
        orbit = np.empty(2*m//3, dtype=int)
        orbit[0] = 1
        for j in range(1, len(orbit)):
            orbit[j] = 2*orbit[j-1] % m
        forcing = np.zeros(m)
        forcing[1::3] = previous
        f = forcing[orbit]
        g = np.zeros(len(orbit))
        g[-1] = sum(np.ldexp(f[(len(orbit)-1+a) % len(orbit)], -a)
                    for a in range(1, min(len(orbit), 1074)+1))
        g[-1] /= 1-2.**(-len(orbit))
        for j in range(len(orbit)-2, -1, -1):
            g[j] = (g[j+1]+f[j+1])/2
        previous = np.zeros(m)
        previous[orbit] = g
    return previous


def probe(k, gamma, mu):
    rho, fullx = eigen(k, gamma)
    r, dbl, lifts = build(k)
    live = r[r % 3 != 0]
    index = np.full(len(r), -1)
    index[live] = np.arange(len(live))
    alpha, beta = 2.**(-gamma), 1.5**gamma
    chosen = lifts[np.arange(len(r)), np.argmin(fullx[lifts], axis=1)]
    rows, cols, weights, odd_labels = [], [], [], []
    for i, s in enumerate(live):
        rows.append(i); cols.append(index[dbl[s]])
        weights.append(alpha); odd_labels.append(0)
        if s % 3 == 2 and chosen[s] % 3 != 0:
            rows.append(i); cols.append(index[chosen[s]])
            weights.append(beta); odd_labels.append(1)
    rows, cols = np.array(rows), np.array(cols)
    weights, odd_labels = np.array(weights), np.array(odd_labels)
    matrix = coo_matrix((weights, (rows, cols)), shape=(len(live), len(live))).tocsr()
    u = np.ones(len(live))/len(live)
    for iteration in range(100000):
        nxt = matrix.T @ u
        nxt /= nxt.sum()
        if np.max(abs(nxt-u)) < 1e-14 * max(nxt):
            u = nxt
            break
        u = nxt
    else:
        raise RuntimeError('Left iteration did not converge')
    x, p = fullx[live], mu[live]
    density = u/(u @ p)
    q = density*p
    relative_entropy = np.sum(q*np.log(density))
    pi = u*x/(u @ x)
    edge_prob = weights*x[cols]/(rho*x[rows])
    entropy = -np.sum(pi[rows]*edge_prob*np.log(edge_prob))
    theta = np.sum(pi[rows]*edge_prob*odd_labels)
    derivative = -np.log(2)+np.log(3)*theta
    identity_error = abs(gamma*derivative-(np.log(rho)-entropy))
    lifted = p[index[(2*live) % len(r)]]/2
    for i,s in enumerate(live):
        if s % 3 == 2:
            lifted[i] += 1.5*mu[lifts[s]].min()
    local_loss = 1-lifted/p
    weighted_loss = q @ local_loss
    mean_loss = p @ local_loss
    # Independent pressure check uses the fixed selected matrix's Perron vectors.
    left_error = np.max(abs(matrix.T @ u-rho*u))/max(u)
    right_error = np.max(abs(matrix @ x-rho*x))/max(x)
    assert max(identity_error, left_error, right_error) < 1e-9
    return dict(k=k, gamma=gamma, rho=rho, concentration_max=float(max(density)),
                relative_entropy_q_mu=float(relative_entropy),
                perron_entropy=float(entropy), odd_edge_frequency=float(theta),
                d_log_rho_d_gamma=float(derivative),
                pressure_identity_error=float(identity_error),
                left_eigen_residual=float(left_error), right_eigen_residual=float(right_error),
                mu_mean_residual=float(mean_loss), policy_weighted_mu_residual=float(weighted_loss),
                mean_residual_note='At gamma=1, 1-rho <= policy_weighted_mu_residual.',
                entropy_bound_at_endpoint=float((5/7)*(relative_entropy+np.log(2))/np.log((5/7)/mean_loss)))


def main():
    results = []
    for k in range(2, 10):
        mu = law(k)
        for gamma in (0.8, 0.9, 1.0):
            result = probe(k, gamma, mu)
            results.append(result)
            print(json.dumps(result), flush=True)
    Path(__file__).with_suffix('.json').write_text(json.dumps(
        dict(status='Exploratory float64; not a proof or interval certificate', results=results), indent=2))


if __name__ == '__main__':
    main()
