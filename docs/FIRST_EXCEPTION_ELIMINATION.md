# Elimination of the first sparse-window exception

The first sparse-window theorem left seven possible odd cycle lengths. This note eliminates the first one:

```text
p = 177780727155637125183.
```

## 1. Midpoint harmonic improvement

For a decreasing convex progression reciprocal

```text
f(x)=1/(rho+D*x),
```

convexity gives, for every integer `j>=1`,

```text
f(j) <= integral_(j-1/2)^(j+1/2) f(x) dx.
```

Hence `c>=1` distinct elements of one residue progression satisfy

```text
sum_(j=0)^(c-1) 1/(rho+D*j)
 <= 1/rho
    + log((rho+D*(c-1/2))/(rho+D/2))/D.
```

This is strictly sharper than the former one-sided integral envelope.

## 2. Larger exact valuation split

Use

```text
P = 6911089648497401,
K = 5000000.
```

Cycle elements are again divided by their incoming exact valuation:

```text
low:  1<=a<=K,
high: a>=K+1.
```

The verifier performs one deterministic modular pass through the first `K` inverse powers of `2 modulo P`. This is not a trajectory search. It finds

```text
minimum low representative = 4493203551.
```

The low contribution is bounded by

```text
less than 2.768*10^(-8).
```

For the high part, the count bound is

```text
h <= floor((67p-1)/(K+1)).
```

The midpoint progression inequality and a common rational tangent give

```text
high contribution < 2.527288580.
```

Thus

```text
sum_i 1/n_i < 2.527288608.
```

## 3. Exact interval comparison

For this exceptional odd length the only possible total valuation is

```text
A = 133*(p-1)/2 + 67.
```

Therefore the exact logarithmic gap is

```text
Lambda = [log(2)-p*log(X^2/2^133)]/2.
```

Using a 30-term positive atanh lower sum for `log(2)` and an exact upper series bound for `log(X^2/2^133)`, the verifier proves

```text
Lambda > (1/X)*sum_i 1/n_i.
```

This contradicts the cycle identity

```text
Lambda = sum_i log(1+1/(X*n_i))
       <= (1/X)*sum_i 1/n_i.
```

Hence the displayed length is impossible.

## 4. Updated sparse window

Up to

```text
355561454311274250377
```

the only lengths not yet excluded are now the six odd values

```text
177780727155637125185
177780727155637125187
177780727155637125189
177780727155637125191
177780727155637125193
177780727155637125195
```

The contiguous cycle barrier consequently rises to

```text
177780727155637125184.
```

Run

```text
python tools/verify_first_exception_elimination.py
```

for the exact certificate.