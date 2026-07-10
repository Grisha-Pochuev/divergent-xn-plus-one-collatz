# Refined minimum valley for the first remaining length

This note strengthens the local minimum theorem for

```text
p = 177780727155637125193.
```

## 1. Refined transition threshold

Use the exact symmetric edge cost

```text
c_i=(s_i-1)+(s_(i+1)-1)+2*O*q_i
```

and choose

```text
K=9000.
```

At most

```text
2587697250820940377
```

edges have `c_i>=9000`.  Every other edge is zero-layer and has adjacent-label
sum at most `9001`.

There are exactly

```text
9000*9001/2 = 40504500
```

such ordered pairs.  A deterministic exact enumeration of their target
classes modulo `2*X^2` proves that the least positive representative is

```text
437624995949268865515542163747121,
```

attained at

```text
(u,v)=(2736,5392).
```

The cheap reciprocal contribution is therefore below `4.004*10^(-13)`.
Combining this with the exact lower bound

```text
sum_i 1/n_i > 0.506785306
```

forces an expensive target at most

```text
5106101578294348744.                              (1)
```

Hence the cycle minimum `m` satisfies (1).

## 2. Exact exclusion of outgoing valuations 57 through 66

At a cycle minimum the outgoing valuation is at most `66`.  For exact
valuation `a`, the minimum must satisfy

```text
m == (2^a-1)*X^(-1) (mod 2^(a+1)).
```

Below the refined bound (1), the numbers of candidates for
`a=57,...,66` are exactly

```text
18,9,4,3,1,1,0,0,0,0.
```

Every candidate is tested against the exact full-output subgroup conditions
modulo `M` and `P`.  None is a full output.  Therefore

```text
a_out<=56.                                        (2)
```

## 3. Refined forced expansion

From (2),

```text
n_next=(X*m+1)/2^a
      > X*m/2^56
      > 1448*m.
```

Thus a hypothetical cycle of the first remaining length contains a minimum
valley with

```text
incoming valuation >=67,
outgoing valuation <=56,
next value >1448*minimum.
```

## 4. Status

This is a strict strengthening for the length `...193`; it does not yet
eliminate that length.  The finite pair enumeration is modular and deterministic,
not a trajectory search.

Run

```text
python tools/verify_first_length_refined_valley.py
```

for the exact certificate.
