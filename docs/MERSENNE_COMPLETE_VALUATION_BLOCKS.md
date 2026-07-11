# Complete valuation blocks for Mersenne multipliers

Let

```text
B=2^m,
X=B-1,
m>=3,
C_X(n)=(X*n+1)/2^v2(X*n+1).
```

This note gives an exact block decomposition for every positive odd `n>1`.
It is independent of the unusable published Mersenne-cycle proof recorded in
`LITERATURE_AUDIT_SANTOS.md`.

Write

```text
n-1=2^r*u,
r>=1,
u odd.
```

## 1. One-step trichotomy

Because

```text
X*n+1=B*n-(n-1)=2^m*n-2^r*u,
```

there are three cases.

### Case A: `r<m`

```text
v2(X*n+1)=r,
C_X(n)=X*u+2^(m-r).                               (1)
```

### Case B: `r>m`

```text
v2(X*n+1)=m,
C_X(n)=X*2^(r-m)*u+1,                             (2)
C_X(n)-1=X*2^(r-m)*u.
```

Thus one step removes exactly one full block of `m` trailing zeroes from
`n-1` and multiplies the remaining odd coordinate by `X`.

### Case C: `r=m`

Here `n=B*u+1`, and

```text
X*n+1=B*(X*u+1).
```

Consequently

```text
v2(X*n+1)=m+v2(X*u+1),
C_X(n)=C_X(u).                                    (3)
```

The exceptional state and the strictly smaller integer `u` have exactly the
same next accelerated value and therefore exactly the same infinite tail after
that point.

## 2. Complete nonexceptional blocks

Suppose

```text
r=m*k+s,
0<=k,
1<=s<=m-1.
```

Then the next `k+1` exact valuations are

```text
m,m,...,m,s
```

with `k` copies of `m`.  For `0<=j<=k`,

```text
C_X^j(n)-1=2^(m*(k-j)+s)*X^j*u.                  (4)
```

The exact endpoint is

```text
C_X^(k+1)(n)=X^(k+1)*u+2^(m-s).                  (5)
```

Subtracting `n=2^(m*k+s)*u+1` gives

```text
C_X^(k+1)(n)-n
 =(X^(k+1)-2^(m*k+s))*u+(2^(m-s)-1).             (6)
```

Hence the whole block grows for every odd `u` whenever

```text
X^(k+1)>2^(m*k+s).                               (7)
```

If the leading coefficient is contracting, the endpoint still obeys the strict
ratio bound

```text
C_X^(k+1)(n)/n > X^(k+1)/2^(m*k+s).              (8)
```

## 3. Complete exceptional blocks

Suppose

```text
r=m*k,
k>=1.
```

After `k-1` valuation-`m` steps, put

```text
w=X^(k-1)*u.
```

Then the current state is `B*w+1`, so the last exceptional step gives

```text
C_X^k(n)=C_X(w).                                  (9)
```

Moreover

```text
w<n,                                               (10)
```

because

```text
X^(k-1)*u < B^k*u+1=n.
```

Equation (9) is stronger than a one-step numerical estimate: the entire future
of `n`, after the block, is exactly the future of the smaller ordinary integer
`w` after one step.

## 4. Specialization to `X=15`

Take

```text
m=4,
B=16,
X=15.
```

The exact universal-growth ranges in (7) are

```text
s=1: k<=31, so r<=125;
s=2: k<=20, so r<=82;
s=3: k<=9,  so r<=39.
```

The first possible contracting nonexceptional blocks therefore require

```text
s=1: r>=129,
s=2: r>=86,
s=3: r>=43.
```

In particular, the smallest possible input of a contracting nonexceptional
block is at least

```text
2^43+1 = 8796093022209.
```

All smaller nonexceptional blocks are rigorously increasing.  Every exceptional
block has the exact smaller-tail replacement (9).

## 5. What remains

This theorem does not prove that `(X,n0)=(15,3)` diverges, and it does not
restore the retracted claim that Mersenne multipliers have only the trivial
cycle.

It reduces the missing argument to two sharply separated phenomena:

1. extremely deep nonexceptional tails, beginning only at `r=43` for `X=15`;
2. exceptional tails, which can always be replaced by an ordinary smaller
   integer with the identical future tail.

A successful well-founded or height-dependent argument may now use the exact
tail replacement rather than the invalid rational divisibility descent in the
published proof.

Independent checker:

```text
python tools/verify_mersenne_complete_valuation_blocks.py
```
