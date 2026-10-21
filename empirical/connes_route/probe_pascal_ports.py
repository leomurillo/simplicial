"""Exact Pascal/congruence and divisor-square checks. No RH claim."""
import json
import math
from pathlib import Path
import sympy as sp

t,u,z,c = sp.symbols('t u z c', real=True)
def B(n,x):
    return sp.Matrix(n,n,lambda i,j:sp.binomial(i,j)*x**(i-j) if i>=j else 0)
checks = {}
checks['pascal_group'] = sp.simplify(B(6,t)*B(6,u)-B(6,t+u)) == sp.zeros(6)
checks['pascal_inverse'] = sp.simplify(B(6,t)*B(6,-t)) == sp.eye(6)
checks['binomial_filter'] = all(sp.expand(sum(sp.binomial(m,j)*(-c)**(m-j)*z**j
                                      for j in range(m+1))-(z-c)**m)==0 for m in range(1,9))
J = sp.diag(1,-1)
Q = sp.simplify(B(2,t)*J*B(2,t).T)
checks['negative_direction_preserved'] = sp.expand(Q.det()) == -1

# A genuine positive-real Pick matrix test, with a planted off-axis quartet.
s = sp.symbols('s')
z0 = 2+sp.I/2
poly = (s*s+1)*(s*s+z0*z0)*(s*s+sp.conjugate(z0)**2)
Z = sp.cancel(sp.diff(poly,s)/poly)
pts = [sp.Rational(3,8)+2*sp.I, sp.Integer(1)]
vals = [Z.subs(s,p) for p in pts]
P = sp.Matrix(2,2,lambda j,k:sp.simplify((vals[j]+sp.conjugate(vals[k]))/(pts[j]+sp.conjugate(pts[k]))))
v = B(2,t).T.inv()*sp.Matrix([1,0])
checks['port_negative_diagonal'] = bool(P[0,0]<0)
checks['transported_negative_witness'] = sp.simplify((v.T*B(2,t)*P*B(2,t).T*v)[0]-P[0,0])==0

rows=[]
for D in [4,8,12]:
    H = sp.Matrix(D,D,lambda i,j:sp.Rational(1,sp.ilcm(i+1,j+1)))
    e=sp.eye(D)[:,0]
    raw=H.inv()*e
    opt=raw/raw[0]
    pascal=sp.Matrix([(-1)**j*sp.binomial(D-1,j) for j in range(D)])
    def report(v):
        return {'main_quadratic':str((v.T*H*v)[0]),
                'floor_error_bound':str(sum(abs(x) for x in v)**2)}
    rows.append({'D':D,'optimized':report(opt),'pascal':report(pascal)})
result={'status':'Exact finite identities and comparisons, not an RH certificate',
        'checks':checks,'planted_port_negative_entry':str(P[0,0]),
        'two_by_two_example':str(Q),'divisor_weight_comparison':rows}
assert all(checks.values())
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
