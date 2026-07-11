# Flow-balanced two-constraint reciprocal dual

This note strengthens the small-value reciprocal certificate for

```text
p = 177780727155637125195.
```

Put

```text
B=A-p=11644637628694231700273.
```

## 1. Flow-completion cost for the 5824 small edges

For every admissible target `n<=1000000`, let

```text
u(n) = source full label of its least-layer predecessor,
s(n) = target full label,
d(n) = least full predecessor layer.
```

The exact enumeration proves:

```text
all 5824 target labels s(n) are distinct,
all 5824 source labels u(n) are distinct,
{u(n)} and {s(n)} are disjoint.
```

For a selected set `S` of such cycle edges, no selected source-target imbalance
can cancel inside `S`.  The rest of the cycle must provide one incoming endpoint
for every selected source label and one outgoing endpoint for every selected
target label.

The selected edge itself costs

```text
C_E(n)=u(n)-1+s(n)-1+2*O*d(n).
```

Any flow completion costs at least one additional copy of the endpoint-label
sum.  Therefore every selected set satisfies the additive bound

```text
sum_(n in S) C_F(n) <= 2*B,                       (1)
```

where

```text
C_F(n)=2*(u(n)+s(n)-2)+2*O*d(n).
```

This is stronger than the former symmetric edge cost on this small set.

## 2. Independent depth-three cost

Let `h_3(n)` be the minimum total full-order layer in an admissible three-edge
inverse window.  The retained exact bound is

```text
C_3(n)=3*(s(n)-1)+O*h_3(n),
sum C_3(n_i)<=3*B.                                (2)
```

## 3. Exact combined dual

Use the rational normalized multiplier

```text
theta = 88385/100000
```

on (2), and the complementary multiplier on (1).  Clearing denominators gives

```text
C(n)=176770*C_3(n)+34845*C_F(n),
sum C(n_i)<=600000*B.                             (3)
```

The exact fractional-selection dual over all `5824` candidates has its boundary
after `204` complete items.  The boundary item is

```text
n = 14771,
target label = 882187649335005189,
source label = 1320942428550803069,
least layer = 124,
h_3 = 158,
C_3 = 296654683229557157664,
C_F = 465887360344537004112,
C = 68673493425694210668547920.
```

The resulting exact rational bound is

```text
sum_(cycle values n<=1000000) 1/n
 < 0.085226905.                                   (4)
```

This improves the previous two-constraint value `0.085239095` and the original
depth-three value `0.085243521`.

## 4. Updated split-range consequence

The independent symmetric middle-range certificate gives

```text
sum_(1000000<n_i<=60000000)1/n_i <0.001370625.
```

Combining with (4),

```text
sum_(n_i<=60000000)1/n_i <0.086597530.
```

Since the exact cycle interval requires more than `0.099934206877`, values above
sixty million must contribute more than `0.013336677`.  Distinctness therefore
forces at least

```text
800201
```

cycle values above sixty million.

## 5. Significance

The gain comes from a genuinely global transition condition: small selected
edges cannot balance their own label flow.  This validates the circulation-dual
route and suggests extending endpoint-disjoint or low-overlap charging to the
middle range and to short inverse windows.

Run

```text
python tools/verify_flow_balanced_two_constraint_dual.py
```

for the exact certificate.
