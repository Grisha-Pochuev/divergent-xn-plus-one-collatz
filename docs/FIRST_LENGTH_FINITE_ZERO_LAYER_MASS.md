# Large finite zero-layer population at the first remaining length

This note localizes most of the reciprocal correction for

```text
p = 177780727155637125193
```

to expensive zero-layer targets in the finite interval

```text
60000000 < n < X.
```

## 1. Retained bounds

The exact logarithmic interval requires

```text
sum_i 1/n_i > 0.506785306837...
```

and the signed-label split-range certificates give

```text
sum_(n_i<=60000000) 1/n_i < 0.086411887.          (1)
```

Use the transition threshold `K=5000`.  The total contribution of all cheap
targets is less than

```text
2.216*10^(-13).                                    (2)
```

At most `6257` positions have positive full-order layer, so their contribution
above sixty million is at most

```text
6257/60000000.                                     (3)
```

## 2. Expensive zero-layer values at least X

Every expensive zero-layer edge has symmetric cost at least `5000`.  The exact
cycle edge-cost budget is

```text
sum c_i = 2*(A-p)=2*B.
```

Therefore the total number of expensive edges is at most

```text
E=floor(2*B/5000)=4657855051477692680.
```

Every target at least `X` contributes at most `1/X`.  Thus all expensive
zero-layer targets at least `X` contribute at most

```text
E/X < 0.044636616.                                 (4)
```

This bound is safe even though some of the `E` edges may be positive-layer or
may lie below `X`.

## 3. Forced finite population

Subtract (1)--(4) from the required reciprocal sum.  Expensive zero-layer
targets in

```text
60000000 < n < X
```

must contribute more than

```text
0.375632520964...
```

Each such distinct target contributes less than `1/60000000`.  Hence at least

```text
22537952
```

distinct expensive zero-layer targets lie strictly between sixty million and
`X`.

This strengthens the earlier finite-interval conclusion

```text
349430 zero-layer expensive targets in (10^6,X)
```

by a factor greater than `64`.

## 4. Exact target now exposed

Any final contradiction for the first remaining length may focus on the finite
set of zero-layer pair classes satisfying

```text
60000000 < n < X,
q=0,
s_source+s_target>=5002.
```

At least `22537952` distinct classes from this finite interval must occur in the
cycle.  The next useful step is a rigorous count or harmonic-sum upper bound for
these classes, not a trajectory scan.

Run

```text
python tools/verify_first_length_finite_zero_layer_mass.py
```

for the exact rational certificate.
