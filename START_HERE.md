# START HERE

Compact entry point for each research session.

## Strict target

Find explicit positive odd integers `X>=5` and `n0>=1` such that

```text
C_X(n)=(X*n+1)/2^v2(X*n+1)
```

tends to positive infinity under iteration.

A cycle, avoidance of `1`, a finite cycle barrier, arbitrarily long finite
growth, heuristic drift, or a huge finite trajectory is not a solution.

## Read first

```text
START_HERE.md
docs/WORKING_PROTOCOL.md
docs/CURRENT_STATUS.md
docs/RETRACTIONS.md
docs/SESSION_CHECKPOINT_2026-07-12_NO_EXCEPTIONAL_BLOCK_FRONTIER.md
```

Read detailed theorem files only when the current argument needs them. GitHub
commits and certificate scripts are the durable source of truth.

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
- exactly `16562000` combined permanent classes survive modulo
  `(2^500-1)*1093^2`;
- every cycle value is greater than `2^500-1`;
- all cycle lengths through `floor(2*X/(3*d))` are impossible, with

```text
10^1201<floor(2*X/(3*d))<10^1202;
```

- every exceptional source satisfies

```text
n>=(u_min*2^4501+1)/(349*2^500-347),
```

  where

```text
u_min=
141554173562669451979142234479211407387695161061947663158036275475013035570532072821977692485924548874811696146286209742307923384940182399969083204712328957713629782297601610389067903491331197096456313288013542743720638224927691460837892079910386115268969408753656537834465197519183303759432510875217219;
```

  the lower-bound source has `1505` decimal digits;
- every hypothetical cycle satisfies the global harmonic window

```text
0<p*delta-D
 <[C0+K*H_(ceil(p/K))/(2*M)]/(X*ln(2)),
C0<10^(-147),
K=16562000,
M=(2^500-1)*1093^2.
```

## New no-exceptional frontier

Suppose a hypothetical cycle has no exceptional complete block. Let `J` be its
number of ordinary complete blocks and

```text
D=4501*p-A=sum_(i=1)^J e_i,
1<=e_i<=4500.
```

Retained strict results:

1. Repeated valuation-`4501` steps form an `X`-adic ladder:

```text
d*F^j(n)==1 (mod X^j).
```

2. All `4500` terminal classes satisfy

```text
rho_e>X/(3*e).
```

3. Hence every no-exceptional cycle obeys

```text
sum_i 1/n_i
 <3*D/X+[d+H_D/2]/(X-1),
```

and

```text
0<p*delta-D
 <{3*D/X+[d+H_D/2]/(X-1)}/[X*ln(2)].
```

4. No ordinary one-block cycle exists for any deficit `1<=e<=4500` or any
cycle length.

5. No ordinary two-block cycle exists for any pair of deficits or lengths.

6. Continued-fraction and longest-block charging prove

```text
Any no-exceptional positive cycle must have J>=245833.
```

This is a block-count frontier, not a cycle-length cutoff.

Main files:

```text
docs/NO_EXCEPTIONAL_X_ADIC_LADDER.md
tools/verify_no_exceptional_x_adic_ladder.py

docs/NO_EXCEPTIONAL_ONE_BLOCK_ALL_CREDITS.md
tools/verify_no_exceptional_one_block_all_credits.py

docs/NO_EXCEPTIONAL_TWO_BLOCK_ALL_CREDITS.md
tools/verify_no_exceptional_two_block_all_credits.py

docs/NO_EXCEPTIONAL_BLOCK_COUNT_FRONTIER.md
tools/verify_no_exceptional_block_count_frontier.py
```

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
and an arbitrarily large finite cycle barrier.

Therefore increasing parameters merely to set a new record is not a priority.

## Decisive remaining split

Every still-possible cycle belongs to one of these branches:

```text
A. no exceptional blocks and at least 245833 ordinary blocks;
B. exactly one exceptional block;
C. at least two exceptional blocks.
```

## Exact next work

Primary target: branch B.

1. Write the cycle as one exceptional contraction followed by an ordinary
   segment.
2. Use the exact 1505-digit exceptional-source floor.
3. Apply the `X`-adic ladder to the ordinary segment.
4. Derive a closure inequality depending on the exceptional excess valuation.
5. Only then use residue or continued-fraction refinement.

For branch A, seek a many-block population theorem from repeated terminal
deficits and their exact classes modulo `X`. Do not merely extend the continued-
fraction denominator for a larger record.

## Independent fallback branches

Retain independently:

- `X=2^3803-4162203,n0=1`, with barrier above `10^1138`;
- `X=2^156-9,n0=1`, with barrier
  `7034970411803187993997906985047212163795395134`, first threshold
  `7034970411803187993997906985047212163795395135`, and exceptional floor
  `1268664615738631005385143083955106787895774776889`;
- `X=2^260-3,n0=1`;
- `X=15,n0=3`;
- `X=9,n0=1`;
- the old fixed candidate with two surviving lengths and `Q<=6241`.

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
used by a cycle. Do not present finite height, a finite barrier, or heuristic
drift as divergence.

## Verification discipline

- Commit each theorem, checker, decisive refutation, and major strategy change
  as a logical unit.
- State exactly which checks ran.
- Do not claim a complete repository run unless it completed.

## Reproduction

```text
python run_checks.py
```
