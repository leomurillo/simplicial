# Born-Helmert Candidate Ledger: \(P=30,\ T=7\) Moment Probe

**Date:** May 24, 2026  
**Author:** Leonardo Murillo Montero + Codex  
**Status:** computational steering note, not a theorem

## Question

Test the simplest unsmoothed centered primorial/Archimedean ledger proposed
by the Born-Helmert route:

\[
y^{(n,T)}(r)
:=
\sum_{\substack{p\le p_n,\ k\ge1\\ p^k\equiv r\pmod {P_n}\\ k\log p\le T}}
\frac{\log p}{p^{k/2}}.
\]

For the first nontrivial stage requested by the peer note,

\[
P_n=30,\qquad p_n=5,\qquad T=7,
\]

so \(p\in\{2,3,5\}\).

Center the ledger:

\[
\widetilde y(r)=y(r)-\frac1{30}\sum_{q\in\mathbb Z/30}y(q),
\]

take character coefficients with Pass-4 normalization

\[
\widehat y_a
=
\frac1{30}
\sum_{r\in\mathbb Z/30}
\overline{\chi_a(r)}\,\widetilde y(r),
\qquad a\ne0,
\]

and define Born atoms

\[
\lambda_a=|\widehat y_a|^2.
\]

The tested Born moments are

\[
M_m^{(30,7)}
=
\sum_{a\ne0}\lambda_a^m.
\]

These are compared against the folded \(\Xi\) moments

\[
\ell_m
=
\sum_{k\ge1}\gamma_k^{-2m},
\]

with \(\gamma_k\) the positive ordinates of the zeta zeros. The comparison
below used the first 100 zeros; for \(m=1\) the Riemann-von Mangoldt tail

\[
\frac{\log(T_0/2\pi)+1}{2\pi T_0}
\]

was added at the last sampled zero \(T_0=\gamma_{100}\).

## Raw Result

The finite ledger has 20 prime-power terms. Parseval checks:

\[
\sum_{a\ne0}|\widehat y_a|^2
=
\frac1{30}\sum_r|\widetilde y(r)|^2
=
0.05858524013589165\ldots
\]

The largest Born atoms are approximately

\[
0.0075423390,\ 0.0075423390,\ 
0.0033645279,\ 0.0033645279,\ 
0.0029878066,\ 0.0029878066.
\]

For reference,

\[
\gamma_1^{-2}=0.005005244123594116\ldots
\]

so the largest raw atom is already larger than the first folded zero atom.

| \(m\) | \(M_m^{(30,7)}\) | \(\ell_m\) approx. | ratio |
|---:|---:|---:|---:|
| 1 | \(5.85852401358917\cdot10^{-2}\) | \(2.31083873399429\cdot10^{-2}\) | \(2.5352370667\) |
| 2 | \(2.12030998874324\cdot10^{-4}\) | \(3.71567769387698\cdot10^{-5}\) | \(5.7063883454\) |
| 3 | \(1.11738315110543\cdot10^{-6}\) | \(1.44173767872171\cdot10^{-7}\) | \(7.7502528206\) |
| 4 | \(7.20751967841223\cdot10^{-9}\) | \(6.63031678201978\cdot10^{-10}\) | \(10.8705510089\) |
| 5 | \(5.09827048695153\cdot10^{-11}\) | \(3.21366415058841\cdot10^{-12}\) | \(15.8643537347\) |
| 6 | \(3.74722873105205\cdot10^{-13}\) | \(1.58769345149097\cdot10^{-14}\) | \(23.6017143456\) |
| 7 | \(2.79702168160499\cdot10^{-15}\) | \(7.90332572404674\cdot10^{-17}\) | \(35.3904391552\) |
| 8 | \(2.10071029942608\cdot10^{-17}\) | \(3.94647139999885\cdot10^{-19}\) | \(53.2300905418\) |
| 9 | \(1.58168434509614\cdot10^{-19}\) | \(1.97326507374497\cdot10^{-21}\) | \(80.1556955597\) |
| 10 | \(1.19210563316217\cdot10^{-21}\) | \(9.87216538329716\cdot10^{-24}\) | \(120.7542202625\) |

## Trace-Fitted Check

If the amplitudes are rescaled by a single scalar so that \(M_1\) matches
\(\ell_1\), then

\[
c^2=\frac{\ell_1}{M_1}=0.3944404304965171\ldots,
\qquad
c=0.6280449271322212\ldots.
\]

The trace-fitted moment ratios become:

| \(m\) | trace-fitted ratio |
|---:|---:|
| 1 | \(1.0000000000\) |
| 2 | \(0.8878184629\) |
| 3 | \(0.4756200368\) |
| 4 | \(0.2631341739\) |
| 5 | \(0.1514710045\) |
| 6 | \(0.0888857404\) |
| 7 | \(0.0525721721\) |
| 8 | \(0.0311895133\) |
| 9 | \(0.0185253834\) |
| 10 | \(0.0110082063\) |

Thus the miss is not a scalar normalization error. After trace matching, the
higher Born moments are too small, meaning the raw finite ledger has the
wrong spectral shape.

## Nearby Variant

A nearby variant was also tested: keep the same projection to
\(\mathbb Z/30\), but include all primes \(p^k\le e^7\) rather than only
\(p\le5\). This made the mismatch dramatically worse:

\[
\frac{M_1}{\ell_1}\approx447.16,
\qquad
\frac{M_2}{\ell_2}\approx5.50\cdot10^5.
\]

So the Pass-4 restriction \(p\le p_n\) is the meaningful finite-stage
candidate. Simply adding more primes at fixed modulus is not the correction.

## Interpretation

The simplest \(t=0\), \(P=30\), \(T=7\) unsmoothed ledger does **not** match
the folded \(\Xi\) cumulants.

This is useful negative information:

1. Born positivity is present automatically.
2. Parseval/trace bookkeeping is correct.
3. The raw moment spectrum is not the folded \(\Xi\) moment spectrum.
4. A scalar gauge cannot repair it.
5. The missing ingredient is structural: an Archimedean/gamma correction,
   a heat/window regularization, a different normalization of the character
   packets, or a more refined primorial-to-Archimedean limiting order.

The result points back to the prime/gamma split of Pass-5 section 17.2:

\[
F=F_{\mathrm{arch}}+F_{\mathrm{prime}}.
\]

The raw candidate tests mostly the prime-power residue ledger. The folded
\(\Xi\) cumulants also include the archimedean channel and the exact
functional-equation centering. The next candidate should therefore include
the odd-in-\(t\) archimedean correction before comparing Born moments.

## Next Probe

The next computational probe should test a corrected ledger:

\[
y_{\mathrm{corr}}^{(n,T)}
=
y_{\mathrm{prime}}^{(n,T)}
+
y_{\mathrm{arch}}^{(n,T)}
\]

where \(y_{\mathrm{arch}}\) is chosen so that the finite jets reproduce the
odd-in-\(t\) archimedean piece

\[
F_{\mathrm{arch}}(x)
=
\frac{A(1/2+t)-A(1/2-t)}{4t}.
\]

Success criterion:

\[
\sum_a|\widehat y_{a,\mathrm{corr}}|^{2m}
\approx
\ell_m
\qquad(1\le m\le10).
\]

The raw probe fails, but it fails cleanly. That is a good diagnostic.
