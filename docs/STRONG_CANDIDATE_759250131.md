# Strong candidate: `(X,n0)=(759250131,1)`

This note combines the Wieferich/strong-Crandall reduction with an exact cycle-length obstruction.

Set

```text
Q = 759250131 = 3*29*271*32203
```

and consider the accelerated map

```text
C_Q(n) = (Q*n+1)/2^v2(Q*n+1)
```

on positive odd integers.

## 1. The orbit from 1 never returns to 1

The multiplicative order of `2` modulo `Q` is

```text
ell = 6762420.
```

Moreover,

```text
gcd(Q, (2^ell-1)/Q) > 1.
```

The quotient is understood modulo `Q`; the exact modular certificate gives gcd `3`.

Thus `Q` is a Wieferich number in the Franco-Pomerance sense. The argument in `WIEFERICH_1093_REDUCTION.md` works without primality:

- every direct predecessor of `1` shares a nontrivial factor with `Q`;
- every output `C_Q(x)` is coprime to `Q`.

The first step is

```text
C_Q(1) = 189812533 != 1.
```

Therefore the orbit from `1` never returns to `1`.

By the positive integer orbit dichotomy, this orbit either tends to infinity or enters a nontrivial positive cycle.

## 2. Product identity for a positive cycle

Suppose a nontrivial positive odd cycle has length `p`, elements

```text
n_0,...,n_(p-1),
```

and exact halving counts `a_i`. Put

```text
A = a_0+...+a_(p-1).
```

Multiplying

```text
2^a_i * n_(i+1) = Q*n_i+1
```

around the cycle gives the exact identity

```text
2^A = product_i (Q + 1/n_i).                    (1)
```

The cycle cannot contain `1`, because the candidate orbit never reaches `1`. Hence every odd cycle element is at least `3`. From (1),

```text
Q^p < 2^A <= (Q+1/3)^p.                         (2)
```

The question is whether an integer power of two can fit inside this very narrow interval.

## 3. Near-half-power structure

The chosen multiplier lies just above the half-integral power `2^29.5`:

```text
Q^2 = 2^59 + 9120093673.
```

Put

```text
U = Q+1/3
```

and define the positive rational number `y` by

```text
U^2 = 2^59 * (1+y).
```

Exactly,

```text
y = 86636343844 / 5188146770730811392.
```

We use the elementary bound, valid for `0<=r*y<1`,

```text
(1+y)^r <= exp(r*y) <= 1/(1-r*y).               (3)
```

## 4. Even cycle lengths

Let `p=2r`. Since `Q^2>2^59`,

```text
Q^p > 2^(59r).
```

Thus (2) would require

```text
A >= 59r+1.
```

For every even `p<=35000000`, we have `r<=17500000`, and exact integer arithmetic verifies

```text
r*y < 1/2.
```

Using (3),

```text
U^p = 2^(59r)*(1+y)^r
    < 2^(59r+1).
```

So the lower end of (2) demands at least `2^(59r+1)`, while the upper end is strictly smaller than that same number. No cycle is possible.

## 5. Odd cycle lengths

Let `p=2r+1`. Because `Q>2^29.5`,

```text
Q^p > 2^(59r+29.5),
```

so an integer exponent would have to satisfy

```text
A >= 59r+30.
```

For every odd `p<=35000000`, we have `r<=17499999`. Exact rational arithmetic verifies

```text
r*y < 1 - U/2^30.
```

Therefore, by (3),

```text
(1+y)^r < 2^30/U,
```

and hence

```text
U^p = 2^(59r)*U*(1+y)^r
    < 2^(59r+30).
```

Again no integer power of two can satisfy (2).

## 6. Rigorous conclusion

The candidate orbit

```text
Q=759250131, n0=1
```

has the following proved dichotomy:

1. it tends to positive infinity; or
2. it enters a nontrivial positive cycle of accelerated odd length strictly greater than `35,000,000`.

It cannot return to `1`, and every shorter nontrivial positive cycle has been excluded by exact inequalities, not by trajectory simulation.

This is not yet the final prize solution: cycles longer than `35,000,000` have not been excluded. But it reduces the remaining obstruction for one explicit pair to an extraordinarily long cycle.

The complete finite arithmetic certificate is checked by

```text
python tools/verify_strong_candidate.py
```

and by `tests/test_strong_candidate.py`.