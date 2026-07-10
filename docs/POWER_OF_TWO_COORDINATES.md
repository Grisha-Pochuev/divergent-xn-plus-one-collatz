# Exact coordinates around powers of two

This note gives exact local normal forms for the two especially structured multiplier families

```text
X_+ = 2^m+1,
X_- = 2^m-1,
```

with `m>=2`.

They are useful because the halving count is controlled by the distance from `-1` in the Fermat-type case and by the distance from `+1` in the Mersenne-type case.

## 1. Fermat-type multiplier `X=2^m+1`

Write a positive odd integer as

```text
n+1 = 2^s*h,
```

where `s>=1` and `h` is odd. Then

```text
X*n+1 = 2^s*X*h - 2^m.
```

Therefore the accelerated transition has three exact cases.

### Case `s<m`

```text
a = v2(X*n+1) = s,
C_X(n) = X*h - 2^(m-s).
```

### Case `s>m`

```text
a = m,
C_X(n) = 2^(s-m)*X*h - 1.
```

In particular,

```text
v2(C_X(n)+1)=s-m.
```

Thus every ordinary valuation-`m` step subtracts exactly `m` units of `v2(n+1)` and multiplies the odd cofactor by `X`.

### Exceptional case `s=m`

```text
X*n+1 = 2^m*(X*h-1),
C_X(n) = oddpart(X*h-1),
a = m+v2(X*h-1).
```

This is the unique exceptional layer already visible in the earlier valuation lemma.

## 2. Exact grouped transition for `X=2^m+1`

Write

```text
s = m*L+r,    0<=r<m.
```

### If `r=0`

After `L-1` ordinary valuation-`m` steps and one exceptional step,

```text
C_X^L(n) = oddpart(X^L*h-1).                     (F0)
```

The previous complete macroblock is the special case `h=1`.

### If `1<=r<m`

After `L` ordinary valuation-`m` steps, the state is

```text
2^r*X^L*h-1.
```

One more accelerated step gives

```text
C_X^(L+1)(n) = X^(L+1)*h - 2^(m-r).              (F1)
```

Equations (F0) and (F1) give the exact exit from every `v2(n+1)` tower, not only towers with cofactor `h=1`.

## 3. Mersenne-type multiplier `Q=2^m-1`

Now write

```text
n-1 = 2^s*h,
```

with `s>=1` and `h` odd. Then

```text
Q*n+1 = 2^m + Q*2^s*h.
```

Again there are three exact cases.

### Case `s<m`

```text
a=s,
C_Q(n)=Q*h+2^(m-s).
```

### Case `s>m`

```text
a=m,
C_Q(n)=1+Q*2^(s-m)*h,
v2(C_Q(n)-1)=s-m.
```

### Exceptional case `s=m`

```text
Q*n+1 = 2^m*(Q*h+1),
C_Q(n)=oddpart(Q*h+1)=C_Q(h).                    (M)
```

Equation (M) is an exact self-similarity identity:

```text
C_(2^m-1)(1+2^m*h) = C_(2^m-1)(h)
```

for every positive odd `h`.

Thus the entire future of `1+2^m*h` merges after one accelerated step with the future of the much smaller number `h`.

## 4. Consequences for the search

1. The Fermat-type regenerative search can now work with arbitrary odd cofactors `h`, rather than only starts `2^(mL)-1`.
2. The exact exits (F0) and (F1) provide a natural compressed transition system for searching chains of growth blocks.
3. The Mersenne identity (M) gives a recursive structure for predecessor basins and cycle investigations.
4. None of these identities alone excludes all positive cycles or proves an infinite divergent orbit. They provide exact algebra for the next certificate search.

All identities are tested over finite grids by `tests/test_power_coordinates.py`.