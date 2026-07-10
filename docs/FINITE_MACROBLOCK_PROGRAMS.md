# Arbitrary finite programs of complete growing macroblocks

Fix

```text
X = 2^m + 1,    m >= 2,
```

and let

```text
C_X(n) = (X*n+1) / 2^v2(X*n+1)
```

on positive odd integers.  This note extends the earlier special start
`2^(mL)-1` to the family

```text
n = 2^(mL)*q - 1,
```

where `q` is any positive odd integer.  The extra odd parameter makes exact
chaining possible.

## 1. General complete macroblock

Let `L >= 1`, let `q` be positive and odd, and put

```text
n_0 = 2^(mL)*q - 1.
```

For `0 <= j <= L-1`,

```text
n_j = 2^(m(L-j)) * X^j * q - 1.                 (1)
```

For `0 <= j < L-1` the exact valuation is `m`.  At the final state,

```text
X*n_(L-1)+1 = 2^m * (X^L*q - 1).
```

Write

```text
r = v2(X^L*q - 1) >= 1.
```

Then the last valuation is exactly `m+r`, and the complete endpoint after
`L` accelerated steps is

```text
H_(m,L)(q) = (X^L*q - 1) / 2^r.                 (2)
```

Thus the exact valuation word of the complete block is

```text
(m, m, ..., m, m+r),
```

with `L-1` copies of `m` before the final symbol.

### Proof

Formula (1) follows by induction.  Whenever `j<L-1`, the exponent of two in
`n_j+1` is strictly greater than `m`, so the valuation lemma for
`X=2^m+1` gives one exact valuation-`m` step and produces the next value in
(1).  At `j=L-1`, direct substitution gives the displayed factorization,
which proves (2).

## 2. A simple complete-growth criterion

Put

```text
delta_m = log2(X/2^m) = log2(1+2^(-m)) > 0.
```

If

```text
L*delta_m > r+1,                                (3)
```

then the complete endpoint is larger than the start:

```text
H_(m,L)(q) > 2^(mL)*q - 1.
```

Indeed,

```text
H_(m,L)(q)
  = (X^L*q-1)/2^r
  > X^L*q/2^(r+1)
  = 2^(mL)*q * 2^(L*delta_m-r-1),
```

and condition (3) makes the last factor greater than one.

The criterion is uniform in `q`: once `L` and `r` satisfy (3), every exact
block with those parameters grows completely, including its exceptional
exit.

## 3. Exact transition between two macroblocks

Suppose a boundary state has the form

```text
n_i = 2^(m*L_i)*q_i - 1,
```

and after its complete block we want the next boundary state to be

```text
n_(i+1) = 2^(m*L_(i+1))*q_(i+1) - 1.
```

Prescribe the final excess valuation `r_i >= 1`.  Equations (1)--(2) show
that this transition is exact if and only if

```text
X^(L_i)*q_i
  = 2^(r_i + m*L_(i+1))*q_(i+1) - 2^r_i + 1.   (4)
```

Equivalently,

```text
q_i = [2^(r_i+m*L_(i+1))*q_(i+1)-2^r_i+1]
      / X^(L_i).                                (5)
```

If (4) holds with positive odd `q_i,q_(i+1)`, then

```text
X^(L_i)*q_i - 1
  = 2^r_i * (2^(m*L_(i+1))*q_(i+1)-1),
```

and the parenthesis is odd.  Therefore the exit valuation is exactly
`r_i`, not merely at least `r_i`.

## 4. Finite-program realization theorem

**Theorem.**  Choose arbitrary integers

```text
L_0, L_1, ..., L_R >= 1
r_0, r_1, ..., r_(R-1) >= 1.
```

Then there exist infinitely many positive odd tuples

```text
(q_0, q_1, ..., q_R)
```

such that every transition (4) holds.  Consequently the accelerated orbit
starting at

```text
n_0 = 2^(m*L_0)*q_0 - 1
```

follows exactly the prescribed `R` complete macroblocks.

If in addition

```text
L_i*delta_m > r_i+1
```

for every `0 <= i < R`, then every boundary strictly increases:

```text
n_0 < n_1 < ... < n_R.
```

### Proof

Work backwards from `q_R`.  Repeated substitution of (5) gives

```text
q_0 = (P*q_R + Q) / X^S,                        (6)
```

where

```text
S = L_0 + ... + L_(R-1)
```

and `P` is a power of two.  Hence `gcd(P,X^S)=1`.  There is exactly one
residue class

```text
q_R == -Q * P^(-1)  (mod X^S)                  (7)
```

for which `q_0` is integral.  The same backward construction then makes
every intermediate `q_i` integral as well.

The modulus `X^S` is odd.  Among two consecutive representatives of the
class (7), one is odd, and adding `2*X^S` gives infinitely many further
positive odd representatives.  Formula (5) shows that all backward values
are positive and odd.  This proves exact finite realizability.  The strict
growth statement follows block by block from criterion (3).

## 5. Concrete examples

For `m=2`, so `X=5`, take four boundary lengths

```text
(7, 7, 7, 7)
```

and three prescribed exits

```text
(1, 1, 1).
```

The checker constructs an exact orbit with three complete growing blocks.
The first boundary has 60 bits, and the successive boundaries have
62, 63, and 64 bits.

A nonperiodic finite example is obtained from the first eleven symbols of a
Thue--Morse choice between lengths 7 and 8:

```text
(7, 8, 8, 7, 8, 7, 7, 8, 8, 7, 7),
```

again with every exit equal to 1.  It realizes ten complete blocks and all
ten boundary transitions grow.  The boundary bit lengths are

```text
175, 177, 178, 180, 181, 183, 184, 185, 187, 188, 189.
```

Both examples are reproduced by

```bash
python tools/build_macroblock_program.py --m 2 \
  --lengths 7,7,7,7 --exits 1,1,1

python tools/build_macroblock_program.py --m 2 \
  --lengths 7,8,8,7,8,7,7,8,8,7,7 \
  --exits 1,1,1,1,1,1,1,1,1,1
```

## 6. What this proves and what remains

The earlier construction gave one arbitrarily long increasing prefix.  The
present theorem is stronger:

1. it includes the exceptional exit of every block;
2. it permits an arbitrary odd payload `q`;
3. it realizes any prescribed finite chain of complete blocks;
4. it can make every complete block strictly increasing;
5. the finite program may be genuinely aperiodic.

This still does not produce one fixed positive integer supporting infinitely
many blocks.  As `R` grows, the congruence (7) changes and normally forces a
new, larger starting integer.  An infinite prescribed program defines a
nested arithmetic target, but finite solvability alone does not imply that
its limiting target is an ordinary positive integer.

The remaining problem is therefore sharply isolated:

> Find an infinite growing macroblock program whose nested congruence targets
> are represented by one fixed positive integer, or prove growth by a finite
> branching certificate that avoids prescribing one exact infinite program.
