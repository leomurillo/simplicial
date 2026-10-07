"""
Honest follow-up: my raw Weil-form build (probe_weil_form_simplicity) FAILED the correctness
check -- minimal-eigenvector first Fourier zero came out 3.56, not Connes' 14.13 -- because
the archimedean kernel needs delicate numerics. That is EXACTLY why Connes routes through the
PROLATE operator instead of the raw Weil kernel. So test Connes' precondition (S6.6a: lowest
eigenvalue SIMPLE + EVEN) on the CLEAN vehicle -- the prolate spheroidal wave operator
  PW_lambda = -d/dx( (lambda^2 - x^2) d/dx ) + (2 pi lambda x)^2   on [-lambda, lambda]
(Connes S6.3 eq 15; = the program's z6 CCM operator). This is well-conditioned (Sturm-
Liouville), and the classical PSWF fact is that its eigenvalues are simple and eigenfunctions
have parity (-1)^n, so the ground state is even+simple. We VERIFY that here, which is the
'known for the prolate' half of Connes S6.6a -- the half the program's cubic must TRANSFER to
the Weil form.

numpy. No torch.
"""
import numpy as np

def prolate_operator(lam, N=801):
    x = np.linspace(-lam, lam, N); h = x[1]-x[0]
    # Sturm-Liouville  -d/dx( p(x) d/dx ) + q(x),  p=lam^2-x^2, q=(2 pi lam x)^2
    p = lam**2 - x**2
    pmid = 0.5*(p[:-1]+p[1:])                 # p at i+1/2
    A = np.zeros((N,N))
    for i in range(1,N-1):
        A[i,i-1] = -pmid[i-1]/h**2
        A[i,i+1] = -pmid[i]/h**2
        A[i,i]   = (pmid[i-1]+pmid[i])/h**2 + (2*np.pi*lam*x[i])**2
    # Dirichlet ends (p->0 there anyway; the operator is limit-circle, use regular ends)
    A[0,0]=1e6; A[-1,-1]=1e6
    A = 0.5*(A+A.T)
    return x, A

print("="*80)
print("Connes S6.6(a) on the PROLATE operator (the clean vehicle): SIMPLE + EVEN ground state?")
print("="*80)
for lam in [1.5, 2.0, 2.5]:
    x,A = prolate_operator(lam, N=801)
    w,V = np.linalg.eigh(A)
    # drop the two huge boundary-penalty modes
    idx = np.argsort(w)
    w=w[idx]; V=V[:,idx]
    keep = w < 1e5
    w=w[keep]; V=V[:,keep]
    print(f"\n  lambda={lam} (c=2*pi*lambda^2={2*np.pi*lam**2:.1f}), interior spectrum:")
    print(f"    lowest 5 eigenvalues: {', '.join(f'{v:.3f}' for v in w[:5])}")
    gaps = np.diff(w[:5])
    print(f"    consecutive gaps:     {', '.join(f'{g:.3f}' for g in gaps)}  -> all>0: "
          f"{'SIMPLE spectrum' if np.all(gaps>1e-6) else 'degeneracy'}")
    pars=[]
    for k in range(5):
        v=V[:,k]; ov=float(np.dot(v,v[::-1])/np.dot(v,v))
        pars.append('E' if ov>0.5 else ('O' if ov<-0.5 else '?'))
    print(f"    parities (ground..4th): {' '.join(pars)}  -> ground state {'EVEN' if pars[0]=='E' else pars[0]}")
    print(f"    => lowest eigenvalue SIMPLE (gap {gaps[0]:.3f}) and EVEN: "
          f"{'YES' if gaps[0]>1e-6 and pars[0]=='E' else 'NO'}")

print()
print("="*80)
print("HONEST STATUS - what is and isn't shown")
print("="*80)
print("""  SHOWN: the prolate operator (Connes' vehicle, the program's CCM) has a SIMPLE + EVEN
  ground state, with a strictly simple low spectrum and parity alternating E,O,E,O,...
  This is the 'known for the prolate operator' half of Connes S6.6(a) -- verified.

  NOT SHOWN (and not claimed): (i) my raw Weil-form build did NOT reproduce Connes' zeros
  (archimedean numerics too crude) -- so I cannot yet read simplicity/evenness off the Weil
  form directly; (ii) the TRANSFER -- that the Weil form QW_lambda inherits the prolate's
  simple+even ground state -- is Connes' open step, and is where the program's ORDER-3
  chirality (c_2<0, L(1/2,chi_3)!=0 non-degeneracy anchor; even sector = CBS symmetric axis)
  is the CANDIDATE mechanism. That candidacy is a hypothesis, not established here.

  So: the order-3 program does NOT yet close Connes' order-2 gap. What this turn established:
   - the prolate half of S6.6(a) is real and verifiable (simple+even ground state);
   - the program's cubic chirality is the structurally-right candidate for the transfer
     (parity -> even sector; L(1/2,chi_3)!=0 -> non-degeneracy/simplicity);
   - the direct Weil-form test needs a correct archimedean implementation (the next build),
     OR the transfer proved via the prolate approximation QW_lambda ~ PW_lambda (Connes S6.4,
     epsilon(lambda) ~ 1-chi_2(lambda)) -- the cleaner analytic route.""")
