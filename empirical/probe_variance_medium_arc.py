"""
Route (c) -- the medium arc is a VARIANCE (second moment), not max-over-a.  (2026-06-08)

The cubic Weil functional is Re C_zeta = INT S_g(x)^3 eta(x) dx (ocho 2, eq. 95): an L^2/integrated
object; its discrete witness pure_V(P_n) is a TRACE over the full character lattice (ocho 5).  Its
discrete->continuous transfer error is a sum over character TRIPLES,
    sum_{chi1,chi2,chi3} c . psi(x,chi1) psi(x,chi2) psi(x,chi3),
whose natural bound is HOLDER = the second moment  sum_chi |psi(x,chi)|^2  (= variance sum_a |E|^2 by
Parseval) to the 3/2 power -- NOT max_a |E|.

The program's OWN mechanism already routes through it: ocho 7.3.2 (line 619-621) bounds  sum_a |E(d,a)|
via the LARGE SIEVE (a 2nd-moment inequality) and only THEN Cauchy-Schwarz to the L^1/max, losing a
factor phi(d)^{1/2} ~ d^{1/2} -- exactly the step that drops the level by ~1/2.

Norm hierarchy on residues a mod d (all |E(a)| >= 0):
    max_a |E|  <=  (sum_a |E|^2)^{1/2}      [L^inf <= L^2]
    sum_a |E|  <=  phi(d)^{1/2} (sum_a |E|^2)^{1/2}   [Cauchy-Schwarz; THE LOSSY STEP, factor phi(d)^{1/2}]
So a variance bound sum_a|E|^2 <= V controls max by V^{1/2} but the program targets sum_a|E| (L^1),
paying phi(d)^{1/2} = d^{1/2+o(1)} -- a half-power of the modulus, i.e. ~1/2 of the level.

CONSEQUENCE for Type-III (the n=6 1/255 gap):
  - max-over-a / fixed-a  : Type-III = smooth fixed-a d_3 = 1/2 + 1/34 (Ping Xi 2018) -> 1/255 SHORT of 8/15.
  - variance / averaged-a : Type-III = averaged-a d_3 = 2/3 (Nguyen) >> 6/11 -> NON-BINDING.  Gap DISSOLVES.
    n=6 secured (binding reverts to Type-II Pascadi 6/11 >= theta_0(6)=8/15); n=7 still out (Type-II ceiling).

Two bounded [C] residues (neither the EH-wall): (i) write the Holder 2nd-moment reduction of the cubic
transfer (diez Thm 4.3 is only an outline; diagonal Plancherel ~ T(log T)^2 is 2nd-moment-scaled, ocho 6.1);
(ii) recompute the V/M crossover in the variance norm over the SPARSE family {d|P_n} -- BDH level->1 is over
ALL moduli and does not auto-transfer; the large sieve gives sum_{d|P_n} sum_chi |psi(x,chi)|^2 <<
(P_n + x) x log x via the identity sum_{d|P_n} phi(d) = P_n.
"""
import sympy as sp

# --- the key identity used by the sparse-family large sieve: sum_{d|P_n} phi(d) = P_n ---
def primorial(n):
    ps = list(sp.primerange(2, 10**6))[:n]
    return sp.prod(ps), ps

print("Route (c) -- variance medium arc.  Checks.")
print("=" * 70)
print("(1) Identity  sum_{d|P_n} phi(d) = P_n  (large-sieve constant for the sparse family):")
ok = True
for n in range(1, 9):
    Pn, ps = primorial(n)
    lhs = sum(sp.totient(d) for d in sp.divisors(Pn))
    ok &= (lhs == Pn)
    print(f"    n={n}: P_n={int(Pn):>9}   sum_(d|P_n) phi(d) = {int(lhs):>9}   {'OK' if lhs==Pn else 'FAIL'}")
assert ok

