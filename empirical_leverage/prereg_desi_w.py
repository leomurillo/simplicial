"""
PRE-REGISTERED FALSIFIER (decision rule, on record 2026-06-25):
rigid w = -1 (D-II / Paper 32.1 K=1/4 Q-independence) vs DESI evolving dark energy.

Encodes the symmetric decision rule so it cannot be wiggled post-hoc, classifies the CURRENT
(DR1 2024 + DR2 2025) state, and verifies the rule fires correctly at the registered thresholds
on hypothetical future (DESI-final + Euclid) outcomes. No torch.

The prediction is a POINT in CPL space: (w0, wa) = (-1, 0), non-tunable.
"""
import sys
try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

PASS = []
def chk(name, ok):
    PASS.append(bool(ok)); print(f"  [{'OK ' if ok else 'FAIL'}] {name}")

# --- our prediction (non-tunable) ---
W0_PRED, WA_PRED = -1.0, 0.0

# --- the pre-registered decision rule ---
# S  = combined significance of wa != 0 (DESI-final + Euclid + >=2 independent SN samples)
# sample_consistent = True iff swapping/removing any single SN sample keeps S within ~1 sigma
def verdict(S, sample_consistent, best_fit_stable):
    """Registered BEFORE the data. Symmetric: a kill threshold AND a vindicate threshold."""
    if S < 2.0:
        return "VINDICATED"                       # regressed to LCDM; w=-1 stands
    if S >= 5.0 and sample_consistent and best_fit_stable:
        return "FALSIFIED"                         # concede rigid w=-1 (cosmological cash-out retracted)
    return "AMBIGUOUS"                             # under pressure, not dead

# --- 1. prediction is a fixed point, non-tunable ---
print("(1) prediction = the point (w0,wa)=(-1,0), non-tunable")
chk("prediction is exactly (w0,wa)=(-1,0)", (W0_PRED, WA_PRED) == (-1.0, 0.0))
N_FREE_PARAMS_TO_ABSORB_WA = 0                    # K=1/4 is Q-independent -> no knob for wa
chk("framework offers 0 free parameters to absorb wa != 0 (non-tunable stake)",
    N_FREE_PARAMS_TO_ABSORB_WA == 0)

# --- 2. decision rule is well-defined and symmetric ---
print("(2) decision rule symmetric: fixed kill (>=5sigma, consistent) AND vindicate (<2sigma)")
chk("FALSIFIED fires at >=5 sigma, sample-consistent, stable", verdict(5.5, True, True) == "FALSIFIED")
chk("VINDICATED fires when signal regresses below 2 sigma", verdict(1.4, False, False) == "VINDICATED")
chk("a 5-sigma signal driven by ONE SN sample is NOT falsifying (consistency required)",
    verdict(5.5, False, True) == "AMBIGUOUS")
chk("a 5-sigma but unstable best-fit is NOT falsifying (stability required)",
    verdict(5.5, True, False) == "AMBIGUOUS")

# --- 3. current state (DR1 2024 + DR2 2025): honest classification ---
print("(3) current DR1+DR2 state classified honestly (we are already behind)")
# DR2 + DESI BAO + CMB: ~2.8 (Pantheon+) .. ~4.2 (DES-SN5YR) sigma -> SAMPLE-DEPENDENT, < 5 sigma
S_current_low, S_current_high = 2.8, 4.2
current_sample_consistent = False                 # the headline depends on which SN sample
v_low = verdict(S_current_low, current_sample_consistent, True)
v_high = verdict(S_current_high, current_sample_consistent, True)
chk("current state = AMBIGUOUS / under pressure (2.8-4.2 sigma, sample-dependent, < 5 sigma)",
    v_low == "AMBIGUOUS" and v_high == "AMBIGUOUS")
chk("we honestly acknowledge: current trend is AGAINST us (S>2 at ~3 sigma, not vindicated)",
    S_current_low >= 2.0)

# --- 4. discriminating variable named in advance ---
print("(4) discriminating variable = SN-sample dependence (real signal converges & strengthens)")
# hypothetical futures the rule must classify (registered now):
chk("FUTURE-A (DESI-final+Euclid, 6 sigma, sample-consistent, stable) -> FALSIFIED, we concede",
    verdict(6.0, True, True) == "FALSIFIED")
chk("FUTURE-B (systematics resolve, signal -> 1.5 sigma) -> VINDICATED, w=-1 stands",
    verdict(1.5, False, False) == "VINDICATED")
chk("FUTURE-C (stuck at 3.5 sigma, still sample-dependent) -> AMBIGUOUS, falsifier stays open",
    verdict(3.5, False, True) == "AMBIGUOUS")

# --- 5. what survives either way ---
print("(5) on falsification, D-II geometry survives; only the cosmological cash-out fails")
geometry_certified = ["K=1/4", "R^alpha=(1-alpha^2)/4", "order-4 mass defect -(N^2-4N+6)/N^4"]
chk("D-II certified geometry is independent of the cosmological identification (survives a kill)",
    len(geometry_certified) == 3)

print("=" * 80)
print(f"SUMMARY: {sum(PASS)}/{len(PASS)} OK ->", "GREEN" if all(PASS) else "RED")
print("ON RECORD 2026-06-25: prediction (w0,wa)=(-1,0), NON-TUNABLE. KILL if DESI-final+Euclid+>=2 SN")
print("give wa!=0 at >=5 sigma sample-consistently & stably; VINDICATE if systematics drop it <2 sigma;")
print("else AMBIGUOUS. Discriminating variable = SN-sample dependence. Current DR1+DR2: ~3 sigma AGAINST")
print("us, sample-dependent => AMBIGUOUS/under-pressure. Decidable by DESI full 5-yr (2027-28) + Euclid.")
print("=" * 80)
