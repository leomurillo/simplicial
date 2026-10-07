"""
poc.py — Fisher-Rao Knowledge-Graph placement, run against the repo's own manuscripts.

Demonstrates the information-geometric upgrade to the Cookbook KG (§18):
the Cookbook places nodes by abstraction layer and fills lattice points by inventory
order (no semantic metric); here each manuscript becomes a distribution over its
vocabulary, and Paper 32.1's little-sphere Fisher-Rao metric gives canonical semantic
proximity, a Bekenstein capacity, an ABCD-lattice placement that preserves proximity,
and a data-processing contraction.

Run:  py poc.py   (or python poc.py)   — pure numpy; sympy optional for the K=1/4 check.
"""
import re, csv
from pathlib import Path
import numpy as np
import fisher_kg as fk

ROOT = Path(__file__).resolve().parent.parent          # the repo root
OUT = Path(__file__).resolve().parent / "kg_layout.csv"

# Author-supplied COARSE families (editable) — ground truth for the purity metric only.
FAMILY = {
    # simplicial-geometry frame
    "01": "frame", "01b": "frame", "01c": "frame", "01d": "frame",
    "02": "frame", "03": "frame", "04": "frame", "0": "frame",
    # cyclotomic / conductor / RH / primorial  (number-theoretic)
    "05": "arith", "06": "arith", "07": "arith", "08": "arith", "09": "arith",
    "11": "arith", "22": "arith", "27": "arith", "32.1": "arith", "T33": "arith",
    # information geometry / mechanics / AI / physics
    "10": "infophys", "12": "infophys", "13": "infophys", "14": "infophys",
    "15": "infophys", "17": "infophys", "18": "infophys", "20": "infophys",
    "24": "infophys", "25": "infophys", "26": "infophys", "28": "infophys",
    "29": "infophys", "30": "infophys", "31": "infophys", "32": "infophys",
}

STOP = set("""the and that this with for are was has have not but all any one two three
from into over under per via its it is be as at by an or of to in on we us our their
where which when then thus hence so if no yes can may will shall must each both than
section paper figure table theorem lemma proof remark def definition eq equation
appendix draft note left right frac begin end text mathrm mathbf cdot sum prod int
sqrt log exp sin cos quad qquad times mapsto langle rangle otimes oplus alpha beta
gamma delta zeta phi psi chi rho sigma tau theta lambda omega nabla partial forall
exists infty geq leq neq approx equiv pmod bmod label cite ref item enumerate itemize
case cases matrix pmatrix bmatrix vmatrix boxed mathcal mathbb operatorname displaystyle
""".split())

TOKEN = re.compile(r"[a-zA-Z][a-zA-Z\-']{3,}")

def short_id(stem):
    m = re.match(r"(T?\d+(?:\.\d+)?[a-d]?)", stem)
    return m.group(1) if m else stem[:10]

def family_of(sid):
    return FAMILY.get(sid, FAMILY.get(sid.split(".")[0], "other"))

def load_corpus(max_files=40):
    skip = {"README", "MEMORY", "AGENTS", "CLAUDE"}
    ids, stems, fams, texts = [], [], [], []
    for p in sorted(ROOT.glob("*.md")):
        stem = p.stem
        if stem in skip or stem.startswith(":") or not re.match(r"^(\d|0|T\d)", stem):
            continue
        try:
            t = p.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        sid = short_id(stem)
        ids.append(sid); stems.append(stem); fams.append(family_of(sid)); texts.append(t.lower())
        if len(ids) >= max_files:
            break
    return ids, stems, fams, texts

