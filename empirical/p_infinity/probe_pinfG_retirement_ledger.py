"""probe_pinfG_retirement_ledger.py -- THE DERIVATION TEST: does the Section 15.4
per-zero retirement mechanism, as a one-mechanism two-parameter law, carry the measured
R_seam(lambda^2) ladder on the post-onset domain?

THE MECHANISM (P-inf-G Sec 15.4, head-math made fittable). Zero rho_j = beta_j + i gamma_j
imprints the arrival stream with normalized amplitude 2/|rho_j| (explicit formula,
n^(-1/2) Lambda-normalization), hence variance share ~ 2/gamma_j^2 per unit of arrival
mass. The renewal predicts the oscillation once it is per-arrival smooth; the per-arrival
phase step is gamma_j / lambda^2 (arrival spacing in y at the window edge is 1/lambda^2).
The transition zone (phase step ~ tau^-1 crossing unity) has width O(1) in ln(lambda^2)
and center lambda^2 = tau * gamma_j. Integrating the excess eating across the zone:

    delta_j = A / gamma_j            (step depth; A = O(1) prediction-gain integral)
    ln R(lambda^2) = ln R0 - A * sum_j (1/gamma_j) * S( (ln lambda^2 - ln(tau gamma_j)) / w )

with S the logistic step and two mechanism variants for the retirement threshold:
    T-1rad : tau = 1      (coherence at phase step ~ 1 rad per arrival)
    T-Nyq  : tau = 1/pi   (aliasing/Nyquist; PREREG_lambda4_floor addendum 2)

The sum over j reproduces Sec 15's log-squared envelope asymptotically (zero density);
the DIFFERENCE from the free envelope is that A is the SAME constant measured locally by
the fixed-N steps (delta_j * gamma_j = A), so the global fit and the local steps must
agree -- a parameter-identity test across two independent instruments.

PRE-REGISTERED (locked before this script is first run; GPD):
  Domain: lambda^2 >= gamma_1 = 14.134725 (the measured deceleration onset, Sec 15.1).
  Fixed: w = 0.30 (from the phase-step geometry, zone phi in [0.5, 1.5] -> half-width
         ~0.55 in ln x; logistic w = 0.55/1.8 ~ 0.3). Sensitivity at w = 0.15 / 0.60
         reported, NOT used for verdicts.
  Fits:  exact linear least squares in (ln R0, A) resp. (a, c) resp. (a, p); all models
         two-parameter; same points, same weights (unit).
  L1 (mechanism): best-tau ledger rms(log) <= 1.15 x envelope rms(log)  AND  fitted
      A in [3, 10] (the Sec 15.4 calibration band)  ->  mechanism-consistent.
  L2 (threshold): rms ratio between tau-variants >= 1.2  ->  provisional threshold
      verdict for the better variant; else 'not separated on archived data' (the
      crossing ensemble in flight is the out-of-sample judge).
  KILL: fitted A outside [1, 20]  OR  ledger rms > 1.5 x envelope rms  ->  the per-zero
      ledger AS STATED is dead (corpse retained; mechanism needs re-derivation).
  OUT-OF-SAMPLE PREDICTION (printed below, BEFORE the ensemble returns): the E2
      discriminant D = mean(crossing-pair rates) - mean(gap-pair rates) over the exact
      ensemble design, computed from each fitted model. The ensemble's measured D
      adjudicates between them with fresh data.

Data: every archived R_seam with lambda^2 in the domain (npz preferred; the fixed-N
values from the run log, dps 160, transcribed with provenance). Mixed-N points carry the
+-20% bandwidth-rounding sawtooth (Sec 15.4 instrument kill) -- model-independent noise,
inflates every rms equally, fair for comparison.

Deterministic, local, seconds. numpy + mpmath (zetazero).
"""
import sys
import numpy as np
import mpmath as mp

sys.stdout.reconfigure(encoding="utf-8")
HERE = "empirical/p_infinity/"
GAMMA1 = 14.134725

# ---------------------------------------------------------------- data assembly
pts = {}   # lam^2 (rounded) -> (R, provenance); later instruments overwrite earlier


def put(l2, R, tag):
    pts[round(float(l2), 4)] = (float(R), tag)


