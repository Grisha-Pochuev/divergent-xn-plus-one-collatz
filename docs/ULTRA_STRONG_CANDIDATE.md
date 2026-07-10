# Ultra-strong fixed candidate

Consider the explicit pair

```text
X  = 104350542602662257699,
n0 = 1.
```

This note proves that its accelerated orbit either tends to positive infinity or enters a nontrivial positive cycle longer than

```text
120,000,000,000,000,000,000
```

accelerated odd steps.

It is still a finite obstruction, not yet a complete proof of divergence.

## 1. Arithmetic structure and permanent avoidance of 1

The multiplier has the form

```text
X = 21*t,
t = 4969073457269631319,
t == 1 (mod 6).
```

Thus `3` divides `X` exactly once and `7` divides `X`.

Let `ell=ord_X(2)`. Because `ord_3(2)=2` and `ord_7(2)=3`, the number `ell` is divisible by `6`. The lifting-the-exponent lemma gives

```text
v3(2^ell-1) >= 2,
```

whereas `v3(X)=1`. Hence

```text
gcd(X,(2^ell-1)/X) >= 3.
```

As in the Wieferich reduction, every direct predecessor of `1` shares a factor with `X`, but every accelerated output is coprime to `X`. The first step is

```text
C_X(1) = 26087635650665564425 != 1.
```

Therefore the orbit from `1` can never return to `1`.

## 2. Every possible nontrivial cycle element is at least 11

For every accelerated step with halving count `a`,

```text
2^a*C_X(n) == 1  (mod X).
```

Since `21|X`, every output satisfies

```text
C_X(n) == 2^(-a)  (mod 21).
```

The six inverse-power residues modulo `21` are

```text
1, 11, 16, 8, 4, 2.
```

An output is odd. Combining each residue with oddness, the least possible positive representatives are respectively

```text
1, 11, 37, 29, 25, 23.
```

The orbit never returns to `1`. Hence every element of any nontrivial cycle reached by this orbit satisfies

```text
n_i >= 11.                                       (1)
```

## 3. Exceptional approximation to a half power of two

The multiplier is the least integer above `2^66*sqrt(2)`:

```text
floor(2^66*sqrt(2)) = 104350542602662257698,
X = floor(2^66*sqrt(2)) + 1.
```

Equivalently,

```text
X^2 = 2^133 + 42455133039302008009.              (2)
```

Put

```text
U = X+1/11
```

and define `y>0` by

```text
U^2 = 2^133*(1+y).
```

Exactly,

```text
y =
7432783035014112638468
/
1317573324717873730530186479975806514757632.
```

## 4. Cycle identity

If the orbit entered a nontrivial positive cycle of length `p`, and `A` were the total number of halvings around it, then

```text
2^A = product_i (X+1/n_i).
```

Using (1),

```text
X^p < 2^A <= U^p.                                (3)
```

## 5. Exact finite barrier

Let

```text
B = 120000000000000000000,
c = 6931/20000.
```

For every `p<=B`, with `r=floor(p/2)`, exact integer arithmetic proves

```text
r*y < c.                                         (4)
```

A rational Taylor estimate, including a rigorous geometric bound for the omitted tail, proves

```text
exp(c) < 2^67/U < 2.                             (5)
```

No floating-point logarithms are used in the certificate.

### Even length

If `p=2r`, then by (2)

```text
X^p > 2^(133r).
```

Hence (3) requires `A>=133r+1`. But (4)-(5) give

```text
U^p = 2^(133r)*(1+y)^r
    < 2^(133r)*exp(c)
    < 2^(133r+1),
```

which is impossible.

### Odd length

If `p=2r+1`, then

```text
X^p > 2^(133r+66.5),
```

so (3) requires `A>=133r+67`. Yet

```text
U^p
 < 2^(133r)*U*exp(c)
 < 2^(133r+67),
```

again impossible.

## 6. Rigorous conclusion

For

```text
(X,n0)=(104350542602662257699,1),
```

the orbit has only two possibilities:

1. it tends to positive infinity;
2. it enters a nontrivial positive cycle of length greater than `120,000,000,000,000,000,000`.

It cannot return to `1`, and all shorter cycles are excluded by a compact exact certificate. The verifier does not simulate that many steps; it checks a small collection of integer and rational inequalities.

Run

```text
python tools/verify_ultra_candidate.py
```

and see `tests/test_ultra_candidate.py`.