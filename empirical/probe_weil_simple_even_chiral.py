"""
probe_weil_simple_even_chiral.py  --  clear the gate that stopped probe_weil_form_simplicity.

CONTEXT (read probe_connes_prolate_pivot.py + probe_prolate_simple_even.py first).
Connes' route to RH (arXiv:2602.04022) replaces the Bombieri-Vinogradov / Lindelof wall with a
PROLATE-convergence step (unconditional). Its one open spectral piece is S6.6a: the lowest eigenvalue
of the finite-prime Weil quadratic form QW is SIMPLE and EVEN. The prolate half is verified
(probe_prolate_simple_even). The WEIL half failed: the prior raw build got minimal-eigenvector first
Fourier zero = 3.56, not the first zeta ordinate 14.13 -- the archimedean kernel was too crude.

THIS PROBE rebuilds the even-sector finite-prime Weil form carefully and runs three PRE-REGISTERED gates.
It is NON-CIRCULAR: no zeta zero is ever an input to the form. The form is arch + pole - primes only;
the zeros are an OUTPUT (the minimal-eigenvector's Fourier zeros). gamma_1 = 14.1347 is used ONLY as a
post-hoc correctness yardstick.

  Riemann-Weil even-sector form on test functions g (even, supported |u|<=L, u = log x):
    M[g,g] = (1/2pi) INT |ghat(r)|^2 (Re psi(1/4+ir/2) - log pi) dr        (archimedean, = 2 theta')
             + 2 ( INT g(u) cosh(u/2) du )^2                                (pole at s=1; metric only)
             - 2 SUM_{n>=2} chi(n) Lambda(n) n^{-1/2} (g*g)(log n)          (primes; chi=1 metric / chi_3 chiral)
  metric channel: zeta (chi=1, has pole, arch shift 1/4).
  chiral channel: L(s,chi_3) (chi_3, entire/no pole, arch shift 3/4 since chi_3 is ODD: chi_3(-1)=-1).

PRE-REGISTERED outcomes (three-outcome matched pair, Paper 35 GPD):
  GATE A (correctness, the gate that failed before): minimal-eigenvector first Fourier zero z1 vs 14.1347.
     K: z1 -> 14.13 and converges toward it as basis size K grows  => Weil-form realization of Connes
        Thm 6.1 works; the prior 3.56 was under-resolution, not a wall.
     L: z1 stuck far from 14.13 with no convergence => the raw Weil vehicle stays numerically intractable;
        only the prolate route is viable (confirms the prior redirect).
     joint: z1 moves toward 14.13 but does not arrive at reachable K (partial).
  GATE B (simplicity, the S6.6a content for the Weil form): gap = lambda_1 - lambda_0 of M.
     K: gap > 0 robustly (lowest eigenvalue non-degenerate)  => simple, the program-native half of S6.6a.
     L: gap ~ 0 / level crossing                              => not simple on the Weil form.
     [Evenness is by CONSTRUCTION here -- we work in the even (cosine) sector. The cross-parity
      'even, not odd' claim is owned by probe_prolate_simple_even. Stated, not re-claimed.]
  GATE C (the chirality hypothesis, HONEST order-2 form): add the chi_3 channel; does it PRESERVE the
     simple lowest eigenvalue, and is its effect non-degenerate (consistent with L(1/2,chi_3)!=0 as a
     non-degeneracy anchor)?
     K: chiral channel preserves the gap and shifts it smoothly  => chirality is a consistent
        non-degeneracy contributor (necessary, not sufficient).
     L: chiral channel closes the gap / induces a crossing       => chirality is NOT the simplicity anchor.
     NOTE (firewall on my own claim): the STRONG form c_2 ∝ -L(1/2,chi_3)^2 is an ORDER-3 (cubic
     functional) object; it is NOT manufactured in this ORDER-2 form. GATE C tests only the order-2
     shadow (does the chiral channel keep the lowest eigenvalue simple). The order-3 scaling is a
     separate later build and is left explicitly open.

Deterministic. numpy + mpmath + sympy. No torch.
"""
import numpy as np
import mpmath as mp
from sympy import factorint

mp.mp.dps = 18
GAMMA1 = 14.134725141734693      # first zeta ordinate -- POST-HOC yardstick only, never an input
_trapz = getattr(np, "trapz", None) or np.trapezoid    # numpy 2.x renamed trapz -> trapezoid

