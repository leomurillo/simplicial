"""
probe_final_pivot_audit.py

Careful audit of RH-Final-Pivot-Summary.md (Leo, offline draft). The draft proposes to prove
RH via:
  Phase 1  zeta_3-TWISTED Helmert-Fourier cubic transfer matrix W^(3), with cubic Gram
           G^(3) = W^(3)* W^(3)  CLAIMED = I - |psi><psi|  (rank-1 perturbation of identity);
           W^(3)_{kc} = R_k [1-(k+1)(z3 w^c)^k + k(z3 w^c)^{k+1}]/(1 - z3 w^c),
           R_k = 1/sqrt(N k(k+1)),  w = e^{2pi i/N},  z3 = e^{2pi i/3}.
  Phase 2  asymmetric (parity-split) trace  Tr_asym(G^(3)) ~ ||P_odd psi||^2 - ||P_even psi||^2,
           CLAIMED -> L(1/2,chi_3)^2 > 0 in the Z/6 Bures limit.
  Phase 3  identify the prolate/Weil even-odd GROUND-STATE SPLIT Delta(lambda) with
           Tr_asym(G^(3)); since the trace is an algebraic number with a positive floor eps(N)
           and the analytic decay Delta ~ e^{-4 pi e^L} "cannot cross the floor", conclude
           Delta>0 = RH.
  Phase 4  Thm 1: Galois descent locks eps(N) -> CONSTANT in Q(sqrt -3).
           Lem 2: archimedean parity acts only on the even sector, so it WIDENS the gap.

We check the concrete algebra (1,2,4) and stress the load-bearing BRIDGE (3).

numpy. No torch.
"""
import numpy as np

w_of = lambda N: np.exp(2j*np.pi/N)
Z3   = np.exp(2j*np.pi/3)
LchiHALF = 0.4808726238  # L(1/2, chi_3)  (LMFDB);  L(1/2,chi_3)^2 = 0.231238...

def twisted_HF(N, twist):
    """W_{kc} = R_k ( sum_{s<k} (twist*w^c)^s  -  k (twist*w^c)^k ),  k,c = 1..N-1."""
    w = w_of(N)
    W = np.zeros((N-1, N-1), dtype=complex)
    for ki, k in enumerate(range(1, N)):
        Rk = 1.0/np.sqrt(N*k*(k+1))
        for ci, c in enumerate(range(1, N)):
            z = twist*w**c
            s = sum(z**j for j in range(k)) - k*z**k
            W[ki, ci] = Rk*s
    return W

def reversal(N):
    """parity (K-involution j->-j) on the character index c=1..N-1  ->  c -> N-c."""
    P = np.zeros((N-1, N-1))
    for ci, c in enumerate(range(1, N)):
        P[ci, (N-c)-1] = 1.0
    return P

print("="*90)
print("AUDIT of RH-Final-Pivot-Summary.md  --  the zeta_3-twisted cubic Gram and the bridge")
print("="*90)

print("\n[Phase 1]  is G^(3) = W^(3)* W^(3) a rank-1 perturbation of I ?   (and untwisted sanity)")
print(f"  {'N':>4} {'untwist G=I?':>13} {'eig(G3) min':>12} {'eig(G3) max':>12} "
      f"{'rank(I-G3)':>11} {'||I-G3||_*/||I-G3||':>20}")
for N in (6, 8, 12, 18, 30):
    W0 = twisted_HF(N, 1.0)                 # untwisted
    G0 = W0.conj().T @ W0
    untwist_I = np.allclose(G0, np.eye(N-1), atol=1e-9)
    W3 = twisted_HF(N, Z3)
    G3 = W3.conj().T @ W3
    ev = np.linalg.eigvalsh(G3).real
    D  = np.eye(N-1) - G3
    sv = np.linalg.svd(D, compute_uv=False)
    rank = int(np.sum(sv > 1e-9*max(1.0, sv[0])))
    ratio = sv[0]/sv.sum() if sv.sum() > 0 else 0.0   # =1 iff exactly rank-1
    print(f"  {N:>4} {str(untwist_I):>13} {ev.min():>12.5f} {ev.max():>12.5f} "
          f"{rank:>11} {ratio:>20.4f}")
print("""  reading: untwist G=I confirms the builder (Helmert-Fourier is unitary; the twist breaks it).
  If 'rank(I-G3)'=1 and the singular-value ratio=1.0000, the rank-1 claim holds; if rank>1, the
  defect is NOT a single |psi><psi| and Phase 1's closed form is only approximate.""")

