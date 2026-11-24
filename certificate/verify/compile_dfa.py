"""Compile a recurrent finite-root grammar to an ordinary LSB-first DFA.
A derivative is a base control function plus finitely many exact overrides.
All transition and accepting-state tables are explicit; there is no oracle
or integer lookup at evaluation time after compilation.
"""
import json,sys,argparse,time,hashlib,random
from pathlib import Path
from functools import lru_cache

def compile_grammar(g,limit=200000):
    b=g.g['base'];D=set(g.D);S=g.m
    @lru_cache(None)
    def value(s,x):return bool(s>=0 and g.contains(x+1,s))
    def clean(s,over):
        return tuple(sorted((x,int(y)) for x,y in over.items() if bool(y)!=value(s,x)))
    deriv=[]
    for s in range(S):
        row=[]
        for d in range(b):
            t=g.T[s][d] if d in D else -1
            o={}
            for x in g.E[s]:
                if (x-1)%b==d:o[(x-1)//b]=1
            for x in g.R[s]:
                if (x-1)%b==d:o[(x-1)//b]=0
            row.append((t,dict(clean(t,o))))
        deriv.append(row)
    ids={};keys=[];trans=[];accept=[]
    def intern(key):
        if key not in ids:
            if len(keys)>=limit:raise RuntimeError('DFA compilation state limit reached; no completeness claim')
            ids[key]=len(keys);keys.append(key)
        return ids[key]
    starts=[intern((s,())) for s in range(S)];dead=intern((-1,()))
    for s,over in keys:
        ov=dict(over);accept.append(int(ov.get(0,value(s,0))));row=[]
        buckets=[{} for _ in range(b)]
        for x,y in over:buckets[x%b][x//b]=y
        for d in range(b):
            t,o=deriv[s][d] if s>=0 else (-1,{})
            no=dict(o);no.update(buckets[d])
            row.append(intern((t,clean(t,no))))
        trans.append(row)
    return {'base':b,'start':starts[g.start],'starts':starts,'dead':dead,'accept':accept,'next':trans,'compiler_states':len(keys),'scope':'Exact digit DFA for n-1 with harmless high zero padding'},keys

def minimize(d):
    T=d['next'];acc=d['accept'];classes=list(acc);rounds=0
    while True:
        new=[];mapping={}
        for i,row in enumerate(T):
            k=(acc[i],tuple(classes[j] for j in row))
            if k not in mapping:mapping[k]=len(mapping)
            new.append(mapping[k])
        rounds+=1
        if new==classes:break
        classes=new
    reps={}
    for i,c in enumerate(classes):reps.setdefault(c,i)
    result=dict(d);result['next']=[[classes[j] for j in T[reps[c]]] for c in range(len(reps))];result['accept']=[acc[reps[c]] for c in range(len(reps))]
    for k in ['start','dead']:result[k]=classes[d[k]]
    result['starts']=[classes[s] for s in d['starts']];result['minimization_rounds']=rounds;result['minimal_states']=len(reps)
    return result,classes

def single_entry(d):
    """Remove states unreachable from the actual entry; keep the dead sink."""
    seen={d['start']};todo=[d['start']]
    for s in todo:
        for t in d['next'][s]:
            if t not in seen:seen.add(t);todo.append(t)
    seen.add(d['dead']);keep=sorted(seen);ren={s:i for i,s in enumerate(keep)}
    out=dict(d);out['next']=[[ren[t] for t in d['next'][s]] for s in keep];out['accept']=[d['accept'][s] for s in keep]
    out['start']=ren[d['start']];out['dead']=ren[d['dead']];out['starts']=[out['start']]
    out['multi_entry_states_before_trim']=len(d['next']);out['minimal_states']=len(keep)
    return out

def member(d,n,state=None):
    if type(n)is not int or n<1:return False
    x=n-1;s=d['start'] if state is None else state
    while x:x,v=divmod(x,d['base']);s=d['next'][s][v]
    return bool(d['accept'][s])

def write_text(d,p):
    with Path(p).open('w') as f:
        print(d['base'],len(d['next']),d['start'],d['dead'],file=f)
        print(*d['accept'],file=f)
        for row in d['next']:print(*row,file=f)

def main():
    a=argparse.ArgumentParser();a.add_argument('--release',required=True);a.add_argument('--input',required=True);a.add_argument('--output',required=True);x=a.parse_args()
    sys.path.insert(0,str(Path(x.release)/'work'))
    from root_automaton import Grammar
    g=Grammar(json.loads(Path(x.input).read_text()));tic=time.time();d,keys=compile_grammar(g);print('compiled',len(keys),'seconds',time.time()-tic,flush=True)
    d,classes=minimize(d);print('minimal',len(d['next']),'seconds',time.time()-tic,flush=True)
    # Exhaustive transition induction on all derivatives establishes equality;
    # additional evaluation controls protect implementation and serialization.
    points=set(range(1,100001))|{n for m in g.g['modes'] for n in m['E']+m['R']}
    rng=random.Random(91354);points.update(rng.randrange(1,10**30) for _ in range(20000))
    for s in range(g.m):
        for n in points:
            if g.contains(n,s)!=member(d,n,d['starts'][s]):raise ValueError(('DFA mismatch',s,n))
    for s in range(len(d['next'])):
        if d['accept'][s]!=d['accept'][d['next'][s][0]]:raise ValueError('Bad zero padding')
    d['membership_comparison_points']=len(points)*g.m;d['seconds']=time.time()-tic
    out=Path(x.output);out.write_text(json.dumps(d,separators=(',',':'))+'\n');write_text(d,out.with_suffix('.txt'))
    print('PASS',d['membership_comparison_points'],'comparisons',flush=True)
if __name__=='__main__':main()
