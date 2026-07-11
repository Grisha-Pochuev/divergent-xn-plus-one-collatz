# Flow-balanced split-range reciprocal dual through sixty million

This note improves the finite reciprocal bound for the harder remaining length

```text
p = 177780727155637125195.
```

Disjoint value ranges may each be granted the entire global cost budget.  This
overcounts the available budget and is therefore safe.

## 1. Small range

For targets

```text
n <= 1000000,
```

the retained flow-balanced depth-three certificate proves

```text
sum 1/n < 0.085226905.                            (1)
```

## 2. Middle range and flow completion

For

```text
1000000 < n <= 60000000,
```

write

```text
u(n) = source full label,
s(n) = target full label,
d(n) = least full predecessor layer.
```

The exact enumeration through sixty million contains

```text
4279760 small-class candidates,
536735 genuine full representatives,
178632 permanent predecessor rejections,
358103 surviving targets.
```

Across all `358103` survivors:

```text
all source labels are distinct,
all target labels are distinct,
the source-label and target-label sets are disjoint.
```

Therefore a selected set of middle-range edges cannot balance its own label
flow.  In addition to paying its own edge cost, the rest of the cycle must pay
one more copy of every selected endpoint label.  The valid flow-completed item
cost is

```text
C_F(n)=2*(u(n)+s(n)-2)+2*O*d(n),
sum C_F(n_i)<=2*(A-p).                            (2)
```

Restricting to the `352279` survivors above one million and applying the exact
fractional dual to (2) gives a boundary after `3350` complete items:

```text
n = 1135801,
C_F = 30963450586533289068,
target label = 58772698851070868,
full delay = 8,
source label = 536465491552174068.
```

The resulting exact bound is

```text
sum_(1000000<n_i<=60000000) 1/n_i
 < 0.001185304.                                   (3)
```

The former symmetric-edge value was `0.001370625`.

## 3. Combined bound and required large tail

Adding (1) and (3), while generously granting each range its own full budget,
gives

```text
sum_(n_i<=60000000) 1/n_i
 < 0.086412209.                                   (4)
```

The exact interval identity requires

```text
sum_i 1/n_i > 0.099934206877...
```

so values above sixty million must contribute more than

```text
0.013521997.
```

Every such distinct value contributes less than `1/60000000`.  Hence at least

```text
811320
```

distinct cycle values must exceed sixty million.

The former unsplit certificate required `738929`; the total improvement is
`72391` additional mandatory large values.

## 4. Status

The result still leaves ample room in a cycle of length about `1.78*10^20`.
Its significance is structural: exact flow balance improves both the deep small
range and the shallower middle range.  Extending the same endpoint-disjoint
charging beyond sixty million is now a concrete route.

Run

```text
python tools/verify_split_range_reciprocal_dual.py
```

for full reproduction.  The verifier performs deterministic modular
classification, not a trajectory search.
