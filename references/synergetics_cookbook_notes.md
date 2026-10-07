# Synergetics Cookbook (Andy Thomson) — extraction & assessment

**Source:** A. R. Thomson, *The Synergetics Cookbook v0.14 — A Comprehensive Catalogue of
Quadray-Native Computational Methods for Tetrahedral Geometry.* Thomson Architecture / ABCD.EARTH.
Dated **2026.06.27**. DOI 10.13140/RG.2.2.14110.91207. CC BY-NC-SA 4.0. 81 pp.
Full text saved alongside this file as `synergetics_cookbook_v0.14_fulltext.txt`
(pdftotext -layout; **lossy on math glyphs** — √, θ, φ, superscripts often dropped; prose & structure intact).

> Cites **our 01 paper** as ref [11] (Murillo 2026, Zenodo 19689050). Mutual: our 01 §1.1 cites
> Thomson's Spread-Quadray Rotors [Thomson, §19]. See `synergetics_cookbook_connection.md`-style notes
> in chat / memory `reference_synergetics_cookbook_thomson`.

---

## 1. One-paragraph thesis

Cartesian XYZ is "optimized for the cube"; describing the tetrahedron in it costs irrational
coordinates (the √3 to "name what the tetrahedron already is"). Quadray/ABCD coordinates — four
basis vectors **A,B,C,D** to the vertices of a regular tetrahedron, `A+B+C+D=0` — make the whole
integer-family (tet, dual, cube, octa, rhombic dodecahedron, cuboctahedron) **integer-exact**, the
golden family **Q(φ)-exact**. The Cookbook catalogues a complete geometry/render kernel that performs
every operation natively in ABCD with **no "Cartesian roundtrip,"** the only surviving Cartesian
being the irreducible f32 GPU upload + OS pixel grid. Two intellectual parents: **Fuller's Synergetics**
(tetrahedral coordinate thinking) and **Wildberger's Rational Trigonometry** (quadrance `Q=d²`,
spread `s=sin²θ` → rational polynomial arithmetic, no transcendentals). Implemented in ABCD.EARTH:
61+ polyhedra generators, ~1426 tests.

## 2. The unified engine (everything else is a specialization)

| Primitive | Object | Section |
|---|---|---|
| **Metric tensor** | `M = 4I − J` (= Gram matrix `B·Bᵀ` of the Tom Ace basis). `Q(p)=4Σpᵢ²−(Σpᵢ)²`. Spread, dot, dihedral all from this one bilinear form. | §5 |
| **Pseudo-inverse / height functions** | `B† = Bᵀ/4` (since `BᵀB=4I₃`). Three rows = edge-pair-midpoint directions `hX,hY,hZ` = "Cartesian axes discovered intrinsically." Grid, plane constraints, projection. | §6–7 |
| **Rotation** | `K(u)` (**our** intrinsic cross-product) + Rodrigues `R(u,θ)=I+sinθ K(u)+(1−cosθ)K(u)²`. F/G/H circulant (vertex C₃ axes) and EdgeAxis V₄ half-turns fall out as exact-rational specializations. | §9 |
| **Convex hull** | orientation = sign of a 3×3 determinant on **zero-sum-normalized** coords; integer polyhedra → exact integer determinants, no FP degeneracy. Cayley–Menger area from quadrances. | §11 |
| **Projection** | `abcd_to_clip` matrix folds Tom Ace basis into view-projection; ABCD 4-vector → clip in one matmul. Inverse projection (cursor→ABCD) is its formal inverse. CAD/DXF export via D-axis ortho. | §10 |

## 3. Section-by-section content map

- **§2–4 Foundations.** Quadray basis (spread 8/9 between every pair = 109.47°). Standard Quadray
  (zero-sum + all-positive, ≅ℝ³) **vs ABCD.EARTH's relaxed signed extension** (native 4 DOF, ℝ⁴,
  negative coords meaningful). Tom Ace Cartesian map A↦(−1,−1,+1) etc. **Rationality Reciprocity**:
  cube-rational ⟺ tet-edge irrational, but `Qtet/Qcube=8/4=2` always integer (the √2 is invisible to RT).
  **Janus inversion** `J(P)=−P` (involution, tet↔dual); negative frequency F<0 scales *through zero*
  (the Janus Point) into Fuller's Negative Universe (star tetrahedron / stella octangula). 16 sign regions.
- **§5 Metric & "Fuller's constant 2."** Tetrahedral Pythagoras `Q=Q₁+Q₂+2⟨d₁,d₂⟩_M`; for unit
  tet edge the cross term is exactly **+2** (legs 3+3 = Wildberger, cross +2 = Fuller). Five "echoes of 2":
  Euler V+F=E+2; Fuller's poles of spinnability; constant relative abundance F=2(V−2),E=3(V−2);
  720° takeout (angular deficit); **Gauss–Bonnet** as the formal bridge (∫K dA = 2πχ = 720°).
  Honest caveat: first four are topological universals, the metric +2 is specific to the unit tet edge.
