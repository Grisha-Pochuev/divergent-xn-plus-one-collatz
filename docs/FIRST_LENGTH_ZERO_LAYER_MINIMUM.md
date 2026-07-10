# Minimum structure in the all-zero-layer first-length branch

Consider the first remaining length

```text
p = 177780727155637125193
```

under the additional hypothesis

```text
q_i=0 for every cycle edge.
```

The refined valley theorem gives

```text
m <= 5106101578294348744,
a_out<=56.
```

Because every incoming layer is zero, the cycle minimum must have full
predecessor delay

```text
d_X(m)=0.                                         (1)
```

## 1. Exact zero-delay sieve by outgoing valuation

For each exact outgoing valuation `a=45,...,56`, enumerate all full outputs
below the minimum bound in the exact congruence class

```text
m == (2^a-1)*X^(-1) (mod 2^(a+1)).
```

For every candidate, compute its least full predecessor delay.  The exact
numbers of zero-delay survivors are

```text
a=45: 20
a=46: 15
a=47: 10
a=48:  6
a=49:  1
a=50:  0
a=51:  1
a=52:  0
a=53:  0
a=54:  0
a=55:  0
a=56:  0.
```

Thus in the all-zero-layer branch

```text
a_out<=51.                                        (2)
```

## 2. The unique a=51 minimum

The sole zero-delay candidate with `a_out=51` is

```text
m_51 = 2512233706332574837.
```

Its exact full-label data are

```text
target label      = 1163144419278463552,
predecessor residue = 48574810891984207784 (mod X),
source label      = 450155079401401655,
full delay        = 0.
```

## 3. Strong dichotomy

Every all-zero-layer cycle of the first remaining length satisfies one of:

### Exceptional zero-layer minimum

```text
m = 2512233706332574837,
a_out=51.
```

### Very strong expansion

Since `a=50` has no zero-delay candidate, every other case has

```text
a_out<=49,
n_next > X*m/2^49 > 185363*m.
```

## 4. Meaning

The all-zero-layer branch is now separated from the positive-layer branch.
Either it passes through one explicit minimum with fully known adjacent class
data, or its first step from the minimum expands by more than five orders of
magnitude.

This is a necessary local structure, not yet a contradiction.  It is designed
for combination with the all-zero-layer affine cycle equation or a signed
height potential.

Run

```text
python tools/verify_first_length_zero_layer_minimum.py
```

for the exact certificate.
