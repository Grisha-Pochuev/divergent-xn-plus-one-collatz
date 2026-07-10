# Current status

## Project navigation

Every new work session must begin with:

```text
START_HERE.md
docs/CURRENT_STATUS.md
docs/VALIDATED_RESULTS.md
docs/RETRACTIONS.md
docs/NEXT_STEPS.md
run_checks.py
```

Use `docs/CHAT_HANDOFF_TEMPLATE.md` when moving the project to a new chat. GitHub is the durable source of truth; chat summaries are secondary.

The strict target is to exhibit odd integers `X>=5` and `n0>=1` whose accelerated odd-only orbit tends to positive infinity.

## Main valid fixed candidate

The strongest retained candidate is

```text
X  = 104350542602662257699,
n0 = 1.
```

For this pair the repository proves:

1. the orbit leaves `1` and can never return to `1`;
2. every possible element of a nontrivial cycle reached by the orbit is at least `25`;
3. every nontrivial positive cycle of accelerated length at most

```text
170000000000000000000
```

is impossible.

Therefore the orbit either tends to positive infinity or enters a nontrivial positive cycle longer than this finite barrier.

The current barrier is proved by the residue-crowding certificate in
`docs/RESIDUE_CROWDING_CYCLE_BARRIER.md` and checked by
`tools/verify_residue_crowding_barrier.py`.

## Residue-crowding improvement

Let

```text
M = 15099,
ord_M(2) = 2154.
```

Every accelerated output lies in one of `2154` allowed odd residue classes modulo `2M`. Elements of a nontrivial cycle are distinct, so the sum of their reciprocals can be bounded by a logarithmic envelope over these arithmetic progressions rather than by the crude linear estimate `p/25`.

This raises the retained direct barrier from

```text
148557456445856651509
```

to

```text
170000000000000000000.
```

No long trajectory simulation or heavy CPU search is used; the verifier checks exact modular and rational inequalities.

## Retraction of the invalid `10^37` claim

The former continued-fraction claim through `10^37` is retracted. It incorrectly assumed

```text
2^A == 1 (mod X)
```

for a cycle. The correct congruence is

```text
2^A * product_i(n_i) == 1 (mod X).
```

The accelerated `5n+1` cycle `13 -> 33 -> 83 -> 13` is a direct counterexample to the invalid order condition. The regression checker preserves this audit. Full details are in `docs/RETRACTIONS.md`.

## Other established results

The authoritative registry is `docs/VALIDATED_RESULTS.md`. In summary:

1. Exact accelerated map and iterate formula.
2. Average-valuation criterion for exponential divergence.
3. Arbitrarily long rigorously increasing finite orbit segments.
4. Finite repetition bound for every exact valuation block.
5. Eventually periodic exact valuations force an eventually periodic orbit.
6. Complete `X=2^m+1` macroblocks whose accumulated growth can survive the exit.
7. A 2-adic isometry and a unique regeneration target at every finite precision.
8. Exact inverse coding of every finite valuation word.
9. General arbitrary-core burst reduction for `X=2^m+1`.
10. Positive integer orbits are either eventually periodic or tend to positive infinity.
11. For `(X,n0)=(1093,1)`, the orbit never returns to `1`.
12. For every fixed odd `X>=5`, a hypothetical cycle minimum has an effectively computable polynomial upper bound in its length.

## Not established

- No explicit orbit has yet been proved to tend to infinity.
- Cycles longer than `170000000000000000000` remain logically possible for the main candidate.
- No ordinary positive integer supporting infinitely many net-positive regenerative bursts has yet been constructed.
- No low-average infinite valuation word with an eventually stable positive coding residue has yet been constructed.

## Current frontier

The prioritized roadmap is `docs/NEXT_STEPS.md`.

### Route A: fixed candidate

Find a global modular or descent obstruction that retains the factor `product_i(n_i)` in the correct cycle congruence and excludes cycles of every length. The immediate lightweight target is to exploit transition constraints among the `2154` allowed classes, rather than treating those classes independently.

### Route B: infinite regenerative chain

For `X=2^m+1`, use the exact arbitrary-core return map

```text
u -> odd_part(X^L*u-1)
```

to construct one ordinary positive start producing infinitely many net-positive bursts.

### Route C: stabilized low-average code

Construct an infinite exact valuation word with average below `log2(X)` whose coding residues eventually stabilize at a positive integer.

### Route D: combine height bounds

Make the logarithmic cycle-height constants explicit and combine the resulting polynomial upper bound with a modular lower bound that grows faster.

Any route would finish the strict prize problem.

## Working constraints

- Do not launch long CPU computations inside ordinary chat sessions.
- Prefer symbolic derivations, exact arithmetic, short residue enumeration, and compact certificates.
- Any large external computation requires explicit user approval.
- Before announcing a theorem, test it against known small cycles and add a regression check where practical.
- After every major result or retraction, update `START_HERE.md`, this file, and the relevant registry.

## Reproducibility

Run

```text
python run_checks.py
```

to execute the retained certificates, including the residue-crowding verifier and the audit preventing reintroduction of the invalid order condition.
