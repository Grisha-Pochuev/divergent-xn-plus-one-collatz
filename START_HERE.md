# START HERE

Compact entry point for each research session.

## Strict target

Find explicit positive odd integers `X>=5,n0` such that

```text
C_X(n)=(X*n+1)/2^v2(X*n+1)
```

tends to positive infinity. A cycle, avoidance of `1`, a finite barrier, a huge
finite trajectory, or heuristic drift is not a solution.

## Read first

```text
START_HERE.md
docs/WORKING_PROTOCOL.md
docs/CURRENT_STATUS.md
docs/RETRACTIONS.md
docs/SESSION_CHECKPOINT_2026-07-12_NONPOSITIVE_RETURN_HARMONIC_BARRIER.md
```

Fetch these files from the current default branch at the start of every session.
GitHub commits and certificate scripts are the durable source of truth. If an
in-chat summary or an older checkpoint conflicts with current `main`, current
`main` wins.

## One-chat research sprint

A broad user request such as `continue solving` authorizes one substantial
research sprint. Do not ask the user to choose among plausible technical routes;
choose the route with the best apparent chance of advancing the strict target.

Each sprint should aim for one main deliverable:

1. a proved lemma that advances a proof gate;
2. a decisive refutation of an approach;
3. a verified computational certificate with mathematical meaning;
4. a literature result that materially changes the strategy, after independent
   checking of the part being used;
5. a precise obstruction plus the next exact experiment when no theorem is
   reached.

Within one sprint, multiple methods and short side investigations are allowed.
Work until one deliverable is reached or the chosen route is rigorously shown to
fail. Then verify it independently where possible, commit the result immediately,
and report separately what was proved, what was only tested, and what remains
open.

Do not claim background work after the response ends. A new sprint begins with a
new user request.

## Research freedom and priorities

The current return-obstruction target below is the primary target, not an
exclusive restriction. It is explicitly allowed to:

- search current and historical literature, including claimed proofs, surveys,
  related generalized Collatz maps, Diophantine approximation, dynamical systems,
  symbolic dynamics, and computer-assisted proof methods;
- inspect alternative candidates `(X,n0)` and previously retained fallback
  branches;
- transfer methods between candidates after checking every hypothesis;
- use symbolic algebra, exact arithmetic, SAT/SMT, theorem provers, finite-state
  models, residue graphs, and small or medium exact searches;
- derive and test new invariants, coordinate systems, block decompositions,
  congruence sieves, height functions, and descent arguments;
- temporarily leave the primary branch when another route has a credible chance
  of closing `G3` faster or proving divergence directly.

Literature search is never prohibited. Prefer primary sources. A claimed proof is
an idea source, not a retained theorem, until the needed argument has been checked
line by line or reduced to an independently verifiable certificate.

A side branch should be committed only when it gives a reusable theorem, a
verified obstruction, a materially better candidate, or a documented strategic
change. Do not spend a sprint merely enlarging a numerical record with no new
infinite argument.

## Primary candidate

```text
N=2^500-1,
B=2^4501,
d=349*2^500-347=2+349*N,
X=B-d=2^4501-349*2^500+347,
n0=1.
```

Proof gates:

```text
G1 explicit pair: closed;
G2 leaves 1 and never returns: closed;
G3 every nontrivial positive cycle excluded: open;
G4 bounded positive orbit implies eventual cycle: closed;
G5 final independent certificate: waits for G3.
```

## Main retained results

- `N|X` and `1093||X`;
- the orbit leaves `1` and never returns;
- exactly `16562000` permanent classes survive modulo `N*1093^2`;
- every cycle value is greater than `N`;
- every exceptional source has at least `1505` decimal digits;
- every cycle length through a number between `10^1201` and `10^1202` is
  impossible;
- the full harmonic and `X`-adic bounds remain available.

## Global ordinary-block frontier

Every hypothetical nontrivial positive cycle has at least

```text
245833 ordinary complete blocks.
```

This allows arbitrary exceptional-block populations and arbitrary block lengths.
It is not a cycle-length cutoff.

Main files:

