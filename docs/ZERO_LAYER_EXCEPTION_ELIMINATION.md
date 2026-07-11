# Elimination of both exceptional all-zero-layer minima

The previous zero-layer minimum certificates left one explicit exceptional
minimum for each remaining cycle length.  Both exceptions are impossible by an
exact two-generation predecessor test.

Assume throughout that

```text
q_i=0 for every cycle edge.
```

Then every cycle value must have a predecessor using its least full output
label, and that predecessor must itself be a full output.

## 1. Exact two-step inverse test

Let `n_0` be a proposed cycle value with least full label `s_0`.  Its unique
zero-layer predecessor is

```text
n_(-1)=(2^s_0*n_0-1)/X.
```

To recover `n_(-1) modulo X^2`, compute the numerator modulo `X^3` before
dividing by `X`.  Let `s_(-1)` be the full label of `n_(-1) modulo X`.
The next zero-layer predecessor residue is

```text
n_(-2) == (2^s_(-1)*n_(-1)-1)/X (mod X).
```

A reached cycle value must belong to the full output subgroup modulo `X`.

## 2. First remaining length

The only exceptional all-zero-layer minimum was

```text
n_0 = 2512233706332574837,
s_0 = 1163144419278463552.
```

Its first predecessor has

```text
n_(-1) mod X = 48574810891984207784,
s_(-1) = 450155079401401655.
```

The exact second predecessor residue is

```text
n_(-2) mod X = 48109505038107715951.
```

This residue is not a full output: its reduction modulo `M=15099` is `9709`,
which is not among the `2154` inverse-power output classes; independently, its
reduction modulo `P` is outside the base-2 subgroup.

Hence this exceptional minimum cannot occur in an all-zero-layer cycle.

Therefore every all-zero-layer cycle of length

```text
177780727155637125193
```

must satisfy

```text
a_out<=49,
n_next>185363*minimum.                            (1)
```

## 3. Second remaining length

The only exceptional all-zero-layer minimum was

```text
n_0 = 6815423150285083765,
s_0 = 401703252155000920.
```

Its first predecessor has

```text
n_(-1) mod X = 102306570270931706569,
s_(-1) = 1619960862681130392.
```

The exact second predecessor residue is

```text
n_(-2) mod X = 30024704914638057554.
```

Its reduction modulo `M` is `5054`, outside the allowed output classes, and its
reduction modulo `P` is also outside the base-2 subgroup.

Hence this exceptional minimum is impossible in an all-zero-layer cycle.

Therefore every all-zero-layer cycle of length

```text
177780727155637125195
```

must satisfy

```text
a_out<=51,
n_next>46340*minimum.                             (2)
```

## 4. Significance

The all-zero-layer branches no longer contain isolated exceptional minima.
They now have unconditional strong expansion from the cycle minimum: (1) for
the first length and (2) for the second.

This does not yet eliminate either length, because later high valuations may
compensate the expansion.  It removes the only local exceptions and leaves a
clean target for a global signed height potential.

Run

```text
python tools/verify_zero_layer_exception_elimination.py
```

for the exact certificate.
