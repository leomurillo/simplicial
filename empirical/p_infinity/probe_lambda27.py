"""
probe_lambda27.py — extend the eps-convergence / prolate-defect test to lambda=2.7.

lambda=2.7 is PAST the 7-joining (sqrt(7)=2.646), primes {2,3,5,7}. True eps ~ c*(1-chi_4) is tiny
(1-chi_4 ~ 2.4e-30), so the Fourier ground needs more modes -> sweep N to 52 with Aitken
extrapolation. Question: does eps(inf) stay POSITIVE with eps/(1-chi_4) ~ O(10), as at 2.0/2.3/2.5?

Reuses build_QW/ground/chi4_defect/aitken from probe_archimedean_eps_converge. dps 45, no torch.
"""
import mpmath as mp
from probe_archimedean_eps_converge import build_QW, ground, chi4_defect, aitken, ns

mp.mp.dps = 45


def main():
    lam = mp.mpf("2.7")
    d4 = chi4_defect(lam)
    print(f"lambda=2.7  (past sqrt(7)=2.646, 7-joining)   1-chi_4(hp) = {ns(d4, 6)}", flush=True)
    print(f"  {'N':>4} {'eps(N)':>16} {'rel prev':>10} {'eps/(1-chi4)':>14}", flush=True)
    seq, primes = [], None
    for N in range(24, 53, 4):
        QW, primes = build_QW(lam, N)
        e = ground(QW, N)
        rel = abs(e - seq[-1]) / abs(seq[-1]) if seq else None
        seq.append(e)
        print(f"  {N:>4} {ns(e, 7):>16} {(f'{float(rel):.2%}' if rel is not None else '--'):>10} "
              f"{float(e / d4):>14.4f}", flush=True)
        if rel is not None and rel < mp.mpf("0.005"):
            print("       (converged: rel < 0.5%)", flush=True)
            break
    ext = aitken(seq)
    print(f"  primes in window: {primes}", flush=True)
    if ext is not None:
        print(f"  Aitken-extrapolated eps(inf) = {ns(ext, 6)}   sign = {'+' if ext > 0 else ('0' if ext == 0 else '-')}",
              flush=True)
        print(f"  eps(inf)/(1-chi_4) = {float(ext / d4):.4f}   "
              f"({'positive & O(10): H0prime holds at lambda=2.7, mechanism through the 7-joining' if (ext > 0 and ext / d4 < 30) else 'examine'})",
              flush=True)


if __name__ == "__main__":
    main()
