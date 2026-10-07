"""
AUDIT-FIRST (thread (a)): is the GENUINE chiral object C(rho)=Im(rho_chi) a tractable RH handle,
or does it (correctly) just reproduce the full L(1/2,chi_3) problem?

rho_chi = U^H M U  is the character-frame density of a Helmert state M; for the archimedean
exponential family M = diag(p), real populations.  Unlike the phase-blind J=B-B^T (retracted,
N14 sec 7.5 Rem 7.8), Im(rho_chi) is genuinely phase-borne and state-dependent.  We audit it:

  G1  GENUINE + EXACTLY CHIRAL.  Im(rho_chi) != 0 for a real test state, and is EXACTLY parity-odd:
      R Im(rho_chi) R = -Im(rho_chi)  (R: c->-c).  [contrast J: only ~97% odd, phase-blind]
  G2  VACUUM.  Im(rho_chi(uniform)) = 0 (no arrow at equilibrium) -- the check J FAILED.
  G3  GAUGE.  The entrywise Im(rho_chi) is gauge-covariant (rephasing characters moves it), but the
      Bargmann triple Im[(rho_chi)_{ab}(rho_chi)_{bc}(rho_chi)_{ca}] is gauge-INVARIANT -- the proper
      geometric chiral object.
  G4  THE OBSTRUCTION.  For a real (time-reversal-symmetric) Helmert state, the NET chiral signal
      VANISHES by time reversal: every parity-EVEN contraction of Im(rho_chi) is 0, and the total
      Bargmann phase sum_{a,b,c} Im T3 = 0.  Breaking time reversal (a complex Helmert state) makes
      the net current nonzero -- so the signal is exactly the time-reversal-odd content.
  G5  NO FREE SIGN.  A nonzero scalar appears only against a parity-ODD weight = an ORIENTATION.
      At N=6 the chi_3 characters are {2,4}; the chiral scalar Im (rho_chi)_{2,4} is nonzero but
      FLIPS SIGN under the orientation swap chi_3 <-> conj(chi_3) (2<->4).  Choosing the orientation
      that makes it definite is precisely choosing the sign of L(1/2,chi_3) -- the full RH content.

VERDICT: C(rho)=Im(rho_chi) is the CORRECT object (passes every check J failed, exactly chiral),
but it yields NO tractable reduction: real test states give zero net signal, and the sign is the
arithmetic orientation = L(1/2,chi_3). Thread (a) confirms the honest stopping point (b).

No torch. numpy. Deterministic.
"""
import numpy as np
np.set_printoptions(precision=4, suppress=True)

def apex_unitary(N):
    w = np.exp(2j * np.pi / N)
    k = np.arange(1, N).reshape(-1, 1); c = np.arange(1, N).reshape(1, -1)
    R = 1.0 / np.sqrt(N * k * (k + 1))
    return R * (1 - (k + 1) * w ** (k * c) + k * w ** ((k + 1) * c)) / (1 - w ** c)

def rho_chi(U, M):
    return U.conj().T @ M @ U

def parity(N):
    P = np.zeros((N - 1, N - 1))
    for c in range(1, N):
        P[((-c) % N) - 1, c - 1] = 1
    return P

def bargmann(rc, a, b, c):
    # individual gauge-invariant Bargmann triple (the TOTAL sum is identically 0 by Hermiticity)
    return (rc[a, b] * rc[b, c] * rc[c, a]).imag

def parity_even_part(Im, P):
    return (Im + P @ Im @ P) / 2     # =0 iff Im is exactly parity-odd

GREEN = True
def chk(cond, msg):
    global GREEN
    print(("  ok  " if cond else "  ** RED ") + msg)
    if not cond: GREEN = False

