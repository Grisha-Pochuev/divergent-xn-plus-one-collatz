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

## Current frontier

Retained global facts include `N|X`, `1093||X`, `16562000` permanent classes,
cycle values above `N`, exclusion through the `10^1201` window, and at least
`245833` ordinary complete blocks in every hypothetical cycle.

Every hypothetical cycle has an actual expanding exit from its least ordinary
boundary `x` to the next ordinary boundary `y>x` with

```text
1<=C<=4500,
L_exit<2^4006.
```

Let `R` and `Lr` be the credit and accelerated length of the remaining actual
return from `y` to `x`.

A new general block-correction theorem proves that every near-power cycle obeys

```text
p < 2*D*B*X/[d*(X-d)],
```

where `D` is total cycle credit. If `R<=0`, then `1<=D<=4500`, and exact integer
comparison gives

```text
p<2^4006.
```

The retained harmonic theorem simultaneously gives

```text
p>Lr>2^(2^974).
```

Therefore the entire nonpositive-return branch is impossible.

The only surviving branch is now

```text
R>=1,
Lr>2^3990.
```

Detailed sources:

```text
docs/NONPOSITIVE_RETURN_BLOCK_CORRECTION_EXCLUSION.md
tools/verify_nonpositive_return_block_correction_exclusion.py
docs/MINIMUM_BOUNDARY_ACTUAL_EXPANDING_SEGMENT.md
docs/MINIMUM_BOUNDARY_RETURN_CREDIT_DICHOTOMY.md
docs/MINIMUM_BOUNDARY_NONPOSITIVE_RETURN_HARMONIC_BARRIER.md
```

## Surviving branch and next target

Primary next target: exclude the positive-credit return from `y>x` to the least
ordinary boundary `x`.

Use the exact return equation

```text
ln(x/y)=R*ln(2)-Lr*ln(B/X)+K_return<0
```

together with the cycle-wide block-correction inequality. Seek either:

1. a quantitative restriction on `R/Lr` incompatible with cyclic closure;
2. a forced placement or repetition pattern for the positive ordinary deficits;
3. a global divisor/source-matching obstruction that remains effective when
   total credit `D` is not bounded by `4500`;
4. an explicit linear-form-in-logarithms bound only if its constants beat the
   actual correction terms.

Do not return to the now-closed nonpositive branch. Do not use finite same-type
windows or any fixed finite `N`-adic ladder as a standalone contradiction.

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
