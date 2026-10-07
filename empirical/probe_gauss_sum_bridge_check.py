"""
probe_gauss_sum_bridge_check.py

Leo's Phase-2 rebuttal: the asymmetric defect trace looks like 0 in the ADDITIVE basis, but the
Gauss-sum bridge (T8 Thm 4.1 / summary pt 5) converts additive -> MULTIPLICATIVE, where the
selection rule is chi_1 chi_2 = psi (not a_1+a_2 = c) and the anchor -> L(1/2,chi_3)^2 > 0. So the
asymmetry should be measured against EVEN/ODD DIRICHLET CHARACTERS, not additive reversal.

Fair test. We compute the MULTIPLICATIVE parity asymmetry of the defect directly. Using T8's own
Gauss-sum identity tau(psi,-a) = psi(-1) tau(psi,a), the even/odd-Dirichlet split of any function
f on units has the closed form (character orthogonality on units):
   A_mult := sum_{chi} chi(-1) |f^(chi)|^2  =  phi(N) * sum_{s in units} f(s) conj(f(-s)),
so NO character table is needed. Here f is the position-space image of the defect,
   f(s) = (1/sqrt N) sum_{c=1}^{N-1} psi_c omega^{c s}   (unitary inverse additive Fourier),
and psi is the rank-1 defect of G^(3) = I - |psi><psi| (Phase 1, confirmed). The multiplicative
parity (s -> -s on units) is genuinely a DIFFERENT sum than the additive reversal (c -> N-c on all
of Z/N), because it restricts to units -- so this is a real, independent check, not a relabeling.

We report, for N in {6,12,18,30,42} (3 | N so chi_3 lives mod N; N=12 is Leo's conductor anchor):
  - additive asymmetry      Re sum_c conj(psi_c) psi_{N-c}                  (the ~0 already found)
  - multiplicative asymmetry Re[ phi(N) sum_{units} f(s) conj(f(-s)) ]      (Leo's basis)
  - both raw and normalized by ||defect||, against L(1/2,chi_3)^2 = 0.231238.

numpy. No torch.
"""
import numpy as np
from math import gcd

w_of = lambda N: np.exp(2j*np.pi/N)
Z3   = np.exp(2j*np.pi/3)
L2   = 0.4808726238**2     # L(1/2,chi_3)^2 = 0.231238...

def twisted_HF(N, twist):
    w = w_of(N)
    W = np.zeros((N-1, N-1), dtype=complex)
    for ki, k in enumerate(range(1, N)):
        Rk = 1.0/np.sqrt(N*k*(k+1))
        for ci, c in enumerate(range(1, N)):
            z = twist*w**c
            s = sum(z**j for j in range(k)) - k*z**k
            W[ki, ci] = Rk*s
    return W

def defect(N):
    W = twisted_HF(N, Z3)
    G = W.conj().T @ W
    D = np.eye(N-1) - G
    ev, U = np.linalg.eigh(D)
    j = int(np.argmax(ev))
    return np.sqrt(max(ev[j], 0.0)) * U[:, j]    # psi_c, c = 1..N-1

print("="*92)
print("GAUSS-SUM BRIDGE CHECK: is the defect's parity asymmetry nonzero in the MULTIPLICATIVE basis?")
print("="*92)
print(f"  {'N':>4} {'phi(N)':>7} {'additive asym':>14} {'MULT asym (raw)':>16} "
      f"{'MULT asym/||.||':>16} {'L(1/2,chi3)^2':>14}")
for N in (6, 12, 18, 30, 42):
    psi = defect(N)                               # additive-character index c=1..N-1
    psi_full = np.zeros(N, complex); psi_full[1:] = psi
    # additive asymmetry: c -> N-c on all nontrivial additive chars
    add_asym = float(np.real(sum(np.conj(psi_full[c])*psi_full[(N-c) % N] for c in range(1, N))))
    # unitary inverse additive Fourier to position space
    w = w_of(N)
    f = np.array([sum(psi_full[c]*w**(c*s) for c in range(N)) for s in range(N)])/np.sqrt(N)
    units = [s for s in range(1, N) if gcd(s, N) == 1]
    phiN = len(units)
    # MULTIPLICATIVE parity asymmetry (even/odd Dirichlet split), closed form via orthogonality
    mult_raw = float(np.real(phiN*sum(f[s]*np.conj(f[(N-s) % N]) for s in units)))
    fnorm = float(np.sqrt(np.real(np.vdot(f, f))))
    mult_norm = mult_raw/(fnorm**2) if fnorm > 0 else 0.0
    print(f"  {N:>4} {phiN:>7} {add_asym:>14.3e} {mult_raw:>16.4f} {mult_norm:>16.4f} {L2:>14.6f}")

