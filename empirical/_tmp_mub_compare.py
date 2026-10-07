import numpy as np

def full_dft_mult(N):
    # Standard DFT (unitary) eigenvalue multiplicities (McClellan-Parks), order [1, i, -1, -i]
    m = N // 4
    r = N % 4
    if r == 0: return (m+1, m,   m,   m-1)
    if r == 1: return (m+1, m,   m,   m)
    if r == 2: return (m+1, m+1, m,   m-1)
    if r == 3: return (m+1, m+1, m+1, m)

def apex_mult_predicted(N):
    q = N // 4
    return {1:(q,q,q,q),2:(q+1,q,q,q),3:(q+1,q,q,q+1),0:(q,q-1,q,q)}[N % 4]

# The trivial constant mode (all-ones) is a DFT eigenvector with eigenvalue +1.
# Apex U_N acts on the mean-zero hyperplane = DFT space minus that one +1 eigenvector.
# So apex spectrum should = full DFT spectrum with ONE +1 removed -- IF U_N were the
# DFT restricted to H_N. But U_N = Helmert-dressed DFT, NOT the bare restricted DFT.
print(f"{'N':>5} {'fullDFT(1,i,-1,-i)':>22} {'minus one +1':>16} {'apexPredicted':>16} {'match?':>7}")
for N in [4,5,6,7,8,9,10,11,12,16,30,64,256,1000,2001,2048,4096]:
    fd = full_dft_mult(N)
    fd_minus = (fd[0]-1, fd[1], fd[2], fd[3])  # remove one +1 (trivial mode)
    ap = apex_mult_predicted(N)
    match = (fd_minus == ap)
    print(f"{N:>5} {str(fd):>22} {str(fd_minus):>16} {str(ap):>16} {str(match):>7}")

# Now compute the ACTUAL apex spectrum and compare clustering to {1,i,-1,-i}
print("\nActual U_N spectrum clustering vs full-DFT-minus-trivial:")
def U_block(N):
    w = np.exp(2j*np.pi/np.float64(N)); j=np.arange(N)
    F = w**np.outer(j,j)/np.sqrt(N)
    H = np.zeros((N,N)); H[0,:]=1/np.sqrt(N)
    for k in range(1,N):
        H[k,:k]=1.0; H[k,k]=-k; H[k]/=np.sqrt(k*(k+1))
    return (H@F.T)[1:,1:]
roots=np.array([1,1j,-1,-1j])
for N in [4,5,6,7,8,9,12,16,30]:
    ev=np.linalg.eigvals(U_block(N)); cnt=[0,0,0,0]
    for e in ev:
        cnt[int(np.argmin(np.abs(e-roots)))]+=1
    fd=full_dft_mult(N); fdm=(fd[0]-1,fd[1],fd[2],fd[3])
    print(f" N={N:>4} apexCluster={tuple(cnt)}  DFTminusTrivial={fdm}  equal={tuple(cnt)==fdm}")
