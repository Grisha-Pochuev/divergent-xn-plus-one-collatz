# Signed-label potential reciprocal dual

This note rigorously recovers and strengthens the small-value reciprocal bound
for

```text
p = 177780727155637125195.
```

It does **not** identify the least-cost predecessor with the actual cycle
source.  Instead it constructs a global potential whose sum telescopes around
every cycle.

Put

```text
B=A-p=11644637628694231700273,
O=ord_X(2)=1860810887857924950.
```

## 1. A general nonnegative label potential

For any function `Phi` on full labels satisfying

```text
-(s-1) <= Phi(s) <= s-1,                          (1)
```

replace the exact edge cost

```text
(u-1)+(s-1)+2*O*q
```

by

```text
C_Phi(u,s,q)
 = (u-1-Phi(u))+(s-1+Phi(s))+2*O*q.               (2)
```

Every term in (2) is nonnegative by (1).  Around a cycle the potential terms
cancel, so exactly

```text
sum_i C_Phi(i)=2*B.                               (3)
```

Therefore every selected subset of cycle edges has total modified cost at most
`2B`.

## 2. Potential tailored to the small target set

For each of the `5824` permanent-sieve survivors `n<=1000000`, let

```text
s(n) = its target full label,
d(n) = its least admissible predecessor layer,
u(n) = the source label at that least layer.
```

The exact certificate proves:

```text
all 5824 target labels are distinct,
all 5824 least-source labels are distinct,
the two label sets are disjoint.                  (4)
```

Define

```text
Phi(label)= +(label-1)  on the target set,
Phi(label)= -(label-1)  on the least-source set,
Phi(label)= 0           otherwise.                (5)
```

This satisfies (1).

For a selected small target, the least-layer edge has modified cost

```text
C_F(n)=2*(u(n)+s(n)-2)+2*O*d(n).                  (6)
```

Any higher admissible layer adds at least `2O`.  Its source contribution in
(2) is nonnegative, whereas the least-layer source contribution is strictly
less than `2O`.  Hence every higher-layer choice has modified cost strictly
larger than (6).  Thus (6) is a valid lower bound for the **actual** edge,
regardless of which layer the cycle chooses.

This is the step missing from the retracted endpoint-identification argument.

## 3. Combination with the depth-three inverse cost

The independent depth-three cost is

```text
C_3(n)=3*(s(n)-1)+O*h_3(n),
sum C_3(n_i)<=3*B.
```

Use normalized weight

```text
theta=88385/100000
```

on the depth-three constraint and the complementary weight on (6).  Clearing
denominators gives

```text
C(n)=176770*C_3(n)+34845*C_F(n),
sum C(n_i)<=600000*B.                             (7)
```

The exact fractional-selection boundary occurs after `204` complete items:

```text
n = 14771,
target label = 882187649335005189,
least-source label = 1320942428550803069,
least layer = 124,
h_3 = 158,
C_3 = 296654683229557157664,
C_F = 465887360344537004112,
C = 68673493425694210668547920.
```

The resulting rational bound is

```text
sum_(cycle values n<=1000000) 1/n
 < 0.085226905.                                   (8)
```

## 4. Logical relation to the retraction

The old proof was invalid because it treated `u(n)` as the actual source label.
The present proof does not.  Formula (5) defines a potential on **all** labels;
formula (3) holds for the actual edge choices; and the least layer is shown to
minimize the modified scalar cost even if the actual source label changes.

Thus the argument is new and valid, while the old endpoint-identification
premise remains retracted.

Run

```text
python tools/verify_signed_label_potential_dual.py
```

for the exact certificate.
