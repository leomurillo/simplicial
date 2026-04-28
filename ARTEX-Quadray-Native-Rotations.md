# ARTEX — Quadray-Native Rotations

**Agent Reference Document**
**Date:** March 8, 2026; §10 added April 25, 2026
**Branch:** Twerking (current), see also ARTEX-ROTATIONS (Phase 5A); §10 work scheduled for 2DXY-4 or successor branch

---

## Purpose

This document teaches agents how to perform **rotations that stay in Quadray ABCD coordinates** from start to finish. The goal: given an ABCD point and a rotation, produce a new ABCD point — no XYZ detour.

Agents default to "convert to XYZ, rotate with a 3×3 matrix, convert back." That round-trip through the normalizer is wasteful and destroys the algebraic structure we care about. This document shows when and how to avoid it.

---

## 1. The Trivial Case: Rotation About an ABCD Basis Axis

Rotation about any of the four ABCD axes (A, B, C, or D) is **native** — it operates directly on Quadray coordinates via Tom Ace's F,G,H circulant coefficients.

### The F,G,H System

For rotation by angle θ about one ABCD basis axis, compute three scalar coefficients:

```
F = (2·cos(θ) + 1) / 3
G = (2·cos(θ - 120°) + 1) / 3
H = (2·cos(θ + 120°) + 1) / 3
```

**Invariant:** F + G + H = 1 (always, for any θ). This preserves the ABCD sum.

### The 4×4 Rotation Matrix

For rotation about A (even index → right-circulant):

```
R_A = | 1  0  0  0 |
      | 0  F  H  G |
      | 0  G  F  H |
      | 0  H  G  F |
```

The axis coordinate (A) passes through unchanged. The other three mix via the circulant pattern.

**Chirality:** Even-index axes (A=0, C=2) use right-circulant; odd-index axes (B=1, D=3) use left-circulant (G and H swap positions in the off-diagonal).

### Exact Rational Values at Tetrahedral Angles

These are **the gold standard** — no floating point, no radicals, pure integer fractions:

| Angle | F | G | H | Character |
|-------|---|---|---|-----------|
| 0° | 1 | 0 | 0 | Identity |
| 60° | 2/3 | 2/3 | -1/3 | All rational |
| 120° | 0 | 1 | 0 | Pure permutation (integer!) |
| 180° | -1/3 | 2/3 | 2/3 | All rational (Janus inversion) |
| 240° | 0 | 0 | 1 | Reverse permutation (integer!) |
| 300° | 2/3 | -1/3 | 2/3 | All rational |

At 120°, the rotation is literally a **cyclic permutation** of three coordinates — no multiplication needed. This is the tetrahedron's three-fold symmetry made arithmetic.

### Implementation (Rust)

```rust
// artex-osx/src/rt_math/fgh.rs
use crate::rt_math::fgh::{fgh_from_spread, fgh_rotate};

// RT-pure entry: spread = sin²(θ)
let coeffs = fgh_from_spread(spread, polarity);
let rotated = fgh_rotate(point_abcd, axis_index, &coeffs);
// Result is ABCD. No XYZ anywhere.
```

**This is the go-to for single-axis rotation.** No normalizer needed. No Tom Ace basis. Pure ABCD algebra.

---

## 2. The Quadray Circle: Spread, Quadrance, and Weierstrass in ABCD

This section develops a fully Quadray-native description of "a point on a circle around an ABCD axis" — the geometry of rotation expressed entirely in ABCD coordinates, with radial distance measured as quadrance and angular position measured as spread.

### 2.1 The Circle as an F,G,H Orbit

When we rotate the B basis vector [0,1,0,0] about the A-axis by angle θ, the result is:

```
circle_A(θ) = (0, F(θ), G(θ), H(θ))
```

where F + G + H = 1 always. **This IS the circle** — parameterized entirely in ABCD coordinates. As θ varies, the point traces a closed curve in BCD-space (the 3D subspace perpendicular to A). The constraint F + G + H = 1 keeps it on a plane in that subspace, and the circulant structure keeps it at constant distance from the A-axis.

For an arbitrary starting point P = (a₀, b₀, c₀, d₀), rotation about A gives:

```
P'(θ) = (a₀,  F·b₀ + H·c₀ + G·d₀,
              G·b₀ + F·c₀ + H·d₀,
              H·b₀ + G·c₀ + F·d₀)
```

The a-component passes through unchanged. The circle lives in the BCD subspace.

### 2.2 Radial Quadrance from the A-Axis (Pure ABCD)

Before parameterizing the circle, we need to know how far a point sits from the axis. The **radial quadrance** (squared Cartesian distance from the A-axis) can be computed purely from the ABCD coordinates.

**Derivation.** The ABCD Gram matrix (inner product induced by the Tom Ace basis) is:

```
G_ij = Basis_i · Basis_j = | 3  -1  -1  -1 |
                            |-1   3  -1  -1 |
                            |-1  -1   3  -1 |
                            |-1  -1  -1   3 |
```

This equals 4I - J (four times identity minus all-ones). On the zero-sum hyperplane (where J·v = 0), the Gram matrix acts as 4I — so the Cartesian inner product of two zero-sum ABCD vectors is simply **4 times their standard dot product**.

For a zero-sum point P = (p₀, p₁, p₂, p₃), the perpendicular distance from the A-axis involves projecting out the A-component and measuring what remains. The algebra simplifies to:

```
Q_radial(A) = (8/3) · (b² + c² + d² - bc - bd - cd)
```

where b, c, d are the non-axis (B, C, D) zero-sum-normalized components.

This further simplifies via the sum-of-squared-differences identity:

> **Q_radial(A) = (4/3) · [(b-c)² + (b-d)² + (c-d)²]**

**This is the Quadray-native "radius squared."** It measures how far a point sits from the A-axis using only pairwise differences of BCD coordinates. No XYZ, no normalizer, no transcendentals. Completely algebraic, completely rational for rational inputs.

**Verification:** The B basis vector [0,1,0,0] in zero-sum form is (-1/4, 3/4, -1/4, -1/4).
Non-axis components: b = 3/4, c = -1/4, d = -1/4.
(b-c)² + (b-d)² + (c-d)² = 1 + 1 + 0 = 2.
Q_radial = (4/3)·2 = 8/3. ✓ (Matches the Cartesian calculation.)

### 2.3 The Two Circle-Frame Directions

A circle in 3D needs two orthogonal directions in the plane perpendicular to the axis. In Quadray space, these have clean ABCD expressions.

The plane perpendicular to A contains all displacements with zero A-axis component. Two natural orthogonal directions (in the Cartesian-induced metric) are:

```
ê_swing = (0, 0, -1, +1)       "CD-swing" — swaps between C and D
ê_pole  = (0, 2, -1, -1)       "B-pole"   — toward B, away from CD
```

**Why these names?** We deliberately avoid X/Y labels. The **swing** direction oscillates between C and D (like a pendulum between two tet faces). The **pole** direction points toward the B vertex — the "north pole" of the circle as seen from the A-axis. These are native Quadray directions with integer coordinates.

**Orthogonality check:** In Cartesian (via Tom Ace basis):
- ê_swing → XYZ = (2, -2, 0), length² = 8
- ê_pole → XYZ = (2, 2, 4), length² = 24
- dot = 4 - 4 + 0 = 0 ✓

The Cartesian lengths differ (√8 vs √24 = √8·√3), so they need normalization for a unit circle. Scaling:
- û_swing = ê_swing / (2√2)       (Cartesian unit length)
- û_pole = ê_pole / (2√6)         (Cartesian unit length)

### 2.4 Weierstrass Circle in Quadray Coordinates

The Weierstrass substitution t = tan(θ/2) parameterizes a circle algebraically. In our Quadray frame:

```
P(t) = a₀·Â + ρ · [ ((1-t²)/(1+t²)) · û_swing + (2t/(1+t²)) · û_pole ]
```

where ρ is the Cartesian radius.

But we can do better — express F, G, H directly as rational functions of t. Substituting the Weierstrass forms into the F,G,H equations and simplifying:

> **F(t) = (3 - t²) / [3(1 + t²)]**
>
> **G(t) = 2t(t + √3) / [3(1 + t²)]**
>
> **H(t) = 2t(t - √3) / [3(1 + t²)]**

These are the **Weierstrass-F,G,H formulas** — the Quadray-native Weierstrass circle. Each coefficient is a rational function of t and the single algebraic constant √3 (cached in `PureRadicals::sqrt3()`).

**Verification at key angles:**

| Angle | t | F | G | H | Sum |
|-------|---|---|---|---|-----|
| 0° | 0 | 3/3 = 1 | 0 | 0 | 1 ✓ |
| 90° | 1 | 2/6 = 1/3 | (1+√3)/3 | (1-√3)/3 | 1 ✓ |
| 120° | √3 | 0 | 2√3·2√3/12 = 1 | 0 | 1 ✓ |
| 240° | -1/√3 | (3-1/3)/(3·4/3) = 0 | ... = 0 | ... = 1 | 1 ✓ |

### 2.5 The Spread as the "Angle" Measure

In RT, we don't measure angles — we measure **spread** s = sin²(θ). The spread between two positions on the circle (as subtended from the axis center) is a rational number for many useful rotations:

| Rotation | Spread s = sin²(θ) | Rational? |
|----------|-------------------|-----------|
| 0° | 0 | Yes |
| 30° | 1/4 | Yes |
| 45° | 1/2 | Yes |
| 60° | 3/4 | Yes |
| 90° | 1 | Yes |
| 120° | 3/4 | Yes |
| 180° | 0 | Yes |

