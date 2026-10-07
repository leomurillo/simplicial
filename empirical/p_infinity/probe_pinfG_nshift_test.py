"""probe_pinfG_nshift_test.py -- THE ATTRIBUTION TEST: is the phase-scan oscillation
kernel content (arithmetic) or the bandwidth-resonance ripple (instrument)?

The July-5 phase scan (gamma_8..gamma_9, N=67 fixed) killed the quadrature (PH1 fired
<= 0) and revealed a coherent +-0.23-0.29 oscillation in the eating rate, period
Delta lambda^2 ~ 2.5-3, phase NOT locked to the zeros (gamma_8: R rises across;
gamma_9: R falls across). The matched-bandwidth family drifts one mode per
Delta lambda^2 = lambda^2/17.312 ~ 2.66 here -- the Sec 15.4 sawtooth mechanism would
produce exactly this period at fixed N via the drifting mismatch.

Discriminator: recompute the steep segment (lambda^2 = 44.3, 45.1, 45.9, 46.7 -- the
+0.29 drop and the -0.23 rise) at N = 66 and N = 68. The kernel does not know N; the
ripple does.

PRE-REGISTERED (locked before first run; GPD):
  NS0: PSD at dps 160 everywhere.
  NS1 (attribution): with r_k(N) the three segment rates at mids 44.7, 45.5, 46.3,
       and dmax = max_k max(|r_k(66)-r_k(67)|, |r_k(68)-r_k(67)|)  [r_k(67) from the
       archived phase scan]:
       dmax >= 0.15 -> INSTRUMENT (bandwidth ripple): the July class analyses (E2, X1)
                       are confounded; the anti-staircase verdict is RETRACTED to
                       'class contrast unattributed'; every rate-level result at these
                       heights needs ripple-immune redesign.
       dmax <= 0.06 -> KERNEL (arithmetic): the oscillation is real zeta content at
                       fixed instrument; the zero-phase relation needs a finer frame
                       (beat/combination tones registered as the next hypothesis).
       between      -> both live; report, design the dense-N sweep.
  Values r_k(67) (archived, pinfG_phase_scan.npz): +0.2897, +0.0018, -0.2299.
"""
import sys
import time
import numpy as np
import mpmath as mp

sys.stdout.reconfigure(encoding="utf-8")
HERE = "empirical/p_infinity/"

src = open(HERE + "probe_pinfG_cubic_drift_v2.py", encoding="utf-8").read()
exec(src[src.index("def primes_upto"):src.index("# ---------------------------------------------------------------- W0c")])

WINDOWS = [44.3, 45.1, 45.9, 46.7]
DPS = 160
R67 = {44.3: 0.01543, 45.1: 0.01224, 45.9: 0.01222, 46.7: 0.01469}  # archived scan
r67 = [0.2897, 0.0018, -0.2299]

mp.mp.dps = DPS
out = {}
for N in (66, 68):
    print(f"== N = {N} ==")
    R = {}
    for l2 in WINDOWS:
        t0 = time.time()
        lam = mp.sqrt(mp.mpf(repr(l2)))
        Q, _, _ = build_QW_mode(lam, N, "true")
        K = to_point(Q, N)
        if not cholesky_psd(K):
            print(f"   lam^2={l2}: STARVED -- abort")
            sys.exit(1)
        d0 = direct_pivot(K, 2 * N + 1, "seam")
        R[l2] = float(d0 / K[0, 0])
        print(f"   lam^2={l2:<5} ({time.time()-t0:.0f}s): R_seam={R[l2]:.5f}")
    rates = [-np.log(R[b] / R[a]) / (b - a)
             for a, b in zip(WINDOWS[:-1], WINDOWS[1:])]
    out[N] = rates
    print(f"   rates: {['%+.4f' % r for r in rates]}")

print("\n== NS1: attribution ==")
print(f"   r(67) archived: {['%+.4f' % r for r in r67]}")
dmax = 0.0
for N in (66, 68):
    d = max(abs(out[N][k] - r67[k]) for k in range(3))
    print(f"   max |r({N}) - r(67)| = {d:.4f}")
    dmax = max(dmax, d)
print(f"   dmax = {dmax:.4f}")
if dmax >= 0.15:
    print("   NS1: INSTRUMENT -- bandwidth ripple; July class analyses CONFOUNDED;")
    print("        anti-staircase verdict RETRACTED to 'class contrast unattributed'")
elif dmax <= 0.06:
    print("   NS1: KERNEL -- the oscillation is arithmetic content, N-invariant")
else:
    print("   NS1: between -- both live; dense-N sweep next")

np.savez(HERE + "pinfG_nshift_test.npz",
         windows=np.array(WINDOWS),
         rates66=np.array(out[66]), rates68=np.array(out[68]),
         rates67=np.array(r67))
print("\nARCHIVED: pinfG_nshift_test.npz")
