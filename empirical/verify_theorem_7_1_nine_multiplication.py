import numpy as np
import sympy as sp

# =============================================================================
# Empirical Skeptical Validation Script
# Target: Theorem 7.1 (9-multiplication kernel) from simplicial_vector_calculus.md
# =============================================================================

def generate_random_zero_sum_vector():
    """Generates a random 4D vector P in the zero-sum hyperplane H."""
    v = np.random.randn(4)
    return v - v.mean()

def generate_random_rotation():
    """Generates a random rotation matrix R on the zero-sum hyperplane H."""
    # Generate random skew-symmetric matrix
    A = np.random.randn(4, 4)
    S = A - A.T
    # Project onto zero-sum hyperplane
    P = np.eye(4) - 0.25 * np.ones((4, 4))
    K = P @ S @ P
    
    # Normalize K so it acts like a valid generator
    norm = np.linalg.norm(K, ord=2)
    if norm > 0:
        K = K / norm
        
    theta = np.random.uniform(0, 2 * np.pi)
    # Rodrigues formula for the zero-sum subspace
    R = np.eye(4) + np.sin(theta) * K + (1 - np.cos(theta)) * (K @ K)
    
    assert np.allclose(R @ np.ones(4), np.ones(4), atol=1e-12, rtol=1e-12)
    assert np.allclose(R.T @ R, np.eye(4), atol=1e-12, rtol=1e-12)
    assert np.allclose(np.linalg.det(R), 1.0, atol=1e-12, rtol=1e-12)
    
    return R

def build_K_u(u):
    """Builds the intrinsic cross product matrix K(u) from Definition 3.1."""
    ul, un, um, up = u
    K_tilde = np.array([
        [0, um - up, up - un, un - um],
        [up - um, 0, ul - up, um - ul],
        [un - up, up - ul, 0, ul - un],
        [um - un, ul - um, un - ul, 0]
    ])
    return K_tilde / np.sqrt(3)

def generate_random_rotation_via_Ku():
    """
    Generates a random rotation matrix R using the explicit Definition 3.1 K(u).
    """
    u = generate_random_zero_sum_vector()
    # Normalize to simplicial unit length: (4/3) * sum(u_i^2) = 1 => sum(u_i^2) = 3/4
    u = u / np.sqrt((4/3) * np.sum(u**2))
    
    K = build_K_u(u)
    theta = np.random.uniform(0, 2 * np.pi)
    R = np.eye(4) + np.sin(theta) * K + (1 - np.cos(theta)) * (K @ K)
    
    assert np.allclose(R @ np.ones(4), np.ones(4), atol=1e-12, rtol=1e-12)
    assert np.allclose(R.T @ R, np.eye(4), atol=1e-12, rtol=1e-12)
    assert np.allclose(np.linalg.det(R), 1.0, atol=1e-12, rtol=1e-12)
    
    return R

def test_1_identity(num_trials=100000):
    """
    Hypothesis 1: Identity of reduced apply and full apply.
    For random zero-sum inputs P in H, verify that the 9-mul kernel equals the full apply RP.
    """
    print("\n--- Testing Hypothesis 1: Identity of reduced apply and full apply ---")
    max_error = 0.0
    for _ in range(num_trials):
        R = generate_random_rotation()
        P = generate_random_zero_sum_vector()
        
        # Full apply
        RP_full = R @ P
        
        # Reduced apply (absorbing index 3, i.e., the 4th component)
        R_tilde = R[:3, :3] - R[:3, 3:4]
        
        P_reduced = P[:3]
        RP_reduced_3 = R_tilde @ P_reduced
        
        # Recover 4th component
        RP_reduced_4 = -np.sum(RP_reduced_3)
        RP_reduced = np.append(RP_reduced_3, RP_reduced_4)
        
        error = np.max(np.abs(RP_full - RP_reduced))
        if error > max_error:
            max_error = error
            
    print(f"Max absolute error over {num_trials} trials: {max_error:.5e}")
    passed = max_error < 1e-12
    print(f"Verdict: {'PASS' if passed else 'FAIL'}")
    return passed, max_error