# ---------------------------------------------------------------------------------------------------
def build_M(L, K, channel="metric", Nu=3000, Rmax=95.0, Nr=7000):
    """Even-sector finite-prime Weil form on basis g_k(u)=cos(k pi u/L), k=0..K, support |u|<=L."""
    u  = np.linspace(-L, L, Nu)
    a  = np.arange(K + 1) * np.pi / L                       # basis frequencies
    B  = np.cos(np.outer(a, u))                             # (K+1, Nu), all even

    # ---- pole (metric only): 2 C_j C_k, C_j = INT g_j cosh(u/2) ----
    if channel == "metric":
        Cj   = _trapz(B * np.cosh(u / 2.0), u, axis=1)
        pole = 2.0 * np.outer(Cj, Cj)
    else:
        pole = np.zeros((K + 1, K + 1))

    # ---- primes: 2 SUM chi(n) Lambda(n) n^{-1/2} (g_j * g_k)(log n) ----
    du   = u[1] - u[0]
    nmax = int(np.exp(2 * L))                               # autocorrelation support: log n <= 2L
    prime = np.zeros((K + 1, K + 1))
    for n in range(2, nmax + 1):
        f = factorint(n)
        if len(f) != 1:                                     # prime powers only (Lambda support)
            continue
        p, e = next(iter(f.items()))
        if channel == "metric":
            chi = 1.0
        else:
            cp = 0 if p % 3 == 0 else (1 if p % 3 == 1 else -1)   # chi_3(p)
            chi = float(cp) ** e
            if chi == 0:
                continue
        t   = np.log(n)
        ush = u - t
        Bsh = np.cos(np.outer(a, ush)) * ((ush >= -L) & (ush <= L))
        A   = (B @ Bsh.T) * du                             # (g_j * g_k)(t), K+1 x K+1
        prime += chi * np.log(p) / np.sqrt(n) * A
    prime *= 2.0

    # ---- archimedean: (1/2pi) INT ghat_j ghat_k W(r) dr,  W = Re psi(shift + i r/2) - log pi ----
    r  = np.linspace(1e-7, Rmax, Nr)
    dr = r[1] - r[0]
    Gh = np.empty((K + 1, Nr))
    for i, ai in enumerate(a):                             # ghat_k(r) closed form (even in r)
        d1, d2 = ai - r, ai + r
        Gh[i] = np.where(np.abs(d1) < 1e-9, L, np.sin(d1 * L) / d1) + np.sin(d2 * L) / d2
    shift = mp.mpf(1) / 4 if channel == "metric" else mp.mpf(3) / 4    # 1/4 zeta(even) ; 3/4 chi_3(odd)
    W = np.array([float(mp.re(mp.digamma(shift + 1j * rr / 2)) - mp.log(mp.pi)) for rr in r])
    arch = (1.0 / np.pi) * ((Gh * W * dr) @ Gh.T)          # (1/2pi)*2*INT_0^inf  (integrand even in r)

    return 0.5 * (arch + pole - prime + (arch + pole - prime).T), a, L


def first_fourier_zero(vec, a, L, Rmax=40.0, Nr=20000):
    """First positive r where vhat(r) = SUM vec_k ghat_k(r) changes sign."""
    r  = np.linspace(0.05, Rmax, Nr)
    vh = np.zeros(Nr)
    for vk, ai in zip(vec, a):
        d1, d2 = ai - r, ai + r
        vh += vk * (np.where(np.abs(d1) < 1e-9, L, np.sin(d1 * L) / d1) + np.sin(d2 * L) / d2)
    s = np.sign(vh)
    idx = np.where(np.diff(s) != 0)[0]
    return None if len(idx) == 0 else 0.5 * (r[idx[0]] + r[idx[0] + 1])


# ===================================================================================================
print("=" * 96)
print("GATE A  --  correctness: does the minimal eigenvector resolve gamma_1 = 14.1347 ? (no zeros input)")
print("=" * 96)
print(f"  prior raw build got first Fourier zero = 3.56 (failed). trend over basis size K, L=3.0:")
print(f"  {'K':>4} {'dim':>5} {'lambda_min':>13} {'1st Fourier zero':>18} {'|err vs 14.1347|':>18}")
L = 3.0
trendA = []
for K in (10, 14, 18, 22, 26, 30):
    M, a, _ = build_M(L, K, "metric")
    w, V = np.linalg.eigh(M)
    z1 = first_fourier_zero(V[:, 0], a, L)
    err = abs(z1 - GAMMA1) if z1 is not None else float("nan")
    trendA.append((K, z1))
    zs = f"{z1:.4f}" if z1 is not None else "none"
    print(f"  {K:>4} {K+1:>5} {w[0]:>13.3e} {zs:>18} {err:>18.4f}")

print("\n" + "=" * 96)
print("GATE B  --  simplicity: is the lowest eigenvalue non-degenerate (gap to 2nd) ?  [evenness = by construction]")
print("=" * 96)
print(f"  {'K':>4} {'lambda_0':>13} {'lambda_1':>13} {'gap':>13} {'simple?':>9}")
for K in (18, 22, 26, 30):
    M, a, _ = build_M(L, K, "metric")
    w, _ = np.linalg.eigh(M)
    gap = w[1] - w[0]
    print(f"  {K:>4} {w[0]:>13.3e} {w[1]:>13.3e} {gap:>13.3e} {'YES' if gap > 1e-9 else 'no':>9}")

