# Split-range reciprocal dual through sixty million

This note improves the finite reciprocal bound for the harder remaining length

```text
p = 177780727155637125195.
```

The key point is that disjoint value ranges may each be given the entire global
cost budget.  This overcounts the available budget and is therefore safe.

## 1. Small range

For targets

```text
n <= 1000000,
```

the retained two-constraint depth-three certificate proves

```text
sum 1/n < 0.085239095.                            (1)
```

## 2. Middle range

For

```text
1000000 < n <= 60000000,
```

use the exact symmetric edge cost

```text
C_E(n)=u(n)-1+s(n)-1+2*O*d_X(n),
```

where `s(n)` is the target label, `d_X(n)` the least full predecessor layer,
and `u(n)` the corresponding source label.  Every cycle satisfies

```text
sum C_E(n_i)<=2*(A-p).
```

The exact modular enumeration through sixty million contains

```text
4279760 small-class candidates,
536735 genuine full representatives,
178632 permanent predecessor rejections,
358103 surviving targets.
```

Restricting to the `352279` survivors above one million and applying the exact
fractional dual gives a boundary after `5179` complete items.  The boundary is

```text
n = 1021885,
C_E = 32815616360883804024,
target label = 1502499629181248314,
full delay = 8,
source label = 1540142525975756512.
```

The resulting exact bound is

```text
sum_(1000000<n_i<=60000000) 1/n_i
 < 0.001370625.                                   (2)
```

## 3. Combined bound and required large tail

Adding (1) and (2) is valid even though each part was granted its own full
budget.  Therefore

```text
sum_(n_i<=60000000) 1/n_i
 < 0.086609720.                                   (3)
```

The exact interval identity requires

```text
sum_i 1/n_i > 0.099934206877...
```

so values above sixty million must contribute more than

```text
0.013324487.
```

Every such distinct value contributes less than `1/60000000`.  Hence at least

```text
799470
```

distinct cycle values must exceed sixty million.

The former unsplit certificate required `738929`; the improvement is `60541`
additional mandatory large values.

## 4. Status

The result still leaves ample room in a cycle of length about `1.78*10^20`.
Its importance is methodological: deep inverse information is most efficient
on the smallest range, while the symmetric edge cost controls the middle range
without diluting the stronger small-value constraint.

Run

```text
python tools/verify_split_range_reciprocal_dual.py
```

for full reproduction.  The verifier performs the retained deterministic
modular enumeration, not a trajectory search.
