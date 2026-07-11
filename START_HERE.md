# START HERE

This is the compact entry point for every new research session.

## Strict target

Find explicit positive odd integers `X>=5` and `n0>=1` such that

```text
C_X(n)=(X*n+1)/2^v2(X*n+1)
```

satisfies

```text
C_X^t(n0)->+infinity.
```

A cycle, avoidance of `1`, a finite cycle barrier, arbitrarily long finite
growth, heuristic drift, or a huge finite trajectory is not a solution.

## Read first

Read only this compact startup set by default:

```text
START_HERE.md
docs/WORKING_PROTOCOL.md
docs/CURRENT_STATUS.md
docs/RETRACTIONS.md
docs/SESSION_CHECKPOINT_2026-07-11_BLOCK_LEDGER_AND_EXCEPTIONAL_SIEVE.md
```

Read `docs/VALIDATED_RESULTS.md`, older checkpoints, and detailed theorem files
only when the current argument needs them.  GitHub commits and certificates are
the durable source of truth.

## How progress is measured

Do not convert preparatory results into one precise proof percentage.  Report
separately:

1. strict proof gates;
2. exact finite frontiers;
3. reusable infinite-family structure;
4. the decisive missing theorem.

For the primary candidate, the explicit-pair gate, no-return gate, and general
positive bounded-orbit dichotomy are available.  The global exclusion of every
nontrivial positive cycle remains open.

## Primary candidate

```text
X=2^156-9
 =91343852333181432387730302044767688728495783927,
n0=1.
```

### Retained strict results

- The Wieferich prime `1093` divides `X` exactly once.
- The orbit leaves `1` and never returns to `1`.
- The first `48` accelerated steps have exact valuation word

```text
(3,1,2,2,5,6)^8
```

  with total valuation `152`, `v2(n_48-1)=4`, and
  `n_48>X^48/2^152`.
- Every ordinary complete near-power block has an exact proved growth or
  contraction sign.
- Every positive cycle length through

```text
7034970411803187993997906985047212163795395134
```

  is impossible.  This is still only a finite barrier.
- Every hypothetical cycle has an exact complete-block ledger.  With cycle
  length `p`, total valuation `A`, and

```text
D=156*p-A,
```

  one has

```text
D=sum ordinary deficits-sum exceptional excesses
```

  and a narrow exact strip for `D`.
- Two adjacent least valuation labels determine each cycle value modulo
  `1093^2`.  Exactly `132496` permanent residue classes survive.
- Combining the exceptional-source progression with that sieve gives

```text
n>=(125*2^156+1)/9
```

  for every exceptional source in a hypothetical cycle.

Detailed statements and checkers are indexed in `docs/CURRENT_STATUS.md`.

## Decisive missing theorem

No theorem yet excludes every cycle above the finite barrier.

The current target is to prove that distinct values constrained to the `132496`
permanent residue classes cannot provide the exact correction sum

```text
sum kappa_j=p*log2(2^156/X)-D
```

around a complete cycle.

The intended ingredients are:

1. the narrow integer strip for `D`;
2. exact ordinary and exceptional block credits;
3. the exceptional-source floor;
4. distinct-value harmonic packing;
5. an unbounded height-dependent potential.

## Exact next work

1. Derive a rigorous harmonic packing inequality over the `132496` permanent
   classes.
2. Separate ordinary and exceptional sources and use the exceptional floor.
3. Use the integer strip for `D` to restrict admissible block-credit patterns.
4. Test a height-credit potential that depends on the actual value, not on a
   fixed finite-state quotient.

One primary target and at most two exploratory directions may be active.  The
full operational policy is in `docs/WORKING_PROTOCOL.md`.

## Independent fallback branches

Retain, but do not confuse with the primary proof:

- `X=2^260-3,n0=1`: stronger finite barrier and exact first `172` steps;
- `X=15,n0=3`: complete Mersenne blocks and second-block escalation;
- `X=9,n0=1`: direct cumulative-valuation target `A_t<=3*t-1`;
- the old fixed candidate with two surviving cycle lengths and `Q<=6241` for
  the first one.

Methods and lemmas may move between branches when hypotheses are checked.
Conclusions may not.

## Non-negotiable corrections

Never use

```text
2^A==1 (mod X).
```

The correct cycle congruence is

```text
2^A*product_i(n_i)==1 (mod X).
```

Never identify the least admissible predecessor source with the source actually
used by a cycle.

Never present finite height, a finite barrier, a finite growing program, or a
probabilistic drift estimate as divergence.

The no-go theorem rules out only a fixed finite-state telescoping proof with a
universal positive mean on all zero-layer transitions.  It does not ban
finite-state, SAT, residue, or word-search methods as exploratory tools or as
certificates for precise finite sublemmas.

## Commit and verification rule

- Commit each theorem, independent checker, decisive refutation, and major
  strategy change as a logical unit.
- Batch trivial wording and maintenance edits.
- State exactly which checks ran.
- Do not claim a full repository run unless it completed.
- Update `START_HERE.md` only when the main branch, decisive obstruction,
  startup sequence, or critical safety rule changes.

## Reproduction

```text
python run_checks.py
```
