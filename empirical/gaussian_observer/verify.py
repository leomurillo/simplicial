"""Author audit; thresholds fixed before first execution of this package.

Not experimental data, an independent peer review, or an optimizer certificate.
Each invocation creates a unique run directory, preserving failures and hashes.

C01 thermal conditional residual and baseline: absolute tolerance 2e-10.
C02 eight archived candidate values and component/work budgets: 3e-9.
C03 covariance/mean/work ODE, including a second gated phase: 3e-8.
C04 direct Van Loan Gaussian channel, posterior and shifted KL: 3e-9.
C05 sample reversible spectral bounds (seed 204): 2e-12; not a proof.
C06 piecewise exact frontier versus independent scalar/2D search: 3e-8.
C07 piecewise drive versus constant-drive certificate: 2e-12.
C08 port ceiling, temperature scaling, positive entropy production: 3e-9.
C09 active blanket diagnostic: passive |partial correlation| <2e-12;
    active witness |partial correlation| >1e-4 (does NOT preserve blanket).
C10 inference-error/log-loss decompositions with exact covariance: 2e-12.
"""
from __future__ import annotations

import hashlib
import json
import platform
import sys
import traceback
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import scipy
from scipy.integrate import solve_ivp
from scipy.linalg import expm, solve_continuous_lyapunov
from scipy.optimize import differential_evolution, minimize_scalar

from model import (CANDIDATES, circulation, evaluate_candidate, frontier,
                   frontier_objective, observer, port_visibility, stiffness)


ROOT = Path(__file__).resolve().parent


def plain(value):
    if isinstance(value, np.ndarray): return value.tolist()
    if isinstance(value, np.generic): return value.item()
    raise TypeError(type(value).__name__)


def near(a, b, tol):
    error = float(np.max(np.abs(np.asarray(a)-np.asarray(b))))
    if error > tol: raise AssertionError(f"error {error:.6g} > {tol:.6g}")
    return error


def c01():
    K=stiffness(1,1); P=np.linalg.inv(K); v=np.array([1.,4/3,0.])
    near(v@P@v, 1/3, 2e-10)
    near(v@P[:,1:], [0,0], 2e-10)
    near(np.linalg.eigvalsh(K), [.16356525412920805,1.279432079707215,9.557002666163578],2e-10)
    result=evaluate_candidate(CANDIDATES["baseline_peak"])
    near(result["visibility"],.0077872529305161,2e-10)
    assert observer(K,100)["visibility"] < 1e-12
    return dict(baseline_peak=result["visibility"],initial_target_variance=v@P@v)


def c02():
    rows={}
    for name,spec in CANDIDATES.items():
        K=stiffness(spec["d"],spec["h"]); result=evaluate_candidate(spec)
        near(result["visibility"],spec["expected"],3e-9)
        assert np.linalg.eigvalsh(K)[0] >= .1-3e-9
        assert result["work_over_T"] <= spec.get("budget",0)+3e-9
        rows[name]={k:v for k,v in result.items() if not isinstance(v,np.ndarray)}
    return rows


def c03():
    rows={}
    for name,spec in CANDIDATES.items():
        K=stiffness(spec["d"],spec["h"]); P0=np.linalg.inv(K)
        M=np.diag([1.,1.,spec.get("mobility",1.)]); N=circulation(spec.get("omega",0.))
        A=M@(K+N)
        def rhs(t,y):
            P=y[:9].reshape(3,3); m=y[9:12]
            return np.r_[(-A@P-P@A.T+2*M).ravel(),-A@m,
                         np.trace(N.T@A@P)-np.trace(M@N)]
        sol=solve_ivp(rhs,[0,spec["t"]],np.r_[P0.ravel(),[1.,0.,0.],0.],
                      rtol=2e-11,atol=2e-13)
        assert sol.success
        z=sol.y[:,-1]; P=z[:9].reshape(3,3); m=z[9:12]
        if "gate_deadline" in spec:
            Mh=np.diag([1.,1.,.01]); Ah=Mh@K
            def hold(t,y):
                Ph=y[:9].reshape(3,3)
                return np.r_[(-Ah@Ph-Ph@Ah.T+2*Mh).ravel(),-Ah@y[9:12]]
            holdsol=solve_ivp(hold,[spec["t"],spec["gate_deadline"]],
                              np.r_[P.ravel(),m],rtol=2e-11,atol=2e-13)
            assert holdsol.success
            P=holdsol.y[:9,-1].reshape(3,3); m=holdsol.y[9:12,-1]
        exact=evaluate_candidate(spec)
        err=near(P,exact["covariance"],3e-8)
        near(m,exact["propagator"][:,0],3e-8)
        near(z[-1],exact["work_over_T"],3e-8)
        near(m[2]**2/(3*P[2,2]),exact["visibility"],3e-8)
        rows[name]=dict(covariance_error=err,work_ode=float(z[-1]))
    return rows


