"""
Diagnose the discrepancy between direct Hurwitz formula and L-function decomposition.

Strategy: compute B_G by BOTH the direct sum and via L-functions at high precision,
print each intermediate value, identify where they diverge.
"""

import mpmath as mp

mp.mp.dps = 50  # very high precision

# Test point: first zeta zero
s = mp.mpc(mp.mpf('0.5'), mp.mpf('14.134725141734693790457251983562'))

# Test G_balanced: G_diag = [1, -1, 0.5, -0.5, 0, 0]
G_diag = [mp.mpf(1), mp.mpf(-1), mp.mpf('0.5'), mp.mpf('-0.5'), mp.mpf(0), mp.mpf(0)]

a = mp.mpc(2) ** (-s)  # 2^{-s}
b = mp.mpc(3) ** (-s)  # 3^{-s}
six_inv_s = mp.mpc(6) ** (-s)  # 6^{-s}

print(f"s = {s}")
print(f"|s - first_zero| = {abs(s - mp.mpc(mp.mpf('0.5'), mp.mpf('14.134725141734693790457251983562'))):.2e}")
print(f"a = 2^(-s) = {a}")
print(f"b = 3^(-s) = {b}")
print(f"6^(-s) = {six_inv_s}")
print(f"a*b = 6^(-s)? diff = {a*b - six_inv_s}")
print()

# Compute Hurwitz zetas directly
H = {}
for r in range(1, 6):
    H[r] = mp.zeta(s, mp.mpf(r)/6)
    print(f"zeta(s, {r}/6) = {H[r]}")

print()

# Compute sigma_r directly
sigma = {}
for r in range(1, 6):
    sigma[r] = six_inv_s * H[r]
    print(f"sigma_{r}(s) = 6^(-s) * zeta(s, {r}/6) = {sigma[r]}")

# Sanity: sum of all sigma_r should equal sum over n not divisible by 6 of n^{-s}
# Also: sigma_1 + sigma_5 should equal zeta(s)(1-a)(1-b)
total_coprime = sigma[1] + sigma[5]
formula_coprime = mp.zeta(s) * (1 - a) * (1 - b)
print(f"\nsigma_1 + sigma_5 = {total_coprime}")
print(f"zeta(s)(1-a)(1-b) = {formula_coprime}")
print(f"Difference: {total_coprime - formula_coprime}")

print()
sigma2_plus_4 = sigma[2] + sigma[4]
formula24 = a * mp.zeta(s) * (1 - b)
print(f"sigma_2 + sigma_4 = {sigma2_plus_4}")
print(f"a * zeta(s)(1-b) = {formula24}")
print(f"Difference: {sigma2_plus_4 - formula24}")

print()
formula3 = b * mp.zeta(s) * (1 - a)
print(f"sigma_3 = {sigma[3]}")
print(f"b * zeta(s)(1-a) = {formula3}")
print(f"Difference: {sigma[3] - formula3}")

# B_G direct
B_G_direct = -sigma[1] + mp.mpf('0.5') * sigma[2] - mp.mpf('0.5') * sigma[3]
print(f"\nB_G direct = {B_G_direct}")

# B_G via L-function decomposition
# L_6 = sigma_1 - sigma_5 (imprimitive)
# L_3 = sigma_1^(3) - sigma_2^(3); sigma_r^(3) = (1/3)^s * zeta(s, r/3)
L_6 = sigma[1] - sigma[5]
sigma1_3 = mp.mpc(3)**(-s) * mp.zeta(s, mp.mpf(1)/3)
sigma2_3 = mp.mpc(3)**(-s) * mp.zeta(s, mp.mpf(2)/3)
L_3 = sigma1_3 - sigma2_3

print(f"\nL_6 (via sigma) = sigma_1 - sigma_5 = {L_6}")
print(f"L_3 (via sigma_3) = sigma_1^(3) - sigma_2^(3) = {L_3}")

# Z(s) = zeta(s) * [-1/2 + a*(3-b)/4]
Z = mp.zeta(s) * (mp.mpf(-1)/2 + a * (3 - b) / 4)
print(f"\nZ(s) = {Z}")

