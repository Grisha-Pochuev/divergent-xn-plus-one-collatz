# Complete near-power blocks and a minimal-basin lemma

Let

```text
B=2^m,
d odd,
1<=d<B/2,
X=B-d>=5,
C_X(n)=(X*n+1)/2^v2(X*n+1).
```

For a positive odd `n`, write

```text
d*n-1=2^r*u,
r>=1,
u odd.
```

This note extends the one-step near-power descent to complete valuation blocks.

## 1. Complete nonexceptional blocks

Suppose

```text
r=m*k+s,
k>=0,
1<=s<=m-1.
```

Then the next `k+1` exact valuations are

```text
m,m,...,m,s
```

with `k` copies of `m`.  If `n_j=C_X^j(n)`, then for `0<=j<=k`,

```text
d*n_j-1=2^(m*(k-j)+s)*X^j*u.                       (1)
```

The exact endpoint is

```text
C_X^(k+1)(n)=(X^(k+1)*u+2^(m-s))/d.                 (2)
```

Indeed, every high-layer step uses

```text
C_X(n_j)=n_j-2^(r_j-m)*u_j,
d*C_X(n_j)-1=2^(r_j-m)*X*u_j,
```

which proves (1) inductively.  At the final low layer, direct substitution gives
(2).

Since

```text
n=(2^(m*k+s)*u+1)/d,
```

we have the exact block displacement

```text
C_X^(k+1)(n)-n
 =((X^(k+1)-2^(m*k+s))*u+(2^(m-s)-1))/d.             (3)
```

Consequently the whole block grows for every allowed odd `u` whenever

```text
X^(k+1)>2^(m*k+s).                                   (4)
```

## 2. Complete exceptional blocks

Suppose

```text
r=m*k,
k>=1.
```

After `k-1` valuation-`m` steps, put

```text
w=X^(k-1)*u.
```

The current state satisfies

```text
d*n_(k-1)-1=B*w,
```

and the final exceptional step gives

```text
C_X^k(n)=C_X(w)/d.                                   (5)
```

The quotient is an integer by the exact near-power divisibility identity.
Moreover every exceptional complete block strictly contracts:

```text
C_X^k(n)<n.                                          (6)
```

To see this, write `b=v2(X*w+1)>=1`.  Then

```text
C_X^k(n)=(X*w+1)/(d*2^b)
         <=(X^k*u+1)/(2*d)
         <(B^k*u+1)/d
         =n.
```

## 3. Minimal-basin lemma

Assume that `C_X` has a nontrivial positive cycle `Gamma`, and let `w0` be the
least positive odd integer whose orbit enters `Gamma`.

Write

```text
d*w0-1=2^r*u.
```

Then necessarily

```text
1<=r<m.                                              (7)
```

If `r>m`, the first high-layer step is strictly smaller than `w0` and remains in
the same basin, contradicting minimality.  If `r` is a positive multiple of
`m`, (6) gives the same contradiction after the complete exceptional block.
If `r=m*k+s` with `k>=1` and `1<=s<m`, the very first valuation-`m` step is also
strictly smaller than `w0`.  Hence all `r>=m` are impossible at the least basin
seed.

For `r<m`, the first step is strictly expanding.  In fact,

```text
C_X(w0)-w0=((B-2^r-d)*w0+1)/2^r>0,                  (8)
```

because `r<=m-1` and `d<B/2`.

Thus every hypothetical nontrivial cycle has a well-founded basin seed in one
of the finitely many low layers `r=1,...,m-1`, and its first step grows.

## 4. Specialization to the hybrid candidate

For

```text
m=260,
d=3,
X=2^260-3,
```

a least seed entering a hypothetical nontrivial cycle must satisfy

```text
1<=v2(3*w0-1)<=259,
```

and its first accelerated step is strictly larger than `w0`.

Every nonexceptional block has the exact endpoint

```text
C_X^(k+1)(n)=((2^260-3)^(k+1)*u+2^(260-s))/3.
```

Every multiple-of-`260` exceptional block is strictly contracting and therefore
cannot begin at the least element of a cycle basin.

## 5. Limitation

The lemma does not exclude contractions later in the orbit, after earlier
expansion has accumulated enough height.  The remaining global task is a
height-credit or record-minimum argument that propagates (7)--(8) beyond the
first block.

Independent checker:

```text
python tools/verify_near_power_complete_blocks.py
```
