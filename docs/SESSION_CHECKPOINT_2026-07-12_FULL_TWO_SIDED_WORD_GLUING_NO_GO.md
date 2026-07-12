# Session checkpoint: full finite two-sided word gluing no-go

Date: 2026-07-12

The strict prize problem remains open. The primary candidate remains

```text
X=2^4501-349*2^500+347,
n0=1.
```

## Retained return frontiers

For the actual return from the larger endpoint of the minimum-boundary expanding
segment back to the least ordinary boundary:

```text
positive return credit    => length >2^3990;
nonpositive return credit => length >2^(2^974).
```

## New strict no-go theorem

Let `V` be any finite positive valuation word that is required to end at a
boundary `x`, and let `W` be any finite positive valuation word required to
start at `x`.

The incoming word `V` fixes one endpoint class modulo

```text
X^len(V),
```

while the outgoing word `W` fixes one odd start class modulo

```text
2^(sum(W)+1).
```

The moduli are coprime. The Chinese remainder theorem therefore gives
infinitely many positive odd boundaries realizing both complete finite words
exactly. This remains true when the incoming `X`-adic depth grows with the
entire finite return word and after any fixed finite lower height bound.

Consequently neither a fixed-depth endpoint comparison nor the full finite
incoming residue modulo `X^len(V)` can by itself exclude a return.

## Exact remaining equation

If `W` maps the least ordinary boundary `x` to `y` and `V` is meant to return
from `y` to `x`, define the standard word constants by

```text
2^A_W*y=X^t*x+Q_W,
2^A_V*x=X^r*y+Q_V.
```

Exact source matching is equivalent to

```text
[2^(A_W+A_V)-X^(t+r)]*x
  =X^r*Q_W+2^A_W*Q_V.
```

Local CRT compatibility is automatic. The remaining obstruction is now
precisely the divisibility and size information in this closure equation,
coupled to minimum-boundary and credit constraints.

Files:

```text
docs/FULL_FINITE_TWO_SIDED_WORD_GLUING_NO_GO.md
tools/verify_full_finite_two_sided_word_gluing_no_go.py
```

## Verification

The standalone checker passed in the chat environment. It verifies:

```text
1536 small exact two-sided gluings;
6 exact gluings for the primary enormous multiplier;
the forward and inverse word formulas;
the exact residual/source-matching identity;
the known 5n+1 cycle 13 -> 33 -> 83 -> 13.
```

The checker is included in `run_checks.py`. A complete repository-wide run was
not executed.

## Remaining obstruction

The uncoupled growing-depth `X`-adic endpoint route is closed. The next target
must attack the exact closure equation itself, preferably by proving that its
left coefficient cannot divide its explicit numerator under the actual
minimum-boundary and positive-return constraints. Other live routes are
regeneration of the expanding exit and a global exclusion of the
nonpositive-return branch beyond its double-exponential frontier.
