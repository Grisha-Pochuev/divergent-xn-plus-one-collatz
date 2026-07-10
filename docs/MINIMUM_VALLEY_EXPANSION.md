# Strong expansion from the minimum of either remaining cycle

The cheap-transition mass theorem proves that every hypothetical cycle at one
of the two remaining lengths contains a value below `X`.  Hence its minimum
`m` satisfies

```text
m <= 9190982840926584716
```

for length `...193`, and

```text
m <= 46609216582838682965
```

for length `...195`.

## 1. The outgoing valuation at a cycle minimum

Let

```text
a=v2(X*m+1),
n'=(X*m+1)/2^a.
```

Since `m` is the cycle minimum, `n'>=m`. Therefore

```text
2^a <= X+1/m < X+1 < 2^67,
```

so initially

```text
a<=66.                                           (1)
```

## 2. Exact sieve for a=59,...,66

For fixed `a`, exact valuation `a` is equivalent to

```text
X*m+1 == 2^a (mod 2^(a+1)),
```

or

```text
m == (2^a-1)*X^(-1) (mod 2^(a+1)).               (2)
```

The verifier enumerates every positive integer satisfying (2) below each of
the two proved minimum bounds.  There are only

```text
8,4,2,1,1,0,0,0
```

candidates for `a=59,...,66` below the first bound, and

```text
40,21,10,5,3,1,0,0
```

below the second.

Each candidate is tested against the exact full-output conditions

```text
m mod M in <2> mod M,
m^ord_P(2) == 1 (mod P),
X=M*P.
```

None is a full output.  A reached cycle element must be a full output, so all
cases `a=59,...,66` are impossible.

Combining with (1) gives

```text
a<=58.                                           (3)
```

## 3. Forced local growth

Using (3),

```text
n'=(X*m+1)/2^a
   > X*m/2^58
   > 362*m.
```

Thus the minimum of either remaining hypothetical cycle is followed by a jump
of more than a factor `362`.

The incoming edge to the minimum has valuation at least `67`, because its
predecessor is also at least `m`.  Hence every remaining cycle contains a
strict local valley of the form

```text
incoming valuation >=67,
minimum m<X,
outgoing valuation <=58,
next value >362*m.
```

## 4. Significance

This is a local transition restriction that uses the global reciprocal
concentration to obtain a finite height range, then an exact modular sieve.
It does not yet eliminate the two lengths, but it strengthens the neighbour
structure of the forced small expensive part and can be inserted into the
global height identities or a deeper predecessor dual.

Run

```text
python tools/verify_minimum_valley_expansion.py
```

for the exact certificate.
