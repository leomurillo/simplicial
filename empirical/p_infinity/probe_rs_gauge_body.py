"""probe_rs_gauge_body.py — certificate for P-infinity-E SS17 (the body for the shape).

The weighted spec of Thm E.16(d) — sup e^{pi|t|/4} |khat_lambda - Xi| -> 0 — names a SHAPE.
This probe certifies the BODY that realizes it: the Riemann-Siegel structure.

CHECK A  (the gauge identity, exact): Xi(t) = -((t^2 + 1/4)/2) * R(t) * Z(t) with
         R(t) = pi^{-1/4} |Gamma(1/4 + it/2)| (the archimedean modulus) and Z the
         Riemann-Siegel Z-function.  The envelope env(t) = ((t^2+1/4)/2) R(t) is smooth and
         zero-free: dividing it out is a GAUGE TRANSFORMATION, and the E.16 weight
         e^{pi t/4} is exactly 1/env up to the polynomial factor t^{7/4} (CHECK B).
CHECK B  (weight identification): env(t) * e^{pi t/4} ~ C * t^{7/4} — fitted exponent 1.75.
CHECK C  (the redshift demystified): in the Z-gauge the E.16(d) protection threshold is O(1):
         the extremum of Xi between gamma_5, gamma_6 (= 2.3e-9, the 'dangerous' amplitude)
         equals env(m*) * (an O(1) extremum of Z).  Zero-protection is an O(1) problem in
         the right gauge; the exp-smallness was a gauge artifact of the archimedean skin.
CHECK D  (the skeleton + the light-cone saddle): the finite Riemann-Siegel main sum
         Z(t) ~ 2 sum_{n <= sqrt(t/2pi)} n^{-1/2} cos(theta(t) - t log n) approximates Z
         within O(t^{-1/4}) at t = 100, 500, 2000; and the cutoff is the STATIONARY-PHASE
         light cone: d/dt[theta(t) - t log n] = 0 exactly at n = sqrt(t/2pi)
         (theta'(t) = (1/2) log(t/2pi) + O(1/t^2) = the instantaneous frequency).
CHECK E  (mode-independent redshift = Agmon universality of the place): the Mellin
         transforms of the oscillator family f_n(x) = x^{2n} e^{-pi x^2} all decay with the
         SAME exponent e^{-pi|t|/4} (only the polynomial prefactor t^{n-1/4} varies):
         the redshift is a property of the archimedean PLACE, not of the state.

Deterministic, local, ~1 min (mpmath).
"""
import sys
import numpy as np
import mpmath as mp

sys.stdout.reconfigure(encoding="utf-8")
mp.mp.dps = 30

def Xi(t):
    s = mp.mpf(0.5) + 1j * t
    return mp.re(mp.mpf(0.5) * s * (s - 1) * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s))

def env(t):
    return (t * t + mp.mpf(0.25)) / 2 * mp.pi ** mp.mpf(-0.25) * abs(mp.gamma(mp.mpf(0.25) + 0.5j * t))

# ---------------- CHECK A: the gauge identity ----------------
print("== CHECK A: Xi(t) = -env(t) * Z(t) exactly (the archimedean gauge) ==")
okA = True
for t in (5.0, 14.0, 21.5, 34.2, 60.0, 95.0):
    lhs = Xi(mp.mpf(t))
    rhs = -env(mp.mpf(t)) * mp.siegelz(t)
    e = abs(lhs - rhs) / max(abs(lhs), mp.mpf("1e-40"))
    okA &= e < mp.mpf("1e-18")
    print(f"   t = {t:6.1f}: Xi = {mp.nstr(lhs, 6, strip_zeros=False):>14}   rel err vs -env*Z: {mp.nstr(e, 2)}")
print("   " + ("PASS — the envelope is exact and zero-free: dividing it out is a gauge move"
               if okA else "FAIL"))

# ---------------- CHECK B: the weight is 1/env up to t^{7/4} ----------------
print("\n== CHECK B: env(t) * e^{pi t/4} ~ C t^{7/4} — the E.16 weight named ==")
ts = [mp.mpf(x) for x in (50, 100, 200, 400, 800)]
vals = [mp.log(env(t)) + mp.pi * t / 4 for t in ts]
slope = np.polyfit([float(mp.log(t)) for t in ts], [float(v) for v in vals], 1)[0]
okB = abs(slope - 1.75) < 0.02
print(f"   fitted exponent d log(env * e^{{pi t/4}}) / d log t = {slope:.4f}   (predict 7/4 = 1.75)")
print("   " + ("PASS — weighted-spec norm == unweighted (poly-normalized) Z-gauge norm"
               if okB else "FAIL"))

