"""
F4 (approach A): a 'central charge' analogue for the program's conductor-packet
structure. Test whether the internal/carry sector reproduces c-hat_internal = 6
(the minimal super-4D internal central charge; gap = dim_R(O) - dim_R(C) = 8-2 = 6).

Exact arithmetic only (Fraction / int). numpy/sympy/pure-python.

Anchors (from corpus, verified before coding):
 - Conductor packet dim_C H_d = phi(d); orthogonal L^2(Z/N) = (+)_{d|N} H_d.
   (FaithfulnessObstruction.md sec 2.1)
 - Z/6: H_6 = A_2(+)A_3(+)M, real dims (1,2,2); A_2={3}(p=2 axis),
   A_3={2,4}(p=3 axis), M={1,5}(carry, conductor 6). (32-v0.3 sec 5.1)
 - Cubic structure constant on Z/N at centroid:
   T_klm = N^2 * sum_{a=0}^{N-1} omega^{(k+l+m)a} = N^3 * 1[k+l+m == 0 mod N].
   (32-v0.3 Lemma 5.1a:  T = 36*sum = 216*1[...] on N=6, i.e. 6^2 * 6 = 6^3.)
 - Z/30 packet atlas already in corpus (quartic_selection_z30.md):
   H_2(1),H_3(2),H_5(4),H_6(2),H_10(4),H_15(8),H_30(8).

Target number: 6 (and the superstring c-hat_total reading 10; spacetime c-hat 4).
"""
from fractions import Fraction
from math import gcd
from itertools import product as iproduct
from sympy import totient, divisors, primefactors

TARGET = 6

# ---------------------------------------------------------------------------
def conductor(k, N):
    return N // gcd(k, N)

def packets(N):
    """conductor d|N, d>1 -> sorted list of indices k in 1..N-1 with cond=d."""
    pk = {}
    for k in range(1, N):
        d = conductor(k, N)
        pk.setdefault(d, []).append(k)
    return {d: pk[d] for d in sorted(pk)}

def carry_conductors(N):
    """'carry' / cross-prime packets: conductors that are NOT prime powers (>1)
    i.e. involve >=2 distinct primes. On Z/6 that's {6}=M. On Z/30 {6,10,15,30}."""
    out = []
    for d in divisors(N):
        if d == 1:
            continue
        if len(primefactors(d)) >= 2:
            out.append(int(d))
    return out

def single_prime_conductors(N):
    """prime-power conductors > 1 (single-prime 'axes')."""
    out = []
    for d in divisors(N):
        if d == 1:
            continue
        if len(primefactors(d)) == 1:
            out.append(int(d))
    return out

# ---------------------------------------------------------------------------
# (a) DIMENSION COUNTS
# ---------------------------------------------------------------------------
def dim_candidates(N):
    pk = packets(N)
    res = {}
    carry = carry_conductors(N)
    sp = single_prime_conductors(N)

    # complex dims = phi(d); real dims = phi(d) (each H_d as real space of real combos
    # has real dim phi(d) too: phi(d) real basis functions cos/sin; matches corpus
    # "real dims (1,2,2)" = phi(2),phi(3)? NO: corpus says A_2 real dim 1=phi(2)=1,
    # A_3 real dim 2=phi(3)=2, M real dim 2=phi(6)=2. So REAL dim H_d = phi(d).)
    res['(a1) dim_C M (single carry packet, conductor=N) = phi(N)'] = int(totient(N))
    res['(a2) sum over CARRY conductors of phi(d)'] = sum(int(totient(d)) for d in carry)
    res['(a3) sum over SINGLE-PRIME conductors of phi(d)'] = sum(int(totient(d)) for d in sp)
    res['(a4) sum over ALL d|N,d>1 of phi(d) = N-1'] = sum(int(totient(d)) for d in divisors(N) if d > 1)
    res['(a5) dim of largest single-prime block max_p phi(p^{v_p})'] = max(
        (int(totient(d)) for d in sp), default=0)
    # number of carry packets, number of single-prime packets
    res['(a6) # carry packets'] = len(carry)
    res['(a7) # single-prime packets'] = len(sp)
    res['(a8) # nontrivial packets total'] = len(pk)
    # 'gap' style: full minus carry, etc.
    res['(a9) (N-1) - dim(carry) = single-prime+? '] = (N-1) - res['(a2) sum over CARRY conductors of phi(d)']
    # division-algebra style: 2*phi(N)? phi(N)+2?
    res['(a10) phi(N) + 2 (Cayley-Dickson +2 reading)'] = int(totient(N)) + 2
    res['(a11) 2*real_dim(M_top)=2*phi(N)'] = 2 * int(totient(N))
    return res

