"""Exact reflection checks and numerical Mellin diagnostics (not interval proofs)."""
import json
from pathlib import Path
import mpmath as mp
from signed_periodic_majorant import RULES

mp.mp.dps = 60
rho = mp.zetazero(1)
kappa = abs((1-mp.power(2,-rho))/rho)**2/4
rows = []
for L,a in RULES.items():
    h = -sum(a.values())
    g = [sum(v*(j//d) for d,v in a.items()) for j in range(L)]
    assert h >= 1 and all(0 <= v <= h for v in g)
    assert all(g[j]+g[L-1-j] == h for j in range(L))
    delta = -sum(mp.mpf(v)*mp.log(d)/d for d,v in a.items())-mp.mpf('.5')
    assert delta*h >= kappa
    rows.append({'period':L,'step_height':h,'delta':str(delta),
                 'delta_times_height':str(delta*h),'exact_reflection':True})

L=12
a=RULES[L]
g=[sum(v*(j//d) for d,v in a.items()) for j in range(L)]
checks=[]
for s in (mp.mpc('.3','2'),rho,mp.mpc('.8','7'),mp.mpc('1.4','1')):
    periodic=mp.power(L,-s)/s*sum(g[j]*(mp.zeta(s,mp.mpf(j)/L)
                                   -mp.zeta(s,mp.mpf(j+1)/L))
                                for j in range(1,L))
    analytic=mp.zeta(s)/s*sum(v*mp.power(d,-s) for d,v in a.items())
    error=abs(periodic-analytic)
    assert error < mp.mpf('1e-50')
    checks.append({'s':str(s),'absolute_error':str(error)})

out={'note':'Decimal values are not interval-certified; proofs are in the companion note.',
     'first_zero_approx':str(rho),'kappa_approx':str(kappa),
     'rules':rows,'mellin_checks':checks}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
