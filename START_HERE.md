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
every exceptional source has at least 1505 decimal digits;
no cycle value in the checked window through 10^1201;
at least 245833 ordinary complete blocks.
```

The former nonpositive-return branch is completely excluded. Its retained
comparison was `p<2^4006` against `p>2^(2^974)`. Do not revisit it.

Sources:

```text
docs/NONPOSITIVE_RETURN_BLOCK_CORRECTION_EXCLUSION.md
tools/verify_nonpositive_return_block_correction_exclusion.py
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

They are now sharpened to the adjacent-coefficient bracket

```text
1007*2^-4002 < delta-epsilon,
delta < 1008*2^-4002.                                  (1)
```

Therefore every actual consecutive complete-block segment of net credit `C`,
accelerated length `L`, source `x`, and endpoint `y` satisfies

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

For full cycle length `p` and total credit `D`, (1)--(2) give

```text
D*2^4002/1008
 <p
 <D*2^4002/1007.                                      (4)
```

The upper endpoint divided by the lower endpoint is `1008/1007`, so the relative
width is exactly

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
L_return>R*2^4002/1008,
L_return<(R+4500)*2^4002/1007.
```

Every return prefix ending at a complete-block boundary has credit

```text
Q>=1-C>=-4499.
```

## Decisive next target

Exclude the positive-credit return after the bounded initial sponsor nest. The
strongest route is now:

1. use the `1/1007` global strip, not the older coarse length bounds;
2. charge every zero-credit arch by the quantitative loss (3);
3. apply the adjacent `1007/1008` length dichotomy to every remaining macroblock;
4. combine arch endpoints with the permanent `N` and `1093^2` labels and the
   exceptional-source floor;
5. prove a lower correction bound incompatible with (4), a repeated exact source
   class, an incompatible adjacent-label lift, or excessive harmonic correction;
6. use `Q>=-4499`, so no return prefix can use an unbounded exceptional reserve.

Secondary routes remain the exact cyclic source-matching divisor and an explicit
linear-form-in-logarithms estimate, but only if their constants beat the actual
correction terms.

Do not use finite same-type windows, a fixed finite `N`-adic ladder, or long
finite trajectories as a standalone contradiction.

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
