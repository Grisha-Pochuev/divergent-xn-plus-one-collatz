# Same-deficit complete blocks have arbitrary finite local persistence

Date: 2026-07-14

## Scope

Let

```text
B=2^m,
d positive odd,
X=B-d>=5,
```

with `m>=3`. An ordinary complete block of length `ell>=1` and terminal
`deficit e` has valuation word

```text
(m,m,...,m,m-e),
1<=e<=m-1,
```

with `ell-1` copies of `m`.

The current nonpositive-return theorem forces one ordinary deficit type to occur
doubly exponentially many times in a hypothetical cycle. This note determines
what can and cannot follow from that repetition by local block arithmetic alone.

## Theorem: arbitrary finite same-deficit persistence

Fix `e` with `1<=e<=m-1`. Let

```text
ell_0,ell_1,...,ell_L
```

be any finite list of positive complete-block lengths. There are infinitely many
positive odd exact orbit segments with consecutive complete-block boundaries

```text
y -> x_0 -> x_1 -> ... -> x_L
```

such that block `j` has length `ell_j` and terminal deficit `e`.
Every retained boundary satisfies the same exact class

```text
d*x_j==2^e (mod X),   0<=j<=L.                         (1)
```

The segment can be chosen above any fixed finite height bound.

Thus neither the number of occurrences of one ordinary deficit type, nor the
exact intervening complete-block lengths in any fixed finite window, has a
universal local upper bound.

## Proof

Concatenate the exact valuation words

```text
W_j=(m,...,m,m-e)
```

for the prescribed lengths `ell_j`. Exact valuation-word coding gives one odd
source class

```text
y==r_W (mod 2^(A_W+1))                                (2)
```

whose positive representatives realize the entire concatenated word exactly.
There are infinitely many such positive representatives, and taking a large
representative puts every state above any prescribed finite bound.

It remains to prove the common boundary class. For one complete block from
source `u` to endpoint `v`, the exact complete-block identity is

```text
2^(m*ell-e)*v=X^ell*u+S_ell,
S_ell=(B^ell-X^ell)/d.                                  (3)
```

Modulo `X`,

```text
S_ell==B^(ell-1) (mod X).
```

Since `B` and `2` are invertible modulo the odd number `X`, reducing (3) modulo
`X` gives

```text
B^ell*2^(-e)*v==B^(ell-1) (mod X),
B*v==2^e (mod X).
```

Finally `B==d (mod X)`, proving (1) for every endpoint. The prepended block
`y -> x_0` makes the first retained boundary `x_0` an endpoint of the same type,
so all `x_0,...,x_L` lie in the common class.

## Primary-candidate N-adic corollary

For the retained candidate

```text
m=4501,
N=2^500-1,
d=349*2^500-347,
X=2^4501-d,
```

we have

```text
N|X,
d==2 (mod N).
```

Therefore every boundary in (1) also satisfies

```text
x_j==2^(e-1) (mod N).                                  (4)
```

More strongly, for a block of length `ell` and every `1<=s<=ell`, equation (3)
reduces modulo `N^s` to

```text
x_j==2^(-(m*ell-e))*S_ell (mod N^s),                   (5)
```

because `N^ell|X^ell`. Hence a long complete block fixes a deep `N`-adic
endpoint class independently of its source.

The theorem shows that every *finite* depth obtained this way is nevertheless
compatible with an exact positive same-deficit block segment. Finite `N`-adic
depth plus finite same-type repetition is therefore not by itself a cycle
obstruction.

## Explicit 5n+1 regression

Take

```text
B=8,
X=5,
d=3,
e=2,
lengths after the prepended block=(2,4,3,1).
```

An exact source is

```text
47150705.
```

The exact valuation word is

```text
(1,3,1,3,3,3,1,3,3,1,1),
```

and the same-deficit boundaries are

```text
117876763,
184182443,
112416043,
109781293,
274453233.
```

All five are congruent to `3` modulo `5`, equivalently

```text
3*x==2^2 (mod 5).
```

The boundaries need not be monotone; the theorem concerns exact local
realizability, not divergence.

## Exact no-go conclusion

The following proof architecture is closed:

```text
one ordinary deficit type occurs extremely many times;
all of its boundaries lie in d*n==2^e (mod X);
inspect only finitely many exact blocks or finitely much N-adic depth;
conclude that so many occurrences are impossible.
```

Arbitrarily long finite counterexamples to that local conclusion exist for every
choice of the common deficit and every prescribed finite list of block lengths.

A successful use of the doubly exponential repetition must retain genuinely
global information, for example:

1. the exact cyclic source-matching divisibility;
2. the minimum-boundary exit/return inequalities;
3. a harmonic or height contribution forced specifically by the repeated type;
4. an interaction with exceptional blocks that cannot be reproduced inside an
   arbitrary finite exact word.

This theorem does not exclude a cycle and does not prove divergence. It narrows
the next target: the repeated population must be converted into a global
cycle-closing correction, not another finite local congruence ladder.

## Verification

Run

```text
python tools/verify_same_deficit_finite_persistence.py
```

The checker verifies `3705` small exact constructions, an explicit `5n+1`
regression, and four primary-candidate regressions including the deep congruence
(5).
