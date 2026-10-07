"""
probe_closure_anatomy.py  --  attempt the closure (ramp tau<1 forces plateau tau>=1 => Q(g)>=0 => RH),
using the now-exact (-1)^n transfer (N5 Thm 6.2) as leverage. Pin EXACTLY how far it goes and where
it breaks. Honest, adversarial (GPD): no forced match.

The closure needs Q(g) = arch + pole - primes >= 0 for all admissible g (Weil criterion). Decompose:

  PART 1 (exact): the t->-t involution splits the cumulant tower into channels.
     even/sum (metric/self-dual)  : log(1+at)+log(1-at) = log(1-a^2 t^2),  kappa_n = -2(n-1)! a^n (n even)
     odd/diff (chiral/connection) : log(1+at)-log(1-at) = 2 artanh(at),    kappa_n = +2(n-1)! a^n (n odd)
     Summed over primes: S_n = sum_p 1/(p-1)^n (Mertens-type), the order-n arithmetic mass.

  PART 2 (exact): WHERE the transfer lives. Pair correlation (n=2) form factor K(tau) = diagonal +
     off-diagonal. The transfer kappa_2^HL = -1/(p-1)^2 is the OFF-DIAGONAL (prime-pair / HL) term;
     the diagonal is the prime-power/PNT term. So the transfer is arithmetic<->arithmetic (HL <-> block),
     entirely inside the PLATEAU side. It gives ZERO leverage on the diagonal(ramp)->offdiag(plateau)
     forcing, which is arithmetic<->ARCHIMEDEAN. This is the precise conservation-of-difficulty.

  PART 3 (mpmath): the archimedean density 2 theta'(r) = Re psi(1/4+ir/2) - log pi. It is NEGATIVE near
     r=0 (broad g = plateau) and ~ +log(r/2pi) for large r (narrow g = ramp). So the archimedean term
     HELPS at high frequency (ramp, |tau|<1) -> unconditional positivity there; but is NEGATIVE at low
     frequency (plateau), where positivity rests on the pole + the EXACT prime cancellation = conditional
     = arch-domination = RH. Reproduces N5's 2theta'(0) ~ -5.37. This is the wall, located.

  PART 4 (numeric): kill the Hadamard garden path. prod_p (1 - t/(p-1)) e^{t/(p-1)} converges (order-1
     Hadamard-type) but its zeros are at t = p-1 (REAL, trivial) -> it is NOT xi, real-rootedness is
     free -> no RH leverage. (Paranoid kill, like V_4 and (p-2)^2.)

sympy + mpmath. No torch.
"""
import sympy as sp
import mpmath as mp
mp.mp.dps = 30

p, t, a = sp.symbols('p t a', positive=True)

print("=" * 90)
print("[1] t->-t channel split (metric=even/self-dual, chiral=odd/connection) + Mertens masses S_n")
print("=" * 90)
apex = sp.log(1 + a * t)
hl = sp.log(1 - a * t)
summ = sp.series(apex + hl, t, 0, 9).removeO()
diff = sp.series(apex - hl, t, 0, 9).removeO()
print(f"  apex+HL = log(1-a^2 t^2) ?  {sp.simplify(summ - sp.series(sp.log(1-a**2*t**2),t,0,9).removeO())==0}")
print(f"  apex-HL = 2 artanh(a t)  ?  {sp.simplify(diff - sp.series(2*sp.atanh(a*t),t,0,9).removeO())==0}")
print(f"  {'n':>3} {'metric ch (even)':>18} {'chiral ch (odd)':>18}   reading")
for n in range(2, 7):
    ce = sp.factorial(n) * summ.coeff(t, n)
    co = sp.factorial(n) * diff.coeff(t, n)
    tag = "metric/Fisher~zeta" if n % 2 == 0 else "cubic/chiral~L(s,chi3)"
    print(f"  {n:>3} {str(sp.simplify(ce)):>18} {str(sp.simplify(co)):>18}   "
          f"{'EVEN '+tag if n%2==0 else 'ODD  '+tag}")
print("  => even orders = -2(n-1)!a^n (metric channel, ALL NEGATIVE); odd orders = +2(n-1)!a^n (chiral,")
print("     ALL POSITIVE). The closure's positivity = metric channel must dominate the chiral channel.")
# summed arithmetic masses
print("  Mertens-type summed masses S_n = sum_p 1/(p-1)^n (order-n arithmetic mass over all primes):")
primes = list(sp.primerange(2, 200000))
for n in (2, 3, 4):
    Sn = mp.fsum([mp.mpf(1) / (mp.mpf(pp) - 1)**n for pp in primes])
    print(f"    S_{n} = sum_p 1/(p-1)^{n} = {mp.nstr(Sn, 12)}   (converges; order-{n} total arithmetic mass)")

