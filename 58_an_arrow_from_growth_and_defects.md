# 58 — An Arrow from Growth and Defects: Capacity, Curvature, and the Low-Entropy Past on Networks of Ports

**Leonardo Murillo Montero**

*ITCR, UNA, UCR*

*First draft — October 2, 2026*

<!--
INTERNAL LOG — NOT FOR PUBLICATION (pandoc drops HTML comments)
2026-10-02 v0.1.  Request (Leo): "set up Paper 58 with those two tests", after a discussion of the past hypothesis and his
intuition of a recursive regime of spacetime phases (our universe as a black hole in a lighter parent phase; the low
initial entropy as inherited from a lighter network with lower configuration density).  That intuition is recorded,
sharpened and fenced in Section 5; the technical body tests the two network mechanisms it needs.
Certificate empirical/arrow58/p58_cert.py (K/L pre-registered before run 1):
  run 1: 3/6 -- K1a, K2a, K2b PASS; K1b-K1d FAILED on a pre-registration DESIGN ERROR ("split the stiffest bond" re-splits
         the new bonds without end; stiffness ~2^64; relaxation overflow).  Retained.
  run 2 (POST-DIAGNOSIS, NOT BLIND; uniform refinement = split the softest bond): 5/6 -- K1d FAILED, retained: retention
         at tau = 1e-3 is 0.092, not > 0.5 (freeze-out happens near tau ~ 1e-4; the log term of J relaxes as soon as the
         variance deficit fills).  Its other branch, f(10) < 0.05, passed (f = 1/64: only the last insertion survives).
Excluded from the technical body: claims about our universe; RH; consciousness.
-->

---

## Abstract

The second law needs a low-entropy past, and the Port Principle assumes it: every lift starts from passive reference states. We test, on networks of ports, two mechanisms that can replace a fine-tuned initial state with properties of a network. *Low* entropy then means low *relative to the network's capacity*.

**(1) Growth makes an arrow [P].** Refine a harmonic chain by splitting a bond of stiffness $k$ into two bonds of stiffness $2k$. This is a Kron reduction, so the old nodes' thermal state is exactly unchanged: the network gains capacity without changing its coarse state. Insert the new node at the midpoint of its neighbours with variance $\varepsilon$. The arrow resource — the relative entropy to the current thermal state, $\beta$ times the available work — then rises by exactly
$$J=\tfrac12\Big(\tfrac{\varepsilon}{s}-1-\ln\tfrac{\varepsilon}{s}\Big),\qquad s=\frac{T}{4k},$$
whatever the prior state. It is zero only for a thermal insertion. Relaxation can only spend this resource.
- Under fast growth the resource accumulates (115.7 nats after 64 cold insertions).
- Under slow growth only the most recent insertion's share survives.
- The arrow therefore lasts while capacity grows faster than the network relaxes. Freeze-out sets in when the insertion interval falls below about $10^{-4}$ of the fastest local relaxation time; our pre-registered guess, $10^{-3}$, missed, and the miss is retained.

**(2) Defects carry entropy [P, exact integers].** On a triangulated torus, a Pachner edge flip creates a 5–5–7–7 disclination quadrupole at fixed node and bond count. Every such defect lowers the spanning-tree count, and so raises the field's thermal entropy at fixed temperature, by $0.023$ nats per quadrupole, additively. In 30 random samples the defect-free network is always the entropy minimum. That gives Penrose's Weyl-curvature hypothesis — a low-entropy universe is a smooth one — a concrete carrier: the uniform network.

**A fenced reading [C].** A new phase of the network starts small and defect-free, with low gravitational entropy and small capacity. It grows, and its maximal entropy outruns its entropy. Gravity spends the gap by writing defects. By the Port Principle, every black hole must radiate at its temperature: Hawking radiation is Kirchhoff's law at a horizon. We state where this picture meets known obstructions, and which tests come next.

---

## 1. What is assumed, and what is tested

