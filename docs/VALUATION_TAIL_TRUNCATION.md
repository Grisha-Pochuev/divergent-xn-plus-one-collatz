# Rigorous truncation of large valuation labels

Fix the main candidate

```text
X = 104350542602662257699
```

and suppose a hypothetical positive cycle has length `p` not exceeding

```text
B = 176022359338834903228.
```

For a cycle element `n`, write

```text
a = v2(X*n+1).
```

## 1. Pointwise height bound from the valuation

The exact step equation is

```text
X*n+1 = 2^a*n',
```

where `n'` is a positive odd integer.  Hence `n'>=1` and

```text
n >= (2^a-1)/X.                                  (1)
```

Therefore

```text
1/n <= X/(2^a-1).                                (2)
```

## 2. Large target labels

Write `a=t+2154*q`, with `1<=t<=2154` and `q>=0`.  Every step with either

```text
t >= T and q=0,
```

or

```text
q >= 1
```

has `a>=T`, provided `T<=2155`.  There are at most `p` cycle elements, so by (2) their total reciprocal contribution is at most

```text
p*X/(2^T-1).                                     (3)
```

For

```text
T=200,
p<=B,
```

exact integer arithmetic gives

```text
B*X/(2^200-1) < 1/10^19.                         (4)
```

Thus all elements whose exact valuation is at least `200` contribute less than `10^(-19)` in total to

```text
sum_i 1/n_i.
```

In particular this includes:

- all base-layer transitions with target label `t>=200`;
- every high-layer transition `q>=1`, since then `a>=2155`.

## 3. Finite reduction

For every cycle length through the current barrier, a transition-aware reciprocal optimization may treat all exact valuations `a>=200` as one rigorously bounded tail of size below `10^(-19)`.  The non-negligible part contains only

```text
a=t, 1<=t<=199,
```

and therefore at most

```text
2154*199 = 428646
```

oriented source-target cells before further reductions.

This turns the exact circulation formulation from an infinite-layer problem into a finite certificate problem at the retained barrier.  It is still not a proof excluding every cycle length.
