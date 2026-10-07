"""
bridge_lfunctions_hankel_positivity.py
======================================

Pass-8 step (6): Hankel/Jacobi positivity check on the LMFDB-derived
joint cumulant sequence

    ell_n^joint(N) := (1/phi(N))? sum_{chi != chi_0} sum_{gamma_chi} 1/gamma^{2n}
                                  (n = 1, 2, 3, ...)

at N = 30.

The relevant positivity criteria (cf. Pass-5 Apex Lemma_HJ) are:

  H_n  =  ( ell_{i+j+1} )_{0 <= i,j <= n}        (Hamburger / classical Hankel)
  J_n  =  ( ell_{i+j+2} )_{0 <= i,j <= n}        (shifted / Stieltjes-jacobi)

If the moment sequence {ell_n} is the moment sequence of a positive measure on
[0, infty), then BOTH H_n and J_n are positive semi-definite for all n >= 0.

Conversely (Hamburger / Stieltjes moment problem), if H_n, J_n succeed 0 for
all n with appropriate growth, the sequence is the moment sequence of a unique
positive measure (under the determinacy assumption from Carleman's criterion).

Our sequence is literally
    ell_n = sum_chi sum_gamma 1/gamma^{2n}
which is the moment sequence of the discrete positive measure
    mu = sum_chi sum_gamma delta_{1/gamma^2}
on [0, 1/gamma_min^2].  So H_n, J_n MUST be positive semidefinite for any
truncation that respects this structural fact.

The non-trivial test is whether the FINITE-zero TRUNCATION (we only have
~25 zeros per L-function from LMFDB) yields positive Hankel matrices, and
whether the eigenvalue structure carries information about the multi-character
spectral content.
"""

import sys
import io
import json

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import numpy as np

# Per-character zero spectra (positive gammas only for self-dual; full pair for
# non-self-dual).  Same data as in compute_lmfdb_final_N30.py.
zeros_zeta = [
    14.134725141734694, 21.022039638771555, 25.010857580145689,
    30.424876125859513, 32.935061587739190, 37.586178158825671,
    40.918719012147495, 43.327073280915000, 48.005150881167160,
    49.773832477672302, 52.970321477714461, 56.446247697063395,
    59.347044002602353, 60.831778524609810, 65.112544048081607,
    67.079810529494174, 69.546401711173979, 72.067157674481908,
    75.704690699083933, 77.144840068874805, 79.337375020249368,
    82.910380854086030, 84.735492980517050, 87.425274613125229,
    88.809111207634465,
]
zeros_chi3 = [
    8.039737155681467, 11.249206207772935, 15.704619176721626,
    18.261997495693128, 20.455770807742493, 24.059414856493451,
    26.577868735774585, 28.218164506233386, 30.745040261382496,
    33.897388927259419, 35.608412653938635, 37.551796556364627,
    39.485207260929351, 42.616379226157568, 44.120572912072202,
    46.274118023513140, 47.514104510117322, 50.375138650636266,
    52.496749599060754, 54.193843101551914,
]
zeros_chi5_leg = [
    6.64845334472771472, 9.83144443288666962, 11.95884562608351453,
    16.03382112838423567, 17.56699429232555520, 19.54073262278475025,
    22.22740545445941091, 24.58846621740819521, 26.77609594800414012,
    28.46103510017752248, 29.70790935048096557, 33.00045600687051437,
    34.72881297890480867, 35.86863837181227459, 38.12918472143653185,
    39.56057294640318171, 41.84243854579169431, 44.03129006144169504,
    45.42730008278228939, 46.49272715949140535, 48.34566182106784618,
    51.08775192674649136, 52.12590223131697419, 53.83044519544216335,
    55.58928033540481015,
]
zeros_chi15_leg = [
    3.05701820980868915, 5.34319209367996892, 7.26763059826680725,
    10.13374815522837580, 12.15969853381077082, 13.48938457315531804,
    15.24040852903903317, 16.63355841618558638, 19.10349718525469466,
    20.66236305141030677, 22.17639768821376109, 23.36799923867493538,
    24.90350116904296768, 26.31976601519719113, 28.65701374833144390,
    29.69227751983587214, 31.36470623994313229, 32.32338008181344539,
    33.78117919887043491, 35.09705568923789179, 36.99584669791703415,
    38.75734135997041883, 39.44089794397602895, 41.22823157698679018,
    41.99740257490063315,
]
zeros_chi5_quart = [
    55.53255, 53.75667, 51.08999, 49.52011, 48.47766, 46.26641, 45.08582,
    43.12543, 40.50893, 39.09162, 37.84762, 36.09653, 33.30775, 31.71404,
    29.70278, 27.81247, 26.47279, 22.96558, 21.28305, 19.72905, 16.99590,
    14.11546, 11.28290, 9.44293, 4.13290,
    6.18358, 8.45723, 12.67495, 14.82503, 17.33780, 18.99859, 22.48758,
    24.36528, 25.53119, 27.98276, 30.46364, 32.19516, 34.45723, 35.49089,
    37.27195, 40.39611, 41.53646, 42.99209, 44.82618, 46.59016, 48.47785,
    50.66421, 51.97705, 53.44223, 54.48544,
]
zeros_chi15_quart = [
    42.88707, 41.80835, 40.40725, 39.02994, 36.85301, 35.99118, 34.37951,
    33.29703, 31.99774, 30.51935, 28.55272, 26.79624, 25.89259, 24.07186,
    23.14895, 21.28464, 19.13784, 17.44476, 16.17189, 14.46446, 13.02896,
    10.32620, 8.26450, 6.59078, 4.40670,
    2.73460, 5.24301, 8.41469, 10.18760, 11.90737, 13.33740, 15.36614,
    17.77239, 18.97700, 20.62763, 21.88397, 23.33848, 25.38803, 27.19473,
    28.39898, 29.66537, 31.19236, 32.15849, 34.25978, 35.81988, 37.22297,
    38.27968, 39.61718, 40.86974, 42.12516,
]

