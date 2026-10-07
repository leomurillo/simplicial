"""After the final run: confirm n=320 clean, print the rows the report needs, and
re-verify the -1/24n and +3/4 drift constants and lambda_1^arith=gamma on the FINAL data."""
import mpmath as mp, json, os
mp.mp.dps = 60
_rp = os.path.join(os.path.dirname(os.path.abspath(__file__)), "reports",
                   "li_coefficients_table.json")
d = json.load(open(_rp))
lam  = {int(k): mp.mpf(v) for k, v in d["lambda"].items()}
arch = {int(k): mp.mpf(v) for k, v in d["lambda_arch"].items()}
N = max(lam); g = mp.euler
def lead(n): return (mp.mpf(n)/2)*(mp.log(n)-1-mp.log(2*mp.pi)+g)
print(f"NMAX in JSON = {N}, all_positive = {d.get('all_positive_up_to_NMAX')}")
print("\nTail cleanliness (arch-(lead+3/4))*n -> -1/24 = -0.0416667 :")
for n in [280,300,310,320]:
    if n>N: continue
    print(f"  n={n}: {mp.nstr((arch[n]-lead(n)-mp.mpf(3)/4)*n,8)}")
print("\nReport rows:")
for n in [1,10,25,50,100,150,200,250,300,320]:
    if n>N: continue
    ar=lam[n]-arch[n]
    m = lam[n]/arch[n] if arch[n]!=0 else mp.mpf('nan')
    r = abs(ar)/arch[n] if arch[n]>0 else mp.mpf('nan')
    print(f"  n={n:3d}: lam={mp.nstr(lam[n],10):>13} arch={mp.nstr(arch[n],10):>13}"
          f" arith={mp.nstr(ar,8):>11} r={mp.nstr(r,5):>9} m={mp.nstr(m,8)}")
print(f"\nlambda_1^arith - gamma = {mp.nstr((lam[1]-arch[1])-g,4)}")
print(f"min lambda_n (n>=1) at n={min(range(1,N+1),key=lambda k:lam[k])}: "
      f"{mp.nstr(min(lam[k] for k in range(1,N+1)),8)}")
mm=min(range(10,N+1),key=lambda k:lam[k]/arch[k])
print(f"min margin (n>=10) at n={mm}: {mp.nstr(lam[mm]/arch[mm],8)}")
amx=max(range(2,N+1),key=lambda k:abs(lam[k]-arch[k]))
print(f"max|arith| at n={amx}: {mp.nstr(lam[amx]-arch[amx],6)}")
