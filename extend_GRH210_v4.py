"""
N=210 Apex Lemma v4: with chi_21 batch + 2 chi_35 pairs.
Coverage: 22/48 L-functions.

LMFDB CAPTCHA blocked further chi_35 fetches; this is the current stopping point
unless we either (a) get more LMFDB data via user-assisted fetching or
(b) compute remaining 26 L-functions via mpmath (estimated 30-40 min).

Status as of this version:
- 18 L-functions from prior sessions (zeta, chi_3, chi_5*3, chi_7*5, chi_15*3, chi_21*5)
- + 4 new L-functions from this session (chi_35(2)+(18) + chi_35(3)+(12) pairs)
"""

import sys, io, time
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from mpmath import mp, mpf, matrix
mp.dps = 300

# Inherit all data from v3, add new chi_35 batch
exec(compile(open(r'C:\Projects\simplicial\extend_GRH210_v3.py').read().split('# Compute and verify')[0], '<inline>', 'exec'))

# Add new chi_35 conjugate pairs to non_self_dual_all
non_self_dual_all["chi_35(2)+chi_35(18) pair (f=35)"] = sorted([mpf(g) for g in [
    "35.59910556888870191104038261084", "34.5491197196213397853178449292",
    "33.139790922880960360837633984477", "31.98429806201945131277114662520",
    "31.14316437994159622782128062278", "30.12097472286172158098414098320",
    "28.91438142656687972759492667454", "26.53942157582756157533475900835",
    "25.94738826735708365552515402428", "24.31453507290520542980915996304",
    "23.96053750711599078301222154631", "22.10785158455013824657689698595",
    "20.9722004665645462449841208562", "19.6913951972389108501187299340",
    "18.16097632199931193431851527847", "16.40798799212429862133596127345",
    "15.09673006095517454118607126277", "13.870216007044681308131658372130",
    "12.99469199329751140900192168461", "11.40305618408171642726960277184",
    "8.9326723563768611725471447826", "7.59617739475376023513821328415",
    "6.195058614860654066255917608380", "4.10981455216769926587429169531",
    "2.45955293864876159220403598747",
    "2.25482763699762490408729632759", "3.800184639831668899720305117076",
    "5.30810329549512608468832877963", "7.53940282731089718088345180747",
    "9.56053378114159156516744300472", "10.71454759968517399891237260839",
    "12.54940421952370673502148455321", "13.75107163835168794846892456630",
    "15.003608723005802107184334105923", "15.93436159450332709011586603405",
    "18.302937061750072741358329909129", "19.954979484248753356949264425323",
    "20.51981840154720851774899142914", "21.867376268165700036905272143251",
    "22.96795193488978953650872254987", "24.567079380133396770061055546504",
    "25.59616376233569921601209715488", "27.188152775860030134872747315948",
    "28.40474534221674878824998352695", "29.879416518472621948159014955233",
    "31.00485230188198038257288282362", "31.80334912458809387038562252908",
    "32.96917005755833550252605032144", "33.84273960730530060122891935750",
    "35.89377509879203932391478691188",
]])

non_self_dual_all["chi_35(3)+chi_35(12) pair (f=35)"] = sorted([mpf(g) for g in [
    "35.80013473603395144869932470468", "34.158330518742277288403798722381",
    "33.51379303900399491664496161263", "32.0350327755604333546765305005",
    "30.71671367385168065015716871519", "29.84923286999480506900671721143",
    "28.60477526369126469121963508977", "27.91872212879256090594703309199",
    "25.7071536840550789463868600973", "24.10864515671436679354702270075",
    "23.4376316269784483465833604334", "22.22675845269073007084478239975",
    "21.11571848579420403991928649107", "19.52193822755942282423909543918",
    "18.33506531340939685212571873723", "16.71797000479940638888174294937",
    "15.20299177757423858075662843866", "13.573690714928856642771938895439",
    "12.42726294034201006771538127779", "11.35423713312006801274194634192",
    "9.97974127688517494176518911515", "7.24740272572690371684591513095",
    "5.83395042694476754865003442461", "4.392224696474392375853104380304",
    "1.969169021137100745218735244449",
    "3.43481525921369310600501690633", "5.138662754376125234002452406466",
    "6.19593039359663724126985999563", "8.03553049727166256414221079787",
    "10.33870006154565848158924862132", "11.72876029289555446369806732339",
    "12.97760753792570457240425600923", "14.62692708812760852913901544285",
    "15.94113780529554755218316419443", "16.81027988209426194463775545133",
    "18.271195512051699914532146571234", "20.55777022636353710996272154172",
    "21.59312202463794910859267667105", "22.71506978607732521960258885206",
    "23.62416837487569539975816556832", "24.912832447440480017061203137664",
    "26.40286115223966556390009930542", "27.60985463714245214892458399196",
    "29.21732571396782478724090916253", "30.08133720772457709176164179164",
    "31.84906682296229395054317923286", "32.524606221947250608406599823684",
    "33.93429512782188324977923086595", "34.4802257503679678150429883356",
    "35.749660366071901960504264976776",
]])

