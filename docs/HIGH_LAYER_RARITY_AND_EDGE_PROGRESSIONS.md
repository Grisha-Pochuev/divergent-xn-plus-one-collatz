# High-layer rarity and exact transition progressions

Fix

```text
X = 104350542602662257699,
M = 15099,
H = 2154.
```

Consider a hypothetical positive accelerated cycle of length `p`.  For every cycle step, write the exact valuation as

```text
a_i = t_i + H*q_i,
1 <= t_i <= H,
q_i >= 0.
```

Let `Q=sum_i q_i` and let `N_high=#{i:q_i>=1}`.

## 1. Exact layer decomposition of the total valuation

If `c_t` is the number of targets having class label `t`, then

```text
A = sum_i a_i
  = sum_(t=1)^H t*c_t + H*Q.                    (1)
```

The cycle identity gives

```text
2^A = product_i (X+1/n_i).
```

Since every `n_i>=1` and `X+1<2^67`,

```text
A <= 67p-1.                                     (2)
```

Combining (1)-(2),

```text
Q <= floor((67p-1-sum_t t*c_t)/H).              (3)
```

Since `sum_t t*c_t>=p`,

```text
Q <= floor((66p-1)/2154).                       (4)
```

Every high-layer step contributes at least one to `Q`, hence

```text
N_high <= Q <= floor((66p-1)/2154).             (5)
```

Thus fewer than `66/2154 = 11/359`, approximately `3.0641%`, of the cycle steps can have `q_i>=1`.

This is a strict global restriction.  It does not contradict finite-word realizability because the latter does not impose cycle closure.

## 2. Exact progression for one oriented transition

Let a cycle element `n` have source class `s`, so

```text
n == 2^(-s) (mod M).
```

Suppose its outgoing exact valuation is

```text
a=t+H*q.
```

Exactness means

```text
X*n+1 == 2^a (mod 2^(a+1)),
```

or equivalently

```text
n == (2^a-1)*X^(-1) (mod 2^(a+1)).              (6)
```

Because `M` is odd, the congruence modulo `M` and (6) combine uniquely by the Chinese remainder theorem.  Therefore every element producing the oriented transition

```text
source s -> target t at layer q
```

lies in one arithmetic progression modulo

```text
M*2^(a+1) = M*2^(t+H*q+1).                      (7)
```

For `q>=1` the spacing contains the enormous factor `2^2154`; by (5), such transitions are also globally rare.

## 3. Exact circulation variables

Define

```text
d_(s,t,q)
```

as the number of cycle elements with source class `s` and outgoing valuation `t+H*q`.  Then

```text
sum_(t,q) d_(s,t,q) = c_s,                      (8)
sum_(s,q) d_(s,t,q) = c_t,                      (9)
sum_(s,t,q) d_(s,t,q) = p,                      (10)
sum_(s,t,q) (t+H*q)d_(s,t,q) = A <= 67p-1.     (11)
```

Equations (8)-(9) say that `d` is an integer circulation.  Each nonzero cell is supported on its own exact progression (7).

## Significance

The correct transition-aware optimization is therefore not merely an occupancy problem in `2154` variables.  It is an integer circulation problem over oriented class pairs, with exact progression spacing depending exponentially on the target label and layer.  Local paths remain unrestricted, but closed cycles must satisfy (8)-(11).
