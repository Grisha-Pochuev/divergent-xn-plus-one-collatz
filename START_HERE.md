# START HERE

Compact entry point for each research session.

## Strict target

Find explicit positive odd integers `X>=5,n0` such that

```text
C_X(n)=(X*n+1)/2^v2(X*n+1)
```

tends to positive infinity. A cycle, avoidance of `1`, a finite barrier, a huge
finite trajectory, or heuristic drift is not a solution.

## Read first

```text
START_HERE.md
docs/WORKING_PROTOCOL.md
docs/CURRENT_STATUS.md
docs/RETRACTIONS.md
docs/SESSION_CHECKPOINT_2026-07-13_GEOMETRIC_FACTOR_PERSISTENCE_NO_GO.md
```

Fetch these files from the current default branch at the start of every session.
GitHub commits and certificate scripts are the durable source of truth. If an
in-chat summary or an older checkpoint conflicts with current `main`, current
`main` wins.

## One-chat research sprint

A broad request such as `continue solving` authorizes one substantial research
sprint. Choose the route with the best apparent chance of advancing the strict
target. Literature, alternative candidates, symbolic algebra, exact arithmetic,
SAT/SMT, theorem provers, residue graphs, and small or medium exact searches are
allowed.

Aim for one main deliverable:

1. a proved lemma advancing a proof gate;
2. a decisive refutation of an approach;
3. a verified computational certificate with mathematical meaning;
4. a literature result that materially changes strategy after independent audit;
5. a precise obstruction and next exact experiment when no theorem is reached.

Work until one deliverable is reached or the chosen route is rigorously shown to
fail. Verify independently where practical, commit immediately, and distinguish
theorem, finite certificate, evidence, and open target. Do not merely enlarge a
finite trajectory or numerical barrier.

## Primary candidate

```text
N=2^500-1,
B=2^4501,
d=349*2^500-347=2+349*N,
X=B-d=2^4501-349*2^500+347,
n0=1.
```

Proof gates:

```text
G1 explicit pair: closed;
G2 leaves 1 and never returns: closed;
G3 every nontrivial positive cycle excluded: open;
G4 bounded positive orbit implies eventual cycle: closed;
G5 final independent certificate: waits for G3.
```

## Main retained arithmetic structure

- `N|X` and `1093||X`;
- the orbit leaves `1` and never returns;
- exactly `16562000` permanent classes survive modulo `N*1093^2`;
- every cycle value is greater than `N`;
- every exceptional source has at least `1505` decimal digits;
- every cycle length through a number between `10^1201` and `10^1202` is
  impossible;
- the harmonic and full `X`-adic bounds remain available.

## Global ordinary-block frontier

Every hypothetical nontrivial positive cycle has at least

```text
245833 ordinary complete blocks.
```

This allows arbitrary exceptional-block populations and block lengths. It is not
a cycle-length cutoff. Under the contrary assumption of at most `245832`
ordinary blocks, the exact signed closure argument gives

```text
p<=544026748963771<10^15,
```

contradicting the retained height barrier.

Files:

```text
docs/GLOBAL_ORDINARY_BLOCK_COUNT_FRONTIER.md
tools/verify_global_ordinary_block_count_frontier.py
```

## Minimum-boundary expanding segment and return dichotomy

The minimum-boundary construction gives one actual consecutive expanding orbit
segment with

```text
1<=net credit C<=4500;
exceptional excess sum <=4499;
number of complete blocks <=4500;
L*log2(B/X)<C;
endpoint y>x.
```

A related bounded positive circulation has

```text
q<=4500,
1<=C<=20250000,
T<=20254499.
```

For the remaining actual return from `y` to the least ordinary boundary `x`, let
`R` be its net credit and `Lr` its accelerated length. Then

```text
R>=1 => Lr>2^3990;
R<=0 => Lr>2^(2^974).
```

The nonpositive result uses the permanent `16562000`-class sieve, harmonic
packing, a correction bound below `2^-4023`, and a one-sided continued-fraction
gap.

Files:

```text
docs/MINIMUM_BOUNDARY_POSITIVE_CIRCULATION.md
tools/verify_minimum_boundary_positive_circulation.py
docs/MINIMUM_BOUNDARY_ACTUAL_EXPANDING_SEGMENT.md
tools/verify_minimum_boundary_actual_expanding_segment.py
docs/MINIMUM_BOUNDARY_RETURN_CREDIT_DICHOTOMY.md
tools/verify_minimum_boundary_return_credit_dichotomy.py
docs/MINIMUM_BOUNDARY_NONPOSITIVE_RETURN_HARMONIC_BARRIER.md
tools/verify_minimum_boundary_nonpositive_return_harmonic_barrier.py
```

## Endpoint-congruence no-go results

Every prescribed finite incoming word and every prescribed finite outgoing word
are compatible at infinitely many positive odd boundaries by exact word coding
and the Chinese remainder theorem. This remains true when incoming `X`-adic
depth grows with the full finite return word.

Therefore fixed endpoint classes, including the entire finite incoming endpoint
class, cannot alone exclude a return. Exact source matching is the missing
global condition.

Files:

```text
docs/FIXED_LOCAL_ENDPOINT_CONGRUENCE_NO_GO.md
tools/verify_fixed_local_endpoint_congruence_no_go.py
docs/FULL_FINITE_TWO_SIDED_WORD_GLUING_NO_GO.md
tools/verify_full_finite_two_sided_word_gluing_no_go.py
```