B_G_decomp = Z - L_6 / 2 + (a / 4) * L_3
print(f"\nB_G decomp = Z - L_6/2 + (a/4)*L_3 = {B_G_decomp}")

print(f"\nDifference: B_G_decomp - B_G_direct = {B_G_decomp - B_G_direct}")
print(f"|Difference|: {abs(B_G_decomp - B_G_direct)}")

# Verify identity: -sigma_1 + 0.5 sigma_2 - 0.5 sigma_3 == Z - L_6/2 + (a/4) L_3
# Expand RHS using sigma decompositions:
# Z = -1/2 zeta (1-a)(1-b) + a/4 zeta(1-b) - b/2 zeta(1-a)
#   = -1/2 (sigma_1 + sigma_5) + a/4 (sigma_1^(3) + sigma_2^(3)) - b/2 * (sigma_3 + ... wait)
# Hmm let me think.

# Actually: zeta(s)(1-a)(1-b) = sigma_1 + sigma_5 (sum over coprime to 6)
# zeta(s)(1-b) = sigma_1^(3) + sigma_2^(3) ? No, that's only mod 3 coprime, but includes 2-multiples.
# zeta(s)(1-b) = sum over n coprime to 3 = sigma over {n: 3 doesn't divide n} = ?
# zeta(s)(1-2^{-s}) = sum over odd n.

# Let me re-derive Z using sigma's directly:
# Z = -1/2 (sigma_1 + sigma_5) + a/4 * [zeta(s)(1-b)] - b/2 [zeta(s)(1-a)]
# But zeta(s)(1-b) is NOT 2^s sigma_1^(3) + 2^s sigma_2^(3) etc; it's sum over n coprime to 3.

# zeta(s)(1-3^{-s}) = sum_{gcd(n,3)=1} n^{-s} = sigma_1^(3) + sigma_2^(3) (where these are the mod-3 versions)
# Note: sigma_r^(3) is mod-3, not mod-6. So this includes both odd and even n that are coprime to 3.

# sigma_2 (mod 6) = subset of mod-3 sigmas. Specifically:
# n ≡ 2 mod 6 means n even AND n ≡ 2 mod 3.
# n ≡ 4 mod 6 means n even AND n ≡ 1 mod 3.

# So sigma_2 (mod 6) = sum over n with n=2k, k ≡ 1 mod 3.
#    sigma_4 (mod 6) = sum over n with n=2k, k ≡ 2 mod 3.

# Hmm wait: 2 mod 6 -> n=2, then n/2 = 1, 1 mod 3 = 1. So sigma_2 (mod 6) corresponds to k ≡ 1 mod 3.
# 4 mod 6 -> n=4, n/2 = 2, 2 mod 3 = 2. So sigma_4 (mod 6) corresponds to k ≡ 2 mod 3.

# Good. So:
# sigma_2^(6) = 2^{-s} * sigma_1^(3)
# sigma_4^(6) = 2^{-s} * sigma_2^(3)

# And zeta(s)(1-3^{-s}) = sigma_1^(3) + sigma_2^(3) = 2^s (sigma_2^(6) + sigma_4^(6))

# Hmm let me double-check that.
print(f"\nVerifying: sigma_1^(3) + sigma_2^(3) vs zeta(s)(1-b):")
total_3 = sigma1_3 + sigma2_3
formula_3 = mp.zeta(s) * (1 - b)
print(f"  sigma_1^(3) + sigma_2^(3) = {total_3}")
print(f"  zeta(s)(1-b) = {formula_3}")
print(f"  diff = {total_3 - formula_3}")

# Also: sigma_2^(6) + sigma_4^(6) = 2^{-s} (sigma_1^(3) + sigma_2^(3)) = 2^{-s} zeta(s)(1-b)
total_24 = sigma[2] + sigma[4]
formula_24 = a * (1 - b) * mp.zeta(s)
print(f"\nVerifying: sigma_2 + sigma_4 vs a*zeta(s)(1-b):")
print(f"  sigma_2 + sigma_4 = {total_24}")
print(f"  a*zeta(s)(1-b) = {formula_24}")
print(f"  diff = {total_24 - formula_24}")