# Joint zero collection: factor 2 for self-dual (positive gammas only listed);
# already-paired data for non-self-dual.  This is the EFFECTIVE multi-set of
# values {1/g^2 : g is a zero of any non-trivial L-function with conductor | 30}.
def doubled(zs):
    """Return both positive and negative gamma contributions: each |gamma|^{-2}
    appears twice in the joint zero multiset for self-dual L-functions."""
    return list(zs) + list(zs)

joint_zeros = (
    doubled(zeros_chi3)                     # self-dual, pair sym -> double pos
    + doubled(zeros_chi5_leg)              # self-dual, pair sym -> double pos
    + doubled(zeros_chi15_leg)             # self-dual, pair sym -> double pos
    + list(zeros_chi5_quart)               # quartic chi_a, full pair listing
    + list(zeros_chi5_quart)               # quartic chi_b (conjugate; same |gamma|)
    + list(zeros_chi15_quart)              # quartic chi_15_a, full pair listing
    + list(zeros_chi15_quart)              # quartic chi_15_b (conjugate; same |gamma|)
)
print(f"Total zero-pair contributions: {len(joint_zeros)}")
print(f"Smallest |gamma| in joint set: {min(abs(g) for g in joint_zeros):.4f}")
print(f"Largest |gamma| in joint set:  {max(abs(g) for g in joint_zeros):.4f}")

# Compute joint cumulants ell_n^joint(30) for n = 1..10
N_max = 10
ell_joint = [sum(1.0 / g ** (2 * n) for g in joint_zeros) for n in range(1, N_max + 1)]

print()
print(f"=== ell_n^joint(30) for n = 1..{N_max} ===")
for n, e in enumerate(ell_joint, 1):
    print(f"  ell_{n}^joint(30) = {e:.6e}")

# ---------------------------------------------------------------------
# Hankel matrices on the cumulant sequence
# ---------------------------------------------------------------------
# H_n[i,j] = ell_{i+j+1}    Hamburger (classical Hankel)
# J_n[i,j] = ell_{i+j+2}    shifted (Stieltjes-jacobi)
#
# We can build up to dimension n+1 where 2n+2 <= N_max, i.e., n <= 4.