def test_1b_identity_via_Ku(num_trials=10000):
    """
    Hypothesis 1b: Identity of reduced apply and full apply, using explicit K(u) generator.
    """
    print("\n--- Testing Hypothesis 1b: Identity via explicit K(u) generator ---")
    max_error = 0.0
    for _ in range(num_trials):
        R = generate_random_rotation_via_Ku()
        P = generate_random_zero_sum_vector()
        
        # Full apply
        RP_full = R @ P
        
        # Reduced apply
        R_tilde = R[:3, :3] - R[:3, 3:4]
        
        P_reduced = P[:3]
        RP_reduced_3 = R_tilde @ P_reduced
        
        # Recover 4th component
        RP_reduced_4 = -np.sum(RP_reduced_3)
        RP_reduced = np.append(RP_reduced_3, RP_reduced_4)
        
        error = np.max(np.abs(RP_full - RP_reduced))
        if error > max_error:
            max_error = error
            
    print(f"Max absolute error over {num_trials} trials: {max_error:.5e}")
    passed = max_error < 1e-12
    print(f"Verdict: {'PASS' if passed else 'FAIL'}")
    return passed, max_error

def test_2_and_3_symbolic_count():
    """
    Hypothesis 2: Multiplication-count certification.
    Hypothesis 3: Independence from theta, u.
    Symbolically count the number of multiplication operations in the 9-mul kernel.
    Using sp.MatrixSymbol makes the 9-count a structural property of the matrix-vector product tree, independent of any specific (u, theta) substitution.
    """
    print("\n--- Testing Hypothesis 2 & 3: Symbolic Multiplication Count & Independence ---")
    
    # Create symbolic 3x3 reduced matrix R_tilde and 3x1 vector P
    R_tilde = sp.MatrixSymbol('R_tilde', 3, 3)
    P = sp.MatrixSymbol('P', 3, 1)
    
    # Perform the reduced multiplication
    RP_reduced = sp.Matrix(R_tilde) * sp.Matrix(P)
    
    # Let's do a stricter count: multiplications between R_tilde and P elements
    strict_muls = 0
    for i in range(3):
        expr = sp.expand(RP_reduced[i])
        # Each term in the expanded sum should be a single multiplication of R_tilde[i,j] * P[j]
        strict_muls += len(expr.args) if isinstance(expr, sp.Add) else 1
        
    print(f"Strict scalar multiplications (R_tilde elements * P elements): {strict_muls}")
    
    # For the 4th component, we just sum the results of the first 3, so 0 new multiplications
    print(f"New multiplications for 4th component recovery: 0 (by definition: -(y1+y2+y3))")
    
    passed = (strict_muls == 9)
    print(f"Verdict: {'PASS' if passed else 'FAIL'}")
    return passed, strict_muls

def test_4_worked_example():
    """
    Hypothesis 4: Worked example sanity check.
    For a specific u, theta, and P, confirm the 9-mul kernel matches the full matrix-vector product.
    """
    print("\n--- Testing Hypothesis 4: Worked example sanity check ---")
    
    a = np.sqrt(3) / 4
    u = np.array([a, a, -a, -a])
    theta = 2 * np.pi / 3
    P = np.array([1/2, -3/2, -1/2, 3/2])
    expected_P_prime = np.array([(np.sqrt(3) - 2) / 2, -np.sqrt(3) / 2, (np.sqrt(3) + 2) / 2, -np.sqrt(3) / 2])
    
    # 1. Build K = K(u) explicitly via Definition 3.1
    K = build_K_u(u)
    
    # 2. Assert on K
    assert np.allclose(K @ np.ones(4), 0, atol=1e-14, rtol=1e-14)
    assert np.allclose(K.T, -K, atol=1e-14, rtol=1e-14)
    assert np.allclose(K @ K @ K, -K, atol=1e-14, rtol=1e-14)
    
    # 3. Assert paper's normalization holds
    G = (4/3) * np.eye(4) - (1/3) * np.ones((4, 4))
    assert np.allclose(u.T @ G @ u, 1.0, atol=1e-14, rtol=1e-14)
    
    # 4. Form R
    R = np.eye(4) + np.sin(theta) * K + (1 - np.cos(theta)) * (K @ K)
    
    # 5. Apply R to P and compare
    RP_full = R @ P
    error_full = np.max(np.abs(RP_full - expected_P_prime))
    print(f"Max absolute error for full apply vs expected: {error_full:.5e}")
    assert error_full < 1e-12
    
    # 6. Apply 9-mul reduced kernel
    R_tilde = R[:3, :3] - R[:3, 3:4]
    RP_reduced_3 = R_tilde @ P[:3]
    RP_reduced_4 = -np.sum(RP_reduced_3)
    RP_reduced = np.append(RP_reduced_3, RP_reduced_4)
    
    error_reduced = np.max(np.abs(RP_reduced - RP_full))
    print(f"Max absolute error for reduced apply vs full apply: {error_reduced:.5e}")
    
    passed = error_reduced < 1e-12 and error_full < 1e-12
    print(f"Verdict: {'PASS' if passed else 'FAIL'}")
    return passed, max(error_reduced, error_full)