def c04():
    # A direct augmented matrix exponential supplies integrated bath covariance,
    # without stationary Lyapunov covariance or the information Riccati equation.
    spec=CANDIDATES["active_peak_E1"]
    K=stiffness(spec["d"],spec["h"]); A=K+circulation(spec["omega"])
    P0=np.linalg.inv(K); t=spec["t"]
    V=expm(np.block([[-A,2*np.eye(3)],[np.zeros((3,3)),A.T]])*t)
    E=V[:3,:3]; Q=V[:3,3:]@E.T
    conditional=E@(P0-np.diag([1/3,0,0]))@E.T+Q
    P=E@P0@E.T+Q
    result=evaluate_candidate(spec)
    err=near(P,result["covariance"],3e-9)
    a=E[2,0]/np.sqrt(3)
    near(a*a+conditional[2,2],P[2,2],3e-9)
    posterior_variance=1-a*a/P[2,2]
    near(posterior_variance,1-result["visibility"],3e-9)
    shift=.7
    record_KL=(a*shift)**2/(2*P[2,2])
    near(record_KL,result["visibility"]*shift**2/2,3e-9)
    return dict(covariance_error=err,posterior_variance=posterior_variance,
                shifted_record_KL=record_KL)


def c05():
    rng=np.random.default_rng(204); worst=-np.inf
    for _ in range(200):
        U,_=np.linalg.qr(rng.normal(size=(5,5))); ev=np.exp(rng.uniform(-3,3,5))
        H=(U*ev)@U.T; t=np.exp(rng.uniform(-3,2)); E=expm(-H*t)
        bound=(np.exp(-ev.min()*t)-np.exp(-ev.max()*t))**2/4
        worst=max(worst,E[0,1]**2-bound)
    assert worst <= 2e-12
    return dict(samples=200,largest_signed_excess=worst)


def c06():
    rows={}; R=4.
    for E in [.1,1.,3.,5.,10.,20.]:
        exact=frontier(E,R)
        # Split at the nonsmooth crossover; a single smooth optimizer can miss it.
        split=min(E/(2*R),np.pi/2); points=[0.,split,np.pi/2]
        candidates=[frontier_objective(x,E,R) for x in points]
        for lo,hi in zip(points[:-1],points[1:]):
            if hi>lo:
                sol=minimize_scalar(lambda x:-frontier_objective(x,E,R),
                                    bounds=(lo,hi),method="bounded",
                                    options={"xatol":1e-13})
                candidates.append(-sol.fun)
        near(exact["visibility"],max(candidates),3e-8)
        def objective(x):
            tau,r=x; work=2*r*r*tau
            return 1+work-E if work>E else -np.exp(-2*tau)*np.sin(r*tau)**2
        numerical=differential_evolution(objective,[(1e-6,3),(0,R)],
                    seed=202,tol=1e-10,popsize=20)
        near(exact["visibility"],-numerical.fun,3e-8)
        assert exact["work_over_T"] <= E+2e-12 and exact["rate"] <= R+2e-12
        rows[str(E)]=dict(**exact,independent_search=-numerical.fun)
    return rows


def c07():
    rates=np.array([1.,3.,-1.,2.]); durations=np.array([.1,.2,.15,.1])
    J=np.array([[0.,-1.],[1.,0.]])
    propagator=np.eye(2)
    for r,t in zip(rates,durations): propagator=expm(-(np.eye(2)+r*J)*t)@propagator
    theta=rates@durations; tau=durations.sum(); E=2*(rates*rates)@durations
    actual=propagator[1,0]**2
    near(actual,np.exp(-2*tau)*np.sin(theta)**2,2e-12)
    constant=np.exp(-4*theta*theta/E)*np.sin(theta)**2
    assert actual <= constant+2e-12
    assert constant <= frontier(E,4)["visibility"]+2e-12
    return dict(piecewise_visibility=actual,constant_same_angle_visibility=constant,
                work_over_T=E)