# ---------------------------------------------------------------------------
# (b) ORDER-2 INVARIANT OF FISHER METRIC RESTRICTED TO CARRY PACKET
# ---------------------------------------------------------------------------
# Fisher metric at centroid p_* = (1/N,...,1/N):
#   g_{ab} = delta_{ab}/p_a - 1  (on the simplex tangent, zero-sum)  [standard]
# In the CHARACTER basis e_k (k=1..N-1), restricted to zero-sum space, the Fisher
# metric at the centroid is g(e_k,e_l) = sum_a (e_k)_a conj((e_l)_a) / p_a
#   = N * sum_a omega^{(k-l)a} = N * N * 1[k==l] = N^2 delta_{kl}.
# (since p_a = 1/N).  So g is N^2 * Identity on the character basis -> the Fisher
# metric in the (orthonormal-up-to-N) character basis is a SCALAR multiple of I.
# Restricted to ANY packet it is N^2 * I_{phi(d)}.
def fisher_carry_invariants(N):
    pk = packets(N)
    res = {}
    carry = carry_conductors(N)
    # Fisher metric eigenvalue on each character = N^2 (exact); restrict to carry.
    lam = N * N
    # trace over the single conductor-N carry packet M (dim phi(N) complex):
    res['(b1) Fisher eigenvalue per character (centroid)'] = lam
    res['(b2) rank of g|_M (M=conductor-N packet)'] = int(totient(N))
    res['(b3) trace g|_M = N^2 * phi(N)'] = lam * int(totient(N))
    res['(b4) trace g|_M / N^2 = phi(N) (normalized)'] = int(totient(N))
    res['(b5) trace g|_(all carry) / N^2 = sum_carry phi(d)'] = sum(int(totient(d)) for d in carry)
    res['(b6) rank g|_(all carry)'] = sum(int(totient(d)) for d in carry)
    # log-det style / "central charge from metric": tr(g)/N^2 over carry = (b5)
    return res

# ---------------------------------------------------------------------------
# (c) SUGAWARA-LIKE CENTRAL CHARGE FROM THE CUBIC STRUCTURE CONSTANT
# ---------------------------------------------------------------------------
# WZW: c = k * dim(g) / (k + h^v).
# Build the most natural analogues from the closing-triple structure.
# Structure constant: T_klm = N^3 * 1[k+l+m == 0 mod N] on dynamical indices 1..N-1.
def closing_triples(N):
    """unordered multisets {k,l,m}, k,l,m in 1..N-1, k+l+m==0 mod N."""
    out = []
    for k in range(1, N):
        for l in range(k, N):
            for m in range(l, N):
                if (k + l + m) % N == 0:
                    out.append((k, l, m))
    return out

def ordered_closing_count(N):
    c = 0
    for k in range(1, N):
        for l in range(1, N):
            for m in range(1, N):
                if (k + l + m) % N == 0:
                    c += 1
    return c

def closing_within(indices_set, N):
    """ordered closing triples with ALL legs in indices_set."""
    s = set(indices_set)
    c = 0
    for k in s:
        for l in s:
            for m in s:
                if (k + l + m) % N == 0:
                    c += 1
    return c

