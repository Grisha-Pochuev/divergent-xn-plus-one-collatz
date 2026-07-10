# Completeness of the 2154-class transition graph

Consider the fixed multiplier

```text
X = 104350542602662257699
```

and the divisor

```text
M = 15099,
H = ord_M(2) = 2154.
```

This note records a strict negative result about the current Priority 1 state space: the `2154` allowed odd residue classes modulo `2M` do not forbid any one-step transition or any finite class word.

## 1. Allowed classes

For `1 <= a <= H`, let `R_a` be the unique odd residue class modulo `2M` whose reduction modulo `M` is

```text
2^(-a) (mod M).
```

Because `ord_M(2)=H`, these are exactly the `H=2154` allowed output classes.

For every accelerated step

```text
n' = (X*n+1)/2^a,
a = v2(X*n+1),
```

we have, since `M|X`,

```text
n' == 2^(-a) (mod M).
```

Thus the class of the output is `R_(a mod H)`.

## 2. Every one-step class transition is realizable

Fix any source class `R_s` and any target class `R_t`.
Choose the exact valuation

```text
a=t,
```

where indices are taken in `{1,...,H}`.

The exact condition `v2(X*n+1)=a` is equivalent to one odd residue class modulo `2^(a+1)`:

```text
n == X^(-1)*(2^a-1) (mod 2^(a+1)).
```

The source-class condition is one odd residue class modulo `2M`:

```text
n == R_s (mod 2M).
```

The two moduli have greatest common divisor `2`, and both prescribed residues are odd. Hence the two congruences are compatible. By the generalized Chinese remainder theorem they have infinitely many positive solutions.

For each such solution, the exact valuation is `a=t`, so the output lies in `R_t`.

Therefore the directed graph on the `2154` classes is the complete directed graph, including loops.

## 3. Every finite class word is realizable

Let

```text
R_(s_0), R_(s_1), ..., R_(s_L)
```

be an arbitrary finite word of allowed classes.
For each `0<=i<L`, choose the exact valuation

```text
a_i=s_(i+1),
```

again using representatives in `{1,...,H}`.

The exact finite valuation-word coding theorem gives one odd residue class

```text
n_0 == c (mod 2^(A+1)),
A = a_0+...+a_(L-1),
```

whose positive representatives follow the exact valuation word

```text
a_0,...,a_(L-1).
```

Impose in addition

```text
n_0 == R_(s_0) (mod 2M).
```

As before, the two congruences are compatible because both residues are odd and the gcd of the moduli is `2`. Thus infinitely many positive starts realize the entire prescribed class word.

## 4. Consequence for Priority 1

No theorem of the following forms can be obtained from the `2154` class labels alone:

- a forbidden one-step transition;
- a forbidden finite transition word;
- a proper subgraph containing every positive orbit.

The current class abstraction forgets precisely the binary information that determines the next valuation. Since the odd modulus `M` is coprime to every power of two, that missing binary information can always be supplied independently by the Chinese remainder theorem.

A useful refinement must therefore retain at least one of:

1. the exact valuation `a`, not only `a mod H`;
2. a binary residue of the source sufficient to constrain `v2(X*n+1)`;
3. a height/layer variable, because large representatives `a=t+qH` force large source values;
4. a global cycle-closure or flow-balance condition that is not local to a finite class word.

This result does not weaken the existing residue-crowding barrier. It proves that the proposed search for impossible short words in the unaugmented `2154`-class graph cannot succeed, and it identifies the additional information required for a stronger transition certificate.
