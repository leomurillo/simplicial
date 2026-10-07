"""
probe_etf_apex_envelope_rates.py  --  make the "algebraic skeleton vs transcendental residue" split
CONCRETE, with rates. Answers Leo's T4-ETF question: is the ETF->orthonormal blending the same
convergence as the apex->archimedean residual? Three objects, one axis:

  (A) ETF defect  -1/(N-1)         : function of N, RATIONAL, -> 0^- at rate 1/N; frame stays kappa=1.
  (A) apex edge displacement d_N   : function of N, -> a CONSTANT < 1/8 (the sqrt i = pi/4 ceiling).
  (C) archimedean envelope         : function of the SPECTRAL variable t (NOT N): modulus 1/sqrt(2cosh pi t),
                                     non-normality ratio e^{pi t} -- TRANSCENDENTAL, the limit residue.

The two (A)'s are the finite-ladder ALGEBRAIC skeleton (both resolve as N->inf, meeting the pi/4 landmark).
The pi/4 = 1/8-turn phase is sqrt i = zeta_8, ABSORBABLE into the M=4I cyclotomic metric (algebraic).
The (C) envelope is the TRANSCENDENTAL residue -- the archimedean place, the RH wall -- not a finite-N
convergence at all. They TOUCH at pi/4; that touch is the absorbable algebraic part, not the residue.

Deterministic numpy + mpmath. No torch.
"""
import numpy as np
import mpmath as mp
mp.mp.dps = 25

# =============================================================================================
# (A1) the ETF / Helmert skeleton: regular simplex ETF in H_N (T4's frame)
# =============================================================================================
def etf_gram(N):
    V = np.eye(N) - np.ones((N, N)) / N            # centered standard basis: columns e_i - 1/N (span H_N)
    V = V / np.linalg.norm(V, axis=0)              # unit vectors = the regular simplex ETF
    G = V.T @ V                                     # Gram
    sv = np.linalg.svd(G, compute_uv=False)
    nz = sv[sv > 1e-9]                              # nonzero singular values on H_N
    offdiag = G[0, 1]
    kappa = nz.max() / nz.min()                    # frame conditioning on H_N
    return offdiag, kappa

# =============================================================================================
# (A2) the apex unitary U_N (Helmert x Fourier) and its edge displacement toward the 1/8 ceiling
# =============================================================================================
def U_apex(N):
    idx = np.arange(1, N)
    K, J = np.meshgrid(idx, idx, indexing='ij')    # rows k, cols j, both 1..N-1
    wj  = np.exp(2j*np.pi*(J % N)/N)
    wjk = np.exp(2j*np.pi*((J*K) % N)/N)
    num = (wjk - 1)/(wj - 1) - K*wjk               # geometric sum minus balancing entry
    return num/np.sqrt(N*K*(K+1.0))

def apex_edge_displacement(N):
    U = U_apex(N)
    unit_err = np.linalg.norm(U @ U.conj().T - np.eye(N-1))   # unitarity check
    ph = (np.angle(np.linalg.eigvals(U))/(2*np.pi)) % 1.0     # eigenphases in TURNS, [0,1)
    roots = np.array([0.0, 0.25, 0.5, 0.75])                  # 4th roots of unity (N3 concentration)
    d = np.abs(ph[:, None] - roots[None, :])
    d = np.minimum(d, 1 - d).min(axis=1)                      # circular dist to nearest 4th root
    return d.max(), unit_err                                  # delta_max(N), unitarity residual

print("="*92)
print("(A) TWO ALGEBRAIC CONVERGENCES IN N  (the finite-ladder skeleton; both resolve as N->inf)")
print("="*92)
print(f"  {'N':>5} {'ETF offdiag -1/(N-1)':>22} {'ETF angle (deg)':>16} {'ETF kappa':>11} {'apex d_max (turns)':>20} {'||UU*-I||':>11}")
Ns = (8, 16, 32, 64, 128, 256, 512, 1024)
deltas = []
for N in Ns:
    off, kap = etf_gram(N)
    dmax, uerr = apex_edge_displacement(N)
    deltas.append(dmax)
    ang = np.degrees(np.arccos(off))
    print(f"  {N:>5} {off:>+22.6f} {ang:>16.4f} {kap:>11.6f} {dmax:>20.6f} {uerr:>11.1e}")
