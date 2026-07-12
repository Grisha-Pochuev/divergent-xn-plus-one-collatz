# Session checkpoint: actual minimum-boundary expanding segment

Date: 2026-07-12

The strict prize problem remains open. The primary candidate remains

```text
X=2^4501-349*2^500+347,
n0=1.
```

## Retained global frontiers

- every hypothetical cycle has at least `245833` ordinary complete blocks;
- a bounded positive formal circulation exists on at most `4500` ordinary
  boundary types.

## New actual consecutive segment

Choose the least cycle value immediately following an ordinary complete block,
and follow the actual orbit to the next such value. The segment contains zero or
more exceptional blocks followed by one ordinary block.

Exact block ratios, minimum-height comparison, and the one-sided
continued-fraction gap prove

```text
1<=net credit C<=4500;
exceptional excess sum <=4499;
number of complete blocks <=4500;
L*log2(B/X)<C;
endpoint > starting value.
```

Thus this is an actual consecutive orbit segment, not a formal splicing, and its
base multiplier satisfies

```text
2^C*(X/B)^L>1.
```

Files:

```text
docs/MINIMUM_BOUNDARY_ACTUAL_EXPANDING_SEGMENT.md
tools/verify_minimum_boundary_actual_expanding_segment.py
```

The standalone checker passed and is included in `run_checks.py`.

## Remaining obstruction

The rest of a hypothetical cycle would have to return from the larger endpoint
to the least ordinary boundary. The next target is a return obstruction using:

1. the endpoint classes modulo `X` and `1093^2`;
2. inverse `X`-adic descent through the return word;
3. the exceptional credit required to compensate the short expanding exit.

A finite trajectory calculation or a larger cycle-length barrier would not
address this obstruction.