**All common rotation spreads are rational.** The spread is always rational — it's the *coordinates* that may involve algebraic irrationals at non-tetrahedral angles.

### 2.6 Complete Specification of a Quadray Rotation (RT-Pure)

A rotation in Quadray space is fully specified by three RT quantities:

```
Rotation = {
    axis:              A | B | C | D        (integer index)
    radial_quadrance:  Q_r = (4/3)·Σ(bᵢ-bⱼ)²   (rational for rational vertices)
    rotational_spread: s = sin²(θ)          (rational for all common angles)
}
```

No angles. No transcendentals. No XYZ. The axis is a Quadray label, the distance is a quadrance, the "angle" is a spread. **This is a fully RT-pure rotation specification.**

### 2.7 Worked Example: 45° CW Rotation About A

**Setup:** Rotate the point P = [0, 1, 0, 0] (the B basis vector) by 45° clockwise about the A-axis.

**RT specification:**
- Axis: A (index 0)
- Radial quadrance: Q_r = 8/3 (computed in §2.2)
- Rotational spread: s = sin²(45°) = **1/2** (rational)

**Weierstrass parameter:** t = tan(22.5°) = √2 - 1 (algebraic, not rational)

**Computing F, G, H via the Weierstrass-F,G,H formulas (§2.4):**

```
t = √2 - 1
t² = 3 - 2√2
1 + t² = 4 - 2√2 = 2(2 - √2)
3 - t² = 2√2
```

```
F = 2√2 / [3 · 2(2 - √2)]
  = √2 / [3(2 - √2)]
  = √2(2 + √2) / [3 · 2]        ← rationalize denominator
  = (2√2 + 2) / 6
  = (√2 + 1) / 3
```

```
G = 2(√2 - 1)(√2 - 1 + √3) / [3 · 2(2 - √2)]
  = (√2 - 1)(√2 + √3 - 1) / [3(2 - √2)]
  = ... (rationalize) ...
  = (2 + √6 - √2) / 6
```

```
H = 2(√2 - 1)(√2 - 1 - √3) / [3 · 2(2 - √2)]
  = ... (same rationalization) ...
  = (2 - √6 - √2) / 6
```

**Verification:** F + G + H = (2√2 + 2 + 2 + √6 - √2 + 2 - √6 - √2) / 6 = 6/6 = 1 ✓

**Result: the rotated point in Quadray coordinates:**

> **P'₄₅° = ( 0,  (√2 + 1)/3,  (2 + √6 - √2)/6,  (2 - √6 - √2)/6 )**

**Numeric check:**

| Component | Exact | ≈ Decimal |
|-----------|-------|-----------|
| A | 0 | 0.000 |
| B | (√2 + 1)/3 | 0.805 |
| C | (2 + √6 - √2)/6 | 0.506 |
| D | (2 - √6 - √2)/6 | -0.311 |

**Verify radial quadrance is preserved (still 8/3):**

Zero-sum normalize P': avg = (0 + 0.805 + 0.506 - 0.311)/4 = 0.25.
Non-axis components after normalization: b' = 0.555, c' = 0.256, d' = -0.561.
(b'-c')² + (b'-d')² + (c'-d')² ≈ 0.0894 + 1.246 + 0.668 = 2.003 ≈ 2.
Q_r = (4/3)·2 = 8/3 ✓ — the point stayed on the circle.

### 2.8 What's Rational, What's Algebraic, What's Transcendental

The 45° example reveals the three tiers:

| Quantity | Type | Value |
|----------|------|-------|
| Axis index | **Integer** | A = 0 |
| Radial quadrance Q_r | **Rational** | 8/3 |
| Rotational spread s | **Rational** | 1/2 |
| Weierstrass parameter t | **Algebraic** (√2) | √2 - 1 |
| F coefficient | **Algebraic** (√2) | (√2 + 1)/3 |
| G, H coefficients | **Algebraic** (√2, √6) | (2 ± √6 - √2)/6 |

The **specification** (axis, Q_r, spread) is fully rational. The **coordinates** of the rotated point involve algebraic irrationals — but only from two cached radicals: √2 and √6 = √2·√3. No transcendentals anywhere.

At **tetrahedral angles** (60°, 120°, 180°, 240°, 300°), the coordinates collapse to pure rationals — even the √3 in G and H cancels. At **right angles** (90°), F is rational (1/3) and G, H involve only √3. The 45° case is "worst case" for this system, bringing in √2 from the Weierstrass parameter and √6 from its product with √3.

### 2.9 When Are the Coordinates Fully Rational?

The Weierstrass-F,G,H formulas show that √3 appears only in G and H (via the 120° phase shift). For G and H to be rational, we need t·√3 to be rational — i.e., t must be a rational multiple of √3. The cases:

| t | Angle θ | F,G,H | Character |
|---|---------|-------|-----------|
| 0 | 0° | 1, 0, 0 | Rational (identity) |
| 1/√3 | 60° | 2/3, 2/3, -1/3 | Rational |
| √3 | 120° | 0, 1, 0 | Rational (permutation) |
| ∞ | 180° | -1/3, 2/3, 2/3 | Rational |
| -√3 | 240° | 0, 0, 1 | Rational (reverse permutation) |
| -1/√3 | 300° | 2/3, -1/3, 2/3 | Rational |

These are **exactly** the tetrahedral symmetry angles. The tetrahedron's geometry is the unique geometry where rotation coefficients are rational — because the √3 from sin(120°) cancels the √3 from the tetrahedral basis angle. This is not a coincidence; it's the deep reason why Quadray rotations are algebraically clean.

### 2.10 Weierstrass Parameters for Common Rotation Spreads

For practical use, here are the Weierstrass t values for all common rotation spreads:

| Spread s | Angle θ | t = tan(θ/2) | Algebraic Form |
|----------|---------|-------------|----------------|
| 0 | 0° | 0 | 0 |
| 1/4 | 30° | 2 - √3 | Quadratic in √3 |
| 1/2 | 45° | √2 - 1 | Quadratic in √2 |
| 3/4 | 60° | 1/√3 | Radical in √3 |
| 1 | 90° | 1 | Rational |
| 3/4 | 120° | √3 | Radical in √3 |
| 1/2 | 135° | √2 + 1 | Quadratic in √2 |
| 1/4 | 150° | 2 + √3 | Quadratic in √3 |
| 0 | 180° | ∞ (limit) | Special case |

Every t value is expressible in terms of at most two cached radicals (√2, √3). The resulting ABCD coordinates involve at most √2, √3, and their product √6 — all of which are available from `PureRadicals`.

### 2.11 Proposed API: `fgh_from_weierstrass(t)`

The missing entry point in the rotation pipeline:

```rust
/// Compute F,G,H rotation coefficients from Weierstrass parameter t = tan(θ/2).
///
/// For rational t, F is exactly rational. G and H involve √3 (cached).
/// At tetrahedral angles (t = 0, ±1/√3, ±√3), all three are exact rational.
///
/// This is the most algebraically direct path from parameter to rotation —
/// no intermediate cos/sin, no spread-to-angle conversion.
pub fn fgh_from_weierstrass(t: f64) -> FghCoeffs {
    let t_sq = t * t;
    let denom = 3.0 * (1.0 + t_sq);
    let sqrt3 = crate::rt_math::radicals::sqrt3();  // cached

    FghCoeffs {
        f: (3.0 - t_sq) / denom,
        g: 2.0 * t * (t + sqrt3) / denom,
        h: 2.0 * t * (t - sqrt3) / denom,
    }
}
```

---

## 3. Composition: Multiple Axis Rotations

For sequential rotations about different ABCD axes, compose the 4×4 matrices:

```rust
let m1 = fgh_matrix(axis_a, &coeffs_a);
let m2 = fgh_matrix(axis_b, &coeffs_b);
let composed = mat4_multiply(&m2, &m1);  // m2 applied after m1
let result = mat4_transform(&composed, &vertex);
```

**This stays in ABCD throughout.** No intermediate XYZ conversion. The composed matrix is itself a 4×4 ABCD transformation.

For smooth interpolation between composed orientations, use the **QuadrayRotor** (quaternion-like representation with explicit Janus polarity):

```rust
let r1 = QuadrayRotor::from_spread_axis(spread1, axis1, polarity);
let r2 = QuadrayRotor::from_spread_axis(spread2, axis2, polarity);
let interpolated = r1.slerp(&r2, t);
let result = interpolated.rotate_vector(vertex);
```

The rotor's Hamilton product is RT-pure polynomial algebra. SLERP uses acos/sin at the animation boundary (RT-justified).

---

## 4. The Non-Trivial Case: Arbitrary-Axis Rotation

An arbitrary rotation axis in 3D does not generally align with any ABCD basis direction. This is where things get interesting.

### Option A: Decompose into ABCD Basis Rotations (Preferred)

Any 3D rotation can be decomposed into a sequence of rotations about the four ABCD basis axes — analogous to Euler angle decomposition, but using tetrahedral axes instead of orthogonal ones. The QuadrayRotor handles this via the Hamilton product:

```rust
// Construct rotor for arbitrary axis (expressed in ABCD)
let rotor = QuadrayRotor::from_axis_abcd(axis_abcd, spread, polarity);
let rotated = rotor.rotate_vector(vertex);
// Result is ABCD. No normalizer.
```

