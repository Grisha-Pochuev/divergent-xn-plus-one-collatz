# Cyclic-rotation gcd criterion for exact positive cycle closure

Let `X>=3` be odd and let

```text
U=(a_0,...,a_(p-1)),
A=sum_i a_i
```

be a finite word of positive valuations. For a word

```text
Z=(z_0,...,z_(p-1))
```

write

```text
Q(Z)=sum_(j=0)^(p-1) X^(p-1-j)*2^(z_0+...+z_(j-1)),
```

with empty prefix sum zero. Put

```text
Delta=2^A-X^p.
```

For each `k` let `U_k` be the cyclic rotation of `U` starting at `a_k`, and put

```text
Q_k=Q(U_k).
```

This note converts the remaining source-matching equation into an exact common-
gcd condition on the cyclic word. It is global: unlike the two-sided local CRT
gluing theorem, it couples every rotation of the proposed cycle.

## 1. Rotation recurrence

The cyclic numerators satisfy, with indices modulo `p`,

```text
2^a_k*Q_(k+1)=X*Q_k+Delta.                         (1)
```

To see this, start from the definition of `Q_k`. Multiplication by `X` shifts
all its terms one `X`-power upward. Multiplication of `Q_(k+1)` by `2^a_k`
reproduces all shifted prefix terms, while its final wrapped term is `2^A`.
The only unmatched term on the other side is `X^p`, giving (1).

Every `Q_k` and `Delta` is odd. Hence powers of two are invertible modulo every
common divisor occurring below.

## 2. Exact gcd identity

For every positive word, without assuming that it closes,

```text
gcd(Q_0,Q_1,...,Q_(p-1))=gcd(Q_0,Delta).           (2)
```

Indeed, any common divisor of all `Q_k` divides (1), hence divides `Delta`.
Conversely, let `h=gcd(Q_0,Delta)`. Since `h` is odd, (1) propagates

```text
h|Q_k  =>  h|Q_(k+1).
```

Going once around the word proves that `h` divides every cyclic numerator.

There is also an adjacent form:

```text
gcd(Q_k,Q_(k+1))=gcd(Q_k,Delta)                    (3)
```

for every `k`, by the same recurrence and oddness.

## 3. Necessary and sufficient cycle criterion

The word `U` is the exact valuation word of a positive accelerated `Xn+1` cycle
if and only if

```text
Delta>0
and
Delta|Q_0.                                         (4)
```

Equivalently, any one of the following conditions may replace the divisibility
in (4):

```text
gcd(Q_0,...,Q_(p-1))=Delta;                        (5)

gcd(Q_k,Q_(k+1))=Delta for one k;                  (6)

gcd(Q_k,Q_(k+1))=Delta for every k.                (7)
```

### Necessity

If positive odd states `n_k` form a cycle with word `U`, the standard affine
word identity, started at each rotation, gives

```text
Delta*n_k=Q_k.                                     (8)
```

Thus `Delta>0` and `Delta|Q_k` for every `k`. Adjacent cycle states are
coprime, because

```text
2^a_k*n_(k+1)-X*n_k=1.
```

Therefore

```text
gcd(Q_k,Q_(k+1))=Delta*gcd(n_k,n_(k+1))=Delta.
```

### Sufficiency

Assume (4). Identity (1) propagates divisibility by `Delta` through all
rotations. Define

```text
n_k=Q_k/Delta.
```

All `n_k` are positive odd integers, and division of (1) by `Delta` gives

```text
2^a_k*n_(k+1)=X*n_k+1.                             (9)
```

Since `n_(k+1)` is odd, the exact valuation of the right side is `a_k`.
Equation (9) therefore realizes the required accelerated transitions and closes
after `p` steps.

This proves all equivalences in (4)--(7).

## 4. Relation to the current split closure equation

Split the cyclic word as

```text
U=W followed by V,
len(W)=t,
len(V)=r.
```

The word constants obey the exact concatenation identity

```text
Q(U)=X^r*Q_W+2^A_W*Q_V.                            (10)
```

Hence the existing source-matching equation

```text
[2^(A_W+A_V)-X^(t+r)]*x
  =X^r*Q_W+2^A_W*Q_V
```

is precisely

```text
Delta*x=Q(U).                                      (11)
```

The local two-sided CRT theorem guarantees compatible finite endpoint classes,
but it does not imply `Delta|Q(U)`. The missing global condition is exactly
that the common divisor of the cyclic numerators reaches its maximum possible
value `Delta`.

## 5. Minimum-boundary information becomes word-internal

When (4) holds, (8) shows that every comparison of cycle heights is exactly a
comparison of cyclic numerators:

```text
n_i<n_j  iff  Q_i<Q_j,
Delta*(n_j-n_i)=Q_j-Q_i.                           (12)
```

For the current primary argument, let rotation `0` start at the least cycle
value immediately following an ordinary complete block, and let rotation `t`
start at the next such boundary. The already proved actual expanding segment
then gives the strict word inequality

```text
Q_t>Q_0.                                           (13)
```

Moreover `Q_0` must be the least cyclic numerator among all rotations beginning
at ordinary boundaries. These are global ordering constraints on one complete
cyclic word; they are absent from the local CRT construction.

For the primary multiplier every hypothetical cycle state is greater than

```text
N=2^500-1.
```

Thus every cyclic numerator of a closing word must also satisfy

```text
Q_k>Delta*N.                                       (14)
```

## 6. Consequence for the proof strategy

This theorem does not exclude all cycles and therefore does not yet prove
divergence. It does, however, replace an open-ended endpoint-matching question
by one exact arithmetic target:

```text
For every admissible complete cyclic word U,
prove gcd(Q_k,Q_(k+1))<Delta for at least one k,
```

or derive a contradiction from (13)--(14) together with the block-credit and
return-length constraints.

A fixed endpoint congruence cannot accomplish this: it sees only reductions of
(11), whereas the required equality is a common divisor of the full cyclic
numerators. The next useful computation should therefore stream the Euclidean
remainders of selected cyclic numerators from complete-block data, rather than
increase a residue modulus or a finite trajectory cutoff.

## 7. Verification

```text
python tools/verify_cyclic_rotation_closure_gcd.py
```

The verifier checks the rotation recurrence, concatenation identity, full and
adjacent gcd identities on an exhaustive small grid, reconstructs every closing
word found there, reproduces the known `5n+1` cycles, and checks large exact
identities for the primary multiplier.
