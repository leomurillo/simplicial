"""probe_gamma1_ladder.py — two-variable (gamma_1, resonance-offset) ladder into the Siegel regime.
Tests Prop C.3 (Bochner forced-harmonic obstruction) + maps d(eps0) as gamma_1 -> small.
Self-similar targets s=min(1, 4.4/gamma_1); harmonic probes at 2*gamma_1; regression at the end.
Engine imported from probe_effectivity_gap_chiral (verified, both parities)."""
import numpy as np, csv, time, sys, math
from multiprocessing import Pool
from probe_effectivity_gap_chiral import (engine_data, pair_rows, mk, B_sets, deficit,
                                          build_dicts, RG, SQ2PI, pr)

ZETA_Z = [14.134725, 21.022040, 25.010858, 30.424876, 32.935062, 37.586178]

def harvest(args):
    D, = args
    try:
        import cypari2
        p = cypari2.Pari()
        Z = p.lfunzeros(p.lfuncreate(int(D)), 19)
        zz = sorted(float(p.real(z)) for z in Z if float(p.real(z)) > 0.05)
        if not zz: return None
        g1 = zz[0]
        union = sorted(zz + ZETA_Z)
        off = min(abs(2*g1 - g) for g in union if abs(g - g1) > 1e-6)
        return (D, g1, zz[1] if len(zz) > 1 else None, off)
    except Exception:
        return None

