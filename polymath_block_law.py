"""
GENERAL BLOCK-FACTORIZATION LAW (the engine).

Setup: b_0=1, b_n=prod_{i=1}^n c_i with c_i=f(p_i)>0. Consider the principal Hankel minor on a
CONSECUTIVE index block {k, k+1, ..., k+r} (size r+1):
    M = det( b_{i+j} )_{i,j in {k,...,k+r}}.
CLAIM: M = (sign/const) * [ prod over the c_l that appear ] * core, and more usefully:
    sign(M) on the valid region {c_l>0} equals sign of a 'reduced' determinant det(R) where
    R_{i,j} = prod_{l=k+i+1}^{k+i+j} c_l   (a matrix whose entries are partial products),
because b_{k+i+j} = b_{k+i} * prod_{l=k+i+1}^{k+i+j} c_l, and b_{k+i}>0 factors out of row i.
Thus M = (prod_{i=0}^r b_{k+i}) * det(R),  and prod b_{k+i} > 0  =>  sign(M)=sign(det R).
det(R) is a polynomial in the c_l (l from k+1 to k+2r). It VANISHES whenever a 'pivotal' c_l=0
in a way that makes rows dependent — but the precise factorization (which c_l divide det R and to
what multiplicity, leaving the 'core') is what we observed. The SIGN law sign(M)=sign(det R) is
EXACT and elementary. Verify it for several blocks/degrees.
"""
from sympy import primerange, Matrix, Integer, symbols, simplify, factor, prod, expand
import sympy as sp
PR=list(primerange(2,200))

def check_block(degree, k, r, label):
    c=symbols('c1:40', positive=True)   # c_1..c_39 generic positive (fully general ratios)
    # b_0=1, b_n=prod_{i=1}^n c_i
    def b(n):
        p=Integer(1)
        for i in range(1,n+1): p*=c[i-1]
        return p
    # M on block {k..k+r}
    idx=list(range(k,k+r+1))
    M=Matrix(r+1,r+1, lambda i,j: b(idx[i]+idx[j]))
    # R reduced: factor b_{k+i} from row i. Hankel entry (i,j) = b_{(k+i)+(k+j)}.
    # = b_{k+i} * prod_{l=(k+i)+1}^{(k+i)+(k+j)} c_l. So R[i][j]=that product.
    def R_entry(i,j):
        ii=idx[i]; jj=idx[j]
        p=Integer(1)
        for l in range(ii+1, ii+jj+1):
            p*=c[l-1]
        return p
    R=Matrix(r+1,r+1,R_entry)
    # claim: M == (prod_{i} b(idx[i])) * det(R)
    lhs=M.det()
    rhs=prod([b(idx[i]) for i in range(r+1)])*R.det()
    eq=simplify(expand(lhs-rhs))==0
    print(f"{label}: M == (prod b_{{k+i}})*det(R) ?  {eq}")
    return eq

print("Proving sign(M_block)=sign(det R) via the identity M=(prod b_{k+i})*det R (generic c_l>0):")
check_block(1,0,2,"block {0,1,2}, size 3")
check_block(1,2,2,"block {2,3,4}, size 3")
check_block(1,1,3,"block {1,2,3,4}, size 4")
check_block(1,2,3,"block {2,3,4,5}, size 4")
check_block(1,0,4,"block {0,1,2,3,4}, size 5")
print("\nSince prod b_{k+i} = prod_{i} prod_{l<=k+i} c_l > 0 on the valid region,")
print("=> sign(M_block) = sign(det R). This is the EXACT, fully general sign-reduction.")
print("(det R is the 'W'-type matrix of partial products; its factorization yields the f(p)-factors")
print(" and the CORE polynomial used in the proofs.)")