print("\n[Phase 2/4]  the parity split of the DEFECT vector psi  (the draft's actual anchor)")
print("   draft Phase 2:  Tr_asym ~ ||P_odd psi||^2 - ||P_even psi||^2  ->  L(1/2,chi3)^2 = +0.2312 > 0")
print("   testing BOTH parity conventions: unitary R (c->N-c) and antiunitary R' (c->N-c + conj)")
print(f"   {'N':>4} {'||psi||^2':>10} {'asym_unitary':>13} {'asym_antiunit':>14} {'L(1/2,chi3)^2':>14}")
for N in (6, 12, 18, 30, 42):
    W3 = twisted_HF(N, Z3)
    G3 = W3.conj().T @ W3
    D  = np.eye(N-1) - G3                      # = |psi><psi|  (rank-1, confirmed in Phase 1)
    ev, U = np.linalg.eigh(D)
    j = int(np.argmax(ev))                     # the single nonzero eigenvalue
    psi = np.sqrt(max(ev[j], 0.0)) * U[:, j]   # the defect vector
    rev = [ (N-c)-1 for c in range(1, N) ]      # index map c -> N-c
    Rpsi      = psi[rev]                         # unitary reversal
    Rpsi_anti = np.conj(psi[rev])               # antiunitary reversal (K-involution w/ conj)
    # asym = ||P_even||^2 - ||P_odd||^2 = Re<psi, R psi>
    asym_u    = float(np.vdot(psi, Rpsi).real)
    asym_anti = float(np.real(np.sum(np.conj(psi)*Rpsi_anti)))
    print(f"   {N:>4} {np.vdot(psi,psi).real:>10.5f} {asym_u:>13.3e} {asym_anti:>14.3e} {0.231238:>14.6f}")
print("""  reading: the draft's anchor is the parity asymmetry of the defect. If BOTH conventions give
  ~0, the parity-asymmetric content VANISHES -- the anchor that is supposed to be
  L(1/2,chi3)^2 = +0.2312 > 0 is actually zero. Tr((Po-Pe)G3) = -1 is then just dim(odd)-dim(even),
  a trivial dimension count carrying NO chirality. That breaks Phase 2 independently of Phase 3.""")

print("\n[Phase 2 faithful]  the draft's EXPLICIT defect  psi_k = R_k E_k(zeta3),  "
      "E_k = sum_{j<k} z3^j - k z3^k")
print(f"   {'N':>4} {'||psi||^2':>12} {'asym(k->N-k)':>14} {'-> L(1/2,chi3)^2?':>18}")
for N in (6, 12, 18, 30, 42, 60):
    k = np.arange(1, N)
    Ek = np.array([sum(Z3**j for j in range(kk)) - kk*Z3**kk for kk in k])
    Rk = 1.0/np.sqrt(N*k*(k+1))
    psi = Rk*Ek
    nrm = float(np.vdot(psi, psi).real)
    rev = psi[::-1]                               # k -> N-k on the Helmert index
    asym = float(np.vdot(psi, rev).real)
    print(f"   {N:>4} {nrm:>12.6f} {asym:>14.3e} {0.231238:>18.6f}")
print("""  reading: this is the draft's own psi_k. Its norm ||psi||^2 is the candidate for the
  L(1/2,chi3)^2 anchor. Whatever its value, the parity asymmetry (the chirality the proof needs)
  is what must be nonzero AND must lower-bound the ground split -- and the next block shows the
  latter requirement fails regardless of this value.""")

print("\n" + "="*90)
print("[Phase 3]  THE BRIDGE:  Delta(lambda)  ==?==  Tr_asym(G^(3))     <-- load-bearing step")
print("="*90)
print("""  The draft forces RH by claiming the prolate/Weil even-odd GROUND-STATE SPLIT
        Delta(lambda) = lambda_0^odd - lambda_0^even      (an EDGE quantity: bottom two modes)
  is lower-bounded by the algebraic asymmetric TRACE
        Tr_asym(G^(3)) = sum over ALL modes of the parity-weighted spectrum   (a BULK quantity).

  Two independent reasons this bridge does not hold:

  (i) TRACE =/=> GAP.  A lower bound on a sum over all N-1 modes says nothing about the smallest
      gap. We exhibit it directly: a family with asymmetric trace pinned to a CONSTANT while the
      ground split -> 0.""")