# Recompute with extended data
n_sd = len(self_dual_all)
n_pairs = len(non_self_dual_all)
n_total_L = n_sd + 2 * n_pairs

print("=" * 78)
print(f" N=210 Apex Lemma — v4 (chi_21 + 2 chi_35 pairs)")
print(f" Coverage: {n_total_L}/48 L-functions ({100*n_total_L/48:.1f}%)")
print("=" * 78)
print()
print(f" Self-dual ({n_sd}):")
for name in self_dual_all: print(f"   - {name}")
print(f" Non-self-dual pairs ({n_pairs}):")
for name in non_self_dual_all: print(f"   - {name}")
print()

M_MAX = 130

def jc(m):
    total = mpf(0)
    for zs in self_dual_all.values():
        total += 2 * sum(z ** (-2 * m) for z in zs)
    for zs in non_self_dual_all.values():
        total += 2 * sum(z ** (-2 * m) for z in zs)
    return total

t0 = time.time()
ell = [None] + [jc(m) for m in range(1, M_MAX + 1)]
print(f"Cumulants in {time.time()-t0:.1f}s. ell_1 = {mp.nstr(ell[1], 6)}")

all_g = []
for zs in self_dual_all.values(): all_g.extend(zs)
for zs in non_self_dual_all.values(): all_g.extend(zs)
gamma_min = min(all_g)
source = ""
for name, zs in self_dual_all.items():
    if min(zs) == gamma_min: source = name; break
for name, zs in non_self_dual_all.items():
    if min(zs) == gamma_min: source = name; break
print(f"gamma_min = {float(gamma_min):.4f} from {source}")

print()
print("Asymptotic check (ell_m / (2*gamma_min^-2m)):")
for m in [40, 60, 80, 100]:
    print(f"  m={m}: {float(ell[m] / (2 * gamma_min ** (-2 * m))):.4f}")

def ldl(M):
    n = M.rows
    A = matrix(n, n)
    for i in range(n):
        for j in range(n):
            A[i, j] = M[i, j]
    diags = []
    for k in range(n):
        d = A[k, k]; diags.append(d)
        if d <= 0: return False, min(diags), k
        for i in range(k+1, n):
            f = A[i, k] / d
            for j in range(k+1, n):
                A[i, j] -= f * A[k, j]
    return True, min(diags), n

def H(n):
    M = matrix(n+1, n+1)
    for i in range(n+1):
        for j in range(n+1):
            M[i, j] = ell[i+j+1]
    return M

def J(n):
    M = matrix(n+1, n+1)
    for i in range(n+1):
        for j in range(n+1):
            M[i, j] = ell[i+j+2]
    return M

print()
print("=" * 78)
print(" Hankel positivity")
print("=" * 78)
print(f"  {'n':>3} {'H_n':>8} {'min D(H)':>22} {'J_n':>8} {'min D(J)':>22}")
print("  " + "-" * 68)

t0 = time.time()
passed = 0
n_to_test = list(range(0, 16)) + list(range(16, 40, 2)) + list(range(40, 65, 5))
for n in n_to_test:
    h_psd, h_min, _ = ldl(H(n))
    j_psd, j_min, _ = ldl(J(n))
    print(f"  {n:>3} {'PSD' if h_psd else 'FAIL':>8} {mp.nstr(h_min, 5):>22} "
          f"{'PSD' if j_psd else 'FAIL':>8} {mp.nstr(j_min, 5):>22}")
    if h_psd and j_psd: passed += 1

print()
print(f"Verified: {passed}/{len(n_to_test)} sampled rungs PSD")
print(f"Wall time: {time.time()-t0:.1f}s")

print()
print("=" * 78)
print(" Cumulative N=210 status")
print("=" * 78)
print()
print(f"{'Round':<35} {'L-funcs':>10} {'gamma_min':>10} {'ell_1':>10}")
print("-" * 70)
print(f"{'Inherited from N=30':<35} {'8':>10} {'2.7346':>10} {'1.7736':>10}")
print(f"{'+ chi_7 batch (5/5)':<35} {'13':>10} {'2.5094':>10} {'3.0024':>10}")
print(f"{'+ chi_21 batch (5/5)':<35} {'18':>10} {'1.6120':>10} {'5.9225':>10}")
print(f"{'+ 2 chi_35 pairs (4/15) THIS':<35} {'22':>10} "
      f"{f'{float(gamma_min):.4f}':>10} {f'{float(ell[1]):.4f}':>10}")
print(f"{'TARGET: complete N=210':<35} {'48':>10} {'?':>10} {'?':>10}")
print()
print(f"Coverage: 22/48 = {100*22/48:.0f}%")
print(f"Remaining: 26 L-functions (chi_35: 11 more, chi_105: 15)")
