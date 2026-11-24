---
title: "F4 > 4.4416832003: Recurrent Digit Grammars and Certified Reciprocal Sums"
author: "Darby Bailey McDonough"
orcid: "0000-0003-4072-6191"
affiliation: "Pip Projects, Inc. · Digital Sidewalk Lab · Independent Researcher"
doi: "10.5281/zenodo.24485654"
date: "13 September 2026 · Certificate-only manuscript, version 1.2"
lang: en-US
---

# Abstract {.unnumbered}

We construct an explicit infinite subset of the positive integers containing no nonconstant four-term arithmetic progression and certify that its reciprocal sum exceeds $4.4416832003$. The construction begins with Walker’s base-55 digit set and develops through finite insertion–deletion exchanges, shared repair costs, recursive root families, branch-dependent continuations, and recurrent policies. Its final description has four reachable control policies with finite exception tables. These tables are compiled into a complete ordinary digit automaton: the minimized single-entry automaton has 1,384 states. An addition-carry product search exhausts 801,373 reachable states and proves progression-freeness at every integer length, without assuming the earlier fixed root pool, safe-residue reduction, or progression catalog. Exact rational matrix moments, active-deletion accounting, and explicit remainder estimates enclose the entire infinite reciprocal sum within an interval of width less than $2.14\times10^{-33}$. A standalone certificate-only supplement recomputes the Walker baseline, verifies the final and predecessor constructions, and certifies their positive difference without the discovery software or earlier archive chain. Historical bounded-insertion exclusions, alternative digit systems, candidate screens, and an archive repair are retained as explicitly scoped records; their withheld computational artifacts are not dependencies of the main theorem. The result is a constructive lower bound, not an unrestricted upper bound, a global optimum, or a proof of the target $5.1$.

**Keywords:** arithmetic progression; reciprocal sum; digit-restricted set; finite automaton; computer-assisted proof; exact arithmetic; combinatorial optimization.

**Mathematical and publication status.** The main result combines written arguments with explicitly identified finite computations. It has not been formalized in a proof assistant or independently peer reviewed. This certificate-only edition is prepared for public deposit; the repository identifier for this deposit is DOI 10.5281/zenodo.24485654. Discovery software and search records are withheld. Historical numerical claims outside the standalone acceptance path are labeled as such. No claim of publication priority or of a current public numerical record is made.

# 1. Introduction and scope

For a set $A$ of positive integers, write

$$
\begin{aligned}
\mathcal W(A)&=\sum_{n\in A}\frac1n,\\
F_4&=\sup\{\mathcal W(A):A\subseteq\mathbb N_{>0},\ A\text{ is four-term-progression-free}\}.
\end{aligned}
\tag{1}
$$

A progression is always nonconstant: its terms are $a,a+h,a+2h,a+3h$ with $a,h\ge1$. The distinction between constructing a set of large reciprocal sum and proving a uniform upper bound is fundamental. This paper concerns the former. An upper endpoint for the sum of one constructed set is not an upper bound for $F_4$.

Walker gives a base-55 digit construction with reciprocal sum approximately $4.43975$, together with a modular sufficient condition for avoiding progressions [1]. We retain that construction as an independently checked starting point. The ensuing improvements are not consequences of choosing a more ambitious numerical target. Each improvement requires an actual set, a complete progression-exclusion argument, and a rigorously enclosed positive change in reciprocal mass.

The main contribution is an explicit recurrent construction with

$$
\boxed{F_4>4.4416832003.}
\tag{2}
$$

The numerical improvement is modest. The accompanying methodological development is more substantial: finite root exceptions and history-dependent continuation rules are compiled into an ordinary digit automaton, permitting an arithmetic-carry proof that no longer depends on a frozen list of candidate roots. Finite-automaton decision procedures for arithmetic properties are established methods; the present contribution is their implementation and integration with the particular construction and its exact signed weight calculation, not a new general decidability theorem [2; C1].

The main constructive lower bound is accompanied by a standalone, certificate-only supplement containing the explicit witness and the software needed to verify its arithmetic-progression exclusion and exact reciprocal-sum enclosure. The proprietary discovery engine, optimization models, proposal generators, screening programs, and search records are not distributed. Reproducibility here concerns verification of the stated mathematical witness, not regeneration of its discovery trajectory.

The article also records the research path that produced the witness. In particular, it preserves negative results rather than presenting only successful searches. Exact exclusions are stated with their baseline, candidate pool, and permitted edits. Time-limited search failures are not converted into impossibility theorems. Root counts are not substituted for changes in infinite reciprocal mass, and redundant or unreachable states are not counted as mathematical improvement.

## 1.1. Documentary scope

The constructive sequence of 11–13 September 2026 is documented by privately retained research archives, identified internally as S01–S26. These identifiers record research history and provenance; they are not promises of public access to discovery software. Earlier manuscripts B01–B04 are retained privately as antecedent context. Their broader research programs are not relabeled as new results of the present construction.

The sole supplementary object designated for public release is `F4-Certificate-Only-Standalone.zip` [C1]. It contains the final grammar, compiled digit automaton, exact rational certificate, predecessor grammar, and solver-free verification code. It reconstructs the Walker calibration, both reciprocal enclosures, and the necessary infinite-progression proofs without any earlier archive. Discovery software and search archives are withheld. Historical experiments outside that acceptance path are presented as recorded observations, not computations replayable from C1. The paper is an artifact-backed research account, not a purported verbatim transcript of conversations or every optimizer iteration.

## 1.2. Organization and evidence conventions

Sections 2–6 give the final construction and its proof. Sections 7–10 describe historical development, general exclusion arguments, and recorded numerical experiments. Sections 11–12 discuss verification and limits. Appendices retain auxiliary analytic proofs, historical experiment ledgers, archive provenance, explicit algorithms, and the exact public-certificate identifiers.

References [1]–[4] are external primary literature. S01–S26 and B01–B04 designate privately retained sources. C1 designates the standalone certificate; V1 identifies its author-side, AI-assisted verification record under `validation/`, and V2 identifies its secondary implementation checks. A historical statement marked *recorded* is supported by a retained source, but its original computation is not asserted to be replayable from C1. General propositions with complete written proofs remain analytic results. The main lower bound and its predecessor comparison are replayable from C1; other historical numerical exclusions are not prerequisites of those claims.

# 2. The final construction and main theorem

## 2.1. Digits, roots, and policies

Let $b=55$ and

$$
D=\{0,1,2,4,5,9,10,11,14,16,17,18,21,24,30,37,39,41,42,45,47\}.
\tag{3}
$$

Put $m=|D|=21$, define

$$
W=1+\mathcal K(D,55),\qquad T_d(n)=55(n-1)+d+1,
\tag{4}
$$

and read the digits of $n-1$ from least significant to most significant. The shift by one is part of the definition and is used consistently in every root residue, transition, and membership test.

There are four policies $s\in\{0,1,2,3\}$. Policy $s$ has finite insertion and deletion tables $E_s,R_s$ and a deterministic transition $\delta(s,d)$ for each $d\in D$. Membership in $A_s$ is specified as follows. Reject $n<1$ and accept $n=1$. For $n>1$, accept an insertion-table hit and reject a deletion-table hit. Otherwise write $n-1=55q+d$. Reject if $d\notin D$; if $d\in D$, continue with $(\delta(s,d),q+1)$. The argument strictly decreases whenever a further digit is consumed, so this is a terminating definition, not an unspecified choice of a fixed point.

Equivalently, with the terminal convention $1\in A_s$,

$$
A_s=\left(E_s\cup\bigcup_{d\in D}T_d(A_{\delta(s,d)})\right)\setminus R_s.
\tag{5}
$$

All insertion roots have low digit outside $D$, all listed deletions have low digit in $D$, and the tables are duplicate-free and disjoint within each policy. The final object is $A=A_0$. Every table entry and transition is contained in `witness/candidate.json`, copied byte-for-byte from S25. Its SHA-256 identifier is recorded in Appendix E.

| Policy | Insertion roots $|E_s|$ | Listed deletions $|R_s|$ | Active deletions $|R_s^*|$ |
|:--|--:|--:|--:|
| 0 | 3,590 | 737 | 737 |
| 1 | 3,547 | 723 | 723 |
| 2 | 3,547 | 718 | 716 |
| 3 | 3,546 | 718 | 716 |

Table 1. The four final policies. These are finite rule counts, not counts of all changed integers. An inactive deletion has zero cost in the exact accounting of Section 6.

For a compact transition table, partition $D$ into

$$
\begin{aligned}
G&=\{2,4,9,14,17,18,24,30,37,42,45,47\},\\
H&=\{11,16,21,41\},\quad J=\{0,5,10\},\quad K=\{1,39\}.
\end{aligned}
\tag{6}
$$

| Current policy | Digits in $G$ | Digits in $H$ | Digits in $J$ | Digits in $K$ |
|:--|--:|--:|--:|--:|
| 0 | 2 | 1 | 3 | 3 |
| 1 | 2 | 0 | 3 | 3 |
| 2 | 2 | 1 | 1 | 3 |
| 3 | 2 | 1 | 1 | 3 |

Table 2. Successor policy $\delta(s,d)$. The same transition row for policies 2 and 3 does not make their languages identical: their exception tables differ.

## 2.2. Main result

**Theorem 2.1 (computer-assisted constructive lower bound).** The set $A_0$ defined by (3)–(6) and the integer tables in `witness/candidate.json` in C1 is four-term-progression-free. Its reciprocal sum satisfies

$$
\begin{aligned}
4.4416832003495265335115002922388
&<\mathcal W(A_0)\\
&<4.4416832003495265335115002922389.
\end{aligned}
\tag{7}
$$

Consequently $F_4>4.4416832003$. Relative to the preceding three-policy construction supplied as `witness/predecessor_grammar.json` in C1 (originally S24), the increase is greater than

$$
0.00000095439183802649.
\tag{8}
$$

**Proof.** Section 4 proves that the compiler constructs an ordinary finite automaton recognizing exactly the membership rule (5). Section 5 establishes that exhaustive reachability in the addition-carry product decides whether that language contains a four-term progression. The final A0 product graph is exhausted without an accepting state. Section 6 proves the signed infinite-series identity, the rational moment equations, and the directed remainder estimates used to compute (7). The exact certificate lies above the displayed lower endpoint and below the displayed upper endpoint. Subtracting the predecessor’s rational upper endpoint from the new rational lower endpoint proves (8). The standalone verifier recomputes the Walker baseline, compiles and proves the predecessor grammar, and derives its upper endpoint before forming the gain. The author-side execution record V1 documents these computations; its stored PASS status is not an input premise. The detailed finite computations, rather than an optimizer’s score, supply the computational portions of the proof. $\square$

The authoritative certificate uses rational endpoints, not the displayed decimal strings. Its interval width is less than $2.14\times10^{-33}$. The lower and upper values printed by the replay begin, respectively,

```
4.4416832003495265335115002922388357781767636075010835...
4.4416832003495265335115002922388379082953774099808229...
```

The displayed decimal enclosure is deliberately wider than those exact endpoints. Neither its upper endpoint nor its small width is an upper estimate for $F_4$.

# 3. From finite repairs to recurrent root families

## 3.1. Modular descent

**Lemma 3.1 (digit descent).** Suppose $D\subseteq\{0,\ldots,b-1\}$ contains no modular four-term progression with nonzero difference modulo $b$. An integer progression whose four shifted terms have low digits in $D$ has common difference divisible by $b$ and a common low digit. Removing that digit produces another integer progression.

**Proof.** Reducing the shifted terms modulo $b$ gives a modular progression in $D$. Its difference must be zero modulo $b$, so all four residues agree. If the common residue is $d$, the parent map $n\mapsto(n-1-d)/b+1$ divides the common difference by $b$ and preserves positivity. $\square$

For (3), all $55\cdot54=2,970$ nonzero-difference start/difference pairs are checked directly, including differences not coprime to 55. Repeated descent proves that $W$ is four-term-free. The same argument underlies the earlier root-catalog certificates [1; S01–S24].

**Lemma 3.2 (branch composition).** Under the hypothesis of Lemma 3.1, if every $C_d$ is four-term-free, then $\bigcup_{d\in D}T_d(C_d)$ is four-term-free.

**Proof.** Any progression must occupy one common low-digit branch and descend into the corresponding $C_d$, where it is impossible. The different children need not coincide. $\square$

