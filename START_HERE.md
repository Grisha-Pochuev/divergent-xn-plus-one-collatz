# START HERE

Compact durable entry point for each research session.

## Strict target

Find explicit positive odd `X>=5,n0` such that

```text
C_X(n)=(X*n+1)/2^v2(X*n+1)
```

tends to positive infinity. A cycle, avoidance of `1`, finite growth, a finite
barrier, or heuristic drift is not a solution.

## Unrestricted research mode

Use all research capacity actually available.  There is no project-imposed cap on
repository reading, literature searches, tool calls, active directions,
candidate multipliers, symbolic calculations, exhaustive finite searches,
SAT/SMT or proof-assistant work, GitHub Actions runs, checkers, branches, or
commits in one session.

A request to continue authorizes broad and sustained work across multiple methods.
The primary candidate may be replaced when another candidate has better rigorous
prospects.  Optimize or narrow the work only after a real platform, context,
runtime, memory, or scientific-value bottleneck is encountered, not because an
older chat or subscription once lagged.

This removes operational limits only.  Mathematical safeguards remain mandatory:
finite trajectories are not divergence proofs, evidence is not a theorem,
retracted arguments stay retracted, and every claimed result must remain
reproducible and auditable.

## Read at startup

Read at minimum these files once per chat unless one changes:

```text
START_HERE.md
docs/WORKING_PROTOCOL.md
docs/CURRENT_STATUS.md
```

These files are an entry point, not a ceiling.  Read any additional theorem,
checker, result, commit history, issue, retraction, archive, literature source, or
the whole repository whenever it may help.

File roles:

- `START_HERE.md`: routing, current candidate, decisive obstruction;
- `docs/WORKING_PROTOCOL.md`: operating and verification rules;
- `docs/CURRENT_STATUS.md`: authoritative mathematical frontier;
- theorem documents and checkers: detailed proofs and certificates;
- `docs/RETRACTIONS.md`: audit history;
- session checkpoints and `docs/archive/`: historical handoffs.

Current `main` and committed checkers override chat summaries.  Search and read
broadly when it improves the chance of a proof; avoid only redundant re-fetches
of unchanged material that add no information.

## Primary long-form candidate and proof gates

```text
N=2^500-1,
B=2^4501,
d=349*2^500-347,
X=B-d=2^4501-349*2^500+347,
n0=1.
```

```text
G1 explicit pair: closed;
G2 leaves 1 and never returns: closed;
G3 all nontrivial positive cycles excluded: open;
G4 bounded positive orbit implies eventual cycle: closed;
G5 final certificate: waits for G3.
```

The strict problem remains open because G3 remains open.

## Parallel short-form candidate: `X=31,n0=3`

Keep the explicit accelerated orbit

```text
X=31,
n0=3,
a_t=v2(31*n_t+1),
A_t=sum_(j<t) a_j,
s_2(n)=number of 1 bits of n.
```

The exact affine iteration bound gives

```text
n_t>3*31^t/2^A_t.
```

Consequently the single global estimate

```text
A_t+s_2(n_t)<=4*t+2 for every t>=1                    (X31)
```

would imply `A_t<=4*t+1` and therefore

```text
n_t>(3/2)*(31/16)^t -> +infinity.
```

Thus a proof of `(X31)` is a complete prize solution.  The exact one-step carry
identity retained for this route is

```text
s_2(31*n_t)=a_t+s_2(n_(t+1)-1).
```

Current status:

```text
(X31) checked with exact integer arithmetic through 100000 accelerated steps;
minimum slack 4*t+2-(A_t+s_2(n_t)) is 0, at t=1;
no proof for all t is known.
```

Files:

```text
docs/X31_BINARY_WEIGHT_LEAD.md
tools/check_x31_binary_weight.py
```

Treat this as an active parallel priority, not as a proved replacement for the
long-form candidate.  At each research session compare the expected rigorous
proof yield of both branches and freely work on the stronger one.  For `X=31`,
do not merely extend the finite trajectory cutoff unless the computation tests a
specific carry potential, induction scheme, block inequality, or counterexample
condition that informs the infinite lemma.

## Retained global facts

Put

```text
Q_credit=
924679364903952241768234680715310598867316370441120757898246831506500507205080014535351439406991342585993538327845986892977536682537320095988153612270886695873966778097766981798062925612878469213187733241206117142814414961418054803443235355123715316220902421623921086365374327267387194352877014114959.
```

Every hypothetical cycle satisfies all of the following:

