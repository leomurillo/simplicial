"""Exact formal intersection-block checks; no arithmetic Hodge-index proof."""
import json
from pathlib import Path
import sympy as s

m11,m12,m22=s.symbols('m11 m12 m22',real=True)
b11,b12,b21,b22=s.symbols('b11 b12 b21 b22',real=True)
M=s.Matrix([[m11,m12],[m12,m22]])
B=s.Matrix([[b11,b12],[b21,b22]])
J=s.Matrix([[0,1],[1,0]])
A=B*J*B.T-M
I=A.row_join(B).col_join(B.T.row_join(J))
T=s.eye(2).row_join(s.zeros(2)).col_join((-J*B.T).row_join(s.eye(2)))
expected=(-M).row_join(s.zeros(2)).col_join(s.zeros(2).row_join(J))
checks={'block_congruence':s.simplify(T.T*I*T-expected)==s.zeros(4),
        'basis_change_determinant_one':T.det()==1}

# A two-graph, genus-one-shaped formal control. All entries are nonnegative.
bad=s.Matrix([[0,11,1,1],[11,0,1,4],[1,1,0,1],[1,4,1,0]])
Bb=bad[:2,2:]
primitive=bad[:2,:2]-Bb*J*Bb.T
checks['control_primitive_indefinite']=primitive.det()<0
checks['control_all_entries_nonnegative']=all(v>=0 for v in bad)

# Independently check the finite-field packet used in the peer certificate.
p=101
points=1+sum(1 if (v:=(x*x*x+x+1)%p)==0 else 2 if pow(v,(p-1)//2,p)==1 else 0 for x in range(p))
checks['elliptic_point_count_105']=points==105
out={'status':'Exact linear algebra and finite point count, not an RH proof',
     'checks':{k:bool(v) for k,v in checks.items()},
     'control_primitive_matrix':str(primitive),
     'control_primitive_determinant':str(primitive.det()),
     'control_full_inertia':'(2 positive, 2 negative), by the congruence',
     'elliptic_point_count':points}
assert all(checks.values())
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