- **§6–7 Cartesian bridge & height functions / plane constraints / 6 Quadray planes.**
- **§8 Catalogue.** 61+ generators: Platonic (4 ℤ, 2 Q(φ)), 13 Archimedean (11 Q, 2 chiral f64),
  13 Catalan, 4 Thomson great-circle families, geodesics, helices, prisms/cones. Precision tracked per shape.
  **Niven's theorem**: only N∈{3,4,6} give rational spread → octahedron is "the complete rational polygon factory."
- **§9 Rotations (full).** F/G/H = inverse-DFT spectra of circulant matrices (C₃); EdgeAxis = C₄ with a
  Nyquist term. Cayley/Gibbs-vector closed-form **composition** (`r₃ = (r₁+r₂+K(r₁)r₂)/(1−⟨r₁,r₂⟩_M)`) —
  answers "our" §8.3 open composition question. Cayley NLERP interpolation; inverse Rodrigues; half-angle
  ABCD Hamilton (v4.3 production rotor, 16 mul/12 add, drift-bounded). **Gauge-sum discipline**:
  zero-sum-project axes on mixed-Janus polyhedra (cube etc.) before K(u). Note: codebase `K = −K_paper` sign bridge.
- **§10 Projection / §11 hull / §12 computational techniques** (deferred √, grid snap, ABCD cross via
  height-functions, face normals, dihedral spread, **central-angle bevel = 90°−180/n**, f64-throughout-then-
  downcast precision rule).
- **§13 Why exact coordinates matter.** *The strongest argument in the paper.* Polyhedral geometry is
  **combinatorial** (hull = sign of a determinant), not continuous; FP error of 1e-16 flips a sign → a
  *structurally different* polyhedron (missing face), with no self-correction / mid-course correction.
  "Magnitude precision ≠ combinatorial correctness." Integer ABCD makes V−E+F=2 and 720° exact *by construction*.
- **§14 Anti-patterns** (XYZ roundtrip, premature radicals, canonical-vs-zero-sum normalization in hull, etc.).
- **§15 CCP frequency** = volumetric grid count (8F³ spheres), not linear scale. IVM / Central Angle Grid.
- **§16 Geodesic subdivision** Quadray-native: barycentric lerp in ABCD + scale to target quadrance
  (one √ per vertex only, at radius termination). **Thomson great-circle / Weierstrass geodesics**:
  vertices on circumsphere by construction (√ count O(V)→O(planes)); the **Jitterbug** as continuous
  Weierstrass deformation.
- **§17 Tetravolumes.** Fuller hierarchy Tet=1, Cube=3, Octa=4, RD=6, VE=20 as **exact integers** via a
  determinant ratio (no √). Cross-checked by de Jong's quadrance-only `tv²` polynomial (Cayley–Menger).
  **Wildberger Bridge to S₃**: `S3 = csc θ_tet = √(9/8)`, `S3² = 1/s_tet = 9/8` rational — the 8/9 (spread)
  and 9/8 (volume dictionary) are one isogonal geometry read twice. A/B quanta modules (vol 1/24 each),
  Mites/Sytes/Coupler. Negative Janus arena (explosion slider −2..+2).
- **§18 The Knowledge Graph (= the UMC).** See §6 below.

## 4. Where our 01 paper is load-bearing (exact citations)

- §9.5 — `K(u)` is named "**Murillo's intrinsic cross-product operator**" (Def 3, the cyclic-difference 4×4).
- §9.5 Thm 4 — "**The cubic identity — Murillo Theorem 3.3**": `K(u)³ = −K(u)` (M-unit zero-sum u).
- §9.6 Prop 1 — "**Murillo Proposition 6.1**": the 9-property Rodrigues table (orthogonality, gauge
  fixation, det=+1, trace 2+2cosθ, hyperplane preservation, gauge equivariance, metric preservation, spectrum).
- §9.7 — the **9-multiplication apply kernel** ("headline performance result from Murillo §7").
- §9.10 — Cayley composition "answers **Murillo's §8.3 'Composition formulas' open question**."
- Metric convergence: his **M = 4I−J = 3G** (our `G=(4/3)I−(1/3)J`). His M-unit axes are rational
  (¼[±1,±1,∓1,∓1]); our √3/4 is "because his convention normalizes against a Euclidean metric — the
  irrational factor drops out under the M-metric." We already use M:=3G=4I−J in 01 §3.5 (the τᵢ, projectors `I+K(τᵢ)²`).

