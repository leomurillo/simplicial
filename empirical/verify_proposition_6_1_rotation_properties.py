import numpy as np

# =============================================================================
# Empirical Skeptical Validation Script
# Target: Proposition 6.1 (Nine structural properties of simplicial rotation)
# =============================================================================

def generate_random_zero_sum_vector():
    """Generates a random 4D vector P in the zero-sum hyperplane H."""
    v = np.random.randn(4)
    return v - v.mean()

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

def generate_random_rotation():
    """Generates a random rotation matrix R on the zero-sum hyperplane H via projection."""
    A = np.random.randn(4, 4)
    S = A - A.T
    P = np.eye(4) - 0.25 * np.ones((4, 4))
    K = P @ S @ P
    norm = np.linalg.norm(K, ord=2)
    if norm > 0:
        K = K / norm
    theta = np.random.uniform(0, 2 * np.pi)
    R = np.eye(4) + np.sin(theta) * K + (1 - np.cos(theta)) * (K @ K)
    return R

def generate_random_rotation_via_Ku():
    """
    Generates a random rotation matrix R using the explicit Definition 3.1 K(u).
    Returns (R, u, theta) to expose the parameters for trace and spectrum tests.
    """
    u = generate_random_zero_sum_vector()
    # Normalize to simplicial unit length: (4/3) * sum(u_i^2) = 1 => sum(u_i^2) = 3/4
    u = u / np.sqrt((4/3) * np.sum(u**2))
    
    K = build_K_u(u)
    theta = np.random.uniform(0, 2 * np.pi)
    R = np.eye(4) + np.sin(theta) * K + (1 - np.cos(theta)) * (K @ K)
    
    return R, u, theta

def preflight_checks():
    """Asserts foundational properties of K(u) and generated R to anchor Proposition 6.1."""
    u = generate_random_zero_sum_vector()
    u = u / np.sqrt((4/3) * np.sum(u**2))
    K = build_K_u(u)
    
    assert np.allclose(K @ np.ones(4), 0, atol=1e-12), "K1=0 failed"
    assert np.allclose(K.T, -K, atol=1e-12), "K^T=-K failed"
    assert np.allclose(K @ K @ K, -K, atol=1e-12), "K^3=-K failed"
    
    R = generate_random_rotation()
    assert np.allclose(R @ np.ones(4), np.ones(4), atol=1e-12), "R1=1 failed"
    assert np.allclose(R.T @ R, np.eye(4), atol=1e-12), "R^TR=I failed"
    assert np.allclose(np.linalg.det(R), 1.0, atol=1e-12), "det(R)=1 failed"

def test_p1_orthogonality(num_trials=10000):
    """(P1 Orthogonality) R^T R = I. Corresponds to Proposition 6.1, item 1."""
    max_err = 0.0
    for _ in range(num_trials):
        R = generate_random_rotation()
        err = np.max(np.abs(R.T @ R - np.eye(4)))
        max_err = max(max_err, err)
    return max_err < 1e-12, max_err

def test_p2_row_sums(num_trials=10000):
    """(P2 Gauge fixation) R1 = 1. Corresponds to Proposition 6.1, item 2."""
    max_err = 0.0
    for _ in range(num_trials):
        R = generate_random_rotation()
        err = np.max(np.abs(R @ np.ones(4) - np.ones(4)))
        max_err = max(max_err, err)
    return max_err < 1e-12, max_err

def test_p3_col_sums(num_trials=10000):
    """(P3 Column sums) R^T 1 = 1. Corresponds to Proposition 6.1, item 3."""
    max_err = 0.0
    for _ in range(num_trials):
        R = generate_random_rotation()
        err = np.max(np.abs(R.T @ np.ones(4) - np.ones(4)))
        max_err = max(max_err, err)
    return max_err < 1e-12, max_err

def test_p4_determinant(num_trials=10000):
    """(P4 Determinant) det R = +1. Corresponds to Proposition 6.1, item 4."""
    max_err = 0.0
    for _ in range(num_trials):
        R = generate_random_rotation()
        err = np.abs(np.linalg.det(R) - 1.0)
        max_err = max(max_err, err)
    return max_err < 1e-12, max_err

def test_p5_trace(num_trials=10000):
    """(P5 Trace) tr(R) = 2 + 2cos(theta). Corresponds to Proposition 6.1, item 5."""
    max_err = 0.0
    for _ in range(num_trials):
        R, _, theta = generate_random_rotation_via_Ku()
        expected_trace = 2 + 2 * np.cos(theta)
        err = np.abs(np.trace(R) - expected_trace)
        max_err = max(max_err, err)
    return max_err < 1e-12, max_err

def test_p6_hyperplane_preservation(num_trials=10000):
    """(P6 Hyperplane preservation) P in H => RP in H. Corresponds to Proposition 6.1, item 6."""
    max_err = 0.0
    for _ in range(num_trials):
        R = generate_random_rotation()
        P = generate_random_zero_sum_vector()
        err = np.abs(np.sum(R @ P))
        max_err = max(max_err, err)
    return max_err < 1e-12, max_err

def test_p7_gauge_equivariance(num_trials=10000):
    """(P7 Gauge-equivariance) R(P + k1) = RP + k1. Corresponds to Proposition 6.1, item 7."""
    max_err = 0.0
    for _ in range(num_trials):
        R = generate_random_rotation()
        P = np.random.randn(4)
        k = np.random.randn()
        left = R @ (P + k * np.ones(4))
        right = (R @ P) + k * np.ones(4)
        err = np.max(np.abs(left - right))
        max_err = max(max_err, err)
    return max_err < 1e-12, max_err

