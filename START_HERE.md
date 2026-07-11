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
docs/SESSION_CHECKPOINT_2026-07-12_MERSENNE_DIVISOR_FAMILY_FRONTIER.md
```

Read `docs/VALIDATED_RESULTS.md`, older checkpoints, and detailed theorem files
only when the current argument needs them. GitHub commits and certificates are
the durable source of truth.

## Progress rule

Do not report one precise proof percentage. Report separately:

1. strict proof gates;
2. exact finite frontiers;
3. reusable infinite-family structure;
4. the decisive missing theorem.

For the primary candidate the explicit-pair, no-return, and positive
bounded-orbit dichotomy gates are available. Exclusion of every nontrivial
positive cycle remains open.

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

Retained strict results:

- `N|X`, so every output lies in only `500` one-label classes modulo `N`;
- `1093` divides `X` exactly once, so the orbit leaves `1` and never returns;
- exactly `16562000` combined permanent classes survive modulo
  `(2^500-1)*1093^2`;
- every hypothetical cycle value is greater than `2^500-1`;
- the combined base reciprocal constant is below `10^(-147)` and the harmonic
  tail coefficient is below `10^(-149)`;
- all positive cycle lengths through `floor(2*X/(3*d))` are impossible, with

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
- with

```text
D=4501*p-A,
delta=log2(2^4501/X),
K=16562000,
M=(2^500-1)*1093^2,
C0=(500/(2^500-1))*(1+H_33124/2),
```

  every hypothetical cycle satisfies

```text
0<p*delta-D
 <[C0+K*H_(ceil(p/K))/(2*M)]/(X*ln(2)),
C0<10^(-147).
```

Exact statements, proofs, and checkers are indexed in `docs/CURRENT_STATUS.md`.

## Reusable family theorem

For

```text
N=2^k-1,
m==r (mod k),
d=2^r+t*N,
X=2^m-d,
```

with `364` not dividing `k`, one can choose a parity-correct `t<2*1093^2`
such that `1093||X`. For sufficiently large `m`, this gives:

- no return to `1` from `n0=1`;
- exactly `k` one-label classes modulo `N`;
- `364*lcm(k,364)` combined classes modulo `N*1093^2`;
- exponentially shrinking harmonic constants;
- an arbitrarily large finite cycle barrier.

Therefore increasing `k` or `m` merely to set a new finite record is not a
priority. The missing theorem must use dynamic transition or height structure.

## Decisive missing theorem

No theorem yet excludes every cycle above the finite barrier. The current target
is to combine the logarithmic harmonic window with the exact near-power block
ledger

```text
D=sum ordinary deficits-sum exceptional excesses.
```

The first split is:

```text
no exceptional blocks;
exactly one exceptional block;
at least two exceptional blocks.
```

The desired contradiction must use together:

1. compatible `500`- and `364`-label sequences;
2. ordinary and exceptional block credits;
3. the 1505-digit exceptional-source floor;
4. distinct-value harmonic packing;
5. a height-dependent lower bound for `p*delta-D`.

## Exact next work

1. Derive the strongest correction lower bound when there are no exceptional
   blocks.
2. Treat exactly one exceptional block using its exact source floor and descent
   coordinate.
3. Treat two or more exceptional blocks using distinct sources and harmonic
   packing.
4. Compare each lower bound with the harmonic upper window.
5. Use continued fractions only after the block-credit structure restricts
   `(p,D)`.

Use one primary target and at most two exploratory directions. Full operational
rules are in `docs/WORKING_PROTOCOL.md`.

## Independent fallback branches

Retain independently:

- `X=2^3803-4162203,n0=1`, with `17886960` classes modulo
  `14726582775529`, barrier above `10^1138`, and exceptional floor
  `(19567017189655*2^3803+1)/4162203`;
- former primary `X=2^156-9,n0=1`, with barrier
  `7034970411803187993997906985047212163795395134`, first block threshold
  `7034970411803187993997906985047212163795395135`, and exceptional floor
  `1268664615738631005385143083955106787895774776889`;
- `X=2^260-3,n0=1`;
- `X=15,n0=3`;
- `X=9,n0=1`;
- the old fixed candidate with two surviving cycle lengths and `Q<=6241` for
  the first one.

Methods and lemmas may move between branches after checking hypotheses.
Conclusions may not.

## Non-negotiable corrections

Do not use the false relation

```text
2^A==1 (mod X).
```

The correct cycle congruence is

```text
2^A*product_i(n_i)==1 (mod X).
```

Do not identify the least admissible predecessor source with the source actually
used by a cycle. Do not present finite height, a finite barrier, a finite growing
program, or probabilistic drift as divergence.

The finite-state no-go theorem rules out only a fixed finite-state telescoping
proof with universal positive mean on all zero-layer transitions. It does not
ban finite-state, satisfiability, residue, or word-search methods as exploratory
tools or as certificates for precise finite sublemmas.

## Commit and verification

- Commit each theorem, checker, decisive refutation, and major strategy change
  as a logical unit.
- Batch trivial maintenance edits.
- State exactly which checks ran.
- Do not claim a full repository run unless it completed.
- Update this file only when the main branch, decisive obstruction, startup
  sequence, or critical safety rule changes.

## Reproduction

```text
python run_checks.py
```
