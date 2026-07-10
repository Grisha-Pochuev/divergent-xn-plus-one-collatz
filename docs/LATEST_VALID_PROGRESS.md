# Latest valid progress

The previously claimed `10^37` cycle barrier remains retracted because it relied on the false condition `ord_X(2) | A` for a cycle. The current work proceeds only from retained valid statements.

For

```text
X  = 104350542602662257699,
n0 = 1,
```

the orbit cannot return to `1`.

## Priority 1 transition results

Let

```text
M = 15099,
ord_M(2) = 2154.
```

The following are now rigorously proved:

1. The bare transition graph on the `2154` allowed output classes is complete, including loops.
2. Every finite class word is realized by infinitely many positive starts, so forbidden-edge and forbidden-short-word searches in this abstraction cannot work.
3. If `c_t` are the class occupancies of a hypothetical cycle of length `p`, then

```text
sum_t c_t = p,
sum_t t*c_t <= 67p-1.
```

4. Cycle closure gives exact source/target flow balance for every class.
5. The class-cost budget strengthens the exact reciprocal certificate.

## Current finite barrier

Every nontrivial positive cycle of accelerated length at most

```text
176022359338834903228
```

is impossible.

Therefore the fixed orbit from `1` either tends to positive infinity or enters a nontrivial cycle longer than that barrier.

The previously recorded project barrier was

```text
170000000000000000000.
```

The current value is about `3.54%` larger. For a fair structural comparison, the old independent-class envelope, if saturated with the same rational logarithm bounds, reaches

```text
176022359338834903224.
```

Thus the strict numerical gain from the transition-class cost information is exactly `4` lengths, although the reciprocal upper bound itself improves from about `4.44061` to about `3.82017`.

Proofs and exact lightweight verifiers:

```text
docs/RESIDUE_TRANSITION_NO_GO.md
tools/verify_residue_transition_no_go.py
docs/RESIDUE_VALUATION_BUDGET.md
tools/verify_residue_valuation_budget.py
docs/TRANSITION_BALANCED_RECIPROCAL_REDUCTION.md
tools/verify_transition_balance.py
docs/TRANSITION_BUDGET_CYCLE_BARRIER.md
tools/verify_transition_budget_barrier.py
```

No long trajectory computation or heavy CPU search is used.

The strict prize problem remains open: cycles longer than the new finite barrier have not yet been excluded. The next Priority 1 step is an exact rational optimization of the balanced reciprocal reduction or, more importantly, a height-dependent global transition invariant capable of excluding infinitely many power-of-two intervals.