The Port Principle and Papers 54–57 derive the form of thermodynamics from passivity. Passivity, however, is an assumption about reference states, and the time lift selects a direction of time without explaining why there was work to spend (PortPrinciple.md, §14). Two classical responses frame this paper:
- **Penrose (1979).** The early universe was close to thermal in its matter but extremely smooth. Its gravitational entropy was minimal, and clumping later raised it.
- **Frautschi (1982); Layzer (1976).** In an expanding universe the maximal entropy grows. If it grows faster than relaxation can follow, an entropy gap opens without a fine-tuned start.

A network of ports gives each response a carrier. *Capacity* is the number of nodes and bonds: the cut law bounds entropy by bonds (Paper 55, Theorem 4.2), and curvature is a bond deficit (Paper 56). We test growth (Section 2) and defects (Section 3).

**Tiers.** [P] proven (exact identity or exact integer computation); [numerics]; [A] structural reading; [C] conjecture, fenced.

---

## 2. Growth makes an arrow

**Setting.** A chain of harmonic nodes sits between two walls, with bond stiffnesses $k_b$ and temperature $T$. Its port dynamics is the overdamped Langevin equation $dx=-\gamma Kx\,dt+\sqrt{2\gamma T}\,dW$, whose thermal state is $\Sigma_{\rm eq}=TK^{-1}$ (PortPrinciple.md, Proposition 11.1). The arrow resource is
$$D(t)=D\big(\rho_t\,\big\|\,\mathcal N(0,\Sigma_{\rm eq}(t))\big)=\beta\big(F(\rho_t)-F_{\rm eq}\big),$$
the work available against the current thermal state (PortPrinciple.md, Corollary 6.13; Paper 54, Theorem 1(d)).

**Growth rule.** Split a bond of stiffness $k$ into two bonds of stiffness $2k$, with a new node between them. Its proper length is unchanged (a spring of stiffness $k$ is two springs of $2k$ in series), so this is a refinement: more nodes, more modes, more capacity, the same geometry. Insert the new node at the midpoint of its neighbours with variance $\varepsilon$.

**Theorem 1 (the growth identity) [P].**
- **(a) Kron.** After the split, the thermal state's marginal on the old nodes equals the old thermal state. Integrating out the new node is a Kron reduction, which turns two springs $2k$ in series back into one spring $k$ (Paper 55, Theorem 2.2(c)).
- **(b) The jump.** If the new node is inserted as $x_{\rm new}=\tfrac12(x_a+x_b)+\xi$ with $\xi\sim\mathcal N(0,\varepsilon)$ independent of everything, then for *every* prior state
$$D_{\rm after}-D_{\rm before}=J(\varepsilon/s)=\tfrac12\Big(\tfrac\varepsilon s-1-\ln\tfrac\varepsilon s\Big)\ \ge0,\qquad s=\frac T{4k},$$
with equality iff $\varepsilon=s$, the thermal conditional variance.
- **(c) Spending.** Between insertions the dynamics preserves $\Sigma_{\rm eq}$, so $D$ is non-increasing (data processing). Hence after $N$ insertions $D\le NJ$, with equality iff there is no relaxation.

*Proof.* (a) Schur complement. (b) By the chain rule of relative entropy, $D_{\rm after}=D_{\rm before}+\mathbb E\,D\big(\rho(x_{\rm new}\,|\,\text{rest})\,\big\|\,\gamma(x_{\rm new}\,|\,\text{rest})\big)$; the marginal term is unchanged by (a). The thermal conditional of the new node depends only on its two neighbours (Markov property), with mean $\tfrac12(x_a+x_b)$ and variance $T/(4k)$, because its two bonds of $2k$ give it stiffness $4k$. The inserted conditional has the same mean and variance $\varepsilon$. The relative entropy of two Gaussians with equal means is $J$. (c) A Markov semigroup with stationary state $\gamma$ contracts $D(\cdot\|\gamma)$. $\square$

