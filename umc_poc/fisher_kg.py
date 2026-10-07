"""
fisher_kg.py — core information-geometry for a UMC/Knowledge-Graph placement engine.

The Cookbook (§18) places nodes on FCC/RD shells by abstraction layer and fills
lattice points by inventory order (no semantic metric). This module supplies the
missing metric layer from Paper 32.1 + 01c:

  - each node is a categorical distribution p over a feature alphabet;
  - Hellinger embed  p |-> 2*sqrt(p)  onto the round sphere of curvature K = 1/4,
    radius 2  (Paper 32.1, Thm 3.1: the "little sphere", made literal);
  - node distance = Fisher-Rao geodesic = 2*arccos(BC), BC = Bhattacharyya
    coefficient sum_i sqrt(p_i q_i)  (the UNIQUE monotone metric, Chentsov);
  - placement: classical MDS on the FR distance matrix -> R^3 -> nearest ABCD
    (Quadray) integer lattice point (Cookbook §6 map  q = (1/4) B xyz, zero-sum);
  - capacity per shell = log Q (Paper 32.1 Thm 4.1, the finite Bekenstein bound);
  - coarse-graining is a monotone contraction (Paper 32.1 §6, data-processing).

Pure numpy. Deterministic. No torch.
"""
import numpy as np

# ---------- the little sphere (Paper 32.1) ----------

def hellinger_embed(P, radius=2.0):
    """p |-> radius*sqrt(p). Rows of P are distributions; image lies on |x|=radius."""
    return radius * np.sqrt(P)

def bhattacharyya_matrix(P):
    """BC_ij = sum_k sqrt(P_ik P_jk) = <sqrt p_i, sqrt p_j>."""
    S = np.sqrt(P)
    return np.clip(S @ S.T, 0.0, 1.0)

def fisher_rao_matrix(P, radius=2.0):
    """Geodesic distance on the radius-2 sphere: d = 2*arccos(BC). Range [0, pi]."""
    return radius * np.arccos(bhattacharyya_matrix(P))

def bekenstein_capacity(n):
    """Finite Bekenstein bound: a shell of Q distinguishable nodes holds <= log Q nats."""
    return float(np.log(n)) if n > 0 else 0.0

def occupancy_entropy(sizes):
    """Entropy of the shell-occupancy distribution; = log(#shells) at the centroid."""
    s = np.asarray(sizes, float); s = s[s > 0]; p = s / s.sum()
    return float(-(p * np.log(p)).sum())

# ---------- placement: MDS -> ABCD/IVM lattice ----------

def classical_mds(D, dim=3):
    """Classical multidimensional scaling of a distance matrix D -> R^dim coords."""
    n = D.shape[0]
    J = np.eye(n) - np.ones((n, n)) / n
    B = -0.5 * J @ (D ** 2) @ J
    w, V = np.linalg.eigh(B)
    order = np.argsort(w)[::-1]
    w, V = w[order], V[:, order]
    Xpos = V[:, :dim] * np.sqrt(np.clip(w[:dim], 0, None))
    return Xpos, w

# Tom Ace basis B (rows A,B,C,D in Cartesian); B^T B = 4 I_3  (Cookbook §2.4, §6).
TOM_ACE = np.array([[-1, -1, 1],
                    [ 1,  1, 1],
                    [-1,  1, -1],
                    [ 1, -1, -1]], float)

def xyz_to_quadray(xyz):
    """Zero-sum Quadray of Cartesian points: q = (1/4) B xyz  (sum q_i = 0 automatically)."""
    return 0.25 * (TOM_ACE @ xyz.T).T

def snap_to_lattice(q, freq):
    """ABCD-native grid snap (Cookbook §12.3): round each component at frequency `freq`."""
    return np.rint(q * freq).astype(int)

def abcd_quadrance(delta):
    """Metric tensor M = 4I - J quadrance of an ABCD displacement (Cookbook §5)."""
    s1 = delta.sum(axis=-1)
    return 4.0 * (delta ** 2).sum(axis=-1) - s1 ** 2

def lattice_distance_matrix(L):
    """Pairwise ABCD (M-metric) distance between integer lattice points L (n,4)."""
    n = L.shape[0]
    D = np.zeros((n, n))
    for i in range(n):
        delta = L[i] - L
        D[i] = np.sqrt(np.clip(abcd_quadrance(delta.astype(float)), 0, None))
    return D

# ---------- neighborhoods + quality metrics ----------

def knn(D, k):
    """Indices of the k nearest neighbours of each row (excluding self)."""
    idx = np.argsort(D, axis=1)
    return idx[:, 1:k + 1]

def knn_purity(D, labels, k):
    """Mean fraction of each node's k-NN sharing its label (only labelled nodes)."""
    labels = np.asarray(labels, object)
    nn = knn(D, k)
    mask = labels != "other"
    if mask.sum() == 0:
        return float("nan")
    hits = [(labels[nbrs] == labels[i]).mean() for i, nbrs in enumerate(nn) if mask[i]]
    return float(np.mean(hits))

def inventory_distance(n):
    """Baseline 'structural index': distance = |inventory index difference|."""
    i = np.arange(n)
    return np.abs(i[:, None] - i[None, :]).astype(float)

def random_distance(n, seed=0):
    """Baseline: random symmetric distances (no information)."""
    rng = np.random.default_rng(seed)
    A = rng.random((n, n)); A = (A + A.T) / 2; np.fill_diagonal(A, 0)
    return A

# ---------- data-processing / monotone contraction (Paper 32.1 §6) ----------

def coarse_grain(P, n_bins, seed=0):
    """Merge the V feature bins into n_bins via a random partition (a coarse-graining)."""
    rng = np.random.default_rng(seed)
    V = P.shape[1]
    assign = rng.integers(0, n_bins, size=V)
    Q = np.zeros((P.shape[0], n_bins))
    for b in range(n_bins):
        Q[:, b] = P[:, assign == b].sum(axis=1)
    return Q

def dpi_contraction_ratio(P, n_bins=12, seed=0):
    """Mean (coarse FR distance)/(fine FR distance); <1 confirms monotone contraction."""
    Dfine = fisher_rao_matrix(P)
    Dcoarse = fisher_rao_matrix(coarse_grain(P, n_bins, seed))
    iu = np.triu_indices(P.shape[0], 1)
    f, c = Dfine[iu], Dcoarse[iu]
    nz = f > 1e-9
    return float(np.mean(c[nz] / f[nz])), float(np.max(c[nz] / f[nz]))
