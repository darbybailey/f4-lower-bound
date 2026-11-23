// Independent 4-AP search on an LSB-first base-55 DFA: BFS over the addition-carry product of four copies of the DFA.
#include <cstdio>
#include <vector>
#include <unordered_set>
#include <cstdint>
using namespace std;
int main(){
    FILE*f=fopen("dfa.txt","r"); int n,start,dead; if(fscanf(f,"%d %d %d",&n,&start,&dead)!=3) return 2;
    vector<int> acc(n); for(int i=0;i<n;i++) if(fscanf(f,"%d",&acc[i])!=1) return 2;
    vector<int> nxt((size_t)n*55); for(int i=0;i<n;i++) for(int j=0;j<55;j++) if(fscanf(f,"%d",&nxt[(size_t)i*55+j])!=1) return 2;
    fclose(f);
    auto enc=[&](int q0,int q1,int q2,int q3,int c1,int c2,int c3,int hf)->uint64_t{
        return (uint64_t)q0 | ((uint64_t)q1<<11) | ((uint64_t)q2<<22) | ((uint64_t)q3<<33) | ((uint64_t)c1<<44) | ((uint64_t)c2<<45) | ((uint64_t)c3<<47) | ((uint64_t)hf<<49); };
    unordered_set<uint64_t> seen; seen.reserve(4000000); vector<uint64_t> q; q.reserve(4000000);
    uint64_t s0=enc(start,start,start,start,0,0,0,0); seen.insert(s0); q.push_back(s0);
    unsigned long long trans=0; bool found=false; uint64_t witness=0;
    for(size_t head=0; head<q.size() && !found; head++){
        uint64_t s=q[head];
        int q0=s&2047,q1=(s>>11)&2047,q2=(s>>22)&2047,q3=(s>>33)&2047,c1=(s>>44)&1,c2=(s>>45)&3,c3=(s>>47)&3,hf=(s>>49)&1;
        for(int xd=0;xd<55;xd++) for(int hd=0;hd<55;hd++){
            trans++;
            int v1=xd+hd+c1, v2=xd+2*hd+c2, v3=xd+3*hd+c3;
            int d0=xd, d1=v1%55, d2=v2%55, d3=v3%55, n1=v1/55, n2=v2/55, n3=v3/55;
            int r0=nxt[(size_t)q0*55+d0], r1=nxt[(size_t)q1*55+d1], r2=nxt[(size_t)q2*55+d2], r3=nxt[(size_t)q3*55+d3];
            if(r0==dead||r1==dead||r2==dead||r3==dead) continue;   // dead is absorbing and rejecting
            int nh=hf|(hd?1:0);
            uint64_t t=enc(r0,r1,r2,r3,n1,n2,n3,nh);
            if(seen.insert(t).second){
                q.push_back(t);
                if(nh && n1==0&&n2==0&&n3==0 && acc[r0]&&acc[r1]&&acc[r2]&&acc[r3]){ found=true; witness=t; break; }
            }
        }
    }
    printf("reachable product states (dead-pruned): %zu, transitions examined: %llu, four-term progression found: %s\n",seen.size(),trans,found?"YES":"NO");
    return found?1:0;
}
