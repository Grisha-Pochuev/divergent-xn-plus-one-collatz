# Augmented finite-path no-go theorem

Consider the fixed multiplier

```text
X = 104350542602662257699
```

with

```text
M = 15099,
H = ord_M(2) = 2154.
```

The earlier no-go theorem showed that the directed graph on the `2154` residue labels is complete. This note strengthens that conclusion: retaining the exact valuation, including its layer

```text
q = (a-t)/H,
a=t+qH,
```

does not create forbidden finite transition words either.

## 1. Compatible augmented paths

Let

```text
s_0 in {1,...,H}
```

be an arbitrary initial residue-class label, and let

```text
a_0,...,a_(L-1)
```

be an arbitrary finite word of positive exact valuations.

Define the later residue labels by the only necessary compatibility rule

```text
s_(i+1) = ((a_i-1) mod H)+1.
```

Thus the augmented path records both the exact outgoing valuation and the residue class of every visited value.

## 2. Exact realization

The finite valuation-word coding theorem gives one odd residue class

```text
n_0 == c (mod 2^(A+1)),
A = a_0+...+a_(L-1),
```

such that every positive representative follows exactly the prescribed valuation word.

Independently impose the initial odd residue class

```text
n_0 == R_(s_0) (mod 2M),
```

where `R_s` is the odd lift of `2^(-s) modulo M`.

The two moduli have gcd `2`, and both prescribed residues are odd. Therefore the generalized Chinese remainder theorem gives infinitely many positive simultaneous solutions.

For every such start, the exact valuation at step `i` is `a_i`; hence the next output class is

```text
2^(-a_i) == 2^(-s_(i+1)) (mod M).
```

The entire augmented finite path is therefore realized exactly.

## 3. Consequence

No local finite-state search can obtain a forbidden finite word merely by retaining:

- the `2154` residue label;
- the exact valuation `a`;
- the layer `q=(a-t)/H`;
- any bounded finite window of those labels.

Every formally compatible finite word occurs on infinitely many positive integer trajectories.

The unresolved obstruction is global. A useful Priority 1 certificate must use at least one condition that finite word coding does not preserve automatically:

1. closure back to the same integer;
2. equality of incoming and outgoing class counts around a cycle;
3. a global height or descent inequality;
4. the exact cycle product identity;
5. a bound coupling a large valuation spike to the surrounding values.

This theorem does not say that every finite word closes into a cycle. It says precisely that local forbidden-word enumeration, even after adding finitely many exact valuation layers, cannot be the missing proof.