d = np.load(HERE + "pinfG_profile_cubic_dense.npz")
for lam, R in zip(d["ladder_lams"], d["ladder_R"]):
    l2 = float(lam) ** 2 if float(lam) < 10 else float(lam)
    put(l2, R, "dense-ladder")

d = np.load(HERE + "pinfG_lambda4_pair.npz")
for lam, R in zip(d["lams"], d["Rseam"]):
    l2 = float(lam) ** 2 if float(lam) < 10 else float(lam)
    put(l2, R, "lambda4-pair(dps175)")

d = np.load(HERE + "pinfG_floor_discriminator.npz")
for lam, R in zip(d["lams"], d["Rseam"]):
    l2 = float(lam) ** 2 if float(lam) < 10 else float(lam)
    put(l2, R, "floor-disc(dps130/150)")

d = np.load(HERE + "pinfG_zero_staircase.npz")
for l2, R in zip(d["l2"], d["R"]):
    put(l2, R, "staircase-scan(dps130)")

d = np.load(HERE + "pinfG_multicrossing.npz")
for l2, R in zip(d["l2"], d["R"]):
    put(l2, R, "multicrossing(dps160,sawtooth)")

# fixed-N pairs: npz stores only rates; values from pinfG_fixedN_steps_run.log (dps 160)
for l2, R in [(29.22, 0.02016), (31.62, 0.02204), (31.74, 0.01837), (34.14, 0.01534),
              (36.39, 0.01423), (38.79, 0.01354), (34.05, 0.01471), (36.45, 0.01475),
              (38.05, 0.01559), (40.45, 0.01499)]:
    put(l2, R, "fixedN-log(dps160)")

data = sorted((l2, R, tag) for l2, (R, tag) in pts.items() if l2 >= GAMMA1)
x = np.array([p[0] for p in data])
y = np.log(np.array([p[1] for p in data]))
print(f"== assembled ladder: {len(data)} windows, lambda^2 in "
      f"[{x.min():.2f}, {x.max():.2f}] (domain >= gamma_1) ==")

# ---------------------------------------------------------------- zeros (exact, cached)
mp.mp.dps = 20
NZ = 120
gam = np.array([float(mp.im(mp.zetazero(n))) for n in range(1, NZ + 1)])
print(f"   zeros: gamma_1..gamma_{NZ} via mp.zetazero (dps 20); "
      f"gamma_1={gam[0]:.6f}, gamma_20={gam[19]:.6f}")

# ---------------------------------------------------------------- models
W = 0.30


def ledger_design(xv, tau, w=W):
    """Column: -sum_j S((ln l2 - ln(tau*g_j))/w)/g_j  (the A-coefficient)."""
    lx = np.log(xv)[:, None]
    lth = np.log(tau * gam)[None, :]
    S = 1.0 / (1.0 + np.exp(-np.clip((lx - lth) / w, -60, 60)))
    return -(S / gam[None, :]).sum(axis=1)


def lsq(cols, yv):
    """Exact linear LSQ; returns params, rms of residual."""
    Amat = np.column_stack(cols)
    prm, *_ = np.linalg.lstsq(Amat, yv, rcond=None)
    r = yv - Amat @ prm
    return prm, float(np.sqrt(np.mean(r ** 2))), r


one = np.ones_like(x)
results = {}
for tag, tau in [("T-1rad", 1.0), ("T-Nyq", 1.0 / np.pi)]:
    col = ledger_design(x, tau)
    (lnR0, A), rms, resid = lsq([one, col], y)
    results[tag] = dict(A=A, rms=rms, resid=resid, tau=tau)
    print(f"   ledger {tag:7s}: A = {A:6.3f}   rms(log) = {rms:.4f}")

(a_e, c_e), rms_env, res_env = lsq([one, -0.25 * np.log(x) ** 2], y)
print(f"   envelope (free c): c = {c_e:6.3f}   rms(log) = {rms_env:.4f}")
(a_p, p_p), rms_pow, _ = lsq([one, -np.log(x)], y)
print(f"   power law (control): p = {p_p:6.3f}   rms(log) = {rms_pow:.4f}")

# sensitivity (reported, not used for verdicts)
for wtest in (0.15, 0.60):
    for tag, tau in [("T-1rad", 1.0), ("T-Nyq", 1.0 / np.pi)]:
        col = ledger_design(x, tau, w=wtest)
        (l0, Aw), rmsw, _ = lsq([one, col], y)
        print(f"   [sens w={wtest}] {tag}: A = {Aw:6.3f}  rms = {rmsw:.4f}")

