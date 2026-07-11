# Complete valuation blocks for `X=13`

This note strengthens `NEAR_POWER_EXCEPTIONAL_DESCENT.md` by grouping every
possible value of

```text
r=v2(3*n-1)
```

into one exact accelerated block.

Throughout,

```text
C(n)=(13*n+1)/2^v2(13*n+1)
```

and `n` is positive and odd.  Write

```text
3*n-1=2^r*u,
```

where `r>=1` and `u` is odd.

## 1. Nonexceptional blocks

Suppose

```text
r=4*k+s,
0<=k,
s in {1,2,3}.
```

Then the next `k+1` exact valuations are

```text
4,4,...,4,s
```

with `k` copies of `4`, and

```text
C^(k+1)(n)=(13^(k+1)*u+2^(4-s))/3.                (1)
```

More precisely, after `j` of the valuation-`4` steps, for `0<=j<=k`,

```text
3*C^j(n)-1=2^(4*(k-j)+s)*13^j*u.                  (2)
```

### Proof

If `v2(3*x-1)>4`, the near-power trichotomy gives

```text
v2(13*x+1)=4,
3*C(x)-1=13*(3*x-1)/16.
```

Applying this identity `k` times proves (2).  At `j=k`, the remaining
valuation of `3*C^k(n)-1` is `s<4`, so the trichotomy gives final valuation
`s`.  Substituting (2) into the last step gives

```text
C^(k+1)(n)
  =(13*(2^s*13^k*u+1)/3+1)/2^s
  =(13^(k+1)*u+2^(4-s))/3.
```

This proves (1).

## 2. Exact growth boundary

Subtracting the starting value

```text
n=(2^(4*k+s)*u+1)/3
```

from (1) gives

```text
3*(C^(k+1)(n)-n)
  =(13^(k+1)-2^(4*k+s))*u+(2^(4-s)-1).            (3)
```

The second term is positive.  Therefore the whole block grows for every
admissible odd `u` whenever

```text
13^(k+1)>2^(4*k+s).
```

The exact universal-growth ranges are

```text
s=1: k<=9,   equivalently r<=37;
s=2: k<=5,   equivalently r<=22;
s=3: k<=2,   equivalently r<=11.
```

Thus a nonexceptional block can contract only from the following first
thresholds:

```text
s=1: r>=41;
s=2: r>=26;
s=3: r>=15.
```

The first possible contracting inputs are already forced into thin and high
binary classes.  Using the least admissible odd `u` in each congruence class,

```text
s=1: n >= (2^41+1)/3,
s=2: n >= (5*2^26+1)/3,
s=3: n >= (2^15+1)/3=10923.
```

For every contracting nonexceptional block, (1) also gives the strict lower
ratio

```text
C^(k+1)(n)/n > 13^(k+1)/2^(4*k+s).                (4)
```

Indeed, after multiplying by the positive denominators, the difference between
the left side of (4) and the right side is `2^(4-s)-13^(k+1)/2^(4*k+s)`,
which is positive in the contracting range.

## 3. Exceptional blocks

Suppose instead

```text
r=4*k,
k>=1.
```

After `k-1` valuation-`4` steps, put

```text
w=13^(k-1)*u.
```

Then

```text
C^(k-1)(n)=(16*w+1)/3.
```

The last step is the exceptional near-power descent, so

```text
v2(13*C^(k-1)(n)+1)=4+v2(13*w+1),
C^k(n)=C(w)/3.                                    (5)
```

The auxiliary input is strictly smaller:

```text
w<n.                                               (6)
```

To prove (6), note that

```text
3*w=3*13^(k-1)*u <16^k*u+1=3*n,
```

because `3*13^(k-1)<16^k` for every `k>=1`.

Thus every multiple-of-four tail is reduced exactly to one application of the
same `13n+1` map at a strictly smaller integer, followed by division by `3`.

## 4. Consequence for the divergence search

Every positive odd state for `X=13` now belongs to exactly one of two explicit
macro-types:

1. a nonexceptional block (1), which is automatically growing except in the
   three thin high-tail ranges above;
2. an exceptional block (5), which invokes the same map at a strictly smaller
   auxiliary integer.

This is not yet a divergence proof.  It reduces the missing global argument to
charging the rare contracting nonexceptional blocks and the recursive
exceptional blocks against the expanding blocks that create their required
binary precision.

Independent checker:

```text
python tools/verify_x13_complete_valuation_blocks.py
```