*Certificate p58* (K1a–K1c): thermal insertion changes $D$ by at most $2\times10^{-14}$; the cold-insertion jump equals $J$ to relative $1.3\times10^{-12}$ at each of 64 insertions, from any prior state; $D_{\rm final}\le NJ$ for every relaxation interval.

**Numerics: freeze-out.** Start from 8 nodes with $k=1$ at equilibrium ($D=0$). Grow to 72 nodes by uniform refinement (always split the softest bond), with cold insertions ($\varepsilon=s/100$, so $J=1.808$ nats each) and relaxation for a time $\tau$ before each insertion ($\gamma=T=1$):

| $\tau$ | 0 | $10^{-4}$ | $10^{-3}$ | $10^{-2}$ | $10^{-1}$ | 1 | 10 |
|---|---|---|---|---|---|---|---|
| retained fraction $f=D/(NJ)$ | 1.000 | 0.455 | 0.092 | 0.019 | 0.016 | 0.016 | 0.016 |
| entropy gap $S_{\rm eq}-S$ (nats) | 147.4 | 81.7 | 25.6 | 4.15 | 2.37 | 2.30 | 2.30 |

- Under fast growth the arrow accumulates: 115.7 nats, an entropy gap of 147 nats.
- Under slow growth, everything but the last insertion relaxes, and $f\to1/64$.
- The pre-registered freeze-out branch (K1d: $f>0.5$ at $\tau=10^{-3}$) **failed** and is retained; the crossover lies near $\tau\approx10^{-4}$. The reason: for very cold insertions, $J$ is dominated by $-\tfrac12\ln(\varepsilon/s)$. That term relaxes as soon as the variance deficit fills, which happens on a fraction $\sim\varepsilon/s$ of the local relaxation time $1/(4\gamma k)$, not on the whole of it.

**Reading [A].** In this model an arrow of time is a *growth effect*. Every insertion colder than thermal — a new mode born with "lower configuration density" than the phase it joins — adds a fixed amount of available work, independent of history. The arrow persists exactly as long as capacity grows faster than the network relaxes, which is Frautschi's mechanism with a microscopic carrier. When growth stops, the resource decays to zero: heat death is the end of growth, not the end of time.

---

## 3. Defects carry entropy