def test_p8_metric_preservation(num_trials=10000):
    """(P8 Metric preservation) <RP, RQ>_s = <P, Q>_s and R^T G R = G. Corresponds to Proposition 6.1, item 8."""
    max_err = 0.0
    G = (4/3) * np.eye(4) - (1/3) * np.ones((4, 4))
    for _ in range(num_trials):
        R = generate_random_rotation()
        P = np.random.randn(4)
        Q = np.random.randn(4)
        
        # Inner product form
        ip_left = (R @ P).T @ G @ (R @ Q)
        ip_right = P.T @ G @ Q
        err_ip = np.abs(ip_left - ip_right)
        
        # Matrix form
        err_mat = np.max(np.abs(R.T @ G @ R - G))
        
        max_err = max(max_err, err_ip, err_mat)
    return max_err < 1e-12, max_err

def test_p9_spectrum(num_trials=10000):
    """(P9 Spectrum) Eigenvalues {1, 1, e^{i theta}, e^{-i theta}} and eigenspace. Corresponds to Proposition 6.1, item 9."""
    max_err = 0.0
    for _ in range(num_trials):
        R, u, theta = generate_random_rotation_via_Ku()
        
        # Eigenvalues
        eigvals = np.linalg.eigvals(R)
        expected_eigvals = np.array([1.0, 1.0, np.exp(1j * theta), np.exp(-1j * theta)])
        
        # Sort by real part then imaginary part to match them up
        # A more robust way: compute distance matrix and find min matching, but for 4 elements sorting by angle is easy
        def sort_key(z):
            # Sort by distance to 1, then by imaginary part
            return (abs(z - 1.0), np.imag(z))
            
        sorted_eigvals = sorted(eigvals, key=sort_key)
        sorted_expected = sorted(expected_eigvals, key=sort_key)
        
        err_eig = np.max(np.abs(np.array(sorted_eigvals) - np.array(sorted_expected)))
        
        # Eigenspace for lambda = 1
        err_u = np.max(np.abs(R @ u - u))
        err_1 = np.max(np.abs(R @ np.ones(4) - np.ones(4)))
        
        # Rank of R - I should be 2 (nullity 2)
        rank_R_minus_I = np.linalg.matrix_rank(R - np.eye(4), tol=1e-10)
        err_rank = abs(rank_R_minus_I - 2)
        
        max_err = max(max_err, err_eig, err_u, err_1, err_rank)
        
    return max_err < 1e-12, max_err

def test_p5_prime_deterministic():
    """(P5' Appendix D) Deterministic check with exact u and theta. Corresponds to Appendix D."""
    a = np.sqrt(3) / 4
    u = np.array([a, a, -a, -a])
    theta = 2 * np.pi / 3
    
    K = build_K_u(u)
    R = np.eye(4) + np.sin(theta) * K + (1 - np.cos(theta)) * (K @ K)
    
    G = (4/3) * np.eye(4) - (1/3) * np.ones((4, 4))
    
    errs = []
    errs.append(np.max(np.abs(R.T @ R - np.eye(4)))) # P1
    errs.append(np.max(np.abs(R @ np.ones(4) - np.ones(4)))) # P2
    errs.append(np.max(np.abs(R.T @ np.ones(4) - np.ones(4)))) # P3
    errs.append(np.abs(np.linalg.det(R) - 1.0)) # P4
    errs.append(np.abs(np.trace(R) - (2 + 2 * np.cos(theta)))) # P5
    
    P = np.array([1/2, -3/2, -1/2, 3/2]) # zero-sum
    errs.append(np.abs(np.sum(R @ P))) # P6
    
    k = 2.5
    errs.append(np.max(np.abs(R @ (P + k * np.ones(4)) - ((R @ P) + k * np.ones(4))))) # P7
    
    errs.append(np.max(np.abs(R.T @ G @ R - G))) # P8
    
    eigvals = np.linalg.eigvals(R)
    def sort_key(z): return (abs(z - 1.0), np.imag(z))
    expected_eigvals = np.array([1.0, 1.0, np.exp(1j * theta), np.exp(-1j * theta)])
    errs.append(np.max(np.abs(np.array(sorted(eigvals, key=sort_key)) - np.array(sorted(expected_eigvals, key=sort_key))))) # P9
    
    max_err = max(errs)
    return max_err < 1e-14, max_err

if __name__ == "__main__":
    np.random.seed(42)
    print("Running preflight checks...")
    preflight_checks()
    print("Preflight checks passed.\n")
    
    print("Testing Proposition 6.1 Properties (10,000 trials each)...")
    results = []
    tests = [
        ("P1 (Orthogonality)", test_p1_orthogonality),
        ("P2 (Row sums = 1)", test_p2_row_sums),
        ("P3 (Col sums = 1)", test_p3_col_sums),
        ("P4 (Determinant = +1)", test_p4_determinant),
        ("P5 (Trace)", test_p5_trace),
        ("P6 (Hyperplane pres.)", test_p6_hyperplane_preservation),
        ("P7 (Gauge-equivariance)", test_p7_gauge_equivariance),
        ("P8 (Metric preservation)", test_p8_metric_preservation),
        ("P9 (Spectrum)", test_p9_spectrum),
        ("P5' (Appendix D det.)", test_p5_prime_deterministic)
    ]
    
    for name, func in tests:
        if name == "P5' (Appendix D det.)":
            passed, err = func()
        else:
            passed, err = func(10000)
        results.append((name, passed, err))
        
    print("\n=============================================================================")
    print(f"{'PROPERTY':<25} | {'STATUS':<6} | {'MAX ERROR'}")
    print("=============================================================================")
    for name, passed, err in results:
        status = "PASS" if passed else "FAIL"
        print(f"{name:<25} | {status:<6} | {err:.5e}")
    print("=============================================================================")
