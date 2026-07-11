# High-Q exclusion from the permanent mod-3 harmonic packing bound

Fix the first remaining cycle length

```text
p = 177780727155637125193
```

and write

```text
O = ord_X(2) = 1860810887857924950,
a_i = s_(i+1) + O*q_i,
Q = sum_i q_i,
B = A-p.
```

The exact full-label identity gives

```text
sum_i (s_i-1) = B-O*Q.                            (1)
```

This note excludes every integer

```text
6242 <= Q <= 6257.                                (2)
```

It uses only the retained finite reciprocal requirement, distinct target
labels below `X`, and the permanent predecessor sieve modulo `3`.

## 1. Required finite zero-layer reciprocal mass

The retained first-length certificate proves that expensive zero-layer targets
in

```text
60000000 < n < X
```

must contribute more than

```text
0.375632520964...
```

to `sum 1/n`.  This already subtracts:

- every target at most `60000000`;
- the complete cheap-transition contribution;
- all possible positive-layer positions;
- the maximum possible contribution of expensive targets at least `X`.

Thus any hypothetical cycle must contain a set `S` of distinct zero-layer
targets in that finite interval whose reciprocal sum exceeds this number.

## 2. Distinct full labels bound the cardinality

A target `n<X` determines its full label uniquely: if two such targets had the
same label `s`, then both would be congruent to `2^(-s)` modulo `X`, hence they
would be equal.

If `m=|S|`, the `m` distinct nonnegative costs `s-1` have sum at least

```text
0+1+...+(m-1)=m*(m-1)/2.
```

By (1),

```text
m*(m-1)/2 <= B-O*Q.                               (3)
```

Let `m_Q` be the largest integer satisfying (3).

## 3. Permanent mod-3 packing

The permanent predecessor sieve refines every one of the `2154` allowed
classes modulo `2M` to three odd lifts modulo

```text
W=6M=90594.
```

Exactly one lift is permanently dead, so every reached target lies in one of
exactly

```text
J=4308
```

surviving residue classes modulo `W`.

Consequently, above `N=60000000`, there are at most `J` possible targets in
each interval of length `W`.  If `r=ceil(m_Q/J)`, the reciprocal sum of any
`m_Q` such targets is at most

```text
J * sum_(k=0)^(r-1) 1/(60000001+W*k).
```

Using the decreasing-integral bound gives the explicit upper estimate

```text
U(Q)
 <= J/60000001
    +(J/W)*log((60000001+W*r)/60000001).           (4)
```

This estimate is deliberately generous: it ignores the large-prime subgroup
condition, the expensive-pair condition, and the exact locations of the
surviving residue classes.

## 4. Exact threshold

The rational logarithm certificate gives

```text
U(6241) > 0.377086594,
U(6242) < 0.375630659.
```

The second number is strictly below the required finite reciprocal mass

```text
0.375632520964...
```

Since `B-O*Q`, hence `m_Q` and `U(Q)`, are nonincreasing in `Q`, every

```text
Q=6242,6243,...,6257
```

is impossible.

Therefore every hypothetical cycle of the first remaining length satisfies

```text
Q <= 6241.                                        (5)
```

## 5. Significance

This is the first strict exclusion of an interval of possible full-order layer
totals.  It does not use character-sum equidistribution or enumerate orbit
values.  The proof combines:

- the exact integer layer decomposition;
- the permanent mod-3 predecessor obstruction;
- a compact harmonic packing inequality.

Run

```text
python tools/verify_high_q_mod3_harmonic_exclusion.py
```

for the exact arithmetic certificate.