**Setting.** A periodic triangular network (torus, $L\times L$, unit bonds). An edge flip (Pachner 2–2 move) removes the bond $(u,v)$ shared by two triangles and adds the bond $(w,z)$ across them. The degrees become 5, 5, 7, 7: a disclination quadrupole with zero net curvature, at fixed node count $N$ and bond count $E$. For the massless classical field at temperature $T$ (zero mode removed),
$$S=\text{const}-\tfrac12\ln\det{}'K=\text{const}-\tfrac12\ln\big(N\,\tau(G)\big),$$
where $\tau(G)$ is the number of spanning trees (Kirchhoff's matrix-tree theorem; Paper 56, Proposition 2.5). So at fixed $N$ and $T$, the field's entropy rises exactly when the spanning-tree count falls.

**Proposition 2 (defects raise the field's entropy) [P, exact integers].**
- One flip lowers $\tau$ for $L=6,8,10$, by the factors $0.9519$, $0.9543$ and $0.9554$: $\Delta S=+0.0246$, $+0.0234$ and $+0.0228$ nats.
- On $L=8$, every one of 30 random networks with $k=1,\dots,6$ disjoint flips has fewer spanning trees than the defect-free network. The mean $\Delta S$ is $+0.0234\,k$ to within $0.6\%$: defect entropy is additive.
- The quantum thermal entropy ($T=1$, mass $m^2=0.1$) also rises for one flip, by $+0.020$ nats.

*Certificate p58* (K2a, K2b: Bareiss integer determinants; quantum value reported).

**Reading [A].** With matter in equilibrium, the smooth, defect-free network is the *least* entropic geometry at fixed size: it is the stiffest, with the most spanning trees, and so admits the fewest thermal fluctuations. Writing defects — the network form of curvature (Paper 56) — raises the entropy of the matter that lives on it, additively per defect. This is Penrose's ordering: a smooth beginning is a low-entropy beginning, and clumping raises entropy. The free energy $F=\tfrac T2\ln\det{}'K$ falls with each defect, so in this model defect formation is entropically favoured: there is a thermodynamic push toward curvature. This links to Paper 56's induced free energy, which is concave in the weights: matter softens geometry.

*What this does not show.* The geometric degrees of freedom are not given an entropy of their own here, and the energy cost of a defect is not modelled. The test fixes $N$ and $E$; in a growing network both change (Section 2). Combining the two mechanisms, growth with defect formation, is the next computation.

---

## 4. The two mechanisms together [A]

| | Penrose (smoothness) | Frautschi (capacity) |
|---|---|---|
| carrier on a network | defect-free bond network | node and bond count |
| result here | defects raise field entropy, $+0.023$ nats per quadrupole (Prop. 2) | cold growth adds $J$ per node exactly; the arrow survives while growth outruns relaxation (Thm 1) |
| what it replaces | a smooth initial state with no explanation | a fine-tuned low-entropy state |
| what it needs | an initial state without defects | growth faster than relaxation |

Together they say that, on a network of ports, a past of low entropy *relative to capacity* follows from two properties of a new phase: it is born small and smooth, and it grows. Neither is a statement about microscopic fine tuning.

---

## 5. A creation story, fenced [C]

The following is a hypothesis, recorded because it organizes the next tests. Nothing in it is claimed for our universe.

> A region of a parent network, compressed past a threshold, rewires into a new phase. In the new phase energy is stored in two conjugate forms, one on nodes and one on links, so its signature becomes Lorentzian and causal time begins (Paper 55, Theorems 3.5 and 3.8: a network without its second storage has no time direction, and an isolated node has no space). The new phase starts small and free of defects: its gravitational entropy is minimal (Section 3) and its capacity small. As it grows, its maximal entropy outruns its entropy (Section 2). That gap is the arrow of time, and gravity spends it by writing defects. Every black hole is a port into a deeper phase.

**Three anchors in proven results.**
- *Time can be born in a transition of phase.* Signature is decided by where energy is stored (Paper 55, Theorem 3.8): RC phase $(0,1,d)$, isolated nodes $(1,0,d)$, Lorentzian $(1,d)$.
- *A one-way port is forbidden.* A port that absorbs at temperature $T$ must emit at $T$, with emissivity equal to absorptivity (PortPrinciple.md, Theorem 8.1). Hawking's spectrum is exactly this: the emission in each mode is the absorption probability (greybody factor) times the Planck occupation (Hawking 1975). Hawking radiation is Kirchhoff's law for a horizon [A].
- *Low entropy is relative to capacity* (Section 2), and *smoothness is low entropy* (Section 3).

**Three obstructions.**
1. *The singularity is in the wrong place.* Inside a Schwarzschild black hole the singularity is in the future, while our Big Bang is in the past. Universe-in-a-black-hole models need a bounce (Pathria 1972; Popławski 2010; cf. Smolin 1992). On a network that would be a transition in rewiring or storage at maximal density, for which there is no theorem here.
2. *From outside, a black hole has maximal entropy.* The interior can be low-entropy only relative to its own future capacity, which is Section 2's sense, not the parent's.
3. *"A lighter phase" needs a definition.* The natural one is a different bond density, and therefore different constants: $c$ from the weights, $G=a_{\rm cell}/(4\eta_b)$ from the bonds (Paper 56). That is not tested.

**Prior art for the cosmological pictures.** Bubble nucleation behind a horizon (Farhi–Guth–Guven 1990); the no-boundary transition from Euclidean to Lorentzian signature (Hartle–Hawking 1983); cosmological natural selection, which makes falsifiable claims (Smolin 1992); a spontaneous, two-sided origin of the arrow (Carroll–Chen 2004).

---

## 6. Next tests

1. **Growth with defects.** Grow a triangulated network by refinement while allowing edge flips. Ask whether the total arrow (Section 2) and the defect entropy (Section 3) add, and whether defects form spontaneously under a passive rewiring rule.
2. **Storage transition.** Couple an RC network to inductive links that switch on past a threshold, and measure the emergence of a front at $1/\sqrt{LC}$: the birth of causal time.
3. **Hawking radiation as Kirchhoff's law, exactly.** In an LC line with a moving impedance step (an analogue horizon), show that the emitted noise equals temperature times the defect Gram of the port.
4. **Freeze-out law.** Derive the crossover $\tau_\ast$ of Section 2 in closed form, as a function of $\varepsilon/s$ and the local relaxation rate; the pre-registered guess was off by a factor of ten.

---

## 7. Certificate

`empirical/arrow58/p58_cert.py` (falsifiers in its docstring, written before run 1).

| Check | Content | Result |
|---|---|---|
| K1a | thermal insertion leaves $D$ unchanged | PASS ($2\times10^{-14}$) |
| K1b | cold insertion raises $D$ by exactly $J$, from any prior state | run 1 FAIL (design error, retained); run 2 PASS ($1.3\times10^{-12}$) |
| K1c | relaxation never increases $D$; $D\le NJ$ | run 1 FAIL (same); run 2 PASS |
| K1d | freeze-out: $f(10^{-3})>0.5$ and $f(10)<0.05$ | run 2 **FAIL, retained** ($f(10^{-3})=0.092$; $f(10)=1/64$ passed) |
| K2a | one flip lowers the spanning-tree count, $L=6,8,10$ | PASS (exact integers) |
| K2b | 30 defected networks all below the perfect one | PASS (exact integers) |

**Run log.** Run 1 (blind) passed 3/6. Its growth rule, "split the stiffest bond", re-split the bonds it had just created; one segment was refined without end, its stiffness reached about $2^{64}$, and the relaxation step overflowed. The rule intended — uniform refinement, the analogue of expansion — splits the softest bond. Run 2 (post-diagnosis, not blind) passed 5/6, with the K1d threshold miss retained.

---

## References

- S. M. Carroll, J. Chen, Spontaneous inflation and the origin of the arrow of time, arXiv:hep-th/0410270 (2004).
- E. Farhi, A. H. Guth, J. Guven, Is it possible to create a universe in the laboratory by quantum tunneling?, *Nucl. Phys. B* 339 (1990) 417.
- S. Frautschi, Entropy in an expanding universe, *Science* 217 (1982) 593.
- J. B. Hartle, S. W. Hawking, Wave function of the Universe, *Phys. Rev. D* 28 (1983) 2960.
- S. W. Hawking, Particle creation by black holes, *Commun. Math. Phys.* 43 (1975) 199.
- G. Kirchhoff, Über die Auflösung der Gleichungen, auf welche man bei der Untersuchung der linearen Vertheilung galvanischer Ströme geführt wird, *Ann. Phys. Chem.* 72 (1847) 497.
- D. Layzer, The arrow of time, *Astrophys. J.* 206 (1976) 559.
- R. K. Pathria, The universe as a black hole, *Nature* 240 (1972) 298.
- R. Penrose, Singularities and time-asymmetry, in *General Relativity: An Einstein Centenary Survey*, Cambridge, 1979.
- N. J. Popławski, Cosmology with torsion: an alternative to cosmic inflation, *Phys. Lett. B* 694 (2010) 181.
- L. Smolin, Did the universe evolve?, *Class. Quantum Grav.* 9 (1992) 173.
- Program: PortPrinciple.md (Cor 6.13, Thm 8.1, Props 11.1–11.2, §14); Paper 54 (Thm 1); Paper 55 (Thms 2.2, 3.5, 3.8, 4.2); Paper 56 (Prop 2.5, §§4–5); Paper 57.
