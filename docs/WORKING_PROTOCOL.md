# Working protocol

This file contains operational rules for future research sessions.  It is meant
to reduce chat drift and duplicated work without forbidding useful methods.

## 1. Session startup

At the beginning of a new session read, in this order:

```text
START_HERE.md
docs/WORKING_PROTOCOL.md
docs/CURRENT_STATUS.md
docs/RETRACTIONS.md
the single latest checkpoint named in START_HERE.md
```

Read `docs/VALIDATED_RESULTS.md` and older checkpoints only when a concrete
argument needs them.  Do not load the whole repository into context by default.

GitHub files and committed certificates are the durable source of truth.  Chat
memory is secondary.

## 2. Research focus

Use:

- one primary proof target;
- at most two parallel exploratory directions;
- one clearly stated next obstruction for each active direction.

Parallel conceptual work is allowed.  Methods and lemmas may be transferred
between branches, but conclusions may not be transferred without a proof that
the hypotheses match.

Do not stay on an old priority merely because it was previously called
`Priority 1`.  Re-rank branches when a new theorem changes their prospects.

## 3. Status labels

Every substantial claim must be labeled internally as one of:

- **theorem**: a complete argument is written;
- **certificate**: exact computation verifies a finite statement;
- **evidence**: experiment or heuristic only;
- **refutation**: an explicit flaw or counterexample closes a claim;
- **open target**: a precisely stated missing lemma.

Never promote evidence to a theorem.  In particular, none of the following is a
proof of divergence by itself:

- a very large finite trajectory;
- positive heuristic drift;
- a finite cycle barrier;
- arbitrarily long finite growing words;
- avoidance of `1`;
- a compatible 2-adic construction without one ordinary positive orbit.

## 4. Computation policy

Short symbolic, modular, and trajectory experiments are allowed when they help
form or test a precise conjecture.

Before a large computation, write down:

1. the exact mathematical question;
2. what output would count as success or refutation;
3. the stopping rule;
4. how the result would contribute to an infinite proof;
5. what reproducible artifact will be saved.

Do not enlarge cutoffs merely to obtain a larger record.  A larger finite
barrier counts as progress only when it closes a stated finite frontier or
supports a new global lemma.

Finite-state, SAT, word-search, and residue-search methods are not banned in
general.  They may be used for exploration, exact sublemmas, or certificates.
What is ruled out is only a proof form already contradicted by a no-go theorem,
such as a fixed finite-state telescoping potential with a universal positive
mean on all zero-layer transitions.

## 5. Proof and verification policy

For each new theorem:

1. state hypotheses and conclusion exactly;
2. test it against known small cycles or a regression example;
3. add an exact checker when practical;
4. record limitations explicitly;
5. connect it to the strict prize target.

If only standalone checks were run, say so.  Do not claim a repository-wide run
unless it actually completed.

When external literature is used, audit the exact lemma needed.  A published
claim is not a dependency until its relevant proof has been independently
checked.

## 6. Commit policy

Create a separate logical commit for:

- a new theorem;
- a new independent checker;
- a decisive refutation or retraction;
- a major status or strategy change.

Batch small wording fixes, link repairs, and minor checker maintenance into one
coherent commit.  Do not create a separate commit for every trivial edit.

After a major result update `CURRENT_STATUS.md`.  Update `START_HERE.md` only
when the primary branch, decisive obstruction, startup sequence, or critical
safety rule changes.

## 7. Progress reporting

Do not report one precise proof percentage unless a weighting scheme was fixed
in advance.

Report separately:

- strict proof gates closed or open;
- exact finite frontiers;
- reusable infinite-family structure;
- the single decisive missing theorem.

A subjective research-maturity estimate may be given only if clearly labeled
as subjective and not as the probability that the proof is nearly complete.

## 8. Handling errors and dead ends

When an error is found:

1. identify the false premise;
2. give a small counterexample when possible;
3. add or update a regression checker;
4. remove the invalid conclusion from current status files;
5. record the history in `docs/RETRACTIONS.md`;
6. restart from the last valid statement.

Do not delete audit history.

A failed method should not be banned more broadly than the proof of failure
supports.  Record exactly which claim or proof architecture is impossible and
which nearby uses remain allowed.

## 9. Recovery after interruption

After a lag, tool failure, or new chat:

1. inspect the latest commits;
2. read the startup files from Section 1;
3. verify the current primary candidate and missing theorem;
4. do not repeat a computation unless its artifact or result is absent;
5. continue from the latest committed checkpoint, not from an uncertain chat
   recollection.

## 10. End-of-session checkpoint

At the end of a substantial session record:

- strict results proved;
- checks actually run;
- refutations discovered;
- files and commits created;
- the exact next target;
- any environment limitation.

The checkpoint should be concise and should link to detailed theorem files
instead of copying them.