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

The former nonpositive-return branch is completely excluded. The general
cycle-wide block-correction theorem gives

```text
p < 2*D*B*X/[d*(X-d)].
```

When a return has nonpositive credit, `1<=D<=4500`, so `p<2^4006`, while the
retained harmonic theorem forces `p>2^(2^974)`. This contradiction is closed and
must not be revisited.

## Positive ballot and sponsor arches

Use the canonical complete-block partition and let `z` be the least value among
all complete-block boundaries. Every block of credit `c` satisfies

```text
endpoint/source < 2^c.
```

Therefore every nonempty cumulative block-credit prefix from `z` is positive:

```text
P_j>=1.
```

For each exceptional block, let `h` be the prefix credit immediately after it,
and choose the last earlier boundary whose prefix credit is at most `h`. The
resulting actual consecutive sponsor arch:

```text
starts with an ordinary block;
ends with the chosen exceptional block;
has net credit 0<=C<=4499;
stays strictly above its final credit level at every internal boundary.
```

Canonical sponsor arches are laminar: two are disjoint or nested, never
crossing. Their maximal members are pairwise disjoint, cover every exceptional
block, and leave only ordinary blocks outside. Thus all exceptional complexity
is compressed into actual nonnegative-credit macroblocks.

Detailed sources:

```text
docs/MINIMUM_BLOCK_BOUNDARY_CREDIT_BALLOT.md
tools/verify_minimum_block_boundary_credit_ballot.py
docs/EXCEPTIONAL_SPONSOR_ARCH_MACRO_EXIT.md
tools/verify_exceptional_sponsor_arch_macro_exit.py
```

## Sharp local length scales

The global cycle-value floor `n>N` sharpens the correction of every complete
block to

```text
kappa<ell/(X*N*ln(2)).
```

Exact rational comparison then gives, for every positive-credit nondecreasing
complete-block segment,

```text
L<C*2^4002/997<C*2^3993.
```

For `C<=4500`, the sharper uniform bound is

```text
L<2^4005.
```

The primary logarithmic drift has the exact two-bit upper sharpening

```text
delta=log2(B/X)<2^-3992.
```

Therefore every positive-credit segment which actually contracts satisfies

```text
y<x and C>=1  =>  L>C*2^3992.
```

A zero-credit sponsor arch always contracts by exact height-credit domination.

Sources:

```text
docs/PRIMARY_DELTA_TWO_BIT_SHARPENING.md
tools/verify_primary_delta_two_bit_sharpening.py
docs/CYCLE_FLOOR_LOCAL_CORRECTION_SHARPENING.md
tools/verify_cycle_floor_local_correction_sharpening.py
docs/EXCEPTIONAL_SPONSOR_ARCH_MACRO_EXIT.md
```

## New strongest exit-return decomposition

At the least boundary `z`, take:

1. the maximal sponsor arch beginning with block `0`, if one exists; or
2. otherwise the first pure ordinary block.

This gives an actual bounded sponsored macro-exit from `z` to `y` with

```text
z<y,
1<=C<=4500,
L_macro<2^4005.
```

If the first ordinary block sponsors a nested family of early exceptions, the
whole maximal nest is absorbed into this macro-exit. The remaining actual return
from `y` to `z` still satisfies

```text
R>=1,
L_return>R*2^3992>=2^3992.
```

Every return prefix ending at a complete-block boundary has credit

```text
Q>=1-C>=-4499.
```

Sources:

```text
docs/EXCEPTIONAL_SPONSOR_ARCH_MACRO_EXIT.md
tools/verify_exceptional_sponsor_arch_macro_exit.py
docs/PRIMARY_DELTA_TWO_BIT_SHARPENING.md
tools/verify_primary_delta_two_bit_sharpening.py
docs/CYCLE_FLOOR_LOCAL_CORRECTION_SHARPENING.md
tools/verify_cycle_floor_local_correction_sharpening.py
docs/MINIMUM_BLOCK_BOUNDARY_PURE_ORDINARY_EXIT.md
tools/verify_minimum_block_boundary_pure_ordinary_exit.py
```

## Decisive next target

Exclude the astronomically long positive-credit return after removing the
bounded initial sponsor nest. Work with the disjoint maximal sponsor arches on
the return:

1. every exception lies in an actual arch of credit at most `4499`;
2. a noncontracting positive-credit arch has
   `L<C*2^4002/997<C*2^3993`, while a contracting one has `L>C*2^3992`;
3. zero-credit arches always contract and are now the only macroblocks lacking a
   credit-proportional length lower bound;
4. combine arch endpoints with the permanent `N` and `1093^2` labels and the
   exceptional-source floor;
5. prove that the long return requires too many contracting arches, a repeated
   exact source class, an incompatible adjacent-label lift, or too much harmonic
   correction;
6. use `Q>=-4499` so no return prefix can use an unbounded exceptional reserve.

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
