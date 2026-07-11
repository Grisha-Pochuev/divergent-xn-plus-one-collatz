# One-block no-exceptional cycles with `D<=500` do not exist

Use the primary candidate

```text
m=4501,
B=2^4501,
N=2^500-1,
d=349*2^500-347,
X=B-d.
```

This note closes an infinite family of hypothetical cycles: every cycle length
is allowed, but the cycle is assumed to contain exactly one complete ordinary
near-power block and total credit

```text
1<=D<=500.
```

No trajectory cutoff or cycle-length cutoff occurs.

## 1. Exact one-block equation

A one-block ordinary cycle of length `p` and terminal deficit `D` has valuation
word, up to cyclic rotation,

```text
m,m,...,m,m-D,
```

with `p-1` copies of `m`. Its source coordinate has the form

```text
d*n-1=2^(m*p-D)*u,
u positive and odd.                                   (1)
```

The complete-block endpoint formula is

```text
C_X^p(n)=(X^p*u+2^D)/d.                              (2)
```

Cycle closure `C_X^p(n)=n` gives

```text
Delta_D(p)*u=2^D-1,                                 (3)
```

where

```text
Delta_D(p)=2^(m*p-D)-X^p.                           (4)
```

Therefore

```text
1<=Delta_D(p)<=2^D-1.                               (5)
```

The quantity `Delta_D(p)` is odd.

## 2. Reduction modulo `N=2^500-1`

The primary construction gives

```text
N|X,
ord_N(2)=500,
m==1 (mod 500).                                     (6)
```

Reducing (4) modulo `N`,

```text
Delta_D(p)==2^(p-D) (mod N),                        (7)
```

where the exponent is reduced modulo `500`.

For `1<=D<=500`,

```text
2^D-1<=N.                                           (8)
```

Let `r` be `p-D` modulo `500`.

If `r!=0`, the least residue in (7) is the even integer `2^r`. By (5) and (8),
`Delta_D(p)` would have to equal that residue, contradicting that
`Delta_D(p)` is odd.

Hence

```text
r=0,
Delta_D(p)=1.                                       (9)
```

## 3. Final contradiction modulo `8`

For the primary multiplier,

```text
X==3 (mod 8).                                       (10)
```

Also

```text
m*p-D>=4501-500>3,
```

so the power of two in (4) vanishes modulo `8`.

If `p` is odd, then

```text
Delta_D(p)==-3==5 (mod 8).
```

If `p` is even, then

```text
Delta_D(p)==-1==7 (mod 8).
```

Neither case is compatible with `Delta_D(p)=1`. This contradicts (9).

Therefore:

```text
There is no one-block no-exceptional positive cycle
with 1<=D<=500, for any cycle length p.             (11)
```

## 4. Meaning

This is the first infinite cycle family completely removed for the new primary
candidate. It is not a finite barrier: `p` is unrestricted.

The next natural extensions are:

1. one block with `501<=D<=4500`;
2. two blocks with `D<=500`;
3. fixed `D` with all of its deficit compositions.

For larger `D`, the simple inequality `2^D-1<=N` no longer holds, so higher
powers `N^2,N^3,...` from the `N`-adic ladder should replace the first-level
congruence.

## 5. Verification

```text
python tools/verify_no_exceptional_one_block_small_credit.py
```

The checker verifies the residue alternatives for every `D=1,...,500` and every
possible `p mod 500`, followed by the modulo-`8` contradiction.
