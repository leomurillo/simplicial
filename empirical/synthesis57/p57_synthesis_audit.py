"""
Paper 57 certificate: the lecture's numbers (exact or CODATA-exact) and a cross-reference audit of the synthesis.
fractions / math / re only.  Usage: python p57_synthesis_audit.py

PRE-REGISTERED (written 2026-10-02 before the first run)
  L1 [exact] Johnson-Nyquist: sqrt(4 k_B T R) for R = 1 kOhm, T = 300 K is 4.0703 nV/sqrt(Hz) (4 significant figures);
     k_B = 1.380649e-23 J/K exactly (SI 2019).
  L2 [exact] Landauer: k_B T ln 2 at 300 K is 2.8710e-21 J (0.017918 eV with e = 1.602176634e-19 C exactly).
  L3 [exact] coaxial line L' = 250 nH/m, C' = 100 pF/m: v = 2e8 m/s, Z = 50 Ohm exactly (rational arithmetic).
  L4 [exact] vacuum: c = 1/sqrt(mu0 eps0) = 299792458 m/s to 1e-9 and Z0 = sqrt(mu0/eps0) = 376.730313668 Ohm to 1e-8
     (CODATA 2018 mu0 = 1.25663706212e-6, eps0 = 8.8541878128e-12).
  L5 [exact] Pendry-Bekenstein: a single channel at P = 1 W carries at most sqrt(pi P/(3 hbar)) = 9.966e16 nats/s
     (hbar = 1.054571817e-34 J s).
  L6 [exact] the two-temperature copy thresholds quoted in the lecture: at Delta T/T = 1/10 the least denominator of a
     fraction strictly inside (x, x(1 + 1/10)) is 11 for x = 1/2 and 3 for x = 1/phi (Stern-Brocot, exact predicates);
     and the D3Q15 weights 8:1 make sum w (k.delta)^4 proportional to |k|^4 (integer polynomial identity).
  A1 [audit] every bold label that Paper 57 cites exists, bold, in the cited manuscript (list below); no dangling
     reference.                                                                L: any missing label.
  A2 [audit] no manuscript touched in this round contains a control character (backslash-mangling class) and the
     word "headline" does not occur in the body of PortPrinciple.md.             L: otherwise.

RUN LOG
  Run 1 (2026-10-02, p57_run1.log): 7/8.  L2 FAILED on a PRE-REGISTRATION TRANSCRIPTION ERROR: the stated reference
  0.017918 eV is mis-rounded; k_B (300 K) ln 2 / e = 0.0179191 eV, so the 5e-5 tolerance was missed by 6e-6 relative.
  The joule value (2.8710e-21 J) and the manuscript's "~0.018 eV" are correct.  Failure retained; reference corrected to
  0.017919 eV.  Run 2 is NOT BLIND for L2.  (Also noted: L5's stated 9.966e16 is likewise rounded up -- the value is
  9.9650e16 nats/s -- but it lies inside its 5e-4 tolerance and passed; left as pre-registered.)
"""
import math, re, os
from fractions import Fraction as Fr

res = []
def check(name, ok, detail=""):
    res.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}", flush=True)

kB = 1.380649e-23; e = 1.602176634e-19; hbar = 1.054571817e-34
v1 = math.sqrt(4 * kB * 300 * 1000)
check("L1 Johnson noise of 1 kOhm at 300 K", abs(v1 / 4.0703e-9 - 1) < 5e-5, f"{v1:.6e} V/sqrt(Hz)")
EL = kB * 300 * math.log(2)
check("L2 Landauer bound at 300 K", abs(EL / 2.8710e-21 - 1) < 5e-5 and abs(EL / e / 0.017919 - 1) < 5e-5,
      f"{EL:.6e} J = {EL / e:.6f} eV")
Lc, Cc = Fr(250, 10 ** 9), Fr(100, 10 ** 12)
check("L3 coax speed and impedance", 1 / (Lc * Cc) == Fr(4 * 10 ** 16) and Lc / Cc == 2500,
      f"v^2 = {1 / (Lc * Cc)}, Z^2 = {Lc / Cc}")
mu0, eps0 = 1.25663706212e-6, 8.8541878128e-12
c = 1 / math.sqrt(mu0 * eps0); Z0 = math.sqrt(mu0 / eps0)
check("L4 vacuum light speed and impedance", abs(c / 299792458 - 1) < 1e-9 and abs(Z0 / 376.730313668 - 1) < 1e-8,
      f"c = {c:.3f} m/s, Z0 = {Z0:.9f} Ohm")
Sd = math.sqrt(math.pi * 1.0 / (3 * hbar))
check("L5 Pendry-Bekenstein entropy rate at 1 W", abs(Sd / 9.966e16 - 1) < 5e-4, f"{Sd:.4e} nats/s")

def simplest(below_lo, above_hi):
    lp, lq, rp, rq = 0, 1, 1, 0
    while True:
        mp_, mq = lp + rp, lq + rq
        if below_lo(mp_, mq):
            lp, lq = mp_, mq
        elif above_hi(mp_, mq):
            rp, rq = mp_, mq
        else:
            return mp_, mq
