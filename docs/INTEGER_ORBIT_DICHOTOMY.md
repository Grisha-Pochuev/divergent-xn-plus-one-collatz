# Positive integer orbit dichotomy

Let `T` be any deterministic map from the positive integers to the positive integers, and let

```text
n_(t+1) = T(n_t).
```

This elementary observation is useful for the generalized Collatz prize because it removes a possible third type of behavior.

## Theorem

Every positive integer orbit satisfies exactly one of the following alternatives:

1. it is eventually periodic;
2. it tends to positive infinity.

Equivalently, if a positive integer orbit is not eventually periodic, then

```text
n_t -> +infinity.
```

## Proof

Assume that the orbit does not tend to positive infinity. Then there is a finite bound `B` such that

```text
n_t <= B
```

for infinitely many values of `t`.

Only the `B` positive integers

```text
1,2,...,B
```

can occur at those times. Hence one value occurs at least twice: there are indices `r<s` with

```text
n_r = n_s.
```

The map is deterministic, so equality propagates forward:

```text
n_(r+j) = n_(s+j)
```

for every `j>=0`. Thus the orbit is periodic from time `r` onward.

The converse is immediate: an eventually periodic positive orbit is bounded and cannot tend to infinity. QED.

## Consequence for the prize problem

For the accelerated map

```text
C_X(n) = (X*n+1)/2^v2(X*n+1),
```

one does not need a separate proof of monotone growth. It is enough to prove that one explicit positive orbit never becomes periodic.

A particularly useful form is:

> If an orbit is proved to avoid every positive cycle, then it automatically tends to positive infinity.

This reduction is applied to the candidate `(X,n0)=(1093,1)` in `WIEFERICH_1093_REDUCTION.md`.