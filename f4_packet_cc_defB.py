"""
F4, approach B: rational-CFT / lattice-vertex-algebra central charge of the
Z/N conductor-packet algebra. INDEPENDENT of approach A (anomaly / c-hat counting).

Question: under the MOST NATURAL CFT/lattice assignments, what central charge
does the Z/6 and Z/30 packet structure carry, and does the carry-packet
('internal', conductor-N) sub-sector reproduce the magic number 6 = c-hat_internal
= dim_R(O) - dim_R(C)?

EXACT ARITHMETIC ONLY (sympy Rational). No torch. No floats for the verdicts.

We evaluate every NATURAL rational-CFT central charge tied to N, with NO fitting,
and check each candidate against the two targets the bridge predicts:
  TARGET-1 (whole algebra): c = 1   (compact boson; the program's own Cor. 9.6 claim)
  TARGET-2 (carry / internal sub-sector): c_internal = 6
We are paranoid skeptics: we list which assignments HIT and which MISS, and we
do NOT let a near-miss masquerade as a hit. We also record the brane/magic ladder.
"""

import sympy as sp

def parafermion_c(N):
    # Fateev-Zamolodchikov Z_N parafermion = SU(2)_N / U(1) coset
    # c = 2(N-1)/(N+2)
    return sp.Rational(2*(N-1), N+2)

def su2_level_k_c(k):
    # SU(2)_k WZW central charge c = 3k/(k+2)
    return sp.Rational(3*k, k+2)

def u1_coset_check(k):
    # parafermion as SU(2)_k WZW (c=3k/(k+2)) minus U(1) (c=1)
    return su2_level_k_c(k) - 1

def lattice_voa_c_rank(rank):
    # lattice VOA of rank r: c = r (one free boson per lattice dimension)
    return sp.Integer(rank)

def euler_phi(n):
    return sp.totient(n)

def divisors(n):
    return sp.divisors(n)

# ---- the program's packet decomposition, by conductor ----
# For R = Z/N, character index k in 0..N-1, conductor c(k) = N/gcd(k,N).
# Drop k=0 (gauge, killed by sum u_a = 0). Group nonzero indices by conductor d|N, d>1.
# real dim of conductor-d packet = #{k : N/gcd(k,N) = d} = phi(d).
def conductor_packets(N):
    packets = {}
    for k in range(1, N):
        d = N // sp.gcd(k, N)
        packets.setdefault(int(d), []).append(k)
    return packets

print("="*78)
print("F4 / approach B : rational-CFT central charge of the Z/N packet algebra")
print("="*78)

