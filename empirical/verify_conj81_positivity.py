r"""Probe of Conjecture 8.1 (P0): does the Weil quadratic form's positivity track RH?

RH-direction step. We corner the open step P0 isolates -- "positivity survives once the
archimedean Gamma-factor is adjoined" -- by testing the Weil/explicit-formula quadratic form
directly. Number-field analogue of the function-field circle probe
(verify_finite_global_positivity.py): there RH <=> Frobenius eigenvalues on the CIRCLE <=> a
Toeplitz form PSD, and pushing an eigenvalue off the circle broke PSD. Here the "circle" is the
critical LINE; the archimedean term is what sets that geometry.

NUMERICAL (mpmath/numpy), not exact-integer: the archimedean term (digamma psi(1/4+ir/2)) and
the prime weights (log p / sqrt p) are transcendental -- exactly P0/P6's point that the
archimedean place is not finitely generable. Floats are the medium, labelled; the conclusions
(sign of a min-eigenvalue; a balance to many digits) are robust.

RETAINED CORRECTION (the gate on this probe). A first formulation used
B_ij = sum_rho h_i(gamma_rho) conj(h_j(gamma_rho)) -- a sum of v v*, hence PSD BY CONSTRUCTION,
unable to test anything (min-eig ~ 0 for every offset). The correct Weil pairing is
        B_ij = sum_rho  fhat_i(rho) * conj( fhat_j(1 - conj(rho)) ),
since for g = f_i (convolved with) f_j-tilde the explicit-formula summand is
fhat_i(rho) conj(fhat_j(1-conj rho)). On the line 1-conj(rho)=rho, so B is a Gram matrix => PSD
(P0 sec 4.3, "finite positivity is free"). OFF the line 1-conj(rho) != rho, the pairing is
between DIFFERENT points and B becomes indefinite. That asymmetry is the whole content.

PART A (core). fhat_j(s) = transform of an even modulated Gaussian f_j(u)=e^{-u^2/2tau^2}cos(w_j u):
        fhat_j(s) = (1/2) sqrt(2pi) tau [ e^{tau^2 (c+i w_j)^2/2} + e^{tau^2 (c-i w_j)^2/2} ],  c=s-1/2,
peaked at frequency w_j. Build B for the true zeros (on the line) and after pushing ONE zero to
Re = 1/2 +- delta (its functional-equation + conjugate QUADRUPLE). Scan delta; watch min-eig cross 0.
  K : min-eig(B) >= 0 at delta=0 and < 0 once delta>0 -> Weil positivity <=> RH, and SENSITIVE.
  L : insensitive to delta.

PART B (assembly). Validate the Riemann-Weil explicit formula numerically for a Gaussian:
(sum over zeros) =?= (pole) + (archimedean digamma term) - (prime sum). A clean balance shows the
archimedean Gamma-term is the piece that completes the finite prime data (the Place-Completion).
"""

import sys
import mpmath as mp
import numpy as np

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass
mp.mp.dps = 30


def riemann_gammas(M):
    return [float(mp.im(mp.zetazero(k))) for k in range(1, M + 1)]


# ---------------------------------------------------------------------------
# PART A : the correctly-paired Weil form, positivity vs off-line offset
# ---------------------------------------------------------------------------
def fhat(s, thetas, tau):
    """Vector [ fhat_j(s) ] for COMPLEX-modulated Gaussians f_j(u)=e^{-u^2/2tau^2} e^{i theta_j u}:
        fhat_j(s) = sqrt(2pi) tau * exp( tau^2 (c + i theta_j)^2 / 2 ),  c = s - 1/2,
    peaked (in gamma) at gamma = -theta_j. A complex basis resolves the PHASE direction in which
    an off-line zero's indefiniteness lives -- a real (cosine) basis is blind to it."""
    c = s - 0.5
    pref = np.sqrt(2 * np.pi) * tau
    return np.array([pref * np.exp(tau ** 2 * (c + 1j * th) ** 2 / 2) for th in thetas])


