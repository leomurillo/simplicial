"""probe_pinfG_sos_bridge.py -- P-inf-G strike 2: the exact square/Moebius form of the
parity bridge (Theorem G.5) certified.

HEAD-MATH (derived before this probe; the probe is the certificate):
From Thm F.27(b)  d_std = Var(t) - Cov(t,u)^2/Var(u)  with
  Var(t) = v0/2 + (d+ + d-)/4 + G,  Cov(t,u) = [(d+ - d-)/2 + G]/sqrt2,
  Var(u) = (d+ + d-)/2,  G = gamma/sqrt2,  d0 = v0 - gamma^2/d+ ,
substituting s = d+ + d- and (d+ - d-)/2 + G = (d+ + G) - s/2 gives the CLOSED FORMS

  (G.5a)  d_std = v0/2 + d+ + 2G - (d+ + G)^2/(d+ + d-)          [exact]
  (G.5b)  d_std - d0/2 = (d+ + G)^2 * d- / (d+ (d+ + d-))        [exact -- NO O(d-^2)]
  (G.5c)  d(d_std)/d(d-) = (1/2 + Y)^2,  Y = ((d+ - d-)/2 + G)/(d+ + d-)   [a square]

CONSEQUENCES (stated in P-inf-G section 8): given even-sector positivity (d+ > 0,
Var(u) > 0), sign(d_std - d0/2) = sign(d-); the certified mixed ledger is an EXACT
chiral-sign certificate; the square degenerates exactly at g = G/d+ = -1 = the measured
lam=1.5 kappa-transient (F.27, retro-explained); the per-arrival increment of the
certified excess routes ALL sign content through the single chiral scalar delta(d-).

PRE-REGISTERED:
  B1: (G.5a) and (G.5b) hold on the certified parity_totals.npz values at all six
      windows to <= 1e-10 relative (float64 grade; the inputs were mp-certified at V7
      to 7.1e-32, and G.5 is algebraically equivalent, so float residuals here are
      pure storage rounding).  FALSIFIER: residual > 1e-8 at any window -> my algebra
      is wrong; retract G.5.
  B2 (mp spot check): rebuild lam=2.0 (dps 50, certified parity machinery inlined from
      probe_pinfF_parity_totals.py) and verify (G.5a)/(G.5b) to <= 1e-30.
  B3 (reading): kappa_exact = (d+ + G)^2/(d+ (d+ + d-)) per window vs F.27's constant
      (1+g)^2; the Moebius correction = the probe's measured sum/d_std deficit.
"""
import sys
import numpy as np
import mpmath as mp

sys.stdout.reconfigure(encoding="utf-8")
HERE = "empirical/p_infinity/"

z = np.load(HERE + "parity_totals.npz")
lams = z["lams"]
dp, dm, gam, v0 = z["d_plus"], z["d_minus"], z["gamma"], z["v0"]
d0, dstd = z["d0"], z["d_std"]

print("== B1: G.5 closed forms on the certified six windows (float lift) ==")
G = gam / np.sqrt(2)
lhs_a = dstd
rhs_a = v0 / 2 + dp + 2 * G - (dp + G) ** 2 / (dp + dm)
res_a = np.abs(lhs_a - rhs_a) / np.abs(lhs_a)
lhs_b = dstd - d0 / 2
rhs_b = (dp + G) ** 2 * dm / (dp * (dp + dm))
res_b = np.abs(lhs_b - rhs_b) / np.maximum(np.abs(lhs_b), 1e-300)
print("   lam    res(G.5a)    res(G.5b)    kappa_exact   (1+g)^2     d_std-d0/2")
for i, l in enumerate(lams):
    kex = (dp[i] + G[i]) ** 2 / (dp[i] * (dp[i] + dm[i]))
    g_ = G[i] / dp[i]
    print(f"   {l:4}  {res_a[i]:.2e}    {res_b[i]:.2e}    {kex:9.4f}    {(1+g_)**2:9.4f}"
          f"   {lhs_b[i]:+.4e}")
b1 = bool(np.all(res_a <= 1e-8) and np.all(res_b <= 1e-8))
print("   B1: " + ("SURVIVES (identities exact at storage grade)" if b1
                   else "FIRED -- algebra wrong, retract G.5"))

print("\n== B2: mp spot check at lam=2.0 (dps 50, certified machinery) ==")
def primes_upto(xx):
    out = []; n = 2
    while n <= xx:
        if all(n % p for p in out):
            out.append(n)
        n += 1
    return out


