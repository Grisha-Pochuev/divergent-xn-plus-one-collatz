# Minimum structure in the all-zero-layer second-length branch

Consider

```text
p = 177780727155637125195
```

under the hypothesis

```text
q_i=0 for every cycle edge.
```

## 1. Refined minimum height

The `K=9000` transition-pair enumeration has least cheap target

```text
437624995949268865515542163747121.
```

Using the exact reciprocal threshold for this length and the exact edge-cost
budget forces an expensive target, and hence the cycle minimum, at most

```text
25894009212734490968.                             (1)
```

The general minimum-valley sieve still gives `a_out<=58`.

## 2. Zero-delay sieve

In an all-zero-layer cycle the minimum must have full predecessor delay zero.
Exact enumeration below (1) gives:

```text
a=58: 0 zero-delay candidates
a=57: 0
a=56: 0
a=55: 0
a=54: 0
a=53: 1
a=52: 0
a=51: 3
a=50: 2.
```

Therefore the largest possible outgoing valuation is `53`.

The unique zero-delay `a=53` minimum is

```text
m_53 = 6815423150285083765.
```

Its exact adjacent full-class data are

```text
target label        = 401703252155000920,
predecessor residue = 102306570270931706569 (mod X),
source label        = 1619960862681130392,
full delay          = 0.
```

## 3. Rigorous dichotomy

Every all-zero-layer cycle of length `...195` satisfies one of:

### Exceptional minimum

```text
m = 6815423150285083765,
a_out=53,
n_next>11585*m.
```

### Stronger expansion

Since `a=52` has no zero-delay candidate, every other case has

```text
a_out<=51,
n_next>X*m/2^51>46340*m.
```

## 4. Status

The second all-zero-layer branch is reduced to one explicit high-valuation
minimum or a growth step exceeding a factor `46340`.  This is still a
necessary local structure, not a complete exclusion.

Run

```text
python tools/verify_second_length_zero_layer_minimum.py
```

for the exact certificate.