for N in (6, 30):
    print()
    print("#"*78)
    print(f"  R = Z/{N}")
    print("#"*78)
    pk = conductor_packets(N)
    total_dim = sum(len(v) for v in pk.values())
    print(f"  conductor packets (d -> indices), dim = phi(d):")
    for d in sorted(pk):
        print(f"    conductor {d:>3}: indices {pk[d]}  (real dim phi({d}) = {euler_phi(d)}, "
              f"actual {len(pk[d])})")
    print(f"  total tangent dim dim H_{N} = {total_dim}  (should be N-1 = {N-1})")
    assert total_dim == N-1

    # carry / 'internal' packet = full-conductor packet d = N (indices coprime to N)
    carry = pk.get(N, [])
    print(f"  carry packet M (conductor-{N}, the 'internal' sector): indices {carry}")
    print(f"     dim M = phi({N}) = {euler_phi(N)}")

    print("  --- NATURAL rational-CFT central-charge assignments (no fitting) ---")
    # (1) compact boson c=1 (whole algebra as a single c=1 boson / U(1) current algebra)
    print(f"   (1) compact boson / U(1) current algebra            c = 1")
    # (2) lattice VOA of rank = total tangent dim
    print(f"   (2) lattice VOA, rank = dim H_{N} = {total_dim}        c = {lattice_voa_c_rank(total_dim)}")
    # (3) lattice VOA, rank = number of packets
    npack = len(pk)
    print(f"   (3) lattice VOA, rank = #packets = {npack}              c = {lattice_voa_c_rank(npack)}")
    # (4) Z_N parafermion coset c = 2(N-1)/(N+2)
    pf = parafermion_c(N)
    print(f"   (4) Z_{N} parafermion (SU(2)_{N}/U(1))   c = 2*{N-1}/{N+2} = {pf} = {sp.nsimplify(pf)} "
          f"~ {float(pf):.6f}")
    # (5) SU(2)_N WZW
    print(f"   (5) SU(2)_{N} WZW                            c = 3*{N}/{N+2} = {su2_level_k_c(N)} "
          f"~ {float(su2_level_k_c(N)):.6f}")
    # (6) carry-packet as its own lattice VOA of rank phi(N)
    print(f"   (6) carry packet as lattice VOA, rank phi({N}) = {euler_phi(N)}   c_internal = {euler_phi(N)}")
    # (7) carry-packet as rank = #carry-conductor indices (= phi(N), same here)
    # (8) sum of phi(d) over d|N, d>1 (= N-1 again); over PROPER nontrivial = ?
    sopf = sum(euler_phi(d) for d in divisors(N) if d > 1)
    print(f"   (8) sum_{{d|{N}, d>1}} phi(d) = {sopf}  (= N-1, sanity)")

    # TARGET CHECKS
    print("  --- target checks (paranoid) ---")
    print(f"   TARGET-1  whole-algebra c == 1 ?")
    print(f"      compact boson:        1 == 1   -> HIT")
    print(f"      lattice rank=dimH:    {total_dim} == 1   -> {'HIT' if total_dim==1 else 'MISS'}")
    print(f"      parafermion:          {pf} == 1   -> {'HIT' if pf==1 else 'MISS'}")
    print(f"   TARGET-2  carry/internal c == 6 ?")
    print(f"      phi({N}) = {euler_phi(N)}:  {euler_phi(N)} == 6  -> {'HIT' if euler_phi(N)==6 else 'MISS'}")

# ---- the magic / brane / division-algebra ladder, exact ----
print()
print("#"*78)
print("  Magic-dimension ladder cross-check (division algebras)")
print("#"*78)
K = {'R':1, 'C':2, 'H':4, 'O':8}
print("  critical D = dim_R(K) + 2 :", {k: v+2 for k,v in K.items()})
print("  brane    D = dim_R(K) + 3 :", {k: v+3 for k,v in K.items()})
print(f"  program 3+1 = C rung (D=4); superstring = O rung (D=10)")
print(f"  gap = dim O - dim C = 8 - 2 = {8-2}  (= c-hat_internal target)")
print(f"  superstring split: c-hat = 10 = 4 (spacetime) + 6 (internal); internal = {10-4}")

# ---- decisive interpretive table ----
print()
print("#"*78)
print("  DECISIVE READOUT")
print("#"*78)
print("""  The compact-boson assignment (c=1) is the ONLY natural whole-algebra
  assignment that reproduces the program's own structural c=1 (Cor. 9.6) AND
  matches a c-hat=1 boson per dimension. The parafermion/WZW values are NOT 1
  and do NOT trend to 1, so the bridge does NOT rest on the parafermion coset.
  The internal/magic 6 appears ONLY for N with phi(N)=6, i.e. N in {7,9,14,18}.
  phi(6)=2  != 6  and  phi(30)=8 != 6 . So the carry packet of Z/6 or Z/30 does
  NOT carry 6 under the lattice/Euler-phi assignment. The '6' of the bridge is
  the division-algebra gap dim_R(O)-dim_R(C), NOT a packet dimension.""")
print(f"  phi values: phi(6)={euler_phi(6)}, phi(7)={euler_phi(7)}, phi(9)={euler_phi(9)}, "
      f"phi(14)={euler_phi(14)}, phi(18)={euler_phi(18)}, phi(30)={euler_phi(30)}")
phi6_eq6 = euler_phi(6)==6
phi30_eq6 = euler_phi(30)==6
print(f"  carry-packet-gives-6 (Z/6):  {phi6_eq6}")
print(f"  carry-packet-gives-6 (Z/30): {phi30_eq6}")
print("DONE")
