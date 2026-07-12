# Current status

## Strict target

Find explicit positive odd `X>=5,n0` such that

```text
C_X(n)=(X*n+1)/2^v2(X*n+1)
```

tends to positive infinity. The strict problem remains open.

## Primary candidate

```text
N=2^500-1,
B=2^4501,
d=349*2^500-347,
X=B-d=2^4501-349*2^500+347,
n0=1.
```

Proof gates:

```text
G1 explicit pair: closed;
G2 leaves 1 and never returns: closed;
G3 every nontrivial positive cycle excluded: open;
G4 bounded positive orbit implies eventual cycle: closed;
G5 final certificate: waits for G3.
```

## Retained arithmetic structure

- `N|X` and `1093||X`;
- the orbit from `1` leaves `1` and never returns;
- the combined permanent sieve leaves `16562000` classes modulo `N*1093^2`;
- every cycle value is greater than `N`;
- every exceptional source has at least `1505` decimal digits;
- every cycle length through a number between `10^1201` and `10^1202` is
  impossible;
- the harmonic and full `X`-adic bounds remain available.

## Global ordinary-block frontier

Every hypothetical nontrivial positive cycle contains at least

```text
245833 ordinary complete blocks.
```

This permits arbitrary exceptional-block populations and arbitrary block
lengths. It is not a trajectory or cycle-length cutoff.

The exact signed closure proof shows that if the ordinary-block count were at
most `245832`, then

```text
every ordinary block length <=2J+6;
every exceptional block length <=2J+5;
number of exceptional blocks <=4500J-1;
p<=544026748963771<10^15,
```

contradicting `p>10^1201`.

Files:

```text
docs/GLOBAL_ORDINARY_BLOCK_COUNT_FRONTIER.md
tools/verify_global_ordinary_block_count_frontier.py
```

## Bounded positive circulation

Choosing the smallest cycle boundary in every occurring ordinary deficit type
produces a functional graph on at most `4500` types. One directed cycle in that
graph gives disjoint orbit intervals satisfying

```text
q<=4500,
1<=C<=20250000,
T<=20254499,
L*delta<C,
delta=log2(B/X).
```

Their formal base multiplier is strictly expanding:

```text
2^C*(X/B)^L>1.
```

Files:

```text
docs/MINIMUM_BOUNDARY_POSITIVE_CIRCULATION.md
tools/verify_minimum_boundary_positive_circulation.py
```

## Actual minimum-boundary expanding segment

Choose the least cycle value immediately following an ordinary complete block
and follow the actual orbit to the next such value. If the segment has total
credit `C`, length `L`, and exceptional excess sum `F`, then exact minimum-height
comparison gives

```text
1<=C<=4500,
F<=4499,
number of complete blocks <=4500.
```

If its base multiplier were nonexpanding, the exact continued-fraction gap would
be greater than `2^-4023`, while the sum of every additive block correction is
less than `2^-4023`. Therefore

```text
L*delta<C,
2^C*(X/B)^L>1,
endpoint > starting value.
```

This is an actual consecutive orbit segment, not a formal splice.

Files:

```text
docs/MINIMUM_BOUNDARY_ACTUAL_EXPANDING_SEGMENT.md
tools/verify_minimum_boundary_actual_expanding_segment.py
```

## Decisive missing theorem

The remaining part of a hypothetical cycle must return from the larger endpoint
of this short expanding segment to the least ordinary boundary.

The primary target is a return obstruction based on one of:

1. inverse `X`-adic descent through the return word;
2. the endpoint classes modulo `X`, `1093^2`, or `X^2`;
3. a mandatory exceptional-credit lower bound incompatible with the harmonic
   correction window;
4. regeneration of the expanding word into a repeatable growing segment.

Further numerical barriers or longer continued-fraction prefixes are not the
priority.

## Reusable family theorem

For

```text
N=2^k-1,
m==r (mod k),
d=2^r+t*N,
X=2^m-d,
```

with `364` not dividing `k`, one can choose parity-correct `t<2*1093^2` with
`1093||X`. This gives no return to `1`, an exponentially thin permanent sieve,
and an arbitrarily large finite barrier.

## Retractions

Do not use

```text
2^A==1 (mod X).
```

The correct cycle congruence is

```text
2^A*product_i(n_i)==1 (mod X).
```

Do not identify a least admissible predecessor source with the source actually
used by a cycle.

## Verification

The new standalone checkers passed in the chat environment and are included in
`run_checks.py`. A complete repository-wide run was not executed.