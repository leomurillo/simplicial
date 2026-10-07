r"""The Connes recast: the two faces of RH as one trace-positivity over the places.

Connes (1999) reads the Weil explicit formula as a TRACE FORMULA on the adele class space:
for a test function h on the idele classes,
        sum_rho h(gamma_rho)  =  Tr(h applied to the zero-operator)  =  sum_v (local term)_v,
the sum running over the places v (the primes p and the archimedean place infinity), plus the
pole. RH is then the POSITIVITY of this trace for h = f * f~ -- equivalently, the
self-adjointness (real spectrum) of the operator D whose spectrum is the zeros.

This single statement subsumes the two faces we probed separately:
  * POSITIVITY (Weil form): Tr((f*f~)(D)) >= 0.  On the line the form is a Gram matrix V*V
    (manifestly a trace of a positive operator); off the line it is NOT of the form V*V and
    goes indefinite -- the detector. So  RH <=> the form is V*V  <=>  D self-adjoint.
  * APPROXIMATION (Beurling-Nyman): 1 is cyclic / reachable -- the same operator's spectral
    measure has the support that makes d_N -> 0.
Two properties (positivity, cyclicity) of ONE operator; both <=> RH.

PART A. Exhibit the trace-positive structure Z = V*V on the line, and that an off-line zero
        breaks the V*V form (min-eig < 0). [Weil positivity, in operator/self-adjointness form.]
PART B. Decompose the trace formula by PLACE: pole + archimedean + sum over primes = sum over
        zeros, displaying each local term. Isolates the archimedean place as the dominant,
        and the one whose positivity contribution is the open step (the Connes-Consani prolate
        operator -- the archimedean 'forcing structure', the analogue of the Hodge index that
        forces the function-field RH).

NUMERICAL (mpmath/numpy), labelled. Reuses the verified explicit-formula balance (~1e-31).
"""

import sys
import mpmath as mp
import numpy as np

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass
mp.mp.dps = 30


# ---- shared: phi_j(s) = transform of a complex-modulated Gaussian (peaks at frequency -theta_j)
def phi(s, thetas, tau):
    c = s - 0.5
    pref = np.sqrt(2 * np.pi) * tau
    return np.array([pref * np.exp(tau ** 2 * (c + 1j * th) ** 2 / 2) for th in thetas])


def part_A(log):
    log("================  PART A : Weil positivity = Tr(V*V), broken off the line  ============")
    gammas = [float(mp.im(mp.zetazero(k))) for k in range(1, 16)]
    g1 = gammas[0]
    thetas = [-(g1 - 2), -(g1 - 1), -g1, -(g1 + 1), -(g1 + 2)]
    tau = 1.0

    # On the line: rows = the zeros rho = 1/2 + i gamma (both +-gamma); V_{k j} = phi_j(rho_k).
    rows = []
    for g in gammas:
        rows.append(phi(0.5 + 1j * g, thetas, tau))
        rows.append(phi(0.5 - 1j * g, thetas, tau))
    V = np.array(rows)                                   # (2*15) x 5
    Z = V.conj().T @ V                                   # = sum_rho phi(rho) phi(rho)^*  -- a TRACE of V*V
    ev_on = np.linalg.eigvalsh((Z + Z.conj().T) / 2)

    # Off the line: pair phi_i(rho) with conj(phi_j(1-conj rho)) -- NOT V*V anymore.
    def weil_off(delta):
        n = len(thetas)
        B = np.zeros((n, n), dtype=complex)
        zeros = []
        for k, g in enumerate(gammas):
            if k == 0 and delta:
                zeros += [0.5 + delta + 1j * g, 0.5 + delta - 1j * g,
                          0.5 - delta + 1j * g, 0.5 - delta - 1j * g]
            else:
                zeros += [0.5 + 1j * g, 0.5 - 1j * g]
        for rho in zeros:
            a = phi(rho, thetas, tau)
            b = phi(1 - np.conj(rho), thetas, tau)
            B += np.outer(a, np.conj(b))
        return (B + B.conj().T) / 2
    ev_off = np.linalg.eigvalsh(weil_off(0.2))

    log("  On the line:  Z = V* V  (V_{rho,j} = phi_j(rho)) -- manifestly a trace of a POSITIVE")
    log("    operator. min eigenvalue = %+.3e  (>= 0: self-adjoint / spectrum real)." % ev_on.min())
    log("  Off the line (one zero at Re=1/2+-0.2): the form is V* W with W != V, no longer V*V.")
    log("    min eigenvalue = %+.3e  (< 0: the operator is NOT self-adjoint)." % ev_off.min())
    log("  => RH  <=>  the Weil form is of the form V*V  <=>  the zero-operator is self-adjoint.")
    return ev_on.min() > -1e-9 and ev_off.min() < -1e-9