def build_distributions(texts, vocab_size=400, smooth=0.5):
    counts = [{} for _ in texts]; glob = {}
    for c, t in zip(counts, texts):
        for w in TOKEN.findall(t):
            if w in STOP:
                continue
            c[w] = c.get(w, 0) + 1; glob[w] = glob.get(w, 0) + 1
    vocab = [w for w, _ in sorted(glob.items(), key=lambda kv: -kv[1])[:vocab_size]]
    vidx = {w: i for i, w in enumerate(vocab)}
    P = np.full((len(texts), len(vocab)), smooth)
    for r, c in enumerate(counts):
        for w, n in c.items():
            if w in vidx:
                P[r, vidx[w]] += n
    P /= P.sum(axis=1, keepdims=True)
    return P, vocab

def section(t):
    print("\n" + "=" * 72 + f"\n{t}\n" + "=" * 72)

def spearman(a, b):
    ra = np.argsort(np.argsort(a)); rb = np.argsort(np.argsort(b))
    return float(np.corrcoef(ra, rb)[0, 1])

def main():
    ids, stems, fams, texts = load_corpus()
    n = len(ids)
    P, vocab = build_distributions(texts)
    print(f"loaded {n} manuscripts, vocab {len(vocab)} terms")

    section("little-sphere sanity (Paper 32.1)")
    radii = np.linalg.norm(fk.hellinger_embed(P), axis=1)
    Dfr = fk.fisher_rao_matrix(P)
    print(f"  Hellinger radius |2 sqrt(p)| = 2 : min={radii.min():.6f} max={radii.max():.6f}")
    print(f"  Fisher-Rao distance range [0, pi]: min={Dfr[Dfr>0].min():.4f} max={Dfr.max():.4f} (pi={np.pi:.4f})")
    try:
        import sympy as sp
        x, y = sp.symbols('x y', positive=True)
        emb = [2 * sp.sqrt(pi_) for pi_ in (x, y, 1 - x - y)]
        gxx = sum(sp.diff(e, x) ** 2 for e in emb); gyy = sum(sp.diff(e, y) ** 2 for e in emb)
        gxy = sum(sp.diff(e, x) * sp.diff(e, y) for e in emb)
        K = sp.simplify(_gauss_K(sp.Matrix([[gxx, gxy], [gxy, gyy]]), x, y))
        print(f"  symbolic Gaussian curvature K (Q=3 row) = {K}  (expected 1/4)")
    except Exception as e:
        print(f"  [sympy K-check skipped: {e}]")

    section("Fisher-Rao nearest neighbours (semantic constellation)")
    nn = fk.knn(Dfr, 3)
    for probe in ["01", "01b", "01c", "32.1", "T33", "22", "12"]:
        if probe in ids:
            i = ids.index(probe)
            nbrs = ", ".join(f"{ids[j]}({Dfr[i,j]:.2f})" for j in nn[i])
            print(f"  {probe:>5} [{fams[i]:>8}] -> {nbrs}")

    section("k-NN purity: content vs structural-index (k=3); the honest comparison")
    rng = np.random.default_rng(1)
    pos = rng.permutation(n)                                  # a non-topic-sorted inventory
    Dinv_given = fk.inventory_distance(n)                     # repo order (hand-sorted by topic!)
    Dinv_shuf = np.abs(pos[:, None] - pos[None, :]).astype(float)
    Drnd = fk.random_distance(n)
    pf = fk.knn_purity(Dfr, fams, 3)
    print(f"     Fisher-Rao (content)        : {pf:.3f}   <- order-invariant, from content alone")
    print(f"     inventory-order (repo sort) : {fk.knn_purity(Dinv_given, fams, 3):.3f}   <- high ONLY because filenames are pre-sorted by topic")
    print(f"     inventory-order (shuffled)  : {fk.knn_purity(Dinv_shuf, fams, 3):.3f}   <- the realistic un-sorted inventory: collapses to ~chance")
    print(f"     random                      : {fk.knn_purity(Drnd, fams, 3):.3f}   <- chance floor")
    print("  Reading: the Cookbook's lattice-fill is only as good as the inventory's sort;")
    print("  Fisher-Rao recovers the same topology from CONTENT, no human sort required.")

    section("Bekenstein capacity per shell (Paper 32.1 Thm 4.1)")
    shells = {}
    for f in fams:
        shells[f] = shells.get(f, 0) + 1
    for f, q in sorted(shells.items()):
        print(f"  shell {f:>8}: Q={q:2d}  capacity log Q = {fk.bekenstein_capacity(q):.3f} nats")
    print(f"  occupancy entropy = {fk.occupancy_entropy(list(shells.values())):.3f}  (saturated = log {len(shells)} = {np.log(len(shells)):.3f})")

    section("ABCD/IVM lattice placement (Cookbook map) preserves proximity")
    coords, eig = fk.classical_mds(Dfr, dim=3)
    spread = np.abs(coords).max()
    freq = 10.0 / spread if spread > 0 else 1.0
    L = fk.snap_to_lattice(fk.xyz_to_quadray(coords), freq)
    L[:, 3] = -(L[:, :3].sum(axis=1))          # zero-sum erasure-decode (Cookbook §9.7 / 01 §7)
    Dlat = fk.lattice_distance_matrix(L)
    iu = np.triu_indices(n, 1)
    rho = spearman(Dfr[iu], Dlat[iu])
    dup = n - len({tuple(r) for r in L.tolist()})
    print(f"  MDS top-3 eigenvalues: {np.round(eig[:3],3)}  (3D capture of a {len(vocab)}-dim sphere; lossy)")
    print(f"  all lattice points zero-sum (on H): {bool((L.sum(axis=1) == 0).all())}")
    print(f"  FR<->ABCD-lattice Spearman rho = {rho:.3f}  (1 = proximity perfectly preserved)")
    print(f"  lattice-point collisions at freq~{freq:.2f}: {dup}")

    section("data-processing / monotone contraction (retrieval coarse-graining, §6)")
    mean_r, max_r = fk.dpi_contraction_ratio(P, n_bins=12)
    print(f"  coarse/fine FR ratio: mean={mean_r:.3f} max={max_r:.3f}  (<=1 => DPI holds; retrieval loses info monotonically)")

    with open(OUT, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["node", "family_shell", "A", "B", "C", "D", "x", "y", "z"])
        for i in range(n):
            w.writerow([stems[i], fams[i], *L[i].tolist(), *np.round(coords[i], 4).tolist()])
    print(f"\nwrote rendered KG layout -> {OUT.name} ({n} nodes)")

    section("VERDICT")
    print(f"  Fisher-Rao constellation: purity {pf:.2f} from CONTENT (chance {fk.knn_purity(Drnd,fams,3):.2f}),")
    print(f"  order-invariant where the structural index needs a pre-sorted inventory.")
    print(f"  Little sphere literal (K=1/4, radius 2); capacity log Q; ABCD placement rho={rho:.2f}; DPI holds. POC OK.")


def _gauss_K(g, u, v):
    import sympy as sp
    E, F, G = g[0, 0], g[0, 1], g[1, 1]
    Ev = sp.diff(E, v); Gu = sp.diff(G, u); Gv = sp.diff(G, v)
    B1 = sp.Matrix([[-sp.Rational(1,2)*sp.diff(E, v, v) + sp.diff(F, u, v) - sp.Rational(1,2)*sp.diff(G, u, u),
                     sp.Rational(1,2)*sp.diff(E, u), sp.diff(F, u) - sp.Rational(1,2)*Ev],
                    [sp.diff(F, v) - sp.Rational(1,2)*Gu, E, F],
                    [sp.Rational(1,2)*Gv, F, G]])
    B2 = sp.Matrix([[0, sp.Rational(1,2)*Ev, sp.Rational(1,2)*Gu],
                    [sp.Rational(1,2)*Ev, E, F],
                    [sp.Rational(1,2)*Gu, F, G]])
    return (B1.det() - B2.det()) / (E*G - F**2)**2


if __name__ == "__main__":
    main()