src4 = open(HERE + "probe_pinfF_wave_limit.py", encoding="utf-8").read()
exec(src4[src4.index("def build_QW_mp"):src4.index("def analyze")])   # build_QW_mp
mp.mp.dps = 50
lam, N = 2.0, 24
dim = 2 * N + 1
Q, Lmp = build_QW_mp(mp.mpf("2.0"), N)
B = mp.zeros(dim, dim)
for n in range(dim):
    for i in range(dim):
        B[n, i] = mp.e**(2j * mp.pi * (n - N) * i / dim) / mp.sqrt(dim)
Kc = (B.H) * Q * B
K = [[(mp.re(Kc[i, j]) + mp.re(Kc[j, i])) / 2 for j in range(dim)] for i in range(dim)]


def schur_quads(Alist, rhs_list):
    nloc = len(Alist)
    A = mp.zeros(nloc, nloc)
    for i in range(nloc):
        for j in range(nloc):
            A[i, j] = Alist[i][j]
    sols = []
    for v in rhs_list:
        b = mp.matrix(nloc, 1)
        for i in range(nloc):
            b[i] = v[i]
        sols.append(mp.lu_solve(A, b))
    return [[mp.fsum(rhs_list[a][i] * sols[b2][i] for i in range(nloc))
             for b2 in range(len(rhs_list))] for a in range(len(rhs_list))]


sq2 = mp.sqrt(2)
m = (dim - 1) // 2
d_ = dim
idx_in = list(range(2, m + 1))
Mp_ = [[(K[k][l] + K[k][d_ - l] + K[d_ - k][l] + K[d_ - k][d_ - l]) / 2
        for l in idx_in] for k in idx_in]
Mm_ = [[(K[k][l] - K[k][d_ - l] - K[d_ - k][l] + K[d_ - k][d_ - l]) / 2
        for l in idx_in] for k in idx_in]
qp = [(K[k][1] + K[k][d_ - 1] + K[d_ - k][1] + K[d_ - k][d_ - 1]) / 2 for k in idx_in]
qm = [(K[k][1] - K[k][d_ - 1] - K[d_ - k][1] + K[d_ - k][d_ - 1]) / 2 for k in idx_in]
bare_p = (K[1][1] + K[1][d_ - 1] + K[d_ - 1][1] + K[d_ - 1][d_ - 1]) / 2
bare_m = (K[1][1] - K[1][d_ - 1] - K[d_ - 1][1] + K[d_ - 1][d_ - 1]) / 2
w0 = [(K[k][0] + K[d_ - k][0]) / sq2 for k in idx_in]
GP = schur_quads(Mp_, [qp, w0])
d_plus = bare_p - GP[0][0]
d_minus = bare_m - schur_quads(Mm_, [qm])[0][0]
c01 = (K[0][1] + K[0][d_ - 1]) / sq2
gamma = c01 - GP[0][1]
v0_ = K[0][0] - GP[1][1]
d0_ = v0_ - gamma**2 / d_plus
# the certified standard-cut edge objects (orientation as in parity_totals)
x = np.arange(dim) * float(Lmp) / dim
s_ = np.abs(x - float(Lmp) / 2)
order = np.argsort(s_, kind="stable")
pair = [int(i) for i in order[dim - 2:]]
p0_, p1_ = pair
bare = (K[p0_][p0_] + K[p1_][p1_]) / 2 + K[p0_][p1_]
interior = [int(i) for i in order[:dim - 2]]
q = [(K[i][p0_] + K[i][p1_]) / sq2 for i in interior]
Aint = [[K[i][j] for j in interior] for i in interior]
d_std_exact = bare - schur_quads(Aint, [q])[0][0]
Gm = gamma / sq2
rhs_a = v0_ / 2 + d_plus + 2 * Gm - (d_plus + Gm)**2 / (d_plus + d_minus)
rhs_b = (d_plus + Gm)**2 * d_minus / (d_plus * (d_plus + d_minus))
ra = abs((d_std_exact - rhs_a) / d_std_exact)
rb = abs(((d_std_exact - d0_ / 2) - rhs_b) / (d_std_exact - d0_ / 2))
print(f"   d_std (direct Schur)   = {mp.nstr(d_std_exact, 12)}")
print(f"   G.5a closed form       = {mp.nstr(rhs_a, 12)}   rel = {float(ra):.1e}")
print(f"   excess d_std - d0/2    = {mp.nstr(d_std_exact - d0_/2, 12)}")
print(f"   G.5b closed form       = {mp.nstr(rhs_b, 12)}   rel = {float(rb):.1e}")
b2 = float(ra) <= 1e-30 and float(rb) <= 1e-30
print("   B2: " + ("SURVIVES (mp-exact)" if b2 else "FIRED -- check orientation/algebra"))

print("\nRESULT: " + ("GREEN -- Theorem G.5 certified (closed-form square/Moebius bridge)"
                      if (b1 and b2) else "FIRED -- diagnose before landing G.5"))
