# Explicit candidates with arbitrarily large finite cycle barriers

This note generalizes the strong candidate construction.

## Theorem

For every positive integer `B`, one can explicitly construct an odd multiplier `Q>=5` such that the accelerated orbit from `n0=1`

1. never returns to `1`; and
2. cannot enter any nontrivial positive cycle of accelerated odd length at most `B`.

Consequently, for every `B` there is an explicit pair `(Q,1)` whose orbit either tends to positive infinity or enters a nontrivial cycle longer than `B`.

The multiplier depends on `B`; therefore this theorem alone is not yet a single divergent orbit.

## 1. Construction

Choose an integer `K>=8` such that

```text
2^K > 255*B.                                     (1)
```

Put

```text
R = 2^K*sqrt(2) = sqrt(2^(2K+1)).
```

Choose `Q` to be the smallest number larger than `R` of the form

```text
Q = 21*t,
```

where `t` is odd and not divisible by `3`.

The allowed values of `t` are the residue classes `1` and `5` modulo `6`. Consecutive allowed multipliers `21*t` differ alternately by `84` and `42`. Hence

```text
0 < Q-R <= 84.                                   (2)
```

The construction is exact and uses an integer square root; see `tools/generate_cycle_barrier.py`.

## 2. Why the orbit cannot return to 1

Let

```text
ell = ord_Q(2).
```

Since `3|Q` and `7|Q`, the order `ell` is a multiple of both

```text
ord_3(2)=2,
ord_7(2)=3.
```

Thus `6|ell`.

Also `3` divides `Q` exactly once because `3` does not divide `t`. By the lifting-the-exponent lemma,

```text
v3(2^ell-1)
 = v3(2^2-1) + v3(ell/2)
 >= 2.
```

Therefore

```text
gcd(Q, (2^ell-1)/Q) >= 3.
```

So `Q` is a Wieferich number in the Franco-Pomerance sense. Every direct predecessor of `1` shares a factor with `Q`, whereas every accelerated output is coprime to `Q`. Once the orbit has left `1`, it can never return.

For `K>=8`, equation (2) also gives

```text
2^K < Q+1 < 2^(K+1),
```

so `Q+1` is not a power of two and the first accelerated step is not `1`.

## 3. Excluding all cycles of length at most B

Suppose the orbit entered a nontrivial cycle of length `p<=B`. As in `STRONG_CANDIDATE_759250131.md`, if `A` is the total number of halvings around the cycle, then

```text
Q^p < 2^A <= (Q+1/3)^p.                          (3)
```

Write

```text
U = Q+1/3 = R+e.
```

From (2),

```text
e <= 84+1/3 = 253/3.
```

Since `R>2^K`, condition (1) gives

```text
p*e/R <= B*e/R < 1/3.
```

Therefore

```text
(U/R)^p = (1+e/R)^p
        < exp(1/3)
        < sqrt(2).                                (4)
```

The last strict inequality follows from

```text
ln(2) > 2/3,
```

which is an elementary midpoint lower bound for the integral of `1/x` on `[1,2]`.

Now distinguish the parity of `p`.

### Even p

If `p=2r`, then

```text
R^p = 2^((2K+1)r)
```

is an integer power of two. We have

```text
R^p < Q^p < 2^A <= U^p < R^p*sqrt(2) < 2*R^p.
```

There is no integer power of two strictly between `R^p` and `2*R^p`, contradiction.

### Odd p

If `p=2r+1`, then `R^p` is exactly a half-integral power of two. The next integer power of two is

```text
R^p*sqrt(2).
```

But (3) and (4) give

```text
R^p < Q^p < 2^A <= U^p < R^p*sqrt(2),
```

again leaving no possible integer power of two.

Thus no nontrivial positive cycle of length `p<=B` exists for the constructed candidate orbit. QED.

## 4. Meaning and limitation

This theorem makes the cycle obstruction arbitrarily remote by construction. For example, one may generate a candidate with a certified barrier larger than `10^100` without iterating its trajectory.

However, increasing `B` changes `Q`. The theorem does not provide one fixed ordinary integer multiplier whose cycles are excluded at every length. The remaining prize-level challenge is precisely to replace this family of arbitrarily strong finite statements by one infinite statement for a single pair.