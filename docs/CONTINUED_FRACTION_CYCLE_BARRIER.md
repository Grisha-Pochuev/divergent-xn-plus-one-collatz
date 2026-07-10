# Continued-fraction cycle barrier through `10^37`

For the fixed candidate

```text
X  = 104350542602662257699,
n0 = 1,
```

this note proves that the accelerated orbit cannot enter any nontrivial positive cycle of length at most

```text
10^37.
```

The proof is exact and finite.

## 1. Cycle identity

Suppose a nontrivial cycle has distinct positive odd elements `n_0,...,n_(p-1)` and total halving count `A`. Multiplying the step equations gives

```text
2^A = product_i (X + 1/n_i).
```

Therefore

```text
A*ln(2) - p*ln(X)
  = sum_i ln(1 + 1/(X*n_i))
  < (1/X) * sum_i 1/n_i.                         (1)
```

## 2. Exact allowed output classes

Every accelerated output satisfies

```text
2^a*n' == 1 (mod 15099),
```

where

```text
15099 = 3*7*719,
ord_15099(2)=2154.
```

Thus every nontrivial cycle element lies in one of exactly `2154` odd output classes. In each class, successive positive odd representatives differ by `2*15099`.

Let `b_1,...,b_2154` be the least nontrivial positive odd representatives of these classes; the smallest is `25`. If a cycle has `p` distinct elements and

```text
K = ceil(p/2154),
```

then an exact class-by-class integral estimate gives

```text
sum_i 1/n_i <= H(p),
```

where the verifier uses

```text
H(p)
 = sum_j 1/b_j
 + (2154/(2*15099))*ln((25+2*15099*(K-1))/25).
```

This is roughly seven times sharper than bounding the elements by all odd integers beginning at `25`.

## 3. Order condition

Reducing the cycle identity modulo `X` gives

```text
2^A == 1 (mod X).
```

The exact order is

```text
ell = ord_X(2) = 1860810887857924950.
```

Hence `A=ell*q`. Put

```text
beta = ln(X)/(ell*ln(2)).
```

Equation (1) gives

```text
0 < q/p-beta < H(p)/(p*ell*X*ln(2)).              (2)
```

## 4. Continued-fraction reduction

For every `p<=10^37`, exact rational logarithm bounds prove

```text
2*p*H(p) < ell*X*ln(2).
```

Therefore

```text
0 < q/p-beta < 1/(2*p^2).
```

After reduction, Legendre's theorem forces `q/p` to be a continued-fraction convergent of `beta`.

The verifier encloses logarithms by rational intervals using

```text
ln(z)=2*sum_(j>=0) t^(2*j+1)/(2*j+1),
t=(z-1)/(z+1),
```

with an explicit geometric tail bound. No floating-point arithmetic is used.

## 5. Elimination of the possible convergents

Only convergents above `beta` can occur because the cycle correction is positive. There are exactly `19` such convergents with denominator at most `10^37`.

For every one, exact rational inequalities prove that its logarithmic gap already exceeds the maximum possible cycle correction `H(10^37)/X`. Therefore none can correspond to a positive cycle.

The largest checked upper-convergent denominator is

```text
7286014786354216885839578116495624057,
```

and the first certified convergent denominator beyond the barrier is

```text
61591102310422922843464723184177907160.
```

## 6. Conclusion

For

```text
(X,n0)=(104350542602662257699,1),
```

the orbit either

1. tends to positive infinity, or
2. enters a nontrivial positive cycle longer than `10^37` accelerated steps.

This improves the original fixed barrier

```text
148557456445856651509
```

by almost seventeen orders of magnitude.

It is still not a complete proof of divergence: cycles longer than `10^37` remain logically possible.

Run

```text
python tools/verify_continued_fraction_barrier.py
```

for the exact certificate.