def sugawara_candidates(N):
    res = {}
    pk = packets(N)
    g_dim = N - 1                      # dim of dynamical tangent (zero-sum) = "dim g"
    carry = carry_conductors(N)
    sp = single_prime_conductors(N)

    n_closing_unordered = len(closing_triples(N))
    n_closing_ordered = ordered_closing_count(N)

    # The "dual Coxeter number" analogue: for an additive (abelian) grading the
    # adjoint action's eigenvalue / the count of closing partners per index.
    # Number of ordered (l,m) with k+l+m=0 for FIXED k (l,m in 1..N-1):
    #   = #{l in 1..N-1 : -(k+l) mod N in 1..N-1} = (N-1) - (#l with l=-k) - (#l with l=0-> none)
    # exact below.
    def partners(k):
        c = 0
        for l in range(1, N):
            m = (-(k + l)) % N
            if 1 <= m <= N - 1:
                c += 1
        return c
    h_dual_like = partners(1)  # same for all k by symmetry? check:
    all_same = len({partners(k) for k in range(1, N)}) == 1

    res['(c0) #closing triples (unordered, dynamical)'] = n_closing_unordered
    res['(c0b) #closing triples (ordered, dynamical)'] = n_closing_ordered
    res['(c0c) closing partners per index (h^v-like)'] = h_dual_like
    res['(c0d) partners-per-index uniform?'] = all_same
    res['(c0e) dim g (=N-1)'] = g_dim

    # ---- Sugawara analogue 1: c = k*dim(g)/(k + h^v) with the natural integer
    #      "level" k=1 and h^v = partners-per-index.
    if (1 + h_dual_like) != 0:
        res['(c1) k=1 Sugawara: 1*dim(g)/(1+h^v)'] = Fraction(g_dim, 1 + h_dual_like)
    # large-level limit -> dim g
    res['(c2) large-k Sugawara limit = dim(g) = N-1'] = g_dim

    # ---- Sugawara analogue 2: carry sector only. "dim g" -> dim(carry),
    #      "h^v" -> closing partners WITHIN carry per carry index.
    carry_idx = [k for d in carry for k in pk[d]]
    dim_carry = len(carry_idx)
    # h^v within carry: ordered (l,m) in carry^2 with k+l+m=0, fixed carry k
    def partners_within(k, idx):
        s = set(idx); c = 0
        for l in s:
            m = (-(k + l)) % N
            if m in s:
                c += 1
        return c
    if carry_idx:
        hv_carry_list = [partners_within(k, carry_idx) for k in carry_idx]
        hv_carry = hv_carry_list[0] if len(set(hv_carry_list)) == 1 else None
        res['(c3) dim(carry sector)'] = dim_carry
        res['(c3b) h^v within carry (per index; None if nonuniform)'] = hv_carry
        res['(c3c) h^v within carry list'] = hv_carry_list
        if hv_carry is not None and (1 + hv_carry) != 0:
            res['(c3d) k=1 Sugawara on carry: dim(carry)/(1+h^v_carry)'] = Fraction(dim_carry, 1 + hv_carry)

    # ---- Sugawara analogue 3: structure-constant NORM based.
    # ||T||^2 = sum_{k,l,m} |T_klm|^2 = (N^3)^2 * #ordered_closing.
    # A dimensionless "central charge" = ||T||^2 / (N^3)^2 = #ordered_closing.
    res['(c4) ||T||^2 / (N^3)^2 = #ordered closing triples'] = n_closing_ordered

    # ---- Sugawara analogue 4: closing-triples carried THROUGH carry vs within single-prime
    # On Z/6 the corpus says: 2 triples close within A_3 (single-prime), 4 forced through M.
    n_within_sp = sum(closing_within(pk[d], N) for d in sp)  # ordered, within a single sp packet
    # ordered closing triples with at least one carry leg:
    def has_carry_leg(t):
        return any(conductor(x, N) in set(carry) for x in t)
    n_with_carry = 0
    for k in range(1, N):
        for l in range(1, N):
            for m in range(1, N):
                if (k + l + m) % N == 0 and has_carry_leg((k, l, m)):
                    n_with_carry += 1
    res['(c5) #ordered closing within a single-prime packet'] = n_within_sp
    res['(c5b) #ordered closing with >=1 carry leg'] = n_with_carry
    # unordered versions (match corpus enumeration style):
    u_within_sp = 0
    for t in closing_triples(N):
        if all(conductor(x, N) in set(sp) and conductor(t[0], N) == conductor(x, N) for x in t):
            u_within_sp += 1
    u_with_carry = sum(1 for t in closing_triples(N) if has_carry_leg(t))
    res['(c5c) #unordered closing entirely within ONE single-prime packet'] = u_within_sp
    res['(c5d) #unordered closing with >=1 carry leg'] = u_with_carry

    return res

