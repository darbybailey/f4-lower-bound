"""Run the supplied secondary carry checker; optionally run the floating check.
These are cross-implementation controls, not external peer review or the exact
weight proof. All generated files go to a temporary directory.
"""
from pathlib import Path
import argparse,json,subprocess,tempfile,os,sys
P=Path(__file__).resolve().parent.parent

def main():
    p=argparse.ArgumentParser();p.add_argument('--with-floating',action='store_true');p.add_argument('--output',type=Path);a=p.parse_args()
    sys.path.insert(0,str(P/'verify'))
    from verify_standalone import manifest
    manifest()
    d=json.loads((P/'witness/candidate_dfa.json').read_text());n=len(d['next'])
    if d['base']!=55 or not(0<n<=2048):raise ValueError('Secondary checker supports base 55 and 11-bit states only')
    if len(d['accept'])!=n or any(x not in (0,1) for x in d['accept']):raise ValueError('Invalid accept flags')
    if not(0<=d['start']<n and 0<=d['dead']<n):raise ValueError('Invalid entry/sink')
    if any(len(row)!=55 or any(not(0<=t<n) for t in row) for row in d['next']):raise ValueError('Invalid transitions')
    if d['accept'][d['dead']] or any(t!=d['dead'] for t in d['next'][d['dead']]):raise ValueError('Invalid dead sink')
    if any(d['accept'][s]!=d['accept'][d['next'][s][0]] for s in range(n)):raise ValueError('Unsafe zero padding')
    result={'status':'PASS','scope':'Secondary implementation of the same carry formulation; optional nonrigorous floating control.'}
    with tempfile.TemporaryDirectory(prefix='f4_secondary_') as td:
        td=Path(td);exe=td/'secondary'
        subprocess.run([os.environ.get('CXX','g++'),'-O3','-std=c++17',str(P/'independent/ap4_product_check.cpp'),'-o',str(exe)],check=True)
        with (td/'dfa.txt').open('w') as f:
            print(n,d['start'],d['dead'],file=f);print(*d['accept'],file=f)
            for row in d['next']:print(*row,file=f)
        r=subprocess.run([str(exe)],cwd=td,text=True,capture_output=True,check=True,timeout=300)
        if '801373' not in r.stdout or 'found: NO' not in r.stdout:raise ValueError('Unexpected secondary result')
        result['secondary_carry_stdout']=r.stdout.strip();print(r.stdout.strip())
    if a.with_floating:
        env={**os.environ,'OPENBLAS_NUM_THREADS':'1','OMP_NUM_THREADS':'1','MKL_NUM_THREADS':'1'}
        r=subprocess.run([sys.executable,str(P/'independent/moment_sum_check.py')],text=True,capture_output=True,check=True,timeout=300,env=env)
        result['floating_control_stdout']=r.stdout.strip();print(r.stdout.strip())
        result['floating_scope']='Double-precision agreement only, not a rational enclosure.'
    if a.output:
        out=a.output.resolve()
        try:r=out.relative_to(P)
        except ValueError:r=None
        if r is not None and r.parts[0]!='runs':raise ValueError('Write outputs outside package or under runs/')
        out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS')
if __name__=='__main__':main()
