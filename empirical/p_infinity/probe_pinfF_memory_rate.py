"""probe_pinfF_memory_rate.py -- strike 1a numeric: is the renewal's MEMORY RATE
(the massive-cell / bulk collapse pace c_{+-} ~ 2.7-3.2 per unit lambda^2) an
ARCHIMEDEAN/criterion property or an arithmetic one?

WHY IT MATTERS (the effective-contraction strike, P-inf-F section 25 candidate): the
F.23 renewal forgets its past at the bulk pace (slaved bulk, c_clean ~ 2.7-3.8; the
parity edge cells at c_+ = 2.81 / c_- = 2.66).  If that pace is a property of the
PRIME-FREE kernel (arch + pole only -- smooth, unconditional, no zeros anywhere), the
contraction half of the (U)-attack consumes ONLY unconditional inputs and becomes a
provable Szego-type statement; the arithmetic then enters only through the seam.

OBJECTS: the no-prime builder (P = 0 in S and D) at the certified bandwidth family;
per window: PSD status, edge remainders R_+ = d_+/bare_+, R_- = d_-/bare_-, seam
R_0 = d_0/K00; paces from consecutive ratios.  An alternate-bandwidth build at
lam = 2.2 tests criterion-dependence (the section 23.2 caveat: the bulk collapse is
'continuum smoothness, criterion').

PRE-REGISTERED:
  M1 (PSD): the no-prime form is PSD at every window (expected: dropping the negative
      prime block leaves the smooth positive part; if it FIRES the no-prime form is
      indefinite like the Cramer mean field -- a finding that kills the simple
      reference-chain framing and reroutes to the F.24(i) bracket).
  M2 (the pace verdict, the strike's question): c_+^{ref}, c_-^{ref} within +-0.7 of
      the arithmetic values (2.81/2.66) -> the massive-cell pace is ARCHIMEDEAN
      (contraction rate unconditional).  Far off -> the pace is arithmetic; report.
  M3 (the seam contrast, reading): R_0^{ref}(lambda) -- if it does NOT follow the
      marginal p = 3.2 law (stays O(1) or collapses fast), the marginal seam is
      ARITHMETIC (the law is created by the primes) -- either way a sharp statement.
  M4 (criterion test): the lam = 2.2 alt-bandwidth (N x 1.5) R-values vs the family
      values -- pace shift reported (criterion-dependence quantified).
dps 40 (the no-prime form has no Euler ladder, E.22.1; conditioning is smooth-symbol
grade).  Runtime ~5 min.
"""
import sys
import time
import numpy as np
import mpmath as mp

sys.stdout.reconfigure(encoding="utf-8")
HERE = "empirical/p_infinity/"

src = open(HERE + "probe_pinfG_cubic_drift_v2.py", encoding="utf-8").read()
exec(src[src.index("def primes_upto"):src.index("# ---------------------------------------------------------------- W0c")])
srcI = open(HERE + "probe_pinfG_increment_bound.py", encoding="utf-8").read()
exec(srcI[srcI.index("def schur_solve"):srcI.index("def tstar_bisect")])

mp.mp.dps = 40


def build_QW_noprime(lam, N):
    """The certified builder with the prime block REMOVED (arch + pole + WR only)."""
    L = 2 * mp.log(lam)
    w = lambda k: 2 * mp.pi * k / L
    pts = mp.linspace(0, L, 14)
    S, D = {}, {}
    for k in range(-N, N + 1):
        wk = w(k)
        A = mp.quad(lambda y: mp.sin(wk * y) * 2 * mp.cosh(y / 2), pts)
        B = mp.quad(lambda y: mp.exp(y / 2) * mp.sin(wk * y) / (2 * mp.sinh(y)) if y != 0 else wk / 2, pts)
        S[k] = A - B
    tailL = mp.log(mp.tanh(L / 2)) / 2
    for k in range(0, N + 1):
        wk = w(k)
        qd = lambda y: 2 * (1 - y / L) * mp.cos(wk * y)
        A = mp.quad(lambda y: qd(y) * 2 * mp.cosh(y / 2), pts)
        Bint = mp.quad(lambda y: (mp.exp(y / 2) * qd(y) - 2) / (2 * mp.sinh(y)) if y != 0
                       else (mp.mpf(1) / 2 - 1 / L), pts)
        WR = (mp.log(4 * mp.pi) + mp.euler) + Bint + 2 * tailL
        D[k] = A - WR
    return assemble_Q(S, D, N)


CASES = [(1.8, 20), (2.0, 24), (2.2, 27), (2.35, 30), (2.5, 32), (2.6926, 34)]
ALT = (2.2, 40)

