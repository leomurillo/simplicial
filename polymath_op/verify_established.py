"""
Verify the ESTABLISHED results and compute Jacobi recurrence coefficients.
GPD discipline: exact arithmetic, paste the numbers.
"""
from sympy import primerange, Matrix, Integer, symbols, factor, Rational, simplify, expand

P = list(primerange(2, 2000))

def bn(f, L):
    """b_0=1, b_n = prod_{i=1}^n f(p_i)"""
    b = [Integer(1)]
    a = Integer(1)
    for i in range(1, L):
        a *= f(P[i-1])
        b.append(a)
    return b

def Hankel(b, N):
    """(N+1)x(N+1) Hankel matrix (b_{i+j})_{0<=i,j<=N}"""
    return Matrix(N+1, N+1, lambda i, j: b[i+j])

def D(f, N):
    b = bn(f, 2*N+2)
    return Hankel(b, N).det()

print("="*70)
print("RE-VERIFY ESTABLISHED RESULTS")
print("="*70)

# f(p)=p control
print("\n[1] f(p)=p :  D(.,3) should be -787680")
val = D(lambda p: p, 3)
print("    D_3 =", val)
print("    Hankel det signs D_0..D_4:")
for N in range(5):
    print(f"      D_{N} = {D(lambda p:p, N)}")

# n! control (c_i = i, i.e. ratios are 1,2,3,...): this is a genuine moment seq
print("\n[2] CONTROL c_i=i (=> b_n = n!): all D_N > 0 (Hamburger moment)")
def bn_ratio(cfun, L):
    b = [Integer(1)]; a = Integer(1)
    for i in range(1, L):
        a *= cfun(i); b.append(a)
    return b
def D_ratio(cfun, N):
    b = bn_ratio(cfun, 2*N+2)
    return Hankel(b, N).det()
for N in range(6):
    print(f"      D_{N} = {D_ratio(lambda i: Integer(i), N)}")

print("\n[3] CONTROL c_i = 2i-1 (odd numbers): should be moment (double factorial)")
for N in range(6):
    print(f"      D_{N} = {D_ratio(lambda i: Integer(2*i-1), N)}")

print("="*70)
print("DEGREE 1 VERIFICATION (monic f(p)=p+c) -- symbolic")
print("="*70)
c = symbols('c', real=True)
def fc(p): return p + c
for N in [1,2,3]:
    b = bn(fc, 2*N+2)
    det = Hankel(b, N).det()
    print(f"\n  D_{N}(c) = {factor(det)}")
