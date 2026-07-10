# Full-label occupancy budget

Fix the retained multiplier

```text
X = 104350542602662257699,
O = ord_X(2) = 1860810887857924950.
```

This note strengthens the former full-class activation bound.  The least label
of a full output class is paid by every occurrence of that class, not only by
the first occurrence.

## 1. Exact decomposition

Let a positive accelerated cycle have length `p` and exact valuations `a_i`.
For the target value `n_(i+1)`, define its full label `s_(i+1)` by

```text
1 <= s_(i+1) <= O,
2^s_(i+1)*n_(i+1) == 1 (mod X).
```

The step equation gives

```text
2^a_i*n_(i+1) == 1 (mod X).
```

Since `O` is the exact order of `2 modulo X`, there is a unique integer
`q_i>=0` such that

```text
a_i = s_(i+1)+O*q_i.                              (1)
```

Summing (1) around the cycle yields the exact identity

```text
A = sum_i s_i + O*Q,
Q = sum_i q_i.                                    (2)
```

Thus

```text
sum_i s_i <= A,
sum_i (s_i-1)+O*Q = A-p.                          (3)
```

In particular, if full class `s` occurs `c_s` times, then

```text
sum_s s*c_s <= A.                                 (4)
```

This is stronger than charging the label `s` only once when the class is
activated.

## 2. Consequences for the two remaining lengths

For either remaining sparse-window length

```text
177780727155637125193,
177780727155637125195,
```

the power-of-two interval fixes `A` exactly.  Exact division gives

```text
floor((A-p)/O) = 6257.
```

Therefore

```text
Q <= 6257.                                        (5)
```

Only at most `6257` cycle steps can lie above the least full-order valuation
layer, and the sum of all their layer numbers is at most `6257`.

The average least full label also satisfies

```text
(sum_i s_i)/p <= A/p < 67.
```

More generally, for every integer `K>=1`, the number of cycle occurrences with

```text
s_i >= K+1
```

is at most

```text
floor((A-p)/K).                                   (6)
```

## 3. Coupling to the two-generation delay

For a cycle value `n`, let `d(n)` be the two-generation delay from
`docs/TWO_GENERATION_PREDECESSOR_COST.md`.  Its actual layer number satisfies

```text
q >= d(n).
```

Combining this with (5) gives the global bound

```text
sum_i d(n_i) <= 6257.                             (7)
```

Hence all but at most `6257` cycle elements have delay `d=0`; if some delay is
larger than one, the number of positive-delay elements is smaller still.

For any selected set `S` of distinct possible cycle values, the unselected
`p-|S|` cycle elements still pay at least one unit each.  Therefore the correct
incremental selection constraint is

```text
sum_(n in S) [s(n)-1+O*d(n)] <= A-p.              (8)
```

This replaces the looser constraint that charged selected values by
`s+O*d` against the whole budget `A`.

## 4. Scope

Equations (2)--(8) are necessary conditions for every hypothetical cycle and
are exact.  They do not by themselves exclude the last two lengths, because a
cycle may repeat low-label full classes many times.  Their main use is in
transition-priced reciprocal duals and in proving that almost every cycle step
must use its least full-order valuation layer.

Run

```text
python tools/verify_full_label_occupancy_budget.py
```

for the exact arithmetic certificate and regression check on the known
accelerated `5n+1` cycle.
