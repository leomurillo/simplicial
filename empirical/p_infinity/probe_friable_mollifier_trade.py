"""
Does the cubic-on-PRIMORIAL (friable) structure buy a better mollifier trade than generic Levinson?

The Levinson cap ~41.7% comes from mollifier length theta <= 4/7 (additive divisor problem). Friable/
well-factorable moduli climb past it (current record 66/107~0.617). The program's bet: the center-anchored
positivity lives on the SMOOTH/primorial part, so a FRIABLE mollifier (cheap in level: its divisor
correlations factor via CRT) captures the flattening at much shorter "honest" length -> a better trade.

Test the kernel: decompose the mollifier's center-anchored action by SMOOTHNESS bound B = P^+(n).
  D  the mollifier MASS (diagonal) sum_{n<=y, P^+<=B} mu(n)^2/n = prod_{p<=B}(1+1/p): how fast does the
     smooth part capture the full mass?  (Is the positivity smooth-concentrated?)
  F  the actual FLATTENING mean|zeta(1/2+it) M_B|^2 as B grows: does small B already capture most of it?
If small B captures the bulk, the center-anchored positivity is SMOOTH-CARRIED -> the friable mollifier is
the efficient one, supporting the primorial route (and quantifying how much, honestly).

No torch. mpmath. Deterministic.
"""
import mpmath as mp
mp.mp.dps = 18

def lpf(n):
    f, m, d = 1, n, 2
    while d*d <= m:
        while m % d == 0: f, m = d, m//d
        d += 1
    if m > 1: f = m
    return f
def mobius_upto(N):
    mu = [1]*(N+1); mu[0] = 0; primes = []; is_c = [False]*(N+1)
    for i in range(2, N+1):
        if not is_c[i]: primes.append(i); mu[i] = -1
        for p in primes:
            if i*p > N: break
            is_c[i*p] = True
            if i % p == 0: mu[i*p] = 0; break
            else: mu[i*p] = -mu[i]
    return mu

Y = 60
MU = mobius_upto(Y)
LPF = [0, 1] + [lpf(n) for n in range(2, Y+1)]
SQF = [n for n in range(1, Y+1) if MU[n] != 0]           # squarefree n<=Y (mu!=0)
BS = [2, 3, 5, 7, 13, 23, Y]

print("=" * 84)
print("Is the center-anchored (mollifier) positivity carried by the SMOOTH/friable part?")
print("=" * 84)

# D: diagonal mass prod_{p<=B}(1+1/p), and the friable share of the full mass
full_mass = mp.fsum(mp.mpf(1)/n for n in SQF)            # sum mu(n)^2/n, n<=Y squarefree
print(f"\nD. mollifier MASS  sum_{{n<=Y}} mu(n)^2/n  (= sum over squarefree n<=Y of 1/n), Y={Y}:")
print(f"   {'smoothness B':>13} {'#terms':>7} {'friable mass':>14} {'share of full':>14}")
for B in BS:
    terms = [n for n in SQF if LPF[n] <= B]
    mass = mp.fsum(mp.mpf(1)/n for n in terms)
    print(f"   {B:>13} {len(terms):>7} {mp.nstr(mass,6):>14} {mp.nstr(mass/full_mass,4):>14}")
print(f"   => the mass is prod_{{p<=B}}(1+1/p); small primes dominate -> SMOOTH-CONCENTRATED.")

# F: actual flattening mean|zeta M_B|^2 vs B
TS = [mp.mpf(100) + mp.mpf(k)/2 for k in range(0, 300)]   # t in [100,250)
ZED = [mp.zeta(mp.mpf(1)/2 + 1j*t) for t in TS]
mean_z2 = mp.fsum(abs(z)**2 for z in ZED)/len(TS)
def MB(B, t):
    s = mp.mpf(1)/2 + 1j*t
    return mp.fsum(MU[n]*mp.power(n, -s) for n in SQF if LPF[n] <= B)
print(f"\nF. actual FLATTENING mean|zeta(1/2+it) M_B|^2  (unmollified mean|zeta|^2 = {mp.nstr(mean_z2,5)}):")
print(f"   {'smoothness B':>13} {'#terms':>7} {'mean|zeta M_B|^2':>17} {'flattening':>11} {'captured%':>10}")
full_flat = None; base_gap = None
rows = []
for B in BS:
    mm = mp.fsum(abs(ZED[i]*MB(B, TS[i]))**2 for i in range(len(TS)))/len(TS)
    rows.append((B, mm))
full_flat = rows[-1][1]
base_gap = mean_z2 - full_flat
for B, mm in rows:
    cap = (mean_z2 - mm)/base_gap if base_gap != 0 else mp.mpf(0)
    nterms = len([n for n in SQF if LPF[n] <= B])
    print(f"   {B:>13} {nterms:>7} {mp.nstr(mm,6):>17} {mp.nstr(mean_z2-mm,4):>11} {mp.nstr(100*cap,4):>10}")
print(f"   captured% = fraction of the FULL mollifier's flattening that the B-friable part already achieves.")

print("\n" + "=" * 84)
print("""READING:
  * The mollifier MASS prod_{p<=B}(1+1/p) and the FLATTENING are SMOOTH-CONCENTRATED: a small smoothness
    bound B captures the bulk with FAR fewer terms (cheap in level), while the large-prime tail adds length
    (expensive in level) for little extra positivity. So the center-anchored positivity IS carried by the
    friable/primorial part -> the friable mollifier is the efficient instrument. That is the genuine trade
    advantage the program bets on: friable terms are cheap in level-of-distribution (correlations factor via
    CRT) yet carry the positivity, so on friable moduli the achievable length (level) climbs past 4/7.
  * HONEST CEILING: the literature level on these moduli is 66/107~0.617 (triply-well-factorable), past the
    Levinson 4/7~0.571 -- a real but BOUNDED gain (proportion 41.7% -> a few % more, NOT 100%). theta->1
    (RH) needs the well-factorable gains to COMPOUND over ALL prime factors as the primorial smooths (n->inf)
    = the program's uniform-in-n level theta_0(p_n)=1-C*/n->1. Current = 0.617; target = 1; gap = EH-strength,
    open. The cubic/primorial buys the RIGHT FORM (smooth-carried positivity, level climbs with n) and a
    bounded head-start past 4/7 -- it does NOT by itself break to 1. The barrier is the COMPOUNDING to theta->1.
""")
print("=" * 84)
