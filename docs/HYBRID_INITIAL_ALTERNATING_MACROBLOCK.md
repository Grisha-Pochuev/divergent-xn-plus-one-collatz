# Initial alternating macroblock for `X=2^m-3`

Let

```text
B=2^m,
X=B-3,
m>=4,
C_X(n)=(X*n+1)/2^v2(X*n+1).
```

This note proves an exact initial macroblock for the orbit from `n0=1`.

## 1. A forced two-step block

Assume that

```text
n == 1 (mod 16).
```

Since `X==13 (mod 16)`,

```text
X*n+1 == 14 (mod 16),
```

so the first exact valuation is

```text
v2(X*n+1)=1.
```

After this step,

```text
n_1=(X*n+1)/2.
```

The numerator of the next accelerated step satisfies

```text
2*(X*n_1+1)=X^2*n+X+2.
```

Modulo `16`,

```text
X^2*n+X+2 == 13^2+13+2 == 24 == 8 (mod 16).
```

Hence

```text
v2(X*n_1+1)=2.
```

Thus every input `n==1 (mod 16)` has the forced valuation pair

```text
(1,2),
```

and its exact two-step image is

```text
F(n)=C_X^2(n)=(X^2*n+X+2)/8.                       (1)
```

## 2. Precision transfer

Subtracting `1` from (1) and using

```text
X^2+X-6=(X+3)*(X-2)=B*(B-5)
```

gives

```text
F(n)-1=[X^2*(n-1)+B*(B-5)]/8.                     (2)
```

For the initial value `n=1`,

```text
v2(F(1)-1)=m-3,                                    (3)
```

because `B-5` is odd.

More generally, if

```text
4<=L=v2(n-1)<m,
```

then the two summands in (2) have distinct valuations `L-3` and `m-3`.
Therefore

```text
v2(F(n)-1)=L-3.                                    (4)
```

So every forced pair removes exactly three binary zeroes from `n-1`.

## 3. Exact initial length

Set

```text
J=floor((m-1)/3).
```

Starting from `n0=1`, equations (3)--(4) show inductively that the first `J`
two-step blocks are all valid and have the exact valuation word

```text
1,2,1,2,...,1,2
```

with `J` copies of `(1,2)`.  After these `2J` accelerated steps,

```text
A_(2J)=3J,
v2(n_(2J)-1)=m-3J in {1,2,3}.                     (5)
```

No trajectory scan is used in this derivation.

## 4. Rigorous growth over the block

Equation (1) gives the strict inequality

```text
F(n)>X^2*n/8.
```

Iterating through all `J` forced pairs yields

```text
n_(2J)>X^(2J)/2^(3J).                               (6)
```

For the hybrid candidate

```text
m=260,
X=2^260-3,
n0=1,
J=86,
```

we obtain exactly

```text
first accelerated steps: 172,
exact valuation word: (1,2)^86,
total valuation: A_172=258,
v2(n_172-1)=2,
n_172>X^172/2^258.
```

Thus the orbit begins with a completely proved expanding macroblock of 172 odd
steps.  Its logarithmic gain is greater than

```text
172*log2(X)-258,
```

which is approximately `44462` bits.

## 5. Limitation

This is a finite exact macroblock, not a divergence proof.  At its endpoint the
precision `v2(n-1)` has fallen to `2`, so the next valuation is no longer forced
by this two-step mechanism.  The next global task is to construct a return or
renewal theorem that recreates a high-precision `n==1 (mod 16)` state while
retaining enough of the accumulated growth.

Independent checker:

```text
python tools/verify_hybrid_initial_alternating_macroblock.py
```