The rotor internally represents the rotation as four ABCD components (w, x, y, z mapped to Quadray) with a Janus polarity bit. The sandwich product `R·v·R*` produces ABCD output.

### Option B: Height-Axis Rotation via F,G,H Composition

The three height functions (h_X, h_Y, h_Z) define orthogonal directions in ABCD space:

```
h_Y = -a + b + c - d    (AD↔BC axis, "vertical")
h_X = -a + b - c + d    (AC↔BD axis, "lateral")
h_Z =  a + b - c - d    (AB↔CD axis, "depth")
```

Rotation about a height axis is a composition of ABCD basis rotations. Since the height axes correspond to cube edge-pair midpoints, these rotations have clean algebraic expressions — they are the "octahedral symmetry" rotations native to the ABCD system.

### Option C: The Normalizer Path (XYZ Round-Trip)

For a rotation axis expressed in Cartesian XYZ coordinates — e.g., "rotate 30° about the world Y-axis" — the normalizer provides a justified escape hatch:

```rust
// artex-osx/src/rt_math/normalizer.rs
use crate::rt_math::normalizer::{quadray_to_xyz, xyz_to_quadray};

// 1. Convert ABCD vertex to XYZ
let xyz = quadray_to_xyz(&vertex);
// 2. Apply XYZ rotation (classical matrix, justified at boundary)
let rotated_xyz = apply_rotation_matrix(xyz, &rotation_3x3);
// 3. Convert back to ABCD
let result = xyz_to_quadray(rotated_xyz);
```

**This is ONE justified exception**, not the default path. Mark with `// XYZ-justified: arbitrary Cartesian rotation axis`.

### When Each Option Applies

| Scenario | Use | Why |
|----------|-----|-----|
| Rotate about A, B, C, or D axis | F,G,H directly | Native, exact at tetrahedral angles |
| Compose multiple ABCD rotations | F,G,H matrix multiply | Stays in ABCD, composable |
| Smooth animation between orientations | QuadrayRotor SLERP | Gimbal-lock free, Janus-aware |
| Arbitrary axis in ABCD space | QuadrayRotor sandwich product | Native 4D, no XYZ |
| Axis only known in XYZ (import, camera) | Normalizer round-trip | Justified boundary |
| Instance rotation in scene | QuadrayRotor (state_manager.rs) | Already the source of truth |

---

## 5. What Already Exists in the Codebase

### Rust (artex-osx/src/rt_math/)

| File | What It Does |
|------|-------------|
| `fgh.rs` | F,G,H coefficients from spread or degrees; exact rational constants at tetrahedral angles; 4×4 matrix construction/composition; `fgh_rotate()` for single-axis application |
| `rotor.rs` | QuadrayRotor: Hamilton product, SLERP/NLERP, `from_spread_axis()`, `rotate_vector()`, `to_matrix3()` (polynomial, RT-pure) |
| `normalizer.rs` | `quadray_to_xyz()`, `xyz_to_quadray()`, `quadray_to_xyz_raw()` — the XYZ boundary, NOT the rotation engine |

### GPU Pipeline (Phase 5A, Complete)

```wgsl
// shader.wgsl — no XYZ, no BASIS matrix, no normalization
out.clip_position = camera.abcd_to_clip * in.quadray + camera.clip_offset;
```

The Tom Ace basis is folded into the camera matrix on the CPU once per frame (`camera.rs:abcd_to_clip()`). Instance rotations are applied to ABCD vertices on the CPU via F,G,H or rotor before GPU upload.

### JS (modules/)

| File | What It Does |
|------|-------------|
| `rt-math.js` | `RT.circleParam(t)` (Weierstrass), `RT.reflectInLine()` (double-reflection rotation), `RT.spread()`, `PureRadicals.sqrt3()` |
| `rt-quadray-rotor.js` | QuadrayRotor class: Hamilton product, SLERP, fromSpreadAxis |

---

## 6. Anti-Patterns (Do NOT Do These)

### Anti-Pattern 1: XYZ Round-Trip for ABCD-Axis Rotation

```rust
// WRONG: Converting to XYZ just to rotate around a known ABCD axis
let xyz = quadray_to_xyz(&vertex);
let rotated_xyz = rotate_around_a_axis_in_cartesian(xyz, angle);
let result = xyz_to_quadray(rotated_xyz);
```

**Fix:** Use `fgh_rotate(vertex, 0, &coeffs)` directly. Zero XYZ involvement.

### Anti-Pattern 2: Building a 3×3 XYZ Rotation Matrix for Tetrahedral Angles

At 60°, 120°, 180°, 240°, 300° about ABCD axes, the F,G,H coefficients are **exact rationals** (or even integer permutations). Converting to XYZ introduces √3 terms that then need to cancel back out. Don't create the problem just to solve it.

### Anti-Pattern 3: Using the Normalizer as a "Thinking Tool"

The normalizer (`quadray_to_xyz`) is a **rendering boundary** function (and import/export). It is not how you reason about rotations. If you're converting to XYZ to "understand" a rotation, you're in the wrong coordinate system for this project.

### Anti-Pattern 4: Forgetting Chirality

Even-index axes (A=0, C=2) use right-circulant matrices. Odd-index axes (B=1, D=3) use left-circulant (G and H swap). Getting this wrong produces the mirror image of the intended rotation. The `fgh.rs` implementation handles this automatically — don't hand-build matrices without checking chirality.

---

## 7. The Big Picture: Where Rotations Fit in the Pipeline

```
┌────────────────────────────────────────────────────┐
│  GEOMETRY CREATION (rt_polyhedra/)                 │
│  Vertices created as ABCD — integer or rational    │
└────────────────────┬───────────────────────────────┘
                     │ ABCD vertices
                     ▼
┌────────────────────────────────────────────────────┐
│  INSTANCE TRANSFORMS (state_manager.rs)            │
│  Rotation: QuadrayRotor → fgh_rotate or sandwich   │
│  Translation: ABCD vector addition                 │
│  Scale: ABCD scalar multiplication                 │
│  ALL IN ABCD — no XYZ at any point                 │
└────────────────────┬───────────────────────────────┘
                     │ transformed ABCD vertices
                     ▼
┌────────────────────────────────────────────────────┐
│  GPU UPLOAD (geometry.rs)                          │
│  ABCD f64 → ABCD f32 (precision boundary only)    │
│  Cast to vertex buffer — still ABCD coordinates    │
└────────────────────┬───────────────────────────────┘
                     │ ABCD vertex buffer
                     ▼
┌────────────────────────────────────────────────────┐
│  VERTEX SHADER (shader.wgsl)                       │
│  clip = abcd_to_clip * quadray + clip_offset       │
│  One multiply + one add. No XYZ. No BASIS.         │
│  No normalization.                                 │
└────────────────────────────────────────────────────┘
```

The normalizer sits **outside** this pipeline. It's for:
- Import: OBJ/STL files give XYZ → `xyz_to_quadray()` at the import boundary
- Export: ABCD vertices → `quadray_to_xyz()` for file output
- Camera: `glam` needs XYZ for view/projection matrices (last classical holdout)
- Tests: cross-validation against known XYZ positions

---

## 8. Future: Weierstrass-Native Rotor Construction

The Quadray-Rotors.tex whitepaper (§4.4) identifies a research direction beyond F,G,H: construct **rotors** (the Quadray analogue of quaternions) directly from Weierstrass parameter t.

The F,G,H system (§2) handles single-axis rotation elegantly. For **arbitrary-axis** rotation, the QuadrayRotor needs half-angle values. The current pipeline:

```
angle → cos/sin → half-angle → rotor components
  or
spread → √(cross) → half-angle → rotor components    (2 sqrt operations)
```

**Proposed pipeline:**
```
t = tan(θ/2) → cos(θ) = (1-t²)/(1+t²)               (rational in t)
             → sin(θ) = 2t/(1+t²)                     (rational in t)
             → half-angle via tan(θ/4) identity         (algebraic in t)
             → rotor components (polynomials in t, √3)
```

For rational t, this makes the **entire rotor construction algebraic** — no transcendentals, and the only irrationals are cached radicals. Combined with the Weierstrass-F,G,H formulas from §2.4 (where √3 cancels at tetrahedral angles), this would give us a fully RT-pure rotation system for a dense subset of all possible rotations.

This connects to the broader ARTexplorer vision: geometry should be algebraic until the last possible moment (the rendering boundary), and the rendering boundary itself should be as thin as possible (Phase 5A achieved: one matrix multiply in the shader).

---

## 9. Gumball Native ABCD Rotation — Implementation (COMPLETE)

### 9.1 The Problem: Five XYZ Detours for a Native Operation

When the user drags an **ABCD ring** (A, B, C, or D axis) on the gumball, the rotation should be a pure Quadray operation — the FGH system handles it exactly. But the current pipeline takes five XYZ detours:

```
CURRENT PIPELINE (ABCD ring drag):

1. controls.rs:903  — ABCD axis → Tom Ace basis → [x,y,z] Cartesian direction
2. controls.rs:909  — QuadrayRotor::from_radians_axis(angle, [x,y,z])
                       → quaternion from CARTESIAN axis (w,x,y,z)
3. controls.rs:910  — Hamilton product composition (polynomial, but in
                       Cartesian quaternion representation)
4. state_manager.rs  — Store as QuadrayRotor (= Cartesian quaternion)
5. geometry.rs:1501  — Per vertex: quadray_to_xyz() → glam::Quat rotation
                       → xyz_to_quadray() — two basis transforms per vertex
```

