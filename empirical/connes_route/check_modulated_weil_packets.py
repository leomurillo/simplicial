"""Independent high-precision spot checks; not interval certificates."""
import json
from pathlib import Path
import mpmath as mp
from probe_translated_prime_cancellation import prime_powers

mp.mp.dps = 60
a = mp.log(2)
def g(v):
    return 2*mp.exp(-abs(v))-mp.exp(abs(v))/2
def G(s):
    return (5-4*mp.cosh(a*s))/(1-s*s)
def integ(fun):
    return mp.quad(fun, [-a, 0, a])

records = json.loads(Path(__file__).with_name('probe_modulated_weil_packets.json').read_text())['samples']
out = []
for w, X in [(14, 10), (50, 100), (100, 1000)]:
    row = next(r for r in records if r['omega']==w and r['X']==X)
    P = mp.fsum(mp.log(p)/mp.sqrt(n)*g(mp.log(mp.mpf(n)/X))*
                mp.exp(-1j*w*mp.log(mp.mpf(n)/X))
                for n,p in prime_powers(2*X) if n >= mp.mpf(X)/2)
    D = mp.mpf(X)**(-mp.mpf('2.5'))*integ(
        lambda v:g(v)*mp.exp((mp.mpf('2.5')+1j*w)*v)/(1-mp.exp(2*v)/X**2))
    K = mp.sqrt(X)*G(mp.mpf('.5')-1j*w)-P-D
    q = 2*mp.re(G(mp.mpf('.5')-1j*w))-mp.mpf('1.5')*(
        mp.euler+mp.log(4*mp.pi)+mp.log(mp.tanh(a/2)))-mp.quad(
        lambda v:(mp.exp(v/2)*g(v)*mp.cos(w*v)-mp.mpf('1.5'))/mp.sinh(v), [0,a])
    out.append({'omega':w,'X':X,'q':mp.nstr(q,45),
                'K_real':mp.nstr(mp.re(K),45),'K_imag':mp.nstr(mp.im(K),45),
                'double_K_error':float(abs(K-complex(row['K_real'],row['K_imag']))),
                'double_q_error':float(abs(q-row['q']))})
result = {'status':'60-digit spot checks, not rigorous interval enclosures','samples':out}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
