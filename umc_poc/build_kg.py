"""
build_kg.py — (a) unified KG export. Runs improvements #1 (Fisher-Rao placement) and
#3 (conductor addressing) together and emits ONE drop-in artifact, kg.csv, with the
continuous little-sphere coordinates, the ABCD/IVM lattice point, the conductor address,
the Boolean-Janus complement, and the top-3 Fisher-Rao neighbours per node.

Run:  py build_kg.py   (or python build_kg.py)
"""
import sys, csv
from pathlib import Path
import numpy as np
import fisher_kg as fk
import conductor_kg as ck
from poc import load_corpus, build_distributions, TOKEN, STOP

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

OUT = Path(__file__).resolve().parent / "kg.csv"

def main():
    ids, stems, fams, texts = load_corpus()
    n = len(ids)
    P, vocab = build_distributions(texts)

    # #1: Fisher-Rao metric -> MDS -> ABCD/IVM lattice (zero-sum)
    Dfr = fk.fisher_rao_matrix(P)
    coords, _ = fk.classical_mds(Dfr, dim=3)
    freq = 10.0 / max(np.abs(coords).max(), 1e-9)
    L = fk.snap_to_lattice(fk.xyz_to_quadray(coords), freq)
    L[:, 3] = -(L[:, :3].sum(axis=1))               # zero-sum erasure decode
    nn = fk.knn(Dfr, 3)

    # #3: conductor address + Boolean-Janus complement
    toks = [[w for w in TOKEN.findall(t) if w not in STOP] for t in texts]
    cond, _ = ck.conductors(ck.topic_masses(toks))

    with open(OUT, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["node", "family",
                    "x", "y", "z",                      # little-sphere (MDS) coords  [#1]
                    "A", "B", "C", "D",                 # ABCD/IVM lattice point on H  [#1]
                    "conductor", "factorization", "rank_omega",  # conductor address  [#3]
                    "complement", "complement_factorization",    # exact Boolean Janus [#3]
                    "fr_nn1", "fr_nn2", "fr_nn3"])      # nearest neighbours          [#1]
        for i in range(n):
            c = int(cond[i]); comp = ck.complement(c)
            w.writerow([stems[i], fams[i],
                        *np.round(coords[i], 4).tolist(),
                        *L[i].tolist(),
                        c, ck.factor_str(c), ck.omega(c),
                        comp, ck.factor_str(comp),
                        *[ids[j] for j in nn[i]]])

    # tiny console digest
    print(f"unified KG written -> {OUT.name}  ({n} nodes)")
    print(f"  columns: little-sphere xyz [#1] + ABCD lattice ABCD [#1] + conductor address [#3]"
          f" + Boolean-Janus complement [#3] + Fisher-Rao neighbours [#1]")
    print(f"  zero-sum check (all ABCD on H): {bool((L.sum(axis=1) == 0).all())}")
    print(f"  distinct conductors: {len(set(int(c) for c in cond))}/{2**len(ck.PRIMES)}")
    print("\n  sample rows:")
    for probe in ["01", "01b", "32.1", "T33", "22", "12"]:
        if probe in ids:
            i = ids.index(probe); c = int(cond[i])
            print(f"    {probe:>5} [{fams[i]:>8}]  ABCD={tuple(L[i].tolist())}  "
                  f"cond={ck.factor_str(c)}  nn={[ids[j] for j in nn[i]]}")

if __name__ == "__main__":
    main()
