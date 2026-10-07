"""
N=30 joint cumulant: complete LMFDB integration.
All 8 primitive Dirichlet L-functions with conductor dividing 30 now have
LMFDB zero data. This is the definitive Pass-7 validation at N=30.
"""

import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# ---------------------------------------------------------------
# All 8 L-functions: LMFDB zeros (positive gammas only for self-dual,
# all gammas for non-self-dual)
# ---------------------------------------------------------------

# Self-dual L-functions: zeros at ±γ pairs; LMFDB lists positive only
zeros = {
    "zeta": [  # conductor 1, self-dual; 25 positive γ
        14.134725141734694, 21.022039638771555, 25.010857580145689,
        30.424876125859513, 32.935061587739190, 37.586178158825671,
        40.918719012147495, 43.327073280915000, 48.005150881167160,
        49.773832477672302, 52.970321477714461, 56.446247697063395,
        59.347044002602353, 60.831778524609810, 65.112544048081607,
        67.079810529494174, 69.546401711173979, 72.067157674481908,
        75.704690699083933, 77.144840068874805, 79.337375020249368,
        82.910380854086030, 84.735492980517050, 87.425274613125229,
        88.809111207634465,
    ],

    "L(chi_3) Legendre mod 3": [  # conductor 3, self-dual; 20 positive γ
        8.039737155681467, 11.249206207772935, 15.704619176721626,
        18.261997495693128, 20.455770807742493, 24.059414856493451,
        26.577868735774585, 28.218164506233386, 30.745040261382496,
        33.897388927259419, 35.608412653938635, 37.551796556364627,
        39.485207260929351, 42.616379226157568, 44.120572912072202,
        46.274118023513140, 47.514104510117322, 50.375138650636266,
        52.496749599060754, 54.193843101551914,
    ],

    "L(chi_5(4)) Legendre mod 5": [  # conductor 5, self-dual; 25 positive γ
        6.64845334472771471612327845997, 9.831444432886669616348321347458,
        11.95884562608351453026565868826, 16.03382112838423567459325378224,
        17.566994292325555202701595268144, 19.54073262278475025037869002299,
        22.227405454459410911877624963081, 24.58846621740819520765626997608,
        26.77609594800414011652357496527, 28.46103510017752247518697827232,
        29.70790935048096556923098651865, 33.00045600687051436794975917721,
        34.728812978904808674143729833981, 35.86863837181227459459504863887,
        38.12918472143653185015141827037, 39.56057294640318170505509505995,
        41.84243854579169430850930688531, 44.03129006144169504470090805842,
        45.4273000827822893888415619096, 46.49272715949140534533919935167,
        48.34566182106784617654820130449, 51.08775192674649135525825720413,
        52.1259022313169741886041306959, 53.83044519544216335105426902233,
        55.58928033540481015096458899849,
    ],

    "L(chi_15(14)) chi_3 x chi_5_Leg": [  # conductor 15, self-dual; 25 positive γ
        3.05701820980868915287415506904, 5.34319209367996891782367161036,
        7.26763059826680725286077767720, 10.133748155228375797259200600348,
        12.15969853381077081792324381745, 13.48938457315531804053322255533,
        15.240408529039033166877888159850, 16.63355841618558638158823442508,
        19.10349718525469465744305631936, 20.66236305141030677303888216364,
        22.17639768821376108756020485300, 23.36799923867493537660362632137,
        24.90350116904296767595196452334, 26.31976601519719112857065676519,
        28.65701374833144389761432722966, 29.69227751983587214188771803184,
        31.36470623994313228882952612958, 32.32338008181344539433639966495,
        33.78117919887043491359601713057, 35.0970556892378917853228489627,
        36.99584669791703414864511396216, 38.757341359970418830354799182704,
        39.44089794397602895029589030001, 41.22823157698679018330044979235,
        41.99740257490063314886123066149,
    ],
}

