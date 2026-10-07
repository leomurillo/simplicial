"""
Recompute ell_1(chi_5(2)) using ALL 50 zeros from LMFDB (both positive and
negative gamma values, since chi_5(2) is non-self-dual).

This corrects an error in earlier compute_dirichlet_zeros_v3.py which only
found positive gamma values via mpmath.
"""

# LMFDB chi_5(2): non-self-dual, order 4 quartic
# 50 zeros (negative gamma values listed first, then positive)

negative_gammas_chi5_2 = [
    55.53255063917714331177635885562, 53.75667308835424588804456665093,
    51.08998804633721267564942694432, 49.5201121831721842836352461905,
    48.47765991878316956160896236195, 46.26641381346456449258634989372,
    45.08582264962074326882242881556, 43.12543488567473830905726366337,
    40.508934445122041603749872022008, 39.0916158639927091132955773909,
    37.84761841624699497844836046640, 36.09652653725364935231283520536,
    33.30774552092450944486851535240, 31.714038216978378088676011094547,
    29.70278103479729044076360156773, 27.81247022179307495811051208168,
    26.47278891481336832795849047572, 22.9655764347914803808601277723,
    21.2830471577778699486763506284, 19.72905478631162605830813598374,
    16.99590394259028444664793427768, 14.11546426656964617536066631834,
    11.2828964415816001332254807924, 9.44293112972850911710026212431,
    4.13290370521285159500191933156,
]
positive_gammas_chi5_2 = [
    6.18357819545085391437751730970, 8.45722917442323072160535286274,
    12.67494641701135578048229914508, 14.82502557032842825143025217404,
    17.33780210685303969091451014241, 18.9985880416861449287245250119,
    22.48758458302875002505567290925, 24.36527977540229805651909575745,
    25.531186800433429601457551452466, 27.982756935693594324451001091893,
    30.46364068840366112797004484191, 32.195159688892272026544832306389,
    34.45722878527839758405756301004, 35.49089317885139349790895129816,
    37.27195057455605008724509915557, 40.39611485175259003483748872182,
    41.53645675792969665969385524901, 42.99208544275153854582429789755,
    44.82617597081092363119666478355, 46.59016101776473881831044964340,
    48.4778466442218740132847945792, 50.66421039080575037299754421231,
    51.977053467572707629124054585044, 53.442232173354543204000399997353,
    54.48544238876467911470039917979,
]

all_abs_gammas = sorted([abs(g) for g in negative_gammas_chi5_2] +
                        positive_gammas_chi5_2)

# Print first 15 zeros by |gamma|
print("=== chi_5(2) zeros by |gamma| (smallest first) ===")
for i, g in enumerate(all_abs_gammas[:15]):
    print(f"  |gamma_{i+1}| = {g:.4f}")
print(f"  ... ({len(all_abs_gammas) - 15} more, up to {all_abs_gammas[-1]:.2f})")

# ell_1 for chi_5(2) alone (all 50 zeros)
ell_1_chi5_2 = sum(1.0/g**2 for g in all_abs_gammas)
print(f"\nell_1(L(chi_5(2))) = sum 1/gamma^2 over all 50 zeros = {ell_1_chi5_2:.6f}")

# Conjugate: chi_5(3) has zeros at negations, same |gamma|, same ell_1
print(f"ell_1(L(chi_5(3))) = same (conjugate)   = {ell_1_chi5_2:.6f}")
print(f"Joint pair contribution = 2 * ell_1 = {2 * ell_1_chi5_2:.6f}")

# Comparison to my earlier mpmath
print(f"\n=== Comparison ===")
print(f"Old mpmath (chi_5_quartic_a positive gammas only): 0.063")
print(f"Old mpmath (chi_5_quartic_b positive gammas only): 0.095")
print(f"Old combined (treating as 2 independent L-functions): 0.158")
print(f"LMFDB ell_1(chi_5(2)) alone (all 50 zeros): {ell_1_chi5_2:.4f}")
print(f"Joint pair (chi_5(2) + chi_5(3)):           {2*ell_1_chi5_2:.4f}")
print(f"Correction factor: {2*ell_1_chi5_2/0.158:.3f}x")

# Update N=30 ell_1^joint estimate
print(f"\n=== Corrected N=30 joint cumulant estimate ===")
# Self-dual contributions (zeros at +/- gamma; doubled from positive-only LMFDB lists):
zeta_ell1 = 2 * sum(1.0/g**2 for g in [
    14.134725141734694, 21.022039638771555, 25.010857580145689,
    30.424876125859513, 32.935061587739190, 37.586178158825671,
    40.918719012147495, 43.327073280915000, 48.005150881167160,
    49.773832477672302,
])

chi3_ell1 = 2 * sum(1.0/g**2 for g in [
    8.039737155681467, 11.249206207772935, 15.704619176721626,
    18.261997495693128, 20.455770807742493, 24.059414856493451,
    26.577868735774585, 28.218164506233386, 30.745040261382496,
    33.897388927259419,
])

print(f"  zeta (self-dual, doubled): {zeta_ell1:.4f}")
print(f"  chi_{{-3}} (self-dual, doubled): {chi3_ell1:.4f}")
print(f"  chi_5(2)+chi_5(3) (non-self-dual pair, all gammas): {2*ell_1_chi5_2:.4f}")
print(f"  chi_5(4) Legendre (self-dual, NEED LMFDB DATA)")
print(f"  chi_15 trio (NEED LMFDB DATA)")

# Use mpmath estimates for missing characters, with proper self-dual handling
chi5_legendre_mpmath = 0.056  # positive gammas only
chi5_legendre_corrected = 2 * chi5_legendre_mpmath
print(f"  chi_5(4) Legendre placeholder (2 * mpmath positive): {chi5_legendre_corrected:.4f}")

# chi_15 placeholders (need verification on self-duality)
chi15_qq_mpmath = 0.193  # chi_3 * chi_5_quad, both real => self-dual
chi15_qq_corrected = 2 * chi15_qq_mpmath
print(f"  chi_15_qq (self-dual: chi_3*chi_5_quad, doubled): {chi15_qq_corrected:.4f}")

# chi_15_q1, chi_15_q2: non-self-dual conjugate pair (chi_3 * chi_5_quartic)
# My mpmath found positive gammas: 0.217 + 0.118 = 0.335 (this captured both + and -|gamma| of one L-function)
chi15_q1_combined_mpmath = 0.217 + 0.118  # both halves of chi_15_q1's zero set
chi15_pair_corrected = 2 * chi15_q1_combined_mpmath
print(f"  chi_15 quartic pair (chi_3 * chi_5_quart_a + conj): {chi15_pair_corrected:.4f}")

total_corrected = (zeta_ell1 + chi3_ell1 + 2*ell_1_chi5_2 + chi5_legendre_corrected
                   + chi15_qq_corrected + chi15_pair_corrected)
print(f"\nCorrected ell_1^joint(30) [first 10-25 zeros each, with factor-2 fix]: {total_corrected:.4f}")
print(f"Observed N=30 trace: 1.5191")
print(f"Ratio (trace/joint): {1.5191/total_corrected:.4f}")
