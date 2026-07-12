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
docs/SESSION_CHECKPOINT_2026-07-12_POSITIVE_BOUNDARY_CIRCULATION.md
```

GitHub commits and certificate scripts are the durable source of truth.

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

For a hypothetical cycle let `J` be its number of ordinary complete blocks.
Exact signed elimination, continued fractions, and the finite cycle barrier prove

```text
Every hypothetical nontrivial positive cycle has J>=245833.
```

This allows arbitrary exceptional-block populations and arbitrary block lengths.
It is not a cycle-length cutoff.

Main files:

```text
docs/GLOBAL_ORDINARY_BLOCK_COUNT_FRONTIER.md
tools/verify_global_ordinary_block_count_frontier.py
```

## New bounded positive circulation

For each occurring ordinary terminal deficit `e`, choose the smallest cycle
boundary value `x_e` of that type. Follow its actual orbit to the next ordinary
boundary of type `f(e)` and value `y_e`. Minimality gives

```text
y_e>=x_(f(e)).
```

The functional graph on at most `4500` types contains a directed cycle. The
selected disjoint orbit intervals satisfy

```text
q<=4500,
1<=C<=20250000,
T<=20254499,
L*delta<C,
delta=log2(B/X).
```

Here `q` is the number of selected ordinary intervals, `C` their total net
credit, `T` the total number of selected complete blocks, and `L` their total
accelerated length. Therefore their formal base multiplier is strictly expanding:

```text
2^C*(X/B)^L>1.
```

The last inequality is strict. If it failed, the exact continued-fraction gap
would exceed `2^-4023`, while all selected additive corrections together are
strictly below `2^-4023`.

Main files:

```text
docs/MINIMUM_BOUNDARY_POSITIVE_CIRCULATION.md
tools/verify_minimum_boundary_positive_circulation.py
```

## Decisive missing theorem

The selected intervals form an expanding circulation of boundary types, but they
need not be consecutive in the original orbit. Their endpoints and the next
selected starts share the same class modulo `X`, yet may be different integers
and may belong to different two-adic word cylinders.

The next target is a splicing or regeneration theorem proving one of:

1. the selected intervals can be concatenated into an admissible growing orbit
   segment;
2. every nonzero mismatch creates a strict height descent;
3. the mismatch is impossible after lifting the boundary equation modulo `X^2`
   or a higher power.

Do not merely extend the continued-fraction denominator or enlarge the finite
cycle barrier.

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
- do not claim a complete repository run unless it completed.

## Reproduction

```text
python run_checks.py
```