```text
N|X and 1093||X;
16562000 permanent classes modulo N*1093^2;
every cycle value>N;
every exceptional source has at least 1505 decimal digits;
no cycle value in the checked window through 10^1201;
total credit D>=Q_credit>2^996;
full accelerated length p>2^4988;
at least ceil(Q_credit/4500) ordinary complete blocks.
```

The exact ordinary-block lower bound is

```text
205484303311989387059607706825624577526070304542471279532943740334777890490017781007855875423775853907998564072854663753995008151674960021330700802726863710194214839577281551510680650136195215380708385164712470476180981102537345511876274523360825625826867204805315796970083183837197154300639336470.
```

Coupling this population to the exact global boundary divisor `g` gives a new
forced repetition.  Since `g` is coprime to

```text
M=(2^500-1)*1093^2,
```

one same-credit ordinary boundary type occurs more than `2^947` times in one
class modulo `g*M`.  Its source values have diameter greater than
`g*2^1466`.

```text
docs/GLOBAL_DIVISOR_ORDINARY_POPULATION.md
tools/verify_global_divisor_ordinary_population.py
```

This supersedes the former bound `245833`, which is retained only as an audit
marker for older consistency checks.

Sources:

```text
docs/PRIMARY_CREDIT_CONTINUED_FRACTION_FRONTIER.md
tools/verify_primary_credit_continued_fraction_frontier.py
```

The former nonpositive-return branch is completely excluded. Its retained
comparison was `p<2^4006` against `p>2^(2^974)`. Do not revisit it unless a
specific error is found in its proof or checker.

```text
docs/NONPOSITIVE_RETURN_BLOCK_CORRECTION_EXCLUSION.md
tools/verify_nonpositive_return_block_correction_exclusion.py
```

## Permanent-label closure no-go

The `N` labels and the adjacent `1093^2` labels do not conflict with cyclic
wraparound. More strongly, every compatible cyclic label word lifts coherently
through every finite power

```text
N*1093^r,  r>=2.
```

At each new `1093`-adic digit, the new valuation-layer digit cancels the new
transition defect independently on each edge. The number of allowed combined
classes modulo `N*1093^r` is

```text
16562000*1093^(r-2),
```

so the higher lifts are completely saturated above the informative `1093^2`
level. No finite deeper `1093`-adic label automaton can exclude a cycle by bare
closure.

Sources:

```text
docs/PERMANENT_LABEL_CYCLIC_CLOSURE_NO_GO.md
tools/verify_permanent_label_cyclic_closure_no_go.py
docs/WIEFERICH_Q_ADIC_LIFT_SATURATION_NO_GO.md
tools/verify_wieferich_q_adic_lift_saturation.py
```

## Positive ballot and sponsor arches

Use the canonical complete-block partition and let `z` be the least value among
all complete-block boundaries. Every nonempty cumulative block-credit prefix
from `z` is positive:

```text
P_j>=1.
```

Every exceptional block lies in a canonical ordinary-to-exceptional sponsor arch
with

```text
0<=C<=4499,
```

and every internal boundary stays strictly above the final credit level. The
arches are laminar. Their maximal members are pairwise disjoint, cover every
exceptional block, and leave only ordinary blocks outside.

Detailed sources:

```text
docs/MINIMUM_BLOCK_BOUNDARY_CREDIT_BALLOT.md
tools/verify_minimum_block_boundary_credit_ballot.py
docs/EXCEPTIONAL_SPONSOR_ARCH_MACRO_EXIT.md
tools/verify_exceptional_sponsor_arch_macro_exit.py
```

## Sharp floor-sensitive height theorem

Every hypothetical cycle value is greater than `N`. Put

```text
delta=log2(B/X),
epsilon=1/(X*N*ln(2)).
```

The former exact estimates

```text
delta<2^-3992,
delta-epsilon>997*2^-4002
```

remain valid and are checked in

```text
docs/PRIMARY_DELTA_TWO_BIT_SHARPENING.md
tools/verify_primary_delta_two_bit_sharpening.py
docs/CYCLE_FLOOR_LOCAL_CORRECTION_SHARPENING.md
tools/verify_cycle_floor_local_correction_sharpening.py
```

They are now sharpened to

```text
1007*2^-4002 < delta-epsilon,
delta < 1008*2^-4002.                                  (1)
```

Every actual consecutive complete-block segment of net credit `C`, accelerated
length `L`, source `x`, and endpoint `y` satisfies

```text
log2(y/x)<C-1007*L*2^-4002.                            (2)
```