# ---------------------------------------------------------------- verdicts
best = min(results, key=lambda t: results[t]["rms"])
other = [t for t in results if t != best][0]
Ab, rb = results[best]["A"], results[best]["rms"]
ratio_tau = results[other]["rms"] / max(rb, 1e-12)
print(f"\n== verdicts (locked rules) ==")
print(f"   best tau-variant: {best}  (A = {Ab:.3f}, rms = {rb:.4f}); "
      f"tau-separation rms ratio = {ratio_tau:.3f}")

kill = (not (1 <= Ab <= 20)) or (rb > 1.5 * rms_env)
l1 = (rb <= 1.15 * rms_env) and (3 <= Ab <= 10)
if kill:
    print("   KILL: the per-zero ledger AS STATED is dead (corpse retained).")
else:
    print(f"   L1 (mechanism-consistent: rms <= 1.15x envelope AND A in [3,10]): "
          f"{'PASS' if l1 else 'no (report)'}"
          f"   [rms/env = {rb/rms_env:.3f}, A = {Ab:.2f}]")
print(f"   L2 (threshold separated on archived data, ratio >= 1.2): "
      f"{'YES -> ' + best if ratio_tau >= 1.2 else 'NOT SEPARATED (ensemble judges)'}")

# ---------------------------------------------------------------- out-of-sample: E2 prediction
PAIRS = [
    ("g4", 29.62, 31.22, 1), ("g5", 32.14, 33.74, 1), ("g6", 36.79, 38.39, 1),
    ("g7", 40.12, 41.72, 1), ("g8", 42.53, 44.13, 1), ("g11", 52.17, 53.77, 1),
    ("g12", 55.65, 57.25, 1), ("g17", 68.75, 70.35, 1),
    ("g9+10", 47.19, 50.59, 2), ("g13+14", 58.39, 61.79, 2), ("g15+16", 64.40, 67.80, 2),
    ("gapA", 44.50, 46.90, 0), ("gapB", 54.00, 55.60, 0),
    ("gapC", 62.00, 63.60, 0), ("gapD", 73.00, 74.60, 0),
]
print(f"\n== registered OUT-OF-SAMPLE prediction for the crossing ensemble (E2) ==")
for tag in ("T-1rad", "T-Nyq"):
    tau = results[tag]["tau"]
    A = results[tag]["A"]
    lnR0 = None  # rates need no intercept
    rates_c, rates_g = [], []
    for name, a, b, nz in PAIRS:
        la = ledger_design(np.array([a]), tau)[0] * A
        lb = ledger_design(np.array([b]), tau)[0] * A
        rate = -(lb - la) / (b - a)
        (rates_c if nz >= 1 else rates_g).append(rate)
    D = np.mean(rates_c) - np.mean(rates_g)
    print(f"   {tag:7s}: predicted crossing mean {np.mean(rates_c):+.4f}, "
          f"gap mean {np.mean(rates_g):+.4f}  ->  D_pred = {D:+.4f}")
env_rates_c, env_rates_g = [], []
for name, a, b, nz in PAIRS:
    rate = c_e * 0.25 * (np.log(b) ** 2 - np.log(a) ** 2) / (b - a)
    (env_rates_c if nz >= 1 else env_rates_g).append(rate)
print(f"   envelope: predicted crossing mean {np.mean(env_rates_c):+.4f}, "
      f"gap mean {np.mean(env_rates_g):+.4f}  ->  D_pred = "
      f"{np.mean(env_rates_c)-np.mean(env_rates_g):+.4f}  (smooth law: D ~ 0)")

# ---------------------------------------------------------------- archive
np.savez(HERE + "pinfG_retirement_ledger.npz",
         l2=x, lnR=y,
         A_1rad=results["T-1rad"]["A"], rms_1rad=results["T-1rad"]["rms"],
         A_nyq=results["T-Nyq"]["A"], rms_nyq=results["T-Nyq"]["rms"],
         c_env=c_e, rms_env=rms_env, p_pow=p_p, rms_pow=rms_pow,
         resid_best=results[best]["resid"], gam=gam[:40])
print("\nARCHIVED: pinfG_retirement_ledger.npz")
