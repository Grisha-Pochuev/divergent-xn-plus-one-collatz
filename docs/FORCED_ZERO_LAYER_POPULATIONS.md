# Forced populations of zero-layer targets

For either remaining length, the exact full-label occupancy identity gives

```text
sum_i q_i <= 6257.
```

Consequently at most `6257` cycle positions can have a positive full-order
layer.

## 1. First remaining length

For

```text
p = 177780727155637125193,
```

the expensive-small-target certificate proves that at least

```text
355687
```

distinct expensive targets lie in

```text
1000000 < n < X.
```

At most `6257` of these can have `q>=1`. Therefore at least

```text
355687-6257 = 349430
```

are zero-layer targets. Since they belong to the expensive part of the
`K=5000` decomposition, each satisfies

```text
q=0,
s_source+s_target >= 5002,
1000000<n<X.                                      (1)
```

## 2. Second remaining length

For

```text
p = 177780727155637125195,
```

the flow-balanced split-range certificate proves that at least

```text
811320
```

distinct cycle values exceed sixty million. Again at most `6257` can have a
positive layer, so at least

```text
811320-6257 = 805063
```

of these values are entered through a zero-layer edge:

```text
q=0,
n>60000000.                                      (2)
```

## 3. Significance

The unresolved reciprocal tail is not merely large; almost all of its
mandatory population lies in the least full-order layer. Any final certificate
may therefore target the distribution of zero-layer pair classes:

- at least `349430` expensive zero-layer targets in the finite interval
  `(10^6,X)` for the first length;
- at least `805063` zero-layer targets above `6*10^7` for the second.

This is a direct arithmetic consequence of retained exact certificates and is
not a probabilistic density claim.

Run

```text
python tools/verify_forced_zero_layer_populations.py
```

for the exact arithmetic check.
