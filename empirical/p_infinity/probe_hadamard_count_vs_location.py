"""
THE LAST TENSION: does the COUNT constrain the LOCATION through zeta being order-1 entire (the
Hadamard-product coupling)?

xi(s) is entire of order 1, so Hadamard couples the zeros: they determine the Li coefficients
   lambda_n = sum_rho [1 - (1 - 1/rho)^n].
RH <=> lambda_n >= 0 for all n (Li's criterion).  The question: the order-1 structure fixes the GROWTH
of lambda_n (the count / Gamma-factor) -- does it thereby pin the real parts (the location)?

The decisive object is the per-zero Li factor  R(rho) = |1 - 1/rho| = |rho-1|/|rho|:
   R = 1  <=>  Re(rho) = 1/2   (ON the line);   R > 1  <=>  Re(rho) < 1/2;   R < 1  <=>  Re(rho) > 1/2.
So:
   ON-line zeros contribute |1-1/rho|^n = 1^n -- BOUNDED; their sum gives the POLYNOMIAL drift
        d_n ~ (n/2)(log(n/2pi) - 1 + euler_gamma)   = the COUNT / archimedean Gamma-factor.
   OFF-line zeros contribute R^n with R>1 -- EXPONENTIAL; an excursion the polynomial drift cannot hold.

We show: COUNT (polynomial drift) and LOCATION (exponential excursion) live on DIFFERENT SCALES, so the
order-1 coupling CANNOT force the location.  Davenport-Heilbronn (order 1, same drift, off-line zeros) is
the witness; the Euler product is the separator.

No torch. mpmath. Deterministic.
"""
import mpmath as mp
mp.mp.dps = 30
EG = mp.euler

def R(beta, gamma):                       # the Li factor modulus |1 - 1/rho|
    rho = mp.mpf(beta) + 1j*mp.mpf(gamma)
    return abs(rho - 1)/abs(rho)
def drift(n):                             # archimedean main term of lambda_n (the COUNT / Gamma-factor)
    n = mp.mpf(n)
    return (n/2)*(mp.log(n/(2*mp.pi)) - 1 + EG) + mp.mpf(3)/4

print("=" * 90)
print("Does order-1 Hadamard let the COUNT pin the LOCATION?  R(rho)=|1-1/rho|, =1 iff on the line")
print("=" * 90)

print("\nA. the per-zero Li factor R: =1 on the line, >1 below it (off-line rate R-1 ~ delta/gamma^2):")
print(f"   {'Re(rho)=beta':>13} {'gamma':>8} {'R=|1-1/rho|':>14} {'R-1':>14} {'~ delta/gamma^2':>16}")
for beta, gamma in [(0.5, 14.13), (0.4, 14.13), (0.4, 50), (0.4, 100), (0.3, 14.13)]:
    r = R(beta, gamma); delta = mp.mpf('0.5') - beta
    approx = delta/gamma**2 if delta != 0 else mp.mpf(0)
    print(f"   {beta:>13} {gamma:>8} {mp.nstr(r,10):>14} {mp.nstr(r-1,5):>14} {mp.nstr(approx,5):>16}")
print("   => on-line R=1 exactly (no growth); off-line R>1 by ~ delta/gamma^2 (small for high zeros).")

print("\nB. COUNT (polynomial drift d_n) vs LOCATION (off-line excursion R^n) -- different scales:")
print(f"   one off-line zero at beta=0.4, gamma=14.13:  R = {mp.nstr(R(0.4,14.13),8)}")
print(f"   {'n':>7} {'count drift d_n':>16} {'excursion R^n':>16} {'R^n / d_n':>14} {'excursion wins?':>16}")
r = R(0.4, 14.13)
for n in [10, 100, 1000, 5000, 20000, 100000]:
    dn = drift(n); Rn = r**n
    print(f"   {n:>7} {mp.nstr(dn,6):>16} {mp.nstr(Rn,6):>16} {mp.nstr(Rn/dn,5):>14} {str(Rn > dn):>16}")
# crossover scale n* where R^n ~ d_n  (real fixed-point iteration n <- log(d_n)/log R); exp always wins
lr = mp.log(r); nn = mp.mpf(1000)
for _ in range(60):
    nn = mp.log(drift(nn))/lr
print(f"   crossover n* (R^n = d_n) ~ {mp.nstr(nn,5)}   (a finite n*; beyond it R^n dominates forever)")
print("   => EXPONENTIAL R^n always overtakes the POLYNOMIAL drift d_n (here near n* ~ gamma^2/delta).")

print("\nC. the scale gap, made explicit:")
print("   COUNT    = polynomial drift d_n ~ (n/2)log(n/2pi)  -- fixed by order-1 + the Gamma-factor;")
print("              SHARED by Davenport-Heilbronn (also order 1, same density).")
print("   LOCATION = the sign of lambda_n.  An off-line zero injects an EXPONENTIAL R^n (R>1) that the")
print("              polynomial drift cannot contain -> lambda_n -> -infinity, RH fails.  R^n is invisible")
print("              to the count (it is a different scale: exp vs poly).")

print("\n" + "=" * 90)
print("""RESOLUTION OF THE TENSION -- the count does NOT constrain the location:
  * Order-1 Hadamard DOES couple the zeros (they determine all lambda_n).  But that coupling fixes only
    the POLYNOMIAL drift of lambda_n -- which is exactly the COUNT / the archimedean Gamma-factor.
  * The LOCATION (an off-line real part) is an EXPONENTIAL excursion R^n, R=|1-1/rho|>1.  Exponential
    always beats polynomial: the count's polynomial drift cannot pin the location's exponential scale.
    They are ORTHOGONAL SCALES, not just orthogonal coordinates.
  * Davenport-Heilbronn is the explicit WITNESS: entire of order 1, functional equation, the SAME
    polynomial drift (count), yet OFF-LINE zeros (the exponential excursion is present) -- some lambda_n<0.
    Order-1 + count is the structure DH SHARES with zeta; it cannot force RH.
  * The separator is the EULER PRODUCT (cross-prime multiplicativity, N9): it is what (conjecturally)
    forbids the exponential excursion for zeta -- i.e., RH = the location = no R^n, which is the
    multiplicative datum, NOT the order-1/count datum.
  NET: the last tension is closed NEGATIVELY and sharply.  count = polynomial drift = Gamma-factor =
  order-1 (free, shared with DH);  location = exponential excursion = Euler product = RH (the wall).
  The Hadamard coupling is real but scale-limited; it can never reach the location. This re-derives the
  Li-Keiper barrier (R^n beats n log n) from the count/location split, and confirms the Gamma-factor
  (count) and RH (location) are separated by the SCALE GAP that only the Euler product bridges.
""")
print("=" * 90)
