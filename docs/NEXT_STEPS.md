# Prioritized next steps

The strict prize problem remains open.  This file records the current research
frontier; operational rules are in `docs/WORKING_PROTOCOL.md`.

## Primary candidate

```text
X=2^156-9
 =91343852333181432387730302044767688728495783927,
n0=1.
```

Closed gates:

- explicit pair;
- the orbit leaves `1` and never returns;
- the positive bounded-orbit dichotomy is available;
- exact block formulas, checkers, and a large finite cycle barrier are retained.

Open decisive gate:

- exclude every nontrivial positive cycle.

## Current exact obstruction

Every hypothetical cycle has a canonical complete-block ledger.  If `p` is its
length, `A` its total valuation, and

```text
D=156*p-A,
```

then `D` lies in a narrow integer strip and is the exact sum of ordinary terminal
deficits minus exceptional excess valuations.

Two adjacent least labels restrict every cycle value to one of exactly `132496`
classes modulo `1093^2`.  Every exceptional source also satisfies

```text
n>=(125*2^156+1)/9.
```

The missing theorem is to prove that distinct values under these restrictions
cannot supply the required exact correction

```text
sum kappa_j=p*log2(2^156/X)-D
```

around a complete cycle.

## Work package A: harmonic packing over permanent classes

1. Enumerate the ordered permanent residue classes symbolically or by an exact
   certificate.
2. Derive an upper bound for the reciprocal contribution of distinct values in
   those classes.
3. Keep the bound dependent on the integer `D` or the block-credit data instead
   of replacing them by a uniform worst case too early.
4. Combine the result with the exact correction identity.
5. Accept only a rational or interval-certified contradiction.

Success means either excluding all cycle lengths or producing a strictly smaller
explicit infinite frontier with a clear next obstruction.

## Work package B: separate ordinary and exceptional sources

1. Charge every exceptional block by its exact excess valuation and height loss.
2. Use the exceptional-source floor and the permanent residue sieve together.
3. Bound how many exceptional sources can occur at each height scale.
4. Prove that ordinary blocks cannot compensate the resulting loss around a
   complete cycle.

A useful intermediate theorem may concern an infinite family of block patterns;
it need not close the full problem immediately.

## Work package C: value-dependent height credit

Seek an unbounded potential depending on the actual integer height, for example
a logarithmic or piecewise logarithmic credit, such that complete blocks satisfy
an inequality of the form

```text
block gain >= potential change + certified global charge.
```

The fixed finite-state positive-mean architecture is ruled out.  Value-dependent
potentials and finite-state components used inside a larger proof remain allowed.

## Exploratory directions

At most two may run beside the primary target:

- test exact renewal mechanisms for the six-step map;
- search for stronger congruence information modulo higher powers or an
  additional prime;
- transfer the block-credit method to `X=2^260-3`;
- revisit the `X=15` or `X=9` branches if a new lemma materially improves them;
- revisit the old `Q=6241` branch when a new global packing theorem applies.

The old fixed candidate is a fallback branch, not a mandatory `Priority 1`.

## Computation policy

Short symbolic, modular, trajectory, finite-state, satisfiability, residue, and
word experiments are allowed for hypothesis formation and exact sublemmas.

Before a large computation, specify:

1. the mathematical question;
2. success and failure outputs;
3. the stopping rule;
4. the relation to an infinite proof;
5. the artifact to commit.

Do not run a large search merely to enlarge a record or cutoff.  Large work does
not require a separate user confirmation when it is reproducible, resource-aware,
and directly tied to a stated proof target; costly external runs should still be
identified clearly.

## Proof discipline

- A finite barrier is not divergence.
- A long growing trajectory is evidence only.
- Conclusions may move between branches only after hypotheses are checked.
- Record decisive dead ends in `docs/RETRACTIONS.md` without banning nearby
  methods more broadly than the no-go proof supports.
- Commit each theorem, checker, refutation, and major strategy change as a
  logical unit; batch minor maintenance.

## Recommended next session

> Start with work package A.  Build a `D`-dependent reciprocal packing bound over
> the `132496` permanent classes, then test whether exceptional-source charging
> closes the remaining correction gap.  Keep one height-credit experiment as a
> parallel route.
