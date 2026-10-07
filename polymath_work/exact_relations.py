"""
NAIL DOWN exact relations. Define everything from scratch, no shortcuts.

H = (b_{i+j})_{i,j>=0}, b_0=1, b_n=prod_{l=1}^n c_l, c_l=f(p_l).

OBJECT 1: leading principal minor of H on {0..N} = D_N. (the original Hankel det)
OBJECT 2: contiguous principal minor of H on {i,i+1,...,i+N} =: D_N^{(i)} (offset i).
OBJECT 3: shifted sequence b^{(k)}_n := b_{k+n}/b_k = prod_{l=k+1}^{k+n} c_l.
          Its leading principal minor on {0..N} =: E_N^{(k)} = det(b^{(k)}_{i+j})_{0<=i,j<=N}.

RELATION (shift): E_N^{(k)} = det( b_{k+i+j}/b_k ) = (1/b_k^{N+1}) det(b_{k+i+j})_{i,j=0..N}.
   But det(b_{k+i+j})_{i,j} is the minor of H on rows {k,k+1,..,k+N} and cols {k,k+1,..,k+N}?
   NO: entry (i,j) is b_{k+i+j} = H_{k+i, j}?? H_{r,c}=b_{r+c}. We want b_{k+i+j}=H_{r,c} with
   r+c=k+i+j. The minor on rows {k..k+N} cols {0..N}: entry H_{k+i, j}=b_{k+i+j}. YES.
   So det(b_{k+i+j})_{i,j=0..N} = minor of H on ROWS {k,..,k+N}, COLS {0,..,N}. That's NOT a
   principal minor (rows != cols) unless k=0. So E_N^{(k)} is (up to b_k^{N+1}>0) a NON-principal
   minor of H. Its sign is NOT directly constrained by PSD.

   HOWEVER, b^{(k)} as a SEQUENCE: is it a moment sequence when b is? b^{(k)}_n = ∫ x^n dν_k,
   ν_k = x^k dμ / b_k. For Hamburger μ (on ℝ), ν_k is a positive measure ONLY if x^k>=0, i.e.
   k EVEN. For k even, ν_k>=0 is a genuine positive measure, so (b^{(k)}_n)_n IS a Hamburger
   moment sequence, hence its LEADING Hankel minors E_N^{(k)} >= 0 for all N.
   => If b is Hamburger-moment, then for every EVEN k and every N: E_N^{(k)} >= 0.
   Contrapositive: E_N^{(k)}<0 for some even k => b NOT moment.   [VALID]

OBJECT 4: Psi(s) earlier = c_{s+2} g_s g_{s+2} - c_s g_{s+1}^2, claimed = sign of contiguous
   minor D_2^{(i)} with s=2i+1. Let me RE-VERIFY that and ALSO compute E_2^{(k)} and see its
   relation to a 'window' so I can use the EVEN-k shift correctly.

Let me compute symbolically:
  E_2^{(k)} leading minor of b^{(k)}: uses ratios c_{k+1},c_{k+2},c_{k+3},c_{k+4} (since
  b^{(k)}_1=c_{k+1}, b^{(k)}_2=c_{k+1}c_{k+2}, etc.) Its det W2-form = det W2 with window c_{k+1}..
  = c_{k+3} (c_{k+2}-c_{k+1})(c_{k+4}-c_{k+3}) - c_{k+1}(c_{k+3}-c_{k+2})^2   [by our gap identity
    det W2 = c3 g1 g3 - c1 g2^2 with c1=c_{k+1},c2=c_{k+2},c3=c_{k+3},c4=c_{k+4}].
  Define W(k) := c_{k+3} (c_{k+2}-c_{k+1})(c_{k+4}-c_{k+3}) - c_{k+1}(c_{k+3}-c_{k+2})^2.
  Sign(E_2^{(k)}) = sign(W(k)).  And W(k)<0 with k EVEN => not moment.

  Compare Psi(s): Psi(s)=c_{s+2}(c_{s+1}-c_s)(c_{s+3}-c_{s+2}) - c_s (c_{s+2}-c_{s+1})^2
    = c_{s+2} g_s g_{s+2} - c_s g_{s+1}^2  with g_l=c_{l+1}-c_l.
  W(k): set s=k+1: W(k)=c_{(k+1)+2}(c_{(k+1)+1}-c_{(k+1)})(c_{(k+1)+3}-c_{(k+1)+2}) - c_{(k+1)}(c_{(k+1)+2}-c_{(k+1)+1})^2
       = Psi(s=k+1). YES! W(k)=Psi(k+1).
  So sign(E_2^{(k)}) = sign(Psi(k+1)).  k EVEN => s=k+1 ODD. So the EVEN-k shift controls ODD s.
  => Psi(s)<0 for ODD s => E_2^{(s-1)} <0 with s-1 even => NOT moment. CONSISTENT with contiguous
     (which also gave odd s). So BOTH methods cover ODD s. EVEN s is the one NOT directly covered!

  Need EVEN s coverage. For EVEN s: s-1 odd, E_2^{(s-1)} uses ODD shift k=s-1 -> ν_k signed. And
  contiguous minor gave s=2i+1 ODD only. So is EVEN-s firing actually a valid witness??
  Let me CHECK directly: does Psi(s)<0 at EVEN s correspond to ANY negative principal minor?
  Earlier OPTION-A search FOUND negative principal minors at various index sets. Let me map an
  EVEN-s firing to an explicit negative PRINCIPAL minor by direct search, to be safe.
"""
from sympy import primerange, Matrix, Integer, symbols, expand, factor
# symbolic check W(k)=Psi(k+1)
c=symbols('c1:8',positive=True)
cc={l:c[l-1] for l in range(1,8)}
def Psi_sym(s):
    g0=cc[s+1]-cc[s]; gm=cc[s+2]-cc[s+1]; g2=cc[s+3]-cc[s+2]
    return cc[s+2]*g0*g2 - cc[s]*gm**2