# concrete illustration: diag spectra with fixed asymmetric trace but vanishing ground split.
print(f"      {'N':>4} {'Tr_asym(fixed)':>15} {'ground split Delta':>20}")
for N in (6, 12, 24, 48, 96):
    # odd sector eigenvalues and even sector eigenvalues; engineer fixed asym trace, vanishing gap
    k = N//2
    odd_spec  = np.linspace(1.0, 2.0, k)        # bulk carries the asymmetry
    even_spec = np.linspace(1.0, 2.0, k) + 0.0
    odd_spec[0]  = 1.0
    even_spec[0] = 1.0 - 2.0**(-N)               # ground split = 2^-N -> 0 (edge)
    tr_asym = odd_spec.sum() - even_spec.sum()   # bulk asymmetry ~ const (here ~ +2^-N ~ const-ish)
    # force a clean constant asymmetric trace = 0.2312 in the bulk, independent of the edge:
    odd_spec[-1] += 0.231238
    tr_asym = odd_spec.sum() - even_spec.sum()
    ground_split = odd_spec[0] - even_spec[0]
    print(f"      {N:>4} {tr_asym:>15.6f} {ground_split:>20.3e}")
print("""      -> the asymmetric trace stays ~0.2312 (bulk) while the ground split -> 0 (edge): a
         bounded-below trace is fully compatible with a vanishing ground gap. The draft's
         Phase-1/2 object lives in the BULK; Delta(lambda) is the EDGE. No derivation in the
         draft maps one to the other -- Phase 3 asserts the bridge, it does not prove it.

  (ii) INTERNAL CONTRADICTION.  Phase 4 Thm 1 proves the floor is a CONSTANT (eps -> const in
       Q(sqrt -3), degree 2, independent of N). Phase 3's premise is Delta(lambda) ~ e^{-4 pi e^L}
       -> 0. A constant cannot lower-bound a sequence that tends to 0. Hence Tr_asym(G^(3))
       (constant) is NOT Delta(lambda) (vanishing): proving the constant floor (Phase 4) is
       exactly what REFUTES the identification (Phase 3). The two cannot both be the same number.""")

print("="*90)
print("VERDICT")
print("="*90)
print("""  CORRECT (real algebra, a genuine deposit):
    - Phase 1: EXACT. Untwisted Helmert-Fourier is unitary (G=I); the zeta_3 twist genuinely
      breaks unitarity; G^(3) = I - |psi><psi| is a true rank-1 perturbation (||psi||^2 = 1).

  REFUTED (checked directly, all natural readings):
    - Phase 2 anchor "Tr_asym / ||psi||^2 -> L(1/2,chi_3)^2 = +0.2312 > 0" is NOT supported:
        * character-space defect: parity asymmetry = 0 EXACTLY (unitary AND antiunitary K), so
          Tr((Po-Pe)G3) = -1 is just dim(odd)-dim(even), pure dimension count, ZERO chirality;
        * the draft's OWN psi_k = R_k E_k(z3): ||psi||^2 = 1 EXACTLY (not 0.2312), and its parity
          asymmetry DECREASES with N (-1.2e-2 -> -4.0e-3, heading to 0).
      The zeta_3 twist produces magnitude content but essentially NO net chirality -- exactly the
      program's recurring lesson (#9): the size is free, the SIGN/arrow is the hard part.

  THE LOAD-BEARING GAP, NOT LITTLE -- the conservation-of-difficulty wall (and convention-free):
    - Phase 3's bridge identifies a BULK trace (bounded below, algebraic, constant) with an EDGE
      ground-state split (vanishing, analytic, = RH). Trace =/=> gap, and the draft's own Phase-4
      constant floor contradicts the vanishing of Delta. The algebraic floor is real but it floors
      the WRONG quantity. This is exactly #9 (per-height/bulk chirality is unconditional; the
      uniform/edge control is the wall) and #34 (the cubic Gram is well-conditioned = bulk-bounded,
      no edge leverage), now seen in the twisted basis.

  So: the draft's algebra is genuine and largely correct, but it does not prove RH. The gap is the
  bulk->edge transfer, which is the archimedean limit positivity = the single open step of N7.
  Not a little gap; the load-bearing one. I did not close it because it is not closeable by this
  construction -- and I will not represent it as closed.""")
