from sympy import primerange, Matrix, Integer, symbols, expand, Poly, simplify, factor, prod
import sympy as sp

# Build primes
P=list(primerange(2,2000000))

def bn(f,L):
    b=[Integer(1)]; a=Integer(1)
    for i in range(1,L):
        a=a*f(P[i-1]); b.append(a)
    return b

# 3x3 principal Hankel minor on {m,m+1,m+2}
# Hankel entry H[i][j] = b_{i+j}. Principal minor rows/cols {m,m+1,m+2}:
#   det Matrix(3,3, lambda i,j: b[(m+i)+(m+j)])
# Note indices go up to (m+2)+(m+2)=2m+4, so need b up to 2m+4.

def minor3(b,m):
    return Matrix(3,3, lambda i,j: b[(m+i)+(m+j)]).det()

# Test deg 1 (f=x) and deg 2,3 and confirm SIGN behavior for several m.
for d in [1,2,3]:
    f=lambda x,d=d: Integer(x)**d
    L=400
    b=bn(f,L)
    print(f"--- degree {d} ---")
    cnt_neg=0
    for m in range(2, 150):
        if 2*m+4 >= len(b): break
        val=minor3(b,m)
        s = '<0' if val<0 else ('>0' if val>0 else '=0')
        if val<0: cnt_neg+=1
        # which 4 primes does it see? entries b_{2m}..b_{2m+4}, ratios involve f(p) at indices
        # b_k = prod_{i=1}^{k} f(p_i)? Actually bn: b[0]=1, b[k]=prod_{i=1..k} f(P[i-1]) = f(p_1)...f(p_k)
        # minor uses b_{2m},...,b_{2m+4}; the c's that vary are f(p_{2m+1}),...,f(p_{2m+4})
        if m<12 or s=='<0':
            print(f"  m={m}: minor {s}  primes seen p_{{2m+1..2m+4}} = {P[2*m]},{P[2*m+1]},{P[2*m+2]},{P[2*m+3]}")
    print(f"  total negative in range: {cnt_neg}")
