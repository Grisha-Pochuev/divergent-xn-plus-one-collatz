# Massive repeated full-transition class

Fix either remaining sparse-window length

```text
p = 177780727155637125193
```

or

```text
p = 177780727155637125195.
```

Let

```text
X = 104350542602662257699,
O = ord_X(2) = 1860810887857924950,
A = (133*p+1)/2.
```

For each cycle value `n_i`, let `s_i` be its least full output label, so

```text
1 <= s_i <= O,
2^s_i*n_i == 1 (mod X).
```

Write the exact valuation on the edge `n_i -> n_(i+1)` as

```text
a_i = s_(i+1) + O*q_i,
q_i >= 0.
```

## 1. Exact edge-cost identity

Assign to edge `i` the nonnegative integer cost

```text
c_i = (s_i-1) + (s_(i+1)-1) + 2*O*q_i.
```

Since every label occurs once as a source label and once as a target label,

```text
sum_i c_i
 = 2*sum_i(s_i-1) + 2*O*sum_i q_i
 = 2*(A-p).                                      (1)
```

Take

```text
K = 197.
```

By (1), fewer than or equal to

```text
floor(2*(A-p)/K)
```

edges can have `c_i >= K`.  Exact arithmetic gives, for both remaining
lengths, at least

```text
59561055798335280522
```

edges with

```text
c_i < 197.                                       (2)
```

Because `197 < 2*O`, every edge in (2) has `q_i=0`.  It also satisfies

```text
s_i+s_(i+1) <= 198.                              (3)
```

There are exactly

```text
sum_(u=1)^197 (198-u)
 = 197*198/2
 = 19503
```

ordered positive label pairs `(u,v)` satisfying `u+v<=198`.

Therefore one ordered pair occurs on at least

```text
ceil(59561055798335280522/19503)
 = 3053943280435589                              (4)
```

cycle edges.

## 2. Every ordered pair is one exact class modulo 2*X^2

For a zero-layer edge with source label `u` and target label `v`,

```text
2^v*n' = X*n+1,
n == 2^(-u) (mod X).
```

Hence the target satisfies the exact congruence

```text
n' == 2^(-v)*(1+X*2^(-u)) (mod X^2).             (5)
```

Because the target is odd, (5) has one odd lift modulo `2*X^2`.

Different ordered pairs `(u,v)` give different odd classes.  Indeed, reduction
modulo `X` recovers `v`; after multiplying by `2^v`, subtracting `1`, and
dividing by `X` modulo `X`, one recovers the source class and therefore `u`.

Thus all occurrences counted in (4) are distinct positive integers in one
arithmetic progression with step

```text
2*X^2.
```

## 3. Height and diameter consequence

If `R` distinct cycle values lie in one odd class modulo `2*X^2`, their range
is at least

```text
2*X^2*(R-1).
```

With `R=3053943280435589`, every hypothetical cycle at either remaining length
has diameter at least

```text
66508995066170702555770104858896894988802023536957800776
```

and hence maximum at least

```text
66508995066170702555770104858896894988802023536957800777.
```

## 4. Meaning

This is a global transition theorem, not a local forbidden-word claim.  Local
pairs are all realizable, but the fixed total valuation forces one very cheap
full-transition class to be occupied more than three quadrillion times.

The result supplies a concrete height lower bound and a highly repeated exact
source-target class for the next circulation or cycle-height argument.  It does
not by itself exclude the two remaining cycle lengths.

Run

```text
python tools/verify_massive_repeated_transition_class.py
```

for the exact certificate.