This lemma permits heterogeneous children, but it does not make an arbitrary addition of the other 34 base-55 digits safe. Changing the ordinary alphabet changes the premise of the argument.

## 3.2. A fully explicit first improvement

The initial finite repair is

$$
B=(W\setminus\{1330,1360\})\cup\{492\}.
\tag{9}
$$

The insertion is outside $W$, since $492-1=8\cdot55+51$, whereas both deletions belong to $W$. A modular check shows that residue 51 cannot begin a progression whose other three residues all lie in $D$. If 492 occupies position $j=1,2,3$, indexing the first position by zero, positivity bounds the difference by $\lfloor491/j\rfloor$. The complete $491+245+163=899$ checks find exactly

$$
(73,492,911,1330),\qquad(58,492,926,1360).
\tag{10}
$$

Deleting their last terms destroys every new progression. Therefore (9) is an infinite four-term-free set, and its exact gain is

$$
\frac1{492}-\frac1{1330}-\frac1{1360}
=\frac{12133}{22248240}>0.
\tag{11}
$$

This elementary certificate is the first step in the constructive lineage, not a finite-prefix approximation [S01].

## 3.3. Complete finite root reduction

For a finite insertion pool $P$, define the superlanguage

$$
U(P)=W\cup\bigcup_{e\in P}\mathcal O(e),\qquad
\mathcal O(e)=\{T_w(e):w\in D^*\}.
\tag{12}
$$

Here $T_w$ denotes an ordered composition and includes the empty word. In the earlier catalogs, every root has low residue in

$$
S=\{7,29,40,51\}.
\tag{13}
$$

The residue test verifies that, for each $r\in S$ and every difference modulo 55, $r+h,r+2h,r+3h$ are not all in $D$.

**Proposition 3.3 (complete root criterion).** For a recursively defined root grammar with the ordinary alphabet (3) and roots satisfying (13), it suffices to check all root-containing progressions generated by the following finite cases: an insertion root in position $j=1,2,3$ with $h\le\lfloor(e-1)/j\rfloor$, and every pair of distinct roots assigned to two distinct progression positions.

**Proof.** Repeated digit descent takes any putative progression to one containing an unscaled insertion root. If a root is not first, positivity gives the stated difference bound. If the first term is the only root, the residue property contradicts ordinary low digits for the remaining three terms. Otherwise a second root and its position determine the difference. The resulting terms lie below $3\max P$. Thus the finite window follows from the proof; it is not an extrapolation from a scan cutoff. $\square$

Earlier acceptances used this reduction to regenerate complete catalogs, including 57,105 rows for the 5,282-root union and 61,539 rows for the 5,755-root union [S21–S24]. The generic final verifier in Section 5 no longer assumes Proposition 3.3.

## 3.4. Shared deletion costs and ancestry

For $n>1$ let $\nu(n)=\sum_{x\in\mathcal O(n)}1/x$. Its orbit identity is

$$
\nu(n)=\frac1n+\sum_{d\in D}\nu(T_d(n)).
\tag{14}
$$

Two deletion orbits rooted in $W$ are either disjoint or nested, because each integer has a unique chain of digit parents. If $\operatorname{Min}(R)$ removes every deletion root with an ancestor already in $R$, then

$$
\mathcal W\!\left(\bigcup_{r\in R}\mathcal O(r)\right)
=\sum_{r\in\operatorname{Min}(R)}\nu(r).
\tag{15}
$$

This follows by replacing the union with disjoint minimal-root orbits. Replacing a deletion antichain $R$ by $R'$ therefore has net cost

