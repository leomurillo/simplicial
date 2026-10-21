"""Independent rational small-level checks for conductor_decomposition.py.

Reuses the earlier exact Syracuse recurrence (syracuse_tao_bridge_exact.lift),
not the floating-point recurrence, and checks saved output consistency.
Run after conductor_decomposition.py. Writes verification.json only.
"""
import json
import hashlib
from fractions import Fraction as F
from pathlib import Path

import numpy as np

from syracuse_tao_bridge_exact import lift
from conductor_decomposition import powers_two, syracuse_next


def main():
    here = Path(__file__).resolve().parent
    results = json.loads((here/'conductor_results/results.json').read_text())
    reports = []
    previous = [F(1)]
    previous_float = np.array([1.])
    for k in range(1,7):
        exact = lift(previous,F(1,2))
        floating = syracuse_next(previous_float,powers_two(k))
        assert max(abs(float(a)-b) for a,b in zip(exact,floating)) < 2e-15
        if k >= 2:
            size = 3**(k-1)
            u = 2*size
            triples = [[u*exact[j+t*size] for t in range(3)]
                       for j in range(size) if j%3]
            hs = [[x-sum(row)/3 for x in row] for row in triples]
            loss = sum(-min(row) for row in hs)/len(hs)
            l1 = sum(sum(abs(x) for x in row) for row in hs)/(3*len(hs))
            energy = sum(sum(x*x for x in row) for row in hs)/(3*len(hs))
            assert F(3,4)*l1 <= loss <= F(3,2)*l1
            assert loss*loss <= 2*energy
            assert all(sum(row)==0 for row in hs)
            saved = next(d['metrics'] for d in results['details']
                         if d['metrics']['family']=='syracuse' and d['metrics']['k']==k)
            for key,val in [('lift_loss',loss),('l1',l1),('top_energy',energy)]:
                assert abs(saved[key]-float(val)) < 2e-13
            reports.append(dict(k=k,lift_loss=str(loss),l1=str(l1),top_energy=str(energy),pass_exact=True))
        previous,previous_float = exact,floating
    # Validate input identity and numerical output across all recorded rows.
    for name,digest in results['source_sha256'].items():
        assert hashlib.sha256((here/name).read_bytes()).hexdigest()==digest
    assert hashlib.sha256((here/'conductor_decomposition.py').read_bytes()).hexdigest()==results['script_sha256']
    for d in results['details']:
        r=d['metrics']
        assert r['parseval_relative_error'] < 2e-10
        assert .75*r['l1'] <= r['lift_loss']+1e-12
        assert r['lift_loss'] <= 1.5*r['l1']+1e-12
        assert abs(sum(b['energy'] for b in d['conductor_blocks'])-r['full_energy']) < 1e-9
        assert d['conductor_blocks'][-1]['modes']==4*3**(r['k']-2)
    payload=dict(all_checks_passed=True,exact_levels=reports,output_vectors_checked=len(results['details']),
                 scope='Exact rational norms/bounds for Syracuse k=2..6; float Fourier checks and source hashes for all rows. No asymptotic proof.')
    (here/'conductor_results/verification.json').write_text(json.dumps(payload,indent=2),encoding='utf-8')
    print(f'PASS: exact k=2..6; {len(results["details"])} output vectors; all input hashes unchanged.')


if __name__=='__main__':
    main()