# Non-self-dual L-functions: conjugate pairs; all γ listed (positive + negative)
zeros_nonself = {
    "L(chi_5(2))": sorted([  # paired with chi_5(3)
        55.53255, 53.75667, 51.08999, 49.52011, 48.47766, 46.26641, 45.08582,
        43.12543, 40.50893, 39.09162, 37.84762, 36.09653, 33.30775, 31.71404,
        29.70278, 27.81247, 26.47279, 22.96558, 21.28305, 19.72905, 16.99590,
        14.11546, 11.28290, 9.44293, 4.13290,
        6.18358, 8.45723, 12.67495, 14.82503, 17.33780, 18.99859, 22.48758,
        24.36528, 25.53119, 27.98276, 30.46364, 32.19516, 34.45723, 35.49089,
        37.27195, 40.39611, 41.53646, 42.99209, 44.82618, 46.59016, 48.47785,
        50.66421, 51.97705, 53.44223, 54.48544,
    ]),

    "L(chi_15(2))": sorted([  # paired with chi_15(8)
        42.88707, 41.80835, 40.40725, 39.02994, 36.85301, 35.99118, 34.37951,
        33.29703, 31.99774, 30.51935, 28.55272, 26.79624, 25.89259, 24.07186,
        23.14895, 21.28464, 19.13784, 17.44476, 16.17189, 14.46446, 13.02896,
        10.32620, 8.26450, 6.59078, 4.40670,
        2.73460, 5.24301, 8.41469, 10.18760, 11.90737, 13.33740, 15.36614,
        17.77239, 18.97700, 20.62763, 21.88397, 23.33848, 25.38803, 27.19473,
        28.39898, 29.66537, 31.19236, 32.15849, 34.25978, 35.81988, 37.22297,
        38.27968, 39.61718, 40.86974, 42.12516,
    ]),
}

def s2(zs):
    return sum(1.0/g**2 for g in zs)

# ---------------------------------------------------------------
# Compute joint cumulant
# ---------------------------------------------------------------
print("=" * 78)
print(" PASS-7 N=30 FINAL VALIDATION (all 8 L-functions from LMFDB)")
print("=" * 78)
print()
print(f"  {'L-function':<40} {'#zeros':>7} {'contribution':>14}")
print(f"  {'-'*40} {'-'*7} {'-'*14}")

total = 0.0
# Self-dual: each contributes 2 * sum positive γ (zeros at ±γ pairs)
for name, zs in zeros.items():
    contribution = 2 * s2(zs)  # factor 2 from ±γ pairs
    total += contribution
    print(f"  {name:<40} {len(zs):>7} {contribution:>14.6f}  (2× LMFDB pos γ)")

# Non-self-dual pairs: each pair contributes 2 * sum 1/γ² over one L's zeros
# (Hadamard product over the pair has each |γ| with multiplicity 2)
for name, zs in zeros_nonself.items():
    pair_name = name + "+conj"
    contribution = 2 * s2(zs)  # factor 2 from pair structure
    total += contribution
    print(f"  {pair_name:<40} {len(zs)*2:>7} {contribution:>14.6f}  (2× LMFDB |γ|, pair)")

print(f"  {'-'*40} {'-'*7} {'-'*14}")
print(f"  {'TOTAL ell_1^joint(30)':<40} {'':>7} {total:>14.6f}")

# Comparison
trace = 1.5191
print()
print("=" * 78)
print(" Comparison to observed trace at N=30, T=7")
print("=" * 78)
print()
print(f"  Observed trace:           {trace:.6f}")
print(f"  ell_1^joint(30) [LMFDB]:  {total:.6f}")
print(f"  Ratio (trace/joint):      {trace/total:.6f}")
print(f"  Deficit:                  {(1 - trace/total)*100:.2f}%")
print()
print(f"  Pass-7 prediction: finite-T deficit ~ 1/T (explicit-formula remainder)")
print(f"  At T=7, predicted deficit: ~ {100/7:.2f}%")
print(f"  Observed deficit:          {(1 - trace/total)*100:.2f}%")
print()
print(f"  Match with predicted 1/T scaling: " +
      ("EXCELLENT" if abs((1-trace/total)*100 - 100/7) < 5 else "approximate"))

# Pass-5 vs Pass-7 comparison
print()
print("=" * 78)
print(" Improvement over previous framings")
print("=" * 78)
print()
print(f"  Pass-5 RH-only:           trace/ell_1(zeta) = 1.519/0.0186 = 81.7")
print(f"  Pass-7 estimates:         trace/ell_1^joint ~ 5x")
print(f"  Pass-7 mpmath:            trace/ell_1^joint ~ 0.95")
print(f"  Pass-7 LMFDB (final):     trace/ell_1^joint = {trace/total:.4f}")
print(f"  Pass-7 improvement over Pass-5: {81.7/(trace/total):.0f}x")

# Per-L-function breakdown
print()
print("=" * 78)
print(" Per-L-function first-zero data (sanity check)")
print("=" * 78)
print()
print(f"  {'L-function':<40} {'γ_1':>10} {'γ_1^{-2}':>10}")
for name, zs in zeros.items():
    print(f"  {name:<40} {zs[0]:>10.4f} {1/zs[0]**2:>10.6f}")
for name, zs in zeros_nonself.items():
    print(f"  {name:<40} {min(zs):>10.4f} {1/min(zs)**2:>10.6f}")
