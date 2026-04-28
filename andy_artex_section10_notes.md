# ARTex Section 10 Review Notes

These are working notes for Leo, not a ready-to-send reply.

## Acknowledgement to lead with

Andy has clearly put a lot of serious engineering work into this. The strength of Section 10 is not just that it picks up the K(u) construction, but that it does so in a production-minded way: shadow-only phases, strict equality tests against the old paths, visual smoke checks, explicit rollback points, and honest notes where a proposed swap turned out not to be clean. That is exactly the kind of discipline that lets a new mathematical primitive enter a live Rust/Metal geometry pipeline without breaking the application.

The best parts to recognize:

- The K(u) integration is being validated at three levels: cross product, operator matrix, and full rotation.
- The codebase-orientation wrapper idea is pragmatic. It keeps net/strut/fold behavior stable while preserving the Murillo-faithful form for verification.
- The 9-mul kernel was only deployed where the input was believed to be zero-sum, which is the right instinct.
- The rotor.rs migration was correctly re-scoped once it became clear that piecewise replacement would not compose cleanly.
- The Janus work is being treated as an architectural concern, not as a local sign hack.

## Main recommendation

Make K(u) the semantic center for arbitrary-axis Quadray rotation, but keep FGH as a specialized exact lane for named ABCD basis-axis rotations. That framing helps both sides:

- K(u) is the general intrinsic operator.
- FGH remains a useful fast path where it is genuinely simpler.
- Zero-sum becomes the algebraic default for rotation/cross-product work.
- Raw ABCD tuples remain available at storage, import/export, and legacy boundaries until the whole pipeline is audited.

This avoids turning the conversation into "FGH versus K(u)". The cleaner split is "specialized exact basis-axis path versus general arbitrary-axis path".

## Potential corrections to Section 10

### 1. Be precise about M-normalization and the raw K matrix

Section 7.5 of the v2 paper says that under the implementation metric

```text
M = 4I - J = 3G
```

the raw cyclic-difference matrix works directly, without the paper-body `1/sqrt(3)` factor, when the axis is already zero-sum and M-unit:

```text
sum(u_i) = 0
sum(u_i^2) = 1/4
```

That is the exact-arithmetic win. It means rational M-unit axes, such as permutations of `[1/4, 1/4, -1/4, -1/4]`, keep K(u), K(u)^2, and the 9-mul apply kernel rational.

It does not mean every ABCD named basis ray stays rational after unit normalization. For example, `e_A = [1,0,0,0]` projects to `[3/4,-1/4,-1/4,-1/4]`, whose M-norm is `sqrt(3)`. If K(u) normalizes that to an M-unit axis, a `sqrt(3)` enters the axis and then cancels at special angles such as 120 degrees. Andy's point about FGH being the cleaner exact path for A/B/C/D rotations is therefore fair.

Suggested wording change:

```text
In the M = 4I - J convention, the raw cyclic-difference K matrix is normalized
only when the input axis is already zero-sum and M-unit. The general constructor
may still introduce one square root when normalizing a non-unit axis. FGH remains
the exact fast path for named A/B/C/D basis-axis rotations.
```

### 2. Soften "K(e_axis) reduces to FGH"

That statement is mathematically right after the relevant conventions are aligned, but implementation readers can misread it as "call K on raw e_A and get the same exact arithmetic path as FGH."

Safer phrasing:

```text
After zero-sum projection, M-normalization, angle convention, and orientation
convention are aligned, the K(u) path matches the FGH basis-axis rotations.
FGH is still preferred for those four named axes because it reaches the exact
rational/permutation matrices without first introducing a normalizing radical.
```

This also matches Andy's shadow tests: the relationship was an exact sign/orientation convention, not a failed derivation.

### 3. Tighten the zero-sum assumption around the 9-mul kernel

This is probably the most important engineering point.

The 9-mul kernel is valid for zero-sum inputs. A displacement `local = v - origin` is zero-sum only if the chosen representatives of `v` and `origin` have the same coordinate sum. If cube/Catalan cases use vertices whose sums differ, then a direct reduced-kernel swap can silently change the gauge representative even when the rendered geometry looks close.

