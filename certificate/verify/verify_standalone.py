"""Solver-free proof replay from the local fixed witnesses.
Stored intervals are comparison targets, never trusted proof premises.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json,subprocess,sys,tempfile,platform,time,random,os
from root_automaton import Grammar,correction_interval,decimal,require
from compile_dfa import compile_grammar,minimize,single_entry,member,write_text
from walker_calibration import enclose
P=Path(__file__).resolve().parent.parent
W=P/'witness'
def load(p):return json.loads(Path(p).read_text())
def canonical(d):return {k:d[k] for k in ['base','start','dead','accept','next']}
def manifest():
    m=load(P/'MANIFEST.sha256.json')['files']
    actual=set()
    for f in P.rglob('*'):
        r=f.relative_to(P)
        require(not f.is_symlink(),'Symlink not allowed: '+str(r))
        if f.is_file() and '__pycache__' not in r.parts and r.parts[0]!='runs' and f!=P/'MANIFEST.sha256.json':actual.add(r.as_posix())
    require(actual==set(m),'Manifest payload set mismatch')
    for n,h in m.items():
        require(not Path(n).is_absolute() and '..' not in Path(n).parts,'Invalid manifest path')
        require(hashlib.sha256((P/n).read_bytes()).hexdigest()==h,'Checksum mismatch: '+n)
    return len(m)
def compile_prove(g,tmp,exe,label):
    raw,_=compile_grammar(g);multi,_=minimize(raw);proofs=[]
    require(g.reachable()==list(range(g.m)),label+': unreachable control')
    require(len(set(multi['starts']))==g.m,label+': equivalent control entries')
    for control in range(g.m):
        d=single_entry(multi) if control==g.start else dict(multi,start=multi['starts'][control])
        text=tmp/(label+'_dfa.txt');out=tmp/(label+'_proof.json');write_text(d,text)
        subprocess.run([str(exe),str(text),str(out),'300','10000000'],check=True)
        r=load(out);require(r['status']=='PROVED_FREE',label+': incomplete or unsafe AP proof')
        require(r['processed_states']==r['reachable_product_states'],label+': product graph not exhausted')
        proofs.append(dict(r,control_state=control))
    return multi,single_entry(multi),proofs

def main():
    a=argparse.ArgumentParser();a.add_argument('--output',type=Path);x=a.parse_args();tic=time.time()
    if x.output:
        x.output=x.output.resolve()
        try:r=x.output.relative_to(P)
        except ValueError:r=None
        require(r is None or r.parts[0]=='runs','Write outputs outside the package or under runs/, never over proof inputs')
    count=manifest()
    with tempfile.TemporaryDirectory(prefix='f4_certificate_') as td:
        tmp=Path(td);exe=tmp/'oracle'
        subprocess.run([os.environ.get('CXX','g++'),'-std=c++17','-O3',str(P/'verify/dfa_ap_oracle.cpp'),'-o',str(exe)],check=True)
        data=load(W/'candidate.json');g=Grammar(data)
        multi,d,proofs=compile_prove(g,tmp,exe,'candidate')
        require(canonical(d)==canonical(load(W/'candidate_dfa.json')),'Compiled DFA differs from saved witness')
        require(len(d['next'])==1384,'Final DFA size mismatch')
        require([p['reachable_product_states'] for p in proofs]==[801373,801373,801373,801382],'Final product closure counts changed')
        # Direct comparisons are controls, not the proof of compiler equivalence.
        points=set(range(1,10001))|{n for mode in data['modes'] for n in mode['E']+mode['R']}
        rng=random.Random(91361);points.update(rng.randrange(1,10**40) for _ in range(1000))
        for s in range(g.m):require(all(g.contains(n,s)==member(multi,n,multi['starts'][s]) for n in points),'DFA/grammar membership mismatch')
        blo,bhi,base=enclose();expected=load(W/'expected_baselines.json')
        require(str(blo)==expected['walker']['lower'] and str(bhi)==expected['walker']['upper'],'Recomputed Walker calibration differs')
        ci8,_=correction_interval(g,8);ci,meta=correction_interval(g,10)
        require(ci8[g.start][0]<=ci[g.start][0]<=ci[g.start][1]<=ci8[g.start][1],'Taylor-order nesting failed')
        lo=blo+ci[g.start][0];hi=bhi+ci[g.start][1];stored=load(W/'weight_certificate.json')
        require(str(lo)==stored['lower'] and str(hi)==stored['upper'],'Recomputed final endpoints differ')
        # Recompute S24's weight and safety from its grammar; no chained archive.
        pg=Grammar(load(W/'predecessor_grammar.json'))
        pm,pd,pproofs=compile_prove(pg,tmp,exe,'predecessor')
        pci,pmeta=correction_interval(pg,8)
        plo=blo+pci[pg.start][0];phi=bhi+pci[pg.start][1]
        require(str(plo)==expected['predecessor']['lower'] and str(phi)==expected['predecessor']['upper'],'Recomputed predecessor endpoints differ')
        gain=lo-phi
        require(gain>F('0.00000095439183802649'),'Certified gain fails')
        require(str(gain)==stored['gain_lower'],'Gain does not equal saved certificate')
        bad=load(W/'candidate.json');bad['modes'][0]['R'].remove(1360);bg=Grammar(bad);w=[58,492,926,1360]
        require(all(bg.contains(n) for n in w),'Deletion corruption control absent')
        bd,_=compile_grammar(bg);bd,_=minimize(bd);bd=single_entry(bd);write_text(bd,tmp/'bad.txt')
        subprocess.run([str(exe),str(tmp/'bad.txt'),str(tmp/'bad.json'),'60','3000000'],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
        br=load(tmp/'bad.json');require(br['status']=='COUNTEREXAMPLE','Corrupted grammar passed')
        bw=list(map(int,br['progression']));require(bw[1]-bw[0]==bw[2]-bw[1]==bw[3]-bw[2]>0 and all(bg.contains(n) for n in bw),'Invalid reconstructed counterexample')
        from test_generic import run
        controls=run(exe);require(controls['status']=='PASS','Generic controls failed')
        display='4.4416832003';require(F(display)<lo,'Displayed strict lower bound fails')
        result={'status':'PASS','certificate_version':'standalone-1','display_strict_lower':display,
          'lower':str(lo),'upper':str(hi),'lower_decimal':decimal(lo),'upper_decimal':decimal(hi),
          'gain_lower':str(gain),'gain_lower_decimal':decimal(gain),
          'walker_recomputed':True,'predecessor_weight_recomputed':True,'predecessor_AP_proved':True,
          'independent_base_calibration':base,'predecessor_lower':str(plo),'predecessor_upper':str(phi),
          'generic_AP_proof':proofs[0],'all_control_proofs':proofs,'predecessor_control_proofs':pproofs,
          'minimal_digit_DFA_states':len(d['next']),'multi_entry_DFA_states':len(multi['next']),
          'control_states':g.m,'membership_control_comparisons':len(points)*g.m,
          'moment_accounting':meta,'controls':controls,'negative_control_progression':w,
          'negative_control_oracle':br,'manifest_payload_files':count,
          'historical_scan_replayed':False,'eight_insertion_theorem_replayed':False,
          'target':'51/10','target_proved':lo>F(51,10),'elapsed_seconds':time.time()-tic,
          'python':platform.python_version(),'compiler':subprocess.check_output([os.environ.get('CXX','g++'),'--version'],text=True).splitlines()[0],
          'scope':'Final explicit four-free witness, exact weight, and gain over the embedded predecessor. No discovery or historical exclusion replay; no global upper bound, optimum, finiteness or 5.1 claim.'}
        if x.output:
            x.output.parent.mkdir(parents=True,exist_ok=True);x.output.write_text(json.dumps(result,indent=2)+'\n')
        print('CERTIFIED F4 >',display);print('Exact enclosure:',decimal(lo),decimal(hi))
        print('Certified gain:',decimal(gain));print('Walker and predecessor recomputed: YES')
        print('Final control closures:',[p['reachable_product_states'] for p in proofs]);print('PASS')
if __name__=='__main__':main()
