# General burst reduction for `X = 2^m + 1`

Fix

```text
X = 2^m + 1,   m >= 2.
```

This note extends the earlier complete macroblock formula from the special start
`2^(mL)-1` to every positive odd core `u`.

## 1. Exact burst formula

Let `L>=1`, let `u` be positive and odd, and put

```text
n_0 = 2^(mL)*u - 1.
```

For `0<=j<=L-1`, define

```text
n_j = 2^(m(L-j))*X^j*u - 1.
```

For every `j<L-1`,

```text
v2(X*n_j+1)=m
```

and the accelerated map sends `n_j` to `n_(j+1)`.

At the final pre-exit state,

```text
n_(L-1)=2^m*X^(L-1)*u-1,
```

so

```text
X*n_(L-1)+1 = 2^m*(X^L*u-1).
```

Write

```text
r = v2(X^L*u-1).
```

Then the final valuation is exactly `m+r`, and after all `L` accelerated steps the endpoint is

```text
T_(m,L)(u) = (X^L*u-1)/2^r.                 (1)
```

Thus every state with a large value of `v2(n+1)` has an exact finite reduction to the odd part of one affine expression.

## 2. A sufficient net-growth criterion

Put

```text
delta_m = log2(1+2^(-m)).
```

If

```text
L*delta_m > r+1,                              (2)
```

then the complete burst grows:

```text
T_(m,L)(u) > n_0.
```

Indeed,

```text
T_(m,L)(u)
  = (X^L*u-1)/2^r
  > X^L*u/2^(r+1)
  = 2^(mL)*u * 2^(L*delta_m-r-1).
```

Condition (2) makes the final factor larger than one, and hence

```text
T_(m,L)(u) > 2^(mL)*u > 2^(mL)*u-1=n_0.
```

The only quantity capable of destroying the accumulated gain is therefore the exit valuation

```text
r=v2(X^L*u-1).
```

## 3. Exact coding of the exit valuation

For every prescribed `r>=1`, the condition

```text
v2(X^L*u-1)=r
```

is equivalent to the single residue condition

```text
u == X^(-L)*(1+2^r)   (mod 2^(r+1)).          (3)
```

Here the inverse is taken modulo `2^(r+1)`.

Proof: exact valuation `r` means

```text
X^L*u-1 == 2^r  (mod 2^(r+1)),
```

and `X^L` is odd and invertible modulo `2^(r+1)`.

Consequently, every desired finite exit valuation occurs for infinitely many positive odd cores `u`. In particular, whenever `r+1<L*delta_m`, there are infinitely many complete bursts with that exact exit and rigorous net growth.

## 4. Canonical decomposition of every positive odd state

For an arbitrary positive odd `n`, write

```text
s=v2(n+1),
s=mL+q,   0<=q<m.
```

If `L>=1`, then the first `L` accelerated steps with valuation `m` are forced until the residual precision falls into the finite low layer `q<=m` (with the equality layer handled by the exit formula above).

Thus the dynamics for `X=2^m+1` naturally separates into:

1. deterministic valuation-`m` bursts;
2. one exit controlled by the odd core and a single congruence;
3. a return to a low-precision layer.

This reduces the infinite-orbit problem to a return map on odd cores rather than the original huge integers.

## 5. Consequence for the divergence search

The earlier special construction was not isolated. Every large-precision state belongs to an explicitly solvable burst family, and every finite exit valuation can be prescribed by one residue class.

A complete proof of divergence can now target a sequence of cores `u_j` and burst lengths `L_j` satisfying

```text
L_j*delta_m > r_j+1
```

with

```text
r_j=v2(X^(L_j)*u_j-1),
```

while the endpoint of one burst supplies the next state. The missing global step is to prove that one ordinary positive start produces infinitely many such net-positive bursts.

The result is exact and finite at every stage; no probabilistic assumption is used.
