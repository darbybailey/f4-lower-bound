// Independent generic addition-carry proof for an LSB-first DFA for n-1.
// No fixed digit alphabet, exceptional-root list, safe residues, or AP catalog.
#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <unordered_map>
#include <vector>
#include <iomanip>
#include <sstream>
using namespace std;
struct Big {
 vector<uint32_t> a{0};
 void muladd(uint32_t m,uint32_t v){uint64_t c=v;for(auto &x:a){c+=uint64_t(x)*m;x=c%1000000000;c/=1000000000;}while(c){a.push_back(c%1000000000);c/=1000000000;}}
 void addtimes(const Big&b,uint32_t m){if(a.size()<b.a.size())a.resize(b.a.size());uint64_t c=0;for(size_t i=0;i<a.size();i++){c+=a[i]+(i<b.a.size()?uint64_t(b.a[i])*m:0);a[i]=c%1000000000;c/=1000000000;}if(c)a.push_back(c);}
 string str()const{ostringstream o;o<<a.back();for(int i=int(a.size())-2;i>=0;i--)o<<setw(9)<<setfill('0')<<a[i];return o.str();}
};
struct Node {array<uint32_t,4> q; uint8_t c1,c2,c3,nz,ad,dd;uint32_t parent;};
int main(int argc,char**argv){try{
 if(argc<3){cerr<<"usage: oracle dfa.txt result.json [seconds=180] [maxstates=3000000]\n";return 2;}
 ifstream f(argv[1]);int b,S,start,dead;f>>b>>S>>start>>dead;
 if(!f||b<2||b>255||S<1||S>16000)throw runtime_error("shape outside supported bounds");
 vector<int>accept(S);for(auto&x:accept)f>>x;
 vector<vector<uint32_t>>T(S,vector<uint32_t>(b));for(auto&row:T)for(auto&t:row){f>>t;if(t>=uint32_t(S))throw runtime_error("invalid target");}
 if(!f||start<0||start>=S||dead<0||dead>=S||accept[dead])throw runtime_error("input");
 for(auto t:T[dead])if(t!=uint32_t(dead))throw runtime_error("not a dead sink");
 for(int s=0;s<S;s++)if(accept[s]!=accept[T[s][0]])throw runtime_error("unsafe zero padding");
 double maxseconds=argc>3?stod(argv[3]):180.;size_t maxstates=argc>4?stoull(argv[4]):3000000;
 auto tic=chrono::steady_clock::now();
 auto elapsed=[&](){return chrono::duration<double>(chrono::steady_clock::now()-tic).count();};
 auto code=[&](const Node&n){uint64_t k=n.nz+2*(n.c3+4*(n.c2+3*n.c1));for(int j=0;j<4;j++)k=k*S+n.q[j];return k;};
 vector<Node>q;q.reserve(100000);unordered_map<uint64_t,uint32_t>seen;seen.reserve(200000);
 Node first{{uint32_t(start),uint32_t(start),uint32_t(start),uint32_t(start)},0,0,0,0,0,0,UINT32_MAX};q.push_back(first);seen[code(first)]=0;
 vector<vector<int>>digits(S);for(int s=0;s<S;s++)for(int d=0;d<b;d++)if(T[s][d]!=uint32_t(dead))digits[s].push_back(d);
 uint64_t edges=0,steps=0;size_t head=0;bool complete=true;int witness=-1;
 for(;head<q.size();head++){
  if(head%1024==0&&(elapsed()>maxseconds||q.size()>maxstates)){complete=false;break;}
  const Node cur=q[head];
  for(int a:digits[cur.q[0]])for(int d=0;d<b;d++){
   steps++;int r1=a+d+cur.c1,r2=a+2*d+cur.c2,r3=a+3*d+cur.c3;
   auto q1=T[cur.q[1]][r1%b];if(q1==uint32_t(dead))continue;
   auto q2=T[cur.q[2]][r2%b];if(q2==uint32_t(dead))continue;
   auto q3=T[cur.q[3]][r3%b];if(q3==uint32_t(dead))continue;
   Node n{{T[cur.q[0]][a],q1,q2,q3},uint8_t(r1/b),uint8_t(r2/b),uint8_t(r3/b),uint8_t(cur.nz||d>0),uint8_t(a),uint8_t(d),uint32_t(head)};edges++;
   auto k=code(n);if(seen.find(k)!=seen.end())continue;
   auto id=uint32_t(q.size());seen.emplace(k,id);q.push_back(n);
   if(n.nz&&!n.c1&&!n.c2&&!n.c3&&accept[n.q[0]]&&accept[n.q[1]]&&accept[n.q[2]]&&accept[n.q[3]]){witness=id;break;}
  }
  if(witness>=0)break;
 }
 ofstream out(argv[2]);out.precision(17);
 out<<"{\"status\":\""<<(witness>=0?"COUNTEREXAMPLE":complete?"PROVED_FREE":"INCOMPLETE")<<"\",\"dfa_states\":"<<S<<",\"reachable_product_states\":"<<q.size()<<",\"processed_states\":"<<head<<",\"accepted_edges\":"<<edges<<",\"digit_pair_checks\":"<<steps<<",\"seconds\":"<<elapsed();
 if(witness>=0){
  vector<pair<int,int>>ds;uint32_t at=witness;while(q[at].parent!=UINT32_MAX){ds.emplace_back(q[at].ad,q[at].dd);at=q[at].parent;}reverse(ds.begin(),ds.end());
  Big a,d;for(auto it=ds.rbegin();it!=ds.rend();++it){a.muladd(b,it->first);d.muladd(b,it->second);}
  if(d.str()=="0")throw runtime_error("invalid reconstructed difference");
  out<<",\"progression\":[";for(int j=0;j<4;j++){if(j)out<<",";Big v=a;v.addtimes(d,j);v.muladd(1,1);out<<'"'<<v.str()<<'"';}out<<"]";
 }
 out<<"}\n";cerr<<"done "<<q.size()<<" states "<<elapsed()<<" seconds status "<<(witness>=0?"counterexample":complete?"free":"incomplete")<<"\n";
 return 0;
}catch(const exception&e){cerr<<"verification error: "<<e.what()<<"\n";return 2;}
}
