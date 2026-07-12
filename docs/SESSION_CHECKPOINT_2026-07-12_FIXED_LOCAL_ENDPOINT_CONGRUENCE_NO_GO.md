# Session checkpoint: fixed local endpoint congruence no-go

Date: 2026-07-12

The strict prize problem remains open. The primary candidate remains

```text
X=2^4501-349*2^500+347,
n0=1.
```

## Retained global frontiers

- every hypothetical cycle has at least `245833` ordinary complete blocks;
- the actual minimum-boundary exit has credit `1<=C<=4500`;
- its exceptional excess is at most `4499`;
- it contains at most `4500` complete blocks and ends at a larger boundary.

## Retained return frontiers

For the actual return from the larger endpoint of the minimum-boundary expanding
segment back to the least ordinary boundary:

```text
positive return credit  => length >2^3990;
nonpositive return credit => length >2^(2^974).
```

## New strict no-go theorem

Fix any finite outgoing valuation word. Also fix any actual incoming complete
block of one of the forms

```text
ordinary:    m,...,m,m-e;
exceptional: m,...,m,m+b.
```

The incoming block prescribes the common boundary modulo `X^ell`, while the
outgoing word prescribes it modulo `2^(A+1)`. Since these moduli are coprime, CRT
constructs infinitely many positive odd boundary values realizing both pieces
exactly.

Therefore no return contradiction can be based only on finitely many local
incoming and outgoing labels modulo `X^2` or any other fixed `X^h`.

This does not close the global `X`-adic route. A successful argument may still
use the entire return word, depth growing with the return length, exact cycle
closure, or minimum-height inequalities.

Files:

```text
docs/FIXED_LOCAL_ENDPOINT_CONGRUENCE_NO_GO.md
tools/verify_fixed_local_endpoint_congruence_no_go.py
```

## Verification

The standalone checker passed in the chat environment. It verifies:

```text
1984 small exact near-power constructions;
5 exact constructions for the primary candidate;
both ordinary and exceptional incoming blocks;
independently prescribed finite outgoing valuation words.
```

The checker is included in `run_checks.py`. A complete repository-wide run was
not executed.

## Remaining obstruction

The fixed-depth local endpoint route is closed. The next target must be genuinely
nonlocal, preferably:

1. inverse `X`-adic descent with depth growing through the whole positive-credit
   return word and coupled to exact closure;
2. regeneration of the actual expanding exit;
3. global exclusion of the doubly-exponential nonpositive branch.