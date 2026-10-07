"""
THE q->1 FLOOR-LIFT, made explicit: interpolate function-field zeta (q>=2, RH a THEOREM) toward
zeta_Q (q->1), and test whether the zero locus stays continuous on the q-invariant 1/2 line.

Frobenius picture.  A function-field zeta over F_q has zeros at s = log(alpha_i)/log q, where alpha_i are
the Frobenius eigenvalues; RH = |alpha_i| = sqrt q (the q-circle) <=> Re(s) = 1/2.  The clean continuous
family that carries the zeta zeros rho_i = 1/2 + i*gamma_i:

        alpha_i(q) = q^{rho_i}      (so the zeta zero in s is exactly rho_i, for EVERY q)

  RH  <=>  |alpha_i(q)| = q^{1/2}  (on the q-circle)  <=>  Re(rho_i) = 1/2.

We test four things as q: 8 -> 1:
  T1  the line is preserved per finite q for free (the zero is rho_i, Re=1/2 if RH) -- Weil-per-q.
  T2  as q->1, alpha_i -> 1 (Frobenius -> identity).  Does the q->1 limit DISTINGUISH on-line from
      off-line, or COLLAPSE both to the unit circle (so RH info moves to the linearization)?
  T3  a HYPOTHETICAL off-line zero rho = 0.6 + i*gamma: does q->1 expel it (a selection mechanism)
      or merely preserve its Re?  (Tests whether q->1 *forces* the line or just inherits it.)
  T4  the linearization: the scaling generator (log alpha_i)/(log q) = rho_i -- the apex archimedean
      operator whose spectrum IS the zeros.  Where the q->1 lift actually lands.

No torch. mpmath. Deterministic.
"""
import mpmath as mp
mp.mp.dps = 25

GAMMA = [mp.mpf(g) for g in ['14.134725142','21.022039639','25.010857580','30.424876126','32.935061588']]
RHO   = [mp.mpf('0.5') + 1j*g for g in GAMMA]          # the zeta zeros (RH: Re=1/2)
RHO_OFF = mp.mpf('0.6') + 1j*GAMMA[0]                    # a HYPOTHETICAL off-line zero (Re=0.6)
QS = [mp.mpf(x) for x in ('8','4','2','1.5','1.1','1.01','1.001')]

print("=" * 90)
print("q->1 interpolation: alpha_i(q)=q^{rho_i}, RH <=> |alpha_i|=sqrt q (the q-circle)")
print("=" * 90)

print("\nT1+T2  on-line zero rho_1 = 1/2 + i*14.1347 :  |alpha_1|/sqrt q = q^{Re rho - 1/2}")
print(f"   {'q':>8} {'|alpha_1|/sqrt q':>18} {'zero Re(s)':>12} {'|alpha_1| (->1)':>16} {'arg(alpha_1)':>14}")
for q in QS:
    a = q**RHO[0]
    ratio = abs(a)/mp.sqrt(q)                            # =1 iff Re rho = 1/2 (RH)
    zRe = mp.re(mp.log(a)/mp.log(q))                     # = Re rho = 1/2
    print(f"   {mp.nstr(q,5):>8} {mp.nstr(ratio,10):>18} {mp.nstr(zRe,6):>12} {mp.nstr(abs(a),6):>16} {mp.nstr(mp.arg(a),5):>14}")
print("   => on-line: ratio == 1 for ALL q (line preserved for free, Weil-per-q); as q->1, alpha_1 -> 1.")

print("\nT3  HYPOTHETICAL off-line zero rho = 0.6 + i*14.1347 : does q->1 expel it or preserve Re?")
print(f"   {'q':>8} {'|alpha|/sqrt q = q^0.1':>22} {'zero Re(s)':>12} {'verdict':>22}")
for q in QS:
    a = q**RHO_OFF
    ratio = abs(a)/mp.sqrt(q)                            # = q^{0.6-0.5} = q^{0.1}
    zRe = mp.re(mp.log(a)/mp.log(q))                     # = 0.6 (constant!)
    verdict = "off-circle (detectable)" if abs(ratio-1) > mp.mpf('0.01') else "collapses to circle"
    print(f"   {mp.nstr(q,5):>8} {mp.nstr(ratio,8):>22} {mp.nstr(zRe,6):>12} {verdict:>22}")
print("   => the zero stays at Re=0.6 for ALL q (q->1 PRESERVES Re, does NOT force the line).")
print("      BUT the modulus ratio q^{0.1} -> 1 as q->1: the q->1 collapse LOSES the on/off-line")
print("      distinction at leading order (both eigenvalues -> the unit circle). RH info is NOT in the")
print("      limit alpha->1 -- it is in the LINEARIZATION (the rate), the scaling generator.")

print("\nT4  the linearization = the scaling generator (log alpha_i)/(log q) = rho_i (the zeros):")
q = mp.mpf('1.001')
print(f"   at q={mp.nstr(q,4)}:  generator (log alpha_i)/(log q) for the 5 zeros:")
for i, rho in enumerate(RHO):
    gen = mp.log(q**rho)/mp.log(q)
    print(f"     rho_{i+1}: generator = {mp.nstr(gen,8)}   (= rho_{i+1}, Re={mp.nstr(mp.re(gen),4)})")
print("   => as q->1 the Frobenius collapses to the identity, but its GENERATOR is exactly the zeros.")
print("      The q->1 linearization IS the archimedean scaling operator (N4-N6 apex operator) whose")
print("      spectrum is {rho_i}; RH = that spectrum on Re=1/2.")

print("\n" + "=" * 90)
print("""HONEST VERDICT -- the q->1 floor-lift, made explicit:
  * The 1/2 line is preserved for FREE at every finite q (the zero is rho_i; Weil gives Re=1/2 for
    genuine function fields) -- so 'do the zeros stay on the line as q->1' is NOT the difficulty.
  * q->1 does NOT force the line: a hypothetical off-line zero stays at its Re for all q (T3). And the
    q->1 limit COLLAPSES every eigenvalue to the unit circle (|alpha|->1), LOSING the on/off-line
    distinction at leading order. There is no 'selection mechanism' in the naive q->1 limit.
  * The RH information survives only in the LINEARIZATION: the scaling generator (log alpha)/(log q) =
    rho_i. That generator is exactly the program's apex archimedean operator (N4-N6) / the CCM scaling
    flow whose spectrum is the zeros. The q->1 floor-lift LANDS on the apex/CCM frontier.
  CONCLUSION: the floor-lift is REAL and UNIFYING -- it shows the proven function-field RH (finite q,
  Frobenius on the q-circle) and the open RH-over-Q (the q->1 linearization, the scaling generator on
  Re=1/2) are the SAME scaling flow at q>1 vs q->1. It does NOT breach: the difficulty is the
  archimedean linearization/completion (infinite spectrum with the right density = the Gamma-factor),
  which is exactly CCM. Two roads -- geometric (function field) and analytic (apex/prolate) -- reach
  the one archimedean completion. Conservation of difficulty, with a genuine unification.
  (Caveat: the *naive* zeta limit as q->1 gives the trivial F_1 zeta, not zeta_Q; reaching zeta_Q is
   precisely the archimedean-completed limit = the open step.)
""")
print("=" * 90)
