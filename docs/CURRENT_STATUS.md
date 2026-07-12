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
endpoint y > starting value x.
```

This is an actual consecutive orbit segment, not a formal splice.

Files:

```text
docs/MINIMUM_BOUNDARY_ACTUAL_EXPANDING_SEGMENT.md
tools/verify_minimum_boundary_actual_expanding_segment.py
```

## Return-credit dichotomy

Follow the remaining actual orbit from `y` back to `x`. Let

```text
R = ordinary-deficit sum - exceptional-excess sum,
Lr = accelerated return length.
```

The exact return ratio and

```text
log2(B/X)<2^-3990
```

prove

```text
R>=1 => Lr>2^3990;
Lr<=2^3990 => R<=0.
```

Files:

```text
docs/MINIMUM_BOUNDARY_RETURN_CREDIT_DICHOTOMY.md
tools/verify_minimum_boundary_return_credit_dichotomy.py
```

## Nonpositive-return harmonic barrier

If `R<=0`, then the total cycle credit is

```text
1<=D=C+R<=4500.
```

The one-sided continued-fraction certificate forces the full natural-logarithmic
cycle gap to exceed `2^-4023`. On the other hand, the permanent `16562000`-class
sieve and harmonic packing of the distinct return values show that every return
with

```text
Lr<=2^(2^974)
```

has return correction below `2^-4024`. The independent correction bound for the
short expanding exit is also below `2^-4024`. Their sum is below `2^-4023`, a
contradiction. Therefore

```text
R<=0 => Lr>2^(2^974).
```

The exact checker obtains

```text
correction upper * 2^4023 = 0.433233945702880...,
gap lower        * 2^4023 = 1.718676385119249....
```

Files:

```text
docs/MINIMUM_BOUNDARY_NONPOSITIVE_RETURN_HARMONIC_BARRIER.md
tools/verify_minimum_boundary_nonpositive_return_harmonic_barrier.py
```

## Decisive missing theorem

A hypothetical cycle can now survive only through one of the following actual
return branches:

```text
positive credit with Lr>2^3990;
nonpositive credit with Lr>2^(2^974).
```

The primary target is a length-independent return obstruction based on one of:

1. inverse `X`-adic descent through a positive-credit return word;
2. endpoint incompatibility modulo `X^2` or a higher power;
3. regeneration of the expanding exit into a repeatable growing segment;
4. a global exclusion of the doubly-exponential nonpositive branch.

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

The standalone checker

```text
python tools/verify_minimum_boundary_nonpositive_return_harmonic_barrier.py
```

passed in the chat environment. Both return checkers are included in
`run_checks.py`. A complete repository-wide run was not executed.