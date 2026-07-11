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
docs/SESSION_CHECKPOINT_2026-07-12_DUAL_WIEFERICH_HARMONIC_FRONTIER.md
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
m=3803,
B=2^3803,
d=4162203,
X=B-d,
n0=1.
```

Retained strict results:

- `3511^2` divides `X`, giving a one-label permanent sieve;
- `1093` divides `X` exactly once, so the orbit leaves `1` and never returns;
- exactly `17886960` combined permanent classes survive modulo
  `14726582775529`;
- their density is between `91312` and `91313` times smaller than the former
  primary `X=2^156-9` sieve density;
- all positive cycle lengths through `floor(2*X/(3*d))` are impossible; this
  exact barrier has `1139` digits and exceeds `10^1138`;
- every exceptional source satisfies

```text
n>=(19567017189655*2^3803+1)/4162203;
```

- every hypothetical cycle of length `p`, with

```text
D=3803*p-A,
delta=log2(2^3803/X),
K=17886960,
M=14726582775529,
```

  satisfies the global harmonic window

```text
0<p*delta-D
 <[1/853 + K*H_(ceil(p/K))/(2*M)]/(X*ln(2)).
```

Exact statements, proofs, and checkers are indexed in `docs/CURRENT_STATUS.md`.

## Decisive missing theorem

No theorem yet excludes every cycle above the finite barrier. The current target
is to combine the logarithmic harmonic window with the exact near-power block
ledger

```text
D=sum ordinary deficits-sum exceptional excesses.
```

The desired contradiction must use together:

1. the permanent class density;
2. the exceptional-source floor;
3. distinct-value harmonic packing;
4. ordinary and exceptional block credits;
5. a height-dependent or Diophantine lower bound for `p*delta-D`.

## Exact next work

1. Split hypothetical cycles by the number of exceptional blocks.
2. Charge every exceptional contraction using its permanent source floor.
3. Derive a block-credit-dependent lower bound for `p*delta-D`.
4. Compare it with the harmonic upper window.
5. Use continued fractions only after the credit structure restricts `(p,D)`.

Use one primary target and at most two exploratory directions. Full operational
rules are in `docs/WORKING_PROTOCOL.md`.

## Independent fallback branches

Retain independently:

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
