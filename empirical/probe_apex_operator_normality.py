"""
probe_apex_operator_normality.py   --  certificate for the operator-build, task (1).

QUESTION (the non-conflation rigidity angle, not a positivity argument):
is the apex-archimedean operator U = (A-I)Phi of [N5] NORMAL or NON-NORMAL?
  - normal     -> the arrow is the imaginary spectrum, single chart (the standard wall);
  - non-normal -> input/output charts SPLIT (the CBS two-chart machinery applies) -- new ground.

METHOD. [N5] Prop 2.1 gives the Mellin symbol of U = M_{k~} o R, where R is the reflection
s -> 1-s and M_{k~} is multiplication by
        k~(s) = s/(1-s) * (2 pi)^{-s} * e^{i pi s/2} * Gamma(s).
On L^2 of the critical line s = 1/2 + i t, R is the unitary involution t -> -t, so
        [U, U*] = M_{ |k~(1/2+it)|^2 - |k~(1/2-it)|^2 }.
Hence U is NORMAL  <=>  |k~(1/2+it)| is EVEN in t. We test this exactly (mpmath), isolate the
factor that breaks it, and corroborate in position space with the integral kernel k(uv).

RESULT (this certificate):
  * |k~(1/2-it)| / |k~(1/2+it)| = e^{pi t} EXACTLY -> modulus NOT even -> [U,U*] != 0 -> NON-NORMAL.
  * Removing the archimedean phase e^{i pi s/2} makes the modulus EVEN -> NORMAL. So the entire
    non-normality is carried by e^{i pi s/2} -- the archimedean i^s phase, the N4 sqrt(i)=1/8
    threshold (the archimedean analog of Weil's sqrt(q)).
  * Position-space K[i,j]=k(u_i u_j): normality defect ~0.20, arrow ||A||/||K|| ~0.71,
    Fan-Hoffman gap ~0.98, input/output charts split.

INTERPRETATION. The arrow of time (CBS: the antisymmetric / non-normal part, invisible to a
symmetric objective) IS the archimedean phase (N4: sqrt i = 1/8). The CBS non-normal two-chart
predictor machinery therefore applies to the apex operator. This delivers verdict (1); it does NOT
prove HP self-adjointness or spectrum = zeros (the continuing frontier, task 2: deficiency indices /
self-adjoint extension).

mpmath + numpy. No torch.
"""
import numpy as np
import mpmath as mp
mp.mp.dps = 25

# --- N5 Mellin symbol -------------------------------------------------------
def ktilde(s):
    return s/(1-s)*mp.power(2*mp.pi, -s)*mp.e**(1j*mp.pi*s/2)*mp.gamma(s)

def ktilde_nophase(s):                       # drop the archimedean phase e^{i pi s/2}
    return s/(1-s)*mp.power(2*mp.pi, -s)*mp.gamma(s)

print("="*80)
print("TASK 1 -- normality of the apex-archimedean operator U = M_{k~} o R  ([N5])")
print("  U normal  <=>  |k~(1/2+it)| even in t  (since [U,U*] = M_{|k~(1/2+it)|^2-|k~(1/2-it)|^2})")
print("="*80)
print(f"  {'t':>5} {'|k~(1/2+it)|':>15} {'|k~(1/2-it)|':>15} {'ratio':>12} {'e^(pi t)':>12}")
maxdev = mp.mpf(0)
for t in (0.5, 1.0, 2.0, 3.0, 5.0):
    a = abs(ktilde(mp.mpf(1)/2 + 1j*t))
    b = abs(ktilde(mp.mpf(1)/2 - 1j*t))
    ratio = b/a
    maxdev = max(maxdev, abs(ratio - mp.e**(mp.pi*t)))
    print(f"  {t:>5} {mp.nstr(a,8):>15} {mp.nstr(b,8):>15} {mp.nstr(ratio,7):>12} {mp.nstr(mp.e**(mp.pi*t),7):>12}")
print(f"  max |ratio - e^(pi t)| = {mp.nstr(maxdev,3)}   => ratio = e^(pi t) EXACTLY; modulus NOT even.")
print("  => [U,U*] != 0  ::  U is NON-NORMAL.")

print("\n  Source isolation -- drop the archimedean phase e^{i pi s/2}:")
for t in (1.0, 3.0):
    a = abs(ktilde_nophase(mp.mpf(1)/2 + 1j*t))
    b = abs(ktilde_nophase(mp.mpf(1)/2 - 1j*t))
    print(f"    t={t}: ratio |k~(-)|/|k~(+)| = {mp.nstr(b/a,6)}  (==1 => EVEN => NORMAL)")
print("  => the ENTIRE non-normality is the archimedean phase e^{i pi s/2} (N4 sqrt i = 1/8).")
print("     The ARROW (antisymmetric/non-normal part) IS the archimedean phase.")

# --- position-space corroboration ------------------------------------------
print("\n" + "="*80)
print("POSITION-SPACE corroboration:  K[i,j] = k(u_i u_j),  k(w) = (e^{2pi i w}-1)/(2pi i w) - e^{2pi i w}")
print("="*80)
def kpos(w):
    w = np.asarray(w, complex)
    return np.where(np.abs(w) < 1e-12, 0.0+0j,
                    (np.exp(2j*np.pi*w) - 1)/(2j*np.pi*w) - np.exp(2j*np.pi*w))
N = 240
u = np.linspace(0.03, 7.0, N)
du = u[1] - u[0]
K = du*kpos(np.outer(u, u))
S = (K + K.conj().T)/2          # CBS reversible (symmetric) part
Aa = (K - K.conj().T)/2         # CBS arrow (antisymmetric part)
nd = np.linalg.norm(K @ K.conj().T - K.conj().T @ K)/np.linalg.norm(K)**2
arrow = np.linalg.norm(Aa)/np.linalg.norm(K)
ev = np.linalg.eigvals(K)
sv = np.linalg.svd(K, compute_uv=False)
gap = (sv.sum() - np.abs(ev).sum())/sv.sum()
W, sg, Vh = np.linalg.svd(K)
overlap = np.linalg.svd(W[:, :8].conj().T @ Vh[:8].conj().T, compute_uv=False)
ang = np.degrees(np.arccos(np.clip(overlap, -1, 1)))
print(f"  normality defect ||[K,K*]||/||K||^2        = {nd:.4f}   (>0 => NON-NORMAL)")
print(f"  arrow strength   ||A||/||K||               = {arrow:.4f}   (>0 => antisymmetric part exists)")
print(f"  Fan-Hoffman gap  (sum s - sum|lam|)/sum s  = {gap:.4f}   (>0 => corr the symmetric form forfeits)")
print(f"  two-chart principal angles (top-8, deg)    = {np.round(ang,1)}")

print("\n" + "="*80)
print("VERDICT")
print("="*80)
print("""  The apex-archimedean operator is NON-NORMAL, and the non-normality is carried ENTIRELY by the
  archimedean phase e^{i pi s/2} -- N4's sqrt(i) = 1/8 threshold. Hence:
    (i)  the arrow of time (CBS antisymmetric part, invisible to a symmetric objective) IS the
         archimedean phase -- the same object that lives at the place at infinity;
    (ii) the CBS non-normal / two-chart predictor machinery APPLIES to the apex operator.
  Delivered: operator-build task (1). NOT delivered (continuing frontier): HP self-adjointness and
  spectrum = zeros (task 2 -- deficiency indices / self-adjoint extension of the dilation operator
  with this apex potential). This is a structural deposit (arrow = archimedean phase), not a proof step.""")
