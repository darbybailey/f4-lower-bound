"""Independent small-instance and corruption controls, standard library only."""
from pathlib import Path
from collections import deque
import random,json,subprocess,tempfile,argparse,sys
from compile_dfa import compile_grammar,minimize,member,write_text

class SmallGrammar:
 def __init__(self,b,D,T,E,R):
  self.g={'base':b};self.D=set(D);self.T=T;self.m=len(T);self.start=0;self.E=list(map(set,E));self.R=list(map(set,R))
 def contains(self,n,state=None):
  if n<1:return False
  s=self.start if state is None else state;b=self.g['base']
  while n>1:
   if n in self.E[s]:return True
   if n in self.R[s]:return False
   q,d=divmod(n-1,b)
   if d not in self.D:return False
   s=self.T[s][d];n=q+1
  return True

def python_oracle(d,cap=1000000):
 b=d['base'];s=d['start'];T=d['next'];dead=d['dead'];acc=d['accept'];v=((s,s,s,s),0,0,0,False);seen={v};q=deque([v])
 while q:
  state,c1,c2,c3,nz=q.popleft()
  for a in range(b):
   for step in range(b):
    raw=(a,a+step+c1,a+2*step+c2,a+3*step+c3);ns=tuple(T[state[j]][raw[j]%b] for j in range(4))
    if dead in ns:continue
    nxt=(ns,raw[1]//b,raw[2]//b,raw[3]//b,nz or step>0)
    if nxt in seen:continue
    seen.add(nxt)
    if nxt[-1] and nxt[1:4]==(0,0,0) and all(acc[t] for t in ns):return False
    if len(seen)>cap:raise ValueError('Independent control cap reached')
    q.append(nxt)
 return True

def finite_dfa(b,values):
 T=[[-1]*b];acc=[0]
 for x in values:
  s=0
  while x:
   x,z=divmod(x,b)
   if T[s][z]<0:T[s][z]=len(T);T.append([-1]*b);acc.append(0)
   s=T[s][z]
  acc[s]=1
 # Accepted numbers permit arbitrary high zeros. Fixtures have equal lengths.
 for s,y in enumerate(acc):
  if y:T[s][0]=s
 dead=len(T);T.append([dead]*b);acc.append(0)
 for row in T:
  for z in range(b):
   if row[z]<0:row[z]=dead
 return {'base':b,'next':T,'accept':acc,'start':0,'dead':dead,'starts':[0]}

def run(oracle):
 rng=random.Random(91360);results=[];comparisons=0
 with tempfile.TemporaryDirectory(prefix='f4_tests_') as tmp:
  tmp=Path(tmp)
  def native(d,label):
   write_text(d,tmp/'dfa.txt');subprocess.run([str(oracle),str(tmp/'dfa.txt'),str(tmp/'out.json'),'30','1000000'],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL);r=json.loads((tmp/'out.json').read_text())
   if r['status']=='INCOMPLETE':raise ValueError('Control incomplete '+label)
   if r['status']=='COUNTEREXAMPLE':
    ap=list(map(int,r['progression']))
    if not(ap[1]-ap[0]==ap[2]-ap[1]==ap[3]-ap[2]>0 and all(member(d,n) for n in ap)):raise ValueError('Bad reconstructed AP')
   py=python_oracle(d)
   if py!=(r['status']=='PROVED_FREE'):raise ValueError('Independent carry disagreement '+label)
   results.append({'case':label,'status':r['status'],'dfa_states':len(d['next'])});return r
  for k in range(48):
   b=3+k%3;S=1+k%2;D={0}|set(rng.sample(list(range(1,b)),rng.randrange(1,min(3,b))));T=[[rng.randrange(S) for _ in range(b)] for s in range(S)]
   E=[];R=[]
   for s in range(S):
    E.append(rng.sample([n for n in range(2,31) if (n-1)%b not in D],min(3,len([n for n in range(2,31) if (n-1)%b not in D]))))
    R.append(rng.sample([n for n in range(2,31) if (n-1)%b in D],3))
   g=SmallGrammar(b,D,T,E,R);d,_=compile_grammar(g);d,_=minimize(d)
   for s in range(S):
    for n in range(1,1001):
     comparisons+=1
     if g.contains(n,s)!=member(d,n,d['starts'][s]):raise ValueError(('Compiler mismatch',k,s,n))
   native(d,f'random_root_grammar_{k}')
  for L in [1,5,30]:
   d=finite_dfa(55,[55**L+j for j in range(4)]);r=native(d,f'large_integer_AP_digits_{L+1}')
   if r['status']!='COUNTEREXAMPLE':raise ValueError('Missed finite progression')
  d=finite_dfa(55,[55**5+j for j in [0,1,2,4]]);r=native(d,'finite_four_free_set')
  if r['status']!='PROVED_FREE':raise ValueError('Wrong finite rejection')
  # A transition to a non-zero-padding-consistent acceptance state is invalid.
  bad={'base':3,'next':[[1,1,1],[1,1,1]],'accept':[1,0],'start':0,'dead':1,'starts':[0]};write_text(bad,tmp/'bad.txt')
  p=subprocess.run([str(oracle),str(tmp/'bad.txt'),str(tmp/'bad.json')],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
  if p.returncode==0:raise ValueError('Zero-padding corruption accepted')
 return {'status':'PASS','independent_carry_cases':len(results),'compiler_membership_comparisons':comparisons,'zero_padding_corruption_rejected':True,'cases':results}
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('--oracle',required=True);a.add_argument('--output',required=True);x=a.parse_args();r=run(Path(x.oracle));Path(x.output).write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({k:v for k,v in r.items() if k!='cases'}))