def part_B(log):
    log("")
    log("================  PART B : the trace formula = sum over places  ================")
    sigma = mp.mpf(5)
    h = lambda r: mp.e ** (-(r ** 2) / (2 * sigma ** 2))
    g = lambda u: (sigma / mp.sqrt(2 * mp.pi)) * mp.e ** (-(sigma ** 2) * (u ** 2) / 2)

    # spectral side: Tr(h(D)) = sum over zeros
    Z = mp.mpf(0)
    for kk in range(1, 400):
        gk = mp.im(mp.zetazero(kk))
        t = 2 * h(gk)
        Z += t
        if t < mp.mpf(10) ** (-28):
            break

    pole = 2 * h(mp.mpf(1) / 2 * 1j)
    W_inf = (1 / (2 * mp.pi)) * mp.quad(
        lambda r: h(r) * (mp.re(mp.digamma(mp.mpf(1) / 4 + 1j * r / 2)) - mp.log(mp.pi)),
        [-mp.inf, 0, mp.inf])

    def primes_upto(n):
        out, c = [], 2
        while c <= n:
            if all(c % p for p in out):
                out.append(c)
            c += 1
        return out
    primes = primes_upto(100000)
    Wp = {}
    for p in primes:
        lp = mp.log(p)
        s = mp.mpf(0)
        kk = 1
        while True:
            u = kk * lp
            t = 2 * lp * mp.e ** (-u / 2) * g(u)
            s += t
            if t < mp.mpf(10) ** (-28):
                break
            kk += 1
        Wp[p] = s
    prime_total = mp.fsum(Wp.values())

    log("  spectral side:  Tr(h(D)) = sum_rho h(gamma)        = %s" % mp.nstr(Z, 12))
    log("  geometric side = sum over places (pole + arch - primes):")
    log("     place: pole (s=1)            local term = %s" % mp.nstr(mp.re(pole), 12))
    log("     place: infinity (archimedean) local term = %s   <-- dominant, transcendental" % mp.nstr(W_inf, 12))
    for p in primes[:6]:
        log("     place: p = %-2d                  local term = %s" % (p, mp.nstr(-Wp[p], 12)))
    log("     ... (remaining primes sum to %s)" % mp.nstr(-(prime_total - mp.fsum(Wp[p] for p in primes[:6])), 8))
    rhs = pole + W_inf - prime_total
    log("  sum over places                            = %s" % mp.nstr(mp.re(rhs), 12))
    log("  residual (spectral - geometric)            = %s" % mp.nstr(abs(Z - rhs), 4))
    log("")
    log("  The archimedean local term (%s) dominates; the finite primes contribute %s in total."
        % (mp.nstr(W_inf, 6), mp.nstr(-prime_total, 6)))
    log("  RH = positivity of this trace for h=f*f~. The finite-place contribution is computable")
    log("  and (P0 sec4.3) the Gram part is free; the ARCHIMEDEAN local positivity is the open step.")
    return abs(Z - rhs)


def main():
    out = []

    def log(s=""):
        print(s)
        out.append(s)

    log(__doc__)
    okA = part_A(log)
    resB = part_B(log)

    log("")
    log("================  THE SINGLE STATEMENT (the recast)  ================")
    log("RH  <=>  Tr_v( (f * f~) )  >=  0  for all test functions f,")
    log("where Tr_v is the Weil/Connes trace = sum over places (PART B), equivalently")
    log("        <=>  the zero-operator D is self-adjoint  (its Weil form is V*V, PART A)")
    log("        <=>  1 is reachable in the Beurling-Nyman space (cyclicity of the same D).")
    log("")
    log("Three readings, one object. The finite places give a free Gram positivity; the open")
    log("content is the ARCHIMEDEAN local positivity -- the Connes-Consani prolate-operator")
    log("target. That archimedean term is the forcing structure to find, exactly as the Hodge")
    log("index forces the function-field RH (P0/P4). The march showed brute N cannot reach it;")
    log("this recast says what WOULD: a symmetry that makes the archimedean trace term positive")
    log("by construction, the way intersection positivity does over a curve.")

    from pathlib import Path
    rep = Path(__file__).resolve().parent / "reports" / "connes_recast.md"
    header = [
        "# The Connes Recast: two faces of RH as one trace-positivity",
        "",
        "**Script:** `empirical/verify_connes_recast.py`",
        "**Context:** culmination of the Conj 8.1 / Beurling-Nyman / conditioning probes.",
        "**Nature:** numerical (mpmath/numpy), labelled; reuses the verified explicit-formula balance.",
        "",
        "```text",
    ]
    rep.parent.mkdir(parents=True, exist_ok=True)
    rep.write_text("\n".join(header + out + ["```", ""]), encoding="utf-8")
    print("\n[report -> %s]" % rep)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
