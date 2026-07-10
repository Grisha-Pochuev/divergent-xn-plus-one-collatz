# Ceiling of the present continued-fraction cycle argument

This note records why the current `10^37` cycle barrier for

```text
X = 104350542602662257699
```

cannot be extended much further merely by increasing numerical precision.

## 1. The last excluded upper convergent

The continued-fraction certificate studies

```text
beta = ln(X) / (ord_X(2) * ln(2)),
ord_X(2)=1860810887857924950.
```

The last relevant upper convergent below the proved barrier has denominator

```text
7286014786354216885839578116495624057
```

and numerator

```text
260381098613578770350.
```

Its positive logarithmic gap is still large enough to dominate the rigorous cycle-correction bound. This is the final upper convergent eliminated by the current mechanism before `10^37`.

## 2. The next upper convergent

The next upper convergent has

```text
p = 61591102310422922843464723184177907160,
A/ell = 2201087886130126749649.
```

Equivalently the candidate total-halving numerator is

```text
A = 2201087886130126749649 * 1860810887857924950.
```

Numerically, for orientation only,

```text
ell*(A/ell)*ln(2) - p*ln(X)
approximately 8.4181084302191596 * 10^(-21).
```

The repository's actual certificates use rational logarithm intervals, not this decimal.

This gap is too small to dominate the presently available harmonic upper bound for

```text
sum_i ln(1+1/(X*n_i)).
```

Therefore the existing correction estimate cannot exclude this convergent.

## 3. Legendre reduction also ends at the same scale

The Legendre step requires

```text
2*p*H(p) < ell*X*ln(2),
```

where `H(p)` is the rigorous harmonic upper bound obtained from distinct allowed output residues.

Solving the same inequality with the exact bound used by the verifier places its ceiling only slightly above `10^37` (approximately `1.02*10^37`). The next upper-convergent denominator displayed above is already far beyond that range.

Thus two independent parts of the current proof stop together:

1. the next upper convergent survives the correction comparison;
2. the general Legendre reduction no longer applies at its denominator.

## 4. Consequence

The barrier `10^37` is not an arbitrary computational checkpoint. It is close to the natural endpoint of the present continued-fraction-plus-harmonic method.

Progress on route A now requires a genuinely new ingredient, for example:

1. a sharper dynamical restriction on which small allowed cycle elements can coexist;
2. a modular obstruction aimed specifically at the next candidate pair `(p,A)`;
3. a descent argument for cycles, rather than a stronger generic logarithmic approximation bound;
4. a proof that the orbit from `1` cannot enter a cycle realizing the required correction sum.

Simply adding more terms to the logarithm series or more continued-fraction digits will not remove this obstruction.
