# Permanent mod-3 predecessor sieve

Fix the retained multiplier

```text
X = 104350542602662257699,
M = 15099,
H = ord_M(2) = 2154.
```

Write `X=3Y`.  Here

```text
X == 3 (mod 9),
Y == 1 (mod 3),
6 | H.
```

This note gives a transition restriction that is stronger than merely listing
the `2154` allowed output classes modulo `2M`.

## 1. Every reached value is coprime to X

For an accelerated step

```text
2^a*n' = X*n+1,
```

any common divisor of `n'` and `X` divides both `X*n+1` and `X`, hence it
divides `1`.  Therefore every accelerated output is coprime to `X`.  The start
`n0=1` is also coprime to `X`.

Consequently a positive integer all of whose direct predecessors are divisible
by `3` cannot occur in the orbit from `1` and cannot belong to a cycle reached
by that orbit.

## 2. One third of the refined lifts are permanently dead

Let a possible output `n` have small residue label `t`, meaning

```text
n == 2^(-t) (mod M),
1 <= t <= H.
```

Its full output label `s` modulo `ord_X(2)` satisfies

```text
s == t (mod H).
```

Every direct predecessor of `n` has a valuation congruent to `s` modulo
`ord_X(2)`.  Since both `H` and `ord_X(2)` are divisible by `6`, every such
valuation `a` satisfies

```text
a == t (mod 6).
```

A direct predecessor is

```text
m = (2^a*n-1)/X.
```

Because `X=3Y` with `3` not dividing `Y`,

```text
3 | m
```

is equivalent to

```text
2^a*n == 1 (mod 9).
```

Using `a==t (mod 6)` and `ord_9(2)=6`, this is equivalent to the finite test

```text
2^t*n == 1 (mod 9).                              (1)
```

Thus condition (1) is independent of which full-order lift of the incoming
valuation is used.  If it holds, every direct predecessor is divisible by `3`.
Such an `n` is permanently unreachable from the fixed orbit.

For each allowed odd class modulo `2M`, its three lifts modulo

```text
lcm(2M,9) = 6M = 90594
```

have three different compatible residues modulo `9`.  Exactly one of the three
satisfies (1).  Therefore the refined transition sieve contains

```text
2154 dead classes,
4308 surviving classes
```

modulo `6M`: exactly one third of the formerly allowed lifts are removed.

## 3. A two-state flow balance

For a surviving value define

```text
r = n mod 3,
b = ((2^t*n-1)/3)*Y^(-1) mod 3.
```

Then `r,b` both lie in `{1,2}`, and every predecessor of `n` has residue `b`
modulo `3`.  Hence every surviving refined class is an oriented edge

```text
b -> r
```

in a two-state graph.

A closed cycle has equal indegree and outdegree at each state.  In particular,
if `N_12` and `N_21` are the numbers of cycle elements of edge types `1->2`
and `2->1`, then necessarily

```text
N_12 = N_21.                                     (2)
```

The exact enumeration modulo `6M` contains `1077` refined classes of each of
the six possible types before deletion; after deleting predecessor residue
`0`, it contains `1077` classes of each surviving type

```text
1->1, 1->2, 2->1, 2->2.
```

## 4. Scope

This is a genuine global reachability and transition restriction.  It does not
contradict the theorem that arbitrary finite valuation words are locally
realizable: a locally generated start need not itself be an accelerated output
coprime to `X`.

The sieve alone does not exclude the final two sparse-window lengths.  Its role
is to remove one third of the candidate representatives before reciprocal and
activation-price optimization, while (2) supplies an additional flow-balance
constraint.

Run

```text
python tools/verify_permanent_predecessor_mod3_sieve.py
```

for the exact certificate.
