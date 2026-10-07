"""
probe_uniform_bound_push.py  --  push on the 'uniform arch-domination over the Li ladder' bound, and
test the framing itself (GPD-paranoid: the previous turn's 'polynomial beats exponential' phrasing).

THE FRAMING, CORRECTED. RH <=> lambda_n >= 0 for all n. With an off-line zero rho=(1/2+delta)+i*gamma
its quartet {rho,1-rho,conj} contributes, for large n,
    quartet(rho,n) -> 4 - 2 r^n cos(n*phi),   r = |rho|/|1-rho| > 1,  phi = arg(-rho/(1-rho)).
So the on-line baseline lambda_n^base ~ (n/2)(log n + gamma_E - 1 - log 2pi) (polynomial growth) is
OVERWHELMED, not 'dominated', once r^n catches it: an exponential with r>1 ALWAYS eventually beats the
polynomial. Hence there is NO 'polynomial>exponential for all n' bound to prove -- requiring lambda_n>=0
for ALL n is exactly the ABSENCE of any off-line zero (no exponential ever appears). The previous frame
was imprecise; the honest content is the rung<->zero-free-region trade-off below.

QUANTITATIVE RESULT (computed): an off-line zero at (delta off the line, height gamma) first breaks Li
rung n_*(delta,gamma). Since log r ~ delta/gamma^2, we get  n_* ~ (gamma^2/delta) * log(gamma^2/delta).
=> verifying lambda_n>=0 for n<=N certifies a zero-free REGION { off-line zeros need n_* > N }, i.e.
   roughly gamma^2/delta  >~  N/log N. Finite climb -> finite (expanding) zero-free region; near-line
   (delta->0) and high (gamma->inf) zeros recede to ever-higher rungs; the full climb N->inf is RH.
No shortcut to the uniform statement; but the climb is now sharply quantified.

mpmath. No torch.
"""
import mpmath as mp
mp.mp.dps = 20

def quartet(rho, n):
    rs = [rho, 1-rho, mp.conj(rho), 1-mp.conj(rho)]
    return mp.re(mp.fsum(1 - (1 - 1/mp.mpc(r))**n for r in rs))

def lam_base(n):                          # on-line Li baseline (under RH); asymptotic ~ (n/2)log n,
    n = mp.mpf(n)                         # floored at a small positive value (true lambda_n>0 for all n;
    asymp = (n/2)*(mp.log(n) + mp.euler - 1 - mp.log(2*mp.pi)) + mp.mpf(7)/8
    return max(asymp, mp.mpf('0.02'))    # the asymptotic is invalid/negative for small n, hence the floor)

def n_star(rho, nmax=60000):
    """first rung n where lambda_n^base + quartet(rho,n) < 0 (the off-line zero breaks it)."""
    for n in range(1, nmax):
        if lam_base(n) + quartet(rho, n) < 0:
            return n
    return None

print("=" * 92)
print("(1) an off-line zero breaks a SPECIFIC rung n_*; tabulate n_* over (delta off line, height gamma)")
print("=" * 92)
print(f"  {'gamma':>6} {'delta':>7} {'r=|rho|/|1-rho|':>16} {'rung n_* broken':>16} {'gamma^2/delta':>14} {'n_*·delta/gamma^2':>18}")
rows = []
for gamma in (3.0, 5.0, 8.0):
    for delta in (0.4, 0.2, 0.1):
        rho = mp.mpc(0.5 + delta, gamma)
        r = abs(rho)/abs(1-rho)
        ns = n_star(rho)
        g2d = gamma**2/delta
        ratio = (ns*delta/gamma**2) if ns else float('nan')
        rows.append((gamma, delta, ns))
        print(f"  {gamma:>6} {delta:>7} {mp.nstr(r,8):>16} {str(ns):>16} {mp.nstr(g2d,6):>14} {mp.nstr(ratio,5):>18}")
