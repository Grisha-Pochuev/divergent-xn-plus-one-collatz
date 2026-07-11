# Signed-label split-range reciprocal dual through sixty million

This note extends the valid signed-label potential from targets below one
million to every retained target through sixty million.  It rigorously
re-establishes numerical bounds that were previously reached by an invalid
endpoint-identification argument.

Fix the harder remaining length

```text
p = 177780727155637125195,
B = A-p = 11644637628694231700273,
O = ord_X(2) = 1860810887857924950.
```

## 1. Exact edge budget

If an actual cycle edge has source full label `u`, target full label `s`, and
full-order layer `q`, its symmetric incremental cost is

```text
C(u,s,q)=(u-1)+(s-1)+2*O*q.
```

Around every hypothetical cycle,

```text
sum C(u_i,s_i,q_i)=2*B.                            (1)
```

For any function `Phi` on full labels satisfying

```text
-(r-1) <= Phi(r) <= r-1,
```

define

```text
C_Phi(u,s,q)
 = (u-1-Phi(u))+(s-1+Phi(s))+2*O*q.                (2)
```

Every term in (2) is nonnegative, and the potential telescopes around the
actual cycle.  Hence

```text
sum C_Phi(u_i,s_i,q_i)=2*B.                        (3)
```

In particular, every selected subset of actual cycle edges has total modified
cost at most `2B`.

## 2. Finite label sets through sixty million

The exact retained enumeration through

```text
60000000
```

contains

```text
4279760 small-class candidates,
536735 genuine full representatives,
178632 permanent predecessor rejections,
358103 surviving targets.
```

For each surviving target `n`, let

```text
s(n) = its target full label,
d(n) = its least admissible predecessor layer,
u(n) = the full label of the source at layer d(n).
```

The exact certificate proves across all `358103` survivors:

```text
all target labels s(n) are distinct,
all least-source labels u(n) are distinct,
the two label sets are disjoint.                   (4)
```

Define one global potential by

```text
Phi(r)= +(r-1)  on the target-label set,
Phi(r)= -(r-1)  on the least-source-label set,
Phi(r)= 0       otherwise.                         (5)
```

Because of (4), this is well-defined and satisfies the required bounds.

## 3. Why the least layer gives a valid cost for the actual edge

For the least admissible edge entering `n`, formulas (2) and (5) give

```text
C_F(n)=2*(u(n)+s(n)-2)+2*O*d(n).                   (6)
```

The actual cycle may enter the same target through a higher admissible layer
and therefore through a different source label.  We do not identify that
source with `u(n)`.

Instead, any higher layer adds at least `2O` to the layer term in (2).  Its
source component is nonnegative.  The least-layer source component in (6) is

```text
2*(u(n)-1) < 2O.
```

Therefore every higher-layer choice has strictly larger modified cost than
(6).  Thus (6) is a lower bound for the modified cost of the **actual** edge,
regardless of which admissible layer the cycle chooses.

This is the logical step that repairs the earlier retracted proof.

## 4. Middle-range fractional dual

Restrict to the

```text
352279
```

surviving targets in

```text
1000000 < n <= 60000000.
```

Apply the exact fractional-selection dual to item value `1/n`, cost `C_F(n)`,
and budget `2B`.  The boundary occurs after `3350` complete items:

```text
n = 1135801,
C_F = 30963450586533289068,
target label = 58772698851070868,
least layer = 8,
least-source label = 536465491552174068.
```

The resulting exact rational bound is

```text
sum_(1000000<n_i<=60000000) 1/n_i
 < 0.001185304.                                    (7)
```

## 5. Combined retained bound

The independent signed-label/depth-three certificate below one million gives

```text
sum_(n_i<=1000000) 1/n_i < 0.085226905.
```

Granting each disjoint value range its own full budget is an overestimate and
is therefore safe.  Adding the two bounds gives

```text
sum_(n_i<=60000000) 1/n_i
 < 0.086412209.                                    (8)
```

The exact cycle interval requires a total reciprocal sum greater than
`0.099934206877...`.  Hence values above sixty million must contribute more
than `0.013521997`.  Since every such distinct value contributes less than
`1/60000000`, at least

```text
811320
```

distinct cycle values must exceed sixty million.

Since at most `6257` cycle positions have positive full-order layer, at least

```text
811320-6257 = 805063
```

of these mandatory large values are zero-layer targets.

## 6. Audit boundary

The old endpoint-identification proof remains invalid: a target does not fix
the source label chosen by the actual cycle.  The present result is independent
of that premise.  It uses a potential defined on all labels, exact telescoping
on the actual cycle, and a proof that the least admissible layer minimizes the
modified scalar cost.

Run

```text
python tools/verify_signed_label_split_range_dual.py
```

for the exact deterministic certificate.  It classifies modular representatives
and does not scan trajectories.
