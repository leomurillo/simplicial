"""Audit the scoped blanket/posterior obstruction; no manuscript edits."""
import json
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import numpy as np
from scipy.integrate import quad, solve_ivp
from scipy.linalg import expm
from model import stiffness, budget_stiffness, observer, port_visibility, CANDIDATES


def audit(K, t, omega=0., mobility=1., temperature=1.):
    a, h, d = K[1, 1], K[1, 2], K[2, 2]
    L = np.array([[-3., -4., 0.], [-4., -a, -(h+omega)],
                  [0., -mobility*(h-omega), -mobility*d]])
    P0 = temperature*np.linalg.inv(K)
    J = np.array([[-4/3, 0.], [1., 0.], [0., 1.]])
    V0 = J@P0[1:, 1:]@J.T
    E = expm(L*t)
    private = 2*temperature*mobility*quad(
        lambda s: expm(L*s)[2, 2]**2, 0., t, epsabs=1e-11)[0]
    ancillary = float((E@V0@E.T)[2, 2]+private)
    D = np.diag([0., 0., 2*temperature*mobility])
    sol = solve_ivp(lambda _, v: (L@v.reshape(3, 3)+v.reshape(3, 3)@L.T+D).ravel(),
                    (0., t), V0.ravel(), rtol=2e-11, atol=2e-12)
    assert sol.success
    ode_error = abs(sol.y[8, -1]-ancillary)
    result = observer(K, t, omega, mobility, temperature=temperature)
    variance = result['covariance'][2, 2]
    pi, pr = result['visibility'], port_visibility(t)
    eta = ancillary/variance
    bound = pr*(1-eta)
    return dict(time=t, omega=omega, memory_visibility=pi, record_visibility=pr,
                ancillary_fraction=eta, private_variance=private,
                visibility_upper_bound=bound, mse_deficit=pr-pi,
                mse_deficit_lower_bound=pr*eta,
                log_loss_deficit=.5*np.log((1-pi)/(1-pr)),
                log_loss_lower_bound=.5*np.log((1-bound)/(1-pr)),
                ode_error=ode_error)


def main():
    root = Path(__file__).parent
    out = root/'compatibility_runs'/datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S_%fZ')
    out.mkdir(parents=True)
    report = {'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'model_sha256': hashlib.sha256((root/'model.py').read_bytes()).hexdigest(),
              'scope': 'Constant controls; equilibrium reference; current scalar memory',
              'tolerances': {'inequality': 2e-9, 'ode_absolute': 2e-7,
                             'precision_derivative': 2e-4}, 'witnesses': {}}
    try:
        for name in ['baseline_peak', 'passive_peak', 'active_peak_E1', 'active_peak_E10']:
            s = CANDIDATES[name]
            report['witnesses'][name] = audit(stiffness(s['d'], s['h']), s['t'], s.get('omega', 0.))
        rng = np.random.default_rng(7419)
        worst_ode, worst_violation, worst_slope = 0., 0., 0.
        for _ in range(100):
            K = budget_stiffness(rng.uniform(.15, 2.), rng.uniform(.05, .95))
            t, w, mu, T = rng.uniform(.05, 3.), rng.uniform(-4., 4.), rng.uniform(.01, 1.), rng.uniform(.2, 3.)
            r = audit(K, t, w, mu, T)
            worst_ode = max(worst_ode, r['ode_error'])
            worst_violation = max(worst_violation, r['memory_visibility']-r['visibility_upper_bound'])
            assert r['private_variance'] > 0
            assert -2e-9 <= r['ancillary_fraction'] <= 1+2e-9
            eps = 1e-7
            slope = observer(K, eps, w, mu, temperature=T)['precision_ei']/eps
            worst_slope = max(worst_slope, abs(slope-4*w/T))
        assert worst_ode < 2e-7
        assert worst_violation < 2e-9
        assert worst_slope < 2e-4
        report.update(status='PASS', random_cases=100, max_ode_error=worst_ode,
                      max_inequality_violation=worst_violation, max_slope_error=worst_slope)
    except Exception as exc:
        report.update(status='FAIL', error=repr(exc))
        raise
    finally:
        (out/'results.json').write_text(json.dumps(report, indent=2), encoding='utf-8')
        print(out)
        print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