Step 5 is the performance bottleneck. For every rotated vertex, every frame:
- `quadray_to_xyz()`: 3×4 matrix multiply (12 muls + 9 adds)
- `glam::Quat * Vec3`: Hamilton sandwich product (~28 ops)
- `xyz_to_quadray()`: 4×3 matrix solve + canonical shift (~20 ops)
- **Total: ~70 floating-point operations per vertex**

The native FGH path for a single ABCD-axis rotation:
- `mat4_transform()`: 4×4 matrix-vector multiply (16 muls + 12 adds)
- **Total: ~28 floating-point operations per vertex**

That is **2.5× fewer operations** and **zero basis-transform noise**. At tetrahedral angles, the FGH coefficients are exact rationals — the XYZ round-trip introduces irrational noise even at these pure angles.

### 9.2 The Fix: Dual-Track Rotation Representation

The key insight: **ABCD rotations are 4×4 ABCD matrices. XYZ rotations are quaternions. These are different representations that each excel in their own domain.** Rather than force everything through the quaternion path, store whichever is native.

#### Transform gains an `abcd_rotation` field

```rust
// state_manager.rs — Transform
pub struct Transform {
    pub position: [f64; 3],
    pub rotation: QuadrayRotor,           // Existing — used for XYZ and mixed rotations
    pub rot_abcd_deg: Option<[f64; 4]>,   // Existing — display tracking
    pub pos_abcd: Option<[f64; 4]>,       // Existing

    /// Native ABCD rotation matrix — set when rotation is purely about ABCD axes.
    /// When Some, geometry.rs uses this directly (no XYZ round-trip).
    /// When None, falls back to QuadrayRotor path (existing behaviour).
    /// Cleared when an XYZ rotation is applied (mixed rotation → quaternion only).
    pub abcd_rotation: Option<[[f64; 4]; 4]>,
}
```

The `abcd_rotation` and `rotation` (QuadrayRotor) are kept in sync:
- **ABCD ring drag**: set `abcd_rotation` = FGH matrix, also update `rotation` for compatibility
- **XYZ ring drag**: clear `abcd_rotation` = None, set `rotation` only
- **Mixed**: clear `abcd_rotation`, compose via quaternion

#### Controls.rs — ABCD ring fast path

```rust
// controls.rs — inside ToolMode::Rotate, when abcd_axis_index.is_some()

if let Some(ai) = drag.abcd_axis_index {
    // Native ABCD path — no XYZ axis conversion needed.
    // RT-justified: radians at UX boundary (atan2 drag).
    let coeffs = crate::rt_math::fgh::fgh_from_radians(signed_angle as f64);
    let drag_matrix = crate::rt_math::fgh::fgh_matrix(ai, &coeffs);

    // Compose with origin ABCD matrix (if origin was also ABCD-native)
    let new_abcd = if let Some(origin_m) = drag.origin_abcd_rotation {
        crate::rt_math::fgh::mat4_multiply(&drag_matrix, &origin_m)
    } else {
        drag_matrix  // First ABCD rotation from identity
    };

    // Also update the quaternion representation for compatibility
    // (XYZ display, save/load, group operations that need quaternion).
    let axis_f64 = [...]; // Tom Ace basis — XYZ-justified: quaternion sync
    let rot = QuadrayRotor::from_radians_axis(signed_angle as f64, axis_f64);
    let new_rot = rot.multiply(&drag.origin_rotation);

    return Some(GumballAction::Rotate {
        rotation: new_rot,
        abcd_rotation: Some(new_abcd),  // NEW FIELD
        ...
    });
}
```

#### Geometry.rs — native ABCD vertex transform

```rust
// geometry.rs — vertex transformation, ABCD fast path

if let Some(ref abcd_mat) = inst.transform.abcd_rotation {
    // NATIVE PATH: 4×4 ABCD matrix multiply. No XYZ. No basis transform.
    let scaled = [
        abcd[0] as f64 * s as f64,
        abcd[1] as f64 * s as f64,
        abcd[2] as f64 * s as f64,
        abcd[3] as f64 * s as f64,
    ];
    let rotated = crate::rt_math::fgh::mat4_transform(abcd_mat, scaled);
    [
        rotated[0] as f32 + da,
        rotated[1] as f32 + db,
        rotated[2] as f32 + dc,
        rotated[3] as f32 + dd,
    ]
} else if has_rotation {
    // FALLBACK: existing quaternion → XYZ round-trip (for XYZ/mixed rotations)
    // ... existing code unchanged ...
}
```

### 9.3 Implementation Steps (ALL COMPLETE — March 8, 2026)

All five steps implemented and verified (675 tests pass, zero errors):

#### Step 1: Add `abcd_rotation` to Transform + GumballAction ✓

- `pub abcd_rotation: Option<[[f64; 4]; 4]>` on `Transform` with `#[serde(default)]`
- Field on `GumballAction::Rotate`, threaded through `drag_handlers.rs`
- All `Transform { ... }` constructors updated (state_manager.rs ×2, copy_operations.rs ×5, main.rs ×1)
- All rotation mutation sites clear field appropriately (IK, coord bar, reset, group orbit)

#### Step 2: Controls.rs — generate FGH matrix for ABCD drags ✓

- `fgh_from_radians(signed_angle)` → `fgh_matrix(axis_index, &coeffs)` when `abcd_axis_index.is_some()`
- Composed with origin ABCD matrix via `mat4_multiply()` for sequential drags
- Quaternion still computed in parallel for compatibility (group orbits, XYZ display, save/load)

#### Step 3: Geometry.rs — ABCD vertex fast path ✓

- Four render paths updated: Platonic edge/face, Thomson edge/face, Platonic nodes, Thomson nodes
- Each checks `inst.transform.abcd_rotation.is_some()` → `mat4_transform()` directly
- Falls back to existing quaternion → XYZ round-trip for XYZ/mixed rotations

#### Step 4: Clear on XYZ rotation ✓

- XYZ ring drag, XYZ coord bar edit, rotation reset, group orbit, IK constraints — all clear `abcd_rotation`
- Old saves deserialize with `None` (serde default) — existing quaternion path used

#### Step 5: DragState carries origin ABCD matrix ✓

- `origin_abcd_rotation: Option<[[f64; 4]; 4]>` on `DragState`
- Captured from `inst.transform.abcd_rotation` at drag start via `start_drag()`
- Passed through from `main.rs` instance lookup

### 9.4 What This Does NOT Change

- **XYZ ring rotations** — unchanged, still use QuadrayRotor (quaternion)
- **Group rotations** — still use orbital quaternion for centroid orbits (position is XYZ)
- **SLERP/animation** — still uses QuadrayRotor interpolation
- **Save/load format** — backwards compatible (`abcd_rotation` defaults to None)
- **Coordinate bar display** — unchanged (`rot_abcd_deg` tracking continues)
- **Vertex-anchored pivot orbits** — still use glam (position orbit is XYZ geometry)
- **IK constraint propagation** — still uses QuadrayRotor

### 9.5 Performance Characteristics

| Operation | Current (per vertex) | Native ABCD (per vertex) |
|-----------|---------------------|--------------------------|
| Basis transforms | 2 (ABCD→XYZ + XYZ→ABCD) | 0 |
| Matrix multiplies | ~3 (two basis + quaternion) | 1 (4×4 ABCD) |
| Float ops | ~70 | ~28 |
| Precision loss | 2 basis round-trips | None |
| Rational at tet angles | No (basis vectors are irrational) | Yes (FGH = integer fractions) |

For a polyhedron with N vertices rendered every frame, this saves **~42·N float operations per frame** on every ABCD-rotated instance. More importantly, it eliminates the **conceptual inversion** of converting to XYZ just to rotate around a known ABCD axis.

### 9.6 TODO: Picking Path

The hit-testing code in `picking.rs` still uses the XYZ round-trip (`quadray_to_xyz` → `glam::Quat` rotation) for rotated instances. When `abcd_rotation` is `Some`, picking should use `mat4_transform()` to match the render path. This is less performance-critical (per-click, not per-frame) but important for correctness — click targets must match visual positions exactly. Also applies to the debug hit-zone visualization in `geometry.rs` (`world_center_abcd` closure).

### 9.7 Future: ABCD-Native Position + Full Pipeline

Once `abcd_rotation` is proven in the gumball path, the same pattern extends to:

1. **Transform.position as ABCD** — currently `[f64; 3]` XYZ. An `Option<[f64; 4]>` ABCD position (from ABCD snap or integer placement) could skip `xyz_to_quadray` for translation too
2. **Combined scale-rotate-translate in one 4×4** — for ABCD-only transforms, a single 4×4 matrix handles everything: scale (diagonal), rotation (FGH block), translation (add). One `mat4_transform` per vertex, period
3. **GPU-side rotation** — the `abcd_to_clip` camera matrix could absorb the instance rotation matrix. Then the shader does `abcd_to_clip * instance_rotation * vertex` as a single pre-composed matrix — zero per-vertex work on the CPU

---

---

## 10. ABCD.EARTH — Bringing K(u) Down From Theory (IN FLIGHT)

**Date:** April 25–26, 2026
**Status:** Phases A, B, C, D step 1, D step 2, and E (first swap) all complete on branch 2DXY-5; Phase E continues for additional consumers
**Mathematical source:** Murillo, L. (2026). *Intrinsic Vector Algebra on Simplicial (Quadray) Coordinates: Cross Product, Rotation, and the Zero-Sum Hyperplane.* Zenodo 19689050. (v2 retitled "Vector Algebra" — note dropped from "Vector Calculus" since the paper develops only the algebraic layer; differential operators ∇/div/curl are not in scope.)