x = Fr(1, 2); d = Fr(1, 10)
p, q = simplest(lambda a, b: Fr(a, b) <= x, lambda a, b: Fr(a, b) >= x * (1 + d))
# golden: x = (sqrt5 - 1)/2, window (x, 1.1 x); exact integer predicates for a/b <= x and a/b >= 11x/10
below = lambda a, b: (2 * a + b) ** 2 <= 5 * b * b                       # a/b <= (sqrt5-1)/2
above = lambda a, b: (20 * a + 11 * b) ** 2 >= 5 * (11 * b) ** 2           # a/b >= 1.1 (sqrt5-1)/2
pg, qg = simplest(below, above)
# D3Q15 identity: 8 * sum_sc (k.d)^4 + sum_bcc (k.d)^4 = 24 |k|^4, checked on integer vectors k
import itertools
sc = [v for v in itertools.product((-1, 0, 1), repeat=3) if sum(abs(t) for t in v) == 1]
bcc = list(itertools.product((-1, 1), repeat=3))
ok_q = all(8 * sum(sum(a * b for a, b in zip(kv, v)) ** 4 for v in sc) +
           sum(sum(a * b for a, b in zip(kv, v)) ** 4 for v in bcc) == 24 * sum(t * t for t in kv) ** 2
           for kv in itertools.product(range(-3, 4), repeat=3))
check("L6 lecture thresholds (11 harmonic, 3 golden at dT/T = 1/10) and the D3Q15 identity",
      q == 11 and qg == 3 and ok_q, f"x=1/2: {p}/{q}; x=1/phi: {pg}/{qg}; D3Q15 identity on 343 vectors: {ok_q}")

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
CITES = {
    "PortPrinciple.md": ["Definition 2.5", "Proposition 2.3", "Proposition 4.4", "Theorem 4.1", "Theorem 4.5",
                         "Theorem 5.1", "Theorem 5.4", "Lemma 6.2", "Theorem 6.3", "Theorem 6.6", "Corollary 6.7",
                         "Theorem 6.9", "Proposition 6.9e", "Theorem 6.10", "Theorem 6.11", "Corollary 6.13",
                         "Proposition 6.14", "Theorem 7.1", "Theorem 7.2", "Lemma 7.4a", "Theorem 7.4",
                         "Proposition 7.5", "Open Problem 7.6", "Theorem 8.1", "Theorem 8.2", "Proposition 8.3",
                         "Theorem 8.4", "Proposition 8.5", "Theorem 9.1", "Theorem 9.3", "Theorem 10.1",
                         "Proposition 11.1", "Proposition 11.2"],
    "54_one_functional_from_passivity.md": ["Theorem 1", "Theorem 2", "Theorem 3", "Theorem 3Q", "Theorem 3H",
                                            "Theorem 4.7", "Theorem 4", "Proposition 2.1"],
    "55_the_network_of_ports.md": ["Theorem 2.2", "Proposition 2.3", "Theorem 3.5", "Proposition 3.7", "Theorem 3.8",
                                   "Theorem 4.1", "Theorem 4.2", "Corollary 4.3", "Theorem 4.4", "Theorem 5.1",
                                   "Theorem 6.1", "Theorem 6.2", "Theorem 6.6", "Lemma 6.7"],
    "56_the_dynamic_network.md": ["Theorem 2.1", "Corollary 2.2", "Corollary 2.3", "Proposition 2.4",
                                  "Proposition 2.5", "Proposition 2.6"],
    "53_passive_ports_and_the_explicit_formula.md": ["Theorem 3.1", "Lemma 3.2", "Corollary 4.1"],
}
missing = []
for fn, labels in CITES.items():
    txt = open(os.path.join(ROOT, fn), encoding="utf-8").read()
    for lab in labels:
        if not re.search(r"\*\*" + re.escape(lab) + r"[\s\(\*′]", txt):
            missing.append(f"{fn}: {lab}")
check("A1 [audit] every label cited by Paper 57 exists (bold) in its manuscript", not missing,
      "; ".join(missing) if missing else f"{sum(len(v) for v in CITES.values())} labels found")
bad = []
for fn in ["PortPrinciple.md", "55_the_network_of_ports.md", "56_the_dynamic_network.md",
           "57_one_inequality_asked_harder.md"]:
    pth = os.path.join(ROOT, fn)
    if not os.path.exists(pth):
        bad.append(f"{fn}: missing file"); continue
    s = open(pth, encoding="utf-8").read()
    cc = [hex(ord(ch)) for ch in s if ord(ch) < 32 and ch not in "\r\n"]
    if cc:
        bad.append(f"{fn}: control chars {cc[:4]}")
pp = open(os.path.join(ROOT, "PortPrinciple.md"), encoding="utf-8").read()
body = pp.split("-->", 1)[1] if "-->" in pp else pp
if "headline" in body.lower():
    bad.append("PortPrinciple body contains 'headline'")
check("A2 [audit] no control characters in the touched manuscripts; no 'headline' in the Port body", not bad,
      "; ".join(bad) if bad else "clean")
print(f"\nTOTAL: {sum(res)}/{len(res)} PASS")
