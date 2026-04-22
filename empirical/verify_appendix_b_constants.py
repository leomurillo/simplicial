import sympy as sp
import numpy as np

def verify():
    u_1, u_2, u_3, u_4 = sp.symbols('u_1 u_2 u_3 u_4', real=True)

    K_tilde = sp.Matrix([
        [0, u_3 - u_4, u_4 - u_2, u_2 - u_3],
        [u_4 - u_3, 0, u_1 - u_4, u_3 - u_1],
        [u_2 - u_4, u_4 - u_1, 0, u_1 - u_2],
        [u_3 - u_2, u_1 - u_3, u_2 - u_1, 0]
    ])

    print("--- Symbolic Analysis ---")

    S_raw = sum(K_tilde[i, j]**2 for i in range(4) for j in range(4))

    # Zero-sum constraint: u_4 = -u_1 - u_2 - u_3
    zero_sum_sub = {u_4: -u_1 - u_2 - u_3}
    S_sub = S_raw.subs(zero_sum_sub).expand()

    u_sq_sum = (u_1**2 + u_2**2 + u_3**2 + u_4**2).subs(zero_sum_sub).expand()
    
    print(f"S simplified under zero-sum constraint: {S_sub}")
    print(f"8 * sum(u_i^2) under zero-sum constraint: {sp.expand(8 * u_sq_sum)}")
    print(f"6 * sum(u_i^2) under zero-sum constraint: {sp.expand(6 * u_sq_sum)}")
    
    diff_8 = sp.simplify(S_sub - 8 * u_sq_sum)
    diff_6 = sp.simplify(S_sub - 6 * u_sq_sum)
    
    if diff_8 == 0:
        print("\nCONCLUSION (i): The sum of squares is 8 * sum(u_i^2), NOT 6 * sum(u_i^2).")
    elif diff_6 == 0:
        print("\nCONCLUSION (i): The sum of squares is 6 * sum(u_i^2).")
    else:
        print("\nCONCLUSION (i): Neither 6 nor 8 match exactly.")
        
    # 5. Compute tr(K_tilde^2)
    K_tilde_sq = K_tilde * K_tilde
    tr_K_tilde_sq = K_tilde_sq.trace().subs(zero_sum_sub).expand()
    print(f"\ntr(K_tilde^2): {tr_K_tilde_sq}")
    print(f"-S: {-S_sub}")
    if sp.simplify(tr_K_tilde_sq - (-S_sub)) == 0:
        print("CONCLUSION (ii): tr(K_tilde^2) = -S is confirmed.")
        
    # 6. Characteristic polynomial of K_tilde
    lambda_var = sp.symbols('lambda')
    char_poly = K_tilde.charpoly(lambda_var).as_expr().subs(zero_sum_sub).expand()
    print(f"\nCharacteristic polynomial of K_tilde (zero-sum): {char_poly}")
    
    c_term = char_poly.coeff(lambda_var, 2)
    print(f"Coefficient of lambda^2: {c_term}")
    if sp.simplify(c_term - 4 * u_sq_sum) == 0:
        print("Confirmed: The lambda^2 coefficient is EXACTLY 4 * sum(u_i^2).")
        
    # 7. Unit-axis condition
    print("\n--- Applying Unit-Axis Condition: sum(u_i^2) = 3/4 ---")
    sum_u2_val = 0.75
    S_val = 8 * sum_u2_val
    tr_K2_val = -S_val
    print(f"S = {S_val}")
    print(f"tr(K_tilde^2) = {tr_K2_val}")
    print(f"Eigenvalues of K_tilde = +/- i * sqrt(4 * 3/4) = +/- i * sqrt(3)")
    print(f"Minimal polynomial for K_tilde: x^3 + 3x = 0  =>  K_tilde^3 = -3 * K_tilde")
    print(f"c^2_unscaled = 3")
    
    print("\nFor scaled K = K_tilde / sqrt(3):")
    print("K^3 = (K_tilde / sqrt(3))^3 = K_tilde^3 / (3 * sqrt(3)) = (-3 * K_tilde) / (3 * sqrt(3)) = - K_tilde / sqrt(3) = -K")
    print("CONCLUSION: Scaled K^3 = -K is PRESERVED.")
    
    # 8. Numerical spot-check
    print("\n--- Numerical Spot-Check ---")
    # Base vector: (3, -1, -1, -1), zero sum.
    u_num_raw = np.array([3, -1, -1, -1], dtype=float)
    # We want sum(u_i^2) = 3/4
    # sum(u_num_raw^2) = 9 + 1 + 1 + 1 = 12
    # So we divide by sqrt(12) to get sum(u^2) = 1, then multiply by sqrt(3/4)
    # Factor = sqrt(3/4) / sqrt(12) = sqrt(3/48) = sqrt(1/16) = 1/4
    u_num = u_num_raw / 4.0
    
    print(f"u = {u_num}")
    print(f"sum(u) = {np.sum(u_num)}")
    print(f"sum(u^2) = {np.sum(u_num**2)} (expected 0.75)")
    
    K_tilde_num = np.array([
        [0, u_num[2] - u_num[3], u_num[3] - u_num[1], u_num[1] - u_num[2]],
        [u_num[3] - u_num[2], 0, u_num[0] - u_num[3], u_num[2] - u_num[0]],
        [u_num[1] - u_num[3], u_num[3] - u_num[0], 0, u_num[0] - u_num[1]],
        [u_num[2] - u_num[1], u_num[0] - u_num[2], u_num[1] - u_num[0], 0]
    ])
    
    K_tilde_3 = np.linalg.matrix_power(K_tilde_num, 3)
    diff_tilde = np.max(np.abs(K_tilde_3 + 3 * K_tilde_num))
    print(f"Max diff for K_tilde^3 + 3*K_tilde = 0: {diff_tilde}")
    
    K_num = K_tilde_num / np.sqrt(3)
    K_3 = np.linalg.matrix_power(K_num, 3)
    diff_K = np.max(np.abs(K_3 + K_num))
    print(f"Max diff for K^3 + K = 0: {diff_K}")

if __name__ == "__main__":
    verify()
