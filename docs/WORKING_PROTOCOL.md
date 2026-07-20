# Working protocol

High-resource research and verification rules for the web-chat project.  The
protocol must maximize the chance of solving the strict prize problem while
preserving mathematical auditability.

## 1. Startup and source roles

At the beginning of a new chat read, at minimum, in order:

```text
START_HERE.md
docs/WORKING_PROTOCOL.md
docs/CURRENT_STATUS.md
```

These three files are the compact entry point, not a ceiling on context.  Read
any theorem file, checker, result, commit, issue, historical checkpoint,
retraction, archive, or the whole repository whenever it may help.  Broad
repository inspection and repeated targeted searches are explicitly allowed.
Avoid only redundant re-fetches of unchanged material that add no information.

Durable source hierarchy:

1. committed theorem documents and exact checkers;
2. `docs/CURRENT_STATUS.md` for the current frontier;
3. `START_HERE.md` for routing and the decisive obstruction;
4. chat summaries only as a convenience.

If these disagree, inspect the latest commits and repair the durable files before
continuing research.

## 2. Research scope and parallelism

Keep one clearly stated primary proof target for reporting, but impose no fixed
cap on the number of exploratory directions.  Work on as many mathematical,
computational, literature, candidate-search, or formal-verification routes as are
useful.  Parallel exploration is allowed.  Re-rank, combine, suspend, or discard
routes whenever evidence changes their prospects.

For every serious direction, record its exact intended contribution and its
current obstruction.  A request to continue authorizes a sustained research
session across multiple methods, candidates, and computations.  Normal research
steps, reproducible experiments, checker construction, and commits do not require
additional permission.

The primary candidate is not protected from replacement.  Screen alternative
multipliers and starts whenever that has a credible chance of producing a
stronger invariant or a complete proof.

## 3. Claim discipline

Internally classify every substantial claim as:

- `theorem`: complete written proof;
- `certificate`: exact finite computation;
- `evidence`: experiment or heuristic;
- `refutation`: explicit flaw or counterexample;
- `open target`: exact missing lemma.

Never promote evidence to a theorem.  In particular, none of these alone proves
divergence:

- a very long or very large finite trajectory;
- positive heuristic drift;
- a finite cycle barrier;
- arbitrarily long finite growing words;
- avoidance of `1`;
- a compatible 2-adic construction without an ordinary positive orbit.

These are mathematical safeguards, not performance restrictions, and they must
remain in force under every subscription or compute level.

## 4. Computation policy

Symbolic algebra, modular arithmetic, trajectory experiments, exhaustive finite
searches, SAT/SMT, proof assistants, continued fractions, integer programming,
graph searches, residue automata, local programs, and GitHub Actions are allowed
at any useful scale supported by the available environment.

Before a substantial computation, record in the code, run metadata, or research
note:

1. the exact mathematical question;
2. success and refutation conditions;
3. the stopping rule or resource budget;
4. how either outcome changes the infinite proof strategy;
5. the reproducible artifact to save.

This recording requirement does not require asking the user for permission.
Cutoffs may be enlarged, methods may be changed, and several searches may be run
when there is a stated mathematical reason.  Stop or redesign a computation only
when it ceases to inform an infinite argument, is dominated by a better method,
or reaches an actual platform/resource limit.

A finite computation counts as a proof only for the finite proposition it
exhaustively certifies.  It counts as progress toward divergence when it closes a
stated frontier, validates a global lemma, supplies a formally checkable
certificate, or decisively refutes a route.

## 5. Proof and verification

For each new theorem:

1. state hypotheses and conclusion exactly;
2. test known small cycles or another regression example;
3. add an exact checker when practical;
4. state limitations;
5. connect it to the strict prize target.

Run standalone checkers, independent cross-checks, and the full `run_checks.py`
suite whenever they are useful.  There is no protocol-imposed restriction that
the full suite be reserved for milestones.  Never claim a repository-wide run
unless it completed, and record any failed or skipped components.

When literature is used, search broadly and independently audit the exact lemma
needed.  Publication, citation count, or an author's claim alone does not make a
statement a trusted dependency.

## 6. Commits and durable memory

Prefer coherent result commits when theorem, checker, and status form one result,
but impose no fixed cap on the number of commits in a session.  Separate commits
are appropriate for independently reusable results, experiments, retractions,
regression fixes, infrastructure, or strategy changes.  Sequential file-update
commits caused by the GitHub tool are acceptable; identify the final head clearly.

Update:

- theorem/checker files for detailed mathematics;
- `docs/CURRENT_STATUS.md` after a major mathematical result;
- `START_HERE.md` when the candidate, proof gates, decisive obstruction, startup
  routing, or operating mode changes;
- `docs/RETRACTIONS.md` when a committed argument is invalidated.

Create a session checkpoint when it materially improves recovery or preserves a
complex handoff.  Checkpoints become historical after their contents are absorbed
into the authoritative files.

Do not use `docs/LATEST_VALID_PROGRESS.md` as current memory; it is only a
compatibility pointer.

## 7. Errors and dead ends

When an error is found:

1. identify the exact false premise;
2. give a small counterexample when possible;
3. add or update a regression checker;
4. remove the invalid conclusion from current status files;
5. record the retraction without deleting audit history;
6. restart from the last valid statement.

A failed method must not be banned more broadly than the proof of failure
supports.  Negative results should narrow the strategy, not create arbitrary
permanent prohibitions.

## 8. Interruption recovery

After a lag, tool failure, or new chat:

1. inspect the latest confirmed head;
2. read the three startup files;
3. verify the primary candidate and decisive obstruction;
4. reuse committed artifacts instead of repeating work unnecessarily;
5. continue from the last confirmed write or fetched SHA.

A tool failure is not a reason to shrink the research program permanently.  Retry
with a different tool, split the computation, use a branch or Action, or save a
partial certified result when appropriate.

## 9. Reporting

Report separately:

- proof gates closed and open;
- exact finite frontiers;
- reusable infinite-family structure;
- the decisive missing theorem;
- checks actually run;
- files and commits created;
- actual environment limitations encountered.

A percentage may be given only as a clearly subjective research-maturity estimate,
not as a probability of imminent solution.

## 10. Unrestricted research mode

There are no repository-imposed caps on:

- files or commits inspected;
- web or literature searches;
- tool calls;
- active hypotheses or candidate multipliers;
- symbolic or numerical experiments;
- local or GitHub Actions computations;
- theorem files, checkers, branches, or commits produced in one session.

Use the maximum resources that are actually available and scientifically useful.
Optimize for lower context or compute use only after a real bottleneck, error, or
cost is observed; do not pre-emptively weaken the investigation because an older
chat or subscription once lagged.

Actual platform limits, tool availability, safety rules, and reproducibility
requirements still apply.  The protocol does not assume that any subscription
makes compute literally unlimited.  It removes the project's former artificial
limits while retaining all correctness and audit safeguards.