print(f"""
READING.
  - If 'MULT asym' is also ~0 or trends to 0: the Gauss-sum bridge does NOT rescue Phase 2 --
    the parity asymmetry is invariant because, by T8's own tau(psi,-a)=psi(-1)tau(psi,a), the
    bridge intertwines additive parity with multiplicative (even/odd-Dirichlet) parity; a
    parity-equivariant transform cannot manufacture chirality.
  - If 'MULT asym' is a robust nonzero value approaching {L2:.4f}: Phase 2's anchor survives in
    the multiplicative basis, and the audit's Phase-2 objection is withdrawn (Phase 3 still stands).

TWO STANDING POINTS regardless of the number above:
  (1) T8's OWN scope (summary pt 6, line 41): the finite truncation is a STRUCTURAL analog whose
      'arithmetic (L-function) content is carried by the GENUINE L(s,chi), NOT the finite
      truncation.' So even a nonzero finite asymmetry is not the value L(1/2,chi_3)^2; that value
      is a CONTINUUM (archimedean) limit. Supplying it to the finite trace is the finite->continuum
      leap = the wall, not a finite identity the bridge provides.
  (2) Phase 3 is untouched. Even granting a strictly positive anchor, a BULK trace does not lower-
      bound the EDGE ground-state split Delta(lambda); and the constant algebraic floor (Phase 4)
      contradicts Delta ~ exp(-4 pi e^L) -> 0. The bridge addresses Phase 2 only; the load-bearing
      gap is Phase 3.""")

print("="*92)
print("ACTUAL RESULT + VERDICT")
print("="*92)
print("""  CORRECTED (Leo was right about the basis):
    - additive-basis asymmetry = 0, but MULTIPLICATIVE-basis asymmetry is NONZERO and POSITIVE
      (odd Dirichlet characters dominate): +0.333, +0.667, +1.000, +1.067, +1.714 for N=6..42.
    - the Gauss-sum bridge restricts to units, so the parity operator there is genuinely different
      from additive reversal -- NOT a relabeling. The chirality anchor is real in this basis. The
      audit's 'Phase 2 anchor vanishes' objection is WITHDRAWN.

  CALIBRATION (what the numbers actually do):
    - the value GROWS with N (0.33 -> 1.71); it does NOT converge to the constant L(1/2,chi_3)^2 =
      0.2312. So the specific identification 'finite asym -> L(1/2,chi_3)^2' is not borne out at the
      finite level. What DOES hold is the weaker, Phase-3-relevant property: the anchor is bounded
      away from zero (indeed growing). T8's own scope (pt 6) attributes the exact L-value to the
      genuine L(s,chi), not the truncation -- consistent with 'bounded below, not = 0.2312.'

  PHASE 3 STILL THE WALL -- now REINFORCED, not weakened:
    - a NONZERO (even growing) BULK asymmetry still does not lower-bound the EDGE ground-state split
      Delta(lambda). Trace =/=> gap is unchanged by which basis the trace is taken in.
    - the contradiction is now SHARPER: the algebraic asymmetry GROWS without bound while
      Delta(lambda) ~ exp(-4 pi e^L) -> 0. A growing quantity is even more clearly NOT the vanishing
      ground split. Phase 2 being vindicated makes Tr_asym and Delta MORE obviously different objects.

  NET: Leo's Phase-2 correction is right and accepted; it does not rescue the proof, because the
  load-bearing step was always Phase 3 (bulk trace vs edge ground split = the archimedean/limit
  positivity = N7's single open step), and the growing anchor sharpens that gap rather than closing it.""")
