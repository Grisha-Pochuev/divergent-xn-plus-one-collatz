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
and follow the actual orbit to the next such boundary. If the segment has total
credit `C`, length `L`, and exceptional excess sum `F`, exact minimum-height
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

## Actual return frontiers

Follow the remaining actual orbit from `y` back to `x`. Let

```text
R = ordinary-deficit sum - exceptional-excess sum,
Lr = accelerated return length.
```

The exact return ratio proves

```text
R>=1 => Lr>2^3990.
```

If `R<=0`, then total cycle credit satisfies `1<=D<=4500`. The one-sided
continued-fraction certificate forces a gap greater than `2^-4023`, while the
permanent `16562000`-class sieve and harmonic packing make the total correction
too small through a double-exponential frontier. Hence

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
docs/MINIMUM_BOUNDARY_RETURN_CREDIT_DICHOTOMY.md
tools/verify_minimum_boundary_return_credit_dichotomy.py
docs/MINIMUM_BOUNDARY_NONPOSITIVE_RETURN_HARMONIC_BARRIER.md
tools/verify_minimum_boundary_nonpositive_return_harmonic_barrier.py
```

## Endpoint-congruence routes closed

The fixed local theorem shows that every prescribed incoming ordinary or
exceptional complete block is compatible with every prescribed finite outgoing
valuation word at infinitely many positive odd boundaries.

The stronger theorem allows an arbitrary entire finite incoming word `V`. Its
endpoint condition is one class modulo

```text
X^len(V),
```

whereas an arbitrary finite outgoing word `W` fixes one odd class modulo

```text
2^(sum(W)+1).
```

The moduli are coprime, so the Chinese remainder theorem constructs infinitely
many positive odd boundaries realizing both words exactly. This remains true
when the incoming `X`-adic depth grows with the complete finite return word and
after any fixed finite lower height bound.

Therefore neither fixed-depth endpoint data nor the full finite incoming
endpoint residue can itself exclude a return. The checker verifies `1536` small
exact gluings, six gluings for the primary multiplier, and the known accelerated
`5n+1` cycle `13 -> 33 -> 83 -> 13`.

Files:

```text
docs/FIXED_LOCAL_ENDPOINT_CONGRUENCE_NO_GO.md
tools/verify_fixed_local_endpoint_congruence_no_go.py
docs/FULL_FINITE_TWO_SIDED_WORD_GLUING_NO_GO.md
tools/verify_full_finite_two_sided_word_gluing_no_go.py
```

## Cyclic-rotation closure gcd theorem

For a complete positive valuation word

```text
U=(a_0,...,a_(p-1)),
A=sum_i a_i,
Delta=2^A-X^p,
```

let `U_k` be its cyclic rotation starting at `a_k`, and let `Q_k` be the standard
affine numerator of `U_k`. Exact algebra gives

```text
2^a_k*Q_(k+1)=X*Q_k+Delta.                         (1)
```

Consequently, for every positive word, whether or not it closes,

```text
gcd(Q_0,...,Q_(p-1))=gcd(Q_0,Delta),               (2)
gcd(Q_k,Q_(k+1))=gcd(Q_k,Delta).                   (3)
```

The word is the exact valuation word of a positive accelerated cycle if and only
if

```text
Delta>0 and Delta|Q_0.                              (4)
```

Equivalently,

```text
gcd(Q_k,Q_(k+1))=Delta                             (5)
```

for one, hence every, adjacent pair. In a closing word the cycle states are

```text
n_k=Q_k/Delta.
```

Thus all minimum-boundary comparisons become comparisons among the cyclic
numerators. For the actual expanding exit, the numerator at the next ordinary
boundary is strictly larger than the numerator at the least ordinary boundary.
Every primary-candidate cycle word must also obey

```text
Q_k>Delta*(2^500-1)
```

for every rotation.

For a split `U=W followed by V`, the concatenation identity

```text
Q(U)=X^r*Q_W+2^A_W*Q_V
```

shows that (4) is exactly the previous source-matching equation. Local CRT
compatibility does not supply this full common divisor.

Files:

```text
docs/CYCLIC_ROTATION_CLOSURE_GCD.md
tools/verify_cyclic_rotation_closure_gcd.py
```

The standalone verifier checks `6820` exhaustive small words, reconstructs `17`
closing words in that grid, verifies three known `5n+1` cycles, and checks three
large exact words for the primary multiplier.

## Exact closure target

Let `W` be the expanding exit word from `x` to `y`, and let `V` be the remaining
return word from `y` to `x`. Define their exact affine constants by

```text
2^A_W*y=X^t*x+Q_W,
2^A_V*x=X^r*y+Q_V.
```

Eliminating `y` gives

```text
[2^(A_W+A_V)-X^(t+r)]*x
  =X^r*Q_W+2^A_W*Q_V.
```

The cyclic-gcd theorem identifies the left coefficient with `Delta` and the
right numerator with `Q(U)`. Exact cycle closure is equivalent to

```text
gcd(Q_k,Q_(k+1))=Delta
```

for adjacent cyclic numerators. A successful whole-return argument must prove
that this maximal gcd cannot occur under the minimum-boundary, block-credit, and
return-length constraints.

## Decisive missing theorem

A hypothetical cycle can survive only through one of the following actual
return branches:

```text
positive credit with Lr>2^3990;
nonpositive credit with Lr>2^(2^974).
```

The primary remaining routes are:

1. prove that every admissible complete cyclic word has some adjacent numerator
   gcd strictly smaller than `Delta` under the positive-return and
   minimum-boundary constraints;
2. prove regeneration of the expanding exit into a repeatable growing segment;
3. globally exclude the nonpositive branch beyond its double-exponential
   frontier;
4. find a different candidate or invariant giving a direct divergence proof.

Further numerical barriers, longer continued-fraction prefixes, and endpoint
classes modulo higher powers of `X` without new closure information are not the
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
python tools/verify_cyclic_rotation_closure_gcd.py
```

passed in the chat environment and is included in `run_checks.py`. A complete
repository-wide run had not yet been executed at the time this status was
written.
