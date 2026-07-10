# Latest valid progress

The former `10^37` claim remains retracted. All current results preserve the correct cycle identity.

For

```text
X  = 104350542602662257699,
n0 = 1,
```

the current contiguous cycle barrier is

```text
177780727155637125192.
```

More strongly, every length through

```text
355561454311274250377
```

is impossible except

```text
177780727155637125193
177780727155637125195.
```

## New transition progress

Let

```text
O=ord_X(2)=1860810887857924950.
```

Every incoming valuation has the unique form

```text
a_i=s_(i+1)+O*q_i,
1<=s_i<=O.
```

The exact occupancy identity is

```text
A=sum_i s_i+O*sum_i q_i.
```

At either remaining length,

```text
sum_i q_i<=6257.
```

The following additional results are now retained:

1. A permanent predecessor sieve removes exactly `2154` of the `6462` refined classes modulo `6*15099`.
2. Possible predecessors of a full representative form an exact linear progression modulo `X`.
3. Requiring the predecessor itself to be a full output gives a pointwise full-layer delay.
4. Below `10^6`, only `133` of `5824` surviving representatives have zero delay; the maximum delay is `347`.
5. Through `6*10^7`, only `9462` of `358103` surviving representatives have zero delay; the maximum is `558`.
6. For the harder remaining length,

```text
sum_(n_i<=60000000) 1/n_i < 0.087618737,
```

while the exact cycle threshold is greater than `0.099934206`.
7. Therefore more than `0.012315` of the reciprocal correction must come from at least `738929` distinct values above sixty million.
8. Finite inverse-window bounds improve strictly at depths one, two, and three.
9. Any hypothetical remaining cycle is either entirely least-layer, or contains at least `28413093679980362` consecutive least-layer steps.
10. If a positive layer occurs, one least-layer block grows by more than

```text
2^1860810887857924884.
```

## Exact remaining obstruction

The last unresolved object is the large zero-delay tail. Blindly enlarging the modular cutoff is not the preferred route. The next useful theorem must provide a global potential, a numerically explicit distribution bound for the initial full-class orbit, or a full transition-circulation inequality.

Primary new files:

```text
docs/FULL_LABEL_OCCUPANCY_BUDGET.md
tools/verify_full_label_occupancy_budget.py
docs/FULL_PREDECESSOR_DELAY.md
tools/verify_full_predecessor_delay.py
docs/FULL_PREDECESSOR_RECIPROCAL_BOUND.md
tools/verify_full_predecessor_reciprocal_bound.py
docs/FINITE_INVERSE_WINDOW_CHARGING.md
tools/verify_finite_inverse_window_charging.py
docs/GIANT_COMPENSATING_GROWTH_BLOCK.md
tools/verify_giant_compensating_growth_block.py
```

No Collatz trajectory scan or large Actions matrix was used. The strict prize problem remains open.
