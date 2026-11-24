"""Finite-state root/repair grammar. Standard library only.
Digits are read least significant first. All 3 mechanisms (root exceptions,
state memory, branch-specific repairs) are described by a single decoder.
"""
from fractions import Fraction as F
from math import comb
from functools import lru_cache
from decimal import Decimal, localcontext
import sys
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)

D=(0,1,2,4,5,9,10,11,14,16,17,18,21,24,30,37,39,41,42,45,47)

def require(test,message):
    if not test:raise ValueError(message)

def decimal(x):
    with localcontext() as c:
        c.prec=65
        return str(Decimal(x.numerator)/Decimal(x.denominator))

def walker(n):
    if type(n) is not int or n<1:return False
    while n>1:
        n,d=divmod(n-1,55);n+=1
        if d not in D:return False
    return True

class Grammar:
    def __init__(self,g,pool=None):
        require(g['base']==55 and g['digits']==list(D),'Wrong base or alphabet')
        self.g=g;self.m=len(g['modes']);self.start=g.get('start',0);self.T=g['next']
        require(type(self.start) is int and 0<=self.start<self.m,'Invalid start')
        require(len(self.T)==self.m,'Transition row count')
        for row in self.T:
            require(len(row)==55 and all(type(v) is int and 0<=v<self.m for v in row),'Invalid transition')
        self.E=[];self.R=[]
        for mode in g['modes']:
            for key in ('E','R'):
                values=mode[key]
                require(isinstance(values,list) and all(type(n) is int and n>1 for n in values),'Invalid roots')
                require(values==sorted(set(values)),'Unsorted/duplicate roots')
            es=set(mode['E']);rs=set(mode['R'])
            require(not es&rs,'Insertion/deletion overlap')
            require(all((n-1)%55 not in D for n in es),'Non-root insertion')
            require(all((n-1)%55 in D for n in rs),'Deletion must have an ordinary low digit')
            if pool is not None:require(es<=pool,'Root outside certified pool')
            self.E.append(es);self.R.append(rs)
        self.D=set(D)

    def contains(self,n,state=None):
        if type(n) is not int or n<1:return False
        s=self.start if state is None else state
        require(type(s) is int and 0<=s<self.m,'Invalid state')
        while n>1:
            if n in self.E[s]:return True
            if n in self.R[s]:return False
            q,d=divmod(n-1,55)
            if d not in self.D:return False
            s=self.T[s][d];n=q+1
        return True

    def active_deletions(self):
        return [sorted(n for n in self.R[s] if self.contains((n-1)//55+1,self.T[s][(n-1)%55])) for s in range(self.m)]

    def reachable(self):
        seen={self.start};todo=[self.start]
        for s in todo:
            for d in D:
                t=self.T[s][d]
                if t not in seen:seen.add(t);todo.append(t)
        return sorted(seen)

    def check_catalog(self,aps):
        checks=0
        for s in range(self.m):
            for a in aps:
                require(len(a)==4 and all(type(n) is int and n>0 for n in a),'Invalid AP')
                require(a[1]-a[0]==a[2]-a[1]==a[3]-a[2]>0,'Invalid AP differences')
                checks+=1
                if all(self.contains(n,s) for n in a):
                    return {'free':False,'state':s,'witness':a,'checks':checks}
        return {'free':True,'checks':checks,'states':self.m,'catalog_rows':len(aps)}


def solve(matrix,rhs):
    """Exact Gaussian elimination; rhs can have several columns."""
    n=len(matrix);r=len(rhs[0]);a=[list(matrix[i])+list(rhs[i]) for i in range(n)]
    for j in range(n):
        pivot=next((i for i in range(j,n) if a[i][j]),None)
        require(pivot is not None,'Singular moment system')
        a[j],a[pivot]=a[pivot],a[j];v=a[j][j];a[j]=[x/v for x in a[j]]
        for i in range(n):
            if i!=j:
                v=a[i][j]
                if v:a[i]=[x-v*y for x,y in zip(a[i],a[j])]
    return [row[n:] for row in a]


def moments(grammar,K):
    """M[k][start][terminal] = sum_words 55^-len * z_word**k.
    z_word = 1-(value(word)+1)/55**len and z_empty=0.
    """
    m=grammar.m;T=grammar.T
    raw=[[[sum((54-d)**k for d in D if T[u][d]==t) for k in range(K+1)] for t in range(m)] for u in range(m)]
    M=[]
    for k in range(K+1):
        f=F(1,55**(k+1))
        matrix=[[F(int(t==u))-f*raw[u][t][0] for u in range(m)] for t in range(m)]
        rhs=[[F(int(k==0 and t==s)) for s in range(m)] for t in range(m)]
        for t in range(m):
            for s in range(m):
                rhs[t][s]+=f*sum((comb(k,j)*raw[u][t][k-j]*M[j][s][u] for u in range(m) for j in range(k)),F())
        cols=solve(matrix,rhs)
        M.append([[cols[t][s] for t in range(m)] for s in range(m)])
        require(all(x>=0 for row in M[k] for x in row),'Negative moment')
        if k:require(all(M[k][s][t]<=M[0][s][t] for s in range(m) for t in range(m)),'Moment domination')
    require(all(sum(row,F())==F(55,34) for row in M[0]),'Zeroth moment mass mismatch')
    return M


def correction_interval(grammar,K=8,scale=10**80):
    """Outward rational intervals for W(A_s)-W(Walker), every state.
    Source reciprocal powers are rounded outwards with integer arithmetic.
    The Taylor remainder is bounded explicitly, never silently truncated.
    """
    require(type(K) is int and K>=0 and type(scale) is int and scale>0,'Invalid precision')
    M=moments(grammar,K+1);R=grammar.active_deletions();m=grammar.m
    low=[[F() for _ in range(K+1)] for _ in range(m)];high=[[F() for _ in range(K+1)] for _ in range(m)]
    remE=[];remR=[]
    for t in range(m):
        E=grammar.E[t]
        for k in range(K+1):
            a=sum(scale//n**(k+1) for n in E);b=sum(scale//n**(k+1) for n in R[t])
            low[t][k]=F(a-b-len(R[t]),scale);high[t][k]=F(a+len(E)-b,scale)
        remE.append(F(sum(scale//(n**(K+1)*(n-1))+1 for n in E),scale))
        remR.append(F(sum(scale//(n**(K+1)*(n-1))+1 for n in R[t]),scale))
    intervals=[]
    for s in range(m):
        lo=sum((M[k][s][t]*low[t][k] for k in range(K+1) for t in range(m)),F())
        hi=sum((M[k][s][t]*high[t][k] for k in range(K+1) for t in range(m)),F())
        lo-=sum((M[K+1][s][t]*remR[t] for t in range(m)),F())
        hi+=sum((M[K+1][s][t]*remE[t] for t in range(m)),F())
        require(lo<=hi,'Inverted weight interval');intervals.append((lo,hi))
    return intervals,{'order':K,'scale':str(scale),'active_deletions':[len(r) for r in R],
        'inactive_deletions':[len(grammar.R[s])-len(R[s]) for s in range(m)],
        'zeroth_moments':[[str(v) for v in row] for row in M[0]],
        'intervals':[{'lower':str(a),'upper':str(b),'lower_decimal':decimal(a),'upper_decimal':decimal(b),'width':str(b-a)} for a,b in intervals]}