print("\n" + "=" * 90)
print("[2] WHERE the transfer lives: pair-correlation diagonal (ramp) vs off-diagonal (plateau)")
print("=" * 90)
# diagonal (prime-power) mass with the von Mangoldt weight (log p)^2 / p^k  -- the PNT/archimedean ramp
diag = mp.fsum([ (mp.log(pp))**2 * mp.fsum([mp.mpf(1)/pp**k for k in range(1, 40)]) for pp in primes[:2000] ])
# off-diagonal (HL prime-pair) transfer mass with weight (log p)^2 / (p-1)^2  -- the plateau
offd = mp.fsum([ (mp.log(pp))**2 / (mp.mpf(pp)-1)**2 for pp in primes ])
print(f"  DIAGONAL (ramp, p=p', prime-power, weight (log p)^2/p^k):   sum = {mp.nstr(diag,10)}   [PNT/archimedean]")
print(f"  OFF-DIAG (plateau, p!=p', HL pair, weight (log p)^2/(p-1)^2): sum = {mp.nstr(offd,10)}   [= transfer kappa_2^HL]")
print(f"  the transfer kappa_2^HL = -1/(p-1)^2 (N5 Thm 6.2) IS the off-diagonal weight (up to (log p)^2).")
print("  => the transfer is arithmetic<->arithmetic (HL <-> conductor block), living ENTIRELY in the")
print("     off-diagonal/PLATEAU. It does NOT connect the diagonal(ramp) to the archimedean. The")
print("     'ramp forces plateau' step is arithmetic<->ARCHIMEDEAN -- ORTHOGONAL to what the transfer")
print("     gives. CONSERVATION OF DIFFICULTY, located exactly: transfer closes term-by-term, NOT the")
print("     ramp->plateau continuation.")

print("\n" + "=" * 90)
print("[3] the archimedean density 2theta'(r): helps the ramp (uncond.), abandons the plateau (=RH)")
print("=" * 90)
def two_theta_prime(r):
    return mp.re(mp.digamma(mp.mpf('0.25') + 1j * r / 2)) - mp.log(mp.pi)
r0 = two_theta_prime(0)
print(f"  2theta'(0) = Re psi(1/4) - log pi = {mp.nstr(r0,8)}   (reproduces N5 'approx -5.37'; NEGATIVE)")
print(f"  {'r':>6} {'2theta_prime(r)':>18}   regime")
for r in (0, 1, 2, 3, 5, 10, 30, 100):
    v = two_theta_prime(r)
    reg = "NEG (plateau: broad g, low freq)" if v < 0 else "POS (ramp: narrow g, high freq)"
    print(f"  {r:>6} {mp.nstr(v,8):>18}   {reg}")
# zero crossing
rc = mp.findroot(two_theta_prime, 2)
print(f"  archimedean density crosses 0 at r ~ {mp.nstr(rc,6)};  ~ +log(r/2pi) as r->inf (PNT growth).")
print("""  READING: the archimedean weight is POSITIVE only at high frequency. A test function broad enough
  to probe the plateau (the conjectural |tau|>=1 arithmetic) sits where 2theta'<0: the archimedean term
  HURTS there. Positivity on the plateau must come from the pole +2(int g cosh)^2 and the EXACT prime
  cancellation -- i.e. arch-domination is NOT free at the plateau; that is precisely RH. At the ramp
  (high freq, |tau|<1) 2theta'>0 dominates the (bounded) prime term -> positivity is UNCONDITIONAL
  (Montgomery/Rudnick-Sarnak restricted support). The wall is the SIGN CHANGE of 2theta' at the
  ramp/plateau boundary.""")

print("\n" + "=" * 90)
print("[4] KILL the Hadamard garden path: prod_p (1-t/(p-1)) e^{t/(p-1)} is trivially real-rooted")
print("=" * 90)
def hadamard_partial(tt, P):
    return mp.fprod([(1 - mp.mpf(tt)/(pp-1)) * mp.e**(mp.mpf(tt)/(pp-1)) for pp in primes[:P]])
for tt in (0.5, 1.5, 3.0):
    vals = [hadamard_partial(tt, P) for P in (2000, 8000, 17000)]
    print(f"  F({tt}) partial products (P=2k,8k,17k): {', '.join(mp.nstr(v,8) for v in vals)}  (converges)")
print("  zeros of F are at t = p-1 = {1,2,4,6,10,12,...} -- REAL and EXPLICIT by construction.")
print("  => F is an order-1 Hadamard-type entire function that is AUTOMATICALLY real-rooted; it is NOT")
print("     xi(s) (whose zeros are the unknown rho). Its real-rootedness is FREE and carries NO RH")
print("     content. Garden path KILLED (matched-pair discipline, cf. V_4 / (p-2)^2).")

print("\n" + "=" * 90)
print("VERDICT  --  closure attempted, wall located, NOT crossed (difficulty conserved)")
print("=" * 90)
print("""  WHAT THE TRANSFER CLOSES (real): the term-by-term identity, exactly, all orders -- and now its
    CHANNEL STRUCTURE: metric channel (even orders, -2(n-1)!a^n, ~zeta) vs chiral channel (odd orders,
    +2(n-1)!a^n, ~L(s,chi3)). The closure's positivity = metric channel dominates chiral channel.
  WHAT IT DOES NOT CLOSE (the wall, located 3 ways):
    (i)  the transfer is arithmetic<->arithmetic (off-diagonal/plateau only); the ramp->plateau forcing
         is arithmetic<->archimedean -- orthogonal (Part 2).
    (ii) the archimedean density 2theta' is NEGATIVE on the plateau (low freq), so arch-domination is
         free on the ramp but is exactly RH on the plateau (Part 3).
    (iii) the clean closed forms do NOT assemble into xi: the natural Hadamard product is trivially
         real-rooted, not xi (Part 4).
  NET: the closure reduces to 'metric (even/zeta) channel dominates chiral (odd/cubic L(s,chi3)) channel
  on the plateau' = the cubic-chirality positivity c_2<0 (the KNOWN candidate: diez sec2.6, N6, Connes
  sec6.6a, unconditional via L(1/2,chi3)=0.4808>0). This is a genuine SHARPENING of the reduction (the
  closure now has an explicit even/odd channel target) but lands on an OPEN door. RH NOT proved;
  structural reduction real. Difficulty conserved.""")
