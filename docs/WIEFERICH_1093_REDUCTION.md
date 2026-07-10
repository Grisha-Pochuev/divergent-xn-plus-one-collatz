# The Wieferich candidate `(X,n0)=(1093,1)`

This note gives a second rigorous attack on the prize problem, independent of the `X=2^m+1` macroblock construction.

For odd positive `n`, write

```text
C_q(n) = (q*n+1)/2^v2(q*n+1).
```

We use

```text
q = 1093.
```

The multiplicative order of `2` modulo `1093` is

```text
ell = 364,
```

and the Wieferich congruence is

```text
2^364 == 1  (mod 1093^2).                       (1)
```

Both statements are checked independently by `tools/verify_wieferich_1093.py`.

## 1. Every direct predecessor of 1 is divisible by 1093

Suppose

```text
C_q(m)=1.
```

Then

```text
q*m+1 = 2^a
```

for some positive integer `a`. Reducing modulo `q` gives

```text
2^a == 1 (mod q).
```

Because `ell=ord_q(2)=364`, we have `a=ell*k` for some `k>=1`.

Congruence (1) implies

```text
2^(ell*k) == 1 (mod q^2),
```

so

```text
m = (2^(ell*k)-1)/q
```

is divisible by `q`.

Therefore every positive odd integer that maps directly to `1` is a multiple of `1093`.

## 2. No output of the accelerated map is divisible by 1093

For every positive odd `x`,

```text
q*x+1 == 1 (mod q).
```

Division by a power of two cannot introduce a factor `q`, because `q` is odd. Hence

```text
gcd(C_q(x),q)=1.                                 (2)
```

Combining the two sections, no value produced by the map can be a direct predecessor of `1`.

## 3. The orbit from 1 never returns to 1

The first accelerated step is

```text
C_1093(1) = 1094/2 = 547 != 1.
```

If the orbit later reached `1`, the value immediately before `1` would be a direct predecessor of `1`. That predecessor would be divisible by `1093` by Section 1, but it would also be an output of the map and therefore coprime to `1093` by Section 2. This is impossible.

Thus

```text
C_1093^t(1) != 1    for every t>=1.              (3)
```

This is a fully rigorous specialization of the strong-Crandall/Wieferich mechanism of Franco and Pomerance.

## 4. Exact remaining obstruction

By the positive integer orbit dichotomy proved in `INTEGER_ORBIT_DICHOTOMY.md`, the orbit of `1` under `C_1093` has only two possibilities:

1. it eventually enters a nontrivial positive cycle not containing `1`;
2. it tends to positive infinity.

Statement (3) eliminates the trivial `1`-cycle completely. Consequently:

> To solve the prize with `(X,n0)=(1093,1)`, it is now enough to prove that this one orbit does not enter a nontrivial positive cycle.

This reduction is stronger than merely observing a long growing trajectory: one entire possible terminal behavior, arrival at `1`, has been excluded for all time.

## Reference

Z. Franco and C. Pomerance, *On a Conjecture of Crandall Concerning the qx+1 Problem*, Mathematics of Computation 64 (1995), 1333-1336.