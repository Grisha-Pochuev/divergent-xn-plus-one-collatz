# Minimal-basin lemma for Mersenne multipliers

Let

```text
B=2^m,
X=B-1,
m>=3.
```

Assume, only for this lemma, that the accelerated map `C_X` has a nontrivial
positive cycle `Gamma`.

Consider the nonempty set

```text
Basin(Gamma)={positive odd n : some iterate of n belongs to Gamma}.
```

By well-ordering it has a least element; call it `w`.

## Theorem

The least basin element satisfies

```text
1<=v2(w-1)<m.                                    (1)
```

Consequently its first accelerated step is strictly expanding:

```text
C_X(w)>w.                                         (2)
```

## Proof

The element `w` is not `1`, because `1` belongs to the separate trivial fixed
cycle for the accelerated Mersenne map.

Write

```text
w-1=2^r*u,
u odd.
```

Suppose first that `r>m`.  The complete Mersenne trichotomy gives

```text
C_X(w)=X*2^(r-m)*u+1.
```

Since `X=B-1<B`,

```text
C_X(w)<B*2^(r-m)*u+1=w.
```

But `C_X(w)` also belongs to `Basin(Gamma)`, contradicting the minimality of
`w`.

Suppose next that `r=m`.  Then the exceptional identity gives

```text
C_X(w)=C_X(u),
u<w.
```

Therefore the orbit of the smaller positive odd integer `u` has the same tail
from that point and also enters `Gamma`, again contradicting minimality.

The only remaining possibility is (1).

For `r<m`, the exact formula is

```text
C_X(w)=X*u+2^(m-r),
w=2^r*u+1.
```

Therefore

```text
C_X(w)-w=(X-2^r)*u+(2^(m-r)-1)>0,
```

because `r<=m-1` and hence `X=2^m-1>2^r`.  This proves (2).

## Specialization to `X=15`

If a nontrivial positive cycle for `15n+1` exists, the least positive odd seed
whose orbit reaches it must have

```text
v2(w-1) in {1,2,3}
```

and must begin with a strictly increasing step.

This does not exclude a cycle, but it proves that neither an ordinary long-zero
contraction nor an exceptional identical-tail contraction can occur at the
well-founded bottom of its basin.  Any completed infinite-descent proof now
only has to handle the three low-tail entrance types.

Dependencies:

```text
docs/MERSENNE_COMPLETE_VALUATION_BLOCKS.md
tools/verify_mersenne_complete_valuation_blocks.py
```
