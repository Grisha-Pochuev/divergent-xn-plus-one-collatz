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
docs/SESSION_CHECKPOINT_2026-07-12_GLOBAL_BLOCK_COUNT_FRONTIER.md
```

GitHub commits and certificate scripts are the durable source of truth.

## Primary candidate

```text
k=500,
N=2^500-1,
m=4501,
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
- exactly `16562000` permanent classes survive modulo `(2^500-1)*1093^2`;
- every cycle value is greater than `2^500-1`;
- every exceptional source has at least `1505` decimal digits;
- every cycle length through a number between `10^1201` and `10^1202` is
  impossible;
- every hypothetical cycle satisfies the logarithmic harmonic window recorded
  in `docs/MERSENNE_DIVISOR_WIEFERICH_FAMILY.md`.

## New global block frontier

Let

```text
J = number of ordinary complete blocks,
R = number of exceptional complete blocks,
E = sum ordinary deficits,
F = sum exceptional excesses,
D = E-F = 4501*p-A.
```

Exact signed block elimination proves:

```text
Every hypothetical nontrivial positive cycle has J>=245833.   (1)
```

This holds for every number `R` of exceptional blocks and arbitrary block
lengths. It is not a cycle-length cutoff.

The proof uses:

1. the continued-fraction gap for every `D<1106246945`;
2. a signed closure identity in which ordinary blocks are positive terms and
   exceptional blocks are negative terms;
3. the consequences, when `J<=245832`,

```text
every ordinary block length <=2J+6;
every exceptional block length <=2J+5;
R<=4500J-1;
```

4. hence

```text
p<=544026748963771<10^15,
```

contradicting the retained barrier `p>10^1201`.

Main files:

```text
docs/GLOBAL_ORDINARY_BLOCK_COUNT_FRONTIER.md
tools/verify_global_ordinary_block_count_frontier.py
```

Earlier strict subresults remain valid:

- no cycle with one or two ordinary blocks and no exceptional block;
- no cycle with one exceptional block and one ordinary block;
- the `X`-adic ladder and all `4500` exact terminal classes.

## Decisive missing theorem

The small-block branches have been unified. Every remaining hypothetical cycle
has at least `245833` ordinary blocks.

The next target is a genuine many-block population theorem using together:

1. only `4500` possible ordinary terminal deficits;
2. repeated boundary classes modulo `X` and `N=2^500-1`;
3. the credit budget `F=E-D` for all exceptional blocks;
4. the `X`-adic ladder inside long valuation-`4501` runs;
5. a height-dependent argument, not a fixed finite-state positive-mean
   potential.

A first unavoidable population fact is that at least one ordinary deficit occurs
at least `55` times. This alone is not yet the missing contradiction; the task is
to convert repeated deficit classes into a shorter positive-credit segment,
height descent, or an impossible closure congruence.

Do not merely extend the continued-fraction denominator or enlarge the finite
cycle barrier for a new record.

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
and an arbitrarily large finite cycle barrier. Increasing parameters alone is
therefore not a priority.

## Independent fallback branches

Retain independently:

- `X=2^3803-4162203,n0=1`;
- `X=2^156-9,n0=1`;
- `X=2^260-3,n0=1`;
- `X=15,n0=3`;
- `X=9,n0=1`;
- the old fixed candidate with two surviving cycle lengths.

Methods may move between branches only after checking hypotheses.

## Non-negotiable corrections

Do not use the false relation

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