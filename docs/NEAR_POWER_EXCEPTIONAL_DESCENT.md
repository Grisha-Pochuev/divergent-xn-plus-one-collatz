# Near-power exceptional descent

This note records an exact structural identity for accelerated maps whose
multiplier lies below a power of two.

Let

```text
B=2^m,
d odd,
1<=d<B,
X=B-d>=5,
C_X(n)=(X*n+1)/2^v2(X*n+1).
```

All variables below are positive odd integers unless stated otherwise.

## 1. Complete valuation trichotomy

For an odd `n` with `d*n>1`, write

```text
r=v2(d*n-1),
d*n-1=2^r*u,
u odd.
```

Since

```text
X*n+1=B*n-(d*n-1)=2^m*n-2^r*u,
```

there are exactly three cases.

### Case A: `r<m`

The bracket after factoring `2^r` is odd, so

```text
v2(X*n+1)=r,
C_X(n)=2^(m-r)*n-u.
```

### Case B: `r>m`

The bracket after factoring `2^m` is odd, so

```text
v2(X*n+1)=m,
C_X(n)=n-2^(r-m)*u.
```

Moreover

```text
d*C_X(n)-1=2^(r-m)*X*u,
```

and hence

```text
v2(d*C_X(n)-1)=r-m.
```

Thus an overlong tail `r>m` is stripped by exactly one block of `m` binary
zeroes.

### Case C: `r=m`

Here

```text
n=(B*u+1)/d.
```

The following exact identity holds:

```text
X*n+1=B*(X*u+1)/d.                         (1)
```

Indeed,

```text
(B-d)*(B*u+1)+d=B*((B-d)*u+1).
```

Because `d` is odd, (1) gives

```text
v2(X*n+1)=m+v2(X*u+1),
C_X(n)=C_X(u)/d.                            (2)
```

The divisibility in (2) is automatic: `d | B*u+1` and `B==X (mod d)`, so
`d | X*u+1`; division by a power of two does not remove an odd factor `d`.

This is the only case in which the valuation can exceed `m`.

## 2. Exceptional-descent formulation

Define, whenever it is integral,

```text
R(u)=(B*u+1)/d.
```

Then `R(u)>u`, because

```text
R(u)-u=(X*u+1)/d>0.
```

Equations (1)--(2) become

```text
v2(X*R(u)+1)=m+v2(X*u+1),
C_X(R(u))=C_X(u)/d.
```

Therefore every step with valuation greater than `m` has a unique smaller
auxiliary integer `u`: the excess valuation is not arbitrary, but is the
valuation of the same `Xn+1` rule at that smaller integer.

If the exceptional representation can be iterated `k` times, then

```text
n=R^k(v),
v2(X*n+1)=k*m+v2(X*v+1),
C_X(n)=C_X(v)/d^k.
```

This is a finite descent because `R(u)>u`.

## 3. Specialization to `X=13`

Take

```text
m=4,
B=16,
d=3,
X=13.
```

For every odd `n`, put `r=v2(3*n-1)`.

- If `r<4`, then `v2(13*n+1)=r`.
- If `r>4`, then `v2(13*n+1)=4` and the new value has
  `v2(3*C_13(n)-1)=r-4`.
- If `r=4`, write

```text
n=(16*u+1)/3.
```

Then

```text
v2(13*n+1)=4+v2(13*u+1),
C_13(n)=C_13(u)/3,
u<n.
```

Thus all dangerous `a>4` steps for `13n+1` are recursively represented by the
same map on a strictly smaller integer.

## 4. What this proves and what remains

This is an exact infinite-family theorem, not trajectory evidence. It replaces
an unstructured large valuation by a finite arithmetic descent and supplies a
new possible route to an unbounded height-dependent potential.

It does **not** yet prove that the orbit of `1` for `X=13`, or any other orbit,
diverges. The missing global step is to show that the exceptional descents
cannot occur frequently enough to compensate for the many expanding low-
valuation steps.

Independent checker:

```text
python tools/verify_near_power_exceptional_descent.py
```
