# Chat handoff template

Copy this text into a new chat when continuing the project.

```text
This is a continuation of the repository
Grisha-Pochuev/divergent-xn-plus-one-collatz.

Before doing new mathematics, read in this order:

1. START_HERE.md
2. docs/CURRENT_STATUS.md
3. docs/VALIDATED_RESULTS.md
4. docs/RETRACTIONS.md
5. docs/NEXT_STEPS.md
6. run_checks.py

Treat GitHub as the durable source of truth. Do not use claims marked as
retracted, superseded, heuristic, or unverified.

The strict target is to find explicit odd positive integers X>=5 and n0 such
that the accelerated odd-only orbit

C_X(n)=(X*n+1)/2^v2(X*n+1)

tends to positive infinity.

Do not count a cycle, mere avoidance of 1, a long finite trajectory, or an
arbitrarily large finite barrier as a solution.

Do not run long CPU computations without my separate explicit permission.
Prefer exact arithmetic, symbolic derivations, short residue checks, and
compact independently verifiable certificates.

Work on one principal route. Before announcing a result:

- independently rederive the key formula;
- test it against known small cycles;
- add a checker or regression test where practical;
- run the retained lightweight checks;
- commit the proof, checker, tests, and status update.

At the end report briefly:

1. what was rigorously proved;
2. what remains unproved;
3. any failed or retracted approach;
4. files and commit SHAs changed;
5. the exact next mathematical step;
6. subjective progress: was -> now.
```
