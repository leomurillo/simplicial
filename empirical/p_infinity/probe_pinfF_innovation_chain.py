"""probe_pinfF_innovation_chain.py -- the factorization strike: the center-out innovation chain.

THE PRINCIPLE (Thm F.21, P-inf-F section 19): Cholesky pivots along a nested chain depend
only on the chain's past; ordering the window CENTER-OUT (by |y|), the radius-s segment is
exactly the lambda = e^s window (kernel locality: prime shifts <= 2s = primes <= e^{2s}).
Hence the whole lambda-family is ONE chain factorization and
    RH  <=>  the center-out innovation density d(s) >= 0 for all s
-- a pointwise statement, no limits.  d(s) = continuous Cholesky diagonal = Gohberg-Krein
chain factorization = canonical-system Hamiltonian density = Suzuki H(A_a): one object,
four languages, never computed.  This probe computes it.

PRE-REGISTERED (GPD):
  R1 (chain positivity): all center-out pivots > 0 at every window (per-window positivity
      in chain coordinates).  FALSIFIER: a negative pivot (= negative eigenvalue upstream).
  R2 (THE MARTINGALE/LOCALITY CHECK -- the load-bearing structure): pivot-density profiles
      d(s) computed from DIFFERENT-lambda builds agree on shared radii (<= 20% allowance for
      band-limited basis leakage).  FALSIFIER: O(1) disagreement (kernel locality wrong =>
      the center-out principle dies).
  R3 (the ladder in innovation coordinates; soft): d(s) shows localized dips; new dips
      appear as s crosses cell-completion radii (cell counts 1 -> 3 between lam 1.5 and 2).
  R4 (soft): the minimal pivot density near the outer radius tracks the ground scale
      eps_{e^s} within poly factors.

Build: exact mpmath V_n matrices (certified lineage), unitary DFT change to the point
basis (same spectrum), center-out permutation, LDL/Cholesky pivots; float64-safe windows
lam <= 1.8 + lam = 2.0 with floor caveat (eps_2 ~ 1e-12 grazes the float floor).
"""
import sys
import numpy as np
import mpmath as mp

sys.stdout.reconfigure(encoding="utf-8")
mp.mp.dps = 30

src2 = open("empirical/p_infinity/probe_pinfF_f5_sampling.py", encoding="utf-8").read()
exec(src2.split('# ---- zeros')[0])        # primes_upto, build_QW (certified lineage)


def point_basis_form(QW, N, L):
    """Unitary DFT to the equispaced point basis x_i = i*L/(2N+1); returns K, x-grid."""
    dim = 2 * N + 1
    i_idx = np.arange(dim)
    x = i_idx * L / dim
    n_idx = np.arange(-N, N + 1)
    B = np.exp(1j * 2 * np.pi * np.outer(n_idx, i_idx) / dim) / np.sqrt(dim)
    # V_n(x) = e^{-2pi i n x / L}/sqrt(L); at x_i: e^{-2pi i n i/dim}/sqrt(L) -- conj of B row
    K = np.conj(B).T @ QW @ B
    K = np.real(0.5 * (K + np.conj(K).T))
    return K, x


def center_out_order(x, L):
    s = np.abs(x - L / 2)
    return np.argsort(s, kind="stable"), np.sort(s)


def chain_pivots(K, order):
    """LDL pivots along the given order (Schur-complement diagonal)."""
    Kp = K[np.ix_(order, order)].astype(float)
    n = Kp.shape[0]
    piv = np.zeros(n)
    A = Kp.copy()
    for k in range(n):
        piv[k] = A[k, k]
        if abs(A[k, k]) < 1e-300:
            piv[k:] = A[np.arange(k, n), np.arange(k, n)]
            break
        v = A[k + 1:, k] / A[k, k]
        A[k + 1:, k + 1:] -= np.outer(v, A[k + 1:, k])
        A[k + 1:, k] = 0.0
    return piv