```text
docs/GLOBAL_ORDINARY_BLOCK_COUNT_FRONTIER.md
tools/verify_global_ordinary_block_count_frontier.py
```

## Bounded positive circulation

For each occurring ordinary terminal deficit `e`, choose the smallest cycle
boundary value `x_e` of that type. The resulting finite functional graph contains
a directed cycle whose selected disjoint orbit intervals satisfy

```text
q<=4500,
1<=C<=20250000,
T<=20254499,
L*delta<C,
delta=log2(B/X).
```

Their formal base multiplier is strictly expanding:

```text
2^C*(X/B)^L>1.
```

Files:

```text
docs/MINIMUM_BOUNDARY_POSITIVE_CIRCULATION.md
tools/verify_minimum_boundary_positive_circulation.py
```

## Actual minimum-boundary expanding segment

Choose the least cycle value immediately following an ordinary complete block,
and follow the actual orbit to the next such value. This gives one consecutive
orbit segment satisfying

```text
1<=net credit C<=4500;
exceptional excess sum <=4499;
number of complete blocks <=4500;
L*delta<C;
endpoint > starting value.
```

Thus the segment itself, without splicing, has expanding base multiplier

```text
2^C*(X/B)^L>1.
```

Files:

```text
docs/MINIMUM_BOUNDARY_ACTUAL_EXPANDING_SEGMENT.md
tools/verify_minimum_boundary_actual_expANDING_SEGMENT.py
```

## Actual return frontiers

Let `R` and `Lr` be the net credit and accelerated length of the remaining actual
orbit from the larger endpoint back to the least ordinary boundary. Two strict
results are retained:

```text
R>=1 => Lr>2^3990;
R<=0 => Lr>2^(2^974).
```

The second result combines the permanent `16562000`-class sieve, harmonic
packing, the small correction on the expanding exit, and the one-sided
continued-fraction gap. It is not a trajectory computation.

Files:

```text
docs/MINIMUM_BOUNDARY_RETURN_CREDIT_DICHOTOMY.md
tools/verify_minimum_boundary_return_credit_dichotomy.py
docs/MINIMUM_BOUNDARY_NONPOSITIVE_RETURN_HARMONIC_BARRIER.md
tools/verify_minimum_boundary_nonpositive_return_harmonic_barrier.py
```

## Decisive missing theorem

A hypothetical cycle can now return only through one of two extreme branches:

```text
positive return credit with Lr>2^3990;
nonpositive return credit with Lr>2^(2^974).
```

The primary next target is a length-independent obstruction proving one of:

1. inverse `X`-adic descent through a positive-credit return word;
2. incompatibility of the exit and final return block modulo `X^2` or a higher
   power;
3. a regeneration theorem turning the expanding exit into a repeatable growing
   segment;
4. a global argument excluding the doubly-exponential nonpositive branch without
   merely increasing its finite cutoff.

This is a priority, not a ban on other routes. A sprint may instead pursue a
direct divergence proof, a stronger candidate, a literature-derived lemma, or a
new global cycle obstruction when its expected value is higher.

Do not merely extend a continued-fraction denominator, a finite trajectory, or a
finite return-length barrier.

## Reusable family theorem

For

```text
N=2^k-1,
m==r (mod k),
d=2^r+t*N,
X=2^m-d,
```

with `364` not dividing `k`, one can choose parity-correct `t<2*1093^2` with
`1093||X`. This gives no return to `1`, an exponentially thin permanent sieve,
and an arbitrarily large finite barrier. Increasing parameters alone is not a
priority.

## Non-negotiable corrections

Do not use

```text
2^A==1 (mod X).
```

The correct cycle congruence is

```text
2^A*product_i(n_i)==1 (mod X).
```

Do not identify a least admissible predecessor source with the source actually
used by a cycle. Do not present a finite computation as divergence.

## Verification discipline

- commit each theorem, checker, decisive refutation, and major strategy change;
- state exactly which checks ran;
- do not claim a complete repository run unless it completed;
- compare every proposed result with current `main` before calling it new;
- preserve failed approaches when the failure prevents future repetition.

## Reproduction

```text
python run_checks.py
```
