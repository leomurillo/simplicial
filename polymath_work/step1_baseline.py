from sympy import primerange, Matrix, Integer, symbols, factor, Rational
import itertools

P = list(primerange(2, 2000))  # plenty of primes

def bn(f, L):
    """b_0..b_{L-1}: b_0=1, b_n = prod_{i=1}^n f(p_i)."""
    b = [Integer(1)]
    a = Integer(1)
    for i in range(1, L):
        a *= f(P[i-1])
        b.append(a)
    return b

def D(f, N):
    """Leading Hankel determinant D_N = det(b_{i+j})_{0<=i,j<=N}."""
    b = bn(f, 2*N+2)
    return Matrix(N+1, N+1, lambda i, j: b[i+j]).det()

# Reproduce established facts
print("=== Reproduce established facts ===")
print("D(p, 3) =", D(lambda p: p, 3), " (expect -787680)")
print("D(p, 1) =", D(lambda p: p, 1))
print("D(p, 2) =", D(lambda p: p, 2))

# n! control via c_i = i (NOT primes): ratio sequence c_i=i -> b_n = n!
# Here we feed an index-based "f" -- but our bn uses f(P[i-1]); to get c_i=i we cheat:
def make_ratio(cseq):
    # returns f-like callable mapping the i-th prime to cseq[i]
    idx = {P[i]: cseq[i] for i in range(len(cseq))}
    return lambda p: idx[p]

# n! : c_i = i  => b_n = n!
cfact = [Integer(i+1) for i in range(40)]  # c_1=1? careful: c_i used as f(p_i). b_n=prod c_i
# Actually b_n = prod_{i=1}^n c_i. For n! we want c_i = i, i.e. c_1=1,c_2=2,...
cfact = [Integer(i) for i in range(1, 40)]
fctrl = make_ratio(cfact)
print("\nn! control (c_i=i): b_n =", [bn(fctrl, 6)[k] for k in range(6)], "(expect 1,1,2,6,24,120)")
for N in range(1, 6):
    print(f"  D_{N}(n!) =", D(fctrl, N))

print("\n=== Degree 1 monic f(p)=p+c symbolic ===")
c = symbols('c')
def fc(cc):
    return lambda p: p + cc
print("D_1 =", factor(D(fc(c), 1)))
print("D_2 =", factor(D(fc(c), 2)))
print("D_3 =", factor(D(fc(c), 3)))
