"""Full PSD (ALL principal minors) on power candidates.
Leading minors of p^16 stay + until N=16. Does a NON-LEADING principal
minor go negative earlier? Berg-Szwarc: leading>=0 is necessary-not-sufficient."""
from search import bn
from sympy import primerange, Matrix, Integer
import itertools

P = list(primerange(2, 100000))

def fpow(r, d):
    def f(p):
        return (Integer(p)+r)**d
    return f

def full_psd_first_neg(f, size):
    """First negative principal minor of (size+1)x(size+1) Hankel (any subset)."""
    b = bn(f, 2*size+2)
    H = Matrix(size+1, size+1, lambda i, j: b[i+j])
    idx = list(range(size+1))
    for k in range(1, size+2):
        for sub in itertools.combinations(idx, k):
            sub = list(sub)
            d = H[sub, sub].det()
            if d < 0:
                return (k, tuple(sub), '-')
    return None

# p^16: leading first-neg at 16. Check full PSD up to size 16 (feasible? 2^17 subsets ~ 131k,
# but determinants of large submatrices are heavy). Do size up to 13 first.
for d in [10, 16, 20]:
    f = fpow(0, d)
    for size in [11, 12, 13]:
        r = full_psd_first_neg(f, size)
        print(f"p^{d}, full PSD size {size}: first neg minor = {r}")
        if r is not None:
            break