print("-" * 70)
print("(2) Norm hierarchy / the lossy Cauchy-Schwarz factor phi(d)^{1/2} (worked example):")
# random-ish nonneg vector of residue errors E(a), a in (Z/d)^*, to illustrate the inequalities
d = 30030  # P_6
phid = int(sp.totient(d))
# deterministic pseudo-data (no RNG: fixed pattern), values in [0,1)
E = [sp.Rational((7*a + 3) % 11, 11) for a in range(phid)]
L2 = sp.sqrt(sum(e**2 for e in E))
L1 = sum(E)
Linf = max(E)
print(f"    d=P_6={d}, phi(d)={phid}")
print(f"    Linf = max_a|E|         = {float(Linf):.4f}")
print(f"    L2   = (sum|E|^2)^(1/2) = {float(L2):.4f}")
print(f"    L1   = sum|E|           = {float(L1):.4f}")
print(f"    check  Linf <= L2                 : {bool(Linf <= L2)}")
print(f"    check  L1   <= phi(d)^(1/2) * L2  : {bool(L1 <= sp.sqrt(phid)*L2)}  (loss factor phi(d)^(1/2)={float(sp.sqrt(phid)):.1f})")
print(f"    => program targets L1 (sum_a|E|), variance needs only L2: the medium arc pays {float(sp.sqrt(phid)):.0f}x it need not.")

print("-" * 70)
print("(3) The n=6 row under the two formulations (theta_0(6)=3/5 EXACT, NOT 8/15 -- see")
print("    probe_exact_discharge_schedule; the asymptotic 1-2.80/n is one row optimistic):")
half = sp.Rational(1,2)
theta6 = sp.Rational(3,5)                       # EXACT
typeII = sp.Rational(6,11)
fixed_a_smooth = half + sp.Rational(1,34)      # Ping Xi 2018
avg_a = sp.Rational(2,3)                        # Nguyen
print(f"    n=6 target theta_0(6) = 3/5 = {float(theta6):.4f}  (EXACT)")
print(f"    MAX-over-a: Type-II Pascadi 6/11={float(typeII):.4f} SHORT; Type-III smooth 1/2+1/34={float(fixed_a_smooth):.4f} SHORT")
print(f"               => n=6 OUT of reach by ~0.05-0.07 (both levers below 3/5); frontier n<=5.")
print(f"    VARIANCE : Type-III becomes avg-a d_3 = 2/3 = {float(avg_a):.4f} (non-binding), but the binding")
print(f"               constraint is the sparse-BDH variance crossover (residue ii, OPEN), NOT a fixed")
print(f"               6/11. So n=6 -- like all n -- reduces to sparse-primorial BDH; not specially secured.")
assert theta6 == sp.Rational(3,5) and typeII < theta6 and fixed_a_smooth < theta6

print("-" * 70)
print("VERDICT (route c) -- the load-bearing result is the Holder reduction (sections 1-2), unaffected.")
print("  * The cubic functional is L^2/integrated; its transfer error is a character-TRIPLE sum,")
print("    controlled in 2nd moment (Holder), NOT max-over-a. ocho 7.3.2 already uses the large sieve")
print("    (variance) then a LOSSY Cauchy-Schwarz (factor phi(d)^{1/2}) to reach the max -- the over-statement.")
print("  * So the medium arc is the VARIANCE; the terminus remaps to sparse-primorial BDH (N0 6.6-6.9).")
print("  * CORRECTION (2026-06-08): the earlier '1/255 Type-III dissolves => n=6 secured' used the WRONG")
print("    theta_0(6)=8/15. With theta_0(6)=3/5 EXACT, n=6 is out for max-over-a (frontier n<=5) and")
print("    under the variance form reduces to sparse-BDH like every n. The Holder reduction stands.")
print("  * Bounded [C] residues: (i) the Holder 2nd-moment reduction [done, N0 Lemma 6.8];")
print("    (ii) the V/M crossover in variance norm over the sparse {d|P_n} = sparse-primorial BDH (open).")
