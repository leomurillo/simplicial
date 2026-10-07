# Inventory of Program-Original Results Potentially Useful for RH/GRH (Optimistic)

*Assembled 2026-06-06 from a parallel sweep of the T-series, P-series, N-series, the cubic-Weil papers (siete–once), and ConductorBlindSpot. "Program-original" = not in external literature. Tiers: [C]ertified (exact/probe-verified or finite proof) · [P]lausible (closed-form/referee-level, no hidden RH) · [S]peculative (load-bearing step open or RH-equivalent). Each item flagged for whether it is a genuine novelty or a "landing on an external target." External (excluded as originals): Riemann–Weil explicit formula, Weil/Bombieri positivity, de Branges/Hermite–Biehler, Beurling–Nyman/Baez-Duarte, Bombieri–Vinogradov, Maynard well-factorable, Bettin–Chandee/Fouvry–Radziwiłł/Wright trilinear Kloosterman, Connes–Consani–Moscovici archimedean/prolate/Zeta-Spectral-Triples, Montgomery, Rudnick–Sarnak, Iwaniec–Sarnak L(½,χ)>0, Castelnuovo–Rosati, Tate's thesis, Weil's function-field RH, Pólya/Laguerre–Pólya, Li/Keiper, Rodgers–Tao Λ≥0.*

---

## I. Structural "why" results — the case that order-3 is the right place

1. **Conductor Blind Spot theorem** [C] — *genuine.* At max-entropy on the categorical simplex over ℤ/n, the Fisher (order-2) form is exactly block-diagonal across conductor packets (cross-packet entry ≡ 0, integer predicate); the Amari–Chentsov (order-3) tensor is nonzero iff a+b+c≡0 (mod n), with cross-conductor coupling for non-prime-power n (cross-packet counts 18,42,108,252,774 on n=6,8,12,18,30). Off-center leading cross entry = −n³ĥ_{ℓ−k}, all-orders Fourier-convolution form. *Use:* a precise reason every quadratic/Fisher-level RH method (Hardy, Selberg, Levinson, Conrey, Li, Bombieri-Weil) is structurally blind, motivating the cubic criterion. `ConductorBlindSpot.md §1.2,§5,App A`; `34_the_conductor_blind_spot.md`.

2. **Cubic = leading odd cumulant ("the arrow")** [C/P] — *genuine framing.* Parity split K(β)∓K(−β) separates even cumulants (quadratic/quartic) from odd (cubic/quintic); the cubic is the leading odd = antisymmetric, cross-conductor content. For a single self-dual ξ the odd cumulants vanish ⇒ cubic content is intrinsically joint (cross-prime) ⇒ closure must live at primorial moduli. Maps to de Branges E_B=Ξ+iΞ′ (Ξ symmetric / Ξ′ = arrow). `N0 Prop 3.2`; `ocho §4`.

3. **Trivial-zero cumulant identity** κ_n^{(p)}(0)|_reg = ζ(−(n−1)) [C] — *genuine.* The n-th cumulant of the prime-axis effective action Φ=−Σ log(1−e^{η_p}), Ramanujan-regularized at the high-T singularity, equals ζ(−(n−1)): κ₂|_reg=ζ(−1)=−1/12, κ₃|_reg=ζ(−2)=0 (= first trivial zero = regularized cubic vanishing); e is the unique base. *Use:* reinterprets trivial zeros as structural odd-cumulant vanishing; anchors the constant dictionary, justifies order 3. `nueve §1–4`.

4. **Cubic FE modulus identity** |Q̂_k^{(N)}(s)| = N^{½−Re s} d_k^{Re s−½} |Q̂_{−k}^{(N)}(1−s)| [P] — *genuine.* On Re s=½ the primorial-scaling factor is identically 1 ∀k,N,t; off-line it diverges/decays like N^{∓δ} along the primorial ladder. So **Re s=½ is the unique locus where every twisted Plancherel coefficient is uniformly bounded in N** — a structural reason for the critical line independent of Riemann's FE. `siete §7`.