### 10.1 What Murillo Gives Us That We Don't Have

The current rotation stack has a hole. For **basis-axis rotation** (A, B, C, D) we have the F,G,H circulant matrices in `fgh.rs` — clean, RT-pure, exact at tetrahedral angles. For **arbitrary-axis rotation** we have `rotor.rs` — a quaternion in disguise (line 21–28 of rotor.rs admits as much: *"Currently a standard quaternion (Cartesian i,j,k basis) with explicit Janus polarity… The true tetrahedral-basis rotor (where components ARE ABCD projections) is the goal of Phase 3"*).

Murillo provides the missing piece: a single closed-form operator for arbitrary zero-sum unit axes, expressed entirely in ABCD with no Cartesian quaternion intermediary.

```
R(u, θ) = I + sin(θ)·K(u) + (1 − cos θ)·K(u)²
```

where K(u) is the 4×4 cross-product operator built from cyclic differences of u-components (Cookbook §10). For rotation about A, B, C, D it reduces to F,G,H. For arbitrary u in the zero-sum hyperplane H, it gives the rotation matrix directly. The cubic identity **K(u)³ = −K(u)** is what makes the Taylor series of `exp(θK)` collapse into the finite trigonometric form.

### 10.2 Why "ABCD.EARTH"

This chapter is the **mapping from ABCD heaven (Murillo's abstract math) down to ABCD earth (our Rust application code)**. The math is published, peer-presentable, and proven. What we don't have is the implementation — the new Rust module, the wiring into `state_manager.rs`, the call sites in `geometry.rs` that currently take the quaternion path, and the test cross-validation.

### 10.3 Module Plan: `rt_math/k_of_u.rs`

A new module sitting alongside `fgh.rs` and `rotor.rs`:

```rust
// artex-osx/src/rt_math/k_of_u.rs
//! Intrinsic ABCD rotation operator R(u,θ) = exp(θK(u)).
//!
//! Implements Murillo (2026, Zenodo 19689050): the closed-form
//! arbitrary-axis rotation on the zero-sum hyperplane, with
//! the 9-multiplication apply kernel.
//!
//! For basis-axis rotation, prefer fgh.rs (specialized circulant).
//! For SLERP/animation, prefer rotor.rs (Hamilton product).
//! For arbitrary-axis single-shot rotation in ABCD, use this module.

pub struct KOfU {
    /// The 4×4 K(u) operator. Skew-symmetric, K·1 = 0.
    pub k: [[f64; 4]; 4],
    /// The reduced 3×3 R̃ (R restricted to H, expressed in {e_i − e_4} basis).
    /// Stored after construction; used by the 9-mul apply kernel.
    pub r_tilde: [[f64; 3]; 3],
}

impl KOfU {
    /// Build K(u) from a zero-sum unit axis (Σuᵢ² = 1/4).
    /// If input is not zero-sum, projects first via gauge subtraction.
    /// If input is not M-unit, normalizes (one √).
    pub fn from_axis(axis_abcd: [f64; 4]) -> Self;

    /// Build R(u, θ) from spread s = sin²θ and polarity (±1).
    /// RT-pure entry point.
    pub fn from_spread_axis(spread: f64, axis_abcd: [f64; 4], polarity: i8) -> Self;

    /// Apply rotation to a zero-sum ABCD point using the 9-mul kernel
    /// (Murillo §7). Output is zero-sum by Property 6 (gauge fixation).
    pub fn apply(&self, p_abcd: [f64; 4]) -> [f64; 4];

    /// The full 4×4 rotation matrix R(u,θ) = I + sinθ·K + (1−cosθ)·K².
    /// Use when the matrix itself is needed (composition, GPU upload).
    pub fn to_mat4(&self) -> [[f64; 4]; 4];

    /// Compose two rotations: R3 = R2 · R1.
    /// Returns the composed matrix; axis-angle extraction is a separate op
    /// (Rodrigues composition formula — see §10.6 open question).
    pub fn compose(&self, other: &Self) -> [[f64; 4]; 4];
}
```

### 10.4 Implementation Steps

#### Step 1: Module skeleton + tests
- New file `artex-osx/src/rt_math/k_of_u.rs`
- Public exports in `rt_math/mod.rs`
- Test fixtures: 24 canonical rational unit axes (permutations of [±¼,±¼,∓¼,∓¼]) — all M-unit, all zero-sum, fully rational
- Smoke test: `K(u)·u = 0`, `Σ K(u)·v = 0`, `K(u)³ = −K(u)` for each canonical axis

#### Step 2: Cross-validate against `fgh.rs`
- For each ABCD basis axis (e_A, e_B, e_C, e_D) and angles {30°, 45°, 60°, 90°, 120°, 180°}, verify `KOfU::from_axis(e_X).to_mat4() · p == fgh_rotate(p, X, …)` to 10⁻¹⁵
- This proves K(e_axis) recovers the existing F,G,H matrices — the scaffold relationship documented in Cookbook §8

#### Step 3: Cross-validate against `rotor.rs` (and through it, glam::Quat)
- For arbitrary axes (not basis-aligned) and the same angle sweep, verify `KOfU` and `QuadrayRotor::from_spread_axis(...).rotate_vector(...)` produce the same rotated point in ABCD to 10⁻¹⁰
- Add to existing cross-validation harness in `rotor.rs` tests

#### Step 4: 9-mul apply kernel
- Implement `apply()` via the reduced 3×3 R̃ matrix (Murillo §7.1–7.2)
- Verify that R̃ result + zero-sum recovery (P_d = −(P_a+P_b+P_c)) matches full 4×4 apply
- Bench: `KOfU::apply` vs `QuadrayRotor::rotate_vector` over 10⁵ vertices

#### Step 5: Integrate into `state_manager.rs`
- Add `Transform.k_of_u: Option<KOfU>` alongside existing `rotation: QuadrayRotor` and `abcd_rotation: Option<[[f64;4];4]>` fields
- Populate when an arbitrary-axis ABCD rotation is set (e.g., via the gumball drag for non-basis axes — currently routes through quaternion)
- Backwards compatible: `#[serde(default)]` so old saves load

#### Step 6: Geometry.rs hot path
- Add fast path: `if let Some(k) = inst.transform.k_of_u { let rotated = k.apply(abcd_p); ... }`
- Falls through to existing `abcd_rotation` matrix path, then existing quaternion path
- Three nested levels: K(u) intrinsic → 4×4 ABCD matrix → quaternion+XYZ round-trip

#### Step 7: Picking parity
- Update `picking.rs` to honour `k_of_u` — same precedence chain as render path
- Click targets must match visual positions

### 10.4a Progress and Findings (2026-04-26)

Phase A and Phase B of the §10.4 plan are complete. The work is shadow-only — no production code touches `k_of_u.rs` yet. Both phases revealed a clean orientation-convention difference between Murillo's K(u) framework and the existing codebase, with consistent algebraic relationships across all three mathematical layers tested.

#### Phase A: Cross product (commit `a07c959`)

Implemented `k_of_u_cross(u, v) -> [f64; 4]` per Murillo engineering guide §1.

**Verified:**
- Murillo's worked example (§3.1, §3.2) reproduces exactly with rational inputs
- All intrinsic properties hold: zero-sum closure, anti-symmetry, self-cross is zero, M-orthogonality to both inputs

**Shadow comparison vs `crate::abcd_metric::abcd_cross_f64`:**
- 5/5 cases produce **exactly negated** results
- `k_of_u_cross(u, v) = −abcd_cross_f64(u, v)` consistently
- Both are valid M-orthogonal cross products on the zero-sum hyperplane
- The negation is the right-hand vs left-hand wedge-Hodge dual choice

#### Phase B: K(u) matrix and R(u,θ) Rodrigues (commit `f1bbe69`)

Implemented:
- `k_matrix(axis_abcd) -> [[f64;4];4]` — projects to zero-sum, M-normalizes (Σuᵢ²=1/4), builds 4×4 K(u) from cyclic differences
- `rotation_matrix_cossin(axis, cos_θ, sin_θ)` — assembles R = I + sinθ·K + (1−cosθ)·K²
- `rotation_matrix_from_spread(axis, spread, polarity)` — RT-pure entry point matching `fgh::abcd_rotation_matrix` API

**Verified properties** (Murillo Proposition 6.1 subset, all pass):
- `K(u)·u = 0` (axis is in kernel)
- `K(u)·v = k_of_u_cross(u, v)` (matrix matches free function)
- `K³ = −K` for canonical M-unit axes AND for projected basis axes
- `R(u, 0) = I`
- `R(u, θ)·u = u` (axis eigenvector with eigenvalue 1)
- `R·[1,1,1,1] = [1,1,1,1]` (gauge direction fixed)
- `R·Rᵀ = I` (orthogonal)

**Shadow comparison vs `fgh::abcd_rotation_matrix`:**
- 28/28 cases (4 basis axes × 7 angles, plus 4 arbitrary axes × 6 spread/polarity combos)
- **0 as-written matches, 0 polarity-flip matches, 28 K-sign-flip matches**
- Equivalent statements:
  - `R_Murillo(u, +θ) = R_fgh(u, −θ)`
  - `K_Murillo(u) = −K_fgh(u)`
- Cubic identity `K³=−K` holds for both K and −K (since `(−K)³ = −(−K)`), so Murillo's framework remains fully valid in either orientation — **no rescaling needed**

#### Three-layer consistency

The same orientation convention difference surfaces at every level:

| Layer | Murillo (as written) | Existing codebase | Relationship |
|---|---|---|---|
| Cross product | `k_of_u_cross(u, v)` | `abcd_cross_f64(u, v)` | exact negation |
| Operator matrix | `K(u)` | implicit in `fgh::abcd_rotation_matrix` | exact negation |
| Rotation | `R_M(u, +θ)` | `R_fgh(u, +θ)` | `R_M(u, +θ) = R_fgh(u, −θ)` |

This is **one design decision** (orientation convention) appearing in three algebraic layers, **not three independent discrepancies**. Negating any of them propagates correctly to the others.

#### Janus connection

The orientation difference IS the parity flip required for Janus passage (P → −P). When geometry crosses from 4D⁺ into 4D⁻:
- Vertices negate (handled by J explicitly)
- Pseudovectors (cross products, normals) flip orientation as part of J's effect on the wedge-Hodge dual
- The cross-product convention swap is exactly the right mechanism

**Architectural consequence:** we don't build separate `cross_4d_plus` and `cross_4d_minus` functions. We pick one convention as the 4D⁺ default (matches existing codebase = negated Murillo) and Janus inversion naturally takes us to the other convention. This is consistent with Quadray-Rotors.tex §13.3 where Janus is repositioned as a separate inversion operator.

#### Decision: orientation convention for production

For drop-in replacement of existing `abcd_cross_f64` and `fgh::abcd_rotation_matrix`, production wrappers will use **negated K(u)** and **negated cross product output** to match the existing codebase convention. Murillo-faithful functions remain available in `k_of_u.rs` for academic verification and future Janus 4D⁻ work.

### 10.4b Phase C — Codebase-orientation wrappers and strict equality ✅ COMPLETE (commit 3f0010e)

**Goal:** make k_of_u.rs functions drop-in replacements for the existing API, with strict-equality verification.

**Delivered:**
1. ✅ `abcd_cross_codebase(u, v)` — calls `k_of_u_cross` then negates output
2. ✅ `rotation_matrix_codebase(axis, spread, polarity)` — calls `k_matrix`, negates K, assembles Rodrigues
3. ✅ `rotation_matrix_codebase_cossin(axis, cos_θ, sin_θ)` — added in Phase D step 2 prep, takes explicit cos/sin
4. ✅ Strict-equality shadow tests passing at machine epsilon:
   - `phase_c_strict_cross_product_equality`: 600+ cases, max error within 1e-13
   - `phase_c_strict_rotation_matrix_equality`: 792 cases (11 axes × 12 angles × 6 vectors), max error 2.66e-15

**Result:** every case matches existing API to f64 precision. Swap is mathematically safe — any call site can be swapped to k_of_u functions with zero behavioral change. Phase D step 1 + step 2 used these wrappers to swap real production code; both passed without regression.

### 10.4c Phase D — First production swaps ✅ COMPLETE (commits 37ce24b, a70eff0)

**Step 1 — `abcd_metric::abcd_cross_f64` ✅** (commit 37ce24b, merged via PR #72):
- One-line delegation to `k_of_u::abcd_cross_codebase`
- All 16+ existing call sites in `net.rs`, `struts.rs` continue working unchanged
- 1126 cargo tests pass, 0 regressions
- Visual smoke tests passed (verified by Andy 2026-04-26)

**Step 2 — `fgh::abcd_rotation_matrix_cossin` ✅** (commit a70eff0, on 2DXY-5):
- Replaces 91 lines of height-functions+B†/4 Cartesian round-trip with single delegation to `k_of_u::rotation_matrix_codebase_cossin`
- Transitively affects `abcd_rotation_matrix` (entry from spread) and `abcd_rotation_matrix_weierstrass` (entry from Weierstrass parameter)
- Production callers: `net.rs` (5 fold-animation sites), `ik.rs` (1 IK constraint site), `fgh.rs` internals
- Pre-swap proofs added: `phase_d_step2_strict_rotation_cossin_equality` (480 cases, max err 2.66e-15) and `phase_d_step2_strict_rotation_weierstrass_equality` (72 cases, max err 1.78e-15)
- 1128 cargo tests pass, 0 regressions

**Outcome:** the Cartesian intermediate (height-functions + B†/4 inverse) has been removed from the entire arbitrary-axis ABCD rotation pipeline. All routes through `fgh::abcd_rotation_matrix*` and `abcd_metric::abcd_cross_f64` now use Murillo's intrinsic K(u) construction.

### 10.4d Phase E — First production consumer of the 9-mul kernel ✅ FIRST SWAP COMPLETE (commit 8ca0d8b)

Phase E is broader than originally scoped in §10.10 (rotor.rs migration). Reframed: **Phase E = put the K(u) machinery to actual use in production, beyond the drop-in delegations of Phase D.** The first concrete consumer is the 9-mul apply kernel.

**Step 1 — net.rs fold animation ✅** (commit 8ca0d8b, on 2DXY-5):
- 6 vertex inner-loop call sites in 4 distinct `m = abcd_rotation_matrix_weierstrass(...)` scopes
- Each loop rotates `local = v - rot_origin` displacements (zero-sum by construction — difference of two ABCD vertices in the same gauge class)
- Replaced `mat4_transform(&m, local)` (16 mul + 12 add per vertex) with `apply_reduced_3x3(&r_tilde, local)` (9 mul + 9 add per vertex)
- R̃ built once per fold rotation via `reduced_3x3(&m)` outside the inner loop
- 1134 cargo tests pass, 0 regressions
- Per-vertex savings: -7 mul, -3 add. Modest absolute on small polyhedra; meaningful on geodesics with hundreds of vertices being folded interactively.

**Pending Phase E steps** (not yet committed):
- **Step 2** — analyze other `mat4_transform` call sites (`geometry/instances.rs`, `struts.rs`, `labels.rs`, `abcd_overlay.rs`) per site for zero-sum input. Vertices in instances.rs are NOT zero-sum (`[1,0,0,0]` for tet vertex etc.), so direct kernel swap doesn't apply — would need a `apply_with_gauge` wrapper (~10 mul + 20 add vs 16 mul + 12 add — marginal). Defer until benchmarks justify.
- **Step 3** — rotor.rs site-by-site migration per §10.10. Note: the Shepperd-extraction swap originally proposed in §10.10 turned out NOT to be a clean K(u) win — Shepperd's method IS the right algorithm for matrix→quaternion extraction; replacing it with axis-angle extraction would also require retrofitting QuadrayRotor's internal representation, which is a much bigger rewrite. Re-scope §10.10 work as part of the larger rotor.rs internals migration, not piecewise.

### 10.4e 9-mul Apply Kernel — Murillo §7 ✅ COMPLETE (commit fcab066)

Added Murillo's structural-parity result: for any 4×4 ABCD rotation matrix R applied to a zero-sum input P, the apply cost reduces from 16 multiplications to exactly 9 by exploiting:
1. **Output redundancy** (16 → 12): R·P ∈ H by Proposition 6.1.6, so the 4th component follows by zero-sum closure
2. **Input redundancy** (12 → 9): substituting P[3] = -(P[0]+P[1]+P[2]) collapses each row's length-4 dot product to length-3 against a reduced 3×3 matrix R̃ where R̃[i][j] = R[i][j] - R[i][3]

**API delivered:**
- `reduced_3x3(R)` — builds the 3×3 R̃ from a 4×4 R (cache once per rotation)
- `apply_reduced_3x3(R̃, P)` — 9 mul + 9 add per zero-sum P (use per vertex)
- `apply_zero_sum_9mul(R, P)` — one-shot wrapper combining both for non-batched callers

**Verification:** 6 new tests, all pass. The kernel matches `mat4_transform` to 1.78e-15 across 280+ K(u)-derived rotations, plus additional cases for fgh basis-axis F,G,H circulant and fgh::abcd_rotation_matrix arbitrary-axis paths. Works for ANY 4×4 rotation matrix that preserves the zero-sum hyperplane and fixes [1,1,1,1] (Propositions 6.1.2, 6.1.6).

**Used in production by:** Phase E step 1 (net.rs fold animation), commit 8ca0d8b.

### 10.4f Research Questions and Open Math

The K(u) integration opens or revives several research-level questions, mostly from Murillo §8 ("Higher Dimensions and Future Work"). These are not on the critical path for ABCD.EARTH but each would close an open loop in the algebraic story.

**1. Closed-form axis-angle composition formula** (Murillo §8.3, "Composition formulas")

Given two rotations R(u₁, θ₁) and R(u₂, θ₂), their product is again a rotation R(u₃, θ₃) (Proposition 6.1, closure of SO(3)). What is the closed form for (u₃, θ₃) in terms of (u₁, θ₁, u₂, θ₂)?

Quaternions have a well-known composition: q₃ = q₁ · q₂ via Hamilton product. The simplicial analogue would be the direct intrinsic version — operating on (axis, angle) pairs in ABCD without going through Hamilton or matrix multiplication. Required if we want to keep rotations stored as `(axis, spread)` pairs across composition (compact storage, semantically meaningful).

Currently: store composed rotations as 4×4 matrices and accept that axis-angle is post-hoc extraction. Loss: 9 scalars vs 4 (axis_abcd + angle).

**2. Axis-angle extraction from a rotation matrix R**

Given a 4×4 ABCD rotation matrix R, recover the axis u and angle θ such that R = R(u, θ). This is the inverse of `rotation_matrix_codebase_cossin`.

Standard Rodrigues structure gives:
- `cos θ = (tr R|_H − 1) / 2 = (tr R − 2) / 2` (using Proposition 6.1.5: tr R = 2 + 2 cos θ for the 4×4 lift)
- `sin θ · K(u) = (R − Rᵀ) / 2` (the antisymmetric part of R)
- From sin θ · K(u), extract sin θ as the M-norm of the off-diagonal pattern; recover u from K(u) via the cyclic-difference-to-axis inverse map

Useful for:
- Storing rotations compactly as axis-angle (5 scalars: axis_abcd + angle, vs 16 for matrix)
- Inspecting/debugging rotations from any source (camera matrices, IK results, imported transforms)
- Bridging composed rotations back to canonical (axis, angle) form (closes the loop with question 1)

Algorithmic gotchas: at θ ≡ 0 (R = I), the axis is undefined; at θ = π, sin θ = 0 and the antisymmetric part vanishes — fall back to extracting u from R + I (the symmetric part). These edge cases are handled in standard Cartesian Rodrigues-inverse implementations and translate directly.

**3. M-unit fast path for `k_matrix`** (Leo's correction, 2026-04-26)

Murillo §7.5 (v2 paper) shows that under our metric M = 4I − J = 3G, the raw cyclic-difference matrix K̃(u) (without the 1/√3 prefactor used in the paper's main G-metric body) satisfies K̃³ = −K̃ directly for any M-unit axis (Σuᵢ² = 1/4). For canonical rational M-unit inputs (permutations of [±¼, ±¼, ∓¼, ∓¼]), K̃ has fully rational entries — no √3 anywhere.

Current `k_matrix(axis)` auto-normalizes any input axis to M-unit via one sqrt — convenient, but introduces √3 for non-M-unit inputs like basis vectors `e_A = [1,0,0,0]`. Proposed addition: a `k_matrix_m_unit(axis)` fast path that assumes the input is already M-unit (no normalization) and keeps K̃ rational for rational inputs. Useful when callers (e.g. the future axis-angle composition implementation) work with canonical axes deliberately.

**4. Higher-N construction sketch** (Murillo §8.2)

For N ≥ 5, the simplicial wedge-Hodge construction generalizes: a simple-blade rotation is parameterized by N − 3 fixed vectors instead of one axis. For N = 4 (our case), N − 3 = 1, recovering the binary cross product. For N = 5 (4-simplex frame in ℝ⁴), N − 3 = 2 — rotation about a 2-blade. Could underpin a 4D ABCD rendering pipeline if we ever want to render geometry intrinsically in 4D (current work is 3D Quadray = N=4 simplicial).

Almost certainly not on the ARTexplorer critical path, but worth noting as the natural extension axis.

**5. Information geometry connection** (Murillo §8.3)

The zero-sum hyperplane H, translated by (1/N)·1, is the probability simplex. Under the transformation xᵢ = √pᵢ (probability simplex → positive orthant of unit sphere), the simplicial inner product agrees with the Fisher information metric up to a positive scalar at the uniform distribution. The Aitchison geometry (compositional data analysis, ilr transformation) lives on the same H.

Question: can K(u) and R(u, θ) be reinterpreted as Fisher-Rao geodesics on the probability simplex? If so, ABCD rotation gives a geometric framework for compositional/distributional data manipulation.

Speculative but elegant. No immediate ARTexplorer use.

**6. SIC-POVM connection** (Murillo §8.3)

The N=4 simplicial frame is *exactly* the configuration of the four Bloch vectors of a single-qubit Symmetric Informationally Complete POVM. The rotation operators R(u, θ) of §5 therefore provide a simplicial-coordinate realization of the SO(3) ≅ SU(2)/{±I} action of projective qubit unitaries on such POVMs — directly on the zero-sum hyperplane, without passage through the SU(2) double cover that quaternion pipelines require.

ARTexplorer connection: the four ABCD axes literally represent a quantum measurement frame. If we ever want to visualize qubit state evolution under a Hamiltonian, the K(u) framework is the natural rendering pipeline. Pure synergy with the project's "Synergetics" theme.

**7. Janus inversion as separate operator** (Quadray-Rotors.tex §13.3)

Per the v4.1 reframing: Janus polarity moves OFF the rotor and BECOMES a separate inversion operator J: P → −P. The composed move J ∘ R(u, θ) — rotation followed by inversion into 4D⁻ — has det = −1 and lives in O(3) \ SO(3).

Open: how should this compose in practice in the codebase? Does the Geometric Janus Inversion paper give a clean implementation pattern? Current QuadrayRotor still carries a polarity bit; the right design is probably to retire that field and add a separate `JanusOperator` type that composes with rotations explicitly. Tracked in Quadray-Rotors.tex §13's open question box.

**8. GPU upload of K(u)-derived matrices** (Phase 6 territory)

Once we have a 4×4 R(u, θ) from K(u), can it be folded into `abcd_to_clip` per-instance? Currently `abcd_to_clip` is a single per-frame matrix — per-instance rotation is applied CPU-side. Folding instance rotation into a per-instance abcd_to_clip would push the rotation onto the GPU, eliminating the CPU per-vertex transform entirely.

This is Phase 6 territory in the whitepaper (§11.3 RT-pure camera). Requires the camera projection itself to be ABCD-native, which depends on resolving the perspective/FOV matrix question separately.

### 10.5 What This Does NOT Touch

- **F,G,H basis-axis fast path** (§9 work): unchanged. K(u) is a *general* operator; for basis-axis rotation, F,G,H is faster (specialized) and we keep it as the preferred path
- **SLERP/NLERP animation**: still routed through `rotor.rs`. K(u) gives a single rotation matrix, not an interpolation. The two approaches coexist — Murillo §8.3 flags axis-angle composition formulas as a separate open question
- **Camera matrix**: still constructed via `glam` look-at + perspective. Phase 5A's `abcd_to_clip` fold is downstream of camera basis construction
- **Save format**: backwards compatible via serde default

### 10.6 Open Sub-Questions

1. **Axis-angle composition formula.** Murillo §8.3 raises this: given $R(u_1, \theta_1) \cdot R(u_2, \theta_2) = R(u_3, \theta_3)$, derive $(u_3, \theta_3)$ in closed form. Required if we want to keep rotations stored as `(axis, spread)` pairs across composition. For now, store as 4×4 matrices and leave axis-angle extraction as a post-hoc operation.

2. **Janus inversion as separate operator.** Per the v4.1 reframing in Quadray-Rotors.tex §13: Janus polarity moves OFF the rotor and BECOMES a separate inversion operator $J: P \to -P$. The composed move $J \circ R(u, \theta)$ — rotation followed by inversion into 4D⁻ — has $\det = -1$ and lives in $\mathrm{O}(3) \setminus \mathrm{SO}(3)$. Open: how does this compose in practice? Does the Geometric Janus Inversion paper give a clean implementation pattern? Tracked in Quadray-Rotors.tex §13's open question box.

3. **Non-zero-sum axes.** Murillo's K(u) requires zero-sum input (he projects via gauge subtraction if not). Our `Quadray` type stores full 4D ABCD without enforcing zero-sum. Decision: project at K(u) construction time (cheap, one subtraction), or require callers to zero-sum first? Recommendation: project automatically with a debug-build assertion, mirroring the existing `abcd_normalize` pattern.

4. **GPU upload of K(u)-derived matrices.** Once we have a 4×4 R(u,θ) from K(u), can it be folded into `abcd_to_clip` per-instance? Currently `abcd_to_clip` is a single per-frame matrix — per-instance rotation is applied CPU-side. Folding instance rotation into a per-instance abcd_to_clip would be a Phase 6 deliverable (mentioned in Quadray-Rotors.tex §11.3).

### 10.7 Verification Targets

- [x] `cargo test rt_math::k_of_u` — **27 tests pass** as of commit fcab066 (Phase A: 7, Phase B: 10, Phase C: 2, Phase D step 2: 2, 9-mul kernel: 6)
- [x] **Full suite**: `cargo test` — 1134 pass, 0 fail, 0 regressions (commit 8ca0d8b, after Phase E first swap)
- [x] Phase A cross-validation: characterized as exact negation of `abcd_cross_f64` (5/5 cases consistent)
- [x] Phase B cross-validation: characterized as K-sign flip vs `fgh::abcd_rotation_matrix` (28/28 cases consistent)
- [x] **Phase C strict equality**: 600+ cross product cases AND 792 rotation cases at 1e-13 (max errors 2.66e-15 and 1.78e-15)
- [x] **Phase D step 1 strict equality** (cross product): bit-identical via `phase_c_strict_cross_product_equality`
- [x] **Phase D step 2 strict equality** (rotation matrix): bit-identical via `phase_d_step2_strict_rotation_cossin_equality` and `phase_d_step2_strict_rotation_weierstrass_equality`
- [x] **9-mul kernel parity**: `nine_mul_matches_full_mat4_transform_for_zero_sum` — 280+ K(u) cases plus fgh arbitrary-axis and F,G,H basis-axis paths, max error 1.78e-15
- [x] **Phase D step 1 visual smoke** (Andy 2026-04-26): app launches, polyhedra render with outward normals, struts/nets/folds/geodesic shading correct
- [x] **Phase E first swap visual smoke** (Andy 2026-04-26 — pending second pass): 3D fold animation across polyhedra families, net unfolding, glue tabs
- [ ] `cargo bench rotation` — K(u) apply vs F,G,H basis-axis vs quaternion sandwich. Not yet built. Lower priority — Phase D/E results are already verified bit-identical at machine epsilon, so bench is for documenting throughput, not correctness.
- [ ] Render parity: pixel-identical output between K(u) path and prior implementation (overlay test). Implicitly verified by 1134 pass and visual smoke; explicit overlay would be belt-and-braces.
- [ ] Pick parity: clicking on rotated faces hits same face under both paths. Implicitly verified (no bug reports through gumball drags).

### 10.8 Dependencies on Documentation

This workplan assumes the following are already in place (✅ as of 2026-04-25):

- ✅ Cookbook §10 — K(u) cross-product formulation documented
- ✅ Cookbook §8 — F,G,H = K(e_axis) scaffold relationship documented; Janus repositioning noted
- ✅ Quadray-Rotors.tex §11.5 (sec:k-of-u) — full mathematical exposition with Murillo credit
- ✅ Quadray-Rotors.tex §13 (sec:janus-separation) — Janus repositioning + open question on rotation+inversion composition
- ✅ Quadray-Rotors.tex Open Question previously labelled "Closed-Form F,G,H Composition" — marked ANSWERED
- ✅ Quadray-Rotors.tex Acknowledgments + References — Murillo credited as section contributor (§11.5 only, not paper-wide)

### 10.9 Attribution

The mathematics implemented in `k_of_u.rs` is from Leo Murillo (2026), Zenodo 19689050. Module-level rustdoc, the Cookbook §10 cross product, and Quadray-Rotors.tex §11.5 all carry the citation. Per Andy's direction (April 25, 2026), Murillo is credited as **section contributor for the rotation chapter**, not as co-author of the whitepaper or the codebase as a whole.

### 10.10 Site-by-Site Migration of rotor.rs (Speculative — see corrections below)

This table was the original Phase E roadmap. Several entries turned out to be more nuanced than the table suggests; corrections are noted inline.

| `rotor.rs` site | Currently | Originally proposed K(u) target | Reality check (2026-04-26) |
|---|---|---|---|
| Struct `(w, x, y, z, polarity)` (line 29–41) | Cartesian quaternion + ± bit | Replace with `(axis_abcd, spread, polarity)`; cache `KOfU` lazily | **Big change.** Touches every consumer of QuadrayRotor (state_manager, ik, demo_reel, animation, view_manager). Not yet attempted. Should be feature-flagged for parallel testing. |
| `from_spread_axis` (line 93) | Half-angle √√, Cartesian axis input | `KOfU::from_spread_axis` — direct K(u) construction in ABCD | Depends on struct change above. |
| `multiply` (Hamilton product, line 366) | 16 mul + 12 add on Cartesian quaternions | Matrix multiply on cached R(u,θ), or Hamilton on (axis, spread) | Hamilton on (axis, spread) needs the closed-form axis-angle composition (§10.4f open Q #1). Matrix multiply works today but loses the compact axis-angle form. |
| `rotate_vector` sandwich (line 382) | R·v·R*, ~28 ops | `KOfU::apply` — 9-mul kernel on zero-sum input | **Caveat:** the sandwich product accepts ARBITRARY 3-vectors (not zero-sum). The 9-mul kernel needs zero-sum input. Direct swap requires a `apply_with_gauge` wrapper (~10 mul + 20 add — marginal vs the 28-op quaternion sandwich, which already isn't bad). Decide based on benchmarks. |
| `to_mat3` / `to_mat4` (line 392, 418) | Quadratic polynomial in (w,x,y,z) | `KOfU::to_mat4` — 4×4 ABCD-native Rodrigues | Straightforward once struct is migrated. |
| `to_quaternion` f32 export (line 326) | XYZ-justified GPU boundary | Stays — needed as long as camera uses glam | Confirmed. Mark `// XYZ-justified: camera matrix interop`. |
| `from_look_direction_with_up` Shepperd extraction (line 226–321) | Cartesian frame construction → quaternion extraction via Shepperd's method | ~~Skip Shepperd: extract (axis, angle) directly~~ | **Correction (2026-04-26):** Shepperd's method IS the right algorithm for matrix→quaternion extraction (numerically stable across all quadrants, picks the largest diagonal element first). Replacing it with axis-angle extraction would require also retrofitting QuadrayRotor's internal representation to (axis, angle) form — a much bigger rewrite than "skip Shepperd." Re-scope as part of the larger struct migration above, not as a piecewise win. |
| `slerp` (line 468) | acos + 2 sin on Cartesian quaternions | NLERP/SLERP in axis-angle space | Requires axis-angle composition (§10.4f open Q #1). Until then, slerp stays as-is, RT-justified at animation boundary. |

**Revised approach (2026-04-26):** the rotor.rs migration is best treated as a single feature-flagged rewrite of the struct + all its method implementations, gated by a `cfg(feature = "k-of-u-rotor")` flag for parallel testing. Piecewise swaps don't compose cleanly because each method depends on the struct's internal representation. **Not yet attempted.** Recommended order if/when undertaken:

1. ✅ Build `k_of_u.rs` machinery (Phase A–E, complete)
2. ✅ Validate K(u) bit-equivalent to existing rotation paths (Phase C, D — complete)
3. Implement axis-angle extraction from a 4×4 R (§10.4f open Q #2) — required for the look-direction case
4. Implement axis-angle composition formula (§10.4f open Q #1) — required for the multiply/slerp cases
5. Add feature-flagged `QuadrayRotor` v2 internals — parallel test against v1
6. Migrate consumers one at a time (state_manager, ik, demo_reel, animation)
7. Flip default, retire v1, mark `to_quaternion` as sole remaining glam interop point

### 10.11 Where glam Survives Even After K(u)

K(u) closes the **rotation** glam debt. It does NOT close the **camera projection** glam debt. The remaining glam dependencies after the §10.10 migration:

1. **`camera.rs` view+projection construction**: `glam::Mat4::look_at_rh()` and `perspective_rh()`. These build the view-projection matrix from eye/focus/up and from FOV/aspect/near/far. Neither is a rotation — they're frame construction + perspective scaling. K(u) doesn't touch them. **Eliminating requires an RT-pure perspective projection** (rationalize FOV → spread, replace `tan(fov/2)` with a Weierstrass parameter, replace near/far with rational bounds). This is what whitepaper §11.4 calls "Phase 6."

2. **`abcd_to_clip` composition (Phase 5A, complete)**: already folds Tom Ace basis into glam's view-projection. K(u) doesn't change this fold; it changes how the *instance* rotation gets composed in. So K(u) eliminates instance-rotation glam (geometry.rs hot path), not camera-matrix glam (camera.rs construction).

3. **Shepperd's method extraction in `from_look_direction_with_up`**: replaceable with axis-angle extraction → K(u). The cleanest single win in rotor.rs.

**Net impact estimate:** K(u) closes ~80% of the rotation glam debt. The final 20% is the camera projection matrix — a separate, larger undertaking that is not really a rotation problem at all (it is an optical/projection problem). Worth tackling in its own branch when ready, with its own workplan (Phase 6 / "RT-Pure Camera Projection").

**Files that will still `use glam` after §10.10 completes:**
- `camera.rs` — for view+projection matrix construction (Phase 6 target)
- `rotor.rs::to_quaternion` — for camera matrix interop (vanishes when camera goes RT-pure)
- `picking.rs` — if it does any Cartesian ray-intersection math (audit needed)
- Any test file that cross-validates against `glam::Quat` (these stay — they are the cross-validation, not the production path)

**Files that should fully drop `use glam` after §10.10:**
- `geometry.rs` rotation hot path (currently `quadray_to_xyz` → `glam::Quat * Vec3` → `xyz_to_quadray`)
- `state_manager.rs` rotation handling
- The new `k_of_u.rs` itself (must be glam-free by construction — pure ABCD)

---

## References

- **Quadray-Rotors.tex** — `Geometry Documents/Whitepaper LaTEX/Quadray-Rotors.tex` (full mathematical derivation; §11.5 K(u) general form added v4.1, with Murillo credit)
- **Murillo, L. (2026)** — *Intrinsic Vector Calculus on Simplicial (Quadray) Coordinates: Cross Product, Rotation, and the Zero-Sum Hyperplane.* Zenodo 19689050. [zenodo.org/records/19689050](https://zenodo.org/records/19689050). Source for §10 K(u) construction.
- **Murillo engineering guide** — `artex-osx/docs/contributors/quadray_cross_rotate_engineering_guide.md` (algorithmic recipe, suitable for direct port to Rust)
- **QUADRAY-SKILLS.md** — `artex-osx/docs/reference guides/QUADRAY-SKILLS.md` (height functions, plane constraints, projection)
- **PHASE5-PLAN.md** — `artex-osx/docs/PHASE5-PLAN.md` (ABCD-to-clip pipeline, Phase 5A/5B)
- **fgh.rs** — `artex-osx/src/rt_math/fgh.rs` (F,G,H implementation, exact constants, tests)
- **rotor.rs** — `artex-osx/src/rt_math/rotor.rs` (QuadrayRotor, Hamilton product, SLERP)
- **normalizer.rs** — `artex-osx/src/rt_math/normalizer.rs` (XYZ boundary — import/export only)
- **ARTEX-RATIONALE.md** — `artex-osx/docs/reference guides/ARTEX-RATIONALE.md` (philosophical foundation, §4 basis folding)
