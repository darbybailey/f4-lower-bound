# An explicit recurrent construction and its standalone certificate

## 1. Claim and witness

Let W(A) = sum_{n in A} 1/n and let F4 be the supremum of W(A) over subsets of
the positive integers with no nonconstant four-term arithmetic progression.
The supplied witness defines A with

    4.4416832003495265335115002922388 < W(A)
                                     < 4.4416832003495265335115002922389,

and therefore F4 > 4.4416832003. Exact rational endpoints, not their decimal
renderings, are authoritative. This is a computer-assisted proof for one
explicit set, not a statement of optimality or a proof of the target 51/10.

The fixed alphabet is

    D = {0,1,2,4,5,9,10,11,14,16,17,18,21,24,30,37,39,41,42,45,47},
    b = 55,    T_d(n) = 55(n-1)+d+1.

Each control state s has finite insertion and repair lists E_s and R_s, and a
successor delta(s,d), all given in `witness/candidate.json`. Accept 1. At n>1,
accept an insertion hit, reject a repair hit, otherwise reject a low digit
outside D or consume it and move to the indicated state at (n-1)//55+1.
This terminates because n strictly decreases. Thus

    A_s = (E_s union union_{d in D} T_d(A_delta(s,d))) minus R_s.

The actual set is A_0. Insertion and deletion lists are disjoint, duplicate-free,
and sorted. Insertion low digits are outside D; deletion low digits lie in D.
There are four reachable, inequivalent control entries. Those are not merely
four ordinary automaton states: the root tables are part of the grammar.

## 2. Exact compilation into a digit DFA

Put f_s(x)=1_{x+1 in A_s}, x>=0, and add a rejecting function f_bottom=0.
A compiler descriptor (s,O) denotes f_s with a finite map of overrides O.
For a digit d, the derivative x -> f_s(55x+d) equals its default successor
function, except at the finitely many matching root arguments. Deriving O
keeps only arguments congruent to d and divides them by 55 after removing d.
Inherited overrides take precedence over base exceptions. Overrides equal to
the default value are discarded.

Induction on digit-word length proves that this descriptor transition denotes
exactly the derivative of the original membership function. Its accepting bit
is its value at zero. Override arguments are bounded by the finite source-root
maximum and shrink under derivatives; the finite collection of possible finite
maps on these arguments gives a finite descriptor space. The implemented
compiler exhausts its reachable descriptors, then Moore refinement merges
precisely equal accepted continuation languages.

The multi-entry DFA has 1385 states; the single-entry witness in
`witness/candidate_dfa.json` has 1384. The driver recompiles and compares the
entire transition and accepting tables, not only a sample of inputs. Membership
samples are additional controls. The accepting bit at each state equals that
at its zero successor, which proves invariance under padding with high zeros.

## 3. Complete arithmetic-progression exclusion

A progression of positive integers corresponds, after subtracting 1, to

    x, x+h, x+2h, x+3h,    x>=0, h>0.

Track four DFA states, carries (c1,c2,c3), and a flag for a nonzero digit of h.
At each position choose digits a,d in {0,...,54}. The four raw digits are

    a, a+d+c1, a+2d+c2, a+3d+c3.

Their residues drive DFA transitions; their quotients become the next carries.
The invariant ranges are c1 in {0,1}, c2 in {0,1,2}, c3 in {0,1,2,3}.
A node is a counterexample precisely if all four states accept, all carries
are zero, and the nonzero flag is true. Every finite positive-step progression
has such a path, by padding to common length. Conversely, every accepting path
reconstructs four accepted integers with a positive common difference.

The finite graph is exhaustively enumerated. A rejecting absorbing DFA sink
can be pruned because no continuation from it accepts. The four final-entry
closures have sizes 801373, 801373, 801373, and 801382 and no accepting node.
Consequently every A_s, and in particular A_0, is four-term-free at all integer
lengths. This argument needs no finite root-pool catalog or safe-residue premise.
The driver independently checks graph exhaustion and rejects resource limits.
Removing deletion 1360 admits (58,492,926,1360); this real corruption is rejected.

## 4. Signed root accounting and absolute convergence

