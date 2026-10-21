from fractions import Fraction as Fr
def signature(M):
    # exact inertia via symmetric Gaussian elimination with pivoting on rationals
    M = [[Fr(x) for x in r] for r in M]; n = len(M); pos = neg = 0
    while n:
        k = next((i for i in range(n) if M[i][i] != 0), None)
        if k is None:
            i, j = next(((i, j) for i in range(n) for j in range(n) if M[i][j] != 0), (None, None))
            if i is None: break
            for c in range(n): M[i][c] += M[j][c]
            for r in range(n): M[r][i] += M[r][j]
            continue
        d = M[k][k]; pos += d > 0; neg += d < 0
        M = [[M[r][c] - M[r][k] * M[k][c] / d for c in range(n) if c != k] for r in range(n) if r != k]; n -= 1
    return pos, neg
p = 101; a = -3; s = [2, a]
for n in range(2, 9): s.append(a * s[-1] - p * s[-2])
print([signature([[0, p**n+1-s[n], 1, 1], [p**n+1-s[n], 0, 1, p**n], [1, 1, 0, 1], [1, p**n, 1, 0]]) for n in range(1, 9)])
q = p; N = p + 1 + 3 * 20
print("control:", signature([[0, N, 1, 1], [N, 0, 1, q], [1, 1, 0, 1], [1, q, 1, 0]]))
