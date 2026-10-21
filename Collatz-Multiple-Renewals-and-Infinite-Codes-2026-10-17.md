# Multiple renewals and the infinite-code obstruction

Status: proved finite realization, density, and periodic-code exclusion statements. The aperiodic positive-integer case remains unresolved. These are elementary deductions from the affine formulas; no novelty claim is made.

Throughout, U(n)=(3n+1)/2^{v_2(3n+1)} is the odd-only Collatz map. An arrow labeled by a word represents multiple U steps, with the word listing their halving exponents.

## 1. Arbitrarily many prescribed switches are compatible

Use the two blocks

\[
A=(1),\quad F_A(x)=(3x+1)/2,
\qquad B=(2,1,1),\quad F_B(x)=(27x+29)/16.
\]

**Theorem 1.** Every finite string of A and B beginning with A occurs on infinitely many positive odd Collatz trajectories. At every individual odd step in that string, the current value is strictly greater than the initial value.

**Existence proof.** Flatten the string into an exponent word (a_1,...,a_m), let S=sum a_i, and compute C by the recursion C_0=S_0=0,

\[
C_{j+1}=3C_j+2^{S_j},\qquad S_{j+1}=S_j+a_{j+1}.
\]

The complete word map is (3^m n+C)/2^S. Its exact admissibility class is

\[
n\equiv(2^S-C)(3^m)^{-1}\pmod{2^{S+1}}. \tag{1}
\]

To justify exact admissibility, invert each odd step as x=(2^a y-1)/3 in the 2-adic integers. Starting with an odd y gives an odd x and exactly v_2(3x+1)=a. Composition sends all odd y onto the residue class (1). For a positive integer n in that class, the forward iterates are therefore positive odd integers with exactly the prescribed exponents. The class contains infinitely many positive integers.

**No-descent proof.** Each affine prefix has positive intercept. The first A gives slope 3/2. At complete block endpoints, subsequent slopes multiply by either 3/2 or 27/16, both greater than one. Within B the relative prefix slopes are 3/4, 9/8, and 27/16. Consequently the smallest possible prefix slope after the initial A is at least (3/2)(3/4)=9/8>1. All individual U-step values therefore exceed the start. ∎

This is stronger than constructing one large refill: any finite schedule of these two patterns is compatible with all its preceding switches and with no descent. It does not produce a single positive integer supporting an infinite schedule; the starting integer depends on the finite schedule.

For example, ABAB is realized by the fully displayed odd-only path

\[
667\xrightarrow{A}1001
\xrightarrow{B:\;1001\to751\to1127\to1691}1691
\xrightarrow{A}2537
\xrightarrow{B:\;2537\to1903\to2855\to4283}4283.
\]

The intermediate decreases 1001->751 and 2537->1903 remain above 667.

## 2. An exact density bound does not exclude an integer survivor

Normalize 2-adic measure so the odd integers have measure one. A cylinder with halving sum S occupies measure 2^{-S}. Distinct A/B strings at the same block depth give disjoint cylinders: at the first differing block, A begins with exponent 1 whereas B begins with exponent 2.

Thus the set of integers that follow at least r blocks from {A,B} has measure exactly

\[
(2^{-1}+2^{-4})^r=(9/16)^r.
\]

With the first block fixed to A, the measure is

\[
\frac12(9/16)^{r-1}.
\]

The corresponding finite-cylinder sets also have these natural densities among positive odd integers. The infinite survivor set has 2-adic measure zero and upper natural density zero, by inclusion in every finite-depth set. This does not imply that it contains no positive integer: a zero-density set can contain exceptional integers.

In particular, this supplies an explicit setting in which an exponential loss of mass and arbitrarily many admissible renewals coexist. A mixing or density estimate alone cannot supply the desired pointwise conclusion.

## 3. All eventually periodic block codes are excluded

**Theorem 2.** No positive integer has an infinite, eventually periodic A/B block code.

**Proof.** After the finite preperiod, suppose the positive odd integer x repeats a nonempty composite block W forever. Its map is

\[
F_W(x)=\frac{3^m x+C}{2^S},\qquad C>0.
\]

Since each A and B block expands in coefficient, D=3^m-2^S>0. Infinitely many repetitions require

\[
v_2(Dx+C)\ge kS+1
\]

for every k. Thus the ordinary integer Dx+C must be zero. But D,x,C are positive, a contradiction. ∎

This excludes all periodic mixtures of the two patterns, not just repetitions of A or B separately. It is a special case of the classical affine repetition argument. It does not exclude general positive Collatz cycles, whose composite coefficients contract.

## 4. A precise smaller target

Define a code to be an infinite sequence of A and B. Each prefix gives a residue class by (1). These classes are nested and their moduli tend to infinity, so the code defines a unique odd 2-adic integer.

Let r_j be the least nonnegative residue for the first j blocks. Since each later class refines the preceding one,

\[
r_{j+1}=r_j+q_j2^{S_j+1},\qquad q_j\ge0.
\]

Therefore r_j is nondecreasing. The code represents a positive integer precisely when r_j is eventually constant: a bounded monotone integer sequence stabilizes, and a fixed positive integer is eventually smaller than every cylinder modulus.

This gives the narrower target

\[
\boxed{r_j\longrightarrow\infty\quad\text{for every infinite A/B code}.} \tag{2}
\]

Theorem 2 proves (2) for eventually periodic codes. The remaining case is aperiodic codes whose least representatives might stabilize. Proving (2) would exclude this whole class of permanently expanding Collatz itineraries. It would be a partial result, not a proof of all Collatz: many other exponent patterns remain outside the class.

No proof of (2) for all aperiodic codes is supplied here. The value of this restricted target is that its transitions, cylinders, density, and periodic exceptions are all explicit; it can test a proposed pointwise arithmetic argument before that argument is claimed for every Collatz orbit.

## 5. A tempting real/2-adic argument that does not work

The inverse block maps are

\[
\phi_A(y)=(2y-1)/3,\qquad
\phi_B(y)=(16y-29)/27.
\]

Both contract in the real metric and in the 2-adic metric. They preserve the real interval [-29/11,-1]. Every code consequently has a negative real limit when inverse compositions are started inside that interval, as well as its odd 2-adic limit.

It would be incorrect to conclude that the 2-adic limit cannot be a positive integer. A sequence of rational numbers can have different limits in different completions. The rational denominators here grow as powers of three. Identifying the two limits is precisely an additional arithmetic claim, not a consequence of contraction in each metric.

## 6. Exact verification

`empirical_01g/multiple_expansion_switches.py` checks every A/B string beginning with A through block length 12: 4,095 schedules and 86,019 individual odd steps. It verifies the exact exponent words, absence of descent at every intermediate odd step, and all 12 finite-depth mass formulas. Full example paths are saved in the adjacent JSON file.

The algebra proves the general statements; these checks guard against errors in indexing, step conventions, and arithmetic. They do not establish the infinite-code exclusion (2).
