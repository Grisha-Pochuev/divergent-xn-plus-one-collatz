# One exceptional block plus one ordinary block is impossible

Use the primary candidate

```text
m=4501,
B=2^4501,
d=349*2^500-347,
X=B-d.
```

This note treats a cycle with exactly two complete blocks:

1. one ordinary block of length `ell` and terminal deficit `e`;
2. one exceptional block of length `k` and excess valuation `b`.

Cycle closure requires

```text
1<=b<e<=4500,
D=e-b>=1,
p=ell+k.
```

The theorem excludes all such parameters and all block lengths.

## 1. Two exact source-core equations

Let `u` be the positive odd core at the ordinary source and `v` the positive
odd core at the exceptional source. Put

```text
q=2^(m*ell-e),
c_e=2^e-1,
c_b=2^b-1.
```

The ordinary block followed by the exceptional source gives

```text
B^k*v=X^ell*u+c_e.                                  (1)
```

The exceptional block followed by the ordinary source gives

```text
2^b*q*u=X^k*v-c_b.                                  (2)
```

Eliminating `v` from (1)--(2),

```text
Delta_D(p)*u=X^k*c_e-B^k*c_b,                       (3)
```

where

```text
Delta_D(p)=2^(m*p-D)-X^p.                           (4)
```

Eliminating `u` instead gives the dual equation

```text
Delta_D(p)*v=2^(m*ell-D)*c_e-X^ell*c_b.             (5)
```

Both left sides are positive in a cycle.

## 2. Choose the shorter block

If

```text
k<=floor(p/2),
```

then the positive right side of (3) is strictly less than

```text
2*B^(k+1)
 <=2*B^(floor(p/2)+1).                              (6)
```

If instead

```text
ell<=floor(p/2),
```

then the positive right side of (5) satisfies the same upper bound:

```text
2^(m*ell-D)*c_e-X^ell*c_b
 <2*B^(ell+1)
 <=2*B^(floor(p/2)+1).                              (7)
```

One of (6)--(7) always applies.

## 3. The positive cycle gap is larger

For every possible total credit

```text
1<=D<=4499,
```

exact rational logarithmic bounds certify the first integer

```text
L_D=floor(D/log2(B/X))+1
```

at which `Delta_D(p)` becomes positive. At that first length, and hence at every
later length,

```text
Delta_D(p)>2^(4500*p-22206).                        (8)
```

Every certified threshold has `p>=12`, and exact integer comparison gives

```text
4500*p-22206
 >1+4501*(floor(p/2)+1).                            (9)
```

Thus

```text
Delta_D(p)>2*B^(floor(p/2)+1).                      (10)
```

This contradicts whichever of (3) or (5) corresponds to the shorter block,
because `u,v>=1`.

## 4. Theorem

```text
For X=2^4501-349*2^500+347,
there is no positive cycle consisting of one exceptional complete block and
one ordinary complete block.
```

Consequently, any cycle with exactly one exceptional block must contain at
least two ordinary blocks.

## 5. Verification

```text
python tools/verify_one_exception_one_ordinary_no_go.py
```

The checker certifies every total credit `D=1,...,4499` and the uniform exponent
comparison. The algebraic duality between (3) and (5) covers both possible
choices of the shorter block.
