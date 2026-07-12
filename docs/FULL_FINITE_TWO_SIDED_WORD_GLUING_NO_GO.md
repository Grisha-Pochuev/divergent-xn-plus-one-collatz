# Full finite two-sided valuation words are always locally glueable

Let `X>=3` be odd and use the accelerated map

```text
C_X(n)=(X*n+1)/2^v2(X*n+1).
```

This note strengthens `FIXED_LOCAL_ENDPOINT_CONGRUENCE_NO_GO.md`.  The earlier
result prescribed one incoming complete near-power block.  Here the incoming
piece may be an arbitrary finite exact valuation word, so its `X`-adic depth
may grow with the entire finite return word.

The theorem is deliberately local.  It does not impose that the source of the
incoming word equals the actual endpoint of the outgoing word.  That exact
source-matching equation is isolated in Section 5.

## 1. Forward constants for a finite word

For a positive valuation word

```text
W=(a_0,...,a_(t-1)),
A_W=sum_j a_j,
```

put

```text
Q_W=sum_(j=0)^(t-1) X^(t-1-j)*2^(a_0+...+a_(j-1)),
```

where the empty prefix sum is zero.  Every orbit segment with word `W` obeys

```text
2^A_W*n_t=X^t*n_0+Q_W.                               (1)
```

Conversely, exact valuation-word coding gives one odd class

```text
n_0==r_W (mod 2^(A_W+1))                              (2)
```

whose positive representatives have exact successive valuations `W`.  In
closed form,

```text
r_W=[2^A_W-Q_W]*X^(-t) (mod 2^(A_W+1)).               (3)
```

## 2. An arbitrary incoming word fixes one endpoint class modulo `X^t`

Now fix another positive word

```text
V=(b_0,...,b_(r-1)),
A_V=sum_j b_j,
```

and ask that an orbit segment with word `V` end at a common boundary `x`.
Equation (1), read with source `y` and endpoint `x`, is

```text
2^A_V*x=X^r*y+Q_V.                                    (4)
```

Thus integrality of the incoming source requires

```text
x==s_V:=Q_V*2^(-A_V) (mod X^r).                       (5)
```

This single congruence is also sufficient.  Starting from such an `x`, define
backwards

```text
z_r=x,
z_j=(2^b_j*z_(j+1)-1)/X.                       (6)
```

The class (5) is exactly the nested inverse class that makes every `z_j` an
integer.  If `x` is odd, all `z_j` are odd.  Taking `x` sufficiently large
makes all of them positive, and then

```text
X*z_j+1=2^b_j*z_(j+1)
```

proves that the incoming valuations are exactly `V`.

## 3. Two-sided gluing theorem

The incoming word `V` prescribes (5) modulo the odd number `X^r`.  The outgoing
word `W` prescribes (2) modulo the power of two `2^(A_W+1)`.  These moduli are
coprime.  The Chinese remainder theorem therefore gives one common class
modulo

```text
X^r*2^(A_W+1).                                        (7)
```

This class contains infinitely many positive odd integers.  Choosing a
sufficiently large representative gives positive backwards states in (6).
Hence:

```text
For every odd X>=3 and every pair of finite positive valuation words V,W,
there are infinitely many positive odd boundaries x such that

- an actual positive orbit segment with exact word V ends at x; and
- the forward orbit from x begins with the exact word W.
```

The statement remains true after imposing any fixed finite lower height bound.
It also allows `V` to have any prescribed finite block decomposition or net
credit compatible with its labels.

## 4. Consequence for the current return strategy

A growing-depth endpoint calculation modulo `X^r` cannot by itself contradict a
finite positive-credit return word: the entire incoming word is still locally
compatible with the outgoing expanding word by (7).

Therefore the following data, even when all are retained exactly, are not by
themselves enough:

1. every valuation in a finite incoming return word;
2. the resulting endpoint class modulo `X^r`;
3. every valuation in a finite outgoing exit word;
4. any fixed finite lower bound on the common boundary.

This does not rule out the project’s global `X`-adic route.  It proves that the
route must use the equality between the incoming source and the actual outgoing
endpoint, or some equivalent global condition such as cycle closure or the
minimum-boundary inequalities.

## 5. The exact source-matching equation

Let `W` be the exit word from `x` to `y`, and let `V` be the remaining return
word from `y` back to `x`.  Write their lengths as `t,r`.  Equations (1) and
(4) give

```text
2^A_W*y=X^t*x+Q_W,
2^A_V*x=X^r*y+Q_V.
```

Eliminating `y` yields the exact closure equation

```text
[2^(A_W+A_V)-X^(t+r)]*x
  =X^r*Q_W+2^A_W*Q_V.                                 (8)
```

Thus, once the two words are fixed, local CRT compatibility is automatic.  The
genuine remaining obstruction is the global divisibility and size condition in
(8), together with positivity, the minimum-boundary property, and the credit
constraints.  Any successful whole-return descent must obtain new information
about (8); merely recomputing the endpoint residue modulo higher powers of `X`
repeats a consequence already encoded in the equation.

For a positive cycle the coefficient on the left of (8) is positive.  Hence a
candidate word pair must satisfy

```text
2^(A_W+A_V)>X^(t+r)
```

and the left coefficient must divide the explicit positive numerator on the
right.

## 6. Verification

```text
python tools/verify_full_finite_two_sided_word_gluing_no_go.py
```

The checker verifies the forward and inverse formulas, constructs exact
positive two-sided gluings on a finite grid, checks large examples for the
primary multiplier, and reproduces the known accelerated `5n+1` cycle

```text
13 -> 33 -> 83 -> 13
```

from the split closure equation (8).
