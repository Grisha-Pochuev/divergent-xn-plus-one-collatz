# Short return to one exact full-transition class

Fix either remaining sparse-window length

```text
p = 177780727155637125193
```

or

```text
p = 177780727155637125195.
```

The massive repeated-transition theorem proves that one zero-layer ordered
full-label pair occurs at least

```text
R = 3053943280435589
```

times.  The target values of those occurrences all lie in one exact odd
residue class modulo

```text
2*X^2,
X = 104350542602662257699.
```

## 1. Cyclic gaps between repeated occurrences

List those `R` target occurrences in cyclic order.  They divide the cycle into
`R` nonempty segments.  For segment `j`, let

```text
L_j = number of accelerated steps,
S_j = sum of the exact valuations on those steps.
```

Then exactly

```text
sum_j L_j = p,
sum_j S_j = A,
A = (133*p+1)/2.
```

Consequently

```text
sum_j (67*L_j+S_j) = 67*p+A.
```

At least one segment therefore satisfies

```text
67*L_j+S_j <= floor((67*p+A)/R).
```

For both remaining values of `p`, exact arithmetic gives

```text
floor((67*p+A)/R) = 7771502.                     (1)
```

Every accelerated valuation is at least one, so `S_j>=L_j`.  Combining this
with (1) yields

```text
L_j <= floor(7771502/68) = 114286,               (2)
S_j <= 7771502-67 = 7771435.                     (3)
```

## 2. Exact short-return conclusion

Every hypothetical cycle at either remaining length contains a nonempty orbit
segment with

```text
1 <= L <= 114286,
L <= S <= 7771435,
```

whose initial and terminal values are congruent modulo

```text
2*X^2.
```

Moreover, both endpoints are occurrences of the same cheap zero-layer
source-target label pair.

## 3. Significance

The residual long-cycle problem now contains a bounded exact-return witness.
Instead of reasoning only about a cycle of length about `1.78*10^20`, one may
study a segment of at most `114286` steps returning to one fixed class modulo
`2*X^2`, with total valuation at most `7771435`.

This does not yet prove that no such segment exists: arbitrary finite valuation
words are locally realizable.  The useful new ingredient is the simultaneous
endpoint congruence modulo `X^2`, the repeated transition labels, and the exact
small bounds on both length and total valuation.  A final attack can combine
these with the affine iterate formula or with a stronger modulus.

Run

```text
python tools/verify_short_full_class_return.py
```

for the exact certificate.
