# RETRACTED: flow-balanced two-constraint reciprocal dual

The former claim in this file is invalid and must not be used.

## False premise

For each small target `n`, the certificate chose the **least-cost admissible
full predecessor** and denoted its source label by `u_min(n)`.  The scalar edge
cost based on this predecessor is a valid lower bound: using a higher full
layer adds `2*O` and cannot reduce the total edge cost.

The invalid step treated `u_min(n)` as if it were the source label of the
**actual cycle edge**.  It then used disjointness of the selected
`u_min(n)` labels and target labels to charge an additional flow-completion
cost.

But a target can have several admissible full predecessor layers.  The actual
cycle may use a higher layer with a different source label.  Thus minimum-cost
source labels do not describe the actual circulation endpoints, and their
apparent imbalance need not be balanced by the rest of the cycle.

## Explicit regression example

For the valid full output

```text
n = 25,
target label = 1208196370322173126,
```

the first admissible predecessor layers include

```text
q=50,  source label=1417145250304345366,
q=58,  source label=1528337129047052390,
q=72,  source label=1031609925039487316,
q=114, source label=246249236019459722,
q=118, source label=188856312470187702.
```

All lead to the same target but have different actual source labels.  This is a
direct counterexample to the endpoint identification used by the retracted
flow argument.

## Consequences

The following claimed improvements are retracted:

```text
small bound 0.085226905,
combined sixty-million bound 0.086412209,
811320 mandatory values above sixty million,
805063 mandatory zero-layer values above sixty million.
```

The last retained valid figures are

```text
small bound 0.085239095,
combined sixty-million bound 0.086609720,
799470 mandatory values above sixty million,
793213 mandatory zero-layer values above sixty million.
```

The scalar symmetric edge-cost bound and the earlier two-constraint dual remain
valid; only the extra endpoint-flow completion charge is retracted.

Run

```text
python tools/verify_flow_balanced_two_constraint_dual.py
```

for the regression audit preventing reintroduction of the false endpoint
identification.
