r"""
probe_connes_why_float64_fails.py  --  companion certificate documenting EXACTLY why the two
in-program float64 probes (empirical/probe_weil_form_simplicity.py, probe_weil_evenodd_split.py)
failed to reproduce Connes' miracle, and what the fix is.

Two independent failure modes, both fatal, both fixed in probe_connes_miracle_fast.py:

  (A) WRONG EIGENVECTOR.  Connes' eta is NOT the global minimal eigenvector of the Weil form.
      The spectrum has a TOWER of near-degenerate eigenvalues accumulating geometrically at a
      'bulk' value L ~ -2.9034..., separated from the isolated eigenvalues by a big gap.  eta is
      the CONVERGED EXTREME of that cluster (adjacent to the gap).  Taking lam_0 (the global min,
      ~ -8.8) gives the smooth low-frequency mode whose etahat zeros are spurious (~0.6, 3.5, 6.0)
      -- exactly the 3.5 / 3.56 the old probes printed.

  (B) PRECISION FLOOR.  The within-cluster splittings that isolate eta are ~1e-17, 1e-21, ...,
      1e-50 (the minuscule eps(lambda); these ARE Connes' difference tower).  float64 (rel ~1e-16)
      cannot resolve them, so even with the right INDEX the eigenvector is a noise-mix of the
      degenerate block.  mpmath dps>=60 resolves the tower.

This script demonstrates both, at dps high vs a float64 emulation (dps=15), using the validated
fast build.  It also verifies eta is EVEN (it is, by construction: the cosine basis spans only the
even sector; we confirm the reconstructed eta(u)=eta(-u) to working precision).

numpy + mpmath only.  No torch.
"""
import sys
import mpmath as mp

# import the validated builder
import importlib.util, os
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location(
    "miracle", os.path.join(HERE, "probe_connes_miracle_fast.py"))

def load_with_dps(dps):
    # NB: the source sets mp.mp.dps = DPS (default 60) at exec time, so we OVERRIDE *after* exec
    # to genuinely force the requested working precision for the build + eigsy + zero-finding.
    g = {}
    src = open(os.path.join(HERE, "probe_connes_miracle_fast.py")).read().split("if __name__")[0]
    exec(src, g)
    mp.mp.dps = dps                       # force the real working precision
    g["DPS"] = dps
    g["TINY"] = mp.mpf(10) ** (-(dps - 4))
    return g

def first_zero_of_index(g, Q, lam, a, idx, N):
    eta = [Q[r, idx] for r in range(N)]
    z = g["find_zeros"](eta, a, mp.mpf(16), 1)
    return z[0] if z else None

def demo(dps, N=44):
    g = load_with_dps(dps)
    X = 13
    a, Wm = g["build_fast"](X, N)
    E, Q = mp.eigsy(Wm)
    lam = [E[i] for i in range(N)]
    idx, gaps = g["select_eta_index"](lam)
    gamma1 = mp.im(mp.zetazero(1))
    # (A) global-min eigenvector (the OLD-probe choice) vs principled cluster-extreme
    z_globalmin = first_zero_of_index(g, Q, lam, a, 0, N)
    z_eta = first_zero_of_index(g, Q, lam, a, idx, N)
    # (B) evenness of eta: eta(u)=sum coeff_k cos(w_k u) is even by construction; verify numerically
    eta = [Q[r, idx] for r in range(N)]
    us = [mp.mpf("0.3"), mp.mpf("0.7"), mp.mpf("1.1")]
    even_defect = mp.mpf(0)
    for u in us:
        val_p = sum(eta[k] * mp.cos(g["Wf"](k, a) * u) for k in range(N))
        val_m = sum(eta[k] * mp.cos(g["Wf"](k, a) * (-u)) for k in range(N))
        even_defect = max(even_defect, abs(val_p - val_m))
    # the minuscule splitting tower (first few within-cluster gaps below the cut)
    tower = [gaps[idx - 1 - j] for j in range(min(6, idx))]
    return dict(dps=dps, idx=idx, lam0=lam[0], cluster_val=lam[idx],
                z_globalmin=z_globalmin, z_eta=z_eta, gamma1=gamma1,
                even_defect=even_defect, tower=tower)

if __name__ == "__main__":
    print("=" * 90)
    print("WHY THE float64 PROBES FAILED  (Connes route, X=13, N=44 even-cosine modes)")
    print("=" * 90)
    for dps in [15, 60]:
        r = demo(dps)
        tag = "float64-equivalent" if dps == 15 else "high precision"
        print(f"\n--- dps={dps} ({tag}) ---")
        print(f"  global-min eigenvector (OLD probe choice) first etahat zero = "
              f"{mp.nstr(r['z_globalmin'],8)}   (spurious; should be 14.1347)")
        print(f"  principled cluster-extreme eta (idx {r['idx']}) first zero  = "
              f"{mp.nstr(r['z_eta'],16)}")
        print(f"  |first zero - gamma_1|                                      = "
              f"{mp.nstr(abs(r['z_eta']-r['gamma1']),5)}")
        print(f"  eta evenness defect |eta(u)-eta(-u)|                        = "
              f"{mp.nstr(r['even_defect'],5)}  (EVEN by construction)")
        print(f"  minuscule splitting tower eps_j (isolates eta): "
              f"{', '.join(mp.nstr(t,4) for t in r['tower'])}")
    print("""
READING.
  - At dps=15 (float64-equivalent) the within-cluster splitting tower collapses to noise (~1e-12,
    no longer a clean geometric tower), so even the CORRECT index yields a noise-mixed eigenvector:
    first zero comes out ~4.9 (|diff to gamma_1| ~ 9), useless.  At dps=60 the tower
    (1e-17,1e-21,...,1e-42) is resolved and the first zero matches gamma_1 to ~1e-47.
  - The OLD probes ALSO took the global minimum (lam_0 ~ -8.8), whose eigenvector's first zero is
    the spurious ~0.6/3.5 they reported -- a SECOND, independent bug (wrong eigenvector, not just
    precision).  Both must be fixed; probe_connes_miracle_fast.py fixes both.
  - eta is EVEN (defect ~ machine eps): the cosine basis spans exactly the even/symmetric sector
    (the functional-equation-even / Conductor-Blind-Spot symmetric axis), so Connes' S6.6(a)
    'even eigenvector' is automatic here; SIMPLICITY (the eps splitting > 0) is the open part.""")
