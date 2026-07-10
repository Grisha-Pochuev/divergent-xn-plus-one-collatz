# Audit of the claimed divergent-density argument for `5x+1`

Robert Tremblay, *The 3x+1 and 5x+1 Problems* (arXiv:2104.10681),
claims that more than `17.6%` of positive integers start divergent `5x+1`
trajectories.  The paper studies the proportion `F_5(k)` of residue classes
whose first `k` iterates do not fall below their starting value and reports

```text
F_5(k) -> 0.176...
```

This does not by itself prove the existence of a divergent trajectory from
an ordinary positive integer.

## 1. Finite survival sets

For every finite depth `k`, the parity/valuation pattern of the first `k`
steps is periodic in the starting integer modulo a power of two.  Therefore
the starts surviving through depth `k` form a finite union of residue
classes.  These finite statements are compatible with the exact valuation
word coding theorem in this repository.

Let

```text
S_k = {positive starts whose stopping time is greater than k}.
```

The sets are decreasing:

```text
S_(k+1) subset S_k.
```

A calculation of the density of every finite `S_k`, even with a positive
limit, is not yet a proof that

```text
intersection_k S_k
```

contains an ordinary natural number.

## 2. The missing interchange of limit and natural density

Natural density is not a probability measure with automatic continuity from
above on arbitrary decreasing sequences of subsets of the natural numbers.
The elementary example

```text
S_k = {n in N : n >= k}
```

has density `1` for every `k`, while its intersection is empty.

The extra periodicity of the finite sets does not repair the logical issue.
Nested periodic sets correspond to nested clopen subsets of the 2-adic
integers.  Compactness guarantees a 2-adic point in a compatible nested
family, but that point need not be an ordinary nonnegative integer.

Indeed, one can construct decreasing periodic sets with densities bounded
away from zero and empty intersection in `N`: enumerate the natural numbers
and remove around the `j`-th one a sufficiently small disjoint residue
cylinder of total density less than `1/2`.  The complements of the first `k`
removed cylinders are periodic, nested, have density at least `1/2`, and
their intersection contains no natural number.

## 3. Exact relation to valuation-word coding

For an infinite exact valuation word, the finite prefix conditions determine
compatible residues

```text
r_k mod 2^(A_k+1).
```

They always define one 2-adic integer.  They define an ordinary positive
start only when the least nonnegative representatives `r_k` eventually
stabilize.

A positive limiting proportion of finite survivor words can therefore
establish a large 2-adic survivor set without exhibiting a single ordinary
positive integer in it.  The stabilization step is exactly what must be
proved and is absent from the density argument.

## 4. Consequence for this project

The paper may still contain useful finite counting information, but its
reported limit cannot be used as a prize solution.  To obtain a valid
positive-integer divergent orbit one must additionally do one of the
following:

1. exhibit a fixed ordinary positive start lying in every survivor set;
2. prove that one compatible residue chain eventually stabilizes;
3. give a different invariant or cycle-exclusion proof for a fixed orbit.

Thus the claimed `17.6%` conclusion encounters the same standard-versus-
2-adic gap as arbitrary finite valuation-word and macroblock constructions.

## Reference

R. Tremblay, *The 3x+1 and 5x+1 Problems*, arXiv:2104.10681v2 (2021),
especially the definition of `F(k)` and the conclusion interpreting
`F_5(k) -> 0.176`.
