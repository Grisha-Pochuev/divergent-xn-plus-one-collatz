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
docs/SESSION_CHECKPOINT_2026-07-11_BLOCK_LEDGER_AND_EXCEPTIONAL_SIEVE.md
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
X=2^156-9
 =91343852333181432387730302044767688728495783927,
n0=1.
```

Retained strict results:

- `1093` divides `X` exactly once, so the orbit leaves `1` and never returns;
- the first `48` steps have exact word `(3,1,2,2,5,6)^8`, total valuation `152`,
  and `n_48>X^48/2^152`;
- every ordinary complete near-power block has an exact proved sign;
- all positive cycle lengths through
  `7034970411803187993997906985047212163795395134` are impossible;
- every hypothetical cycle has a complete-block ledger with `D=156*p-A`
  restricted to a narrow integer strip;
- two adjacent least labels restrict every cycle value to one of `132496`
  classes modulo `1093^2`;
- every exceptional source satisfies `n>=(125*2^156+1)/9`.

Exact statements, proofs, and checkers are indexed in `docs/CURRENT_STATUS.md`.

## Decisive missing theorem

No theorem yet excludes every cycle above the finite barrier. The current target
is to prove that distinct cycle values in the `132496` permanent classes cannot
supply the exact block correction

```text
sum kappa_j=p*log2(2^156/X)-D.
```

Use together:

1. the narrow integer strip for `D`;
2. ordinary and exceptional block credits;
3. the exceptional-source floor;
4. distinct-value harmonic packing;
5. an unbounded height-dependent potential.

## Exact next work

1. Derive a harmonic packing inequality over the permanent classes.
2. Separate ordinary and exceptional sources.
3. Restrict admissible block-credit patterns using the integer strip for `D`.
4. Test a value-dependent height-credit potential.

Use one primary target and at most two exploratory directions. Full operational
rules are in `docs/WORKING_PROTOCOL.md`.

## Independent fallback branches

Retain independently:

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
