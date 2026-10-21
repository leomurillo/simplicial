"""Structure of the a priori optimum (Paper 53 §4.12(c), certificate K10c): agreement with mu, mollifier weights, tight constraints."""
import math
import numpy as np
from p53_chebyshev_lp import J_of, F, psi_table, mobius
from p53_apriori_scale import apriori_sparse
from p53_apriori_lp import S, b
psi,_ = psi_table(10**5); mu = mobius(10**6)
for x, r in ((10**4, 8), (10**5, 6)):
    J = J_of(x); s = math.isqrt(x); K = int(r*s)
    E, c, _ = apriori_sparse(x, K, J)
    ks = np.arange(1, K+1)
    A = (J[:,None]//ks[None,:] - J[:,None]//(2*ks[None,:])).astype(float)
    G = A @ c
    H = float(np.sum(c*np.array([F(x//k) for k in ks])))
    win = psi[x]-psi[x//2]
    dev = np.nonzero(np.abs(c - mu[1:K+1]) > 1e-6)[0]
    print(f"x={x} K={K}: window={win:.2f} <= exact H(c)={H:.2f} <= E(c)={E:.2f};  min G-[j=1] on J = {np.min(G-(J==1)):.2e}")
    print(f"   first deviation from mu at k={dev[0]+1} (x^(1/4)={x**0.25:.1f});  C(1)={np.sum(c/ks):+.3e}  C'(1)-1={-np.sum(c*np.log(ks)/ks)-1:+.3e}")
    for lo, hi in ((1, s//4), (s//4, s), (s, 2*s), (2*s, 4*s), (4*s, K)):
        seg = c[lo-1:hi-1] if hi>lo else c[:0]
        m = mu[lo:hi]
        if len(seg):
            corr = np.corrcoef(seg, m)[0,1] if np.std(seg)>0 and np.std(m)>0 else float('nan')
            print(f"   k in [{lo},{hi}): l1={np.sum(np.abs(seg)):8.2f}  mean c/mu on mu!=0: {np.mean(seg[m!=0]/m[m!=0]):+.3f}  corr(c,mu)={corr:+.3f}  nonzero on mu=0: {np.sum(np.abs(seg[m==0])>1e-6)}/{np.sum(m==0)}  max|c|={np.max(np.abs(seg)):.2f}")
    tight = np.abs(G-(J==1)) < 1e-7
    print(f"   tight constraints: {np.sum(tight)}/{len(J)}  (j<=sqrt x: {np.sum(tight & (J<=s))}/{np.sum(J<=s)})")
