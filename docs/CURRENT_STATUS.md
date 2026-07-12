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
lengths. It is not a trajectory or cycle-length cutoff. If the ordinary-block
count were at most `245832`, the exact signed closure argument would force

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
produces a functional graph on at most `4500` types. One directed cycle gives
disjoint orbit intervals satisfying

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
and follow the actual orbit to the next such boundary. Exact minimum-height
comparison gives

```text
1<=C<=4500,
exceptional excess sum F<=4499,
number of complete blocks <=4500.
```

The exact continued-fraction gap is greater than `2^-4023`, while the total
additive correction is less than `2^-4023`. Therefore

```text
L*delta<C,
2^C*(X/B)^L>1,
endpoint y>starting value x.
```

This is one actual consecutive orbit segment, not a formal splice.

Files:

```text
docs/MINIMUM_BOUNDARY_ACTUAL_EXPANDING_SEGMENT.md
tools/verify_minimum_boundary_actual_expanding_segment.py
```

## Actual return frontiers

Follow the remaining actual orbit from `y` back to `x`. Let

```text
R=ordinary-deficit sum-exceptional-excess sum,
Lr=accelerated return length.
```

The exact return ratio proves

```text
R>=1 => Lr>2^3990.
```

If `R<=0`, then total cycle credit satisfies `1<=D<=4500`. The permanent
`16562000`-class sieve, harmonic packing, the expanding-exit correction, and a
one-sided continued-fraction gap give

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

Every prescribed incoming ordinary or exceptional complete block can be
followed by every prescribed finite outgoing valuation word at infinitely many
positive odd boundaries. The stronger theorem allows the entire finite incoming
word. The incoming endpoint condition is one class modulo `X^r`, while the
outgoing word fixes one odd class modulo a power of two; the moduli are coprime.

Therefore fixed-depth endpoint data and full finite incoming endpoint data cannot
alone exclude a return. Exact source matching remains global.

The checker verifies `1536` small exact gluings, six primary-multiplier gluings,
and the known `5n+1` cycle `13 -> 33 -> 83 -> 13`.

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

let `U_k` be its cyclic rotations and `Q_k` their affine numerators. Exact
algebra gives

```text
2^a_k*Q_(k+1)=X*Q_k+Delta.                         (1)
```

Consequently

```text
gcd(Q_0,...,Q_(p-1))=gcd(Q_0,Delta),               (2)
gcd(Q_k,Q_(k+1))=gcd(Q_k,Delta).                   (3)
```

The word closes to a positive accelerated cycle if and only if

```text
Delta>0 and Delta|Q_0.                              (4)
```

Equivalently,

```text
gcd(Q_k,Q_(k+1))=Delta                             (5)
```

for one, hence every, truly adjacent pair. In a closing word `n_k=Q_k/Delta`.
All primary-candidate rotations obey

```text
Q_k>Delta*(2^500-1).
```

Files:

```text
docs/CYCLIC_ROTATION_CLOSURE_GCD.md
tools/verify_cyclic_rotation_closure_gcd.py
```

The standalone verifier checks `6820` exhaustive small words, reconstructs `17`
closing words in that grid, verifies three known `5n+1` cycles, and checks three
large exact words for the primary multiplier.

## Complete-block gcd compression no-go

For a complete near-power block

```text
W=(m,...,m,a), a!=m,
S_ell=(B^ell-X^ell)/d,
```

the affine constant is `S_ell`, independently of the terminal valuation. Every
exact block from source `n` to endpoint `n'` satisfies

```text
2^A_W*n'=X^ell*n+S_ell,
gcd(n,n')=gcd(n,S_ell).                              (6)
```

For cyclic numerators at the two block boundaries,

```text
2^A_W*Q_j=X^ell*Q_i+Delta*S_ell,
gcd(Q_i,Q_j)=gcd(Q_i,Delta*S_ell).                  (7)
```

If the full word closes, then

```text
gcd(Q_i,Q_j)=Delta*gcd(n_i,S_ell).                  (8)
```

Exact word coding and CRT produce infinitely many exact positive complete blocks
with the entire extra geometric factor. For `ell>=2`, `S_ell>X^(ell-1)`. The
regression is

```text
X=5,
91 --a=3--> 57 --a=1--> 143,
gcd(91,143)=13=(8^2-5^2)/3.
```

Thus block boundaries cannot replace a truly adjacent accelerated pair without
new global coprimality information.

