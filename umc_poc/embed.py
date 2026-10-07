"""
embed.py — improvement (a), laptop tier: a local, no-torch semantic encoder (LSA).

The little sphere (Paper 32.1) is metric-agnostic: Hellinger `p -> 2*sqrt(p)` with the
Bhattacharyya inner product is ONE chart; L2-normalized embeddings with cosine are another,
with geodesic distance `arccos(cosine)`. So "swap the node representation to embeddings"
= replace the Bhattacharyya inner product on sqrt(p) by the cosine inner product on
embedding vectors. Everything downstream (MDS placement, capacity-matched depth, conductor
addressing) is unchanged.

This module provides Latent Semantic Analysis embeddings: TF-IDF term-document matrix ->
truncated SVD (numpy) -> dim-d doc vectors. Genuinely semantic (captures co-occurrence /
synonymy), pure numpy, runs on the laptop. The GCP/production tier swaps this one function
for a sentence-embedding model; the rest of the stack does not change.

NOTE (honest): once nodes are embeddings, "KG Fisher-Rao ranking" and "plain cosine
ranking" COINCIDE (arccos is monotone in cosine). So the embedding swap does not give the KG
a *ranking* edge over vanilla cosine-RAG; its residual value over cosine-RAG is the
SELECTION layer -- capacity-matched depth, conductor filter, exact Janus, gaps.
"""
import numpy as np

def build_lsa(C, dim=48):
    """C: (n_docs, n_terms) integer counts. Returns LSA model dict."""
    n, V = C.shape
    tf = C / (C.sum(1, keepdims=True) + 1e-9)
    df = (C > 0).sum(0)
    idf = np.log((n + 1) / (df + 1)) + 1.0
    X = tf * idf
    U, S, Vt = np.linalg.svd(X, full_matrices=False)
    k = int(min(dim, len(S)))
    return {"doc_emb": U[:, :k] * S[:k], "Vk": Vt[:k].T, "idf": idf, "S": S[:k], "k": k}

def cosine_distance_matrix(E):
    """Round-sphere geodesic distance arccos(cosine) between rows of E (n, d)."""
    N = E / (np.linalg.norm(E, axis=1, keepdims=True) + 1e-9)
    return np.arccos(np.clip(N @ N.T, -1.0, 1.0))

def encode_query(query_counts, model):
    """Fold a query (count vector over the vocab) into the LSA doc space."""
    qtf = query_counts / (query_counts.sum() + 1e-9)
    return (qtf * model["idf"]) @ model["Vk"]

def cosine_to(query_vec, E):
    """Cosine similarity of one query embedding to all doc embeddings E (n,d)."""
    n = E / (np.linalg.norm(E, axis=1, keepdims=True) + 1e-9)
    q = query_vec / (np.linalg.norm(query_vec) + 1e-9)
    return n @ q