print()
print("=" * 80)
print(" Hankel H_n: H_n[i,j] = ell_{i+j+1}^joint(30)")
print("=" * 80)
for n in range(5):
    H = np.array([[ell_joint[i+j] for j in range(n+1)] for i in range(n+1)])
    eigvals = np.linalg.eigvalsh(H)
    det_H = np.linalg.det(H)
    pos = all(e > -1e-12 for e in eigvals)
    print(f"\n  n = {n}, dim = {n+1}")
    print(f"    eigenvalues: {[f'{e:.4e}' for e in eigvals]}")
    print(f"    det(H_{n}) = {det_H:.6e}    PSD: {pos}")

print()
print("=" * 80)
print(" Jacobi J_n: J_n[i,j] = ell_{i+j+2}^joint(30)")
print("=" * 80)
for n in range(4):
    if 2 * n + 2 > N_max:
        break
    J = np.array([[ell_joint[i+j+1] for j in range(n+1)] for i in range(n+1)])
    eigvals = np.linalg.eigvalsh(J)
    det_J = np.linalg.det(J)
    pos = all(e > -1e-12 for e in eigvals)
    print(f"\n  n = {n}, dim = {n+1}")
    print(f"    eigenvalues: {[f'{e:.4e}' for e in eigvals]}")
    print(f"    det(J_{n}) = {det_J:.6e}    PSD: {pos}")

# ---------------------------------------------------------------------
# Note: structural certainty
# ---------------------------------------------------------------------
# Because ell_n = integral_{[0, gamma_min^{-2}]} t^n d_mu(t) for the
# discrete positive measure mu = sum delta_{1/gamma^2}, Hamburger's
# theorem guarantees H_n, J_n succeed 0 for ALL n.  The truncated zero
# data preserves positivity exactly because truncation just restricts mu
# to a sub-multiset of atoms.  The interesting numerical question is
# how rapidly det H_n, det J_n decay (they decay roughly like product
# of eigenvalues, which decreases geometrically).

print()
print("=" * 80)
print(" Structural note")
print("=" * 80)
print()
print("  The sequence {ell_n^joint(30)} consists of moments of the discrete")
print("  positive measure mu = sum_{chi, gamma} delta_{1/gamma^2} on")
print("  [0, 1/gamma_min^2].  Hence H_n succeed 0 AND J_n succeed 0 for all")
print("  finite truncations (and would for the full infinite-zero sequence).")
print("  This is the LMFDB-truncated witness of the Apex Lemma_HJ at N = 30.")
print()
print("  Det H_n decay (Hadamard-style) reflects the support condensation")
print("  near gamma_min^{-2} = 1/gamma_1^2 where gamma_1 = 3.057 (smallest")
print("  zero, from chi_15 Legendre).")
print()

# ---------------------------------------------------------------------
# Persist
# ---------------------------------------------------------------------
out = {
    "N": 30,
    "n_joint_zeros": len(joint_zeros),
    "min_gamma": min(abs(g) for g in joint_zeros),
    "max_gamma": max(abs(g) for g in joint_zeros),
    "ell_joint": ell_joint,
    "hankel": [
        {"n": n,
         "dim": n+1,
         "eigvals": list(np.linalg.eigvalsh(
            np.array([[ell_joint[i+j] for j in range(n+1)] for i in range(n+1)])
         )),
         "det": float(np.linalg.det(
            np.array([[ell_joint[i+j] for j in range(n+1)] for i in range(n+1)])
         )),
        }
        for n in range(5)
    ],
    "jacobi": [
        {"n": n,
         "dim": n+1,
         "eigvals": list(np.linalg.eigvalsh(
            np.array([[ell_joint[i+j+1] for j in range(n+1)] for i in range(n+1)])
         )),
         "det": float(np.linalg.det(
            np.array([[ell_joint[i+j+1] for j in range(n+1)] for i in range(n+1)])
         )),
        }
        for n in range(4)
    ],
}
with open(r"C:\Projects\simplicial\bridge_lfunctions_hankel_positivity.json", "w") as f:
    json.dump(out, f, indent=2, default=lambda o: float(o.real) if hasattr(o, 'real') else o)
print("  Wrote: bridge_lfunctions_hankel_positivity.json")
