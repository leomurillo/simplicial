"""probe_S_limit_multiplicity.py — toward (S)-in-the-limit = mu_lambda -> 0.
EXP1 (window pinning): is the gamma_1 tension window set by ABSOLUTE frequency (pole 1/2-geometry)
or by the ample class H's scale?  Fixed fields D=-8 (g1=3.576, in-window), D=505 (1.771), D=-3 (8.04);
H widths 2/4/6.4.  Pinned => d independent of H-width => zeta's spectrum (g>=14.13) lives forever in
the exponential bulk.  EXP2 (multiplicity = the mu_lambda carrier): zeta multi-channel classes
w_k = avg of k zero-channels (gamma_1..gamma_k), ALL channels probe-constrained; d(eps0) vs k.
Growth with k locates the limit obstruction at spectral multiplicity (the prolate danger);
flat/tiny = strongest finite evidence yet toward mu_lambda -> 0.  Engine: verified chiral module."""
import numpy as np, csv, time, sys
from probe_effectivity_gap_chiral import (engine_data, pair_rows, mk, B_sets, deficit,
                                          build_dicts, SQ2PI, pr)

ZZ = [14.134725, 21.022040, 25.010858, 30.424876, 32.935062, 37.586178,
      40.918719, 43.327073, 48.005151, 49.773832, 52.970321, 56.446248]

def run_cell(eng, wE, wc, HE, Hc, plist, dE):
    Bww = B_sets(wE, wc, wE, wc, eng); BwH = B_sets(wE, wc, HE, Hc, eng); BHH = B_sets(HE, Hc, HE, Hc, eng)
    disc = BwH*BwH - Bww*BHH
    if Bww >= 0 or disc <= 0: return None, Bww
    eps0 = (-BwH + np.sqrt(disc))/BHH
    tw = np.array([float(wc @ pair_rows(wE, pk, *eng)) for pk in plist])
    tH = np.array([float(Hc @ pair_rows(HE, pk, *eng)) for pk in plist])
    M = np.stack([pair_rows(dE, pk, *eng) for pk in plist])
    nrm = np.abs(M).max(axis=1); M = M/nrm[:, None]
    t = (tw + eps0*tH)/nrm
    return float(deficit(M, t)/(np.abs(t).max() + 1e-30)), Bww

def main():
    t0 = time.time()
    DICTS = dict(build_dicts()); dE = DICTS["D6"]
    P1 = [(float(a), 0.20, 0.0) for a in np.linspace(0.3, 3.9, 12)]
    pr("=== EXP1: window pinning — d at fixed gamma_1 vs ample width ===")
    HS = {"H2": np.linspace(-1.0, 1.0, 8), "H4": np.linspace(-2.0, 2.0, 12), "H6": np.linspace(-3.2, 3.2, 16)}
    for D, g1 in [(-8, 3.576), (505, 1.771), (-3, 8.040)]:
        eng = engine_data(D)
        s_w = min(1.0, 4.4/g1)
        wE, wc = mk([(1.4, s_w, g1)]), np.array([1.0])
        line = f"  D={D:>4} g1={g1:.2f}: "
        for hn, grid in HS.items():
            HE, Hc = mk([(float(a), 0.30, 0.0) for a in grid]), np.ones(len(grid))/len(grid)
            d, Bww = run_cell(eng, wE, wc, HE, Hc, P1, dE)
            line += f"{hn}:{'NS' if d is None else f'{d:.2e}'}  "
        pr(line)
    pr("  [pinned => d ~ constant across H-widths; covariant => systematic shift]")

    pr("\n=== EXP2: zeta multi-channel (prolate-like) classes — d(eps0) vs multiplicity k ===")
    eng = engine_data(1)
    HE, Hc = mk([(float(a), 0.30, 0.0) for a in np.linspace(-2.0, 2.0, 12)]), np.ones(12)/12
    rows = []
    for k in (1, 2, 4, 8, 12):
        wE = mk([(1.4, 0.35, ZZ[j]) for j in range(k)])
        wc = np.ones(k)/k
        plist = P1 + [(1.0, 0.35, ZZ[j]) for j in range(k)] + [(2.2, 0.35, ZZ[j]) for j in range(k)]
        d, Bww = run_cell(eng, wE, wc, HE, Hc, plist, dE)
        pr(f"  k={k:>2} (K={len(plist)} probes, all channels constrained): B(w,w)={Bww:+.4f}  "
           f"d(eps0)={'NS' if d is None else f'{d:.3e}'}")
        rows.append(dict(k=k, K=len(plist), Bww=Bww, d=d))
    with open("S_limit_multiplicity.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader()
        for r in rows: w.writerow(r)
    ds = [r['d'] for r in rows if r['d'] is not None]
    if len(ds) >= 3:
        trend = "GROWING (limit obstruction = spectral multiplicity)" if ds[-1] > 3*ds[0] else \
                ("flat/declining (spread classes saturate — strongest finite evidence toward mu_lambda->0)")
        pr(f"\n  VERDICT: d(k): {' -> '.join(f'{d:.1e}' for d in ds)}   => {trend}")
    pr(f"[total {time.time()-t0:.0f}s]")

if __name__ == "__main__":
    main()
