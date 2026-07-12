# Session checkpoint: actual minimum-boundary segment and return dichotomy

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

## Actual consecutive expanding segment

Choose the least cycle value immediately following an ordinary complete block,
and follow the actual orbit to the next such value. Exact block ratios,
minimum-height comparison, and the one-sided continued-fraction gap prove

```text
1<=net credit C<=4500;
exceptional excess sum <=4499;
number of complete blocks <=4500;
L*log2(B/X)<C;
endpoint y > starting value x.
```

Thus this is an actual consecutive orbit segment, not a formal splice, and its
base multiplier satisfies

```text
2^C*(X/B)^L>1.
```

Files:

```text
docs/MINIMUM_BOUNDARY_ACTUAL_EXPANDING_SEGMENT.md
tools/verify_minimum_boundary_actual_expanding_segment.py
```

## New strict return-credit dichotomy

Follow the remaining actual orbit from `y` back to `x`. Let

```text
R = ordinary deficit sum - exceptional excess sum,
Lr = accelerated return length,
delta = log2(B/X).
```

The exact return ratio and positivity of every additive correction give

```text
R < Lr*delta.
```

Exact integer bounds on the primary parameters give

```text
delta < 2^-3990.
```

Therefore every hypothetical return satisfies:

```text
R>=1  =>  Lr>2^3990;
Lr<=2^3990  =>  R<=0.
```

Equivalently, every shorter return requires total exceptional excess at least as
large as the total ordinary deficit. This closes the short positive-credit return
branch, but does not yet exclude zero/negative-credit returns or an
astronomically long positive-credit return.

Files:

```text
docs/MINIMUM_BOUNDARY_RETURN_CREDIT_DICHOTOMY.md
tools/verify_minimum_boundary_return_credit_dichotomy.py
```

The new standalone checker passed in the chat environment.

## Remaining obstruction

The next proof target is now sharply split:

1. exclude a return with nonpositive net credit by a mandatory exceptional-cost
   or harmonic-window contradiction; or
2. exclude a positive-credit return whose accelerated length exceeds `2^3990`,
   preferably by inverse `X`-adic descent or endpoint congruences.

A finite trajectory calculation or a larger generic cycle barrier would not
address either branch.