"""T8 / prime-crystal conductor probe. Float64 exploration, not a proof.

Run from any directory: python conductor_decomposition.py
Only writes conductor_results/{results.json,metrics.csv,conductor_blocks.csv}.
Saved certificates store c(r) only for r=2 mod 3. Reconstruct r=1 using
lambda*c(r)=2**(-gamma)*c(2r), and independently check the full operator.
Character convention: chi_t(2**j)=exp(2*pi*i*t*j/phi(3**k)).
Uniform probability measure on units is used for every norm and FFT.
"""
import argparse
import csv
import hashlib
import json
import math
from pathlib import Path
import platform
import time

import numpy as np
from scipy.signal import lfilter

HERE = Path(__file__).resolve().parent


def powers_two(k):
    m = 3**k
    g = np.empty(2*m//3, dtype=np.int64)
    g[0] = 1
    for j in range(1, len(g)):
        g[j] = 2*g[j-1] % m
    assert 2*g[-1] % m == 1
    return g


def syracuse_next(previous, g):
    """Geometric circular convolution, without Monte Carlo or long tail cutoff."""
    m = 3*len(previous)
    forcing = np.zeros(m)
    forcing[1::3] = previous
    f = forcing[g]
    length = len(g)
    a = np.arange(1, length+1)
    last = np.sum(np.exp2(-a.astype(float))*f[(length-1+a) % length])
    last /= 1 - 2.0**(-length)
    out = np.empty(length)
    out[-1] = last
    # Backwards recurrence G[j]=.5 F[j+1]+.5 G[j+1].
    out[:-1] = lfilter([0.5], [1, -0.5], f[:0:-1], zi=[0.5*last])[0][::-1]
    mu = np.zeros(m)
    mu[g] = out
    assert abs(mu.sum()-1) < 2e-12
    assert np.max(np.abs(mu.reshape(3, -1).sum(0)-previous)) < 2e-12
    return mu


def operator_data(k):
    m = 3**k
    r = np.arange(m)
    q = ((2*r-1)//3) % (m//3)
    return r, 2*r % m, q


def phi(c, gamma, data, average=False):
    r, dbl, q = data
    triples = c.reshape(3, -1)
    selected = triples.mean(0) if average else triples.min(0)
    return np.where(r % 3 != 0, 2**(-gamma)*c[dbl]
                    + np.where(r % 3 == 2, 1.5**gamma*selected[q], 0), 0)


def eigen(k, gamma, tol=2e-12):
    data = operator_data(k)
    live = data[0] % 3 != 0
    c = live.astype(float)
    c /= c.sum()
    for iteration in range(30000):
        nxt = phi(c, gamma, data)
        lam = nxt.sum()
        nxt /= lam
        if iteration > 20 and np.max(np.abs(nxt[live]/c[live]-1)) < tol:
            residual = np.max(np.abs(phi(nxt, gamma, data)[live]/nxt[live]-lam))
            assert residual < 2e-10
            return nxt, float(lam), iteration+1, float(residual)
        c = nxt
    raise RuntimeError(f'No convergence: k={k}, gamma={gamma}')


def share_top(x, fraction):
    x = np.sort(np.asarray(x))[::-1]
    return float(x[:max(1, math.ceil(len(x)*fraction))].sum()/x.sum())


def fraction_for(x, share):
    x = np.sort(np.asarray(x))[::-1]
    return float((np.searchsorted(np.cumsum(x), share*x.sum())+1)/len(x))


def analyze(c, k, g, family, gamma=None, extra=None):
    m = len(c)
    units = np.arange(m) % 3 != 0
    u = int(units.sum())
    f = c*(u/c.sum())
    triples = f.reshape(3, -1)
    coarse = np.arange(m//3)
    live = coarse % 3 != 0
    avg = triples.mean(0)
    h = triples - avg
    hu = h[:, live]
    l1 = float(np.abs(hu).mean())
    energy = float((hu**2).mean())
    loss_by_context = (avg-triples.min(0))[live]
    loss = float(loss_by_context.mean())
    coeff = np.fft.fft(f[g])/u
    freq = np.arange(u)
    top = freq % 3 != 0
    spectral_energy = float(np.vdot(coeff[top], coeff[top]).real)
    parseval_error = abs(spectral_energy-energy)/max(energy, 1e-300)
    assert parseval_error < 2e-10
    assert loss <= 1.5*l1+2e-12
    assert loss <= math.sqrt(2*energy)+2e-12
    # Full conductor spectrum: t=0 has conductor 1; nonzero t has
    # conductor 3**max(1,k-v_3(t)). The order-two character has conductor 3.
    depth = np.zeros(u, dtype=np.int16)
    nz = freq[1:].copy()
    valuation = np.zeros(u-1, dtype=np.int16)
    mask = nz % 3 == 0
    while mask.any():
        valuation[mask] += 1
        nz[mask] //= 3
        mask = nz % 3 == 0
    depth[1:] = np.maximum(1, k-valuation)
    blocks = []
    for j in range(k+1):
        select = depth == j
        blocks.append(dict(family=family,k=k,gamma=gamma,conductor=3**j,
                           modes=int(select.sum()),energy=float(np.abs(coeff[select]).dot(np.abs(coeff[select])))))
    full_energy = float(np.mean(f[units]**2))
    assert abs(sum(b['energy'] for b in blocks)-full_energy) < 2e-10*full_energy
    # Independent direct character summation and projection on small groups.
    direct_error = 0.0
    projection_error = 0.0
    if k <= 5:
        for t in range(u):
            direct = np.mean(f[g]*np.exp(-2j*np.pi*t*np.arange(u)/u))
            direct_error = max(direct_error, float(abs(direct-coeff[t])))
        topcoeff = np.where(top, coeff, 0)
        projected = np.fft.ifft(topcoeff*u)
        projection_error = float(np.max(np.abs(projected-h.reshape(-1)[g])))
        assert direct_error < 2e-12 and projection_error < 2e-12
    context_abs = np.abs(hu).mean(0)
    context_energy = (hu**2).mean(0)
    depth_input = coarse[live]+1
    depths = np.zeros(len(depth_input), dtype=int)
    mask = depth_input % 3 == 0
    while mask.any():
        depths[mask] += 1
        depth_input[mask] //= 3
        mask = depth_input % 3 == 0
    spatial = []
    for d in range(k):
        s = depths == d
        spatial.append(dict(depth=d,contexts=int(s.sum()),
            l1_share=float(context_abs[s].sum()/context_abs.sum()),
            energy_share=float(context_energy[s].sum()/context_energy.sum()),
            loss_share=float(loss_by_context[s].sum()/loss_by_context.sum())))
    top_power = abs(coeff[top])**2
    top_indices = freq[top][np.argsort(top_power)[-8:][::-1]]
    row = dict(family=family,k=k,gamma=gamma,units=u,lift_loss=loss,l1=l1,
        l2=math.sqrt(energy),top_energy=energy,full_energy=full_energy,
        loss_over_l1=loss/l1,l1_bound=1.5*l1,l2_bound=math.sqrt(2*energy),
        l1_fraction90=fraction_for(context_abs,.9),energy_fraction90=fraction_for(context_energy,.9),
        loss_fraction90=fraction_for(loss_by_context,.9),
        l1_top1pct_share=share_top(context_abs,.01),energy_top1pct_share=share_top(context_energy,.01),
        spectral_top1pct_share=share_top(top_power,.01),
        parseval_relative_error=parseval_error,direct_character_error=direct_error,
        projection_error=projection_error)
    if extra:
        row.update(extra)
    detail=dict(metrics=row,conductor_blocks=blocks,spatial_depth=spatial,
        largest_top_modes=[dict(t=int(t),energy=float(abs(coeff[t])**2)) for t in top_indices])
    print(f'{family:12s} k={k:2d} g={str(gamma):6s} loss={loss:.7f} L1={l1:.7f} L2={math.sqrt(energy):.7f}',flush=True)
    return detail


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--max-k', type=int, default=14)
    parser.add_argument('--fixed-max-k', type=int, default=10)
    parser.add_argument('--endpoint-max-k', type=int, default=14)
    args = parser.parse_args()
    out = HERE/'conductor_results'
    out.mkdir(exist_ok=True)
    start = time.time()
    summary = json.loads((HERE/'kl_cert_summary.json').read_text())
    details = []
    sources = {}
    mu = np.array([1.0])
    for k in range(1,args.max_k+1):
        g = powers_two(k)
        mu = syracuse_next(mu,g)
        if k == 1:
            assert np.max(abs(mu-np.array([0,1/3,2/3]))) < 1e-14
            continue
        if k == 2:
            assert np.max(abs(mu-np.array([0,8,16,0,11,4,0,2,22])/63)) < 1e-14
        data = operator_data(k)
        live = data[0] % 3 != 0
        err = float(np.max(abs(phi(mu,1,data,average=True)[live]/mu[live]-1)))
        assert err < 2e-11
        syr = analyze(mu,k,g,'syracuse',extra={'operator_residual':err})
        details.append(syr)
        if 9 <= k <= 14:
            path = HERE/f'kl_cert_k{k}.npy'
            sources[path.name] = hashlib.sha256(path.read_bytes()).hexdigest()
            principal = np.load(path)
            meta = summary[str(k)]
            gamma = meta['gamma_cert']
            root = meta['eig_at_cert']
            c = np.zeros(3**k)
            c[2::3] = principal
            r1 = np.arange(1,3**k,3)
            c[r1] = 2**(-gamma)/root*c[2*r1 % (3**k)]
            residual = float(np.max(abs(phi(c,gamma,data)[live]/c[live]-root)))
            assert residual < 2e-8, (k,residual)
            principal_ratio = float(principal.reshape(3,-1).min(0).mean()/principal.mean())
            assert abs(principal_ratio-meta['ratio']) < 1e-12
            details.append(analyze(c,k,g,'kl_saved',gamma,
                {'operator_residual':residual,'root':root,'principal_retention':principal_ratio}))
        gammas = (.5,.8,.9,1.) if k <= args.fixed_max_k else ((1.,) if k <= args.endpoint_max_k else ())
        if gammas:
            for gamma in gammas:
                c,root,iterations,residual = eigen(k,gamma)
                details.append(analyze(c,k,g,'kl_fixed',gamma,
                    {'operator_residual':residual,'root':root,'iterations':iterations}))
        for d in details:
            row = d['metrics']
            if row['k'] != k:
                continue
            row['loss_over_syracuse_loss'] = row['lift_loss']/syr['metrics']['lift_loss']
            row['l1_bound_over_syracuse_loss'] = row['l1_bound']/syr['metrics']['lift_loss']
            row['l2_bound_over_syracuse_loss'] = row['l2_bound']/syr['metrics']['lift_loss']
            if row['family'] != 'syracuse':
                defect = 2**(-row['gamma'])+1.5**row['gamma']/3-row['root']
                err = abs(defect-1.5**row['gamma']/3*row['lift_loss'])
                row['deficit_identity_error'] = err
                assert err < 2e-8
    result=dict(description='Exploratory float64 conductor decomposition; no asymptotic or exact-arithmetic claims.',
        args=vars(args),versions=dict(python=platform.python_version(),numpy=np.__version__),
        source_sha256=sources,script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        seconds=time.time()-start,all_checks_passed=True,details=details)
    (out/'results.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    rows=[d['metrics'] for d in details]
    for filename, data_rows in [('metrics.csv',rows),('conductor_blocks.csv',[b for d in details for b in d['conductor_blocks']])]:
        keys = list(dict.fromkeys(key for row in data_rows for key in row))
        with (out/filename).open('w',newline='',encoding='utf-8') as f:
            writer=csv.DictWriter(f,fieldnames=keys)
            writer.writeheader(); writer.writerows(data_rows)
    print(f'All checks passed; {len(details)} vectors; {time.time()-start:.1f}s. Outputs: {out}',flush=True)


if __name__ == '__main__':
    main()