# ---------------------------------------------------------------------------
def run(N):
    print("=" * 72)
    print(f"  R = Z/{N}Z      (factorization: {dict((int(p),int(__import__('sympy').factorint(N)[p])) for p in primefactors(N))})")
    print("=" * 72)
    pk = packets(N)
    print(" conductor packets (d : phi(d)=dim : indices):")
    for d, idx in pk.items():
        tag = "carry" if len(primefactors(d)) >= 2 else "single-prime"
        print(f"   H_{d:<3} dim={int(totient(d)):<2} {tag:<13} k={idx}")
    print(f"   single-prime conductors: {single_prime_conductors(N)}")
    print(f"   carry (cross-prime) conductors: {carry_conductors(N)}")
    print()

    allres = {}
    for name, block in (("(a) DIMENSION COUNTS", dim_candidates(N)),
                        ("(b) FISHER ORDER-2 INVARIANT ON CARRY", fisher_carry_invariants(N)),
                        ("(c) SUGAWARA-LIKE FROM CUBIC STRUCTURE CONSTANT", sugawara_candidates(N))):
        print(f"--- {name} ---")
        for kk, vv in block.items():
            hit = ""
            try:
                if vv == TARGET:
                    hit = "   <<<<< == 6 TARGET HIT"
                elif isinstance(vv, Fraction) and vv == Fraction(TARGET):
                    hit = "   <<<<< == 6 TARGET HIT"
                elif isinstance(vv, (int, Fraction)) and abs(float(vv) - TARGET) <= 1 and vv != TARGET:
                    hit = f"   (near 6: off by {float(vv)-TARGET:+g})"
            except Exception:
                pass
            print(f"   {kk:<58} = {vv}{hit}")
            allres[(N, kk)] = vv
        print()
    return allres

if __name__ == "__main__":
    r6 = run(6)
    r30 = run(30)

    # explicit hit report
    print("=" * 72)
    print("  HITS == 6 (exact), across both rings:")
    print("=" * 72)
    any_hit = False
    for (N, name), v in {**r6, **r30}.items():
        is6 = (v == 6) or (isinstance(v, Fraction) and v == Fraction(6))
        if is6:
            any_hit = True
            print(f"   Z/{N}: {name} = {v}")
    if not any_hit:
        print("   (none)")

    # also report which definitions give the CONSISTENT division-algebra gap idea:
    # spacetime c-hat=4 (=phi? ) check; gap dim O - dim C = 6.
    print()
    print("  cross-check: phi(N) on the two rings (the 'top carry packet dim'):")
    print(f"     phi(6)={int(totient(6))}, phi(30)={int(totient(30))}")
    print("  cross-check: sum_carry phi(d):")
    cs6 = sum(int(totient(d)) for d in carry_conductors(6))
    cs30 = sum(int(totient(d)) for d in carry_conductors(30))
    print(f"     Z/6 = {cs6}   Z/30 = {cs30}")
    print("  cross-check: dim g = N-1:  Z/6=5, Z/30=29")
