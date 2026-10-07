import sympy as sp
from itertools import product

# PART (a): Is T = grad^3 Phi globally constant in ANY affine coordinate system?
#
# Phi = log Z = log( sum_a exp(theta . e_a) )  (categorical/multinomial log-partition,
#   natural parameters theta_1..theta_{N-1}, atom 0 as reference).
#
# KEY FACT: under an affine (invertible-linear + shift) change of natural coordinate
#   theta = A psi + b, the 4th derivative tensor transforms TENSORIALLY:
#       T4'_{ijkl}(psi) = sum A_i^a A_j^b A_k^c A_l^d  T4_{abcd}(theta(psi)).
#   So T4 vanishes identically in SOME affine frame  <=>  T4 vanishes identically
#   in EVERY affine frame (linear map of a tensor that is identically zero is zero;
#   and conversely if it's nonzero somewhere, the linear image is nonzero since A invertible).
#   Therefore: T = grad^3 Phi is globally constant in SOME affine coordinate
#   <=> T4 = grad^4 Phi == 0 everywhere <=> the 4th cumulant tensor vanishes identically.
#
# A 4th cumulant of a NON-degenerate exponential family is the 4th-order connected
# moment. We prove it is NOT identically zero by exhibiting it nonzero at the centroid,
# and we QUANTIFY the flow. Cumulants are coordinate-affine-covariant, so one nonzero
# component in one frame => nonzero tensor in every frame.

def cumulants_categorical(N, p):
    """Return k2,k3,k4 cumulant tensors of the sufficient statistic e_a = standard basis
    indicator on atoms 1..N-1 (atom 0 reference), under probability vector p (len N).
    These are the central connected moments of the indicator vector (X_1..X_{N-1}),
    X_i = 1[atom == i]. Exact via sympy rationals."""
    n = N-1
    # E[X_i] = p_i  (i=1..N-1)
    mu = [p[i+1] for i in range(n)]
    # For multinomial single-draw indicators:
    # moments: E[prod over chosen] = p of the common index if all equal else 0 (indicators of disjoint events; product of distinct indicators = 0)
    # Actually X_i X_j = 0 for i!=j (disjoint atoms); X_i^m = X_i.
    # So joint raw moment E[ X_{i1}...X_{ir} ] = p_i if i1=...=ir=i, else 0.
    def raw(idx):
        s=set(idx)
        if len(s)==1:
            i=idx[0]
            return p[i+1]
        else:
            return sp.Integer(0)
    # central via cumulant formulas in terms of raw moments and mu.
    # k2_{ij} = E[X_i X_j] - mu_i mu_j
    k2 = [[raw((i,j)) - mu[i]*mu[j] for j in range(n)] for i in range(n)]
    # k3_{ijk} = E[XiXjXk] - sum E[XiXj]mu_k (3 terms) + 2 mu_i mu_j mu_k
    def k3comp(i,j,k):
        m3 = raw((i,j,k))
        m2 = raw((i,j))*mu[k] + raw((i,k))*mu[j] + raw((j,k))*mu[i]
        return m3 - m2 + 2*mu[i]*mu[j]*mu[k]
    k3 = [[[k3comp(i,j,k) for k in range(n)] for j in range(n)] for i in range(n)]
    # k4_{ijkl}: 4th cumulant in terms of raw moments
    # k4 = m4 - sum_{(3|1)} m3 m1 (4 terms) - sum_{(2|2) pair-partitions, 3 of them} m2 m2
    #      + 2 sum_{(2|1|1), 6 terms} m2 m1 m1 - 6 m1 m1 m1 m1
    def k4comp(i,j,k,l):
        idx=(i,j,k,l)
        m4 = raw(idx)
        # 3|1 splits: choose which single index is split off; 4 ways
        m31 = (raw((j,k,l))*mu[i] + raw((i,k,l))*mu[j] + raw((i,j,l))*mu[k] + raw((i,j,k))*mu[l])
        # 2|2 splits into unordered pairs of pairs: {ij,kl},{ik,jl},{il,jk}
        m22 = (raw((i,j))*raw((k,l)) + raw((i,k))*raw((j,l)) + raw((i,l))*raw((j,k)))
        # 2|1|1 splits: choose the pair (6 ways), times product of the two singles' mu
        pairs = [((i,j),(k,l)),((i,k),(j,l)),((i,l),(j,k)),
                 ((j,k),(i,l)),((j,l),(i,k)),((k,l),(i,j))]
        m211 = sum(raw(p2)*mu[a]*mu[b] for (p2,(a_,b_)) in
                   [((i,j),(k,l)),((i,k),(j,l)),((i,l),(j,k)),((k,l),(i,j)),((j,l),(i,k)),((j,k),(i,l))]
                   for (a,b) in [ tuple(sorted(set((i,j,k,l)) - set(p2))) ] )
        m1111 = mu[i]*mu[j]*mu[k]*mu[l]
        return m4 - m31 - m22 + 2*m211 - 6*m1111
    k4 = {}
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    k4[(i,j,k,l)] = sp.nsimplify(k4comp(i,j,k,l))
    return k2,k3,k4

# Sanity check against KNOWN closed forms via grad^4 of log Z directly (symbolic), N=3.
def logZ_cumulants_symbolic(N):
    th = sp.symbols(f'th1:{N}', real=True)  # theta_1..theta_{N-1}
    Z = 1 + sum(sp.exp(th[i]) for i in range(N-1))  # atom0 weight 1
    Phi = sp.log(Z)
    n=N-1
    g = [[sp.diff(Phi, th[i], th[j]) for j in range(n)] for i in range(n)]
    T3 = [[[sp.diff(Phi, th[i], th[j], th[k]) for k in range(n)] for j in range(n)] for i in range(n)]
    T4 = {}
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    T4[(i,j,k,l)] = sp.diff(Phi, th[i],th[j],th[k],th[l])
    return th, Phi, g, T3, T4

# N=3 centroid: theta=0 => p = (1/3,1/3,1/3)
th, Phi, g, T3, T4sym = logZ_cumulants_symbolic(3)
subs0 = {th[0]:0, th[1]:0}
print("=== N=3, centroid (theta=0, p=(1/3,1/3,1/3)) ===")
print("g (metric, =grad^2 Phi):")
g0 = sp.Matrix([[sp.simplify(g[i][j].subs(subs0)) for j in range(2)] for i in range(2)])
sp.pprint(g0)
print("k3 components (grad^3 Phi):")
for i in range(2):
    for j in range(2):
        for k in range(2):
            print(f"  T3[{i}{j}{k}] =", sp.simplify(T3[i][j][k].subs(subs0)))
print("k4 components (grad^4 Phi) at centroid:")
mx=sp.Integer(0)
for key,val in T4sym.items():
    v=sp.simplify(val.subs(subs0))
    if v!=0:
        print(f"  T4{key} =", v)
        mx=max(mx, abs(v))
print("MAX |T4| at centroid =", mx, " => T4 != 0 AT the centroid (proves NOT a cubic-polynomial point).")
