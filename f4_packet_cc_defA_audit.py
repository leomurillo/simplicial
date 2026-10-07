"""
F4 audit / paranoia pass:
 1. enumerate explicitly the unordered closing triples within ONE single-prime
    packet on Z/30 (to confirm the (c5c)=6 is real, not a bug), and on Z/6.
 2. Test STABILITY: does ANY candidate give the SAME value on Z/6 and Z/30?
    A genuine 'central charge analogue' must be ring-stable (c-hat_internal=6 is
    supposed to be intrinsic to the division-algebra rung, not to the modulus).
 3. Honest near-miss catalogue with the division-algebra ladder.
"""
from math import gcd
from sympy import totient, divisors, primefactors

def conductor(k, N): return N // gcd(k, N)
def sp_conductors(N): return [int(d) for d in divisors(N) if d>1 and len(primefactors(d))==1]
def carry_conductors(N): return [int(d) for d in divisors(N) if d>1 and len(primefactors(d))>=2]
def packets(N):
    pk={}
    for k in range(1,N): pk.setdefault(conductor(k,N),[]).append(k)
    return {d:pk[d] for d in sorted(pk)}

def closing_unordered(N):
    out=[]
    for k in range(1,N):
        for l in range(k,N):
            for m in range(l,N):
                if (k+l+m)%N==0: out.append((k,l,m))
    return out

print("=== explicit: unordered closing triples WITHIN one single-prime packet ===")
for N in (6,30):
    pk=packets(N); sp=sp_conductors(N)
    print(f"\nZ/{N}: single-prime packets {[(d,pk[d]) for d in sp]}")
    found=[]
    for t in closing_unordered(N):
        conds={conductor(x,N) for x in t}
        if len(conds)==1 and list(conds)[0] in sp:
            found.append((t, list(conds)[0]))
    for t,d in found:
        print(f"   {t}  all in H_{d}")
    print(f"   COUNT = {len(found)}")

print("\n=== STABILITY: which candidate (if any) is equal on Z/6 AND Z/30? ===")
def candidates(N):
    pk=packets(N); sp=sp_conductors(N); carry=carry_conductors(N)
    c_un=closing_unordered(N)
    def has_carry(t): return any(conductor(x,N) in set(carry) for x in t)
    return {
      "phi(N) (top carry dim)": int(totient(N)),
      "sum_carry phi(d)": sum(int(totient(d)) for d in carry),
      "sum_sp phi(d)": sum(int(totient(d)) for d in sp),
      "N-1 (dim g)": N-1,
      "#carry packets": len(carry),
      "#sp packets": len(sp),
      "#nontrivial packets": len(pk),
      "#closing unordered": len(c_un),
      "#closing within one sp packet": sum(1 for t in c_un if len({conductor(x,N) for x in t})==1 and {conductor(x,N) for x in t}.pop() in sp),
      "#closing with carry leg (unord)": sum(1 for t in c_un if has_carry(t)),
      "phi(N)+2": int(totient(N))+2,
      "2*phi(N)": 2*int(totient(N)),
      "#closing - #carry (unord)": len(c_un)-len([t for t in c_un if has_carry(t)]),
    }
c6=candidates(6); c30=candidates(30)
print(f"{'candidate':<40}{'Z/6':>8}{'Z/30':>8}  stable?")
for k in c6:
    s = "  STABLE" if c6[k]==c30[k] else ""
    six = "  ->6 on Z/6" if c6[k]==6 else ""
    six30 = "  ->6 on Z/30" if c30[k]==6 else ""
    print(f"{k:<40}{c6[k]:>8}{c30[k]:>8}{s}{six}{six30}")

print("\n=== division-algebra ladder cross-check ===")
print(" magic dims D = dim_R K + 2: K=R,C,H,O -> 3,4,6,10")
print(" 4D-superstring: c-hat_total=10 = c-hat_spacetime(4)+c-hat_internal(6)")
print(" gap = dim O - dim C = 8-2 = 6")
print(" program top carry dims phi(N): Z/6 -> 2 ; Z/30 -> 8")
print("   2 = dim_R(C); 8 = dim_R(O)  <-- note: these are division-algebra DIMS, not the +2 magic dims")
print(" phi(N)+2: Z/6 -> 4 (=D for C, the 3+1 rung!); Z/30 -> 10 (=D for O, the superstring rung!)")
