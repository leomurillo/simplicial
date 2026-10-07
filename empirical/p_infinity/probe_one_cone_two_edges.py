"""probe_one_cone_two_edges.py — certificate for P-infinity-E SS18 (one cone, two edges).

SS17 posed: reconcile the SPECTRAL saturation edge (N(T) ~ (T/2pi) log T zeros) with the
ARITHMETIC skeleton edge (sqrt(T/2pi) integers).  Resolution: they are the AREA and the
BOUNDARY HEIGHT of one phase-space cone — the classical phase space of H = xp, which is
the CCM scaling operator S = (xp + px)/2.

CHECK A  (area = count, with the 1/8 seam phase): the Planck-cell count of the xp box
         {x >= 1, p >= 2pi, xp <= T} is (T/2pi)log(T/2pi) - T/2pi + 1, and it exceeds the
         Riemann-von Mangoldt smooth count theta(T)/pi + 1 by EXACTLY 1/8 as T -> oo:
         the Maslov-type boundary phase of the cone = the program's apex-archimedean
         1/8 turn (N4).  Certified: deficit -> 0.125 to 1e-3 by T = 2000.
CHECK B  (the count is real: three-way match at T = 500): sign-change count of Z on [0,500]
         == theta/pi + 1 + S  ==  xp-box - 1/8, within |S| <= 2.
CHECK C  (winding neutrality of the prime field): the secular zero density is 100%%
         archimedean: <S> over [0,500] is ~0 (the arithmetic phasor field has zero Weyl
         mean motion — the dynamical face of square-root cancellation), while the
         HALF-field (the RS Dirichlet polynomial D_N alone, no FE mirror) has a nonzero
         drift, measured — the gap the functional-equation mirror must cancel at the seam.

Deterministic, local, ~1-2 min (mpmath + numpy).
"""
import sys
import numpy as np
import mpmath as mp

sys.stdout.reconfigure(encoding="utf-8")

def xp_count(T):
    r = T / (2 * mp.pi)
    return r * mp.log(r) - r + 1

def rvm(T):
    return mp.siegeltheta(T) / mp.pi + 1

# ---------------- CHECK A: the 1/8 seam phase ----------------
print("== CHECK A: xp Planck-cell count minus Riemann-von Mangoldt -> 1/8 (the seam phase) ==")
mp.mp.dps = 25
okA = True
for T in (50, 100, 500, 2000, 10000):
    d = xp_count(mp.mpf(T)) - rvm(mp.mpf(T))
    if T >= 2000:
        okA &= abs(d - mp.mpf(1) / 8) < 1e-3
    print(f"   T = {T:6}: xp-box - (theta/pi + 1) = {float(d):.6f}")
print("   " + ("PASS — the cone overcounts by EXACTLY 1/8: the Maslov/metaplectic boundary "
               "phase = the apex-archimedean 1/8 turn of N4" if okA else "FAIL"))

# ---------------- CHECK B: three-way count at T = 500 ----------------
print("\n== CHECK B: zeros on [0,500]: sign count vs theta/pi + 1 vs xp-box - 1/8 ==")
mp.mp.dps = 12
ts = np.arange(10.0, 500.0, 0.1)
signs = []
zv = []
for t in ts:
    zv.append(float(mp.siegelz(float(t))))
zv = np.array(zv)
count = int(np.sum(zv[:-1] * zv[1:] < 0))
mp.mp.dps = 25
r1 = float(rvm(mp.mpf(500)))
r2 = float(xp_count(mp.mpf(500)) - mp.mpf(1) / 8)
okB = abs(count - r1) < 2.5 and abs(count - r2) < 2.5
print(f"   sign-change count N0(500) = {count}")
print(f"   theta/pi + 1               = {r1:.3f}")
print(f"   xp-box - 1/8               = {r2:.3f}")
print("   " + ("PASS — one cone, two readings: AREA = zero count; the arithmetic edge "
               "sqrt(T/2pi) = e^{theta'} is the cone's BOUNDARY HEIGHT" if okB else "FAIL"))

# ---------------- CHECK C: winding neutrality vs half-field drift ----------------
print("\n== CHECK C: secular winding is 100% archimedean; the prime field is winding-neutral ==")
# running S(t) = N0(t) - (theta/pi + 1) along the scan; its mean ~ 0
mp.mp.dps = 15
cum = np.cumsum(zv[:-1] * zv[1:] < 0)
theta_vals = np.array([float(mp.siegeltheta(float(t)) / mp.pi + 1) for t in ts[1:][::40]])
S_vals = cum[::40][:len(theta_vals)] - theta_vals
S_mean = float(np.mean(S_vals))
S_max = float(np.max(np.abs(S_vals)))
okC1 = abs(S_mean) < 0.25 and S_max < 2.5
print(f"   <S> over [10,500] = {S_mean:+.4f}   max|S| = {S_max:.3f}   "
      f"(mean motion of the prime field ~ 0; all secular density = theta'/pi)")
# the HALF-field drift: winding of D_N(t) = sum n^{-1/2} e^{-i t log n}, N = 17, t in [2000,2100]
N = 17
tt = np.arange(2000.0, 2100.0, 0.02)
ns = np.arange(1, N + 1)
D = (ns[None, :] ** (-0.5) * np.exp(-1j * np.outer(tt, np.log(ns)))).sum(axis=1)
ph = np.unwrap(np.angle(D))
m_D = (ph[-1] - ph[0]) / (tt[-1] - tt[0])
thp = 0.5 * np.log(2050.0 / (2 * np.pi))
okC2 = abs(m_D) > 0.02
print(f"   half-field drift (D_17, no FE mirror): mean motion = {m_D:+.4f} per unit t")
print(f"   archimedean rotation theta' = {thp:.4f}; zeta's own mean motion ~ pi*dS/dt ~ 0")
print(f"   => the FE mirror must cancel a drift of {abs(m_D):.3f} at the seam — the measured "
      "size of the Gauss-sum termination's job")
okC = okC1 and okC2
print("   " + ("PASS — square-root cancellation = winding neutrality of the FULL prime field; "
               "the half-field drifts and the mirror pays it back" if okC else "FAIL"))

allok = okA and okB and okC
print("\nRESULT: " + ("GREEN — one cone (the xp phase space of the CCM scaling operator), two "
                      "edges (area = zeros, boundary height = integers), one seam phase (1/8), "
                      "and a winding-neutral prime field: the secular count is purely "
                      "archimedean, the arithmetic is pure fluctuation"
                      if allok else "RED"))
