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
176022359338834903228
```

is impossible.

Therefore the orbit either tends to positive infinity or enters a nontrivial positive cycle longer than this finite barrier.

The current barrier is proved in

```text
docs/TRANSITION_BUDGET_CYCLE_BARRIER.md
tools/verify_transition_budget_barrier.py
```

and uses exact modular and rational arithmetic only.

## Priority 1 transition analysis

Let

```text
M = 15099,
ord_M(2) = 2154.
```

### Complete local graph: a proved no-go result

The graph whose vertices are the `2154` allowed odd output classes modulo `2M` is complete, including loops. More strongly, every finite word of these class labels is realized by infinitely many positive starts.

Reason: an exact valuation word fixes one odd residue modulo a power of two, while the desired initial class fixes one odd residue modulo `2M`; the generalized Chinese remainder theorem combines them because `M` is odd.

Consequences:

- there are no forbidden one-step transitions at the level of the bare `2154` labels;
- there are no forbidden finite class words at that level;
- any stronger finite-state certificate must retain exact binary information, a height layer, or a global cycle-closure condition.

Files:

```text
docs/RESIDUE_TRANSITION_NO_GO.md
tools/verify_residue_transition_no_go.py
```

### Global valuation-cost budget

If `c_t` is the number of cycle elements in class `t`, then entering class `t` requires an exact valuation congruent to `t modulo 2154`, hence at least `t`. For a cycle of length `p`, the exact cycle identity and `X+1<2^67` give

```text
sum_t c_t = p,
sum_t t*c_t <= 67p-1.
```

This couples the class occupancies and strictly improves the independent-class reciprocal envelope.

Files:

```text
docs/RESIDUE_VALUATION_BUDGET.md
tools/verify_residue_valuation_budget.py
```

### Exact flow balance

Cycle closure gives the stronger identity

```text
#{cycle elements currently in class t}
=
#{cycle steps whose successor enters class t}.
```

Thus the same occupancy vector is constrained both by:

1. arithmetic progressions modulo `2M` for current classes;
2. binary progressions modulo `2^t` for outgoing target classes.

This reduces the next reciprocal estimate to a finite separable concave optimization in `2154` count variables.

Files:

```text
docs/TRANSITION_BALANCED_RECIPROCAL_REDUCTION.md
tools/verify_transition_balance.py
```

## Numerical barrier comparison

The previously recorded project barrier was

```text
170000000000000000000.
```

The current exact transition-budget barrier is

```text
176022359338834903228.
```

This is about `3.54%` larger than the previously retained round value. For a fair structural comparison, the old independent-class envelope, if pushed to its own exact limit with the same rational logarithm bounds, reaches

```text
176022359338834903224.
```

Thus the new transition-class cost information adds exactly `4` lengths beyond the saturated old envelope. The reciprocal upper bound itself improves from about `4.44061` to about `3.82017`, but division by the enormous `X` makes its effect on this particular power-of-two interval barrier very small.

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
13. The bare `2154`-class transition graph is complete, so local forbidden-word searches in that abstraction cannot work.
14. Hypothetical cycle class counts satisfy a global valuation budget and exact source/target flow balance.

## Not established

- No explicit orbit has yet been proved to tend to infinity.
- Cycles longer than `176022359338834903228` remain logically possible for the main candidate.
- No ordinary positive integer supporting infinitely many net-positive regenerative bursts has yet been constructed.
- No low-average infinite valuation word with an eventually stable positive coding residue has yet been constructed.
- The transition-balanced concave optimization has not yet been converted into a stronger exact certificate.

## Current frontier

The prioritized roadmap is `docs/NEXT_STEPS.md`.

### Route A: fixed candidate, Priority 1

Do not search again for forbidden edges or short words in the unaugmented `2154`-class graph; that route is rigorously closed by completeness.

The immediate next step is to solve or upper-bound the transition-balanced reciprocal optimization with exact rational tangent certificates. However, reciprocal improvements alone can move the present interval barrier by only a few lengths, so a useful breakthrough must also seek a stronger global closure invariant, a height-dependent transition state, or a descent argument that can cross infinitely many power-of-two intervals.

### Other routes

The regenerative-chain, stabilized-code, cycle-height, and `X=9` digital-invariant routes remain recorded in `docs/NEXT_STEPS.md`, but they were not worked on in the present Priority 1 session.

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

to execute the retained certificates, including the transition no-go theorem, valuation budget, flow-balance audit, exact cycle barrier, and the regression preventing reintroduction of the invalid order condition.
