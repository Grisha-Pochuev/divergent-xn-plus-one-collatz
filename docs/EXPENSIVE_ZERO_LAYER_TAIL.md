# Mandatory expensive zero-layer tail

This note sharpens the split-range tail populations by proving that the
mandatory values may be counted specifically among expensive zero-layer
transitions.

Use the retained threshold

```text
K=5000.
```

An edge is cheap when

```text
q=0,
s_source+s_target<=5001,
```

and expensive otherwise.  The exact transition-concentration certificate gives
the global reciprocal bound

```text
sum_(cheap targets) 1/n < 2.216*10^(-13).          (1)
```

Also, at most

```text
6257
```

cycle positions have positive full-order layer.

## 1. Remove cheap and positive-layer contributions

For either remaining length, let `R` be the reciprocal contribution still
required from values above sixty million after applying the common finite-range
upper bound

```text
sum_(n_i<=60000000)1/n_i <0.086411887.
```

The contribution above sixty million from positive-layer positions is at most

```text
6257/60000000.
```

The contribution from all cheap targets, including those above the cutoff, is
bounded by (1).  Therefore expensive zero-layer values above sixty million must
contribute more than

```text
R - 6257/60000000 - 2.216*10^(-13).                (2)
```

Each such distinct value contributes less than `1/60000000`.

## 2. Exact populations

For

```text
p=177780727155637125193,
```

formula (2) forces at least

```text
25216149
```

distinct expensive zero-layer targets above sixty million.

For

```text
p=177780727155637125195,
```

it forces at least

```text
805083
```

distinct expensive zero-layer targets above sixty million.

The small cheap contribution is far below one unit at the final integer
counting scale, so these are the same numerical zero-layer counts obtained by
subtracting `6257`, now with the stronger conclusion that every counted target
may be taken from the expensive part.

## 3. Consequence

The remaining obstruction is concentrated in exact zero-layer pair classes
satisfying

```text
s_source+s_target>=5002,
n>60000000.
```

Any final distribution or reciprocal certificate may ignore the cheap pair
classes after charging their already certified negligible total contribution.

Run

```text
python tools/verify_expensive_zero_layer_tail.py
```

for the exact rational calculation.
