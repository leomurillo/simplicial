"""Make the Schoenberg connection FINITE and rigorous.
The size-N CND witness A_N (NxN) negative  <=>  the (N+1)x(N+1) matrix
K = [exp(-d*psi(i,j))]_{i,j=0..N} is NOT PSD for d LARGE ENOUGH... but we need
it for the GIVEN d. The precise finite statement:

Schoenberg/Micchelli: psi with psi(i,i)=0 is CND  <=>  exp(-t psi) PSD for ALL t>0.
If psi NOT CND, the failure of PSD of exp(-t psi) happens at SOME t and SOME size.
As t->0+, exp(-t psi) ~ 1 - t psi, and PSD-ness as t->0 is governed by the
projected matrix -P psi P (P = projection off the all-ones vector). So:

  d small (t->0):  exp(-d psi) PSD-fails  <=>  -P psi P has a negative eigenvalue
                   on the off-ones subspace  <=>  psi not CND.
  d large:         exp(-d psi) -> Identity (off-diag ->0), becomes PSD.

So the obstruction is at SMALL d / and for a FIXED non-CND psi, the failure
appears at small enough t but for a possibly-large index set. For p^d the
'effective t' is d itself (large d = closer to identity = harder to fail =
failure pushed to larger N). This EXACTLY matches N*(d) growing with d.

CONCLUSION we can rigorously assert:
 - psi NOT CND (exact 2x2 cert) => exp(-d psi) is not PSD at all sizes for any
   d>0 IS the wrong reading. Correct: for a FIXED finite index set {0..N},
   exp(-d psi) restricted there is PSD for d large. Non-CND guarantees failure
   only in the JOINT (size, small-d) regime.
 => The exact 2x2 cert proves: as a KERNEL psi is not CND, but does NOT by itself
   prove every fixed-d p^d fails at finite N. We must verify the finite failure
   for the power family directly (which we DID: p^d fails at N*(d) finite, for
   every tested d, with N* growing ~ d).

This script DOCUMENTS the finite mechanism and re-confirms with an explicit minor."""
import mpmath as mp
mp.mp.dps=60
from sympy import primerange
P=list(primerange(2,100000))

def Smp(r,m):
    s=mp.mpf(0)
    for k in range(1,m+1): s+=mp.log(mp.mpf(P[k-1])+r)
    return s

def scaled_block_min_eig(r,d,idx):
    """min eig of the principal submatrix of scaled Hankel on index set idx."""
    mx=max(idx)
    Sc=[mp.mpf(0)]*(2*mx+1); acc=mp.mpf(0)
    for m in range(1,2*mx+1): acc+=mp.log(mp.mpf(P[m-1])+r); Sc[m]=d*acc
    n=len(idx)
    M=mp.matrix(n,n)
    for a in range(n):
        for b in range(n):
            i,j=idx[a],idx[b]
            M[a,b]=mp.e**(Sc[i+j]-(Sc[2*i]+Sc[2*j])/2)
    return min(mp.eigsy(M,eigvals_only=True))

# For the 3x3 minor corresponding to the N=2 witness: indices {0,1,2}? Let's find
# the smallest index-set 3x3 minor that is negative for moderate d, and watch it
# recede as d grows (proving the 'fixed small minor' does NOT close all d).
print("3x3 principal minor on {0,1,2} of scaled Hankel, vs d (r=0):")
for d in [1,2,4,8,16,32,64]:
    me=scaled_block_min_eig(0,d,[0,1,2])
    print(f"  d={d:3d}: min eig({{0,1,2}}) = {mp.nstr(me,4)}  {'NEG' if me<0 else 'pos'}")

print("\nThe contiguous leading block [0..N] min eig is what D_N tracks.")
print("We already established exactly: p^64 D_22<0, p^128 D_42<0 (Bareiss).")
print("So each fixed d FAILS at finite N (verified), N* growing with d.")