The sentence in Section 10.4d saying that `local = v - rot_origin` is zero-sum "by construction" should be guarded. Different vertices are not in the same gauge class; they are different points. What may be true is that the mesh has chosen representatives with a shared gauge sum. That should be asserted, not assumed.

Recommended API split:

```rust
// Fast path: caller proves sum(local) == 0.
fn apply_reduced_3x3(r_tilde: [[f64; 3]; 3], local_h: HVec4) -> HVec4;

// Safe path: accepts any ABCD representative, preserves its gauge component.
fn apply_with_gauge(r_tilde: [[f64; 3]; 3], local: [f64; 4]) -> [f64; 4] {
    let g = mean(local);
    let h = subtract_mean(local);
    let rh = apply_reduced_3x3(r_tilde, h);
    add_mean(rh, g)
}
```

If raw gauge preservation does not matter for a call site, the `+ g*ONE` restoration can be skipped. But for net/fold/Catalan code, preserving the representative may prevent downstream surprises.

Concrete test to add:

```text
For every reduced-kernel call site, assert either:
1. abs(sum(input)) < eps, or
2. the call goes through apply_with_gauge and preserves the input gauge sum.
```

### 4. Keep zero-sum as the algebraic default, but migrate through types

I agree with the instinct that zero-sum should become the default for the rotation/cross-product pipeline. It is the canonical gauge, removes redundancy, and enables the 9-mul apply kernel.

The safe migration path is not "project every tuple globally" in one pass. It is:

- Keep `AbcdPoint` or `QuadrayRaw` for persisted/imported/legacy coordinates.
- Introduce `HVec4` for zero-sum vectors with a constructor that subtracts the mean.
- Optionally introduce `HVec3Packed` for hot loops, storing `(a,b,c)` and recovering `d = -(a+b+c)`.
- Require `HVec4` for K(u), cross product, and reduced-kernel APIs.
- Use `apply_with_gauge` at boundaries where raw ABCD representatives still matter.

The storage win from 4 numbers to 3 is real in CPU data structures, but GPU buffers may still prefer 16-byte `vec4` alignment. So treat packed triples as a benchmarked optimization, not an automatic global rewrite.

### 5. Orientation convention: choose one public story

The current codebase appears to use the opposite orientation convention from Murillo's paper. Andy has already handled this cleanly with `abcd_cross_codebase` and `rotation_matrix_codebase`.

Long-term, the risk is having two unmarked conventions in circulation. Future contributors and agents will make mistakes if they cannot tell which convention a function is using.

Options:

- Keep the existing codebase orientation internally, but name it explicitly.
- Migrate to a right-handed public/default convention in a separate branch with a large orientation test suite.
- Expose both through an enum or clearly named functions, but never through two nearly identical unmarked APIs.

Suggested naming pattern:

```rust
enum OrientationConvention {
    CodebaseLegacy,
    MurilloRightHanded,
}
```

If a right-handed migration is desired, it should be its own branch. Do not mix it with the K(u) production swap. The tests should include outward normals, face winding, Janus inversion, net folding, struts, picking, and even/odd tetrahedral relabelings.

### 6. Clarify Janus normal language

A small wording correction may prevent confusion for agents.

Under central inversion `J: P -> -P`, edge vectors also negate, so a naive cross product computed from the transformed edges gives:

```text
(-u) x (-v) = u x v
```

So the computed cross product itself does not flip just because both inputs flipped. The reason the outward normal must flip is geometric: the face center moved from `c` to `-c`, and the old normal now points inward relative to the inverted body.

Practical wording:

```text
Janus should be an explicit inversion operator on geometry, with an explicit
normal-orientation policy for outward normals. The cross-product convention
does not need duplicate plus/minus functions; what needs testing is that
outward normals remain outward after J.
```

Suggested test:

```text
For convex faces, after Janus inversion and normal correction,
dot(face_center, outward_normal) > 0
```

