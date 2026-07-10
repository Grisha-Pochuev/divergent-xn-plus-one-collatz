# Continued-fraction cycle barrier through `10^36`

For the fixed candidate

```text
X  = 104350542602662257699,
n0 = 1,
```

this note proves that the accelerated orbit cannot enter any nontrivial positive cycle of length at most

```text
10^36.
```

The proof is exact and finite. It combines four facts:

1. the orbit never returns to `1`;
2. every possible nontrivial cycle element is at least `25`;
3. the total halving count around a cycle is divisible by `ell=ord_X(2)`;
4. distinct cycle elements make the logarithmic correction only harmonic in the cycle length.

## 1. Cycle identity and distinctness

Suppose a nontrivial cycle has distinct positive odd elements

```text
n_0,...,n_(p-1)
```

and total halving count `A`. Multiplying the step equations gives

```text
2^A = product_i (X + 1/n_i).
```

Therefore

```text
A*ln(2) - p*ln(X)
  = sum_i ln(1 + 1/(X*n_i))
  < (1/X) * sum_i 1/n_i.                         (1)
```

Since all cycle elements are distinct odd integers at least `25`, after sorting them,

```text
n_i >= 25 + 2*i.
```

Hence

```text
sum_i 1/n_i
 <= sum_(i=0)^(p-1) 1/(25+2*i)
 < 1/25 + (1/2)*ln((2*p+23)/25).                 (2)
```

Denote the right side by `H(p)`.

## 2. The order condition

Reducing the cycle identity modulo `X` gives

```text
2^A == 1 (mod X).
```

The exact order is

```text
ell = ord_X(2) = 1860810887857924950.
```

Thus

```text
A = ell*q
```

for some positive integer `q`.

Put

```text
beta = ln(X)/(ell*ln(2)).
```

Equations (1)-(2) imply

```text
0 < q/p - beta < H(p)/(p*ell*X*ln(2)).           (3)
```

## 3. Legendre reduction

For every `p <= 10^36`, exact rational logarithm bounds prove

```text
2*p*H(p) < ell*X*ln(2).
```

Therefore (3) gives

```text
0 < q/p - beta < 1/(2*p^2).
```

After reducing `q/p`, Legendre's theorem implies that it must be a convergent of the continued fraction of `beta`.

The verifier encloses `ln(2)` and `ln(X)` by rational intervals using the identity

```text
ln(z) = 2 * sum_(j>=0) t^(2*j+1)/(2*j+1),
t = (z-1)/(z+1),
```

with an explicit geometric tail bound. The two endpoint intervals determine a common continued-fraction prefix far beyond denominator `10^36`.

## 4. Elimination of all upper convergents

Only convergents above `beta` can occur, because the correction in (1) is strictly positive.

There are exactly `18` upper convergents with denominator at most `10^36`. For every one, exact rational bounds prove

```text
ell*num*ln(2) - den*ln(X) > H(10^36)/X.          (4)
```

If `q/p` reduces to `num/den`, its logarithmic gap is a positive integer multiple of the left side of (4), while the entire cycle correction is strictly smaller than the right side. This contradicts the cycle identity.

The largest checked upper-convergent denominator is

```text
208191887234528835665081861753663977,
```

and the first certified convergent denominator beyond the barrier is

```text
7286014786354216885839578116495624057.
```

## 5. Conclusion

For the fixed pair

```text
(X,n0)=(104350542602662257699,1),
```

the orbit either

1. tends to positive infinity, or
2. enters a nontrivial positive cycle longer than `10^36` accelerated steps.

This improves the previous fixed barrier

```text
148557456445856651509
```

by more than fifteen orders of magnitude.

It is still not a complete divergence proof: cycles longer than `10^36` remain logically possible.

Run

```text
python tools/verify_continued_fraction_barrier.py
```

for the independent exact certificate.