def is_fund(D):
    if D in (0, 1) or D == -1: return False
    m = D if D % 4 == 1 else (D//4 if D % 4 == 0 else None)
    if m is None: return False
    mm = abs(m); d = 2
    while d*d <= mm:
        if mm % (d*d) == 0: return False
        d += 1
    if D % 4 == 0 and (m % 4 not in (2, 3)): return False
    return True

def measure(arg):
    D, g1, g2, off = arg
    try:
        eng = engine_data(D)
        s_w = min(1.0, 4.4/g1)
        wE, wc = mk([(1.4, s_w, g1)]), np.array([1.0])
        HE, Hc = mk([(float(a), 0.30, 0.0) for a in np.linspace(-2.0, 2.0, 12)]), np.ones(12)/12
        Bww = B_sets(wE, wc, wE, wc, eng); BwH = B_sets(wE, wc, HE, Hc, eng); BHH = B_sets(HE, Hc, HE, Hc, eng)
        disc = BwH*BwH - Bww*BHH
        if Bww >= 0 or disc <= 0:
            return dict(D=D, g1=g1, off=off, s=s_w, sg1=s_w*g1, note="not spacelike", q2=np.nan,
                        d_D4=np.nan, d_D6=np.nan, d_D6_harm=np.nan, eps0=np.nan)
        eps0 = (-BwH + np.sqrt(disc))/BHH
        # q^2 = |v_hat(g1)|^2/(v0 v1) for v = w + eps0 H  (closed forms)
        def mval(a, s, w, z):
            return np.exp(z*a)*(s*SQ2PI/2)*(np.exp(s**2*(z + 1j*w)**2/2) + np.exp(s**2*(z - 1j*w)**2/2))
        vg = mval(1.4, s_w, g1, 1j*g1) + eps0*sum(mval(float(a), 0.30, 0.0, 1j*g1) for a in np.linspace(-2, 2, 12))/12
        v0 = mval(1.4, s_w, g1, -0.5) + eps0*sum(mval(float(a), 0.30, 0.0, -0.5) for a in np.linspace(-2, 2, 12))/12
        v1 = mval(1.4, s_w, g1, 0.5) + eps0*sum(mval(float(a), 0.30, 0.0, 0.5) for a in np.linspace(-2, 2, 12))/12
        q2 = float(abs(vg)**2/abs(v0*v1))
        P1 = [(float(a), 0.20, 0.0) for a in np.linspace(0.3, 3.9, 12)]
        PH = P1 + [(1.4, 0.5, 2*g1), (2.2, 0.5, 2*g1)]
        DICTS = dict(build_dicts())
        out = {}
        for tag, dE, plist in [("d_D4", DICTS["D4"], P1), ("d_D6", DICTS["D6"], P1), ("d_D6_harm", DICTS["D6"], PH)]:
            tw = np.array([float(wc @ pair_rows(wE, pk, *eng)) for pk in plist])
            tH = np.array([float(Hc @ pair_rows(HE, pk, *eng)) for pk in plist])
            M = np.stack([pair_rows(dE, pk, *eng) for pk in plist])
            nrm = np.abs(M).max(axis=1); M = M/nrm[:, None]
            t = (tw + eps0*tH)/nrm
            out[tag] = float(deficit(M, t)/(np.abs(t).max() + 1e-30))
        return dict(D=D, g1=g1, off=off, s=s_w, sg1=s_w*g1, q2=q2, eps0=eps0, note="", **out)
    except Exception as e:
        return dict(D=D, g1=g1, off=off, s=np.nan, sg1=np.nan, q2=np.nan, eps0=np.nan,
                    d_D4=np.nan, d_D6=np.nan, d_D6_harm=np.nan, note=type(e).__name__)

def main():
    t0 = time.time()
    cands = [D for D in list(range(-30000, -2)) + list(range(5, 30000))
             if is_fund(D) and (abs(D) <= 600 or abs(D) % 11 == 3)]
    pr(f"[harvest] scanning {len(cands)} fundamental discriminants for (gamma_1, offset)")
    H = []
    with Pool(20) as pool:
        for r in pool.imap_unordered(harvest, [(D,) for D in cands], chunksize=8):
            if r: H.append(r)
    pr(f"[harvest] {len(H)} fields; gamma_1 range [{min(h[1] for h in H):.2f}, {max(h[1] for h in H):.2f}]  [{time.time()-t0:.0f}s]")
    # stratify: gamma_1 bins x offset extremes
    H.sort(key=lambda h: h[1])
    chosen = H[:14]                      # the 14 lowest-gamma_1 fields: the Siegel regime
    for lo in np.arange(0.8, 8.0, 0.9):
        binf = [h for h in H if lo <= h[1] < lo + 0.9]
        if not binf: continue
        binf.sort(key=lambda h: h[3])
        picks = [binf[0]] + ([binf[len(binf)//2]] if len(binf) > 2 else []) + ([binf[-1]] if len(binf) > 1 else [])
        chosen += picks
    seen = set(); sel = []
    for h in chosen:
        if h[0] not in seen: seen.add(h[0]); sel.append(h)
    pr(f"[select] {len(sel)} fields stratified in (gamma_1, offset)")
    rows = []
    with Pool(11) as pool:
        for r in pool.imap_unordered(measure, sel, chunksize=1):
            rows.append(r)
            pr(f"  D={r['D']:>7} g1={r['g1']:.3f} off={r['off']:.3f} sg1={r.get('sg1', float('nan')):.2f} "
               f"q2={r.get('q2', float('nan')):.2f} dD6={r.get('d_D6', float('nan')):.2e} "
               f"dHarm={r.get('d_D6_harm', float('nan')):.2e} {r['note']}")
    with open("gamma1_ladder_siegel.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader()
        for r in rows: w.writerow(r)
    ok = [r for r in rows if r['note'] == "" and np.isfinite(r['d_D6']) and r['d_D6'] > 0]
    pr(f"\n[regress] n={len(ok)} clean rows")
    if len(ok) >= 8:
        X = np.array([[r['g1'], math.log(max(r['off'], 1e-3)), r['sg1'], 1.0] for r in ok])
        y = np.array([math.log(r['d_D6']) for r in ok])
        beta, *_ = np.linalg.lstsq(X, y, rcond=None)
        pred = X @ beta; ss = 1 - ((y - pred)**2).sum()/((y - y.mean())**2).sum()
        pr(f"  log d(D6) = {beta[0]:+.3f}*g1 {beta[1]:+.3f}*log(off) {beta[2]:+.3f}*sg1 {beta[3]:+.2f}   R^2={ss:.3f}")
        jumps = [(r['d_D6_harm'] - r['d_D6'], r['q2']) for r in ok if np.isfinite(r['d_D6_harm'])]
        hi = [j for j, q in jumps if q > 0.5]; lo2 = [j for j, q in jumps if q <= 0.5]
        pr(f"  harmonic-probe jump: mean {np.mean(hi) if hi else float('nan'):.2e} (q2>1/2, n={len(hi)})"
           f" vs {np.mean(lo2) if lo2 else float('nan'):.2e} (q2<=1/2, n={len(lo2)})  [Prop C.3 prediction: former >> latter]")
        small = sorted(ok, key=lambda r: r['g1'])[:6]
        pr("  smallest gamma_1 rows (Siegel direction): " +
           "; ".join(f"g1={r['g1']:.2f}->d={r['d_D6']:.1e}" for r in small))
    pr(f"[total {time.time()-t0:.0f}s]")

if __name__ == "__main__":
    main()