$$
\sum_{r\in R'\setminus R}\nu(r)-
\sum_{r\in R\setminus R'}\nu(r).
\tag{16}
$$

The second term refunds a previously charged part of a newly deleted ancestor orbit. It does not necessarily restore any integer. Confusing normalization with restoration would overstate the gain [S04; S16–S17].

The later multi-policy grammar can delete descendants of inserted roots and can have overlapping signed contributions. It cannot be priced by assuming that every listed deletion is a disjoint Walker orbit. Section 6 replaces that assumption with an exact indicator recurrence.

## 3.5. Joint feasibility and component selection

In the union model, let $P_e$ be the insertion origins needed by a progression and $Q_e$ its available deletion origins. Binary choices $x,y$ satisfy

$$
\sum_{p\in P_e}x_p-\sum_{r\in Q_e}y_r\le |P_e|-1.
\tag{17}
$$

At least one required insertion is absent or one supporting point is deleted. Charging each selected deletion once allows distinct insertions to share repair costs.

The earlier branch construction grouped origins into components. For each catalog row that could occur under a component subfamily, the verifier checked that the relevant insertion and deletion labels were nonempty and belonged to one common component. Omitting that component removes an insertion origin; retaining it supplies a deletion. Consequently arbitrary selections of complete components remain safe within the checked universe. Different digit branches may choose different component subfamilies. This is the *component lemma* used in S21–S23, not a statement that arbitrary new root edits remain safe without renewed checks.

# 4. Compiling the entire construction into a digit automaton

The four policies are not four states of an ordinary digit-only automaton. Their finite integer tables contain additional information. The compilation described here incorporates all of that information into ordinary states and transitions.

Put $f_s(x)=\mathbf1_{A_s}(x+1)$ for $x\ge0$ and introduce the dead function $f_\bot\equiv0$. A compiler descriptor $(s,O)$ consists of a base function $f_s$ and a finite map $O$ overriding its values at specified nonnegative arguments. Its digit derivative is the function

$$
g_d(x)=g(55x+d),\qquad 0\le d<55.
\tag{18}
$$

Away from root exceptions, the derivative of $f_s$ is $f_{\delta(s,d)}$ for $d\in D$ and $f_\bot$ otherwise. A root $r$ contributes an exception only when $(r-1)\bmod55=d$, then at the contracted argument $(r-1-d)/55$. An existing override at $y$ survives only when $y\bmod55=d$, then moves to $\lfloor y/55\rfloor$. Existing overrides take precedence over the base derivative’s exceptions. An override agreeing with the new base value is removed.

**Theorem 4.1 (compiler correctness and finiteness).** The completed descriptor construction recognizes exactly the base-55 least-significant-digit-first representations of $n-1$ for $n\in A_s$.

**Proof.** The transition rule is an exact calculation of (18), including the precedence of point overrides. Induction on the consumed digit word therefore identifies each descriptor with the corresponding derivative of the original membership function. Its accepting bit is its value at zero; after the last digit this is exactly the original integer’s membership.

There are finitely many base policies and all override arguments lie in a bounded set determined by the largest source-table argument: differentiation contracts existing arguments and introduces only contracted source roots. A descriptor uses a finite partial Boolean map on that bounded set. The total descriptor universe is therefore finite. Enumeration by interning descriptors reaches a finite closed transition graph. A resource-limited run that stops before closure is not a proof of completion.

For the completed graph, each accepting bit equals that of its zero-digit successor. Hence appending high zero digits leaves membership unchanged. The exported graph is an ordinary DFA, and its runtime membership procedure needs no integer lookup table or call to the grammar evaluator. $\square$

Moore partition refinement merges states with the same residual language. The four entry functions remain pairwise inequivalent. The multi-entry automaton has 1,385 states. Trimming to the single entry for $A_0$ removes one unreachable auxiliary state and gives the 1,384-state minimized automaton used by the final proof [C1; V1]. Control-policy reachability and ordinary-DFA reachability are different notions; the extra multi-entry state is not counted as a fifth policy.

Compiler–grammar comparisons on sampled integers are useful regression controls, but the semantic induction above is the reason all integers are covered. During replay the canonical compiled automaton is also compared with the shipped automaton, so a mismatching saved transition table is not silently accepted.

# 5. A generic infinite progression certificate

## 5.1. Addition-carry product

Let a complete zero-padding-invariant DFA have $Q$ states, transition function $\tau$, an accepting set, and a dead sink. For a hypothetical progression write the shifted terms as

$$
x,\quad x+h,\quad x+2h,\quad x+3h,
\qquad x\ge0,\ h>0.
\tag{19}
$$

A product state is

$$
(q_0,q_1,q_2,q_3,c_1,c_2,c_3,\epsilon),
\tag{20}
$$

with $c_1\in\{0,1\}$, $c_2\in\{0,1,2\}$, $c_3\in\{0,1,2,3\}$, and $\epsilon\in\{0,1\}$. Initially all four DFA states are the selected entry and all carries and the flag are zero. Choose a digit $a$ of $x$ and a digit $d$ of $h$. The raw digit values are

$$
a,\quad a+d+c_1,\quad a+2d+c_2,\quad a+3d+c_3.
\tag{21}
$$

Their residues modulo 55 drive the four DFA transitions; their integer quotients give the next carries. Set the flag when a nonzero difference digit occurs. The stated carry ranges are invariant: if $0\le c_j\le j$, then the next quotient is at most $j$.

A product state is successful when all four DFA states accept, all carries vanish, and $\epsilon=1$. Its digit path reconstructs an ordinary positive nonconstant progression after adding one to each shifted term.

**Theorem 5.1 (soundness and completeness).** A successful product state is reachable if and only if the recognized positive-integer set contains a nonconstant four-term progression.

**Proof.** Every transition implements the base-55 addition identities (21), so a successful finite path with zero terminal carries represents the four integers in (19). The flag ensures $h>0$. Acceptance of the four component states gives membership.

Conversely, represent $x$ and $h$ in base 55 and pad with high zeros until all four terms and all carries are exhausted. The digit identities force the corresponding product path. Zero-padding invariance preserves the four memberships, and the positive difference sets the flag. The terminal product state is successful. $\square$

There are at most $48Q^4$ formal product states. Breadth-first reachability either reconstructs a counterexample or exhausts the reachable subgraph. Transitions entering the dead sink can be omitted because no later digit can make that component accept. Exhaustion without success proves the absence of progressions at every integer length. A time or state limit produces `INCOMPLETE`, never `PROVED_FREE`.

## 5.2. Executed closure and controls

For the final single entry, the native exact-integer implementation exhausts **801,373** reachable product states with no successful state. The four control-entry languages are separately checked through the multi-entry compilation:

| Entry language | Reachable product states | Outcome |
|:--|--:|:--|
| $A_0$ | 801,373 | Complete; no progression |
| $A_1$ | 801,373 | Complete; no progression |
| $A_2$ | 801,373 | Complete; no progression |
| $A_3$ | 801,382 | Complete; no progression |

Table 3. The sum 3,205,501 counts visits across four checks, not distinct states in one shared graph. The $A_0$ row is the proof of the exported single-entry automaton; the other rows prove the remaining control-entry languages [C1; V1].

A concrete corruption control removes deletion 1360 from policy 0. The progression $(58,492,926,1360)$ is then admitted, and the generic checker rejects the altered grammar. A separate Python carry implementation and the C++ checker agree on 52 finite-generator controls, including a length-sensitive base-55 digit-31 witness. Compiler fixtures cover 72,000 integer memberships; the standalone verifier compares the winning grammar and DFA on 61,732 policy/integer pairs from the root tables, a finite prefix, and large integers. The historical S25 release used a different 115,948-comparison sample, including catalog points; that historical count is not attributed to C1. These controls test implementation consistency. They are not an independent peer review or a substitute for the completed product proof.

The proof in this section takes only the complete DFA as input. It assumes neither safe exceptional residues, a modularly four-free ordinary alphabet, the 5,755-root pool, nor the 61,539-row catalog. That distinction is what permits the final acceptance of roots outside the preceding catalog.

# 6. Exact weight of the entire infinite construction

## 6.1. Active deletions and the signed recurrence

A listed deletion must be charged only if the point would be present before applying that deletion. Define

$$
R_s^*=\{r\in R_s:r=T_d(q),\ d\in D,\ q\in A_{\delta(s,d)}\}.
\tag{22}
$$

In the final data, policies 2 and 3 each list two inactive deletions, 22110112 and 22110150. Their subtraction is zero. Some active deletions remove descendants of inserted roots rather than members of $W$ [C1; V1].

Let $h_s(n)=\mathbf1_{A_s}(n)-\mathbf1_W(n)$ and

$$
c_s(n)=\mathbf1_{E_s}(n)-\mathbf1_{R_s^*}(n).
\tag{23}
$$

Because insertion residues lie outside $D$, and because the ordinary branches are disjoint by their low digit, subtraction of the Walker recurrence from (5) gives

$$
h_s(n)=c_s(n)+\sum_{d\in D}\mathbf1_{n=T_d(q)\text{ for some }q}\,
 h_{\delta(s,d)}(q).
\tag{24}
$$

Here $h_s(1)=0$. Unrolling (24) is exact: source terms may cancel, so no unjustified disjointness of all signed root orbits is required.

## 6.2. Absolute convergence

For a low-digit word $w$ of length $\ell$ and value $v_w$, define

$$
z_w=1-\frac{v_w+1}{55^\ell},\qquad
T_w(n)=55^\ell(n-z_w),\qquad 0\le z_w<1.
\tag{25}
$$

The empty word has $z=0$. Every source root exceeds one, and therefore

$$
\sum_{w\in D^*}\frac1{T_w(n)}
<\frac1{n-1}\sum_{\ell\ge0}\left(\frac{21}{55}\right)^\ell
=\frac{55}{34(n-1)}.
\tag{26}
$$

There are finitely many source roots in finitely many policies. Equation (26) bounds the absolute value of their total word expansion by a finite sum. Consequently all regroupings used to compute the signed reciprocal correction are justified by absolute convergence. This proves convergence for the explicit family; it is not a uniform bound over arbitrary four-term-free sets.

## 6.3. State-conditioned matrix moments

For starting policy $s$ and terminal policy $t$, put

$$
M_{k;s,t}=\sum_{w:\delta(s,w)=t}55^{-|w|}z_w^k,
\tag{27}
$$

with the empty-word contribution interpreted as one when $k=0$. Appending a higher digit $d$ changes $z$ to $(54-d+z)/55$. Define

$$
Q_{u,t,r}=\sum_{d\in D:\delta(u,d)=t}(54-d)^r.
\tag{28}
$$

**Proposition 6.1 (rational moment systems).** The moments satisfy

$$
\begin{aligned}
M_{k;s,t}-55^{-k-1}\sum_u Q_{u,t,0}M_{k;s,u}
={}&\mathbf1_{k=0}\mathbf1_{s=t}\\
&+55^{-k-1}\sum_u\sum_{j<k}\binom{k}{j}
 Q_{u,t,k-j}M_{j;s,u}.
\end{aligned}
\tag{29}
$$

These systems have unique rational solutions, and

$$
\sum_tM_{0;s,t}=\frac{55}{34}.
\tag{30}
$$

**Proof.** Separate the empty word from every nonempty word and condition on its final appended digit. The word discount contributes $1/55$ and the $k$th power contributes $55^{-k}$. Expanding $(54-d+z)^k$ and collecting the terms with $j=k$ on the left gives (29). The matrix $Q_{u,t,0}$ has nonnegative entries and row sum 21, hence spectral radius at most 21. Division by $55^{k+1}$ gives spectral radius below one, so the linear system is invertible. All coefficients and earlier-order moments are rational, proving rationality inductively. Summing over terminal policies counts every word exactly once and gives the geometric series (30). $\square$

The implementation uses exact rational Gaussian elimination. It also checks nonnegativity and domination by the zeroth moments. For example, the first zeroth-moment row of the final transition law is

$$
\left(\frac{29370}{29087},\frac{15565}{116348},
\frac6{17},\frac{239}{1972}\right),
\tag{31}
$$

whose sum is $55/34$.

## 6.4. Signed reciprocal enclosure

For $n>1$ and $0\le z<1$, the exact finite expansion yields

$$
0\le\frac1{n-z}-\sum_{k=0}^{K}\frac{z^k}{n^{k+1}}
\le\frac{z^{K+1}}{n^{K+1}(n-1)}.
\tag{32}
$$

For each terminal policy define

$$
C_{k,t}=\sum_{e\in E_t}e^{-k-1}-\sum_{r\in R_t^*}r^{-k-1},
\qquad Z_{K,s}=\sum_t\sum_{k=0}^{K}M_{k;s,t}C_{k,t}.
\tag{33}
$$

The total correction $\Delta_s=\mathcal W(A_s)-\mathcal W(W)$ obeys

$$
\begin{aligned}
\Delta_s&\ge Z_{K,s}-\sum_tM_{K+1;s,t}
 \sum_{r\in R_t^*}\frac1{r^{K+1}(r-1)},\\
\Delta_s&\le Z_{K,s}+\sum_tM_{K+1;s,t}
 \sum_{e\in E_t}\frac1{e^{K+1}(e-1)}.
\end{aligned}
\tag{34}
$$

**Proof.** Apply (32) separately to every positive source and every negative source in the absolutely convergent expansion (24). A negative source reverses the direction of the bound. Grouping words by their terminal policy gives exactly (33)–(34). $\square$

Finite reciprocal-power sums are enclosed by integer division at scale $10^{80}$. Positive and negative coefficients use their respective outward directions. The final release uses $K=10$ and verifies containment within a separately recomputed $K=8$ interval. Thus the reported value is not a finite truncation of the set, a simulation of an unobserved tail, or an optimizer objective.

## 6.5. Independent calibration of the Walker sum

Digit-restricted reciprocal series have a substantial established computational literature [3]. Here the baseline is recomputed with an explicit leading-block partition. A short earlier implementation is useful for displaying the entire argument [S01–S03].

Write a Walker integer as $1+d+55v$. Take four padded digits for $v$ and $d\in D$, giving $21^5=4,084,101$ head terms. For a longer $v$, choose its unique nonzero leading four-digit block $u$, followed by $k\ge1$ digits. There are $20\cdot21^3=185,220$ possible leading blocks. Then $n=55^{k+1}(u+t)$, where $0\le t\le\theta=48/55$, and

$$
\frac1u-\frac t{u^2}\le\frac1{u+t}
\le\frac1u-\frac t{u^2}+\frac{\theta t}{u^3}.
\tag{35}
$$

The remainder is $t^2/[u^2(u+t)]$, which proves both inequalities. Put $p=21/55$, $\mu=21^{-1}\sum_{d\in D}d$, $q=\mu/54$, and $\eta=(\mu+1)/55$. Averaging the trailing digits gives $\mathbb E t=q+(\eta-q)55^{-k}$. Summing the geometric counts and first moments over all $k\ge1$ yields

$$
K_0=\frac{441}{1870},\qquad K_1=\frac{27830481}{308961400}.
\tag{36}
$$

The entire omitted tail is between $K_0\sum u^{-1}-K_1\sum u^{-2}$ and that quantity plus $\theta K_1\sum u^{-3}$. Directed integer floors enclose the finite head and these three finite prefix sums. This proves the early coarse enclosure

$$
4.43975336925447<\mathcal W(W)<4.43975336925458.
\tag{37}
$$

The later calibration uses a leading three-digit block, moments through order 10, 80 low-word lengths, and integer scale $10^{100}$ [S24–S25]. The standalone module `verify/walker_calibration.py` specializes this mathematics to the one fixed alphabet and recomputes the baseline, rather than reading it as a trusted constant. Each long integer still has a unique leading-block/low-word decomposition. The uncomputed positive tail after $H$ low-word lengths is bounded by

$$
\frac{21^2\cdot20}{55^2}
\frac{(21/55)^H}{1-21/55}.
\tag{38}
$$

Alternating finite expansions of $1/(u+t)$ give directed bounds for the computed lengths. This sharper enclosure lies inside (37) and is combined with (34), without rounding the common baseline to a printed decimal. Comparing successive constructions cancels or consistently bounds that common baseline, avoiding a false gain inferred from separately rounded displays.

## 6.6. Exact standalone calibration and predecessor comparison

For clarity, the earlier four-digit head argument in Section 6.5 is not an additional input dependency. The public acceptance path uses the following complete specialization. Its finite head is $n=1+d+55a$ for $a,d\in D$, comprising 441 integers whose shifted values have at most two base-55 digits, with zero padding permitted. Every remaining integer has a unique representation

$$
n=55^\ell u+v_w+1,\qquad \ell\ge0.
\tag{39}
$$

Here $w$ is a low word of length $\ell\ge0$, and $u$ is a three-digit block with nonzero highest digit. There are $N=20\cdot21^2=8,820$ such blocks and $u\ge55^2$. Set $t_w=(v_w+1)/55^\ell\in(0,1]$ and

$$
\begin{aligned}
L_{k,\ell}&=\sum_{|w|=\ell}55^{-\ell}t_w^k,\qquad L_{k,0}=1,\\
L_{k,\ell+1}&=55^{-k-1}\sum_{j=0}^{k}\binom{k}{j}
\left(\sum_{d\in D}d^{k-j}\right)L_{j,\ell}.
\end{aligned}
\tag{40}
$$

The recurrence follows directly from $t_{wd}=(t_w+d)/55$. For even $K$, finite geometric expansion gives

$$
\sum_{k=0}^{K-1}\frac{(-t)^k}{u^{k+1}}
\le\frac1{u+t}
\le\sum_{k=0}^{K}\frac{(-t)^k}{u^{k+1}}.
\tag{41}
$$

Indeed, the remainder after order $r$ is $(-t)^{r+1}/[u^{r+1}(u+t)]$, so its sign proves both inequalities. Multiplying by the positive low-word discounts and summing gives exact rational lower and upper bounds in terms of (40). The finite block sums $\sum_u u^{-k-1}$ are rounded outward by integer division at scale $10^{100}$, with their signs respected. The uncomputed lengths $\ell\ge H$ contribute at most (38), because each reciprocal is at most $55^{-\ell}/55^2$. Taking $H=80$ and $K=10$ independently reconstructs the narrow Walker enclosure in V1, of width less than $1.67\times10^{-33}$.

The predecessor witness is compiled and checked by the same generic carry algorithm, not accepted from its old numeric endpoint. Its three complete control closures contain 737,910, 737,910, and 737,917 states. Its order-8 signed correction is added to the newly calculated Walker interval. The final order-10 lower endpoint minus the recomputed predecessor upper endpoint yields (8). The expected fractions in `witness/expected_baselines.json` are output-equality controls only; they are not premises in either derivation [C1; V1].

# 7. Experimental development of the construction

The experiments in Sections 7, 9, and 10 are retained research history, not claims that C1 reproduces their searches. Only the supplied final and predecessor witnesses are in its acceptance path. Reported scan coverage, solver behavior, and intermediate optima depend on privately retained records.

## 7.1. Successive certified witnesses

Table 4 gives the principal recorded accepted milestones. A displayed threshold is a deliberately truncated strict lower bound; it should not be interpreted as the exact sum of that construction. The private source archives retain the historical endpoints and integer rules. C1 supplies and rechecks the final and predecessor witnesses only.

| Stage | Description | Strict lower threshold for $F_4$ | Source |
|:--|:--|--:|:--|
| 1 | First finite repair, 1 insertion and 2 deletions | 4.4402987157 | S01 |
| 2 | Joint finite repair, 77 insertions and 29 deletions | 4.4406225704 | S02 |
| 3 | First recurrent root law, 74 insertions and 27 deletions | 4.4411450124 | S03, S17 |
| 4 | Expanded recurrent law, 693 insertions and 224 deletions | 4.4414864658 | S03 |
| 5 | Shared-repair refinement, 724 insertions and 243 deletions | 4.4414973129 | S04 |
| 6 | Shared-repair expansion, 2,890 insertions and 524 deletions | 4.4416312481 | S04 |
| 7 | Conditional repair, 2,902 insertions and 519 deletions | 4.4416342256 | S05 |
| 8 | Cooperative two-point finite patch | 4.4416488737 | S13 |
| 9 | Repeated patch with cross-level repairs | 4.4416579401 | S16 |
| 10 | Joint withdrawal/restoration of infinite families | 4.4416580904 | S20 |
| 11 | Historical-pool joint exchange | 4.4416698697 | S21–S22 |
| 12 | Enlarged recursive pool | 4.4416711811 | S21–S22 |
| 13 | First digit-dependent finite outer patch | 4.4416714370 | S21–S22 |
| 14 | Final five-digit branch patch | 4.4416719015 | S21–S22 |
| 15 | Completed 60M harvest and finite restoration | 4.4416821160 | S23 |
| 16 | Three recurrent policies with fixed tables | 4.4416822459 | S24 |
| 17 | Joint three-policy table changes | 4.4416824701 | S25 |
| 18 | Depth-sensitive policy recipes | 4.4416825784 | S25 |
| 19 | Reoptimized transitions; four reachable policies | 4.4416826569 | S25 |
| 20 | New roots beyond 60M; final witness | **4.4416832003** | C1, V1 |

Table 4. Constructive history. Finite outer actions and globally repeated root rules are different mathematical objects; their counts are not interchangeable. Stage 3 is the saved intermediate root certificate, not the larger endpoint of S03.

## 7.2. Shared repair as a concrete mechanism

The decisive finite cooperative patch inserts $8577$ and $14627$ and deletes $17605,17615,17625$ from the then-current infinite baseline $C$. Its exact gain is

$$
\begin{aligned}
G_*&=\frac1{8577}+\frac1{14627}
-\frac1{17605}-\frac1{17615}-\frac1{17625}\\
&=\frac{133924666248781}{9142757707411384875}>0.
\end{aligned}
\tag{42}
$$

The complete new-progression list is

| Progression | Deleted term |
|:--|--:|
| $(4053,8577,13101,17625)$ | 17625 |
| $(4058,8577,13096,17615)$ | 17615 |
| $(4063,8577,13091,17605)$ | 17605 |
| $(13128,14627,16126,17625)$ | 17625 |
| $(13133,14627,16121,17615)$ | 17615 |
| $(13138,14627,16116,17605)$ | 17605 |

Table 5. The two insertions share exactly the same displayed three-deletion repair [S13].

For either insertion alone, its three baseline conflict supports are disjoint. Any repair retaining that insertion must pay at least

$$
c=\frac1{17605}+\frac1{17615}+\frac1{17625}
=\frac{37234583}{218629012875}.
\tag{43}
$$

Each individual reward is less than $c$, while their combined reward exceeds it. The displayed deletions attain the lower repair cost for the fixed pair. Thus joint profitability is proved, although neither global optimality nor the best possible pair among all integers follows.

A previous mixed-integer formulation made no branch-and-bound progress in a recorded 180-second continuation. Constraint feedback and fractional feedback did not resolve that bottleneck. A Boolean clause formulation with LP linearization disabled found the patch and finished with status `FEASIBLE`, not `OPTIMAL`. This is a successful engineering change on one instance, not a controlled theorem about general acceleration [S12–S13].

## 7.3. Repeating a repair is not automatically safe

Applying the pair and its planned deletions under the 21 digit maps produced 44 inserted points and 66 planned deletions including the original layer. Of 133 new progressions, one escaped the planned repair:

$$
(471720,3993756,7515792,11037828).
\tag{44}
$$

Deleting 11037828 repaired the first-level edit. Repeating the revised rule at every depth exposed 82 further conflicts. Seven old insertion families were withdrawn to destroy them jointly; deletion ancestry normalization removed 17 redundant rules. The resulting infinite construction had 2,897 insertion roots, 506 deletion roots, and threshold $4.4416579401$ [S16]. This episode is the operational meaning of feedback in the project: a measured failure changes the represented set and is followed by a complete new check.

The next exchange withdrew insertion roots 22405226 and 43201980 while restoring five deletion families, at roots 22412464, 22423375, 39632805, 43203124, and 43220432. Exact orbit pricing proved a further gain exceeding $0.00000015036049133549$ and gave $4.4416580904$ [S20]. These are whole-family changes, not finite point rewards.

## 7.4. Branch-dependent finite outer edits

Within the enlarged recursive law, component

$$
E_*=\{402003,408053\},\qquad R_*=\{346210,678960\}
\tag{45}
$$

was omitted beneath digits $\{0,1,5,10,39\}$. The loss in its conditional infinite mass was offset by coordinated finite outer insertions and restorations. The final S21/S22 construction had 3,186 finite outer insertions and 549 finite outer deletions, with sum between $4.44167190157105$ and $4.44167190157115$.

The conditional branch weight is

$$
\nu_d(n)=\sum_{x\in\mathcal O(n)}\frac1{T_d(x)}.
\tag{46}
$$

If $\nu_d(n)=\sum_{k\ge0}C_k(d)n^{-k-1}$, coefficient comparison gives

$$
C_k(d)=\frac{(54-d)^k+
\sum_{j<k}\binom{k}{j}C_j(d)\sum_{a\in D}(54-a)^{k-j}}
{55^{k+1}-21},\qquad C_0(d)=\frac1{34}.
\tag{47}
$$

The same positive remainder method used in (32) encloses every omitted depth. This earlier scalar conditional recurrence and the later matrix recurrence are consistent descriptions at different levels of generality. The discovery moments and the independent coefficient recurrence agreed in 126 conditional comparisons and six partition identities [S21–S22].

## 7.5. The completed 60M candidate screen

S23 completed four contiguous shards, $[1,15\text{M}]$, $(15\text{M},30\text{M}]$, $(30\text{M},45\text{M}]$, and $(45\text{M},60\text{M}]$, with 16, 89, 79, and 312 positive proposals. It tested 4,360,499 missing safe-residue candidates against its frozen enrichment seed. All 23 proposals from the earlier incomplete 50M–51.893M scan were reproduced; 288 proposals lay beyond the old stopping point.

The 496 proposals included 473 roots absent from the old pool, expanding the pool from 5,282 to 5,755. Reconsideration as complete infinite edits accepted 376 and rejected 97. The complete union catalog grew from 57,105 to 61,539 progression rows. The harvested recursive fallback had 3,544 insertion roots and 728 deletion roots; subsequent finite outer restoration gave the stage-15 bound in Table 4 [S23].

This is completion under a declared screening policy: one safe-residue insertion paid for by at most two larger deletions, against the specified seed. It does not exhaust arbitrary simultaneous insertions, every deletion budget, every residue class, or every recurrent language. The old statement that the search was capped at 200,000 described one earlier pool, not the later completed scan.

## 7.6. Re-entry into policies and joint recipe changes

S24 coupled the earlier branch winner, the harvested recursive law, and a restorative variant into three recurrent policies. The old winning branch behavior could then recur at deeper digit histories. The search checked 8,380 transition proposals including repeats and controls, passed 2,174 catalog screens, and made 32 incumbent updates. Its accepted gain was greater than $1.2991131235721\times10^{-7}$ [S24].

S25 changed the policies’ insertion and deletion tables as well as their transitions. A coupled three-policy pass examined 26,371 proposals and recorded 86 updates. A six-defined-policy depth split examined 43,010 proposals and recorded five updates. Transition reoptimization checked 21,514 proposals; the accepted language retained four reachable, inequivalent policies, with the two unreachable policies removed. A separate broad mixed-integer model with 71,616 variables and 238,968 rows retained its seed at a 150-second limit. The latter is not an optimality certificate [S25].

The gain from re-entry is therefore not evidence that a three-state digit-only automaton encodes the whole construction. The root tables are material information. Only the subsequent 1,384-state compilation incorporates that information into an ordinary automaton.

## 7.7. Roots outside the old catalog

The completed interval $[60000001,65000000]$ contained 363,637 eligible candidates under the saved safe-residue singleton policy. It produced 32 proposals requiring no local deletion and five paid proposals. The 32 were accepted jointly; the five paid proposals were accepted sequentially after full infinite checking and positive exact gain tests. They add seven listed deletion rules [S25]. All 37 insertion roots are outside the old 5,755-root pool and are enumerated in Appendix D.

The new rules are assigned to the relevant recurrent policy. They apply at digit histories reaching that policy; they are not indiscriminately copied into every branch. Their combined additional gain over the reoptimized within-pool grammar exceeds $5.4338333493787\times10^{-7}$. The final compilation and generic product proof verify the entire resulting language again. The old catalog is retained for its own benchmark and intermediate stages, not improperly reused to certify these new roots.

# 8. Exact exclusions and their mathematical boundaries

## 8.1. A mass obstruction for a frozen universe

For any finite pool $P$ of roots greater than one and any policy or history-dependent construction $A\subseteq U(P)$, the analytic envelope is

$$
\mathcal W(A)\le\mathcal W(U(P))
<\mathcal W(W)_{\mathrm{upper}}+\frac{55}{34}\sum_{e\in P}\frac1{e-1}.
\tag{48}
$$

**Proof.** Include every insertion orbit, remove no points, and ignore every progression conflict. This only increases the possible mass. Apply the orbit bound (26) and sum over the finite pool. No computation of a particular pool is needed for this general inequality. $\square$

**Recorded numerical specialization (S24; outside public replay).** For the old 5,755-root pool, the private exact evaluation of the right-hand side begins $4.44541006081315550036989498597275$, giving a ceiling below $4.445411<5.1$. Earlier S06 records a tighter-moment ceiling below $4.445068$ for its 5,257-root pool. These numerical specializations are conditional on the identified frozen pools, which C1 does not distribute or replay. They are not upper bounds on $F_4$ and are not used in Theorem 2.1. The old numerical ceiling is not transferred to the enlarged S25 pool containing 37 additional roots.

## 8.2. A general deletion-cost certificate

Let $I$ be a proposed insertion set and $C$ a retained baseline. Each progression in $C\cup I$ meeting $I$ requires a deletion from its baseline support $Q_e=e\setminus I$. If supports $Q_{e_1},\ldots,Q_{e_k}$ are pairwise disjoint, then every valid deletion set $J$ satisfies

$$
\mathcal W(J)\ge\sum_{i=1}^k\frac1{\max Q_{e_i}}.
\tag{49}
$$

Each support requires at least one deletion, and its largest point is the cheapest possible one. Disjointness prevents charging one deleted point twice. More generally, nonnegative rational multipliers $y_e$ satisfying

$$
\sum_{e:d\in Q_e}y_e\le\frac1d
\quad\text{for every baseline point }d
\tag{50}
$$

give $\mathcal W(J)\ge\sum_e y_e$ by summing the mandatory support-hitting inequalities. Only genuine necessary conflicts are needed; the row collection need not be complete for this upper-exclusion use.

## 8.3. Scope of the bounded-insertion record

The numerical optimum formerly labeled Theorem 8.1 is retained as a recorded S15 result in Appendix B.6, rather than as a theorem replayed by this public supplement. Its complete computational argument requires exhaustive subset coverage, exceptional-subset duals, the frozen baseline, and primal feasibility. The 4,008 dual certificates alone do not establish that every other subset was excluded. None of those private numerical artifacts is required to prove the main lower bound or the predecessor comparison. The general deletion-capacity arguments in Section 8.2 remain fully stated mathematical facts.

## 8.4. Spacing and restoration exclusions

The following numerical exclusions are recorded from S18–S19, not replayed by C1. Their displayed necessary-conflict arguments illustrate the exact certificates used historically; the withheld baseline and coverage data are not inputs to Theorem 2.1.

Against the later 2,897-root/506-deletion baseline, S18 exactly excludes 14,526 safe-residue singleton insertions and 126,613 pairs at nine specified spacings through 200,000. All singletons and all but one pair are excluded by (49). The remaining pair, $I=\{55712,55822\}$, has four necessary conflict supports. Exhaustive enumeration of at most $3^4$ choices gives the cheapest cover $\{54701,54716\}$, with

$$
\Delta\mathcal W\le\frac1{55712}+\frac1{55822}
-\frac1{54701}-\frac1{54716}
=-\frac{42490077697}{61237881861980512}<0.
\tag{51}
$$

The successful earlier gap $14627-8577=6050=2\cdot55^2$ therefore does not guarantee another profitable pair.

S19 tests the 16 deleted Walker roots at most 200,000 that the safe-residue insertion pool omitted. Their necessary conflicts split into components with disjoint baseline deletion supports. Exact minimum-cover enumeration excludes every nonempty restoration subset within each component and therefore every restoration-only union of those components. A further 1,091-cover experiment finds no positive raw-gain candidate union. That latter cover-template experiment is not an exhaustive exclusion of all possible joint restoration and insertion actions.

## 8.5. Stacking requires cross-block proof

Large separation alone does not preserve progression-freeness: $\{1\}$ and $\{10^9+1,2\cdot10^9+1,3\cdot10^9+1\}$ are separately four-free, but their union is a progression.

A sufficient interval condition is the following. If $B_1\subseteq[1,M]$, $B_2\subseteq[L,U]$, $L>2M$, and $U<3L-2M$, and both blocks are four-free, then their union is four-free. A crossing progression with at least two lower terms cannot reach $L$; one with one lower term $a$ and first upper term $y$ has last term $3y-2a\ge3L-2M>U$. This proves the assertion [S09].

The privately retained S10–S11 computations, which C1 does not replay, record the following exclusions. Eight repaired fixed-block trials in S10 had raw mass below $4.126976343$, so no deletion strategy for those particular blocks could improve the incumbent. S11 considered all 4,096 adjacent cuts of a specified million-point-horizon template. Raw mass excluded 3,933 cuts. For the remaining 163, disjoint upper-support progression packings gave compulsory deletion costs via (49); their largest repaired upper certificate was below $4.277589103$. The latter numerical ceiling applies only to those 163 qualified cuts, while the other cuts have their individual raw exclusions. None of these statements excludes general stacking, alternative upper blocks, or joint changes to the lower block.

# 9. Alternative representations and hypotheses

## 9.1. Small automata and all-digit experiments

S20 implemented two-state digit-only generators. S23 generalized the search to three and four live states, enforcing reachability and inequivalence rather than counting redundant representations of Walker’s set. Eight time-limited runs made 2,161,018 proposed mutations, including repeats. The best saved genuine three-state and four-state sums were approximately $4.438383692542405$ and $4.439749664081650$, respectively, below the incumbent. All 16 saved selections received independent carry checks and exact infinite enclosures; 1,060 control comparisons passed. These are negative results for the executed searches, not complete exclusions of the automaton classes [S20; S23].

The earlier five changed digits were an observed outcome, not a hard branch-count cap. S23 exposed all $21\cdot2904=60,984$ component-continuation choices in the certified ordinary alphabet. A separate all-55 experiment selected any outer digit subset $U\subseteq\{0,\ldots,54\}$ in

$$
A(U)=\bigcup_{d\in U}T_d(W).
\tag{52}
$$

It generated 1,430 forbidden-digit constraints from 23 completable carry states, each with a concrete progression witness. An independent forward computation regenerated the constraints and all branch-weight intervals. The numerical optimizer retained the old 21-digit alphabet. Its `Optimal` floating-point status is not an exact rational or global optimum theorem. This family also lacks the incumbent’s exception tables and does not represent every possible 55-digit recurrent grammar [S23].

Opening each of the other 34 digits as a whole additional branch gave a concrete progression; examples are $(4,11,18,25)$ for digit 3 and $(6,8,10,12)$ for digit 7. S25 went beyond whole-digit openings and tested 144 conditional dead-to-live DFA changes sampled from 14,361 eligible placements. All 144 produced counterexamples, with no timeout. These trials reject the actual tested changes, not all conditional openings.

## 9.2. The arithmetic “middle” and quasiperiodicity

Every positive nonconstant four-term progression has the unique representation

$$
(2u-v,u,v,2v-u),\qquad u<v<2u.
\tag{53}
$$

Indeed, its middle pair is $u=a+h$, $v=a+2h$, and conversely these inequalities give positive first term and positive difference. Two overlapping three-term progressions thus share the central pair. This identity supplies a conflict representation, not a geometric theorem about a physical crystal.

The project’s useful combination was to place insertion decisions, repair choices, and digit-history transitions in one recurrent grammar. A convex average of three old scalar scores cannot exceed their maximum; a new underlying set is required. Equation (5), rather than a numerical barycenter, is the substantive mathematical combination [S24].

A literal irrational-rotation window need not be progression-free. Let $\alpha=(\sqrt5-1)/2$ and $B=\{n\ge1:\{n\alpha\}<1/2\}$. Then $(2,10,18,26)\subset B$. An elementary exact check uses $2.236<\sqrt5<2.237$, obtained by squaring rational endpoints. It gives $0.618<\alpha<0.6185$; the four products lie respectively in $(1.236,1.237)$, $(6.18,6.185)$, $(11.124,11.133)$, and $(16.068,16.081)$. Their fractional parts are all between zero and one half. The model-set literature likewise cautions against identifying quasiperiodicity with avoidance of arithmetic progressions [4].

S24 instead tested 32 aperiodic *digit-depth schedules*, selected by $\lfloor(j+1)\alpha+\theta\rfloor-\lfloor j\alpha+\theta\rfloor$, combining $D$ with affine modularly four-free alphabets. Such schedules are safe by digit descent. The best certified sum was approximately $4.415972700244811028$, below the benchmark. No golden-ratio advantage, physical mechanism, or exhaustive aperiodic optimum is established.

## 9.3. Periodic alphabets and fixed shifted tails

Earlier stationary and alternating digit searches also found no improvement. They did produce a concrete distinction between modular sufficiency and full carry verification: the alternating base-5 alphabets $\{0,2\}$ and $\{0,1,2,4\}$ give a four-free integer set, although the corresponding base-25 alphabet contains a modular progression. Its sum is only about $2.35872903908536577097$ [S07].

If a periodic digit alphabet admits a modular progression and the next alphabet contains $0,1,2$, an ordinary progression can be completed in the next digit. To see this, reverse the modular progression if needed so its difference is at most $b/2$; its integer representatives then lie below $3b$, and the next digits lie in $\{0,1,2\}$. Hence a stationary alphabet containing $0,1,2$ must be modularly four-free. Omitting small digits to escape that restriction can be expensive in reciprocal weight.

For every shift $1\le q\le512$, S07 also certifies that retaining the entire fixed tail $q+\mathcal K(D,55)$ and adding any permissible head below $q$ cannot exceed $4.43975336925454064867$. A carry test identifies head points incompatible with three tail points; giving every remaining eligible head point its full reward is already below the incumbent. This is an exact exclusion of those fixed-tail families, not an exclusion of tail deletions or larger shifts.

## 9.4. Prime patterns and chamber-derived proposals

The factorization audit covers 3,571 distinct roots in eight complete milestones. Reference populations condition on size and residue, and separately on nearby digit context. It does not show consistent prime enrichment. For the then-current 2,897 insertion roots, 182 were prime, compared with a size/residue reference expectation of 196.60. Observed divisibility by 29 among some deletion cohorts was exploratory and did not provide an independently replicated predictive advantage [S17].

The imposed safe residues imply $n\equiv8\pmod{11}$ for insertion roots; roots in one of the four residue classes are divisible by 5. These imposed features must not be mistaken for discovered prime effects. Prime status is not preserved by the digit maps: $T_1(14627)=804432$ is composite. If $29\mid n$, then $T_d(n)\equiv d+4\pmod{29}$, and none of the allowed digits yields divisibility by 29. Root statistics therefore do not automatically describe descendants.

The chamber-coordinate experiment mapped four numerical coordinates into arithmetic proposal controls and compared equal proposal budgets with scrambled-coordinate, uniform-coordinate, and ordinary randomized-priority baselines. It generated 6,144 candidates across six bases. Its best certified outcome, about $4.29316769210005$ in base 83, did not improve the incumbent. The matched-feedback comparisons did not establish a specific physical or element-grounded predictive benefit. Coordinate normalization, physical labels, and arithmetic validity are separate questions [S08]. The related Hassium proposal report is retained as background B04, not as a physical premise of any theorem here.

# 10. What the frontier pass rejected

The final certificate became less dependent on its discovery assumptions precisely because finite-prefix successes can be misleading. S25 screened 185,421 missing candidates through 300,000 outside the old pool against a longer finite prefix and found no positive singleton. A near-miss screen produced 78 records and 37 apparently profitable pair or triple proposals. Three targeted experiments involving root 98992 and a possible repair at 89920 became nonpositive after complete infinite checking.

For example, inserting 98992 creates

$$
(98992,179095,259198,339301),
\tag{54}
$$

which extends beyond a naive 300,000 membership window. This is why an attractive finite-prefix objective cannot be accepted as the actual infinite gain. The failed trials are retained in S25’s outside-pool ledger with their witnesses and costs.

The safe-residue screens, heuristic mutation counts, and solver time budgets describe where candidates were proposed. They do not define the correctness criterion. The final candidate is accepted only after its complete DFA is compiled, every reachable product state is exhausted, active deletions are recomputed, and the exact infinite weight interval is obtained.

# 11. Verification, reproducibility, and archival integrity

## 11.1. Standalone verification and author-side replay

Extract C1 and run from its root directory:

```sh
python3 -O verify.py --output runs/verification.json
```

The acceptance path requires Python’s standard library and a C++17 compiler, not an optimizer, network service, or previous research archive. It checks the immutable payload manifest, recompiles the defining grammar and compares the supplied DFA, exhausts the arithmetic-carry products, and recomputes exact state-conditioned moments with explicit remainder bounds. The four final control closures contain 801,373, 801,373, 801,373, and 801,382 states. The predecessor closures contain 737,910, 737,910, and 737,917 states. The fixed-alphabet Walker calibration and both exact reciprocal enclosures are recomputed; stored expected endpoints are only comparisons of independently derived outputs.

The certificate’s own `validation/build_replay.json` and `validation/build_replay.log` are the author-side, AI-assisted replay record [V1]. This is the documented execution cited for the standalone mathematical result, not an unarchived assertion that another system ran it. The record reports PASS, the exact endpoints of Theorem 2.1, and its certified gain. It reports Python 3.13.5 and g++ 14.2.0; its timing is an observation of that execution, not a promised runtime. Recorded logs are not accepted instead of fresh computation: the command above computes new results.

The checks under `independent/`, with their recorded outputs in `validation/secondary_replay.json` and `validation/secondary_replay.log`, are cross-implementations, not peer review [V2]. The secondary carry implementation exhausts the same 801,373-state main closure. Its optional floating-point weight calculation is a numerical consistency control, not an exact enclosure. The primary verifier itself includes 52 Python/native carry controls, 72,000 compiler-fixture comparisons, 61,732 actual-witness policy/integer comparisons, and the deletion-1360 rejection control. These roles are not interchangeable.

C1 verifies the final mathematical witness and the supplied predecessor comparison. It does not replay historical scan coverage, reproduce search efficiency, or establish the S15 eight-insertion optimum. Outputs belong under `runs/` or outside the package so repeated execution does not alter the immutable-input manifest.

## 11.2. Why archive repair belongs in the scientific record

The original S21 digit-branch archive was damaged: its closing ZIP directory was absent, a progression JSON record was truncated, advertised verifier files were missing, and several paths were incorrect. A partial recovery preserved 57 intact files but was not a complete repair. The S22 replacement restored verifier sources from ancestor releases, rebuilt the missing wrapper, regenerated the complete 57,105-row catalog, corrected paths, and supplied checksums. The regenerated catalog agreed with every surviving byte of the partial original [S21–S22; S26].

This was a packaging failure, not evidence of a mathematical counterexample. Nevertheless, the damaged package could not support its advertised reproducibility until repaired. The original and repaired archives are retained privately as provenance records. C1 does not depend on the damaged ZIP, reconstructed catalog, or any earlier archive: it rebuilds the final proof from its local witnesses. This repair narrative is historical provenance, not a public acceptance dependency.

## 11.3. Independence and trust boundaries

The private research record contains several kinds of cross-checks, including catalog enumeration versus discovery clauses and conditional moments versus coefficient recurrences. The public acceptance path retains grammar/DFA comparisons, native/Python carry controls, exact moment calculations, and optional secondary implementations. They share definitions or inputs and reduce particular implementation risks; they are not independent peer review or validation of historical priority. A replay is attributed only when its execution record is included and examined.

The computational proofs still rely on the stated algorithms, their implementations, the execution environment, and the supplied finite data. Hashes identify bytes and reveal accidental changes; they do not prove mathematical correctness by themselves. Resource exhaustion is a failed proof attempt, not a negative theorem. Regression tests supply deliberately false controls, not a proof that every possible software defect is absent.

# 12. Discussion and conclusion

The final language improves Walker’s starting construction by approximately $0.001929831095$ in reciprocal mass. The increase over the immediately preceding three-policy witness is about $9.54391838\times10^{-7}$. Those magnitudes should be reported plainly. The numerical target $5.1$ remains separated from the accepted construction by approximately $0.65831679965047$; no argument in this paper bridges that gap.

The main structural lessons are specific. Shared deletion supports can make a pair profitable when each singleton is not. Copying a useful pattern through digit maps introduces new cross-level obligations. State-dependent rules can improve the available tradeoffs, but additional state names are not useful unless their languages are reachable and inequivalent. A complete finite automaton is a broader certificate interface than a fixed root catalog. Finally, signed indicator recurrences are needed once repair rules overlap or remove inserted-root descendants.

The old fixed-pool ceiling explains why rearranging the same represented universe cannot reach $5.1$. It does not prove that $5.1$ is impossible for a different family. The final language leaves the old pool but retains the ordinary alphabet and finite recurrent exception framework. Its successful new roots do not establish that unrestricted all-digit, mixed-base, or arbitrary finite-state constructions have been optimized.

The paper therefore establishes an explicit computer-assisted lower bound, supplies a standalone replay of that certificate and its predecessor comparison, and records the methodological development, historical exclusions, and unsuccessful hypotheses. It does not establish finiteness of $F_4$, global optimality, the Erdős–Turán conjecture, a general advantage for quasicrystal or chemical proposals, or a universal mathematical solver. The public supplement’s mathematical claims are traceable to its explicit witnesses and verifier. Privately retained historical numerical statements are labeled separately and are not needed by the main proof.

# Appendix A. Earlier auxiliary results and complete proofs

## A.1. Exact optimum in the 2–3-smooth chamber

Let $\mathcal S=\{2^i3^j:i,j\ge0\}$ and let $M_4(\mathcal S)$ be the maximum reciprocal mass of a four-term-free subset of this specified domain. Its total mass is three. This is a restricted-domain problem, not the unrestricted problem (1).

**Lemma A.1.** Every nonconstant four-term progression in $\mathcal S$ is $(g,2g,3g,4g)$ for some $g\in\mathcal S$.

**Proof.** Divide the progression $a,a+d,a+2d,a+3d$ by $\gcd(a,d)$. Its terms remain 2–3-smooth and now $\gcd(a,d)=1$. If $d$ is even, all terms are odd powers of 3. Coprimality implies $a=1$, but the third term $2\cdot3^r-1>1$ is not a power of 3. Thus $d$ is odd. If $3\mid d$, all terms are powers of 2; coprimality again gives $a=1$, and the third term is odd and larger than one, a contradiction. Thus $3\nmid d$.

The two odd terms are powers of 3 and differ by $2d$. They cannot both be divisible by 3, so one is one. Positivity makes this the first term, giving $a=1$. Since $1+2d=3^r$, we have $d\equiv1\pmod3$. The other two terms are therefore powers of 2: $1+d=2^u$ and $1+3d=2^v$, with $v>u\ge1$. Subtraction yields $2^v-3\cdot2^u=-2$. The factor in parentheses after taking out $2^u$ is odd, so $u=1$, and hence $d=1$. Restoring the common divisor proves the classification. $\square$

**Theorem A.2.** $M_4(\mathcal S)=18/7$, and the optimum is attained.

**Proof.** Let $z_{i,j}$ indicate deletion of $2^i3^j$. Lemma A.1 gives

$$
z_{i,j}+z_{i+1,j}+z_{i+2,j}+z_{i,j+1}\ge1.
\tag{55}
$$

Select rows with $i=3r$ and assign multiplier $\lambda_{r,j}=1/(4\cdot8^r3^j)$. Relative to each point’s reciprocal weight, the incident loads are $1/4$ at $(3r,0)$, one at $(3r,j)$ for $j\ge1$, $1/2$ at $(3r+1,j)$, and one at $(3r+2,j)$. Thus the load never exceeds the point’s reciprocal cost. Summing (55) gives excluded weight at least

$$
\sum_{r,j\ge0}\lambda_{r,j}
=\frac14\frac1{1-1/8}\frac1{1-1/3}=\frac37.
\tag{56}
$$

Finite partial sums followed by monotone convergence justify the infinite dual. Hence retained mass is at most $3-3/7=18/7$.

Conversely, retain exactly the points with $i\equiv0$ or $1\pmod3$. Every classified progression contains three consecutive powers of 2 in its exponent pattern and therefore loses one point. The retained mass is

$$
\frac{1+1/2}{1-1/8}\frac1{1-1/3}=\frac{18}{7}.
\tag{57}
$$

This proves equality and attainment. $\square$

The argument predates the present construction and is credited to the P0 manuscript, with a recovered explicit dual in S01. Its finite controls checked 1,106 incidence loads and 975 progressions in a 1,066-point smooth-number rectangle, and rejected an inflated multiplier. Those finite controls support implementation consistency; the classification and infinite dual prove the theorem.

## A.2. Why independent chambers do not give a uniform global bound

Every positive integer has a unique form $m2^i3^j$ with $\gcd(m,6)=1$. Consider the relaxation imposing only the classified progression constraints separately within these multiplicative chambers. Giving each chamber its full infinite budget from Theorem A.2 bounds its truncated reciprocal optimum above by

$$
\frac{18}{7}\sum_{\substack{m\le N\\(m,6)=1}}\frac1m
=\frac67\log N+O(1).
\tag{58}
$$

The matching logarithmic coefficient is attained in the relaxation by retaining all integers whose 2-adic valuation is 0 or 1 modulo 3. Its reciprocal sum through $N$ is

$$
\sum_{\substack{i\ge0\\i\equiv0,1\ (3)}}2^{-i}
\sum_{\substack{u\le N/2^i\\u\text{ odd}}}\frac1u
=\frac67\log N+O(1).
\tag{59}
$$

The bounded error follows from convergence of $\sum_i i2^{-i}$ and the odd harmonic-sum estimate. This relaxation therefore diverges logarithmically. Its matching set is not four-term-free in the full integers; for example it contains $(1,5,9,13)$. Cross-chamber constraints cannot be discarded. This earlier obstruction is retained from B01 and is consistent with, but different from, the constructive lower bounds in the main text.

## A.3. A positive-row-ratio obstruction

**Proposition A.3.** Suppose a continuous relaxation on $[0,1]^N$ consists of rows $\sum_i a_{ri}^{(N)}x_i\le b_r^{(N)}$ with nonnegative coefficients, positive coefficient sum for every nonzero row, nonnegative right-hand side for zero rows, and

$$
\eta=\inf_{N,r:\sum_i a_{ri}^{(N)}>0}
\frac{b_r^{(N)}}{\sum_i a_{ri}^{(N)}}>0.
\tag{60}
$$

Writing $\delta=\min(1,\eta)$, the relaxation’s reciprocal objective is at least $\delta H_N$ and therefore cannot yield a bound independent of $N$.

**Proof.** The constant vector $x_i=\delta$ satisfies every row and the unit bounds. Its reciprocal objective is $\delta\sum_{i=1}^N1/i$. Equivalently, any nonnegative dual covering the reciprocal weights has cost at least $\delta H_N$, by multiplying its coverage inequalities by $\delta$ and using $b_r\ge\delta\sum_i a_{ri}$. $\square$

Adding rows, taking nonnegative combinations, or repricing at different horizons does not evade this obstruction while the positive lower row ratio remains. Auxiliary variables, nonlinear constraints, or additional integral structure require a new analysis. The proposition does not assert that the integral four-term-free problem has a constant-density feasible solution [S01; B03].

## A.4. Profitable singleton edits of the unedited Walker set

Suppose a missing safe-residue point $n$ is inserted into $W$ alone. It cannot be the first term of a new progression. Every relevant conflict point is below $3n$, and deleting a point at most $n$ already costs at least the insertion reward. Every useful deletion therefore exceeds $n$ and costs more than $1/(3n)$. Three such deletions are unprofitable. Hence a positive singleton edit against this *unedited Walker baseline* has a repair with at most two larger deletions [S02].

For a two-point cover, select one point from an uncovered conflict. The second must lie in every remaining uncovered conflict; choosing the largest point in that intersection minimizes reciprocal cost. This supplies a complete small hitting-set procedure in the stated class. The lemma is not automatically valid for a later seed containing larger unscaled insertion roots, where a first-position insertion may interact with a distant exceptional point. The later two-deletion scans are expressly described as screening policies.

## A.5. A simple recurrence amplification bound

For disjoint one-policy insertion and deletion orbits, put

$$
g(t)=\sum_{e\in E}\frac1{e-1+t}-\sum_{r\in R}\frac1{r-1+t},
\qquad G=g(1).
\tag{61}
$$

If $\sum_e e^{-2}-\sum_r(r-1)^{-2}=\Delta>0$, then $g'(t)\le-\Delta$ on $[0,1]$, so $g(t)\ge G$. At digit depth $j$, each word contributes $55^{-j}g((v+1)/55^j)$ and there are $21^j$ words. Absolute convergence gives

$$
\mathcal W(C)-\mathcal W(W)\ge\frac{55}{34}G.
\tag{62}
$$

For the 693-root construction, the recorded values are $G\approx0.0010706588777723963$ and $\Delta\approx0.000003034982217902689$. This explains a provable amplification of a compatible edit pattern. Compatibility must first be established by the full progression check. The sharper moment enclosure used in its accepted result includes the variation of $g(t)$ rather than replacing it by $G$ [S03].

# Appendix B. Detailed experiment and exclusion ledger

This appendix records historical computations from the private S01–S26 archive. Except where a final or predecessor witness is explicitly linked to C1, these rows are not replayed by the public certificate. Recorded coverage and search outcomes must not be read as public reproduction claims.

## B.1. Candidate pools, search objectives, and coverage

| Release | Declared search or certificate | Recorded outcome and scope |
|:--|:--|:--|
| S01 | Nine first-digit/tail combinations in bases 11, 22, 55; 1,454 safe-residue candidates through 20,000 | No digit-combination improvement; the repair at 492 was the only positive singleton under the stated cover rule. |
| S02 | All 72,727 safe-residue candidates through 1M against Walker | 85 positive singleton offers, 57 requiring no deletion. Joint model: 85 insertion choices, 95 deletion choices, 52 clauses; accepted 77/29 finite patch. |
| S03 | Recursive feedback and extension through 10M | Final joint pool: 989 insertions, 3,250 possible deletions, 3,744 clauses. Accepted 693/224 recursive law. |
| S04 | Shared-cost feedback; restricted scan through 50M | 3,635,670 missing candidates tested; 4,245 positive local offers. Pool 5,257; 56,303 union conflicts; accepted 2,890/524 law. |
| S05 | Alternating deletion minimization, insertion changes, joint Hamming-24 neighborhoods | Ninety-second subproblems; accepted 2,902/519 law. Numerical solver statuses not exact global optima. |
| S12 | Full infinite baseline with 1,453 new finite insertion choices through 20,000 | 4,719 possible deletions; 305,707 progression clauses. Time-limited full and neighborhood MIPs found no positive edit. |
| S13 | Boolean reformulation of the same 305,707 clauses | Positive shared pair; 388,310 reported branches; final status FEASIBLE. Exact patch verified independently. |
| S14 | Deletion-first and optional-deletion neighborhoods through 100,000 | 22,870, 64,377, and 84,334 fixed-template passes; 14,505 optional neighborhoods, 69 optimized. No improvement; counts overlap. |
| S15 | All insertion subsets of size at most eight in the 7,262-point frozen pool | Exact optimum $G_*$; 4,008 rational dual certificates after rigorous pruning. |
| S18 | All safe singletons and nine selected pair spacings through 200,000 | 14,526 singleton and 126,613 pair exclusions, with exact repair bounds. |
| S19 | Sixteen restored low deletion roots; then 1,091 repair templates | Restoration-only subsets excluded exactly; no combined template passed the raw-gain screen. |
| S21–S22 | Historical-pool exchanges, broader pool, and digit-specific finite outer edits | Broad discovery pool 19,780 roots; 40,431,882 union witnesses. A 6,336-root shortlisted search did not improve its seed. Accepted smaller-pool branch witness verified. |
| S23 | Four complete scan shards through 60M | 4,360,499 candidates; 496 offers; 473 new pool roots; 376 accepted infinite additions after rechecking. |
| S24 | Recurrent transitions with three fixed recipes | 8,380 checks, 2,174 catalog-screen acceptances, 32 incumbent updates; accepted stage-16 witness. |
| S25 | Joint recipe changes, transition changes, and 60M–65M harvest | Four reachable final policies; 37 outside-pool roots accepted; generic infinite verification replaces fixed-catalog acceptance for the new roots. |

Table B1. These rows concern different baselines, objectives, horizons, and proposal policies. Their counts must not be added as independent or distinct constructions.

## B.2. Exact selected-spacing exclusions

| Spacing | Candidate pairs | Profitable pairs |
|--:|--:|--:|
| 6,050 | 14,069 | 0 |
| 5,995 | 14,072 | 0 |
| 6,105 | 14,064 | 0 |
| 5,940 | 14,076 | 0 |
| 6,160 | 14,060 | 0 |
| 3,025 | 14,288 | 0 |
| 9,075 | 13,852 | 0 |
| 12,100 | 13,633 | 0 |
| 110 | 14,499 | 0 |
| **Total** | **126,613** | **0** |

Table B2. The S18 baseline is the 2,897-root/506-deletion construction. This table is not an exclusion of all pairs or of later recurrent grammars.

## B.3. Affine digit-family certificates

S06 enumerated 90,515 distinct zero-containing affine images of ten recorded seed alphabets, each used as an outer digit layer over the fixed Walker tail. Upward-rounded rational branch weights gave the following actual finite-family upper certificates.

| Base | Distinct images | Certified family upper bound |
|--:|--:|--:|
| 11 | 12 | 4.428942015438537 |
| 22 | 10 | 4.424993279167750 |
| 55 | 42 | 4.439753369254551 |
| 97 | 99 | 4.397574700113050 |
| 121 | 3,960 | 4.425529881017356 |
| 157 | 6,708 | 4.391333889789773 |
| 177 | 5,336 | 4.391802971595314 |
| 191 | 9,500 | 4.405164597033458 |
| 193 | 9,408 | 4.390303750134873 |
| 605 | 55,440 | 4.437335061051435 |

Table B3. These ceilings apply only to the enumerated affine images and their specified tail. The separate 30 integer alphabet searches and 12 heterogeneous-child searches were not exhaustive. An imported base-105 seed containing $(1,9,17,25)$ was rejected before contributing any accepted result.

## B.4. Alternative digit and block outcomes

| Experiment | Coverage | Best recorded result or exclusion |
|:--|:--|:--|
| Stationary and alternating digits, S07 | 36 bounded searches; 42 saved records, 40 descriptions; 847 carry controls | Best stationary selection reproduced Walker; best alternating selection approximately 4.42174753239823. |
| Fixed shifted tails, S07 | All shifts 1–512, retaining the entire shifted tail | Every declared head-plus-tail family below 4.43975336925454064867. |
| Chamber-coordinate proposals, S08 | Six bases, eight repeats, 32 proposals per method; four methods | 6,144 candidates; best about 4.29316769210005. No demonstrated chamber-specific predictive benefit. |
| Composite bases, S09 | Bases 115, 185, 385; 1,536 heuristic attempts | Largest found alphabets 31, 45, 75 digits; best Walker-tail hybrids about 4.248344993, 4.199245088, 4.108250792. |
| Fixed-block stacking, S10 | Eight block pairs | Best repaired finite union about 4.1047115437; raw mass ceiling below 4.126976343 for all eight. |
| Adjacent gated stacking, S11 | All 4,096 cuts; 163 passed raw mass gate | Remaining cuts excluded by disjoint-support repair packings; qualified-family repaired ceiling below 4.277589103. |
| Two-state digit-only generators, S20 | Four initialization policies; 1,668,501 mutations; 672 controls | Best genuinely different-alphabet saved sum about 4.435010089881478; no improvement. |
| Three-/four-state digit-only generators, S23 | Eight runs; 2,161,018 mutations; 1,060 controls | Best genuine saved sums 4.438383692542405 and 4.439749664081650. |
| Aperiodic digit-depth schedules, S24 | Eight non-Walker affine alphabets at four rational phases | All 32 rigorously priced; best about 4.415972700244811028. |
| Conditional DFA openings, S25 | 144 trials among 14,361 eligible placements | Every tested opening rejected by a concrete progression; no timeout. |

Table B4. Approximate best values describe recorded candidates, not maxima over unexhausted mathematical classes. Exact family exclusions are explicitly identified as such.

## B.5. Source-specific details retained outside the tables

The early full incremental finite-edit model had 26,323 rows containing one new candidate, 496 containing two, 103,705 containing three, and 175,183 containing four. Their sum is 305,707. Candidate–candidate interactions therefore constitute most of that model; checking only isolated insertions would miss them [S12–S13].

The uncapped S23 continuation model had 5,755 outer insertion choices, 8,261 finite deletion choices, 59,248 clauses, and all 60,984 component decisions, of which 176 were clause-active. A subsequent complete coordinate sweep over 213 relevant choices found no beneficial single flip. That coordinate-local conclusion is not a multi-coordinate optimum.

The S17 prime audit uses eight complete milestone lists and marks first appearances separately. Repeated survival across snapshots is not independent replication. Its sieve-based reference computations extend through 134,217,727 and include 1,694,763 Walker integers for the size/residue controls. Those controls do not condition on every possible progression-feasibility feature. Divisibility-by-29 comparisons remain descriptive rather than significant, causal, or prospective predictive tests.

Detailed per-run seeds, time limits, discovery candidates, root-list differences, and original search records remain in the private source reports and archives. C1 contains only the explicit witnesses and computations required for the final theorem and predecessor comparison. These historical tables neither distribute discovery records nor claim to reproduce their coverage.

## B.6. Recorded bounded-insertion result (S15; not replayed in the public supplement)

The private S15 archive records the following result. Freeze the S05 recursive baseline $C$ with 2,902 insertion roots and 519 deletion roots. Let

$$
P_{100}=\{p\le100000:p\notin C,\ (p-1)\bmod55\in S\},
\qquad |P_{100}|=7262.
\tag{63}
$$

**Recorded historical statement, formerly Theorem 8.1.** The private certificate reports, conditional on the specified four-term-free baseline $C$,

$$
\max_{\substack{I\subseteq P_{100},\ |I|\le8\\J\subseteq C\text{ finite}\\(C\setminus J)\cup I\text{ four-free}}}
\bigl(\mathcal W(I)-\mathcal W(J)\bigr)=G_*.
\tag{64}
$$

There is no cardinality or location restriction on $J$. The maximizing example is the pair and deletion triple in (42)–(43) [S15].

**Recorded certificate structure (not a public replay).** The lower bound is the explicit valid patch of Table 5. For the upper bound, the search tree uses (49): a prefix of insertion reward $R$, certified repair cost $L$, at most $k$ remaining choices, and remaining candidates at least $a$ has final gain at most $R+k/a-L$. Directed integer rounding yields valid pruning at scale $10^{18}$. A second implementation at scale $10^{15}$ reproduces the exceptional subsets.

For insertion cardinalities 1 through 8, the respective unpruned subset counts are $0,1,0,7,51,195,886,2868$. All 4,008 remaining subsets have rational dual certificates satisfying (50), comprising 105,921 positive-weight progression rows. Each dual proves gain at most $G_*$. The pair attains equality. Verification checks all memberships, progression identities, capacities, branch counts, and rational bounds. The archived report concludes that no unresolved subset remains in that declared class. The complete coverage, dual, baseline, and primal artifacts are not included in C1; this paragraph is a historical account, not a replacement for those withheld computations.

The number $\binom{7262}{8}=191097212783647016778110245$ counts subsets covered by pruning and certification, not individually executed tests. Later recursive constructions do not contradict (64): they change infinite families, permit different root tables, and leave its frozen finite-edit class.


The public supplement therefore does not claim to verify this numerical optimum, and the main lower bound does not use it. The exhaustive pruned-coverage program is part of the historical proof obligation, not merely a dispensable discovery heuristic. Publishing only the 4,008 duals and survivor lists would leave coverage unproved. Any later public S15 certificate would have to supply an independently checkable coverage argument together with the frozen inputs, primal feasibility, and exceptional-subset duals.

# Appendix C. Archive repair, supersession, and corrected interpretations

## C.1. The damaged original

The original `F4-Digit-Branches-Verified.zip` was not a complete standard ZIP. A second retrieval reproduced the same bytes. Recovery identified 57 intact entries; `union_verified.json` ended mid-record, and the closing directory was absent. The advertised verification entry points and checksum manifest were not among the recoverable files. Several checkpoint paths also pointed to a directory not present in that layout.

The initial audit’s JSON parsing, source syntax checks, and 21 scoped consistency checks did not find a mathematical counterexample. They were expressly not a replacement for the missing full proof chain. The partial-recovery archive is retained as S26 and is labeled non-authoritative for full verification.

## C.2. The complete replacement

The S22 replacement used earlier releases to restore the verifier sources, rebuilt the missing wrapper, regenerated the entire 57,105-progression catalog, corrected paths, and created a new manifest. Its 80 archive entries passed extraction and CRC tests, and its full verifier and 17 regression tests passed from a clean extraction. The regenerated catalog matched every surviving byte of the truncated original catalog.

The original damaged bytes and their complete replacement are retained privately. Later internal releases used the corrected dependency chain, but C1 requires none of that chain. Its generic automaton proof and recalculated weights are derived from the included final and predecessor witnesses. Archive repair remains part of the research history, not a condition on public replay.

## C.3. Interpretive corrections carried forward

A finite outer insertion is not a globally repeated root family. An inactive deletion is not a paid removal. A redundant descendant deletion removed during ancestry normalization is not necessarily a restoration. A low number of control policies does not measure the number of ordinary automaton states needed to encode finite exception tables. An optimal flag from a floating numerical subproblem is not an exact global theorem. A failed bounded search is not an exclusion of its unsearched complement.

The original five changed digits were not a five-branch cap. The base has 55 possible residues, but the original modular proof uses 21 ordinary digits. The fixed-pool ceiling is not an upper bound on $F_4$. The infinite baseline sum cannot be added to a new finite upper block without accounting for the baseline tail already present. These distinctions are incorporated into the definitions, tables, and conclusions above rather than left as footnotes to superseded claims.

# Appendix D. Explicit data and algorithms

## D.1. Word convention and membership

For a word $w=(d_0,\ldots,d_{\ell-1})$ read from low to high digit,

$$
T_w=T_{d_0}\circ T_{d_1}\circ\cdots\circ T_{d_{\ell-1}},
\qquad v_w=\sum_{j=0}^{\ell-1}d_j55^j.
\tag{65}
$$

This convention fixes the order of the root-word family and of the state transition $\delta(s,w)$.

```text
MEMBER(policy s, integer n)
    if n < 1: return false
    while n > 1:
        if n is in E[s]: return true
        if n is in R[s]: return false
        (q, d) = quotient_and_remainder(n - 1, 55)
        if d is not in D: return false
        s = delta(s, d)
        n = q + 1
    return true
```

The final release provides the ordinary-DFA evaluator as well as this defining grammar. The former needs only the exported states, accepting bits, and transitions. The latter is useful as a structurally different membership control.

## D.2. Product-graph acceptance algorithm

```text
AP_CHECK(DFA, entry)
    verify transition domains, dead sink, and zero-padding invariance
    initial = (entry, entry, entry, entry, 0, 0, 0, false)
    queue = [initial]; seen = {initial}
    while queue has an unprocessed state:
        if a resource limit is exceeded: return INCOMPLETE
        for a in 0,...,54 and d in 0,...,54:
            compute raw values a, a+d+c1, a+2d+c2, a+3d+c3
            follow the four residue transitions; update the three carries
            skip a transition if any component is the dead sink
            update the nonzero-difference flag
            if the resulting state is new:
                store it and its predecessor digits
                if all four states accept, carries are zero, flag is true:
                    reconstruct and check the integer progression
                    return COUNTEREXAMPLE
                append it to the queue
    return PROVED_FREE
```

The finite-graph argument in Theorem 5.1, not the pseudocode alone, establishes the relationship between this result and the infinite set. The shipped implementation reconstructs large witnesses using its own arbitrary-length decimal arithmetic rather than assuming a fixed maximum integer length.

## D.3. The 37 final high-range insertion roots

The 32 locally zero-deletion proposals accepted together are

```text
60181877, 60846937, 60847377, 60847388, 60969125, 61013752,
61419113, 61499501, 61499578, 61499677, 61499941, 61500007,
61539662, 61845187, 61918238, 62011562, 62012013, 62749662,
63082863, 63248787, 63343002, 63509388, 63914727, 64247477,
64340812, 64341252, 64455762, 64456202, 64456213, 64461812,
64462263, 64839937.
```

| Paid insertion root | Additional listed deletion roots |
|--:|:--|
| 61499908 | 134671642 |
| 61845055 | 135049451, 153350701 |
| 62011430 | 135215826 |
| 62011551 | 135216553, 153517803 |
| 64839805 | 92291982 |

Table D1. The sequential acceptance order is recorded from the private S25 harvest history. The resulting policy assignment and all final roots and repairs are supplied in `witness/candidate.json`. C1 verifies the entire resulting construction; it deliberately omits the harvest ledger and does not replay the proposal sequence.

## D.4. Complete integer tables are part of the theorem

The thousands of root entries and all 1,384 ordinary-DFA transition rows are supplied electronically rather than printed as a long decimal appendix. This is not an omission of the construction: the exact files, hashes, decoding rule, compiler, and independent acceptance program specify it completely. C1 supplies the complete final grammar, DFA, weight certificate, and predecessor grammar under `witness/`. The earlier search universes and historical integer tables are privately retained and are not needed by the main theorem.

# Appendix E. Public reproduction and exact identifiers

## E.1. Replaying the standalone certificate

Extract `F4-Certificate-Only-Standalone.zip`, enter `F4-Certificate-Only-Standalone/`, and run:

```sh
python3 -O verify.py --output runs/verification.json
```

The README specifies Python 3.10 or later and a C++17 `g++` compiler, with `CXX` available to select a compatible compiler. The cited author-side run used Python 3.13.5 and g++ 14.2.0; that observed environment is not a claim of testing every supported platform. The primary path needs no optimizer, NumPy, network connection, predecessor ZIP, catalog, or discovery record.

A successful run must close the complete product graphs, reproduce the canonical final DFA, recompute both endpoint pairs and the certified gain, and pass the rejection controls. Neither a checksum match nor a stored PASS string is sufficient. A timeout or resource limit is not a proof. Generated outputs must be written under `runs/` or outside the extracted package; they are not immutable certificate inputs.

Optional secondary commands are:

```sh
python3 independent/run_checks.py --output runs/secondary.json
python3 independent/run_checks.py --with-floating \
  --output runs/secondary.json
```

Only the floating option requires NumPy. The wrapper validates the secondary carry checker’s text format, 11-bit state bound, rejecting sink, and padding assumptions before invocation. The optional floating comparison does not replace rational bounds. Historical scans and the S15 bounded-insertion result are not replayed.

## E.2. Mathematical dependencies and recorded runs

The source tables define the set. The compiler derives its ordinary digit language. The addition-carry checker proves progression-freeness from that language. The rational moment engine prices the signed root recurrence with active deletions. The constant-alphabet block routine derives the Walker interval with an explicit remainder. The same compiler, carry verifier, and rational accounting rederive the predecessor certificate. The final gain is an exact subtraction, not a comparison of rounded decimals.

The author-side replay is `validation/build_replay.json` with `validation/build_replay.log` [V1]. The secondary cross-implementation records are `validation/secondary_replay.json` and `validation/secondary_replay.log` [V2]. All four are preserved within C1. They document actual executions, but are not proof premises or external peer-review reports. The final theorem has no dependency on a historical scan-completeness flag, the old pool, a harvest ledger, or S15’s coverage computation.

## E.3. Exact identity of the public objects

C1 is certificate version `standalone-1`, comprising 23 ZIP members and 22 payload files covered by `MANIFEST.sha256.json` (the manifest does not hash itself). Its checksum identifies the unchanged certificate-only candidate, not the private dossier. The following full SHA-256 identifiers fix the key objects; the payload manifest identifies every other file.

**`F4-Certificate-Only-Standalone.zip`**

```text
b65f3e02b96156de3053709b6c018b87d06996902fb71f06e51b8c5ffcdd8e9a
```

**`witness/candidate.json`**

```text
93d0327411a868507be3e7362881defbc2f630713cf850d58a3db70c4d4163cb
```

**`witness/candidate_dfa.json`**

```text
990311f822c2575195b4174ae04b1dca997ad19d8e2b7044d2b5e42a50eb34b0
```

**`witness/weight_certificate.json`**

```text
bc59818f56ea9d8e7e641932e6a047cc4bc08b08fdbe1f1ea1b08751d1b9efff
```

**`witness/predecessor_grammar.json`**

```text
ab4b0416085cd145b47ee18af26d0a4beed2a4863acad7d722100f453a2bbc22
```

**`validation/build_replay.json`**

```text
1ea4a1b21f0e938e5a887e1fc50e18f468ec1fa0022f0e4e9bc1b482e508865b
```

The long rational numerators and denominators in `witness/weight_certificate.json` are preserved exactly. The display in (7) is deliberately wider than those endpoints. `witness/expected_baselines.json` supplies expected outputs checked only after recomputation. `PROVENANCE.json` identifies the unchanged source modules and predecessor witness without requiring or distributing their historical source archives.

# Appendix F. Availability, internal provenance, and attribution

## F.1. Public certificate and retained internal identifiers

The sole supplementary artifact designated for public deposit is [F4-Certificate-Only-Standalone.zip](F4-Certificate-Only-Standalone.zip) [C1], certificate version `standalone-1`. The relative link refers to the accompanying file, not an established public repository. Its full checksum is given in Appendix E. The repository DOI for this deposit is 10.5281/zenodo.24485654. No sandbox link is presented as a permanent scholarly identifier.

**Availability statement.** The explicit construction, its digit automaton, exact rational certificate, and standalone verification software are provided in the certificate-only supplement. The supplement recomputes the main lower bound and the comparison with the supplied predecessor without access to the proprietary discovery engine. Optimization and screening routines, proposal generators, and search records are not distributed. Historical numerical exclusions not replayed by the supplement are identified as such and are not used in the main proof.

The following S01–S26 labels are internal provenance identifiers only. Their titles preserve the research chronology. No private archive download links or source-archive attachments are included in this edition.

| ID | Internal research record | Availability in this edition |
|:--|:--|:--|
| S01 | P0 dual and first finite Walker repair | Private provenance; not in C1 |
| S02 | Joint finite insertion–deletion certificate | Private provenance; not in C1 |
| S03 | Recursive root-family certificates | Private provenance; not in C1 |
| S04 | Shared-deletion feedback and expansion | Private provenance; not in C1 |
| S05 | Conditional repair and joint swaps | Private provenance; not in C1 |
| S06 | Target 5.1 tests and family ceilings | Private provenance; not in C1 |
| S07 | Alternative digit and shifted-tail constructions | Private provenance; not in C1 |
| S08 | Chamber-coordinate proposal experiment | Private provenance; not in C1 |
| S09 | Stacking audit and composite bases | Private provenance; not in C1 |
| S10 | Conflict-aware finite stacking | Private provenance; not in C1 |
| S11 | Gated stacking and repair-cost packings | Private provenance; not in C1 |
| S12 | Full infinite-baseline finite joint edits | Private provenance; not in C1 |
| S13 | Boolean solver repair and cooperative pair | Private provenance; not in C1 |
| S14 | Reverse deletion and optional-cover search | Private provenance; not in C1 |
| S15 | Exact at-most-eight-insertion barrier | Private provenance; not in C1 |
| S16 | Recursive lift and cross-level repairs | Private provenance; not in C1 |
| S17 | Root factorizations and arithmetic controls | Private provenance; not in C1 |
| S18 | Exact selected-spacing exclusions | Private provenance; not in C1 |
| S19 | Restoration tests and search diagnosis | Private provenance; not in C1 |
| S20 | Two-state generators and orbit exchange | Private provenance; not in C1 |
| S21 | Original digit-branch release: DAMAGED | Private provenance; not in C1 |
| S22 | Complete repaired digit-branch release | Private provenance; not in C1 |
| S23 | 60M scan, larger automata, uncapped branches | Private provenance; not in C1 |
| S24 | Three-policy recurrent middle construction | Private provenance; not in C1 |
| S25 | Four-policy final recurrent construction | Private provenance; not in C1 |
| S26 | Partial recovery and original archive audit | Private provenance; not in C1 |

S21 is retained privately as damaged forensic evidence, S26 as a partial recovery, and S22 as its historical complete replacement. C1 supersedes the chain as the standalone public verification object. The identifiers do not imply that original discovery programs or every historical numerical certificate are publicly accessible.

## F.2. Privately retained antecedent manuscripts

**B01.** Darby Bailey McDonough. *Reciprocal Sums of Four-Term-Progression-Free Sets: Finite certificates and an exact smooth-number model.* Research checkpoint, version 1.0, 10 September 2026. Privately retained antecedent. Its smooth-number theorem is reproduced with a complete analytic proof in Appendix A; its finite-horizon computational records are not part of C1.

**B02.** Darby Bailey McDonough. *Recursive Certificates and Information Limits for Arithmetic Progression Free Sets.* Research manuscript, 10 September 2026. Privately retained background on finite certificates and representation limits, not a new result of this constructive release.

**B03.** Darby Bailey McDonough. *Moment Repairs and Uniformity Obstructions for Arithmetic Progression Free Sets.* Research manuscript, 11 September 2026. Privately retained antecedent. The positive-row-ratio obstruction is stated and proved in Appendix A; the other studies are not part of C1’s computational scope.

**B04.** *Hs108 Void Atlas F4 Report.* Privately retained proposal report. It supplies historical context, not a physical premise, external validation, or dependency of the main arithmetic certificate.

The private reports and source archives are not attached or promised on request by this availability statement. Their historical results retain their explicit scope; only C1 is the accompanying verification supplement.

## F.3. Contributions, AI assistance, and release status

Darby Bailey McDonough supplied the research direction, hypotheses, construction goals, and cross-assistant audit requests. The retained record documents AI-assisted formalization, software development, bounded search, verification, and drafting under that direction. This manuscript was prepared with ChatGPT assistance, including source retrieval, mathematical exposition, document preparation, and computational checking. The supplied secondary implementations provide additional software consistency checks. AI systems are not authors or independent peer reviewers. The named human author retains responsibility for review and any eventual submission.

The author-side replay is cited through V1, and the secondary checks through V2. A conversation’s report of an additional run is not counted as another archived execution without its underlying record.

No institutional affiliation, funding attribution, license, or independent peer-review endorsement is inferred. Funding, conflicts of interest, rights, and submission declarations require the author’s confirmation. The public license is not selected or granted by this editorial revision; C1’s README expressly leaves that decision open. The certificate and manuscript intentionally disclose the successful mathematical construction and its verification methods, but not the discovery engine. No claim that verification software lacks intellectual property value follows from its role. No DOI registration, repository publication, or forum posting was performed in preparing this edition.

# References {.unnumbered}

[1] Alexander Walker. *Integer Sets of Large Harmonic Sum Which Avoid Long Arithmetic Progressions.* arXiv:2203.06045, first submitted 2022; version 2, 2025. [Primary paper](https://arxiv.org/abs/2203.06045v2). Source of the unedited base-55 construction and modular digit-descent background.

[2] Hamoon Mousavi. *Automatic Theorem Proving in Walnut.* arXiv:1603.06017, 2016. [Primary paper](https://arxiv.org/abs/1603.06017). Background on automata-based decision procedures; not an endorsement or verification of the present witness.

[3] Thomas Schmelzer and Robert Baillie. “Summing a Curious, Slowly Convergent Series.” *The American Mathematical Monthly* **115**(6), 525–540, 2008. [DOI: 10.1080/00029890.2008.11920559](https://doi.org/10.1080/00029890.2008.11920559). Background on rigorous and efficient evaluation of digit-restricted reciprocal series.

[4] Anna Klick, Nicolae Strungaru, and Adi Tcaciuc. *On arithmetic progressions in model sets.* arXiv:2003.13860, 2020. [Primary paper](https://arxiv.org/abs/2003.13860). Background separating quasiperiodic/model-set structure from automatic progression avoidance.

[S01–S26] Darby Bailey McDonough, with the AI-assisted research workflow identified in the retained reports. Unpublished private research records, 11–13 September 2026. Internal titles appear in Appendix F; discovery archives and historical numerical certificates outside C1 are not publicly distributed. These records identify the sources of historical statements, not additional dependencies of Theorem 2.1.

[C1] Darby Bailey McDonough, with AI-assisted preparation. *F4: standalone certificate-only release candidate*, version `standalone-1`, 13 September 2026. `F4-Certificate-Only-Standalone.zip`; full checksum in Appendix E. Accompanying witness and verification supplement; DOI 10.5281/zenodo.24485654.

[V1] *Standalone certificate author-side verification replay*, 13 September 2026. C1, `validation/build_replay.json` and `validation/build_replay.log`. Author-side AI-assisted execution documenting endpoints, graph closures, predecessor comparison, and controls; not peer review.

[V2] *Standalone certificate secondary implementation checks*, 13 September 2026. C1, `validation/secondary_replay.json` and `validation/secondary_replay.log`; source under `independent/`. Cross-implementation carry and optional floating checks; neither peer review nor a substitute for exact rational bounds.