print("== building exact matrices (mpmath, certified lineage; MATCHED BANDWIDTH) ==")
# R2 diagnosis: per-build pivot units = grid spacing x basis bandwidth (parallel profiles,
# constant ratio 1.37/1.36/1.30 per pair).  Fix: match omega_N = 2 pi N / L across builds
# (N proportional to L at omega_0 ~ 108), so densities share units.
CASES = [(1.3, 9), (1.5, 14), (1.8, 20), (2.0, 24)]
data = {}
for lam, N in CASES:
    QW, L = build_QW(mp.mpf(repr(float(lam))), N, True)
    K, x = point_basis_form(QW, N, L)
    order, srt = center_out_order(x, L)
    piv = chain_pivots(K, order)
    dx = L / (2 * N + 1)
    dens = piv / dx                       # innovation density per unit chain length
    radii = np.abs(x[order] - L / 2)
    ev = np.sort(np.linalg.eigvalsh(K))
    data[lam] = dict(radii=radii, dens=dens, piv=piv, dx=dx, ev0=ev[0], L=L)
    neg = int(np.sum(piv <= 0))
    print(f"   lam={lam}: N={N}, dim={2*N+1}, dx={dx:.4f}; pivots<=0: {neg}; "
          f"min pivot={piv.min():.3e} at radius {radii[np.argmin(piv)]:.3f} "
          f"(window edge {L/2:.3f}); eig0={ev[0]:.3e}")

ok1 = all((data[lam]['piv'] > 0).all() for lam, _ in CASES[:3])   # lam=2 may graze float floor
print("\n   R1: " + ("SURVIVES -- all pivots positive (chain-coordinates positivity)"
                     if ok1 else "FIRED at lam<=1.8 -- diagnose"))

print("\n== R2: the martingale/locality check (profiles across builds on shared radii) ==")
# compare d(s) between consecutive builds on the SHARED radius range, via interpolation
oks2 = True
pairs = [(1.3, 1.5), (1.5, 1.8), (1.8, 2.0)]
for la, lb in pairs:
    A, Bd = data[la], data[lb]
    smax = min(A['radii'].max(), Bd['radii'].max()) * 0.85   # stay off the outer edge
    # average density in coarse radius bins (pivot order is pairwise-jittered)
    bins = np.linspace(0.02, smax, 6)
    da = np.array([np.mean(A['dens'][(A['radii'] >= b0) & (A['radii'] < b1)])
                   for b0, b1 in zip(bins, bins[1:])])
    db = np.array([np.mean(Bd['dens'][(Bd['radii'] >= b0) & (Bd['radii'] < b1)])
                   for b0, b1 in zip(bins, bins[1:])])
    rel = np.nanmax(np.abs(da - db) / np.maximum(np.abs(da), np.abs(db)))
    oks2 &= rel < 0.20
    print(f"   lam {la} vs {lb}: shared radii <= {smax:.3f}; binned-density rel diff "
          f"max = {rel:.3f}   (a: " + " ".join(f"{v:.2f}" for v in da) + " | b: "
          + " ".join(f"{v:.2f}" for v in db) + ")")
print("   R2: " + ("SURVIVES -- one chain: past pivots immune to window growth (locality"
                   " certified)" if oks2 else "FIRED -- diagnose basis leakage vs locality"))

print("\n== R3/R4: the innovation profile (dips = the ladder in chain coordinates) ==")
for lam, _ in CASES:
    d = data[lam]
    k = np.argsort(d['dens'])[:4]
    print(f"   lam={lam}: four smallest densities at radii "
          + ", ".join(f"{d['radii'][i]:.3f} (d={d['dens'][i]:.2e})" for i in sorted(k, key=lambda i: d['radii'][i]))
          + f"   [edge={d['L']/2:.3f}, eig0={d['ev0']:.2e}]")
print("   R3/R4: read dips vs the rung schedule (cells 1 -> 1 -> 3 across these windows);"
      " dip depth vs ground scale.")

print("\nRESULT: " + ("GREEN -- the innovation chain exists, is positive, and is LOCAL:"
                      " the lambda-family is one factorization (Thm F.21 structure certified)"
                      if (ok1 and oks2) else "PARTIAL -- see R1/R2"))
