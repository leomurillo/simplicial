"""Repeat bounded numerical searches; results are candidates, not certificates.

Example: python empirical/gaussian_observer/optimize.py --case all --seeds 7 23
Every run preserves settings, raw optimizer status, feasibility, and source hashes.
"""
import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import scipy
from scipy.optimize import differential_evolution, minimize

from model import GAP, MAX_D, budget_stiffness, observer


ROOT=Path(__file__).resolve().parent
CASES=["passive_peak","constant_deadline","passive_gated",
       "active_peak_E1","active_peak_E10","active_gated_E1","active_gated_E10"]


def setup(case):
    bounds=[(GAP+1e-6,MAX_D-1e-6),(0.,1.)]
    active=case.startswith("active")
    gated="gated" in case
    budget=float(case.rsplit("E",1)[1]) if active else 0.
    if active: bounds += [(-4.,4.),(1e-5,3.)]
    elif case=="passive_peak": bounds += [(1e-5,10.)]
    elif case=="constant_deadline": bounds += [(-2.,0.)]
    else: bounds += [(1e-5,3.),(-2.,0.)]
    def evaluate(x):
        K=budget_stiffness(x[0],x[1])
        if active:
            kwargs=dict(omega=x[2],t=x[3])
            if gated: kwargs.update(gate_deadline=10.,gate_mobility=.01)
        elif case=="passive_peak": kwargs=dict(t=x[2])
        elif case=="constant_deadline": kwargs=dict(t=10.,mobility=10**x[2])
        else: kwargs=dict(t=x[2],gate_deadline=10.,gate_mobility=10**x[3])
        return observer(K,**kwargs),K,kwargs
    return bounds,budget,evaluate


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case",choices=CASES+["all"],default="all")
    parser.add_argument("--seeds",type=int,nargs="+",default=[7,23])
    parser.add_argument("--maxiter",type=int,default=250)
    parser.add_argument("--popsize",type=int,default=12)
    args=parser.parse_args()
    stamp=datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S_%fZ")
    run=ROOT/"optimization_runs"/stamp; run.mkdir(parents=True,exist_ok=False)
    report=dict(settings=vars(args),python=sys.version,numpy=np.__version__,scipy=scipy.__version__,
                source_sha256={p.name:hashlib.sha256(p.read_bytes()).hexdigest()
                               for p in ROOT.glob("*.py")},
                qualification="Heuristic global search plus local polish; no global certificate",cases={})
    with (run/"run.log").open("x",encoding="utf-8") as log:
        for case in CASES if args.case=="all" else [args.case]:
            bounds,budget,evaluate=setup(case); rows=[]
            for seed in args.seeds:
                def objective(x):
                    r,_,_=evaluate(x)
                    return -r["visibility"]+max(0.,r["work_over_T"]-budget)**2
                z=differential_evolution(objective,bounds,seed=seed,tol=1e-8,
                    maxiter=args.maxiter,popsize=args.popsize,polish=False)
                constraints=[]
                if budget>0:
                    constraints=[dict(type="ineq",fun=lambda x:budget-evaluate(x)[0]["work_over_T"])]
                polished=minimize(lambda x:-evaluate(x)[0]["visibility"],z.x,
                    bounds=bounds,constraints=constraints,method="SLSQP",
                    options=dict(ftol=1e-12,maxiter=200))
                r,K,kwargs=evaluate(polished.x)
                row=dict(seed=seed,parameters=polished.x.tolist(),K=K.tolist(),protocol=kwargs,
                         visibility=r["visibility"],work_over_T=r["work_over_T"],
                         budget=budget,feasible=bool(r["work_over_T"]<=budget+1e-7),
                         de_success=bool(z.success),de_message=str(z.message),
                         polish_success=bool(polished.success),polish_message=str(polished.message))
                rows.append(row)
                line=f"{case} seed={seed}: visibility={row['visibility']:.12g}, W/T={row['work_over_T']:.12g}, feasible={row['feasible']}"
                print(line,flush=True); log.write(line+"\n"); log.flush()
                report["cases"][case]=rows
                (run/"results.json").write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
        print(f"Saved {run}")
    return 0 if all(r["feasible"] for rows in report["cases"].values() for r in rows) else 1


if __name__=="__main__":
    raise SystemExit(main())
