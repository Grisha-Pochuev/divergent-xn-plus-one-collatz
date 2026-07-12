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

Let `J` be the number of ordinary complete blocks in a hypothetical cycle.
Signed elimination of all block cores gives upper bounds for the positive cycle
gap after all exceptional terms are discarded. The exact continued-fraction
gap then proves:

```text
Every hypothetical nontrivial positive cycle contains at least
245833 ordinary complete blocks.
```

This allows arbitrary exceptional-block populations and arbitrary block lengths.
It is not a finite trajectory or cycle-length cutoff.

If `J<=245832`, the proof forces

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

## Minimum-boundary positive circulation

For every occurring ordinary deficit type `e`, choose the smallest cycle
boundary value `x_e` of that type. Follow the actual orbit to the next ordinary
boundary of type `f(e)` and value `y_e`. Then

```text
y_e>=x_(f(e)).
```

The functional graph on at most `4500` types contains a directed cycle. The
selected disjoint orbit intervals have actual height product at least `1`.
Writing `C` for their total net credit, `L` for total accelerated length, and
`T` for the number of selected complete blocks, exact estimates prove

```text
q<=4500,
1<=C<=20250000,
T<=20254499,
L*delta<C,
delta=log2(B/X).
```

Thus their formal base multiplier is strictly expanding:

```text
2^C*(X/B)^L>1.
```

The proof is global, not experimental. If `L*delta>C`, the one-sided
continued-fraction theorem gives a natural-log gap greater than `2^-4023`, while
the total selected additive correction is less than `2^-4023`, a contradiction.
Equality is impossible because `X^L` is odd and cannot be a power of two.

Files:

```text
docs/MINIMUM_BOUNDARY_POSITIVE_CIRCULATION.md
tools/verify_minimum_boundary_positive_circulation.py
```

## Decisive missing theorem

The selected intervals form an expanding circulation of boundary types, but
need not be consecutive in the original orbit. An endpoint and the next selected
start have the same ordinary boundary class modulo `X`, yet may be different
integers and may lie in different two-adic word cylinders.

The next target is a splicing or regeneration theorem proving one of:

1. the intervals concatenate into an admissible growing orbit segment;
2. every nonzero mismatch forces strict height descent;
3. the mismatch is impossible after lifting the boundary equation modulo `X^2`
   or a higher power.

Further finite barriers or longer continued-fraction prefixes are not the
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