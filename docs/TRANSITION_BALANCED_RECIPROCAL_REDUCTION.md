# Transition-balanced reciprocal reduction

Consider the fixed multiplier

```text
X = 104350542602662257699
```

with

```text
M = 15099,
H = ord_M(2) = 2154.
```

This note gives a strict transition-aware reduction for the reciprocal sum in a hypothetical positive cycle. It combines the residue class of each cycle element with the binary condition determining the class of its successor.

## 1. Source and target class labels

For every allowed cycle element `n`, define its source-class label

```text
sigma(n) in {1,...,H}
```

by

```text
n == 2^(-sigma(n)) (mod M).
```

For the outgoing step from `n`, put

```text
a(n) = v2(X*n+1),
theta(n) = ((a(n)-1) mod H)+1.
```

Then the accelerated successor satisfies

```text
C_X(n) == 2^(-a(n)) == 2^(-theta(n)) (mod M),
```

so

```text
sigma(C_X(n)) = theta(n).                     (1)
```

## 2. Exact flow balance in a cycle

Let `S` be the set of elements of a positive cycle of length `p`. The elements are distinct. For each class `t`, define

```text
c_t = #{n in S : sigma(n)=t}.
```

Because the successor map permutes the cycle and (1) holds,

```text
c_t = #{n in S : theta(n)=t}.                 (2)
```

Thus the source-class occupancy vector is exactly the outgoing-target occupancy vector. In particular,

```text
sum_t c_t = p.
```

The global valuation budget gives the additional necessary condition

```text
sum_t t*c_t <= 67p-1.                         (3)
```

Equations (2)-(3) are the finite balance constraints missing from the independent-class envelope.

## 3. Source-class reciprocal envelope

Let `rho_t` be the least positive admissible element of source class `t` modulo `2M`. For the class containing the literal value `1`, use the next representative because the fixed orbit cannot return to `1`.

The distinct positive elements of source class `t` are contained in

```text
rho_t, rho_t+2M, rho_t+4M, ...
```

Hence, if the cycle uses the class `c_t` times, its source-class contribution is at most

```text
R_t(c_t) = 0                                           if c_t=0,
R_t(c_t) = 1/rho_t
           + log(1+2M*(c_t-1)/rho_t)/(2M)             if c_t>=1.
```

Therefore, for

```text
S_recip = sum_(n in S) 1/n,
```

we have

```text
S_recip <= sum_t R_t(c_t).                     (4)
```

This is the class-count version of residue crowding.

## 4. Outgoing-target binary envelope

If `theta(n)=t`, then `a(n)>=t`. Consequently

```text
2^t divides X*n+1,
```

and therefore

```text
n == -X^(-1) (mod 2^t).                        (5)
```

Let `eta_t` be the least integer at least `25` satisfying (5). The lower cutoff `25` is valid for every nontrivial cycle reachable by the fixed orbit.

All cycle elements with outgoing-target label `t` lie in the progression

```text
eta_t, eta_t+2^t, eta_t+2*2^t, ...
```

so their reciprocal contribution is at most

```text
B_t(c_t) = 0                                           if c_t=0,
B_t(c_t) = 1/eta_t
           + log(1+2^t*(c_t-1)/eta_t)/2^t             if c_t>=1.
```

Using the exact balance (2), the same counts `c_t` occur here. Thus

```text
S_recip <= sum_t B_t(c_t).                     (6)
```

## 5. Safe combined bound

Both (4) and (6) bound the same reciprocal sum. Therefore, for every real `lambda` with `0<=lambda<=1`,

```text
S_recip
 <= lambda*sum_t R_t(c_t)
    +(1-lambda)*sum_t B_t(c_t),                (7)
```

subject to

```text
c_t are nonnegative integers,
sum_t c_t = p,
sum_t t*c_t <= 67p-1.
```

For fixed `lambda`, the right-hand side is a finite separable concave resource-allocation problem in only `2154` count variables. It contains no trajectory search and no assumption of random valuation frequencies.

## 6. Why this is stronger than the old abstraction

The previous envelope treated the `2154` source progressions independently and allowed each one its own worst-case population. The transition-balanced reduction forces the same occupancy vector to satisfy two incompatible-looking descriptions:

1. modulo `2M`, according to the class of the current element;
2. modulo `2^t`, according to the exact binary divisibility needed to enter class `t` next.

The local class graph is complete, but a closed cycle must be globally balanced. This is the first retained reduction that uses that closure condition directly.

## 7. Remaining finite task

To turn (7) into a stronger numerical cycle barrier:

1. choose a rational `lambda`;
2. maximize the concave envelope under the two linear constraints;
3. certify the maximum using rational tangent bounds and the same exact logarithm inequalities used by the residue-crowding verifier;
4. substitute the resulting reciprocal bound into the even- and odd-length power-of-two interval inequalities.

This note is a reduction, not yet a completed improved barrier and not a proof that all cycles are impossible.
