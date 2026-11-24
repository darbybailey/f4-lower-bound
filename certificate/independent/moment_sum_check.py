"""Independent floating-point check of the reciprocal sum of the DFA language (different decomposition from verify/root_automaton.py).
Top two base-55 digits form the prefix u; low words are summed by state-conditioned moments up to order 22.  Result agrees with
witness/weight_certificate.json to double precision.  Requires numpy.  This is a cross-check, not the rigorous enclosure."""
import json, numpy as np, sys
from math import comb
from pathlib import Path
d=json.load(open(Path(__file__).resolve().parent.parent/'witness/candidate_dfa.json')); nxt=np.array(d['next'],dtype=np.int64); acc=np.array(d['accept'],dtype=bool); start=d['start']; dead=d['dead']; b=55
live=[s for s in range(len(nxt)) if s!=dead]; idx={s:i for i,s in enumerate(live)}; N=len(live); I=22
def state_lsb(x):
    s=start
    while x: s=nxt[s][x%b]; x//=b
    return s
head=sum(1.0/(x+1) for x in range(b*b) if acc[state_lsb(x)])
A=np.zeros((I+2,N)); T=np.zeros((I+2,N,N)); B=np.zeros((I+2,N)); M=np.zeros((I+2,N))
for s in live:
    for u in range(b,b*b):
        if acc[nxt[nxt[s][u%b]][u//b]]:
            for i in range(I+2): A[i,idx[s]]+=u**(-(i+1.0))
for sp in live:
    for dd in range(b):
        s=nxt[sp][dd]
        if s!=dead:
            for j in range(I+2): T[j,idx[s],idx[sp]]+=dd**j
for dd in range(b):
    s=nxt[start][dd]
    if s!=dead:
        for i in range(I+2): B[i,idx[s]]+=(1.0/b)*((dd+1.0)/b)**i
for i in range(I+2):
    rhs=B[i].copy()
    for h in range(i): rhs+=b**(-(i+1.0))*comb(i,h)*(T[i-h]@M[h])
    M[i]=np.linalg.solve(np.eye(N)-b**(-(i+1.0))*T[0],rhs)
W=head+sum((-1)**i*float(A[i]@M[i]) for i in range(I+1))
cert=json.load(open(Path(__file__).resolve().parent.parent/'witness/weight_certificate.json'))
print(f"independent value {W:.16f}; certificate lower {cert['lower_decimal'][:20]} upper {cert['upper_decimal'][:20]}")
sys.exit(0 if abs(W-float(cert['lower_decimal'][:40]))<1e-13 else 1)