print("== memory rate: the prime-free reference chain (dps=40) ==\n")
REF = {}
for lam, N in CASES + [ALT]:
    t0 = time.time()
    tag = "alt-bw" if (lam, N) == ALT else "family"
    Q = build_QW_noprime(mp.mpf(repr(lam)), N)
    K = to_point(Q, N)
    dim = 2 * N + 1
    psd = cholesky_psd(K)
    ob = bridge_observables(K, dim)
    bare_p = ob["dp"] + (ob["dp"] - ob["dp"])  # placeholder; recompute below
    # remainders relative to bare (sector edges) and K00 (seam)
    d_ = dim
    m = (dim - 1) // 2
    bare_pl = (K[1, 1] + K[1, d_ - 1] + K[d_ - 1, 1] + K[d_ - 1, d_ - 1]) / 2
    bare_mn = (K[1, 1] - K[1, d_ - 1] - K[d_ - 1, 1] + K[d_ - 1, d_ - 1]) / 2
    Rp = float(ob["dp"] / bare_pl)
    Rm = float(ob["dm"] / bare_mn)
    R0 = float(ob["d0x"] / ob["K00"])
    REF[(lam, tag)] = dict(Rp=Rp, Rm=Rm, R0=R0, psd=psd,
                           oddshare=ob["oddshare"], dim=dim)
    print(f"   lam={lam:<7} [{tag}] (dim={dim}, {time.time()-t0:.0f}s): "
          f"PSD={'OK' if psd else 'INDEFINITE'}  R+={Rp:.4e}  R-={Rm:.4e}  R0={R0:.4f}"
          f"  oddshare={ob['oddshare']:.3f}")

print("\n== M1: PSD ==")
m1 = all(REF[k]["psd"] for k in REF)
print("   " + ("SURVIVES -- prime-free form PSD everywhere" if m1 else
               "FIRED -- indefinite (reroute to the F.24 bracket; report)"))

print("\n== M2: the pace (per unit lambda^2, consecutive family windows) ==")
fam = [(lam, N) for lam, N in CASES]
print("   pair          c+_ref   c-_ref   c0_ref   | true: c+=2.81 c-=2.66 seam p=3.2")
cps, cms = [], []
for (la, _), (lb, _) in zip(fam, fam[1:]):
    dl2 = lb**2 - la**2
    cp = -np.log(REF[(lb, 'family')]["Rp"] / REF[(la, 'family')]["Rp"]) / dl2
    cm = -np.log(REF[(lb, 'family')]["Rm"] / REF[(la, 'family')]["Rm"]) / dl2
    c0 = -np.log(REF[(lb, 'family')]["R0"] / REF[(la, 'family')]["R0"]) / dl2
    cps.append(cp); cms.append(cm)
    print(f"   {la}-{lb}:   {cp:+.3f}   {cm:+.3f}   {c0:+.3f}")
cpg, cmg = np.mean(cps), np.mean(cms)
m2 = abs(cpg - 2.81) <= 0.7 and abs(cmg - 2.66) <= 0.7
print(f"   global means: c+_ref = {cpg:.3f}  c-_ref = {cmg:.3f}")
print("   M2: " + ("SURVIVES -- the massive-cell pace is ARCHIMEDEAN (unconditional)"
                   if m2 else "pace differs -- arithmetic component in the rate (report)"))

print("\n== M3: the seam contrast ==")
lams = np.array([la for la, _ in fam])
R0s = np.array([REF[(la, 'family')]["R0"] for la, _ in fam])
if np.all(R0s > 0):
    co = np.polyfit(np.log(lams), np.log(R0s), 1)
    print(f"   no-prime seam: R0 = {R0s.round(4)}  power-fit p_ref = {-co[0]:.2f} "
          f"(rms {np.std(np.log(R0s)-np.polyval(co,np.log(lams))):.3f})  | true p = 3.20")
else:
    print(f"   no-prime seam R0 values: {R0s}")

print("\n== M4: criterion test (lam=2.2, N=27 vs N=40) ==")
a, b = REF[(2.2, 'family')], REF[(2.2, 'alt-bw')]
print(f"   R+ {a['Rp']:.4e} -> {b['Rp']:.4e}   R- {a['Rm']:.4e} -> {b['Rm']:.4e}   "
      f"R0 {a['R0']:.4f} -> {b['R0']:.4f}")

np.savez(HERE + "pinfF_memory_rate.npz",
         lams=lams, Rp=np.array([REF[(la,'family')]['Rp'] for la,_ in fam]),
         Rm=np.array([REF[(la,'family')]['Rm'] for la,_ in fam]), R0=R0s,
         psd=np.array([REF[(la,'family')]['psd'] for la,_ in fam]))
print("\nARCHIVED: pinfF_memory_rate.npz")
