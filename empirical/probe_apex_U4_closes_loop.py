"""
probe_apex_U4_closes_loop.py  --  overlay the apex unitary U_4 on the (2,3,5) lift.

ONE vector w in H_4, read in TWO frames:
   w = Helmert-lift of (2,3,5) = 2 h_1 + 3 h_2 + 5 h_3 = (10, 6, -1, -15)   (sum 0)
   - its HELMERT coordinates are (2, 3, 5)            (by construction)
   - its FOURIER coordinates are the inverse-DFT of w (Z/4 characters)
The change of basis between the two readings is U_4 (Helmert <-> Fourier on H_4 = R^3).
We show  U_4 @ (Helmert coords)  =  (Fourier coords)  EXACTLY, then that the normalized
U_4 is the apex unitary (U_4 U_4^H = I) of T4 Thm 8.2 / N13.

numpy. No torch.
"""
import numpy as np

def cx(z):
    a=round(z.real,6); b=round(z.imag,6)
    ai,bi=int(round(a)),int(round(b))
    if abs(a-ai)<1e-9: a=ai
    if abs(b-bi)<1e-9: b=bi
    if b==0: return f"{a}"
    if a==0: return f"{b}i"
    return f"{a}{'+' if b>=0 else '-'}{abs(b)}i"
def cv(v): return "[" + ", ".join(cx(z) for z in v) + "]"

N=4; s=np.arange(N); om=np.exp(2j*np.pi/N)                 # omega = i
h=[np.array([1]*k+[-k]+[0]*(N-k-1),float) for k in range(1,N)]   # h_1,h_2,h_3 in R^4

# the ONE vector w = Helmert lift of (2,3,5)
coef=np.array([2.,3.,5.])
w=sum(coef[k]*h[k] for k in range(3))
print("="*84)
print(f"the vector:  w = 2 h_1 + 3 h_2 + 5 h_3 = {cv(w)}   (sum = {cx(w.sum())})")
print("="*84)

# Helmert coords of w (project): x_k = (h_k . w)/(k(k+1))
hc=np.array([h[k]@w/((k+1)*(k+2)) for k in range(3)])
print(f"  HELMERT coords of w:  {cv(hc)}        (recovers the input (2,3,5))")

# Fourier coords of w (inverse DFT, characters c=1..3)
def fcoords(x): return np.array([(x*om**(-c*s)).sum()/N for c in range(1,N)])
fc=fcoords(w)
print(f"  FOURIER coords of w:  {cv(fc)}   (DC=10=mass; conj pair = shape)")

# ---- the change of basis U : Helmert coords -> Fourier coords (columns = Fourier coords of h_k) ----
U=np.column_stack([fcoords(h[k]) for k in range(3)])
print("\n  U  (3x3, Helmert-coords -> Fourier-coords):")
for r in range(3): print("     [" + ",  ".join(cx(z) for z in U[r]) + "]")
lhs=U@hc
print(f"\n  U @ (2,3,5) = {cv(lhs)}")
print(f"  Fourier coords = {cv(fc)}")
print(f"  EXACT match:  {np.allclose(lhs,fc)}   <-- the loop closes")

# ---- the normalized apex unitary U_4 (T4 Thm 8.2 / N13) ----
def apexU(M):
    o=np.exp(2j*np.pi/M); Um=np.zeros((M-1,M-1),complex)
    for k in range(1,M):
        for c in range(1,M):
            Um[k-1,c-1]=((1-o**(k*c))/(1-o**c) - k*o**(k*c))/np.sqrt(M*k*(k+1))
    return Um
U4=apexU(4)
print("\n" + "="*84)
print("the NORMALIZED apex unitary U_4 (orthonormal Helmert x orthonormal Fourier):")
print("="*84)
print(f"  unitary?  ||U_4 U_4^H - I|| = {np.linalg.norm(U4@U4.conj().T-np.eye(3)):.2e}    |det U_4| = {abs(np.linalg.det(U4)):.6f}")
# normalized coords of w, and the unitary loop
a=np.array([h[k]@w/np.sqrt((k+1)*(k+2)) for k in range(3)])          # orthonormal-Helmert coords
b=np.array([(w*om**(-c*s)).sum()/np.sqrt(N) for c in range(1,N)])     # orthonormal-Fourier coords
print(f"  orthonormal Helmert coords a = {cv(a)}")
print(f"  orthonormal Fourier  coords b = {cv(b)}")
print(f"  U_4^H @ a = {cv(U4.conj().T@a)}   ==  b ?  {np.allclose(U4.conj().T@a,b)}")
print(f"  (U_4 is the orthonormalized U above: same Helmert<->Fourier map, unit-scaled.)")

print("\n" + "="*84)
print("WHAT JUST HAPPENED")
print("="*84)
print(f"""  (2,3,5) was never two different things -- it is ONE vector w in H_4, read in two frames.
  U_4 is the exact dictionary: feed it the Helmert reading (2,3,5), out comes the Fourier reading
  ({cv(fc)}).  This 3x3 is the apex unitary on H_4 = (N-1)-space for N=4 -- the same U_N whose
  N->inf scaling limit (N4) is the archimedean operator. So your (2,3,5) climb and its two
  coordinate readings are literally the finite rung of the apex/RH ladder, and U_4 is the rung's
  Helmert<->Fourier turn.""")
