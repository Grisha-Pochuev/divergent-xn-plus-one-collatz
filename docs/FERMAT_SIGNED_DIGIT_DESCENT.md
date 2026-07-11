# Signed digit descent for `X=2^m+1`

This note gives an exact digital description of every large valuation for a
Fermat-type multiplier.

Put

```text
B=2^m,
X=B+1,
m>=2.
```

For a sign `epsilon` in `{+1,-1}`, define the signed odd-part map

```text
T_epsilon(n)=(X*n+epsilon)/2^v2(X*n+epsilon),
```

whenever the numerator is positive. The original accelerated `Xn+1` map is
`T_+` on positive odd integers. The auxiliary map `T_-` appears naturally in
the descent below.

## 1. One-block descent

If

```text
n != -epsilon (mod B),
```

then

```text
v2(X*n+epsilon)=v2(n+epsilon)<m,                 (1)
```

because `X==1 (mod B)`.

If instead

```text
n=B*u-epsilon,
```

then the exact factorization is

```text
X*n+epsilon
  =(B+1)*(B*u-epsilon)+epsilon
  =B*((B+1)*u-epsilon)
  =B*(X*u-epsilon).                              (2)
```

Therefore

```text
v2(X*n+epsilon)=m+v2(X*u-epsilon),
T_epsilon(n)=T_(-epsilon)(u).                    (3)
```

Thus every full block of `m` binary zeroes removes one signed base-`B` suffix
and flips the sign.

## 2. Exact iteration

Let

```text
epsilon_j=(-1)^j*epsilon,
S_k=1-B+B^2-...+(-B)^(k-1).
```

The descent can be applied at least `k` times exactly when

```text
n == -epsilon*S_k (mod B^k).                    (4)
```

In that case there is a unique nonnegative integer `u` such that

```text
n=B^k*u-epsilon*S_k,                             (5)
```

and repeated use of (2)--(3) gives

```text
v2(X*n+epsilon)=k*m+v2(X*u+(-1)^k*epsilon),
T_epsilon(n)=T_(((-1)^k)*epsilon)(u).            (6)
```

Consequently

```text
floor(v2(X*n+epsilon)/m)
```

is exactly the number of removable alternating signed suffix blocks. This is
an identity, not a statistical model.

## 3. Specialization to `X=9`

Take

```text
m=3,
B=8,
X=9.
```

For the original plus map:

```text
v2(9*n+1)>=3*k
```

if and only if

```text
n == -(1-8+8^2-...+(-8)^(k-1)) (mod 8^k).       (7)
```

The first residues are

```text
k=1: n == 7   (mod 8),
k=2: n == 7   (mod 64),
k=3: n == 455 (mod 512),
k=4: n == 455 (mod 4096).
```

In ordinary base-8 digits, the required low-order pattern for the plus map is

```text
7,0,7,0,7,0,...
```

read from least significant digit upward. After each removed digit the
auxiliary sign flips.

Examples:

```text
n=7:  9*n+1=64,       v2=6;
n=23: 9*n+1=208,      v2=4.
```

For `n=7`, two complete three-bit blocks are removed. For `n=23`, only one full
block is removed and the signed remainder contributes one additional bit.

## 4. Relevance to the prize problem

For the orbit `X=9,n0=1`, the earlier transformed recurrence reduces divergence
to a global upper bound on cumulative valuations. The present theorem gives an
exact description of the only way a single valuation can be large: the current
integer must carry a long, uniquely prescribed signed base-8 suffix.

The remaining global question is now sharper:

> Prove that the `9n+1` orbit from `1` cannot create these alternating suffixes
> often enough for the cumulative halving count to reach `3t`.

This theorem alone is not a divergence proof. It supplies the exact digital
mechanism that any proof of the proposed `X=9` invariant must control.

Independent checker:

```text
python tools/verify_fermat_signed_digit_descent.py
```
