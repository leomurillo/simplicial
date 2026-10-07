"""
Confirm the q-pieces tile (-inf, -5] with no gaps/overlaps, so Region A is fully covered.
Piece for prime p_k (k>=1, p_k>=3): B in [ -(p_k+p_{k+1}), -(p_{k-1}+p_k) ].
Upper end of piece k = -(p_{k-1}+p_k) = lower end of piece k-1. So consecutive pieces share endpoints.
Piece k=1 (p=3): B in [-(3+5),-(2+3)] = [-8,-5]. Upper end -5 matches Region A boundary.
As k->inf, lower end -(p_k+p_{k+1}) -> -inf. So union of pieces k>=1 = (-inf, -5]. Verify endpoints chain.
"""
from sympy import primerange
P=list(primerange(2,2000))
prev_lower=None
ok=True
for k in range(1,30):
    pk=P[k]
    lower=-(P[k]+P[k+1])   # lower B end
    upper=-(P[k-1]+P[k])   # upper B end
    if k==1:
        chain = (upper==-5)
    else:
        chain = (upper==prev_lower)   # this piece's upper == previous piece's lower
    if not chain: ok=False
    if k<=8:
        print(f"  k={k} (p={pk}): B in [{lower}, {upper}]   chain-ok={chain}")
    prev_lower=lower
print("...")
print("Pieces chain with shared endpoints, k=1 upper = -5:", ok)
print("Union of pieces k>=1 = (-inf, -5].  Region A fully tiled. (q=2 piece is (-5,+inf)=Region B.)")