using the same sign convention as the existing positive-universe tests.

### 7. Align the Shepperd note

Section 10.10 correctly says that replacing Shepperd extraction is not a clean piecewise K(u) win until the QuadrayRotor internal representation changes.

Section 10.11 then says Shepperd extraction is "the cleanest single win in rotor.rs." Those two statements pull against each other.

Suggested fix:

```text
Shepperd extraction remains justified while QuadrayRotor stores Cartesian
quaternion internals. It becomes replaceable only as part of a feature-flagged
QuadrayRotor v2 that stores axis/spread or an ABCD-native rotation
representation directly.
```

## FGH emphasis

FGH deserves to stay, but probably as a specialized lane rather than the mental center of the whole rotation model.

Questions worth answering with counters/benchmarks:

- How often do real user actions rotate about A/B/C/D rings?
- How often do IK, constraints, snapping, group drag, hinge/universal joints, or arbitrary transforms use non-basis axes?
- How much runtime is spent constructing rotation matrices versus applying them to many vertices?
- How much of the exactness benefit matters in interactive f64 rendering versus tests, code generation, and saved construction documents?

Likely outcome:

- Keep FGH for A/B/C/D UI rings and exact tetrahedral constants.
- Use K(u) for arbitrary axes, IK constraints, snap/group transforms, and future general rotation APIs.
- Let the 9-mul kernel optimize application after a rotation matrix has already been built.

## Exact algebraic arithmetic

Leo's intuition here is sound. The general idea is standard: exact arithmetic in a number field, such as `Q[sqrt(2), sqrt(3)]`, where expressions are carried symbolically and simplified by rules like:

```text
sqrt(3) * sqrt(3) = 3
```

For ARTex, I would not put a general symbolic algebra engine in the interactive render path. A practical split is better:

- Runtime path: f64, with strict parity tests.
- Exact test path: rational and small quadratic-field types for golden cases.
- Codegen/constants path: exact generation of FGH and common K(u) matrices.
- Optional feature: `exact-rt` or `exact-quadray` for experiments and documentation builds.

Useful exact domains:

- `Q` for rational M-unit axes and rational Weierstrass `t`.
- `Q[sqrt(2)]`, `Q[sqrt(3)]`, or `Q[sqrt(2), sqrt(3)]` for common angles.
- A small quadratic-extension type may cover most current needs better than a full CAS.

This would let tests prove that radicals cancel where expected, while the app stays fast and simple.

## Catalan and non-zero-sum breakage checklist

Given Andy's note that Catalans broke because cube cases do not sum to zero, I would focus tests here before any broad migration:

- For every polyhedron family, record whether vertex representatives have constant coordinate sum.
- For every fold rotation, assert whether `v - rot_origin` is zero-sum before using the reduced kernel.
- Add a safe `apply_with_gauge` wrapper and compare it against the full 4x4 path.
- Test fold-flat and reverse-cascade unfolding across tetrahedra, cubes, Catalans, Archimedeans, and duals.
- Check render parity and pick parity after each swap.
- Check outward normal parity before and after Janus inversion.

This should separate true geometry issues from gauge-representative issues.

## Suggested near-term path

1. Keep Andy's current codebase-orientation wrappers as the production-safe path.
2. Add or strengthen zero-sum typed wrappers around the 9-mul kernel.
3. Add `apply_with_gauge` for call sites where the input representative may not be zero-sum.
4. Clarify Section 10 wording around M-unit axes, raw K, and FGH exactness.
5. Keep rotor.rs migration feature-flagged and postponed until axis-angle extraction/composition are ready.
6. Decide later, with tests and counters, whether a full right-handed convention migration is worth the churn.

The biggest help to Andy's agenda is probably not pushing a conceptual rewrite all at once. It is giving the agents sharper invariants: "this value is zero-sum", "this value is raw ABCD", "this convention is legacy/codebase", "this convention is Murillo/right-handed", and "this call site preserves gauge". Once those invariants are typed and tested, the broader zero-sum-first architecture becomes much less risky.