def W_sym(k):
    return cc[k+3]*(cc[k+2]-cc[k+1])*(cc[k+4]-cc[k+3]) - cc[k+1]*(cc[k+3]-cc[k+2])**2
print("W(1)-Psi(2) =", expand(W_sym(1)-Psi_sym(2)), "(expect 0 => W(k)=Psi(k+1))")

# Now the REAL question: even-s firing -> explicit NEGATIVE PRINCIPAL minor. Direct search.
Pg=list(primerange(2,500000))
def make_b(ff,L):
    b=[Integer(1)];A=Integer(1)
    for i in range(1,L):
        A*=ff(Pg[i-1]); b.append(A)
    return b
import itertools
def Psi(ff,s):
    def C(l): return Integer(ff(Pg[l-1]))
    g0=C(s+1)-C(s); gm=C(s+2)-C(s+1); g2=C(s+3)-C(s+2)
    return C(s+2)*g0*g2 - C(s)*gm**2
# f=p, first EVEN firing s=8. Find a NEGATIVE PRINCIPAL 3x3 minor (rows=cols) anywhere.
for name,ff in [("p",lambda p:p),("p^12+3",lambda p:p**12+3),("p^7+1",lambda p:p**7+1)]:
    se=next(s for s in range(2,300000) if s%2==0 and Psi(ff,s)<0)
    lim=min(2*se+6, 38)
    b=make_b(ff, 2*lim+4)
    # search principal minors on index windows near se
    found=None
    Hbig=Matrix(lim+1,lim+1,lambda i,j:b[i+j])
    for idx in itertools.combinations(range(lim+1),3):
        if Hbig[idx,idx].det()<0:
            found=idx; break
    print(f"{name:10s}: first EVEN firing s={se}; a NEGATIVE PRINCIPAL 3x3 minor at indices {found} "
          f"(det<0 => not moment). [principal minor EXISTS regardless of parity]")
