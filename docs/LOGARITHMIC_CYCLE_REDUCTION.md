# Logarithmic reduction for hypothetical positive cycles

Consider the accelerated map

```text
C_X(n) = (X*n+1)/2^v2(X*n+1)
```

on positive odd integers, with fixed odd `X>=5`.

This note gives a global reduction for any hypothetical positive cycle. It does not solve the prize by itself, but it turns the unrestricted height of a cycle into an effective polynomial ceiling in its length.

## 1. Exact cycle identity

Let

```text
n_0, n_1, ..., n_(p-1)
```

be a positive cycle of accelerated odd length `p`, and write

```text
a_i = v2(X*n_i+1),
A   = a_0+...+a_(p-1),
m   = min_i n_i.
```

Multiplying the `p` cycle equations gives

```text
2^A = product_i (X + 1/n_i).
```

Hence

```text
Lambda := A*log(2)-p*log(X)
        = sum_i log(1+1/(X*n_i)).
```

In particular,

```text
0 < Lambda <= p/(X*m).                         (1)
```

The strict positivity follows because every factor `X+1/n_i` is larger than `X`.

Also

```text
A*log(2) <= p*log(X+1),
```

so `A=O_X(p)`.

## 2. Effective polynomial ceiling for the minimum

Because `X` is odd and larger than `1`, the algebraic numbers `2` and `X` are multiplicatively independent. Therefore the standard effective lower bounds for a nonzero linear form in two logarithms imply the existence of effectively computable constants

```text
c_X > 0,
C_X > 0,
```

such that, for all positive integers `p,A`,

```text
|A*log(2)-p*log(X)| >= c_X * p^(-C_X),         (2)
```

where the fact that `A=O_X(p)` absorbs `A` into the same power of `p`.

Combining (1) and (2) yields

```text
m <= (1/(X*c_X)) * p^(C_X+1).                  (3)
```

Thus:

**Theorem.** For every fixed odd `X>=5`, there are effectively computable constants `K_X,D_X>0` such that every positive accelerated `Xn+1` cycle of odd length `p` contains an element at most

```text
K_X * p^D_X.
```

This is a qualitative-effective theorem. To turn it into a numerical certificate for a chosen `X`, one must insert an explicit two-logarithm bound and calculate the resulting constants.

## 3. Irrationality-measure form

The same argument can be stated more flexibly. Put

```text
alpha = log_2(X).
```

Suppose an explicit irrationality estimate is available:

```text
|alpha-A/p| >= c / p^mu
```

for all relevant `p,A`. Then

```text
Lambda = p*log(2)*|A/p-alpha|
       >= c*log(2)*p^(1-mu).
```

Together with (1), this gives the sharper explicit ceiling

```text
m <= p^mu / (X*c*log(2)).                       (4)
```

This formulation connects directly to continued-fraction and two-logarithm computations.

## 4. Why this matters for the fixed ultra candidate

For the current fixed candidate

```text
X = 104350542602662257699,
n0 = 1,
```

all nontrivial cycles up to accelerated length

```text
10^37
```

are already excluded, and every possible nontrivial cycle element is at least `25`.

The present theorem says that any longer exceptional cycle cannot simultaneously have arbitrary length and arbitrary height: its minimum is bounded above by an effective polynomial in its length.

This identifies a concrete global completion route:

1. compute a practical explicit irrationality measure for `log_2(X)`;
2. obtain a numerical polynomial ceiling `m<=H_X(p)`;
3. combine it with a modular or descent argument excluding all possible cycle minima below `H_X(p)`.

The current residue bound `m>=25` is constant and therefore not enough by itself. A successful completion needs a lower bound on the minimum that grows faster than the polynomial ceiling, or a direct modular exclusion of every admissible minimum.

## 5. Status

This result is a rigorous global reduction, not a proof of divergence. It explains exactly what kind of new ingredient can turn the existing enormous finite cycle barrier into a proof for all cycle lengths.

Related literature includes standard Baker--Wuestholz/Matveev lower bounds for linear forms in logarithms and earlier use of such estimates in generalized Collatz cycle bounds.