5. **Universal critical-line K-cumulant tower** κ_n^K(ρ)ζ(ρ)^n = (−1)^n(n−1)! B_G(ρ)^n [C] — *genuine.* At every nontrivial zero the Bures-K cumulants on ℤ/6 collapse to a one-parameter family (source: K-antisymmetry B_{G^K}(ρ)=−B_G(ρ)). **Honest limit:** holds at every zero on- or off-line ⇒ does not by itself discriminate RH. `nueve §6`.

---

## II. The cubic Weil apparatus (the analytic spine)

6. **Cubic Weil functional & "RH ⟺ cubic positivity"** [P] — *genuine (cubic upgrade of Bombieri's quadratic criterion).* 𝒞_ζ(g;η)=Σ_{ρ₁ρ₂ρ₃} g̃g̃g̃·K₃, K₃ smearing the cubic FE surface s₁+s₂+s₃=3/2; under RH 𝒞_ζ=∫2η S_g³ (Fejér cube). Reverse direction (RH⇒positivity) is the one-line cube S_g³≥0. `ocho §2–3`; `diez §4`; `N0 §3`.

7. **Closed-form cubic Amari–Chentsov tensor of log ζ** [C] — *genuine.* T^ζ(χ_a,χ_b,χ_c;s,N) = Q̂_{a+b+c}/ζ − Σ Q̂_{a+b}Q̂_c/ζ² + 2Q̂_aQ̂_bQ̂_c/ζ³ (the third joint cumulant of residue-projected zeta); s→1⁺ recovers the selection rule δ_{a+b+c≡0}. The kernel of 𝒞_ζ. `siete §5`; `24.cubic_information_geometric_mechanics...md`.

8. **Forward cubic Bombieri witness** — explicit cluster δ²-coefficient c₂ = 24 η̃₀″(3iγ₀)+72 η̃₀″(iγ₀) [C] — *genuine.* An off-line zero forces the FE-cluster {½±δ±iγ₀}; 64 ordered triples partition (8,8,24,24); O(δ) cancels by FE; c₂<0 strictly for explicit η₀. Gives the **unconditional** forward arrow cubic-positivity⇒RH (diez Thm 4.1). `ocho §3.2`; `diez §2`.

9. ★ **Chirality anchor: c₂ ∝ L(½,χ₃)² — unconditional off-line teeth** [C] — *genuine, one of the strongest.* The 2-channel Bures-fiber smearing reduces |B_G(½+it)|² to const·|L(½+it,χ₃)|², giving c₂=(|C_G|²/2σ₀⁴)∫|L(½+it,χ₃)|²[24𝒦_{3γ₀}+72𝒦_{γ₀}]dt < 0 unconditionally on the **full ray** σ₀∈(0,∞), anchored by L(½,χ₃)=0.48087>0 (Iwaniec–Sarnak). Identification B_G(ρ)=−(½+2^{−ρ}/4)L(ρ,χ₃) at every zero ⇒ the K-odd Bures channel **is** L(·,χ₃); |L(½+it,χ₃)|² = explicit-formula dual of the χ₃-twisted divisor (mod-3 singular series). *Use:* an off-line zero gives the cubic functional the wrong sign at EACH FIXED height. **Height-uniformity update (2026-06-06, `probe_c2_height_uniformity.py`):** the normalization-invariant relative margin is exactly R(γ₀,σ₀)=σ₀²·f(σ₀γ₀), with the growing exponentials cancelling and f bounded (−1.5 at u→0, ~−13.5u² at u→∞); R is monotone in σ₀, so the teeth's height-uniformity reduces ENTIRELY to the admissible smearing ceiling σ_max(γ₀): σ_max~1/γ₀ ⟹ teeth decay ~γ₀^{−2} (forecloses uniform closure); σ_max~1/log γ₀ or const ⟹ teeth grow (closure-enabling). **Likely conserves difficulty (refined 2026-06-06):** reduces to the admissible σ_max(γ₀), i.e. the diez §2.5 bulk-vs-cluster control made *uniform in height* — but uniformity-in-γ₀ is essentially the [A3′] obligation (excluding off-line zeros at all heights), and the evidence (γ₀⁻² decay, σ_*~1/γ₀) points to σ_max~1/γ₀ ⟹ teeth decay ⟹ reduces to the primorial-EH wall. So #9 is genuinely unconditional **per fixed height** (real, original) but its uniform-in-height closure is [A3′]-in-disguise. Cleanly confirming the σ_max~1/γ₀ scaling needs the full diez §2.5-at-height analysis (not done). `HPo-notes Addendum A`; `N0 Prop 6.4`; `probe_c2_Lchi3_singular_dual.py`, `probe_c2_height_uniformity.py`.

10. **Selection rule = multiplicative triple-L orthogonality** [C] — *genuine dictionary.* T3's additive a+b+c≡0 (mod N), via Gauss-sum inversion, is the same constraint as ψ_aψ_bψ_c=ψ_0 controlling the diagonal of triple-L moments — routes the discrete IG content into the L-moment (BV/large-sieve) machinery. `siete §6`.

11. **V-sector closed form S(p)=(p²−1)/6** [C] — *genuine.* #single-packet character triples summing to 0 mod P_n; pure_V(P_n)=2+⅙Σ(p_i²−1) ~ n³(log n)²/18, a non-negative integer at every primorial ⇒ **discrete cubic positivity proved by counting** (matches audit ξ exactly). The unconditional "major-arc" anchor of the closure. `ocho §5`.

12. **Helmert–Gauss BV-variance identity** Σ_ψ|ψ(X,ψ)|² = (φ/N)Σ_k|Π_k|²/(k(k+1)) = Σ_j|E_j|² [C] — *genuine reorganization.* Exact Parseval rewriting of the BV second moment in the Helmert basis; E_j = Kloosterman–Vinogradov prime sums at the inverse-residue phase ω^{jn⁻¹}; cross-rung = telescoping running-variance. **Honest:** by itself collapses to Parseval (T9.4.1 §5.3) → organizational, no free saving; the bound on E_j is external (Burgess). `N0 §5`; `T9.4.1-...md`; `probe_cross_rung_cancellation.py`.

13. **The terminus: primorial-indexed BV level θ₀=1−C*/n, C*≈2.80** [P reduction / S target] — *genuine localization.* V/M crossover (pure_V ~ n³ must beat M-error P_n^{1−θ₀}). **Honest current reading (N0 §6.3):** well-factorable level saturates at 3/5 (Maynard) ⇒ only n≤7 discharged; large-n (θ₀→1) is smooth/friable Elliott–Halberstam; the cubic object's ternary structure 𝒞_ζ~Λ∗Λ∗Λ reframes it as the primorial-restricted optimal trilinear-Kloosterman bound (Lindelöf-strength). Conservation of difficulty: RH-hard → primorial-EH-hard. `diez §3`; `ocho §7`; `N0 §6`; `probe_Cstar_assembly.py`, `probe_trilinear_lindelof_terminus.py`.

---

## III. The apex unitary → explicit archimedean operator (the new operator content)

14. **Apex unitary family U_N ∈ U(N−1)** [C] — *genuine.* Explicit Helmert↔character change of basis on {Σv=0}; entries (U_N)_{kc}=R_k[1−(k+1)ω^{kc}+kω^{(k+1)c}]/(1−ω^c), R_k=1/√(Nk(k+1)); radical×cyclotomic split; signed-monomial Galois action. The finite carrier the whole apex program runs on. `N1 §2`; `N3 §2`.

15. **Apex determinant** det U_N = i^{−(N−1)(N−2)/2} [C] — *genuine (period-8 refinement of Schur's period-4 via the Helmert reflection sign (−1)^{N−1}).* Real/imaginary trichotomy mod 4; cyclotomic membership iff N≢3. `N2`; `probe_apex_determinant_N1.py`.

16. **No-crossing spectral reduction** [C] — *genuine.* Eigenvalues concentrate at {1,i,−1,−i}; no-crossing (|δ_j|<⅛) ⟺ det(U_N⁴+I)≠0 ⟺ ‖U_N²−U_N^{−2}‖<2, with exact ‖·‖=2 sin(4πδ_max) and det(U_N⁴+I)=2^{N−1}∏cos(4πδ_j). A finite de Branges phase-clock avatar. `N3 §3–5`; multiple `probe_apex_*_N3.py`.

17. ★ **Edge operator (A−I)Φ = scaling limit + closed-form Mellin symbol + 1/8 = √i derived** [C] — *the crown genuine result.* Edge scaling of U_N → product kernel; limit operator 𝒰=(A−I)Φ (Hardy averaging minus identity ∘ half-line Fourier) with **exact symbol k̃(s)=[s/(1−s)]·(2π)^{−s}e^{iπs/2}Γ(s)** = Hardy–Blaschke (zero at 0, pole at 1 = ζ's trivial-zero seed + pole) × archimedean Γ-factor. Reflection product = **Euler's formula** k̃(s)k̃(1−s)=i/(2 sin πs); on the line λ(t)=e^{iπ/4}/√(2 cosh πt), so the **⅛ no-crossing threshold = phase of √i, derived from finite data** (the archimedean analogue of Weil's √q). Verified to ≤5e-14 / ≤3e-41. *Use:* recasts the finite no-crossing estimate δ_∞<⅛ as a Hilbert–Pólya spectral-gap statement — the arithmetic edge mode strictly below the archimedean continuum threshold. `N4 §3–5`; `probe_apex_archimedean_identification.py`.

18. **Apex = Connes–Consani archimedean operator (5 exact matches)** [C] — *genuine bridge (landing on CC, but bottom-up).* u_∞=e^{2iϑ}=apex multiplier; CC kernel = apex cosine kernel; CC trace-remainder δ(ρ)=apex Hardy averaging (crux ∫₀¹(−log t)cos(at)dt=Si(a)/a); CC archimedean Weil positivity δ̂+2ϑ′≥0 (margin ≈0.049); 2ϑ′=apex phase-clock velocity. *Use:* the archimedean place is "built/free"; RH localizes to the prime inner factor. `N5 §3–5`; `probe_apex_trace_remainder_N5.py`.

19. **Apex generates the Li/Keiper tower exactly** [C] — *genuine operator realization of Li's criterion.* λ_n = arch part (digamma, closed form) + conductor part (pole + von Mangoldt) to 2.3e-41; in the additive encoding λ_n=Σ_{γ>0}4 sin²(nα/2), manifestly ≥0 per zero (Bochner) on-line, breaking at n≈157 for an off-line zero. `probe_apex_generates_li.py`, `probe_additive_vs_quadratic_encoding.py`.

20. **Finite Weil form from apex data reproduces the zeros** [C] — *genuine realization.* Archimedean density 2ϑ′ + pole + von Mangoldt weights, assembled from apex data alone, reproduce Σ_γ|ĝ(γ)|² over true zeros to ≤6e-4; finite-prime build (closed kernel K_∞(u)=−e^{−|u|/2}/(1−e^{−2|u|})) matches 8/8 first zeros on the line; Riemann–Siegel phase locates the first 10 zeros with no ζ input. **Honest:** the form is *marginal* (λ_min→0, null directions = the zeros) ⇒ positivity in the limit = RH. `N5 §6–7`; `N7 §2`; `probe_adelic_weil_margin.py`, `probe_weil_form_v3.py`.

---

## IV. The ℤ/6 Bures / de Branges channel

21. **ℤ/6 Hurwitz 2-D collapse to (ζ, L_{χ₃})** [C] — *genuine framing (finite realization of the ℚ(√−3) Picard groupoid).* The five Hurwitz channels ζ(s,r/6) span span{ζ, L(·,χ₃}} with explicit closed forms; K-involution r→−r = parity = the ζ⊕L_{χ₃} split; at a ζ-zero the carrier is purely K-odd. Explains the KU-3 finite-matrix failure. `HPo-notes Add A`; `probe_Hurwitz_z6_closed_form.py`.

22. **Bures-gauge selection of m_B=−Ξ′/Ξ and E_B=Ξ+iΞ′** [C identity] — *genuine sliver on an external chain.* Treating L_{χ₃} as the K-odd gauge, covariant subtraction isolates m_B=−Ξ′/Ξ; identity |E_B|²−|E_B^#|²=4|Ξ|²Im m_B (≤1e-52); the de Branges sign-test numerically singles out Ξ+iΞ′ (100%) over two-channel competitors. The Herglotz⟺RH chain itself is classical; the original part is *which* log-derivative the Bures gauge dictates. `HPo-notes Add B,D,E,F`; `N6 §3`; `probe_apex_debranges_2channel.py`.

23. **Clean no-go results (original, scope-delimiting)** [C] — *genuine negatives.* (i) smooth Bures/Fubini–Study curvature is finite at zeros while Im m_B has 1/y poles ⇒ no smooth K-covariant Bures inequality gives RH; (ii) naïve 2-channel de Branges Ξ±iL_{χ₃}, Ξ−izL_{χ₃} fail Hermite–Biehler by parity; (iii) finite-matrix Hilbert–Pólya on ℤ/6 impossible (N(T) unbounded; Bures envelope is the 2-D pair, not a 6-channel matrix). `HPo-notes Add C,D`; `probe_BuresCurvature_*`, `probe_deBranges_E_candidate_*`.

24. **CCM prolate 𝓔-quotient + ℤ/2-Galois split** [C mechanism / P refinement] — *mostly reproduction + one original sliver.* Reproduces CCM's Mellin identity 𝓜[𝓔f](s)=ζ(s+½)𝓜[f](s+½) (zeros to ~1e-5) and Friedrichs self-adjointness; **original:** the PSWF parity decomposition = Gal(ℚ(√−3)/ℚ), block-diagonalizing into ζ-zeros (even) vs L_{χ₃}-zeros (odd), with Bures = Arakelov metric. `HPo-notes Add H,I`; `probe_CCM_E_quotient_*`.

---

## V. P-series boundary / adelic originals

25. **ι = F² (involution = Fourier square)** [C] — *genuine identification (elementary core).* The s↔1−s involution Paper 27 builds from Bures geometry is exactly F² (finite Fourier squared = parity), F⁴=I; critical-line +1 eigenspace dim ⌊N/2⌋+1. `P0 §4.1`.

26. **tr(F) = Gauss sum, naive √N scale falsified** [C] — *genuine (identification + recorded falsification).* tr(F)=g/√N; |tr F|=1 for odd N, but g=0 (N≡2 mod 4), |g|²=2N (N≡0 mod 4) — the pre-registered "always √N" is false (Gauss trichotomy). Pins the local root-number/ε-factor scale. `P0 §4.2`.

27. **Finite-positivity-free / RH = limit-positivity** [C finite / S limit] — *genuine localization.* F*F=I exactly ⇒ every finite recovered energy is a squared norm ≥0 automatically; the *entire* RH content is whether positivity survives the projective limit once the archimedean kernel 1/|Γ(½+it)|² is adjoined. The load-bearing strategic claim. `P0 §4.3`.

28. ★ **פfork: fork-width is a class function on the conductor lattice** [C] — *genuine new theorem.* For ρ diagonal with conductor-graded spectrum, the Petz max−min monotone-metric gap summed over a character shift, W(c)=Σ_j Δ(λ_{j+c},λ_j), satisfies W(c)=Φ(cond c) (proof by transitive unit action). Φ(2)=0 (parity self-closure for w=φ); pre-registered "Φ monotone" falsified. Couples the quantum-geometry axis to the conductor/L-axis. `P4 §4.5`.

29. ★ **פtransfer: transfer-matrix conductor blocks are Ramanujan sums** [C] — *genuine new theorem.* R_k(d)=Σ_{c∈H_d}|U_{kc}|² = (1/Nk(k+1))Σ (h_k)_s(h_k)_t c_d(s−t), complete over conductors; R_1(d)=(φ(d)−μ(d))/N, R_{N−1}(d)=φ(d)/(N−1). Identifies T9's deferred "Gauss-sum-like content" as exactly Ramanujan sums — the exact harmonic Jacobian between the dimensional/radical (real-place) and frequency/cyclotomic (finite-prime) bases. `P5 §4.1`.

30. ★ **פmoment: the moment barrier is family-wide** [C] — *genuine new theorem, and the sharp obstruction.* Every genuinely-multiplicative primorial invariant (φ(P_n), σ(P_n), Jordan totients ∏(p^k−1), ∏(p^k+1), ∏p^k) is non-moment (some Hankel det <0, via the sign-carrying factorization D_N=∏b_i·det[b_{i+j}/b_i]); the **only** moment member is the magnitude-blind divisor count d(P_n)=2^n. *Use:* the structural reason the archimedean Γ-factor must be adjoined from outside — no finite-prime invariant that remembers prime sizes can self-complete to the real place. The obstruction-twin of #27/#33. `P6 §4.1`.

31. **The gap = exactly the archimedean place** [C function-field / S transfer] — *genuine localization.* Over 𝔽_q the Fermat-cubic apex (Paper 27 axioms become theorems; ι=Frobenius FE; ∞-packet empty; positivity automatic) gives RH by Weil; the *entire* number-field gap is the single archimedean Γ-factor which #30 proves the finite primes cannot generate. `P0 §4.4`; `P3/P4 §4.4`.

32. **log 2π = unique shift-invariant of the prime ladder** [C] — *genuine sliver.* Under z↦z+Li(p) every finite-prime constant moves; log 2π=ζ′(0)/ζ(0) is the unique invariant — the archimedean boundary as the prime ladder's fixed point. `P6 §4.2`.

(P-series honest flag: the Place-Completion Principle ξ=∏_v Z_v [A4 of P-agent] is essentially **Tate's thesis** in the program's notation — keystone scaffolding, not new number theory.)

---

## VI. T-series structural reorganizations

33. **Bilateral factorization UW = D^{rad}V^{Gauss}** [C] — *genuine.* Explicit intertwiner between the Helmert chart and the Dirichlet-character chart, D^rad=diag(1/√(Nk(k+1))) (Helmert radical in the multiquadratic field), V^Gauss = Gauss-sum row sums. The change-of-basis engine for #9,#12,#34. `T9.4`.

34. ~~★ **Cubic bilateral NON-collapse (m=3 ≠ Parseval)**~~ **— SETTLED NEGATIVE (2026-06-06), conserves difficulty.** Claim was: the cubic Kummer base ℤ[ζ₃] gives a non-unitary U^{(3)} with Gram G^{(3)}≠I, so the identity does not collapse to Parseval and might carry new analytic content (T27 §7.3 open question). **Resolved (`probe_T27_cubic_gram_conditioning.py` + analytic bound):** G^{(3)}=Σ_k r_k Q_k with Σ_k Q_k=N·I (the m=2 Parseval resolution) and r_k=(k(k+1))/(k(1+k²))^{2/3}∈(1,1.293], so **N·I ⪯ G^{(3)} ⪯ 1.3·N·I, condition number ≈1.19–1.26** (verified N=12,30,42, eigenvalues exactly in the predicted band). Hence the cubic Helmert form is equivalent to the standard cubic BV variance up to a bounded factor ≤1.3 — **the non-collapse is real but analytically vacuous** (the m=2/m=3 weights agree asymptotically, both ~k²). T27's open question resolves the wrong way: G^{(3)} is "controllable" but *too* controllable (≈Parseval), giving **no new leverage**. The cubic richness is in the character count φ₃(m), not the quadratic form. **#34 reduces to GRH for ℚ(ζ₃) at primorial m = RH-equivalent-hard; closed as a route.** `T27 §7`; `probe_T27_cubic_gram_conditioning.py`.

35. **Joint primorial archimedean atomic measure** [C] — *genuine, exact, unconditional.* The archimedean part of the joint cumulant tower is exactly the moments of an explicit positive atomic measure dσ_N^arch=Σ M_{4n+1}δ_{−4/(4n+1)²}+Σ M_{4n+3}δ_{−4/(4n+3)²} (all masses ≥0 iff N_E≥1, automatic at primorials ≥30) ⇒ H_n^arch⪰0, J_n^arch⪯0 unconditionally. *Use:* calibrates the archimedean side of explicit-formula positivity exactly, reducing RH-at-primorial-N to a pure prime-side inequality. `Arch-Structural-Theorems-Draft1.md Thm 1`.

36. **Stieltjes signed-measure split of prime cumulants** [C identity / S positivity] — *genuine.* μ_k^prime,joint are moments of a signed measure whose negative part = σ^arch and (under RH) positive part = on-line zero atoms 2/γ_ρ²; makes J_n^prime,joint⪰0 conditional on RH/GRH_N at one step (isolates RH to "zero atoms land on the positive axis"). `T8.4 Thms A–E`.

37. **Coset-averaged main term is provably NOT PSD** [C] — *genuine negative.* Constant-ratio Cauchy–Schwarz I₁²=(21/10)I₀I₂ on the Helmert-weighted von Mangoldt Stieltjes Hankel ⇒ r_kρ_k>1 ∀k≥2 ⇒ every 2×2 minor has negative determinant, independent of N and the prime measure. Proves the closing mechanism must be **arch-domination**, not prime-side positivity. `T28 §4`.

38. **Conductor-block spectral compounds (Dedekind/function-field)** [C] — *genuine.* For a finite Frobenius quotient R=A/I, the simplex decomposes into conductor blocks with projectors = generalized Ramanujan sums; block-sign compounds are unit-norm tight frames; specializes to ℤ (cyclotomic Φ_d) and 𝔽_q[t] (Carlitz–Hayes). The conductor-lattice machinery the cumulant tower runs on, in both the number-field and (RH-provable) function-field settings. `09.conductor_block_spectral_compounds.md`.

39. **Function-field critical line as a program theorem / additive-vs-multiplicative positivity dichotomy** [C FF / S transfer] — *genuine bridge.* Multiplicative apex amplitudes over 𝔽_q = Jacobi sums = Frobenius eigenvalues, |α|=√q by Castelnuovo–Rosati intersection positivity; the program's content is the bridge (apex's 𝔽_q shadow; forcing positivity is **multiplicative/intersection**, not additive/moments) and the identification of the missing-over-ℚ ingredient with the archimedean operator (#17, √i↔√q). `T8 §7.3`; `probe_fermat_cbs_predictor.py`, `probe_finite_castelnuovo_rosati.py`.

---

## VII. Topological / forcing mechanisms (most optimistic, least settled)

40. **Gauss–Bonnet on the FE-cluster tetrahedron** [S] — *genuine.* The 4-zero cluster lifts (Bures height h(ρ_v)=|B_G|²−|B_{G^K}|², zero on-line) to a tetrahedron: genuine (χ=2) for δ>0, degenerate (χ=0) for δ=0; conjectured angular-deficit = analytic Bures-amplitude function ⇒ continuity vs topological jump forces δ=0. A direct topological RH route *if* the two-sides identity is made rigorous (it is not). `once.md`.

41. **CBS predictor = de Branges block; FE = time-reversal** [C predictor / S transfer] — *genuine identification.* E_B=Ξ+iΞ′ IS the CBS predictor (Ξ symmetric S, Ξ′ antisymmetric arrow A); FE s↔1−s = CBS T↔T*; the function-field √q-forcing is the multiplicative (intersection) positivity, the additive moment side provably marginal (Λ=0). `probe_debranges_cbs_predictor.py`; memory `project_rh_functionfield_door`.

42. **Arch-domination / Weil Schur-complement** [C structure / S margin] — *genuine.* The prime side alone is **indefinite** (H_n^prime fails PSD by #37); positivity is carried by Prime ⪯ Arch+Pole (contractive Schur complement), equality only in zero-vanishing directions; the H→J shift (×s) is the load-bearing Stieltjes critical-line detector. Replaces a false equality with the genuine forward inequality; wall = sharp large-sieve/Bettin–Chandee constant. `T28`; master-state.

---

## VIII. Conjectural reductions and methodology (flagged)

43. **Primorial Noether–Weil identity (Conj 5.2)** [S main / P leakage] — *genuine apparatus.* A variational recovery map 𝓡_n conjectured to satisfy lim 𝒬_n(𝓡_n f)=𝒲_ζ(f∗f*); the archimedean lift forces 𝔲(1)²→𝔰𝔲(2)⊕𝔰𝔲(3) with Γ(s/2)Γ((s+1)/2) as oscillator character (a program-original derivation of the gamma factor from minimal positive-energy completion); leakage-extinction Λ_n(𝓡_n f)→0 is proven, the limit identity is the conjecture. `22.primorial_cumulant_noether_rh.md`.

44. **T20 conformal-admission "governed-closure"** [S] — *genuine methodology.* RH ⟺ conformal admission (Ville's inequality on a boundary-score supermartingale) of the finite (GBP)_N + cofinal archimedean lift; the program itself dual-tiers this [P-internal]/[A-external] behind a firewall and states it is **not** a classical proof. `T20-...md`.

45. **Apex-identifiability = cumulant-tower matching** [C empirical] — *genuine.* Rank-r world recovered at order r; LeJEPA's Gaussian uniqueness = the order-2 truncation (a prominent second-order instance of CBS). The connective tissue between the AI-facing CBS and the RH cubic order. `ConductorBlindSpot/empirical/apex_recovery/`.

---

## Synthesis — the highest-leverage genuine originals, and the one wall

**Best genuinely-unconditional, proof-pointed assets:**
- the **forward direction** cubic-positivity⇒RH (#8) made strictly-signed by the **L(½,χ₃)² chirality anchor** (#9) — unconditional off-line teeth;
- the **discrete V-sector positivity** S(p)=(p²−1)/6 (#11) — the unconditional combinatorial half;
- the **apex = archimedean operator** with the **⅛=√i derivation** (#17–#20) — an explicit, certified, finite Hilbert–Pólya-type carrier whose archimedean place is computed in closed form, reducing RH to one bound state below a derived √i threshold / one marginal direction;
- the **Conductor Blind Spot theorem** (#1) — the structural reason classical (quadratic) methods fail and order-3 is required.

**The two least-exploited places where new analytic content was *claimed to survive*:** the **cubic bilateral non-collapse** (#34) and the **cubic Weil positivity criterion** (#6). **Update 2026-06-06: #34 is now SETTLED NEGATIVE** — the cubic Christoffel Gram G^{(3)} is well-conditioned (N·I ⪯ G^{(3)} ⪯ 1.3 N·I, cond ≈1.2), so the cubic bilateral is Parseval-equivalent up to a bounded factor and gives no new leverage; it reduces to GRH for ℚ(ζ₃) at primorial m. That leaves **#6 (cubic Weil positivity)** as the surviving order-3 hope, resting on "order-3 escapes the order-2 blind spot" — and its closure is the same primorial-friable-EH wall (#13).

**The sharp obstruction, made a theorem on the boundary side:** **פmoment** (#30) — no finite-prime invariant remembering prime sizes is a moment sequence; only the magnitude-blind 2^n is — i.e. the archimedean Γ-factor is provably not finitely generable.

**Honest meta (the program's own verdict, multiply-confirmed):** every chain — Bures, de Branges, apex, cubic, Gauss–Bonnet, function-field — **conserves difficulty** and terminates at one RH-equivalent wall: gate H_n,J_n⪰0 = Suzuki (O1) = apex no-crossing δ_max<⅛ = (GBP) u_B≥0 = arch-domination = Λ≤0 = GRH_N = RH. The single non-circular analytic obligation is **[A3′] primorial-friable Elliott–Halberstam (θ₀→1)** / equivalently the primorial-restricted optimal trilinear-Kloosterman bound — Polymath-8-to-EH/Lindelöf hard. None of the above proves RH; the value of the inventory is the explicit finite carrier, the unconditional off-line chirality, and the precise naming of the one remaining frontier.