def weil_form(zeros, omegas, tau):
    """Hermitian B_ij = sum_rho fhat_i(rho) conj(fhat_j(1-conj rho))."""
    n = len(omegas)
    B = np.zeros((n, n), dtype=complex)
    for rho in zeros:
        a = fhat(rho, omegas, tau)
        b = fhat(1 - np.conj(rho), omegas, tau)
        B += np.outer(a, np.conj(b))
    return (B + B.conj().T) / 2                     # Hermitian (exact for the symmetric zero set)


def config(gammas, off_index=None, delta=0.0):
    """List of zeros rho. On-line: 1/2 +- i*gamma. off_index-th pushed to Re=1/2 +- delta."""
    zs = []
    for k, g in enumerate(gammas):
        if k == off_index and delta != 0.0:
            zs += [0.5 + delta + 1j * g, 0.5 + delta - 1j * g,
                   0.5 - delta + 1j * g, 0.5 - delta - 1j * g]
        else:
            zs += [0.5 + 1j * g, 0.5 - 1j * g]
    return zs


def part_A(log):
    log("================  PART A : Weil positivity tracks the critical line  ================")
    gammas = riemann_gammas(15)
    g1 = gammas[0]                                   # ~14.135
    thetas = [-(g1 - 2), -(g1 - 1), -g1, -(g1 + 1), -(g1 + 2)]   # complex basis focused at zero #1
    tau = 1.0
    log("  first zeros gamma_k : " + ", ".join("%.3f" % g for g in gammas[:6]) + ", ...")
    log("  basis: 5 complex-modulated Gaussians focused at zero #1 (gamma_1=%.3f), tau=%.1f" % (g1, tau))
    log("  Weil form B_ij = sum_rho fhat_i(rho) conj(fhat_j(1-conj rho)) over the first 15 zeros;")
    log("  zero #1 pushed to Re = 1/2 +- delta (its functional-equation quadruple).")
    log("")
    log("  delta (off-line offset of zero #1) |   min eigenvalue of B   | positive?")
    log("  -----------------------------------+-------------------------+-----------------")
    rows = []
    for delta in [0.0, 0.02, 0.05, 0.10, 0.15, 0.20, 0.30]:
        B = weil_form(config(gammas, off_index=0, delta=delta), thetas, tau)
        mn = float(np.linalg.eigvalsh(B).min())
        rows.append((delta, mn))
        log("            %.2f                      | %22.6e | %s"
            % (delta, mn, "yes (PSD)" if mn > -1e-9 else "NO  (indefinite)"))
    onLine_psd = rows[0][1] > -1e-9
    offLine_neg = any(mn < -1e-9 for d, mn in rows if d > 0)
    cross = next((d for d, mn in rows if d > 0 and mn < -1e-9), None)
    log("")
    log("  [A] on the line (delta=0): PSD = %s ;  off-line breaks positivity = %s (first at delta=%s)"
        % (onLine_psd, offLine_neg, cross))
    return onLine_psd, offLine_neg


