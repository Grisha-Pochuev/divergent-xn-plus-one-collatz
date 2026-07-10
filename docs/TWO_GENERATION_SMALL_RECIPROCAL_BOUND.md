# Two-generation bound for small reciprocal contributors

This note applies the permanent predecessor sieve and the two-generation cost
to the hardest remaining sparse-window length

```text
p = 177780727155637125195.
```

The power-of-two interval fixes the total valuation exactly:

```text
A = 133*(p-1)/2+67
  = 11822418355849868825468.
```

## 1. Complete exact list below one million

Use

```text
C = 1000000.
```

Among the `2154` allowed progressions modulo `2M`, there are exactly

```text
71318
```

positive candidates at most `C`.  The exact index-eight subgroup test modulo

```text
P = 6911089648497401
```

leaves exactly

```text
8727
```

genuine full output representatives.

For every such representative `n`, Pohlig--Hellman in the smooth order

```text
ord_P(2)=5^2*2677*15137*852763
```

recovers its full label `s`.  The permanent mod-3 sieve removes `2903` values,
leaving exactly

```text
5824
```

representatives that possess a coprime first-generation predecessor.

For each survivor, the `45297`-state certificate gives its delay `d`, and every
cycle occurrence must spend at least

```text
w(n) = s+ord_X(2)*d
```

units of total valuation.

## 2. Exact fractional-knapsack dual

Cycle elements are distinct.  If `x_n` is the indicator that a surviving
representative `n<=C` occurs, then

```text
sum_n w(n)*x_n <= A.
```

For every positive rational `lambda`,

```text
sum_n x_n/n
 <= lambda*A + sum_n max(0,1/n-lambda*w(n)).       (1)
```

The exact certificate sorts the `5824` items by the ratio

```text
1/(n*w(n)).
```

The fractional boundary occurs after `2362` complete items.  The boundary item
is

```text
n = 106255,
s = 1741820788677582842,
d = 10,
w = 20349929667256832342.
```

Taking

```text
lambda = 1/(n*w)
```

in (1) and evaluating with exact rational arithmetic gives

```text
sum_(cycle elements n<=1000000) 1/n
 < 0.099005753.                                    (2)
```

No floating-point comparison is used in the proof.

## 3. Consequence for the final exceptional length

For the target length, exact atanh-series bounds give

```text
X*Lambda > 0.099934206,
```

where

```text
Lambda = A*log(2)-p*log(X)
       = sum_i log(1+1/(X*n_i)).
```

Since

```text
X*Lambda <= sum_i 1/n_i,
```

(2) proves that the values at most one million cannot supply the required
correction by themselves.  More precisely, every hypothetical cycle of this
length must satisfy

```text
sum_(n_i>1000000) 1/n_i > 0.000928.
```

Consequently it must contain at least

```text
929
```

distinct elements larger than one million whose reciprocal contribution is
still essential.

## 4. Scope

This does not yet eliminate the length: the present certificate does not bound
the contribution above one million sharply enough.  It does, however, move the
hardest case from an independent-class envelope to an exact transition-priced
selection problem and leaves a quantified residual target.

Run

```text
python tools/verify_two_generation_small_reciprocal.py
```

for the exact certificate.
