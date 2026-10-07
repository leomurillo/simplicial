"""
probe_primepower_transfer_p2.py  --  (a) prime-power test, (b) transfer constant, (c) the real p=2.

(a) PRIME-POWER TEST (phi vs coprimality, the decisive one):
    The per-prime keystone weight is 1/(p-1)^n. Is p-1 the conductor-block dimension phi(p) (our
    object) or just the coprimality count? They COINCIDE at primes; they SPLIT at prime powers
    (phi(p^k)=p^{k-1}(p-1) != p-1). Resolution: the HL singular series is per-prime (residues mod p),
    hence SQUAREFREE; the program's cubic is squarefree-closed (paper 17 Constraint 3). On squarefree
    N, phi(N)=prod(p-1)=the HL product EXACTLY. So the distinction is moot on the shared domain ->
    CONFIRMS the conductor-block identification (does not kill it).

(b) TRANSFER CONSTANT: race the CORRECT connected HL cumulant vs the apex cumulant, n=2,3.
(c) THE REAL p=2: the user's (p-2)^2 vanishing is an artifact; find the genuine p=2 subtlety.

sympy exact. No torch.
"""
import sympy as sp
import itertools

print("=" * 84)
print("(a) PRIME-POWER TEST: phi(squarefree)=prod(p-1)=HL product;  phi(p^k) != p-1")
print("=" * 84)
print("  squarefree N: conductor-block dim phi(N) vs HL coprimality product prod_{p|N}(p-1):")
for N, ps in [(6, [2, 3]), (30, [2, 3, 5]), (105, [3, 5, 7]), (210, [2, 3, 5, 7])]:
    phi = int(sp.totient(N))
    prod = int(sp.prod([p - 1 for p in ps]))
    print(f"    N={N:>4} (={'*'.join(map(str,ps))}):  phi(N)={phi:>3}   prod(p-1)={prod:>3}   equal? {phi==prod}")
print("  prime powers: phi(p^k) = p^(k-1)(p-1) != (p-1) -> phi and coprimality SPLIT here:")
for q in [4, 8, 9, 25, 27]:
    p = sp.factorint(q); pp = int(list(p.keys())[0])
    print(f"    q={q:>3} (={pp}^{p[sp.Integer(pp)]}):  phi={int(sp.totient(q)):>3}   (p-1)={pp-1:>3}   differ? {int(sp.totient(q))!=pp-1}")
print("  HL local factor uses nu_p = #residues mod p (NOT mod p^2): the singular series is per-prime,")
print("  i.e. SQUAREFREE. The program's cubic is squarefree-closed (paper 17 Constr.3). So both live on")
print("  squarefree support, where phi(N)=prod(p-1)=HL EXACTLY. => conductor-block identification CONFIRMED;")
print("  the phi-vs-coprimality split (prime powers) is excluded by the program's own squarefree closure.")

print("\n" + "=" * 84)
print("(b) TRANSFER CONSTANT: connected HL cumulant vs apex cumulant (CORRECT objects)")
print("=" * 84)
def loc(nu, p, k): return (1 - sp.Rational(nu, p)) / (1 - sp.Rational(1, p))**k
m = sp.symbols('m', positive=True)
print(f"  {'order n':>8} {'HL connected':>16} {'apex cumulant (m=p-1)':>22} {'|ratio|':>8} {'sign':>6}")
# n=2: HL T2 = w2 - 1 ; apex Sigma off-diag = -1/m^2
for p in [3, 5, 7]:
    hl2 = sp.nsimplify(sp.simplify(loc(2, p, 2) - 1))
    ap2 = sp.Rational(-1, (p - 1)**2)
    print(f"  n=2 p={p}:  {str(hl2):>14} {str(ap2):>22} {str(sp.Abs(hl2/ap2)):>8} {'same' if sp.sign(hl2)==sp.sign(ap2) else 'opp':>6}")
