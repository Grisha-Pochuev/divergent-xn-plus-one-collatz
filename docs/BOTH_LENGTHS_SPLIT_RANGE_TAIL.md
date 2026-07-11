# Split-range tail populations for both remaining lengths

The signed-label and integral-layer certificates were developed for the harder
remaining length

```text
p_2 = 177780727155637125195.
```

They also apply, without weakening, to

```text
p_1 = 177780727155637125193,
```

because its incremental budget is smaller:

```text
B_1 = B_2-131.
```

Every selected-item inequality proved using budget `B_2` is therefore a safe
upper bound at `p_1` as well.

## 1. Common finite-range upper bound

For either remaining length, the retained certificates give

```text
sum_(n_i<=1000000) 1/n_i < 0.085226583,
sum_(1000000<n_i<=60000000) 1/n_i < 0.001185304.
```

Hence, for both lengths,

```text
sum_(n_i<=60000000) 1/n_i
 < 0.086411887.                                    (1)
```

## 2. First remaining length

For

```text
p_1 = 177780727155637125193,
```

the exact logarithmic interval requires

```text
sum_i 1/n_i > 0.506785306837...
```

Combining this with (1), values above sixty million must contribute more than

```text
0.420373419837...
```

Each distinct value above sixty million contributes less than `1/60000000`.
Therefore at least

```text
25222406
```

distinct cycle values exceed sixty million.

At most `6257` cycle positions have positive full-order layer, so at least

```text
25222406-6257 = 25216149
```

of these values are zero-layer targets.

This strengthens the former first-length zero-layer population

```text
349430
```

by a factor greater than `72`.

## 3. Second remaining length

For

```text
p_2 = 177780727155637125195,
```

the same calculation gives the retained updated figures

```text
811340 values above sixty million,
805083 of them zero-layer.
```

## 4. Significance

Both residual cycle lengths now require macroscopic zero-layer populations in
the same tail range:

```text
p=...193: at least 25216149 zero-layer targets above 60000000,
p=...195: at least   805083 zero-layer targets above 60000000.
```

The first length is therefore no longer represented only by a small-expensive
target count.  It is subject to the same zero-layer distribution problem as the
second length, but with a much larger mandatory population.

Run

```text
python tools/verify_both_lengths_split_range_tail.py
```

for the exact rational calculation.
