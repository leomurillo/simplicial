# Arithmetic ANEC via relative entropy — the diagnostic: where positive energy enters

**Goal (not a proof).** Transcribe the QFT proof of the averaged null energy condition (ANEC) from relative entropy to the arithmetic setting, and **locate exactly which step requires positive energy** (= RH). By the FH-guillotine this route must be circular; the value is *pinpointing* the circularity and harvesting the structure. Anchored to validated this-session pieces (§8.2 firewall, §8.4 Borchers, §8.7 margin) and standard theorems.

---

## 1. The QFT argument (what we transcribe)

ANEC $\int\langle T_{uu}\rangle\,du\ge0$ is a *theorem* (Faulkner–Leigh–Parrikar–Wang 2016; Ceyhan–Faulkner 2020) built from four ingredients:
- **(i)** $S_{\mathrm{rel}}(\psi\|\Omega)\ge0$ — positivity of relative entropy (Klein's inequality). **Unconditional.**
- **(ii)** $S_{\mathrm{rel}}$ monotone under subalgebra inclusion — data-processing / monotonicity. **Unconditional.**
- **(iii)** Longo (coherent-state entropy): in the chiral model $S_{\mathrm{rel}}=\,$const$\cdot$(null energy). **Unconditional in the chiral model.**
- **(iv)** Bisognano–Wichmann / Wiesbrock: the modular flow $\Delta^{it}$ **is** the geometric boost/dilation, equivalently the inclusion is $+$half-sided modular — which holds **iff positive energy** (the spectrum condition). **THIS is the input.**
The null deformation slides the cut; the derivative of the modular Hamiltonian is $\int T_{uu}$; (i)+(ii) then force $\ge0$ — *using* (iv) to identify the deformation with the energy.

## 2. The arithmetic dictionary

| QFT | arithmetic (program) |
|---|---|
| relative entropy $S_{\mathrm{rel}}(\psi\|\Omega)$ | the Weil positivity $=$ relative entropy (N14) |
| modular Hamiltonian $K=-\log\Delta$ | scaling/dilation generator $\log\Delta=-2\pi D$ (§8.4) |
| OS/physical Hamiltonian $H_{\mathrm{OS}}\succeq0$ | positive-energy generator $P$; $\,e^{-sP}$ bounded $=$ RH (§8.4) |
| null energy $\int T_{uu}$ | arithmetic stress tensor; arch-domination $\int T_{uu}\ge0$ (P∞) |
| $+$half-sided modular inclusion / B–W | the scaling inclusion $\mathcal V_s\subset\mathcal V$ is $+$hsm (§8.3, Borchers) |
| coherent-state $S_{\mathrm{rel}}=$const$\cdot$energy (Longo) | $S_{\mathrm{rel}}$ vs the Weil form $Q(g)$ — **decoupled by §8.2** |

## 3. Where positive energy enters — pinpointed

Run the chain. (i) and (ii) transcribe **unconditionally**: the arithmetic relative entropy (N14) is $\ge0$ and monotone in the scaling inclusion (§8.3). The null-deformation derivative of $K=-2\pi D$ along the scaling is, by the **§8.4 Borchers identity** (analytically continued $t\to-\tfrac i4$),
$$\Delta^{1/4}U(s)\Delta^{-1/4}=e^{-sP}\quad\Longleftrightarrow\quad \int T_{uu}\ \text{“}=\text{”}\ P,$$
i.e. the modular sum rule identifies the averaged null energy with the translation generator $P$. **Positive energy enters here, at step (iv):** the identification "modular-deformation $=$ energy" $=$ "$\Delta^{it}$ is the geometric scaling" $=$ "$\mathcal V_s\subset\mathcal V$ is $+$hsm" $=$ "$e^{-sP}$ bounded" $=$ $P\succeq0$ $=$ **RH**. 

Equivalently, **the §8.2 firewall is exactly the obstruction.** The unconditional entropy facts (i)+(ii) live on the **modular** side ($K=-\log\Delta$, KMS-symmetric, $\langle\text{even}|K|\text{even}\rangle=0$, spectrum symmetric — verified `probe_modular_borchers_obstruction.py`). Arch-domination lives on the **energy** side ($H_{\mathrm{OS}}=P\succeq0$, $=$ the Weil form $Q(g)$, §8.7). **§8.2: $K\ne H_{\mathrm{OS}}$.** So $S_{\mathrm{rel}}\ge0$ (a $K$-statement) does **not** give $Q(g)\ge0$ (an $H_{\mathrm{OS}}$-statement); Longo's bridge (iii) "$S_{\mathrm{rel}}=$const$\cdot$energy" holds **only in the chiral/positive-energy reference**, and the primes' breaking of B–W (§8.3a) is exactly what severs it. 

Sharpest form: in the ANEC argument the boundary term is the **asymptotic relative entropy** as the cut $\to\infty$ (the $s\to\infty$ scaling limit). ANEC needs it to vanish; **its vanishing $=$ $e^{-sP}$ bounded in the limit $=$ positive energy $=$ RH.** Positive energy is *the asymptotic boundary term of the relative entropy.*

## 4. Verdict — circular, but pinpointed, and unifying

- **Circular (FH-guillotine confirmed).** The arithmetic ANEC reduces arch-domination to relative-entropy positivity+monotonicity (unconditional) **plus** the $+$hsm/B–W identification (§8.4), which **is** $P\succeq0=$ RH. No escape.
- **Pinpointed.** Positive energy enters at a *single* step — the $K\to H_{\mathrm{OS}}$ bridge (the §8.2 firewall $=$ §8.4 Borchers $=$ $+$hsm $=$ the asymptotic boundary term). Every unconditional ingredient sits strictly on the modular ($K$) side of that firewall.
- **Unification deposit (genuine).** The route welds the program's faces into one identity:
$$\text{arch-domination}=\text{arithmetic ANEC}=\text{modular sum rule}=\textstyle\int T_{uu}=P\succeq0=\text{(§8.4) }e^{-sP}\text{ bounded}=\text{(§8.7) pole-driven margin}=\text{(N14) }S_{\mathrm{rel}}\text{ bridge}.$$
The CCM/operator thread (§8), the stress-tensor thread (P∞), the entropy thread (N14), and the explicit-formula thread (§8.7) are **one statement**, with the RH-content isolated at the $+$hsm step.

## 5. The SSA offshoot — TESTED, thin (RH-insensitive)  **[RETIRED]**

*Certificate: `empirical/probe_arch_domination_ssa_convexity.py`.* The hope: strong subadditivity (Lieb–Ruskai) on nested scaling intervals $\to$ an unconditional **scale-convexity** of the arithmetic relative entropy, possibly a new constraint "like Rodgers–Tao $\Lambda\ge0$." **Tested → thin.** The scale-convexity is $\Theta''(s)=\sum_n\omega_n^2 e^{-s\omega_n}$, and **every term is convex for any real $\omega_n$ — including $\omega_n<0$ (an off-line zero / RH violation)**, since $\partial_s^2 e^{-s\omega}=\omega^2e^{-s\omega}>0$ regardless of $\mathrm{sign}(\omega)$. Verified: the RH-FALSE spectrum (negative mode) is convex *more* strongly than the RH-true one ($\Theta''=112$ vs $10^{-22}$ at $s=0.3$). So **scale-convexity is automatic and RH-INSENSITIVE** — it does not constrain the zeros to the line. It is **not** a $\Lambda\ge0$ analogue ($\Lambda\ge0$ is a genuine *zero-side* heat-flow result that detects RH; the entropy convexity lives on the modular ($K$) side and detects nothing without the Bisognano–Wichmann bridge $=$ positive energy $=$ RH — the same §8.2 firewall). The RH content is in **boundedness** (§8.7, $e^{-sP}$ bounded $=P\succeq0$), **not convexity**. SSA is therefore the QNEC/local face of this diagnostic, same firewall; **no new constraint.** Retired.

## 6. Honest status

C is **retired as a closure route** (circular, FH-guillotine), exactly like A — but unlike A it leaves two deposits: (a) the *pinpoint* — positive energy enters at the single $+$hsm/§8.2-firewall step, as the asymptotic boundary term of the relative entropy (the cleanest localization the program has of "where RH lives" in the modular/entropy language); (b) the *unification* — six faces collapse to $\int T_{uu}=P\succeq0$. The one non-relabel offshoot, **arithmetic SSA**, is a candidate *new unconditional constraint* (not a closure), the single follow-up worth a probe.

---

**Anchors.** Faulkner–Leigh–Parrikar–Wang 2016 (ANEC from relative entropy); Ceyhan–Faulkner 2020 (modular sum rule, half-sided inclusions); Longo 2019 / Casini–Grillo–Pontello (coherent-state entropy $=$ energy); Lieb–Ruskai 1973 (SSA); Bisognano–Wichmann, Wiesbrock (modular $=$ boost iff positive energy). Program: N14 (Weil $=$ relative entropy), P∞ (stress tensor, arch-domination $=$ energy condition), §8.2 (firewall $K\ne H_{\mathrm{OS}}$, `probe_modular_borchers_obstruction.py`), §8.3/8.4 (Borchers $+$hsm, $e^{-sP}$), §8.7 (pole-driven margin, `probe_explicit_formula_heat_kernel.py`), `ArchDomination-Brainstorm-Draft1.md` (idea C).
