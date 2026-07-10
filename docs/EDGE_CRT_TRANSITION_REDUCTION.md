# CRT edge reduction for the 2154 residue classes

Fix

```text
X = 104350542602662257699,
M = 15099,
H = ord_M(2) = 2154.
```

This note strengthens the transition-balanced reduction by retaining the source
and target labels of each individual edge of a hypothetical positive cycle.

## 1. Edge labels

For a cycle element `n`, let

```text
sigma(n)=s
```

mean

```text
n == 2^(-s) (mod M),   1<=s<=H.
```

Let

```text
a(n)=v2(X*n+1),
theta(n)=((a(n)-1) mod H)+1=t.
```

Then the successor of `n` has source label `t`.

Choose `r_s` to be the unique odd residue modulo `2M` reducing to
`2^(-s) modulo M`. Every edge from source class `s` to target class `t`
satisfies

```text
n == r_s             (mod 2M),
n == -X^(-1)         (mod 2^t).                    (1)
```

The second congruence is necessary because `a(n)>=t`.

## 2. One progression per directed edge

Both residues in (1) are odd, so they agree modulo

```text
gcd(2M,2^t)=2.
```

The generalized Chinese remainder theorem therefore gives exactly one
solution class modulo

```text
lcm(2M,2^t)=M*2^t.                                  (2)
```

Let `mu_(s,t)` be its least positive representative. Thus every cycle element
whose transition label is `s -> t` belongs to

```text
mu_(s,t), mu_(s,t)+M*2^t, mu_(s,t)+2*M*2^t, ... .   (3)
```

If the least representative is the literal value `1`, it is forbidden for the
fixed orbit and must be replaced by the next member of (3).

This is a necessary superset, not an assertion that every member has exact
valuation congruent to `t modulo H`. That distinction keeps the reduction
rigorous.

## 3. Balanced transition matrix

Let `d_(s,t)` count cycle edges from class `s` to class `t`. A directed cycle
has

```text
sum_t d_(s,t) = c_s,
sum_s d_(s,t) = c_t,
sum_(s,t) d_(s,t) = p,                              (4)
```

where `c_s` is the number of cycle elements in class `s`. Hence row sums and
column sums are the same occupancy vector. Also

```text
sum_(s,t) t*d_(s,t) <= A <= 67p-1.                 (5)
```

## 4. Edgewise reciprocal envelope

Elements assigned to one directed edge are distinct and lie in (3). If that
edge is used `d` times, its reciprocal contribution is at most

```text
E_(s,t)(0)=0,
E_(s,t)(d)=1/mu_(s,t)
            + log(1+M*2^t*(d-1)/mu_(s,t))/(M*2^t)  for d>=1.   (6)
```

Therefore every hypothetical cycle satisfies

```text
sum_i 1/n_i <= sum_(s,t) E_(s,t)(d_(s,t)),         (7)
```

subject to the exact balance constraints (4) and valuation budget (5).

Equation (7) dominates the previous target-only binary envelope because it
also retains the source residue modulo `2M`. For large `t`, the spacing grows
exponentially as `M*2^t`.

## 5. Consequence for the research route

The correct finite object is not the complete unweighted graph on 2154
vertices. It is a balanced integer circulation on its directed edges, with an
edge-dependent arithmetic progression and target cost.

The remaining numerical task is to upper-bound the concave objective (7)
without enumerating trajectories. Possible certificates include:

1. rational tangent prices for row, column, and valuation constraints;
2. aggregation of large target labels, whose edge spacings are enormous;
3. a dual potential `u_s-v_t-w*t` bounding every marginal edge gain.

This result is structural. It does not by itself exclude all cycles or prove
divergence.
