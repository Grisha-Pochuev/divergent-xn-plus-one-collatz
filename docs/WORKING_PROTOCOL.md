# Working protocol

Operational rules for reliable web-chat research without unnecessary context or
tool overhead.

## 1. Startup and source roles

At the beginning of a new chat read, in order:

```text
START_HERE.md
docs/WORKING_PROTOCOL.md
docs/CURRENT_STATUS.md
```

Read each once unless it changes. Do not load the whole repository by default.
Open theorem files, old checkpoints, `docs/RETRACTIONS.md`, or archive files only
when a concrete argument needs them.

Durable source hierarchy:

1. committed theorem documents and exact checkers;
2. `docs/CURRENT_STATUS.md` for the current frontier;
3. `START_HERE.md` for routing and the decisive obstruction;
4. chat summaries only as a convenience.

If these disagree, inspect the latest commits and repair the durable files before
continuing research.

## 2. Research focus

Maintain:

- one primary proof target;
- at most two active exploratory directions;
- one explicit obstruction for each active direction.

A third idea may be screened briefly, but must be discarded or replace an active
direction. Re-rank routes when a new theorem changes their prospects. Do not stay
on a branch merely because it was previously called a priority.

A request to continue authorizes one substantial sprint. Select the strongest
available route and work until a checked result, a rigorous no-go, or a precisely
located obstruction is obtained.

## 3. Claim discipline

Internally classify every substantial claim as:

- `theorem`: complete written proof;
- `certificate`: exact finite computation;
- `evidence`: experiment or heuristic;
- `refutation`: explicit flaw or counterexample;
- `open target`: exact missing lemma.

Never promote evidence to a theorem. In particular, none of these alone proves
divergence:

- a very long or very large finite trajectory;
- positive heuristic drift;
- a finite cycle barrier;
- arbitrarily long finite growing words;
- avoidance of `1`;
- a compatible 2-adic construction without an ordinary positive orbit.

## 4. Computation policy

Short symbolic, modular, trajectory, SAT/SMT, word, and residue experiments are
allowed when they test a precise conjecture.

Before a large computation record:

1. the exact mathematical question;
2. success and refutation conditions;
3. the stopping rule;
4. how the result could contribute to an infinite proof;
5. the reproducible artifact to save.

Do not enlarge a cutoff merely to improve a record. A finite computation counts
as progress only when it closes a stated finite frontier or supports a new global
lemma.

## 5. Proof and verification

For each new theorem:

1. state hypotheses and conclusion exactly;
2. test known small cycles or a regression example;
3. add an exact checker when practical;
4. state limitations;
5. connect it to the strict prize target.

Run the new standalone checker first. Run the full `run_checks.py` suite only
before a major public milestone, after shared-infrastructure changes, when a new
result may affect many older claims, or in an environment that can execute it
reliably. Never claim a repository-wide run unless it completed.

When literature is used, independently audit the exact lemma needed. Publication
alone does not make a claim a trusted dependency.

## 6. Commits and durable memory

Prefer one coherent result commit per sprint when theorem, checker, and status
form one result. Separate commits are appropriate for independently reusable
results, retractions, regression fixes, or major strategy changes. Sequential
file-update commits caused by the GitHub tool are acceptable; identify the final
head clearly.

Update:

- theorem/checker files for detailed mathematics;
- `docs/CURRENT_STATUS.md` after a major mathematical result;
- `START_HERE.md` only when the candidate, proof gates, decisive obstruction, or
  startup routing changes;
- `docs/RETRACTIONS.md` when a committed argument is invalidated.

Create a session checkpoint only when a handoff cannot be represented adequately
in `START_HERE.md` and `CURRENT_STATUS.md`, or when an urgent retraction must be
seen immediately. Checkpoints are historical after their contents are absorbed.

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
supports.

## 8. Interruption recovery

After a lag, tool failure, or new chat:

1. inspect the latest confirmed head;
2. read the three startup files;
3. verify the primary candidate and decisive obstruction;
4. reuse committed artifacts instead of repeating computations;
5. continue from the last confirmed write or fetched SHA.

Do not restart the entire setup inside the same chat unless repository state is
actually uncertain.

## 9. Reporting

Report separately:

- proof gates closed and open;
- exact finite frontiers;
- reusable infinite-family structure;
- the decisive missing theorem;
- checks actually run;
- files and commits created;
- environment limitations.

A percentage may be given only as a clearly subjective research-maturity estimate,
not as a probability of imminent solution.

## 10. Web-chat efficiency

Prefer targeted reads and standalone checks. Avoid repeated calls returning the
same information. Save a rigorous partial result as soon as it is stable. Keep
detailed proofs in repository files and user updates short. Do not trade
mathematical verification for speed, and do not add new restrictions without a
concrete bottleneck.