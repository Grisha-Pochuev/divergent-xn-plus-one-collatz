# Global valuation budget for the 2154 residue classes

Consider the fixed multiplier

```text
X = 104350542602662257699
```

and

```text
M = 15099,
H = ord_M(2) = 2154.
```

The unaugmented transition graph on the `2154` output classes is complete, so local forbidden edges do not exist. Nevertheless, a hypothetical cycle cannot use the classes with arbitrary frequencies: every class carries a minimum exact-valuation cost, and the total valuation around a cycle has a strict global budget.

## 1. Class cost

For every allowed odd class modulo `2M`, define its index

```text
tau(n) in {1,...,H}
```

by

```text
n == 2^(-tau(n)) (mod M).
```

This is well defined because `ord_M(2)=H`.

For an accelerated step

```text
n_(i+1) = (X*n_i+1)/2^a_i,
a_i = v2(X*n_i+1),
```

we have

```text
n_(i+1) == 2^(-a_i) (mod M).
```

Therefore

```text
a_i = tau(n_(i+1)) + H*q_i
```

for some integer `q_i>=0`. In particular,

```text
a_i >= tau(n_(i+1)).
```

Thus visiting a class of index `t` consumes at least `t` units of the total halving count on the incoming edge.

## 2. Total valuation budget in a cycle

Let

```text
n_0,...,n_(p-1)
```

be a positive accelerated cycle and let

```text
A = sum_i a_i.
```

The exact cycle identity is

```text
2^A = product_i (X + 1/n_i).
```

Since every `n_i>=1` and

```text
X+1 < 2^67,
```

we obtain

```text
2^A < 2^(67p).
```

Hence, because `A` is an integer,

```text
A <= 67p-1.
```

Summing the class costs around the cycle and cyclically relabelling the terms gives the strict global restriction

```text
sum_i tau(n_i) <= A <= 67p-1.                 (1)
```

## 3. Frequency consequences

For any threshold `T` with `1<=T<=H`, let `N_T` be the number of cycle elements whose class index is at least `T`. From (1),

```text
T*N_T <= sum_i tau(n_i) <= 67p-1,
```

so

```text
N_T <= floor((67p-1)/T).                      (2)
```

Examples:

```text
index >= 68   can occur at most floor((67p-1)/68) times;
index >= 134  can occur at most floor((67p-1)/134) times;
index >= 2154 can occur at most floor((67p-1)/2154) times.
```

The last class is the residue class `1 modulo M`; it can therefore occupy at most about `3.11%` of a cycle, independently of the exclusion of the literal value `1`.

More generally, if `c_t` denotes the number of cycle elements in class `t`, then every hypothetical cycle must satisfy

```text
sum_(t=1)^H c_t = p,
sum_(t=1)^H t*c_t <= 67p-1.                   (3)
```

These constraints were absent from the independent-class reciprocal envelope.

## 4. Significance for the reciprocal bound

The current residue-crowding proof bounds each class independently. Constraint (3) supplies a finite global coupling between the class occupancies. It rules out the artificial worst case in which all `2154` progressions are populated at their independent maximum without paying for their valuation indices.

A stronger reciprocal certificate should maximize

```text
sum_(t=1)^H sum_(j=0)^(c_t-1) 1/(rho_t+2M*j)
```

subject to (3), where `rho_t` is the least admissible positive representative of class `t` (with the literal value `1` removed for the fixed orbit).

This is a finite concave resource-allocation problem. It uses genuine transition information: class `t` is the output of an edge whose exact valuation is congruent to `t` modulo `H` and is therefore at least `t`.

## 5. What this does and does not prove

This result is strict and global, but it does not yet exclude all cycles. It provides the missing occupancy constraint needed to replace the current independent-class reciprocal envelope by a transition-aware one.

It does not use the retracted condition `ord_X(2)|A`; the exact relation between each incoming valuation and its output class is retained throughout.
