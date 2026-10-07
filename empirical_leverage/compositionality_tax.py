"""
THE COMPOSITIONALITY TAX -- synthetic core of the faithfulness phase-boundary prediction.

Tier-A falsifiable prediction (firewall-irrelevant; pure ML/representation claim):
  The minimum probe ORDER needed to faithfully read a behavior = the cumulant ORDER of its
  interactions = its compositional depth. Faithfulness is a PHASE BOUNDARY, not a gradient:
  an order-m probe is faithful iff m >= k (the true interaction order); it is EXACTLY blind below.

  => "How compositional is this behavior?" becomes a MEASURED number tau = the order at which a
     readout saturates. tau is the compositionality tax.

This file is the EXACT synthetic gate (numpy, deterministic). The full LLM version -- probe a
trained transformer at varying readout order vs its measured interaction order -- is GCP/torch,
specified in `compositionality_tax_protocol.md`, NOT run here (local-torch hardware constraint).

Construction (generalizes the D-IV faithfulness obstruction to all orders): for true order k, the
k-th finite difference is the null vector of the order-(k-1) moment map, so two distributions
p = base + eps*Delta^k, q = base - eps*Delta^k are matched through order k-1 and differ at order k.
An order-m probe (moments up to m) distinguishes them IFF m >= k. The faithfulness matrix is then
lower-triangular with a SHARP step at m=k -- the phase boundary; tau(k) = k.
"""
import sys
import numpy as np
from math import comb
try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

PASS = []
def chk(name, ok):
    PASS.append(bool(ok)); print(f"  [{'OK ' if ok else 'FAIL'}] {name}")

def kth_finite_difference(k):
    """Delta^k = [(-1)^(k-j) C(k,j)] -- null vector of [v^0,...,v^(k-1)], nonzero on v^k."""
    return np.array([(-1)**(k - j) * comb(k, j) for j in range(k + 1)], dtype=float)

def matched_pair(k, eps=0.02):
    """Two distributions on {0..k}: identical moments through order k-1, different at order k."""
    vals = np.arange(k + 1, dtype=float)
    base = np.full(k + 1, 1.0 / (k + 1))
    d = kth_finite_difference(k)
    pert = eps * d / np.abs(d).sum()
    return vals, base + pert, base - pert

def moment_discrepancy(vals, p, q, m):
    """max |E_p[v^r] - E_q[v^r]| over r = 0..m  (what an order-m probe can see)."""
    return max(abs(p @ vals**r - q @ vals**r) for r in range(m + 1))

Ks = [2, 3, 4, 5]
Ms = [0, 1, 2, 3, 4, 5]
TOL = 1e-12

# --- (1) the matched pairs are valid distributions, matched below k, differ at k ---
print("(1) order-k matched pairs: valid, identical moments < k, different moment k")
for k in Ks:
    vals, p, q = matched_pair(k)
    valid = np.all(p > 0) and np.all(q > 0) and abs(p.sum() - 1) < TOL and abs(q.sum() - 1) < TOL
    below = moment_discrepancy(vals, p, q, k - 1) < TOL              # matched through k-1
    at = abs(p @ vals**k - q @ vals**k) > 1e-6                        # differ at order k
    chk(f"k={k}: valid distributions; moments 0..{k-1} identical; moment {k} differs", valid and below and at)

# --- (2) the faithfulness PHASE BOUNDARY: order-m probe faithful iff m >= k ---
print("(2) faithfulness is a SHARP phase boundary: order-m probe distinguishes iff m >= k")
F = np.zeros((len(Ks), len(Ms)), dtype=int)
disc = np.zeros((len(Ks), len(Ms)))
for i, k in enumerate(Ks):
    vals, p, q = matched_pair(k)
    for j, m in enumerate(Ms):
        d = moment_discrepancy(vals, p, q, m)
        disc[i, j] = d
        F[i, j] = int(d > TOL)
print("    F[k][m] (1 = order-m probe is faithful to order-k behavior):")
print("           m=" + "  ".join(f"{m}" for m in Ms))
for i, k in enumerate(Ks):
    print(f"      k={k}:   " + "  ".join(f"{F[i,j]}" for j in range(len(Ms))))
boundary_ok = all(F[i, j] == int(Ms[j] >= Ks[i]) for i in range(len(Ks)) for j in range(len(Ms)))
chk("F[k][m] == 1 iff m >= k exactly (lower-triangular phase boundary, no gradient)", boundary_ok)

# --- (3) the boundary is a STEP, not a ramp: discrepancy is exactly 0 below k, jumps at k ---
print("(3) the transition is a discontinuous STEP (exact zero below, jump at k)")
step_ok = True
for i, k in enumerate(Ks):
    for j, m in enumerate(Ms):
        if m < k and disc[i, j] > TOL: step_ok = False           # must be exactly 0 below
        if m == k and disc[i, j] < 1e-6: step_ok = False         # must jump at k
chk("discrepancy exactly 0 for m < k and strictly positive at m = k (phase transition, not gradient)",
    step_ok)

# --- (4) the compositionality tax: tau(k) = min faithful order = k ---
print("(4) compositionality tax tau(k) = min{m : order-m probe faithful} = k (the measuring stick)")
def tau(k):
    vals, p, q = matched_pair(k)
    for m in range(0, 2*k + 1):
        if moment_discrepancy(vals, p, q, m) > TOL:
            return m
    return None
taus = {k: tau(k) for k in Ks}
print(f"    tau = {taus}")
chk("tau(k) = k for all tested k (cumulant order = compositional depth = required probe order)",
    all(taus[k] == k for k in Ks))

# --- (5) the falsifier, encoded: a gradient (faithfulness rising smoothly with m) would kill it ---
print("(5) pre-registered falsifier: smooth degradation (a gradient) instead of a step")
# our prediction => for fixed k, F jumps 0->1 once. A gradient world would show intermediate
# partial-faithfulness at m=k-1. We verify the prediction's signature (single sharp jump) holds.
single_jump = all(sum(abs(np.diff(F[i]))) == 1 for i in range(len(Ks)))
chk("each row has exactly ONE 0->1 transition (a step) -- gradient/multi-step would falsify",
    single_jump)

print("=" * 80)
print(f"SUMMARY: {sum(PASS)}/{len(PASS)} OK ->", "GREEN" if all(PASS) else "RED")
print("COMPOSITIONALITY TAX: an order-m probe is faithful to an order-k behavior IFF m >= k -- a")
print("sharp PHASE BOUNDARY (exact-zero discrepancy below k, jump at k), not a gradient. The tax")
print("tau(k) = k turns 'how compositional is this behavior?' into a measured number: the order at")
print("which a readout saturates. Synthetic gate exact; LLM protocol (GCP) in the companion .md.")
print("=" * 80)