def test_5_non_zero_sum():
    """
    Hypothesis 5: Non-zero-sum input sanity (negative test).
    Confirm that for a generic non-zero-sum input P, the 9-mul kernel output disagrees with RP.
    """
    print("\n--- Testing Hypothesis 5: Non-zero-sum input sanity (negative test) ---")
    R = generate_random_rotation()
    # Generate non-zero-sum P
    P = np.random.randn(4)
        
    # Full apply
    RP_full = R @ P
    
    # Reduced apply
    R_tilde = R[:3, :3] - R[:3, 3:4]
            
    RP_reduced_3 = R_tilde @ P[:3]
    RP_reduced_4 = -np.sum(RP_reduced_3)
    RP_reduced = np.append(RP_reduced_3, RP_reduced_4)
    
    # Check predicted disagreement structure
    # For P not in H, the 9-mul kernel assumes P_p = -(P_1 + P_2 + P_3).
    # The true RP_i = sum_{j=1}^4 R_ij P_j
    # The kernel RP_i = sum_{j=1}^3 R_ij P_j - R_i4 (P_1 + P_2 + P_3)
    # Difference: RP_i - kernel_i(P) = R_i4 P_4 + R_i4 (P_1 + P_2 + P_3) = R_i4 * sum(P_k)
    
    sum_P = np.sum(P)
    predicted_diff_3 = R[:3, 3] * sum_P
    actual_diff_3 = RP_full[:3] - RP_reduced[:3]
    
    diff_error = np.max(np.abs(actual_diff_3 - predicted_diff_3))
    print(f"Max absolute error between actual and predicted disagreement: {diff_error:.5e}")
    
    passed = diff_error < 1e-12
    print(f"Verdict: {'PASS' if passed else 'FAIL'} (Disagreement matches prediction)")
    return passed, diff_error

def test_6_absorbed_index_invariance(num_trials=10000):
    """
    Hypothesis 6: Absorbed-index invariance.
    Absorb any of the four indices and build the corresponding reduced kernel.
    Confirm all four variants give the same RP.
    """
    print("\n--- Testing Hypothesis 6: Absorbed-index invariance ---")
    max_error = 0.0
    for _ in range(num_trials):
        R = generate_random_rotation()
        P = generate_random_zero_sum_vector()
        
        RP_full = R @ P
        
        for k in range(4): # Absorb index k
            # Indices to keep
            indices = [i for i in range(4) if i != k]
            
            # Build reduced matrix using slicing
            R_keep = R[indices, :]
            R_tilde = R_keep[:, indices] - R_keep[:, [k]]
                    
            # Reduced apply
            P_reduced = P[indices]
            RP_reduced_3 = R_tilde @ P_reduced
            
            # Recover k-th component
            RP_reduced_k = -np.sum(RP_reduced_3)
            
            # Reconstruct full vector
            RP_reduced = np.zeros(4)
            RP_reduced[indices] = RP_reduced_3
            RP_reduced[k] = RP_reduced_k
            
            error = np.max(np.abs(RP_full - RP_reduced))
            if error > max_error:
                max_error = error
                
    print(f"Max absolute error over {num_trials} trials across all absorbed indices: {max_error:.5e}")
    passed = max_error < 1e-12
    print(f"Verdict: {'PASS' if passed else 'FAIL'}")
    return passed, max_error

if __name__ == "__main__":
    np.random.seed(42)
    print("Starting Empirical Skeptical Validation for Theorem 7.1...")
    
    p1, e1 = test_1_identity()
    p1b, e1b = test_1b_identity_via_Ku()
    p23, c23 = test_2_and_3_symbolic_count()
    p4, e4 = test_4_worked_example()
    p5, e5 = test_5_non_zero_sum()
    p6, e6 = test_6_absorbed_index_invariance()
    
    print("\n=============================================================================")
    print("SUMMARY OF RESULTS")
    print("=============================================================================")
    print(f"H1 (Identity):          {'PASS' if p1 else 'FAIL'} (Max Error: {e1:.5e})")
    print(f"H1b (Identity Ku):      {'PASS' if p1b else 'FAIL'} (Max Error: {e1b:.5e})")
    print(f"H2 & H3 (Symbolic):     {'PASS' if p23 else 'FAIL'} (Mul Count: {c23})")
    print(f"H4 (Worked Example):    {'PASS' if p4 else 'FAIL'} (Max Error: {e4:.5e})")
    print(f"H5 (Non-zero-sum):      {'PASS' if p5 else 'FAIL'} (Disagreement Error: {e5:.5e})")
    print(f"H6 (Absorbed Index):    {'PASS' if p6 else 'FAIL'} (Max Error: {e6:.5e})")
    print("=============================================================================")