## Exact cyclic closure

For a complete cyclic valuation word `U=(a_0,...,a_(p-1))`, total valuation `A`,
cyclic rotations `U_k`, and affine numerators `Q_k`, put

```text
Delta=2^A-X^p.
```

Exact algebra gives

```text
2^a_k*Q_(k+1)=X*Q_k+Delta.
```

The word closes to an actual positive accelerated cycle if and only if

```text
Delta>0 and Delta|Q_0.
```

Equivalently,

```text
gcd(Q_k,Q_(k+1))=Delta
```

for one, hence every, truly adjacent cyclic pair. Also

```text
gcd(Q_0,...,Q_(p-1))=gcd(Q_0,Delta).
```

Files:

```text
docs/CYCLIC_ROTATION_CLOSURE_GCD.md
tools/verify_cyclic_rotation_closure_gcd.py
```

## Complete-block gcd compression no-go

For a complete near-power block of length `ell`, put

```text
S_ell=(B^ell-X^ell)/d.
```

If `n` and `n'` are its exact source and endpoint, then

```text
gcd(n,n')=gcd(n,S_ell).
```

For block-boundary cyclic numerators,

```text
gcd(Q_i,Q_j)=gcd(Q_i,Delta*S_ell).
```

If the full word closes, this becomes

```text
gcd(Q_i,Q_j)=Delta*gcd(n_i,S_ell).
```

Local word coding and CRT produce infinitely many exact positive complete blocks
with the full extra factor. The regression is

```text
X=5: 91 -> 57 -> 143, gcd(91,143)=13.
```

Thus naive compression of a whole block to one boundary edge loses the sharp
adjacent coprimality.

Files:

```text
docs/COMPLETE_BLOCK_GCD_COMPRESSION_NO_GO.md
tools/verify_complete_block_gcd_compression_no_go.py
```

## Geometric-factor strong divisibility and persistence no-go

The geometric factors form a strong divisibility sequence:

```text
gcd(S_r,S_s)=S_gcd(r,s).
```

They also satisfy

```text
gcd(S_ell,B*X)=1,
gcd(S_ell,d)=gcd(ell,d).
```

Hence primes common to several block-boundary defects are controlled by the gcd
of the corresponding block lengths. In particular, block lengths with gcd `1`
have no common defect prime.

This does not give a local proof. For any finite prescribed list of complete
blocks whose lengths have common divisor `h>=2`, any odd prime `q|S_h` can be
forced by exact word coding and CRT to divide every block boundary. The explicit
regression is

```text
X=5,
lengths=(2,4,6),
q=13,
boundaries=
2620090395 -> 4093891243 -> 1249356459 -> 297869793,
boundary gcd defects=(13,13,39).
```

Thus repeated local block compression need not wash out the extra gcd, no matter
how many finite blocks are prescribed.

For the primary candidate,

```text
gcd(S_ell,N*1093^2)=1
```

for every `ell`. The geometric defect has no prime from the permanent-sieve
modulus; any useful interaction with that sieve must use actual source classes,
not direct factor overlap.

Files:

```text
docs/GEOMETRIC_FACTOR_STRONG_DIVISIBILITY_PERSISTENCE_NO_GO.md
tools/verify_geometric_factor_strong_divisibility.py
```

## Decisive missing theorem

A hypothetical cycle can return only through one of two extreme branches:

```text
positive return credit with Lr>2^3990;
nonpositive return credit with Lr>2^(2^974).
```

Fixed-depth endpoint congruences, full finite two-sided word gluing, naive
complete-block gcd compression, and the claim that repeated local compression
must remove defect primes are closed.

The primary next target is genuinely global. Prove one of:

1. a strategically selected family of actual cycle block lengths has gcd `1`,
   so no prime can persist in every corresponding geometric defect;
2. the return word, minimum-boundary constraints, or permanent-sieve classes
   exclude every prime divisor of `S_gcd(lengths)` at the actual boundaries;
3. some truly adjacent accelerated cyclic numerator pair has gcd smaller than
   `Delta`;
4. the expanding exit regenerates as a repeatable growing segment;
5. the doubly-exponential nonpositive branch is globally impossible;
6. a different candidate or invariant gives a direct divergence proof.

Do not merely extend a continued-fraction denominator, finite trajectory, finite
return-length barrier, endpoint modulus, or locally concatenated block list
without new closure information.

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
and an arbitrarily large finite barrier. Increasing parameters alone is not a
priority.

## Non-negotiable corrections

Do not use

```text
2^A==1 (mod X).
```

The correct cycle congruence is

```text
2^A*product_i(n_i)==1 (mod X).
```

Do not identify a least admissible predecessor source with the source actually
used by a cycle. Do not present a finite computation as divergence.

## Verification discipline

- commit each theorem, checker, decisive refutation, and major strategy change;
- state exactly which checks ran;
- do not claim a complete repository run unless it completed;
- compare every proposed result with current `main` before calling it new;
- preserve failed approaches when their failure prevents repetition.

## Reproduction

The general check entry point is

```text
python run_checks.py
```

For the current frontier specifically run

```text
python tools/verify_geometric_factor_strong_divisibility.py
python tools/check_project_consistency.py
```
