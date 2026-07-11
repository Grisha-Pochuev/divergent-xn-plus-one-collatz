# Ordinary cycles need more than 245832 blocks

Use the primary candidate

```text
m=4501,
B=2^4501,
d=349*2^500-347,
X=B-d.
```

This note proves a cycle-length-independent frontier:

```text
Any positive cycle with no exceptional complete block
must contain at least 245833 ordinary complete blocks.       (1)
```

The result contains the one-block and two-block theorems as very small special
cases, but those direct proofs remain useful as transparent local models.

## 1. General block-core closure

Suppose a hypothetical no-exceptional cycle has `J` complete blocks. For block
`i`, write

```text
ell_i>=1,
1<=e_i<=4500,
q_i=2^(m*ell_i-e_i),
c_i=2^e_i-1,
```

and let `u_i` be its positive odd source core. The exact block relation is

```text
q_(i+1)*u_(i+1)=X^ell_i*u_i+c_i,                   (2)
```

with cyclic indices.

Put

```text
p=sum_i ell_i,
D=sum_i e_i,
Delta_D(p)=2^(m*p-D)-X^p.                           (3)
```

Choose block `1` to be a longest block. Eliminating `u_2,...,u_J` from (2)
gives

```text
Delta_D(p)*u_1=R,                                   (4)
```

where

```text
R=sum_(i=1)^J
  c_i*(product_(r=2)^i q_r)*X^(sum_(r=i+1)^J ell_r). (5)
```

Every term in (5) is strictly less than

```text
B^(p-ell_1+1).
```

Therefore

```text
R<J*B^(p-ell_1+1).                                  (6)
```

Also

```text
ell_1>=ceil(p/J).                                   (7)
```

## 2. Continued-fraction control of every admissible total deficit

Let

```text
delta=log2(B/X),
beta=1/delta=ln(2)/ln(B/X).                         (8)
```

A positive cycle gap requires

```text
p/D>beta.                                           (9)
```

Exact rational logarithmic bounds certify the following continued-fraction
prefix of `beta` after its enormous integer part:

```text
[1,1,145062,23,1,4,1,12,2].                        (10)
```

The relevant convergent denominators are

```text
q_7=41487887,
q_8=532379529,
q_9=1106246945.                                     (11)
```

Because the next coefficient is `2`, the last upper semiconvergent before the
next upper convergent is

```text
(P_*/Q_*)=(P_7+P_8)/(Q_7+Q_8),
Q_*=573867416.                                      (12)
```

The standard one-sided best-approximation property of continued fractions says
that for every integer pair

```text
0<D<q_9,
p/D>beta,
```

we have

```text
p-D*beta>=P_*-Q_*beta.                              (13)
```

Exact interval arithmetic proves the right side positive. Multiplying by
`ln(B/X)` gives

```text
z=p*ln(B/X)-D*ln(2)>2^(-22205).                     (14)
```

## 3. Lower bound for the positive cycle gap

From (3) and (14),

```text
Delta_D(p)
 =B^p*2^(-D)*(1-exp(-z)).                           (15)
```

For positive `z`, and using (14),

```text
1-exp(-z)>2^(-22206).                               (16)
```

Hence

```text
Delta_D(p)>2^(m*p-D-22206).                         (17)
```

## 4. Contradiction for at most 245832 blocks

If

```text
J<=245832,
```

then

```text
D<=4500*J<=1106244000<q_9.                          (18)
```

Thus (13)--(17) apply.

Because `D>=J`, equation (9) gives

```text
p/J>beta.
```

Therefore the longest block satisfies

```text
ell_1>=ceil(beta).                                  (19)
```

The integer `ceil(beta)` has `1202` decimal digits. Exact integer comparison
then gives

```text
m*ell_1-D-22206
 >18+m,                                             (20)
```

where `J<2^18`.

Combining (6), (17), and (20),

```text
Delta_D(p)
 >J*B^(p-ell_1+1)
 >R.                                                 (21)
```

Since `u_1>=1`, this contradicts the exact closure equation (4).

Therefore (1) holds.

## 5. Meaning

This is not a cycle-length cutoff. The block lengths may be arbitrarily large.
The theorem excludes all no-exceptional cycles with up to `245832` complete
blocks at once.

The remaining no-exceptional case has

```text
J>=245833,
D>=245833,
```

and still obeys the full `X`-adic reciprocal bound

```text
sum_i 1/n_i
 <3*D/X+[d+H_D/2]/(X-1).
```

The next step is not to push the continued-fraction denominator merely for a
larger record. It is to use the many-block structure itself: deficit
populations, boundary classes, and repeated visits to the same terminal types.

## 6. Verification

```text
python tools/verify_no_exceptional_block_count_frontier.py
```

The checker certifies the logarithmic interval, the continued-fraction prefix,
the upper semiconvergent, the denominator frontier, and the final exponent
comparison using exact rational and integer arithmetic.