Let B=1+K(D,55) be the unedited Walker digit set. Charge a listed repair r only
if it is present before its deletion:

    R_s^* = {r in R_s : (r-1)//55+1 in A_delta(s,(r-1) mod 55)}.

The signed source c_s is +1 on E_s, -1 on R_s^*, zero otherwise. The difference
1_{A_s}-1_B satisfies the digit recurrence with source c_s. Unrolling gives
signed root-word contributions. Some deletions remove inserted descendants;
no disjointness of all deletion orbits or universal Walker membership is assumed.
Two deletion rules are inactive in each of policies 2 and 3 and cost zero.

For a low word w of length ell and value v_w define

    z_w=1-(v_w+1)/55^ell,    T_w(n)=55^ell(n-z_w),    0<=z_w<1.

All source roots exceed 1. For each such root,

    sum_w 1/T_w(n) < (1/(n-1)) sum_{ell>=0}(21/55)^ell
                   = 55/[34(n-1)].

The finite source tables therefore give an absolutely convergent signed series.
This justifies rearrangement and the subsequent moment sums.

## 5. Exact state-conditioned moments

For starting state s and terminal state t let

    M_{k;s,t} = sum_{w:delta(s,w)=t} 55^{-|w|} z_w^k,
    Q_{u,t,r} = sum_{d in D:delta(u,d)=t} (54-d)^r.

Appending the next higher digit d changes z to (54-d+z)/55. Hence

    M_{k;s,t} - 55^(-k-1) sum_u Q_{u,t,0} M_{k;s,u}
      = 1_{k=0}1_{s=t}
        + 55^(-k-1) sum_u sum_{j<k} binom(k,j) Q_{u,t,k-j} M_{j;s,u}.

The count matrix has row sum 21 and discounted spectral radius at most 21/55<1.
Each rational system is invertible; exact Gaussian elimination computes it.
Nonnegativity, domination by zeroth moments, and sum_t M_{0;s,t}=55/34 are checked.

For n>1 and 0<=z<1 the geometric remainder gives

    0 <= 1/(n-z) - sum_{k=0}^K z^k/n^{k+1}
       <= z^{K+1}/[n^{K+1}(n-1)].

Finite inverse-power sums are enclosed by integer division at scale 10^80.
The displayed remainder bounds omitted positive and negative sources separately.
The driver recomputes orders 8 and 10, checks interval nesting, and uses order 10
for the final endpoints. Thus all digit depths, not just a finite prefix, count.

## 6. Recomputing the absolute Walker offset

No stored Walker endpoint is used as a proof premise. The constant-alphabet
checker `verify/walker_calibration.py` recomputes it as follows. The finite head
consists of n=1+d+55a for a,d in D. Every remaining n has a unique form

    n = 55^ell u + v_w + 1,

where w is a low word of length ell>=0 and u is an exactly three-digit block
with nonzero highest digit. There are N=21^2*20 such u, all u>=55^2. Put

    t_w=(v_w+1)/55^ell,  0<t_w<=1,
    L_{k,ell}=sum_{|w|=ell}55^-ell t_w^k.

Then L_{k,0}=1, and appending a higher digit gives

    L_{k,ell+1}=55^(-k-1) sum_{j=0}^k binom(k,j)
                                      (sum_{d in D} d^{k-j}) L_{j,ell}.

These finite-depth moments are exact rational numbers. For even K, the
alternating polynomial through K-1 is a lower bound for 1/(u+t), while the
polynomial through K is an upper bound. The sums of 1/u^{k+1} are rounded
outwards at scale 10^100; every sign is accounted for. All uncomputed ell>=H
contribute at most

    [N/55^2] (21/55)^H / (1-21/55).

Taking H=80 and K=10 reproduces precisely the archived narrow Walker interval.
The package compares the computed fractions with expected values only after
computing them. Adding the signed correction from Section 5 proves the claimed
absolute bound with no chain of trusted calibration data.

## 7. The comparison with the predecessor

`witness/predecessor_grammar.json` is the unchanged S24 grammar. The same compiler
and generic carry checker prove its three control entries four-term-free. Its
order-8 signed correction plus the newly recomputed Walker offset reproduces
both of its archived endpoints. Subtracting its verified upper endpoint from
the final lower endpoint proves gain greater than

    0.00000095439183802649.

This is a proof replay from the supplied predecessor witness, not a rerun of
the old search or the old catalog method. No predecessor ZIP is required.

## 8. Acceptance scope and reproducibility

The primary path uses only Python standard-library rational arithmetic and a
C++17 compiler. All checks remain active under Python optimization. It includes
52 cross-implementation carry controls, 72000 compiler-control membership checks,
actual-witness membership comparisons, and real corruption controls. These are
implementation checks, not statistically independent experiments or peer review.
The two separately supplied secondary checkers are additional controls; the
floating-point checker is not the rigorous enclosure.

The historical eight-insertion theorem, scan-completeness claims, solver timings,
search-efficiency comparisons, and other earlier numerical exclusions are outside
this certificate. None is required for the main construction proof. Discovery
programs and records are intentionally withheld. The explicit construction,
proof mathematics, and verification code are disclosed; this is not a claim that
those disclosures reveal no reusable ideas.

Background: Alexander Walker, *Integer Sets of Large Harmonic Sum Which Avoid
Long Arithmetic Progressions*, arXiv:2203.06045, supplies the base digit construction.
The certificate does not rely on a claimed literature record. Provenance and
unchanged-source hashes are recorded in `PROVENANCE.json`.
