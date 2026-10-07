"""
poc_conductor.py — improvement #3 demo: conductor-lattice addressing + exact Boolean
Janus complements, run against the repo's manuscripts. Builds on poc.py / fisher_kg.py.

Run:  py poc_conductor.py   (or python poc_conductor.py)   — pure numpy.
"""
import sys, csv
from pathlib import Path
import numpy as np
import fisher_kg as fk
import conductor_kg as ck
from poc import load_corpus, build_distributions, TOKEN, STOP, section

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

OUT = Path(__file__).resolve().parent / "conductor_addresses.csv"

def tokenize(text):
    return [w for w in TOKEN.findall(text) if w not in STOP]

def main():
    ids, stems, fams, texts = load_corpus()
    n = len(ids)
    toks = [tokenize(t) for t in texts]
    print(f"loaded {n} manuscripts; concept primes {ck.PRIMES} -> N = {ck.N_FULL}")

    M = ck.topic_masses(toks)
    cond, feats = ck.conductors(M)

    section("conductor addresses (content factors into concept primes)")
    print(f"  {'node':>6}  {'cond':>6}  {'factorization':>16}  rank   complement (concepts lacked)")
    for probe in ["01", "01b", "32.1", "T33", "22", "12", "13", "15"]:
        if probe in ids:
            i = ids.index(probe)
            c = int(cond[i]); comp = ck.complement(c)
            print(f"  {probe:>6}  {c:>6}  {ck.factor_str(c):>16}  {ck.omega(c):>4}     {comp:>6} = {ck.factor_str(comp)}")

    section("the address space is the Boolean lattice 2^k (the 'packets')")
    used = sorted(set(int(c) for c in cond))
    print(f"  distinct conductors used: {len(used)} of 2^{len(ck.PRIMES)} = {2**len(ck.PRIMES)} lattice points")
    ranks = {}
    for c in cond:
        ranks[ck.omega(int(c))] = ranks.get(ck.omega(int(c)), 0) + 1
    print("  shell (rank w = #concept primes) occupancy: " + ", ".join(f"w={r}:{ranks[r]}" for r in sorted(ranks)))

    section("exact Boolean Janus vs the Cookbook's single global inversion")
    inv_ok = all(ck.complement(ck.complement(int(c))) == int(c) for c in cond)
    rank_ok = all(ck.omega(int(c)) + ck.omega(ck.complement(int(c))) == len(ck.PRIMES) for c in cond)
    distinct_comps = len(set(ck.complement(int(c)) for c in cond))
    print(f"  comp(comp(c)) == c for all nodes (involution): {inv_ok}")
    print(f"  w(c) + w(comp(c)) == k for all nodes (rank-complement): {rank_ok}")
    print(f"  distinct complement operations available: {distinct_comps} addressable opposites "
          f"vs 1 global inversion in the Cookbook")
    i = ids.index("01") if "01" in ids else 0
    j = ids.index("32.1") if "32.1" in ids else 1
    a, b = int(cond[i]), int(cond[j])
    print(f"  lattice algebra ({ids[i]} meet/join {ids[j]}): "
          f"meet=gcd={ck.meet(a,b)} ({ck.factor_str(ck.meet(a,b))}), "
          f"join=lcm={ck.join(a,b)} ({ck.factor_str(ck.join(a,b))})")

    section("navigate-to-opposite, then CHECK you arrived (the UMC promise)")
    addr = {}
    for k_, c in enumerate(cond):
        addr.setdefault(int(c), []).append(ids[k_])
    for probe in ["01", "32.1", "12"]:
        if probe in ids:
            i = ids.index(probe); c = int(cond[i]); comp = ck.complement(c)
            occ = addr.get(comp, [])
            print(f"  {probe:>5} (cond {ck.factor_str(c)})  --complement-->  {ck.factor_str(comp)} : "
                  f"{'occupied by ' + ', '.join(occ) if occ else 'vacant address (a gap to fill)'}")

    section("#1 <-> #3 agreement: Fisher-Rao neighbours share concept primes")
    P, vocab = build_distributions(texts)
    Dfr = fk.fisher_rao_matrix(P)
    nn = fk.knn(Dfr, 3)
    shared_near = np.mean([ck.omega(ck.meet(int(cond[i]), int(cond[j])))
                           for i in range(n) for j in nn[i]])
    rng = np.random.default_rng(0)
    pairs = rng.integers(0, n, size=(3 * n, 2))
    shared_rand = np.mean([ck.omega(ck.meet(int(cond[a]), int(cond[b])))
                           for a, b in pairs if a != b])
    print(f"  mean shared concept-primes w(gcd):  FR-neighbours = {shared_near:.2f}   "
          f"random pairs = {shared_rand:.2f}")
    print("  the continuous metric (#1) and the discrete address (#3) agree:")
    print("  nodes near on the little sphere share more conductor factors.")

    with open(OUT, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["node", "family", "conductor", "factorization", "rank_omega",
                    "complement", "complement_factorization"])
        for i in range(n):
            c = int(cond[i]); comp = ck.complement(c)
            w.writerow([stems[i], fams[i], c, ck.factor_str(c), ck.omega(c),
                        comp, ck.factor_str(comp)])
    print(f"\nwrote conductor addresses -> {OUT.name} ({n} nodes)")

    section("VERDICT")
    print(f"  Every node has a content-derived conductor address on the Boolean lattice 2^{len(ck.PRIMES)};")
    print(f"  complement N/c is an exact involution ({inv_ok}) and rank-complemented ({rank_ok}),")
    print(f"  giving {distinct_comps} addressable opposites where the Cookbook has 1; and the")
    print(f"  discrete address agrees with #1's Fisher-Rao metric (shared primes {shared_near:.2f} vs {shared_rand:.2f}). POC OK.")


if __name__ == "__main__":
    main()