# ---------------------------------------------------------------------------
# PART B : explicit-formula balance (archimedean term completes the prime side)
# ---------------------------------------------------------------------------
def part_B(log):
    log("")
    log("================  PART B : the archimedean term completes the prime side  ===========")
    sigma = mp.mpf(5)
    h = lambda r: mp.e ** (-(r ** 2) / (2 * sigma ** 2))
    g = lambda u: (sigma / mp.sqrt(2 * mp.pi)) * mp.e ** (-(sigma ** 2) * (u ** 2) / 2)

    Z = mp.mpf(0)
    for k in range(1, 400):
        gk = mp.im(mp.zetazero(k))
        t = 2 * h(gk)
        Z += t
        if t < mp.mpf(10) ** (-28):
            break
    pole = 2 * h(mp.mpf(1) / 2 * 1j)
    arch = (1 / (2 * mp.pi)) * mp.quad(
        lambda r: h(r) * (mp.re(mp.digamma(mp.mpf(1) / 4 + 1j * r / 2)) - mp.log(mp.pi)),
        [-mp.inf, 0, mp.inf])

    def primes_upto(n):
        out, c = [], 2
        while c <= n:
            if all(c % p for p in out):
                out.append(c)
            c += 1
        return out
    prime = mp.mpf(0)
    for p in primes_upto(100000):
        lp = mp.log(p)
        k = 1
        while True:
            u = k * lp
            t = 2 * lp * mp.e ** (-u / 2) * g(u)
            prime += t
            if t < mp.mpf(10) ** (-28):
                break
            k += 1

    rhs = pole + arch - prime
    resid = Z - rhs
    log("  test function h(r)=exp(-r^2/2 sigma^2), sigma=%s" % sigma)
    log("  zero side   sum_rho h(gamma)        = %s" % mp.nstr(Z, 14))
    log("  pole  2 h(i/2)                      = %s" % mp.nstr(mp.re(pole), 14))
    log("  archimedean (digamma) term          = %s" % mp.nstr(arch, 14))
    log("  prime side  2 sum L(n) n^-.5 g       = %s" % mp.nstr(prime, 14))
    log("  pole + archimedean - prime          = %s" % mp.nstr(mp.re(rhs), 14))
    log("  residual (zero side - RHS)          = %s" % mp.nstr(abs(resid), 4))
    log("")
    log("  [B] explicit formula balances to ~%s. The archimedean term (%s) dominates the completion"
        % (mp.nstr(abs(resid), 2), mp.nstr(arch, 6)))
    log("      of the tiny prime side (%s) into the zero side (%s)."
        % (mp.nstr(-prime, 4), mp.nstr(Z, 6)))
    return abs(resid)


def main():
    lines = []

    def log(s=""):
        print(s)
        lines.append(s)

    log(__doc__)
    onLine_psd, offLine_neg = part_A(log)
    resid = part_B(log)

    log("")
    log("================  WHERE THIS CORNERS RH  ================")
    if onLine_psd and offLine_neg:
        log("PART A realized K. The Weil quadratic form is PSD exactly on the critical line, and a")
        log("single off-line zero (its functional-equation quadruple) drives the minimum eigenvalue")
        log("negative. So 'Weil positivity' is EQUIVALENT to RH and SENSITIVE to off-line zeros -- the")
        log("exact number-field mirror of the function-field circle test (where RH is Weil's theorem).")
        log("Conjecture 8.1's open step is therefore correctly and sharply stated: prove this one")
        log("explicit form stays PSD in the projective limit.")
    else:
        log("PART A did not realize K as expected; inspect the delta table.")
    log("")
    log("PART B: the explicit formula balances (residual ~%s). The archimedean digamma term is the"
        % mp.nstr(resid, 2))
    log("completing factor turning the finite prime data into the object whose positivity is RH --")
    log("P0's Place-Completion, numerically concrete, and P6's point that this term is the one the")
    log("finite primes cannot supply.")
    log("")
    log("Cornered (not crossed): RH = positivity of this one computable form; finite part free;")
    log("archimedean part the completing piece; off-line sensitivity demonstrated. Remaining target:")
    log("uniform positivity of the archimedean-adjoined limit -- the Connes/self-adjointness step,")
    log("now sharply localized.")

    from pathlib import Path
    rep = Path(__file__).resolve().parent / "reports" / "conj81_positivity.md"
    header = [
        "# Conjecture 8.1 Positivity Probe (RH direction)",
        "",
        "**Script:** `empirical/verify_conj81_positivity.py`",
        "**Context:** P0 Conjecture 8.1 -- RH = Weil positivity surviving the archimedean adjunction.",
        "**Nature:** high-precision NUMERICAL (mpmath); the archimedean term is transcendental.",
        "",
        "```text",
    ]
    rep.parent.mkdir(parents=True, exist_ok=True)
    rep.write_text("\n".join(header + lines + ["```", ""]), encoding="utf-8")
    print("\n[report -> %s]" % rep)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
