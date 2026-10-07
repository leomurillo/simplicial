"""
conductor_kg.py — improvement #3: conductor-lattice addressing + exact Boolean Janus.

The Cookbook KG (§18.4) gives each node ONE global complement (central inversion P |-> -P).
Here a node's *address* is a squarefree **conductor** c | N = product of "concept primes"
it contains, so the address factors into the node's conceptual primes. The conductor
lattice 𝒟_N is the Boolean lattice 2^[k] (Cookbook "packets = 2^k - 1"; 32.1 §13 / T33
divisor family), and it is **complemented**: every node has an exact, self-inverse,
*addressable* opposite — the complementary divisor N/c — not one shared axis.

  meet(a,b)  = gcd(a,b)          (shared concepts)
  join(a,b)  = lcm(a,b)          (union of concepts)
  comp(c)    = N // c            (the concepts it lacks);  comp(comp(c)) = c  (involution)
  rank(c)    = omega(c)          (shell = number of concept primes = Boolean-lattice rank)

Pure python/numpy. Deterministic.
"""
import math
import numpy as np

# Six "concept primes", each a topic with discriminative marker terms.
PRIMES = [2, 3, 5, 7, 11, 13]
TOPICS = {
    2:  ["simplicial", "quadray", "rotation", "tetrahedron", "rodrigues", "hodge",
         "curl", "wedge", "octahedron", "rotor"],
    3:  ["primorial", "mertens", "totient", "landau", "sieve", "euler"],
    5:  ["fisher", "cumulant", "amari", "chentsov", "divergence", "entropy"],
    7:  ["riemann", "hypothesis", "critical", "zeros", "weil", "hadamard", "explicit"],
    11: ["character", "dirichlet", "hurwitz", "conductor", "modular", "cyclotomic"],
    13: ["quantum", "density", "hamiltonian", "noether", "gravity", "bekenstein",
         "holographic", "bures"],
}
N_FULL = math.prod(PRIMES)                      # 30030 = P_6

def topic_masses(tokenized_docs):
    """(n, 6) matrix: fraction of each doc's tokens hitting each topic's markers."""
    marker_to_prime = {m: p for p, ms in TOPICS.items() for m in ms}
    pidx = {p: j for j, p in enumerate(PRIMES)}
    M = np.zeros((len(tokenized_docs), len(PRIMES)))
    for i, toks in enumerate(tokenized_docs):
        if not toks:
            continue
        for w in toks:
            p = marker_to_prime.get(w)
            if p is not None:
                M[i, pidx[p]] += 1
        M[i] /= len(toks)
    return M

def conductors(M):
    """Feature present iff a doc is above-average (z>0) on that topic; conductor = product."""
    z = (M - M.mean(0)) / (M.std(0) + 1e-12)
    feats = z > 0
    cond = np.ones(M.shape[0], dtype=np.int64)
    for i in range(M.shape[0]):
        c = 1
        for j, p in enumerate(PRIMES):
            if feats[i, j]:
                c *= p
        cond[i] = c
    return cond, feats

def omega(c):
    return sum(1 for p in PRIMES if c % p == 0)

def complement(c, N=N_FULL):
    assert N % c == 0, f"{c} does not divide {N}"
    return N // c

def meet(a, b):
    return math.gcd(int(a), int(b))

def join(a, b):
    return int(a) * int(b) // math.gcd(int(a), int(b))

def factor_str(c):
    fs = [str(p) for p in PRIMES if c % p == 0]
    return "*".join(fs) if fs else "1"