Files:

```text
docs/COMPLETE_BLOCK_GCD_COMPRESSION_NO_GO.md
tools/verify_complete_block_gcd_compression_no_go.py
```

The standalone checker verifies

```text
13212 exact block lifts;
3303 full geometric-factor CRT blocks;
7056 cyclic compression cases;
8 closing cyclic cases;
the regression 91 -> 57 -> 143.
```

## Geometric-factor strong divisibility and persistence no-go

For

```text
S_ell=(B^ell-X^ell)/d,
B=2^m,
X=B-d,
```

the geometric factors satisfy the exact strong-divisibility law

```text
gcd(S_r,S_s)=S_gcd(r,s).                            (9)
```

They also obey

```text
S_ell is odd,
gcd(S_ell,B*X)=1,
gcd(S_ell,d)=gcd(ell,d).                             (10)
```

For block-boundary defects

```text
g_i=gcd(n_i,n_(i+1))=gcd(n_i,S_(ell_i)),
```

any common prime is therefore controlled by the gcd of the corresponding block
lengths. If selected lengths have gcd `1`, their defects share no prime.

However, this does not yield a local cycle obstruction. Given any finite list of
complete blocks whose lengths have common divisor `h>=2`, choose any odd prime
`q|S_h`. Exact valuation-word coding and CRT give infinitely many positive odd
starts for which `q` divides every block boundary. Hence the same defect prime
can survive through arbitrarily many prescribed finite complete-block
compressions.

Explicit regression:

```text
X=5,
lengths=(2,4,6),
q=13,
n0=2620090395,
boundaries=
2620090395 -> 4093891243 -> 1249356459 -> 297869793,
boundary gcd defects=(13,13,39).
```

This closes the local shortcut that repeated block compression must eventually
recover adjacent coprimality.

For the primary candidate,

```text
gcd(S_ell,N*1093^2)=1                              (11)
```

for every `ell`. Thus no geometric defect prime lies in the prime support of the
permanent sieve modulus. Any useful sieve interaction must use the actual source
classes, not direct factor overlap.

Files:

```text
docs/GEOMETRIC_FACTOR_STRONG_DIVISIBILITY_PERSISTENCE_NO_GO.md
tools/verify_geometric_factor_strong_divisibility.py
```

The standalone checker verifies

```text
71136 strong-divisibility pair cases;
1990 exact complete blocks;
116 persistent-boundary CRT constructions;
24 primary-candidate lengths;
the explicit X=5 three-block regression.
```

An independent brute-force check verified unique exact word residues in `30`
small cases. A complete repository-wide run was not executed.

## Exact closure target

Let `W` be the expanding exit word from `x` to `y`, and `V` the remaining return
word from `y` to `x`. If

```text
2^A_W*y=X^t*x+Q_W,
2^A_V*x=X^r*y+Q_V,
```

then exact elimination gives

```text
[2^(A_W+A_V)-X^(t+r)]*x
  =X^r*Q_W+2^A_W*Q_V.
```

The cyclic-gcd theorem identifies the left coefficient with `Delta` and the
right side with the cyclic affine numerator. Closure remains equivalent to

```text
gcd(Q_k,Q_(k+1))=Delta
```

for truly adjacent cyclic numerators.

## Decisive missing theorem

A hypothetical cycle can survive only through

```text
positive credit with Lr>2^3990;
nonpositive credit with Lr>2^(2^974).
```

The primary remaining routes are now:

1. use actual return or sieve constraints to force a selected family of actual
   complete-block lengths to have gcd `1`;
2. exclude every prime divisor of `S_gcd(lengths)` from the corresponding actual
   cycle boundaries;
3. prove that some truly adjacent cyclic numerator gcd is smaller than `Delta`;
4. prove regeneration of the actual expanding exit into a repeatable growing
   segment;
5. globally exclude the doubly-exponential nonpositive branch;
6. find a different candidate or invariant giving direct divergence.

Further numerical barriers, longer continued-fraction prefixes, higher endpoint
moduli, naive block-boundary gcd calculations, and arbitrary finite block
concatenations without new closure information are not the priority.

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

The current standalone commands are

```text
python tools/verify_geometric_factor_strong_divisibility.py
python tools/check_project_consistency.py
```

The new verifier passed in the chat environment. The project-wide `run_checks.py`
was updated to include it, but a complete repository-wide run was not executed.
