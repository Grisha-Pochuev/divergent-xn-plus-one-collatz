# START HERE

Compact durable entry point for each research session.

## Strict target

Find explicit positive odd `X>=5,n0` such that

```text
C_X(n)=(X*n+1)/2^v2(X*n+1)
```

tends to positive infinity. A cycle, avoidance of `1`, finite growth, a finite
barrier, or heuristic drift is not a solution.

## Read at startup

Read exactly these files, once per chat unless one changes:

```text
START_HERE.md
docs/WORKING_PROTOCOL.md
docs/CURRENT_STATUS.md
```

File roles:

- `START_HERE.md`: routing, current candidate, decisive obstruction;
- `docs/WORKING_PROTOCOL.md`: operating and verification rules;
- `docs/CURRENT_STATUS.md`: authoritative mathematical frontier;
- theorem documents and checkers: detailed proofs and certificates;
- `docs/RETRACTIONS.md`: audit history, read only when a related argument arises;
- session checkpoints and `docs/archive/`: historical handoffs, not startup memory.

Current `main` and committed checkers override chat summaries. Do not load the
whole repository or fetch an unchanged file repeatedly without a concrete need.

## Primary candidate and proof gates

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

## Retained global facts

Every hypothetical cycle satisfies all of the following:

```text
N|X and 1093||X;
16562000 permanent classes modulo N*1093^2;
every cycle value>N;
no cycle value in the checked window through 10^1201;
at least 245833 ordinary complete blocks.
```

The former nonpositive-return branch is completely excluded. The general
cycle-wide block-correction theorem gives

```text
p < 2*D*B*X/[d*(X-d)].
```

When a return has nonpositive credit, `1<=D<=4500`, so `p<2^4006`, while the
retained harmonic theorem forces `p>2^(2^974)`. This contradiction is closed and
must not be revisited.

## New strongest decomposition

Use the canonical complete-block partition and let `z` be the least value among
all complete-block boundaries.

Every complete block of credit `c` obeys the exact domination

```text
endpoint/source < 2^c.
```

Therefore, when blocks are read from `z`, every nonempty cumulative block-credit
prefix is a positive integer:

```text
P_j>=1.
```

Consequences:

```text
the first block after z is ordinary;
its deficit is 1<=e<=4500;
it is one pure ordinary block, with no exceptional block in the exit;
its base multiplier already expands;
its endpoint z' is strictly larger than z.
```

The remaining actual return from `z'` to `z` satisfies

```text
R>=1,
L_return>2^3990.
```

Moreover every return prefix ending at a complete-block boundary has credit

```text
Q>=1-e>=-4499.
```

Thus the surviving return cannot front-load an unbounded exceptional debt.
Every exceptional excess unit is matched, in actual cyclic order, to an earlier
ordinary deficit unit; exactly `D` ordinary units remain unmatched after the
whole cycle.

Detailed sources:

```text
docs/MINIMUM_BLOCK_BOUNDARY_CREDIT_BALLOT.md
tools/verify_minimum_block_boundary_credit_ballot.py
docs/MINIMUM_BLOCK_BOUNDARY_PURE_ORDINARY_EXIT.md
tools/verify_minimum_block_boundary_pure_ordinary_exit.py
docs/NONPOSITIVE_RETURN_BLOCK_CORRECTION_EXCLUSION.md
tools/verify_nonpositive_return_block_correction_exclusion.py
```

## Decisive next target

Exclude the astronomically long positive-credit return after the pure ordinary
exit. The strongest route is now an ordered sponsor obstruction:

1. use the ballot matching to pair every exceptional excess unit with an earlier
   ordinary deficit unit;
2. combine each pair with the exceptional-source floor and the permanent `N` and
   `1093^2` labels;
3. prove that a sponsor cannot pay for its matched exception without forcing an
   impossible source repetition, an incompatible adjacent-label lift, or too
   much harmonic correction;
4. exploit the uniform return-prefix debt bound `Q>=-4499` so that no argument
   needs an unbounded initial exceptional reserve.

Secondary routes remain the exact cyclic source-matching divisor and an explicit
linear-form-in-logarithms estimate, but only if their constants beat the actual
correction terms.

Do not return to the closed nonpositive branch. Do not use finite same-type
windows, a fixed finite `N`-adic ladder, or long finite trajectories as a
standalone contradiction.

## Non-negotiable corrections

Do not use `2^A==1 (mod X)`. The correct relation is

```text
2^A*product_i(n_i)==1 (mod X).
```

Do not identify a least admissible predecessor with the predecessor actually used
by a cycle. Never present finite computation as divergence.

## Continue instruction

A request to continue authorizes one substantial research sprint. Choose the
strongest route, verify it, save a rigorous theorem, certificate, or strict no-go,
and commit the result. Keep chat updates short; keep detailed mathematics in the
repository.