# deceleration + geometric-tail extrapolation of the apex edge limit
diffs = [deltas[i+1] - deltas[i] for i in range(len(deltas)-1)]
ratios = [diffs[i+1]/diffs[i] for i in range(len(diffs)-1)]
r = diffs[-1]/diffs[-2]
est = deltas[-1] + diffs[-1]*r/(1-r) if 0 < r < 1 else float('nan')
print(f"\n  apex d_max increments (per N-doubling): {', '.join(f'{d:.5f}' for d in diffs)}")
print(f"  increment ratios (<1 = decelerating):  {', '.join(f'{rr:.3f}' for rr in ratios)}")
print(f"  geometric-tail extrapolation: d_inf ~ {est:.4f}  (ROUGH; N4 value 0.097; ceiling 1/8 = 0.125)")
print("  => ETF defect -> 0^- at rate 1/N (RATIONAL), angle -> 90^+ , kappa == 1 EXACTLY (perfect skeleton).")
print("     apex d_max INCREASES, decelerating, settling near ~0.09 (consistent with N4 d_inf=0.097),")
print("     STRICTLY BELOW the 1/8 = sqrt i / pi/4 ceiling throughout. Both ALGEBRAIC in N.")

# =============================================================================================
# (B) the pi/4 = 1/8-turn landmark where they meet, and its split: phase (absorbable) vs modulus (residue)
# =============================================================================================
print("\n"+"="*92)
print("(B) the pi/4 landmark: N4 eigenvalue scale  lambda(t) = e^{i pi/4} / sqrt(2 cosh pi t)")
print("="*92)
C = np.array([[0,0,0,-1],[1,0,0,0],[0,1,0,0],[0,0,1,0]], float)   # companion of x^4+1 = mult-by-zeta_8
CtC = C.T @ C
C4  = np.linalg.matrix_power(C, 4)
S2  = C + np.linalg.matrix_power(C, 7)                             # zeta_8 + zeta_8^{-1} = sqrt 2
print(f"  PHASE  arg lambda = pi/4 = 1/8 turn = sqrt i = zeta_8 = e^{{i pi/4}} = (1+i)/sqrt2  -- the apex d ceiling.")
print(f"    zeta_8 as integer companion C (x^4+1):  C^T C = I? {np.allclose(CtC, np.eye(4))};  C^4 = -I? {np.allclose(C4,-np.eye(4))}")
print(f"    sqrt2 = C + C^7 integer, (C+C^7)^2 = 2I? {np.allclose(S2@S2, 2*np.eye(4))}   => pi/4 ABSORBS into M=4I (ALGEBRAIC, finite).")
print(f"  MODULUS  1/sqrt(2 cosh pi t)  -- t-dependent, transcendental (next).")

# =============================================================================================
# (C) the transcendental residue: a function of the SPECTRAL variable t, NOT of N
# =============================================================================================
print("\n"+"="*92)
print("(C) THE TRANSCENDENTAL RESIDUE  (function of t = the archimedean place; the LIMIT, not a finite-N rate)")
print("="*92)
print(f"  {'t':>6} {'envelope 1/sqrt(2cosh pi t)':>28} {'non-normality e^{pi t}':>22}")
for t in (0.5, 1.0, 2.0, 5.0):
    env = float(1/mp.sqrt(2*mp.cosh(mp.pi*t)))
    nn  = float(mp.e**(mp.pi*t))
    print(f"  {t:>6} {env:>28.6e} {nn:>22.6e}")
print("  => exponential in t, NOT a function of N: this is what REMAINS after N->inf. e^{pi} is transcendental")
print("     (Gelfond 1934), in NO cyclotomic field Q(zeta_N). It is the archimedean envelope = the residue.")

print("\n"+"="*92)
print("VERDICT -- three objects, three number fields")
print("="*92)
print(f"""  ETF defect  -1/(N-1)        in  Q            (rational; -> 0^- at rate 1/N; frame kappa == 1)   |  ALGEBRAIC
  apex ceiling sqrt i = zeta_8 in  Q(zeta_8)     (degree 4; the pi/4=1/8 landmark; absorbs into M=4I)  |  SKELETON
  envelope e^{{pi t}}             TRANSCENDENTAL  (Gelfond; function of t, the LIMIT; in no Q(zeta_N))   |  RESIDUE

  So the convergence T4 hints at -- the simplex ETF blending into the orthonormal Cartesian frame
  (angle -> 90^+, defect -1/(N-1) -> 0, kappa == 1) -- is the finite ladder's ALGEBRAIC, perfectly-
  conditioned SKELETON. The apex edge rides on it, approaching the pi/4 = 1/8 ceiling = sqrt i = zeta_8,
  which is ABSORBABLE into the same M=4I metric (N4 Rem 4.3 <-> T4). But the apex->archimedean RESIDUAL
  -- the thing that equals RH -- is the TRANSCENDENTAL envelope e^{{pi t}} / 1/sqrt(2 cosh pi t), a function
  of the spectral variable t, the N->inf LIMIT, carried by NEITHER the ETF geometry nor any cyclotomic
  metric. The two convergences TOUCH at pi/4 (the absorbable algebraic landmark) but are different IN KIND:
  algebraic skeleton (resolved by the ladder) vs transcendental residue (the archimedean place, the wall).
  A real and deep rhyme; an identity it is not.""")