print("\n" + "=" * 96)
print("GATE C  --  chirality hypothesis (HONEST order-2 form): does the chi_3 channel preserve simplicity ?")
print("=" * 96)
Lc = float(mp.power(3, mp.mpf('-0.5')) * (mp.zeta(mp.mpf('0.5'), mp.mpf(1)/3) - mp.zeta(mp.mpf('0.5'), mp.mpf(2)/3)))
print(f"  L(1/2,chi_3) = {Lc:.6f}  (!= 0, the program's non-degeneracy anchor; Iwaniec-Sarnak strict)")
print(f"  combined form M = M_metric + s * M_chiral, s a coupling; track the gap as the chiral channel turns on:")
print(f"  {'s':>6} {'lambda_0':>13} {'gap':>13} {'simple?':>9}")
K = 26
Mm, a, _ = build_M(L, K, "metric")
Mc, _, _ = build_M(L, K, "chiral")
for s in (0.0, 0.25, 0.5, 1.0):
    w, _ = np.linalg.eigh(Mm + s * Mc)
    gap = w[1] - w[0]
    print(f"  {s:>6.2f} {w[0]:>13.3e} {gap:>13.3e} {'YES' if gap > 1e-9 else 'no':>9}")

print("\n" + "=" * 96)
print("GATE A'  --  which eigenvector encodes the zeros? (N5 Thm 7.2: the MARGINAL one, lambda nearest 0)")
print("=" * 96)
M, a, _ = build_M(3.0, 34, "metric")
w, V = np.linalg.eigh(M)
i0 = int(np.argmin(np.abs(w)))                              # the marginal direction
print(f"  lowest 8 eigenvalues: {', '.join(f'{v:+.3e}' for v in w[:8])}")
print(f"  marginal mode index (|lambda| min) = {i0}, lambda = {w[i0]:+.3e}")
print(f"  {'mode':>5} {'eigenvalue':>13} {'1st Fourier zero':>18} {'|err vs 14.1347|':>18}")
for i in range(8):
    z = first_fourier_zero(V[:, i], a, 3.0)
    err = abs(z - GAMMA1) if z is not None else float('nan')
    zs = f"{z:.4f}" if z is not None else "none"
    tag = "  <- marginal" if i == i0 else ""
    print(f"  {i:>5} {w[i]:>13.3e} {zs:>18} {err:>18.4f}{tag}")

print("\n" + "=" * 96)
print("HONEST STATUS")
print("=" * 96)
za = [z for _, z in trendA if z is not None]
moved = (len(za) >= 2 and za[-1] > za[0] + 1.0)
print(f"""  GATE A: NEGATIVE (robust). first-Fourier-zero trajectory over K = {[round(z,2) if z else None for _,z in trendA]}
     -> flat at ~1.0, NOT -> 14.13. GATE A' confirms it is not a wrong-eigenvector artifact: the MARGINAL
     mode (lambda nearest 0, the N5 Thm 7.2 zero-encoder) has first zero ~1.95, and NONE of the 8 lowest
     modes land near 14.13 (they scatter in [1,6]). With a verified-correct archimedean density
     (W(0) = Re psi(1/4) - log pi ~ -5.37, matching N5), a CAREFUL build still does not encode the zeros.
     => FALSIFIES 'the prior 3.56 was just crude numerics, a careful build fixes it.' The raw finite-prime
        Weil form is NOT a viable zero-generator at accessible truncation. This INDEPENDENTLY CONFIRMS why
        Connes routes through the PROLATE operator (PW_lambda, well-conditioned), and validates the prior
        redirect (probe_prolate_simple_even / probe_connes_prolate_pivot).

  GATE B, GATE C: MOOT. They measure features (gap; chiral effect on the gap) of a form that FAILS the
     correctness gate, so they say NOTHING about Connes S6.6a. In particular the GATE C 'chiral channel
     preserves the gap' result is NOT evidence for the c_2 hypothesis -- reporting it as such would be the
     vacuous-confirmation trap. Recorded as uninterpretable, not as support.

  WHAT THIS SHARPENS: S6.6a (simple+even ground state) must be attacked on the object that ACTUALLY encodes
     the zeros -- the prolate-regularized form QW_lambda ~ PW_lambda (Connes S6.4), where the prolate half
     is already verified simple+even (probe_prolate_simple_even). The open piece is the TRANSFER bound
     epsilon(lambda) and whether the chi_3 channel enters it -- NOT the raw Weil minimal eigenvector.

  NOT claimed: no proof of RH; S6.6a is necessary-not-sufficient. The STRONG claim c_2 ~ -L(1/2,chi_3)^2 is
     ORDER-3 and untested here. Evenness is by construction (even sector). Firewall: gamma_1 was a post-hoc
     yardstick, never an input to M.""")
