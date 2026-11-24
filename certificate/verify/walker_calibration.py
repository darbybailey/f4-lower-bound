"""Exact constant-Walker calibration. No search, proposals or quasiperiodic schedules.

Partition n-1 into <2 digits (the finite head), or a low word of length ell
and a nonzero-leading 3-digit block u. Its reciprocal is 55**(-ell)/(u+t),
where 0<t<=1. Odd/even alternating sums bound this fraction. Finite-depth
moments are exact, leading-block inverse powers are rounded outwards, and
all remaining low-word lengths are covered by an explicit geometric tail.
This specializes the verified block decomposition of S24 to the one fixed
alphabet D. See PROOF.md for the recurrence and the tail inequality.
"""
from fractions import Fraction as F
from math import comb
from functools import lru_cache
from root_automaton import D,require,decimal

@lru_cache(maxsize=4)
def enclose(H=80,K=10,scale=10**100):
    require(type(H) is int and H>0,'Invalid depth')
    require(type(K) is int and K>=2 and K%2==0,'Even Taylor order required')
    require(type(scale) is int and scale>0,'Invalid integer scale')
    b=55;m=len(D)
    require(0 in D and 0<m<b,'Invalid alphabet')
    # The head contains every admissible n-1 with fewer than two digits.
    head=[1+d+b*a for a in D for d in D]
    hs=sum(scale//n for n in head)
    lo=F(hs,scale);hi=F(hs+len(head),scale)
    leads=[a+b*c+b*b*d for d in D if d for c in D for a in D]
    N=len(leads);powers=[sum(scale//u**(k+1) for u in leads) for k in range(K+1)]
    raw=[sum(d**k for d in D) for k in range(K+1)]
    M=[F(1)]*(K+1) # t_empty=1, weight 1.
    for ell in range(H):
        require(M[0]==F(m,b)**ell,'Low-word count mismatch')
        require(all(0<=x<=M[0] for x in M),'Invalid t moments')
        for k in range(K+1):
            lower=F(powers[k],scale);upper=F(powers[k]+N,scale)
            if k<K:lo+=M[k]*(lower if k%2==0 else -upper)
            hi+=M[k]*(upper if k%2==0 else -lower)
        M=[F(1,b**(k+1))*sum((comb(k,j)*raw[k-j]*M[j] for j in range(k+1)),F()) for k in range(K+1)]
    tail=F(N,b*b)*F(m,b)**H/(1-F(m,b));hi+=tail
    require(lo<hi,'Inverted Walker enclosure')
    return lo,hi,{'H':H,'K':K,'scale':str(scale),'head_terms':len(head),
        'leading_blocks':N,'remaining_tail_upper':str(tail),
        'lower':str(lo),'upper':str(hi),'lower_decimal':decimal(lo),'upper_decimal':decimal(hi),
        'recomputed_from_digits':True}
