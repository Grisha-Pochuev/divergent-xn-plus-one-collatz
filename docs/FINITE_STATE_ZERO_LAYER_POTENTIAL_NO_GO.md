# No-go theorem for positive finite-state zero-layer potentials

The current Priority 1 plan considered a finite quotient of zero-layer carry
states and a telescoping inequality with a fixed positive mean cost.  This note
shows that such an approach cannot work when the charged cost vanishes on the
least-label zero-layer edge.

## 1. Arbitrarily long zero-cost segments

Fix the retained odd multiplier `X`.  For every integer `L>=1`, consider the
exact valuation word

```text
1,1,...,1
```

of length `L`.

The exact valuation-word coding theorem gives one odd residue class modulo

```text
2^(L+1)
```

whose positive representatives follow this word exactly.  Independently impose

```text
n_0 == 2^(-1) (mod X).
```

Since `X` is odd, the Chinese remainder theorem combines the two conditions.
Thus infinitely many positive odd starts realize `L` consecutive transitions
with

```text
a_i=1,
q_i=0,
s_i=s_(i+1)=1.
```

Every value in the segment has full output label `1`, because modulo `X` the
step equation gives

```text
n_(i+1) == 2^(-1) (mod X).
```

Consequently both natural transition costs vanish on every edge of the segment:

```text
q_i=0,
(s_i-1)+(s_(i+1)-1)+2*O*q_i=0.                    (1)
```

These are finite orbit segments, not infinite divergent or cyclic orbits.
Their existence is nevertheless enough to obstruct a universal finite-state
mean-cost certificate.

## 2. Finite-state obstruction

Let `Sigma` be any finite set, let `sigma(n)` assign a state to every positive
odd orbit value, and let `Phi:Sigma->R` be any potential.  Suppose there were a
constant `delta>0` such that every zero-cost edge satisfied

```text
cost(edge) >= delta + Phi(sigma(next))-Phi(sigma(current)).   (2)
```

Choose the all-ones segment above with length greater than `|Sigma|`.  Two of
its projected states are equal.  Sum (2) along the nonempty subsegment between
them.  The potential telescopes and every edge cost is zero by (1), giving

```text
0 >= delta * positive_length,
```

a contradiction.

Therefore:

**Theorem.** No finite-state projection admits a universal telescoping
inequality with fixed `delta>0` for either the full-order layer cost `q` or the
symmetric incremental cost, because both costs vanish on arbitrarily long
realizable all-label-one segments.

## 3. Scope

This theorem does not rule out:

- an unbounded height-dependent potential;
- a reciprocal potential depending on the actual integer value;
- an inequality that is only asserted after a globally forced event;
- a distribution theorem for the zero-layer pair representatives;
- a potential whose accumulated gain depends on segment endpoints rather than
  a fixed positive cost per edge.

It rules out the specific proposed route of finding a positive minimum mean
layer cost on a fixed finite quotient of all zero-layer transitions.  Local
finite automata cannot supply the missing global obstruction.

Run

```text
python tools/verify_finite_state_zero_layer_no_go.py
```

for finite exact-word regression checks.
