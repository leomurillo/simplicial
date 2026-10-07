import numpy as np

def U_block(N):
    w = np.exp(2j*np.pi/np.float64(N)); j=np.arange(N)
    F = w**np.outer(j,j)/np.sqrt(N)
    H = np.zeros((N,N)); H[0,:]=1/np.sqrt(N)
    for k in range(1,N):
        H[k,:k]=1.0; H[k,k]=-k; H[k]/=np.sqrt(k*(k+1))
    return (H@F.T)[1:,1:]

# Bare DFT restricted to mean-zero hyperplane: project out all-ones, eigenvalues of F on H_N
def F_restricted_spectrum(N):
    w = np.exp(2j*np.pi/np.float64(N)); j=np.arange(N)
    F = w**np.outer(j,j)/np.sqrt(N)
    # Helmert H gives orthonormal basis; rows 1.. span H_N. Restrict F to that basis:
    H = np.zeros((N,N)); H[0,:]=1/np.sqrt(N)
    for k in range(1,N):
        H[k,:k]=1.0; H[k,k]=-k; H[k]/=np.sqrt(k*(k+1))
    Fr = (H @ F @ H.conj().T)[1:,1:]   # F restricted to H_N in Helmert coords (bare DFT, NOT transposed/conjugated dressing)
    return np.linalg.eigvals(Fr)

# Key question: is U_N = H F^T [1:,1:] EXACTLY equal to bare DFT restricted? Compare to H F H* form.
for N in [5,6,7,8]:
    w = np.exp(2j*np.pi/np.float64(N)); j=np.arange(N)
    F = w**np.outer(j,j)/np.sqrt(N)
    H = np.zeros((N,N)); H[0,:]=1/np.sqrt(N)
    for k in range(1,N):
        H[k,:k]=1.0; H[k,k]=-k; H[k]/=np.sqrt(k*(k+1))
    U = (H@F.T)[1:,1:]                      # apex unitary (Helmert-dressed, transpose)
    Frestr = (H@F@H.conj().T)[1:,1:]        # bare DFT genuinely restricted to H_N
    evU = np.sort_complex(np.linalg.eigvals(U))
    evF = np.sort_complex(np.linalg.eigvals(Frestr))
    # are they the same matrix up to the conj/transpose convention?
    diff = np.min([np.max(np.abs(U-Frestr)), np.max(np.abs(U-Frestr.conj().T))])
    print(f"N={N}: |U - F|restr min(direct,conj.T) = {diff:.3e}")
    print(f"   apex eigs:      {np.round(evU,4)}")
    print(f"   bareDFT|H eigs: {np.round(evF,4)}")
    print(f"   |det U|={abs(np.linalg.det(U)):.4f} det U={np.linalg.det(U):.4f}  det(F|H)={np.linalg.det(Frestr):.4f}")
