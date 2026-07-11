# Split-range reciprocal dual through sixty million

This note gives the retained finite reciprocal bound for the harder remaining
length

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

the retained valid two-constraint depth-three certificate proves

```text
sum 1/n < 0.085239095.                            (1)
```

## 2. Middle range

For

```text
1000000 < n <= 60000000,
```

use the scalar symmetric lower cost

```text
C_E(n)=u_min(n)-1+s(n)-1+2*O*d_X(n),
```

where `d_X(n)` is the least full predecessor layer and `u_min(n)` its source
label.  This is a valid scalar lower bound on the cost of any actual edge
entering `n`: using a higher layer adds `2*O`, more than any possible reduction
of the source-label term.

The exact modular enumeration contains

```text
4279760 small-class candidates,
536735 genuine full representatives,
178632 permanent predecessor rejections,
358103 surviving targets.
```

Restricting to the `352279` survivors above one million and applying the exact
fractional dual gives a boundary after `5179` complete items:

```text
n = 1021885,
C_E = 32815616360883804024,
target label = 1502499629181248314,
full delay = 8,
least-cost source label = 1540142525975756512.
```

The resulting exact bound is

```text
sum_(1000000<n_i<=60000000) 1/n_i
 < 0.001370625.                                   (2)
```

## 3. Combined bound and required large tail

Adding (1) and (2), while generously granting each range its own full budget,
gives

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

## 4. Retraction boundary

The least-cost source labels are useful only inside the scalar cost lower
bound.  They are not necessarily the source labels chosen by the actual cycle,
because a target can have several admissible full predecessor layers.  Hence
they must not be used as actual circulation endpoints.  The attempted
flow-completion improvement is retracted in
`docs/FLOW_BALANCED_TWO_CONSTRAINT_DUAL.md`.

Run

```text
python tools/verify_split_range_reciprocal_dual.py
```

for full reproduction.