Consequences for positive-credit segments:

```text
nondecreasing: L<C*2^4002/1007;
contracting:   L>C*2^4002/1008.
```

A zero-credit sponsor arch has the quantitative contraction

```text
log2(source/endpoint)>1007*L*2^-4002.                  (3)
```

Sources:

```text
docs/PRIMARY_ONE_OVER_1007_CYCLE_STRIP.md
tools/verify_primary_one_over_1007_cycle_strip.py
docs/ZERO_CREDIT_ARCH_QUANTITATIVE_CONTRACTION.md
tools/verify_zero_credit_arch_quantitative_contraction.py
```

## Global one-over-1007 cycle strip

For full cycle length `p` and total credit `D`,

```text
D*2^4002/1008
 <p
 <D*2^4002/1007.                                      (4)
```

The relative width is exactly

```text
1/1007<0.1%.
```

This replaces the older `27/997<2.71%` strip as the strongest current
cycle-wide restriction. It is more than 27 times narrower.

## Strongest exit-return decomposition

At the least boundary `z`, take the maximal sponsor arch beginning with block `0`,
if one exists, or otherwise the first pure ordinary block. This gives an actual
bounded sponsored macro-exit from `z` to `y` with

```text
z<y,
1<=C<=4500,
L_macro<C*2^4002/1007<2^4005.
```

The remaining actual return from `y` to `z` satisfies

```text
R>=1,
D=C+R>=Q_credit,
L_return>R*2^4002/1008,
L_return<(R+4500)*2^4002/1007.
```

Every return prefix ending at a complete-block boundary has credit

```text
Q>=1-C>=-4499.
```

## Decisive next targets and strategy pivot

For the long-form candidate, exclude the positive-credit return after the bounded
initial sponsor nest.  The finite `1093`-adic closure route is rigorously
exhausted.  This is a proved mathematical no-go, not a restriction on trying
other primes, other invariants, or other candidates.

The strongest remaining route for the long-form candidate is:

1. use the 300-digit total-credit frontier and the `1/1007` global strip;
2. charge every zero-credit arch by the quantitative loss (3);
3. apply the adjacent `1007/1008` length dichotomy to every remaining
   positive-credit macroblock;
4. use the `N*1093^2` classes for global occupancy and correction bounds;
5. strengthen the proved `>2^947` same-credit population in one class modulo
   `g*N*1093^2` into a height or reciprocal-mass contradiction;
6. exploit `Q>=-4499`, so no return prefix can use an unbounded exceptional
   reserve.

For the short-form `X=31` route, prove `(X31)` by deriving a genuine global
binary-carry invariant, an induction closed under the exact accelerated map, or
an unbounded telescoping carry potential.  A counterexample to `(X31)` is also a
decisive result: record the first failure and use its carry pattern to redesign
or retire the route.

In parallel, freely screen alternative candidates, primes, prime powers,
valuation codes, automata, global divisors, Diophantine estimates, formal proof
methods, and computational certificates.  If the exact global-divisor route
fails to couple the labels, deprioritize the long-form candidate rather than
extending a structurally saturated local sieve.  If the `X=31` inequality resists
all structurally informed induction or potential constructions, do not preserve
it merely because a long finite prefix survives.

The scalar continued-fraction method alone has reached its certified 300-digit
credit frontier. Further progress must use nonlocal arithmetic, stronger
occupancy/correction, a genuinely new analytic estimate, a global digital
invariant, or a better candidate.

Finite same-type windows, a fixed finite `N`-adic ladder, finite `1093`-adic
lifts, or long finite trajectories may be used for reconnaissance and lemma
discovery, but not as a standalone contradiction or divergence proof.

## Non-negotiable corrections

Do not use `2^A==1 (mod X)`. The correct relation is

```text
2^A*product_i(n_i)==1 (mod X).
```

Do not identify a least admissible predecessor with the predecessor actually used
by a cycle. Never present finite computation as divergence.

## Continue instruction

A request to continue authorizes an unrestricted research session within actual
platform limits.  Inspect as much of the repository and literature as useful,
pursue several routes, change candidates, run substantial calculations, build
and verify certificates, and commit every durable result or rigorous no-go.

Do not stop merely because an older operating rule preferred short searches or a
small number of directions.  Stop or narrow only for an actual resource failure,
a rigorous dead end, loss of relevance to the infinite target, or completion of
a checked result suitable for handoff.  Report exactly what was proved, tested,
committed, and left open.
