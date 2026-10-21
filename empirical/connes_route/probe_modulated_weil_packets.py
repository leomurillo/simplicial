"""Arithmetic two-packet diagnostics. Numerical only, no RH certificate.

Uses no zeta zeros. The final transfer-factor examples are hypothetical modes,
not claimed zeros. They measure a filter's sensitivity, not a detection theorem.
"""
import cmath
import json
import math
from pathlib import Path

import numpy as np
from scipy.integrate import quad

from probe_translated_prime_cancellation import prime_powers


A = math.log(2)


def g(v):
    return 2 * math.exp(-abs(v)) - .5 * math.exp(abs(v))


def G(s):
    if s == 1 or s == -1:
        return 1.5 * A
    return (5 - 4 * cmath.cosh(s * A)) / (1 - s * s)


def integrate_complex(fun):
    return sum(complex(quad(lambda v: fun(v).real, lo, hi, epsabs=2e-12)[0],
                       quad(lambda v: fun(v).imag, lo, hi, epsabs=2e-12)[0])
               for lo, hi in [(-A, 0), (0, A)])


def q_diag(w):
    constant = .5772156649015328606 + math.log(4 * math.pi) + math.log(math.tanh(A/2))
    def integrand(v):
        if v == 0:
            return -1.75
        return (math.exp(v/2)*g(v)*math.cos(w*v)-1.5)/math.sinh(v)
    integral = quad(integrand, 0, A, epsabs=2e-12, limit=500)[0]
    return 2 * G(.5-1j*w).real - 1.5 * constant - integral


def main():
    pairs = prime_powers(2_000_000)
    ns = np.array([n for n, _ in pairs], dtype=float)
    lps = np.array([math.log(p) for _, p in pairs])
    windows = [3, 10, 100, 1000, 10000, 100000, 1000000]
    frequencies = [0, 14, 21, 50, 100]
    records = []
    quadrature_errors = []
    for w in frequencies:
        q = q_diag(w)
        direct = integrate_complex(lambda v: g(v)*cmath.exp(-(.5-1j*w)*v))
        quadrature_errors.append(abs(direct-G(.5-1j*w)))
        for X in windows:
            mask = (ns >= X/2) & (ns <= 2*X)
            n = ns[mask]
            r = n/X
            v = np.log(r)
            weights = lps[mask]/np.sqrt(n)*np.where(r <= 1, 2*r-1/(2*r), 2/r-r/2)
            terms = weights*np.exp(-1j*w*v)
            P = complex(math.fsum(terms.real.tolist()), math.fsum(terms.imag.tolist()))
            correction = X**(-2.5)*integrate_complex(
                lambda v: g(v)*cmath.exp((2.5+1j*w)*v)/(1-math.exp(2*v)/X**2))
            K = math.sqrt(X)*G(.5-1j*w)-P-correction
            records.append({"omega": w, "X": X, "q": q,
                            "K_real": K.real, "K_imag": K.imag,
                            "abs_K_over_q": abs(K)/q,
                            "two_packet_min_Rayleigh": (q-abs(K))/1.5})
    transfer = []
    for H in [100, 1000, 10000]:
        delta = .1
        raw = abs(G(delta+1j*H))
        tuned = abs(G(delta))
        transfer.append({"hypothetical_height": H, "displacement": delta,
                         "fixed_packet_response": raw,
                         "frequency_matched_response": tuned,
                         "response_ratio": tuned/raw})
    previous = json.loads(Path(__file__).with_name('probe_translated_prime_cancellation.json').read_text())
    zero_checks = [abs(row['K_real']-prior['K_logX'])
                   for row, prior in zip([r for r in records if r['omega']==0], previous['samples'])]
    out = {"status": "Numerical diagnostics only; no interval enclosure and no RH proof",
           "max_transform_quadrature_error": max(quadrature_errors),
           "max_omega_zero_previous_probe_difference": max(zero_checks),
           "tested_pairs": len(records),
           "min_tested_two_packet_Rayleigh": min(r['two_packet_min_Rayleigh'] for r in records),
           "max_tested_abs_K_over_q": max(r['abs_K_over_q'] for r in records),
           "q_by_omega": {str(w): q_diag(w) for w in frequencies},
           "hypothetical_transfer_factors": transfer, "samples": records}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='samples'}, indent=2))


if __name__ == '__main__':
    main()