# n=3: HL T3 = w3 - 3 w2 + 2 ; apex T_ijk all-distinct = +2/m^3
for p in [3, 5, 7]:
    hl3 = sp.nsimplify(sp.simplify(loc(3, p, 3) - 3 * loc(2, p, 2) + 2))
    ap3 = sp.Rational(2, (p - 1)**3)
    print(f"  n=3 p={p}:  {str(hl3):>14} {str(ap3):>22} {str(sp.Abs(hl3/ap3)):>8} {'same' if sp.sign(hl3)==sp.sign(ap3) else 'opp':>6}")
print("""  => MAGNITUDE transfer constant = 1 EXACTLY at n=2 and n=3 (HL connected and apex cumulant have
     equal magnitude 1/(p-1)^2 and 2/(p-1)^3). The SIGN: n=2 same (the metric, alpha-independent);
     n=3 opposite. That sign is NOT free: it is the Amari dual-connection (the cubic enters the
     e-/m-connections as Gamma = Gamma^LC -/+ (alpha/2) T, T2 sec.4) -- the m-connection (alpha=-1)
     carries the HL sign. So the 'transfer constant' = magnitude 1, sign = the dual-flat connection.
     (The message's '1, 1/2' came from its incorrect W_HL; the real answer is cleaner.)""")

print("\n" + "=" * 84)
print("(c) THE REAL p=2: the (p-2)^2 vanishing is an ARTIFACT; the genuine subtlety is ADMISSIBILITY")
print("=" * 84)
hl3_p2 = sp.nsimplify(sp.simplify(loc(3, 2, 3) - 3 * loc(2, 2, 2) + 2))
print(f"  connected HL 3-cumulant at p=2 (= -2/(p-1)^3 at p=2) = {hl3_p2}  -> NOT 0; the cubic is MOST")
print(f"  active at p=2 (smallest (p-1)). So the message's 'annihilation at p=2' is false.")
# genuine p=2: admissibility of a 3-tuple {0,h1,h2} mod 2 (inadmissible if it covers both parities)
adm = inadm = 0
for h1, h2 in itertools.product(range(2), repeat=2):
    nu2 = len({0, h1 % 2, h2 % 2})
    if nu2 == 2: inadm += 1
    else: adm += 1
print(f"  REAL p=2 subtlety = ADMISSIBILITY: of the 4 patterns of {{0,h1,h2}} mod 2, {inadm} cover both")
print(f"  parities ( INADMISSIBLE -- always contain an even, never all prime) and {adm} are admissible.")
print(f"  This is the genuine 'p=2 is special' (cf. the twin-prime p=2 factor of 2) -- a restriction on")
print(f"  WHICH tuples contribute, NOT a vanishing of the cubic weight. The message pointed at the right")
print(f"  prime (p=2 special) but the wrong mechanism ((p-2)^2 zero vs admissibility).")

print("\n" + "=" * 84)
print("VERDICT (a)+(b)+(c)")
print("=" * 84)
print("""  (a) CONFIRMED: phi(squarefree N)=prod(p-1)=HL product exactly (6,30,105,210 checked); phi(p^k)
      splits from (p-1) only at prime powers, which the squarefree-closed cubic (paper 17) excludes.
      The conductor-block dimension phi IS the source of the n-level weight, on the shared squarefree
      domain. Identification stands -- not killed.
  (b) TRANSFER = magnitude 1 (exact, n=2,3) with sign = the Amari dual (m-)connection. Not a free
      constant; fixed by the dual-flat geometry. The '1,1/2' of the message was an artifact.
  (c) The (p-2)^2 p=2 blind spot is FALSE (cubic is -2, maximal, at p=2). The real p=2 subtlety is
      admissibility (3/4 mod-2 patterns inadmissible), like the twin-prime p=2 factor -- a different,
      genuine statement.
  NET: the keystone is the clean per-prime identity HL connected = -2/(p-1)^3, apex K^CH = +2/(p-1)^3
  (magnitude 1/phi(p)^n both sides, sign = dual connection), on squarefree support. NO (p-2)^2.""")