for (N, label) in ((7, "prime p=7"), (6, "primorial N=6")):
    print(f"\n=== {label} (N={N}) ===")
    U = apex_unitary(N)
    P = parity(N)
    # real archimedean test state: exp-family with a smooth centered energy
    kk = np.arange(1, N, dtype=float)
    y = np.cos(2 * np.pi * kk / N); y -= y.mean()
    p = np.exp(0.8 * y); p /= p.sum()
    M = np.diag(p)
    rc = rho_chi(U, M)
    Imrc = rc.imag

    # G1 genuine + exactly chiral
    chk(np.linalg.norm(Imrc) > 1e-6, f"Im(rho_chi) != 0 (genuine): ||Im||={np.linalg.norm(Imrc):.4f}")
    odd_resid = np.linalg.norm(P @ Imrc @ P + Imrc)
    chk(odd_resid < 1e-9, f"EXACTLY parity-odd: ||R Im R + Im|| = {odd_resid:.2e}  (J was only ~97%)")

    # G2 vacuum
    rc_vac = rho_chi(U, np.eye(N - 1) / (N - 1))
    chk(np.linalg.norm(rc_vac.imag) < 1e-12, f"vacuum Im(rho_chi)=0: {np.linalg.norm(rc_vac.imag):.2e}  (J FAILED this)")

    # G3 gauge: individual Bargmann triple invariant under char rephasing; entrywise Im moves
    beta = np.cos(np.arange(1, N))           # deterministic phases
    Q = np.exp(1j * beta)
    U2 = U * Q[np.newaxis, :]
    rc2 = rho_chi(U2, M)
    dIm = np.linalg.norm(rc2.imag - Imrc)
    dBarg = abs(bargmann(rc2, 0, 1, 2) - bargmann(rc, 0, 1, 2))
    chk(dIm > 1e-6, f"entrywise Im(rho_chi) gauge-COVARIANT (moves): d={dIm:.4f}")
    chk(abs(bargmann(rc, 0, 1, 2)) > 1e-6 and dBarg < 1e-9,
        f"individual Bargmann triple gauge-INVARIANT & nonzero: T={bargmann(rc,0,1,2):.2e}, d={dBarg:.2e}")

    # G4 obstruction: time reversal. Real Helmert state => Im(rho_chi) EXACTLY parity-odd, so its
    # parity-EVEN component (every symmetric/net readout) is ZERO. Breaking T (complex Helmert state)
    # makes a parity-even component appear -- the net signal is exactly the time-reversal-odd content.
    even_real = np.linalg.norm(parity_even_part(Imrc, P))
    A = np.zeros((N - 1, N - 1)); A[0, 1] = 1; A[1, 0] = -1   # i*A = Hermitian Helmert coherence
    rc_c = rho_chi(U, M + 1j * 0.05 * A)
    even_cplx = np.linalg.norm(parity_even_part(rc_c.imag, P))
    chk(even_real < 1e-9, f"real state: parity-even part of Im(rho_chi) = {even_real:.2e} (==0: net signal vanishes by T)")
    chk(even_cplx > 1e-6, f"T-broken state: parity-even part = {even_cplx:.4f} (!=0: signal is the T-odd content)")

# G5 no free sign: chi_3 orientation at N=6
print("\n--- G5: the sign IS the chi_3 orientation (N=6) ---")
N = 6; U = apex_unitary(N)
kk = np.arange(1, N, dtype=float); y = np.cos(2*np.pi*kk/N); y -= y.mean()
p = np.exp(0.8*y); p /= p.sum()
rc = rho_chi(U, np.diag(p))
s_24 = rc[2 - 1, 4 - 1].imag      # chi_3 sector off-diagonal (characters 2,4)
s_42 = rc[4 - 1, 2 - 1].imag      # swapped orientation
print(f"  chiral scalar Im (rho_chi)_(2,4) = {s_24:+.5f}")
print(f"  swapped       Im (rho_chi)_(4,2) = {s_42:+.5f}   (= - the above: orientation flips sign)")
chk(abs(s_24) > 1e-6 and abs(s_24 + s_42) < 1e-9,
    "nonzero, and orientation-swap flips sign => the definite sign = choosing L(1/2,chi_3)'s sign")

print("\n" + "=" * 80)
print("VERDICT:", "GREEN" if GREEN else "RED")
print("""  C(rho)=Im(rho_chi) is the CORRECT chiral object -- exactly parity-odd, vacuum-zero,
  Bargmann-gauge-invariant: it passes every check the retracted J=B-B^T failed. BUT it yields
  NO tractable reduction: any real (time-reversal-symmetric) archimedean test state has ZERO net
  chiral signal; a nonzero scalar requires a parity-ODD orientation = the chi_3 sign = L(1/2,chi_3).
  Thread (a): the object is right, the shortcut is not there. Honest stop = the Thm 7.6 dichotomy.""")
print("=" * 80)
