# Conjectural digital-invariant route for `X=9, n0=1`

This note records a promising but **unproved** route.  It must not be cited as a divergence proof.

## 1. Exact transformed recurrence

Let `n_t` be the accelerated odd-only orbit for

```text
X=9,
n_0=1,
```

and write

```text
a_t = v2(9*n_t+1),
A_t = a_0+...+a_(t-1),
A_0 = 0.
```

Define

```text
S_t = 2^A_t * n_t.
```

Because every `n_t` is odd,

```text
v2(S_t)=A_t.
```

Multiplying the accelerated step equation

```text
2^a_t*n_(t+1)=9*n_t+1
```

by `2^A_t` gives the exact recurrence

```text
S_(t+1)=9*S_t+2^A_t
       =9*S_t+2^v2(S_t),
S_0=1.                                             (1)
```

Thus the original orbit can be studied through one integer recurrence involving the position of the lowest set bit of `S_t`.

## 2. A sufficient invariant

Since every added term in (1) is positive,

```text
S_t >= 9^t.
```

Therefore

```text
n_t = S_t/2^A_t >= 9^t/2^A_t.                    (2)
```

It would be enough to prove, for every `t>=1`,

```text
A_t <= 3*t-1.                                     (3)
```

Indeed, (2)--(3) would give

```text
n_t >= 2*(9/8)^t -> +infinity.
```

The stronger experimentally observed inequality is

```text
A_t <= 3*t-2.                                     (4)
```

Equivalently, because `A_t=v2(S_t)`, the desired theorem is a digital bound on the number of trailing zeroes of the recursively defined integer `S_t`.

## 3. Finite exact check

The script

```text
python tools/check_x9_digital_invariant.py --steps 10000
```

checks with exact integer arithmetic that:

1. recurrence (1) agrees with the accelerated orbit;
2. `S_t=2^A_t*n_t` at every checked step;
3. inequality (4) holds for the first `10000` accelerated steps.

For that prefix the minimum value of

```text
3*t-A_t
```

is `2`, first attained at `t=1`.

This is finite evidence only.  A trajectory check, however long, cannot establish (3) or (4) for every `t`.

## 4. Exact missing lemma

A complete proof along this route would follow from:

> For the recurrence `S_0=1`, `S_(t+1)=9*S_t+2^v2(S_t)`, prove that `v2(S_t)<=3*t-1` for every `t>=1`.

A stronger and more useful version would identify a finite-state invariant of the binary expansion of

```text
S_t / 2^v2(S_t)
```

that prevents a carry chain long enough to make `v2(S_t)` reach `3t`.

## 5. Status

- The transformed recurrence and the implication from (3) to divergence are exact.
- The first `10000` steps satisfy the stronger bound (4).
- No induction or finite automaton proving the bound for all `t` is currently known.
- Therefore this is a recorded research lead, not a validated prize solution.