## 5. Honest assessment — potential & limits

**Genuinely strong:**
- The **exactness-as-combinatorial-correctness** thesis (§13) is sound and well-argued; it's the real value prop.
- **Unified small engine**: one metric + one pseudo-inverse + one rotation primitive; F/G/H, V₄, hull,
  projection are all specializations. "Code shrinks ⇒ truer" as a falsifiable design test (Forward).
- Strong scholarship welding Fuller ↔ Wildberger ↔ Euler/Descartes/Gauss–Bonnet, with tiered honesty
  (topological-universal vs metric-specific +2; "operationally native vs semantically XYZ-equivalent").
- A **working, tested** non-Cartesian render pipeline incl. ABCD-native camera matrix and CAD export.

**Caveats to keep in view:**
- *"ABCD-native" is partly semantic.* Thomson concedes it (§5.1): `pᵀMq = (Bp)·(Bq)` = Cartesian dot of
  the images. The genuine novelty is **exactness/rationality + permutation symmetry + structural disclosure**,
  not a new geometry. (Same status as our 01: a *presentation*, isometric to the Cartesian theory.)
- *Exactness is a regular-simplex / golden-field phenomenon.* Arbitrary rotations, chiral snubs → f64.
  Holds for the symmetric family, not universally (the planned **surd hull** Q(√2,√3) would extend it).
- *"4D" is Fuller's structural sense*, not a spatial dimension (well-disclosed).
- *The UMC / knowledge-graph framing is visionary* — separate the solid engineering (the kernel, the tests)
  from the interpretive "Fuller specified this in 1975" reading (defensible but generous).

**Where it could go / why it matters to us:**
- Immediate practical payoff: **CAD/fabrication kernel** for tensegrity, geodesic domes, space frames —
  exact strut/panel schedules, bevel-per-valence, DXF/SVG. Already real.
- **Exact computational geometry** (CGAL-like combinatorial robustness) native to the tetrahedral family.
- For our program: an **engineering-grade, independently-tested deployment** of the simplicial-coordinate
  line — our K(u)/cubic-identity/Rodrigues/9-mul are load-bearing in a live system. The information-geometry
  hooks (our 01 §3.5/Cor 3.9: Fisher metric = M, the uniform Amari–Chentsov cubic from `I+K(τᵢ)²`) are the
  bridge from this Quadray world into our T-series / cubic-info-geometric-mechanics papers.

## 6. The UMC / Knowledge Graph (§18) — the subject of Thomson's public post

`knowledge_graph.rs` lays the **codebase + the entire Synergetics corpus** on **nested rational shells**
(Shell 0 Alpha tetrahedron; Shell 1 ideas — quadrance/spread/F,G,H; Shell 2 forms — Platonics…; Shell 3
instances — camera/render/state). Shell capacities are exact integer formulas (RD/FCC shell = 10ν²+2;
tet shell = ⅙ν(ν+1)(ν+2)); corpus on an outer RD shell of frequency 6 (252 = 10·6²+2 slots).
Each node placed at an integer/rational ABCD lattice point, projected by the same `abcd_to_clip`.
**Claims are run, not cited**: a §-reference that fails to resolve in embedded fulltext = provenance
regression caught automatically; executable claims name the test that runs them.
**Janus coins / complementary storage**: every concept is the *other face* of the module that embodies
it; "opposite" is an **exact, addressable, self-inverse involution** (run, not inferred) — explicitly
contrasted with learned embeddings where "opposite" is a fuzzy direction "not guaranteed to return home
when applied twice." Thomson identifies this with Fuller's **Ultra Micro Computer** (Synergetics §427.16–.17,
"Nuclear Computer Design"): a substrate to RECEIVE/STORE/RETRIEVE/**CONSTELLATE** info, broadcasting on
the VE's 25 great circles, holding on the icosahedron's 31, keyed by Mite/Coupler. Fuller assumed hardware;
Thomson's claim: it's software, and the running graph contains a node literally named `ultra_micro_computer`.

## 7. References list in the Cookbook (selected)
[2] Wildberger, *Divine Proportions* (2005). [3] Notowidigdo–Wildberger, *Tetrahedral Chromogeometry*
(arXiv:1909.08814). [4] Fuller, *Synergetics* (1975). [5] Edmondson, *A Fuller Explanation* (1987).
[6] Urner (Quadray origin). [7] Tom Ace (basis map). [8] Thomson, *Geometric Janus Inversion* v10.6.
[9] Thomson, *Spread-Quadray Rotors* v3.0. [10] Thomson, *4D± Prime Projection Conjecture* v5.1.
[11] **Murillo, *Intrinsic Vector Calculus on Simplicial (Quadray) Coordinates*, Zenodo 19689050.**
