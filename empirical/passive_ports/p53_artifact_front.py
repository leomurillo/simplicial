"""Artifact front of the finite zeta port (Paper 53 §4.7): sigma_min(X, t) = smallest real part among the port's
off-line zeros in the window [t0, t0 + 20], 1/2 < sigma < 1.  The band 1/2 < sigma < sigma_min is certified free
of off-line zeros of the port at that resolution and height."""
import numpy as np
from p53_third_law_curve import make
from p53_persistence_probe import strip_zeros

XS = [31, 53, 97, 167, 293, 509, 887, 1543, 2689, 4679, 8147]
print("sigma_min - 1/2 (blank: no off-line zero in the window)   rows: window start; columns: X =", XS)
for t0 in (30.0, 110.0, 410.0, 1610.0, 3210.0):
    cells = []
    for X in XS:
        F, arch = make("zeta_c", X)
        z = strip_zeros(F, 0.502, 0.999, t0, t0 + 20.0)
        cells.append(f"{np.min(z.real) - 0.5:6.3f}" if len(z) else "   -  ")
    print(f"  t0={t0:6.0f}: " + " ".join(cells), flush=True)
