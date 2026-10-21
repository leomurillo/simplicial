"""Reusable exact RC/filter record model extracted unchanged from experiment_stress.py.
No runs or output writes on import.
"""
from pathlib import Path
import os, sys, json, csv
import numpy as np
from scipy.linalg import expm, solve_continuous_lyapunov, toeplitz, eigh
from scipy.stats import chi2

NQ=13; DT=.05; STEPS=400; DIM=NQ+1
Kbase=np.diag(np.full(NQ,2.2))+np.diag(-np.ones(NQ-1),1)+np.diag(-np.ones(NQ-1),-1)
BASEVAR=np.linalg.inv(Kbase)[0,0]; NV=.01*BASEVAR
OMEGA0=2*np.pi*100*.01
NPAR=3*NQ+1+5
# Packed log multipliers: 13 R, 13 Cp, 14 Cc, fc, gain, T, input PSD, output var.
names=([f'R{i}' for i in range(NQ)]+[f'Cp{i}' for i in range(NQ)]+
       [f'Cc{i}' for i in range(NQ+1)]+['fc','gain','T','input_noise_PSD','output_noise_var'])
def sym(A): return (A+A.T)/2

def state(logp=None,fc=100.,noise_sd_factor=1.,dt=DT):
    p=np.exp(np.zeros(NPAR) if logp is None else logp)
    R=p[:NQ]; Cp=5*p[NQ:2*NQ]; Cc=p[2*NQ:3*NQ+1]
    fcm,gain,T,front,post=p[-5:]
    K=np.diag(1/Cp+1/Cc[:-1]+1/Cc[1:])
    K+=np.diag(-1/Cc[1:-1],1)+np.diag(-1/Cc[1:-1],-1)
    A=np.zeros((DIM,DIM)); A[:NQ,:NQ]=-K/R[:,None]
    omega=2*np.pi*fc*fcm*.01
    A[-1,0]=omega; A[-1,-1]=-omega
    # White detector input PSD fixed as bandwidth changes; 80/20 split at 100 Hz.
    D1=np.zeros((DIM,DIM)); D1[np.arange(NQ),np.arange(NQ)]=2*T/R
    D1[-1,-1]=omega**2*(2*.8*NV/OMEGA0)*front*noise_sd_factor**2
    D0=D1.copy(); D0[np.arange(1,NQ),np.arange(1,NQ)]=0.
    F=expm(A*dt)
    S1=sym(solve_continuous_lyapunov(A,-D1))
    S0=sym(solve_continuous_lyapunov(A,-D0))
    Q1=sym(S1-F@S1@F.T); Q0=sym(S0-F@S0@F.T)
    Pinit=np.zeros((DIM,DIM)); Pinit[:NQ,:NQ]=T*np.linalg.inv(K)
    H=np.zeros(DIM); H[-1]=gain*5/Cp[0]
    rv=.2*NV*post*noise_sd_factor**2
    return dict(F=F,P=Pinit,H=H,Q0=Q0,Q1=Q1,S0=S0,S1=S1,rv=rv,K=K,A=A,D1=D1,T=T)

def records(s,steps=STEPS):
    F,H=s['F'],s['H']; O=np.empty((steps+1,DIM)); O[0]=H
    for j in range(steps): O[j+1]=O[j]@F
    out=[]
    for j in [0,1]:
        S=s[f'S{j}']; lag=O@S@H
        V=toeplitz(lag)+O@(s['P']-S)@O.T+s['rv']*np.eye(steps+1)
        out.append(sym(V))
    return out[0],out[1],O

def projected(s,w):
    # Independent backward accumulation of initial and exact step noises.
    ell=s['H']*w[-1]; v=np.array([s['rv']*(w@w)]*2)
    for j in range(len(w)-1,0,-1):
        v+=np.array([ell@s['Q0']@ell,ell@s['Q1']@ell])
        ell=s['H']*w[j-1]+s['F'].T@ell
    v+=ell@s['P']@ell
    return v