# ---------------- CHECK C: protection threshold is O(1) in the Z-gauge ----------------
print("\n== CHECK C: the E.16(d) dangerous amplitude, re-read in the Z-gauge ==")
g5, g6 = 32.93506, 37.58618
ts2 = mp.linspace(g5 + 0.2, g6 - 0.2, 80)
xv = [abs(Xi(t)) for t in ts2]
i = max(range(80), key=lambda k: xv[k])
m_star, E_xi = ts2[i], xv[i]
Z_ext = abs(mp.siegelz(float(m_star)))
okC = mp.mpf("0.05") < Z_ext < 20
print(f"   extremum between gamma_5, gamma_6: |Xi| = {mp.nstr(E_xi, 3)} at t = {float(m_star):.3f}")
print(f"   same point in the Z-gauge: |Z| = {mp.nstr(Z_ext, 4)} = O(1);  ratio = env = {mp.nstr(E_xi / Z_ext, 3)}")
print("   " + ("PASS — the 1e-9 'redshifted' threshold is an O(1) threshold in the Z-gauge: "
               "the exp-smallness was the archimedean skin, not the flesh" if okC else "FAIL"))

# ---------------- CHECK D: the RS skeleton and the stationary-phase light cone ----------------
print("\n== CHECK D: finite skeleton Z_RS(t) and the saddle n* = sqrt(t/2pi) ==")
def Z_rs(t):
    N = int(mp.floor(mp.sqrt(t / (2 * mp.pi))))
    th = mp.siegeltheta(t)
    return 2 * mp.fsum(mp.cos(th - t * mp.log(n)) / mp.sqrt(n) for n in range(1, N + 1))

okD = True
for t in (100.0, 500.0, 2000.0):
    err = abs(Z_rs(t) - mp.siegelz(t))
    bound = 2 * t ** (-0.25)
    okD &= err < bound
    print(f"   t = {t:6.0f}: |Z_RS - Z| = {float(err):.4f}   (allow 2 t^-1/4 = {float(bound):.4f})  "
          f"N(t) = {int(mp.floor(mp.sqrt(t/(2*mp.pi))))} modes")
for t in (500.0, 2000.0):
    fprime = mp.diff(mp.siegeltheta, t)             # instantaneous frequency theta'(t)
    nstar = mp.exp(fprime)                          # stationary phase: log n = theta'(t)
    okD &= abs(nstar - mp.sqrt(t / (2 * mp.pi))) / nstar < 1e-3
    print(f"   t = {t:6.0f}: stationary-phase mode e^{{theta'}} = {float(nstar):.4f}  "
          f"vs sqrt(t/2pi) = {float(mp.sqrt(t/(2*mp.pi))):.4f}")
print("   " + ("PASS — finite arithmetic skeleton at every height; cutoff = the light cone of "
               "the instantaneous frequency" if okD else "FAIL"))

# ---------------- CHECK E: mode-independent redshift (Agmon universality) ----------------
print("\n== CHECK E: Mellin of x^{2n} e^{-pi x^2}: same e^{-pi|t|/4}, only poly varies ==")
def Mf(n, t):
    s = mp.mpf(0.5) + 1j * t
    return abs(mp.mpf(0.5) * mp.pi ** (-(s + 2 * n) / 2) * mp.gamma((s + 2 * n) / 2))

okE = True
for n in (0, 2, 5):
    c1 = mp.log(Mf(n, mp.mpf(40))) + mp.pi * 40 / 4 - (n - mp.mpf(0.25)) * mp.log(20)
    c2 = mp.log(Mf(n, mp.mpf(80))) + mp.pi * 80 / 4 - (n - mp.mpf(0.25)) * mp.log(40)
    okE &= abs(c2 - c1) < 0.05
    print(f"   n = {n}: [log|M f_n| + pi t/4 - (n - 1/4) log(t/2)] at t=40 vs t=80: "
          f"{float(c1):+.4f} vs {float(c2):+.4f}  (drift {float(abs(c2-c1)):.4f})")
print("   " + ("PASS — the pi/4 exponent is universal across oscillator levels: the redshift "
               "belongs to the PLACE (the metric), not the state" if okE else "FAIL"))

allok = okA and okB and okC and okD and okE
print("\nRESULT: " + ("GREEN — the body is Riemann-Siegel: exact archimedean gauge, O(1) "
                      "thresholds in the Z-gauge, finite skeleton with stationary-phase light "
                      "cone, and a place-universal redshift" if allok else "RED"))