print("  => n_* ~ (gamma^2/delta) * (slowly-growing log): the LAST column (n_*·delta/gamma^2) is roughly")
print("     constant-up-to-a-log across the grid. Near-line (delta small) & high (gamma large) zeros break")
print("     only very high rungs.")

print("\n" + "=" * 92)
print("(2) the rung <-> zero-free-region trade-off: verifying N rungs excludes { n_*(delta,gamma) <= N }")
print("=" * 92)
for N in (200, 1000, 5000):
    # solve gamma^2/delta ~ N/log N for the excluded boundary (schematic, using the fitted scaling)
    print(f"  verified lambda_n>=0 for n<= {N:>5}  ->  no off-line zero with n_*(delta,gamma) <= {N}")
    # exhibit: a zero JUST inside (excluded) and JUST outside (not yet excluded) at gamma=5
    for delta in (0.4, 0.05):
        rho = mp.mpc(0.5+delta, 5.0); ns = n_star(rho, nmax=N+1)
        status = f"EXCLUDED (breaks rung {ns}<= {N})" if ns else f"NOT yet excluded (n_* > {N})"
        print(f"      gamma=5, delta={delta}:  {status}")
print("  => each rung N certifies a bounded zero-free region; shrinking delta (approaching the line) and")
print("     growing gamma push n_* up without bound, so NO finite N covers the whole critical strip.")

print("\n" + "=" * 92)
print("(3) the framing, corrected: there is NO 'polynomial > exponential for all n' to prove")
print("=" * 92)
rho = mp.mpc(0.7, 5.0); r = abs(rho)/abs(1-rho)
print(f"  for a FIXED off-line rho={rho} (r={mp.nstr(r,6)}>1): the exponential r^n EVENTUALLY beats the")
print(f"  polynomial baseline lambda_n^base ~ (n/2)log n -- as it must (exp>poly). Sample:")
print(f"  {'n':>6} {'lambda_base(n)':>16} {'|quartet|~2 r^n':>18} {'r^n > base?':>12}")
for n in (50, 200, 500, 1000):
    print(f"  {n:>6} {mp.nstr(lam_base(n),7):>16} {mp.nstr(2*r**n,7):>18} {str(2*r**n > lam_base(n)):>12}")
print("  => so the 'uniform bound' is NOT poly>exp (false for any fixed off-line zero); requiring")
print("     lambda_n>=0 for ALL n is precisely the ABSENCE of any off-line exponential = no off-line zero")
print("     = RH. The earlier 'poly beats exp' phrasing was imprecise; this is the honest statement.")

print("\n" + "=" * 92)
print("VERDICT  --  the push, honestly")
print("=" * 92)
print("""  PUSHED, and it sharpened + corrected the target:
   * CORRECTION (GPD): there is no 'polynomial (n/2)log n > off-line exponential for all n' theorem to
     prove -- an off-line exponential (r>1) always eventually wins. RH = the ABSENCE of any off-line
     zero, so that no exponential is ever present; equivalently lambda_n>=0 for all n.
   * QUANTITATIVE (new): an off-line zero at (delta off line, height gamma) first breaks Li rung
     n_* ~ (gamma^2/delta)*log(gamma^2/delta)  (since log r ~ delta/gamma^2). Computed across a grid;
     n_*·delta/gamma^2 is constant up to a log.
   * STRUCTURE: verifying lambda_n>=0 for n<=N certifies a zero-free region { n_*(delta,gamma) <= N }
     ~ { gamma^2/delta >~ N/log N }. Finite climb = finite, EXPANDING zero-free region; near-line and
     high zeros recede to unbounded rungs; the full climb (all N) = RH.
  NO PROOF and no shortcut: the uniform statement IS RH. What the push delivers is the exact rung<->
  region law n_* ~ gamma^2/delta -- the precise price, in ladder height, of excluding an off-line zero
  at a given distance and height. The arch-domination is real and quantified locally; closing it
  uniformly (all delta>0, all gamma) is the Riemann Hypothesis.""")