def c08():
    rows={}
    for name,spec in CANDIDATES.items():
        result=evaluate_candidate(spec)
        deadline=spec.get("gate_deadline",spec["t"])
        assert result["visibility"] <= port_visibility(deadline)+3e-9
        assert result["drive_entropy_production"] >= -3e-9
        for T in [.2,3.]:
            scaled=evaluate_candidate(spec,temperature=T)
            near(scaled["visibility"],result["visibility"],3e-9)
            near(scaled["work_over_T"],result["work_over_T"],3e-9)
        rows[name]=dict(port_visibility=port_visibility(deadline),
                        entropy_production=result["drive_entropy_production"])
    return rows


def c09():
    passive=evaluate_candidate(CANDIDATES["passive_peak"])
    active=evaluate_candidate(CANDIDATES["active_peak_E1"])
    K=stiffness(CANDIDATES["active_peak_E1"]["d"],CANDIDATES["active_peak_E1"]["h"])
    A=K+circulation(CANDIDATES["active_peak_E1"]["omega"])
    Ps=solve_continuous_lyapunov(A,2*np.eye(3)); Qs=np.linalg.inv(Ps)
    steady_partial=-Qs[0,2]/np.sqrt(Qs[0,0]*Qs[2,2])
    assert abs(passive["partial_correlation_ei_given_b"]) < 2e-12
    assert abs(active["partial_correlation_ei_given_b"]) > 1e-4
    assert abs(steady_partial) > 1e-4
    return dict(passive_partial=passive["partial_correlation_ei_given_b"],
                active_transient_partial=active["partial_correlation_ei_given_b"],
                active_stationary_partial=steady_partial,
                conclusion="Active example does not preserve the static blanket")


def c10():
    # U,R,M have unit variances, with two independent Gaussian channel noises.
    p=.25; a=.7; cov=np.array([[1,np.sqrt(p),np.sqrt(p)*a],
                              [np.sqrt(p),1,a],[np.sqrt(p)*a,a,1]])
    b=.2; pm=p*a*a
    direct=np.array([1,0,-b])@cov@np.array([1,0,-b])
    split=(1-p)+(p-pm)+(np.sqrt(pm)-b)**2
    near(direct,split,2e-12)
    Vq=.9; Vm=1-pm; Vr=1-p
    logloss=.5*(np.log(Vq/Vr)+direct/Vq-1)
    information=.5*np.log(Vm/Vr)
    forward_KL=.5*(np.log(Vq/Vm)+(Vm+(np.sqrt(pm)-b)**2)/Vq-1)
    near(logloss,information+forward_KL,2e-12)
    # Usual variational gap reverses the KL; it is not the log-loss residual.
    reverse_KL=.5*(np.log(Vm/Vq)+(Vq+(np.sqrt(pm)-b)**2)/Vm-1)
    return dict(mse=direct,logloss_excess=logloss,forward_KL=forward_KL,
                reverse_variational_KL=reverse_KL)


def main():
    stamp=datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S_%fZ")
    run=ROOT/"runs"/stamp
    run.mkdir(parents=True,exist_ok=False)
    hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(ROOT.glob("*.py"))}
    report=dict(timestamp_utc=stamp,python=sys.version,numpy=np.__version__,
                scipy=scipy.__version__,platform=platform.platform(),source_sha256=hashes,
                interpretation="Author audit; candidate validation is not global optimization",checks=[])
    tests=[c01,c02,c03,c04,c05,c06,c07,c08,c09,c10]
    with (run/"run.log").open("x",encoding="utf-8") as log:
        for test in tests:
            try:
                result=test(); row=dict(id=test.__name__,passed=True,result=result)
                line=f"PASS {test.__name__}"
            except Exception:
                row=dict(id=test.__name__,passed=False,error=traceback.format_exc())
                line=f"FAIL {test.__name__}\n{row['error']}"
            report["checks"].append(row); print(line,flush=True); log.write(line+"\n"); log.flush()
        report["passed"]=sum(r["passed"] for r in report["checks"])
        report["total"]=len(tests)
        summary=f"{report['passed']}/{report['total']} checks passed. Run: {run}"
        print(summary); log.write(summary+"\n")
    (run/"results.json").write_text(json.dumps(report,indent=2,default=plain)+"\n",encoding="utf-8")
    return 0 if report["passed"]==len(tests) else 1


if __name__=="__main__":
    raise SystemExit(main())
