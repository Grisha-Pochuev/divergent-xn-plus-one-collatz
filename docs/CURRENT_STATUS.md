# Current status

Authoritative summary of the active mathematical frontier. Detailed proofs live
in the linked theorem files and exact checkers.

## Strict target and candidate

Find explicit positive odd `X>=5,n0` such that

```text
C_X(n)=(X*n+1)/2^v2(X*n+1)
```

tends to positive infinity. The strict problem remains open.

Primary candidate:

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

## Retained global structure

- `N|X` and `1093||X`;
- `16562000` permanent classes survive modulo `N*1093^2`;
- every cycle value is greater than `N`;
- every exceptional source has at least `1505` decimal digits;
- the cycle window through `[10^1201,10^1202]` is impossible;
- every hypothetical cycle has at least `245833` ordinary complete blocks.

## Minimum-boundary exit and return

Every hypothetical cycle contains an actual consecutive expanding exit from its
least ordinary boundary `x` to the next ordinary boundary `y>x` with

```text
1<=C<=4500,
exceptional excess<=4499,
complete blocks<=4500,
L_exit*log2(B/X)<C,
L_exit<2^4006.
```

Write `R` for the credit of the remaining actual return from `y` to `x`. The
retained dichotomy gives

```text
R>=1 => L_return>2^3990,
R<=0 => L_return>2^(2^974).
```

Sources:

```text
docs/MINIMUM_BOUNDARY_ACTUAL_EXPANDING_SEGMENT.md
docs/MINIMUM_BOUNDARY_RETURN_CREDIT_DICHOTOMY.md
docs/MINIMUM_BOUNDARY_NONPOSITIVE_RETURN_HARMONIC_BARRIER.md
```

## New theorem: every nonpositive return is impossible

For any near-power multiplier

```text
B=2^m,
X=B-d,
0<d<B/2,
```

partition a hypothetical positive cycle into complete blocks. If `p` is its
accelerated length and

```text
D=m*p-A
```

is its total credit, the exact block-correction identity and a uniform correction
bound prove

```text
p < 2*D*B*X/[d*(X-d)].
```

The proof uses

```text
sum_j ln(1+q_j)=p*ln(B/X)-D*ln(2),
0<q_j<ell_j*d/(2*X^ell_j),
sum_j ell_j=p,
ln(B/X)>d/B.
```

On a nonpositive return,

```text
D=C+R,
1<=D<=4500.
```

For the primary candidate exact integer arithmetic gives

```text
2*4500*B*X < 2^4006*d*(X-d),
```

hence

```text
p<2^4006.
```

But the retained return theorem gives

```text
p>L_return>2^(2^974)>2^4006.
```

Contradiction. Therefore

```text
R<=0 is impossible.
```

Sources:

```text
docs/NONPOSITIVE_RETURN_BLOCK_CORRECTION_EXCLUSION.md
tools/verify_nonpositive_return_block_correction_exclusion.py
```

This closes both former nonpositive subdivisions `h=1` and `h>=2`. The earlier
phase-sieve, block-explosion, and repeated-type theorems remain valid conditional
theorems, but their common hypothesis now cannot occur in a positive cycle.

## Only surviving return branch

Every hypothetical nontrivial positive cycle must now satisfy

```text
R>=1,
L_return>2^3990.
```

Thus G3 has been reduced to one branch: exclude an actual positive-credit return
from `y>x` to the least ordinary boundary `x`.

The total cycle credit is

```text
D=C+R>=2,
```

but it is no longer uniformly bounded by `4500`, so the new length upper bound
does not by itself exclude this branch.

## Exact cyclic closure and closed local routes

For a cyclic valuation word and its rotated affine numerators `Q_k`,

```text
Delta=2^A-X^p,
2^a_k*Q_(k+1)=X*Q_k+Delta.
```

The word closes to a positive cycle iff `Delta>0` and `Delta|Q_0`. Equivalently,
a truly adjacent pair satisfies

```text
gcd(Q_k,Q_(k+1))=Delta.
```

For complete blocks,

```text
S_ell=(B^ell-X^ell)/d,
gcd(n,n')=gcd(n,S_ell),
gcd(S_r,S_s)=S_gcd(r,s).
```

Fixed local endpoint congruences, finite two-sided word gluing, naive block
compression, finite repeated-defect persistence, arbitrary finite same-deficit
runs, and any fixed finite `N`-adic depth do not force exact cyclic source
matching; exact valuation-word coding and CRT realize those local constraints at
infinitely many positive starts.

Sources:

```text
docs/CYCLIC_ROTATION_CLOSURE_GCD.md
docs/FIXED_LOCAL_ENDPOINT_CONGRUENCE_NO_GO.md
docs/FULL_FINITE_TWO_SIDED_WORD_GLUING_NO_GO.md
docs/COMPLETE_BLOCK_GCD_COMPRESSION_NO_GO.md
docs/GEOMETRIC_FACTOR_STRONG_DIVISIBILITY_PERSISTENCE_NO_GO.md
docs/SAME_DEFICIT_FINITE_PERSISTENCE_NO_GO.md
```

## Retained global block-gcd identity

Let `ell_i` be all complete-block lengths of a hypothetical cycle and put

```text
h=gcd_i ell_i,
D=sum_i(4501-a_i),
S_h=(B^h-X^h)/d,
g=gcd of all complete-block boundaries b_i.
```

Exact cyclic closure proves

```text
g=gcd(b_i,S_h) for every b_i,
S_h/g divides 2^D-1,
S_h/gcd(S_h,2^D-1) divides g divides S_h,
n_t==B^(-j)*S_j (mod g),  j=t mod h.
```

These identities remain available on the positive-credit branch. The former
strong `h>=2` harmonic consequences used the now-impossible small-credit range
`1<=D<=4500` and should not be applied unchanged when `R>=1`.

Sources:

```text
docs/GLOBAL_BLOCK_GCD_PHASE_SIEVE.md
tools/verify_global_block_gcd_phase_sieve.py
```

## Decisive next target

Exclude the positive-credit return. The strongest current routes are:

1. combine the segment equation

   ```text
   ln(x/y)=R*ln(2)-L_return*ln(B/X)+K_return<0
   ```

   with the cycle-wide block-correction lower bound to narrow the possible
   density `R/L_return`;
2. obtain a global restriction on where the positive ordinary deficits can occur
   relative to exceptional blocks and the minimum boundary;
3. use exact cyclic source matching or the global divisor `g` in a way that does
   not require `D<=4500`;
4. seek an explicit linear-form-in-logarithms estimate only if it produces a
   quantitative bound strong enough for the actual parameters.

A finite trajectory calculation, a fixed finite residue ladder, or another lower
bound on the already excluded nonpositive branch is not useful.

## Critical corrections

Do not use `2^A==1 (mod X)`. The correct cycle congruence is

```text
2^A*product_i(n_i)==1 (mod X).
```

Do not identify a least admissible predecessor with the predecessor actually used
by a cycle. Finite computation is not divergence. Full history is in
`docs/RETRACTIONS.md`.

## Verification state

The new standalone checker

```text
python tools/verify_nonpositive_return_block_correction_exclusion.py
```

verified `22993` exact complete-block correction cases, all three known
accelerated `5n+1` cycle regressions, the exact primary comparison giving
`p<2^4006`, and the exponent contradiction with `p>2^(2^974)`.

The related retained standalone checkers are

```text
python tools/verify_near_power_cycle_block_ledger.py
python tools/verify_minimum_boundary_return_credit_dichotomy.py
python tools/verify_minimum_boundary_nonpositive_return_harmonic_barrier.py
```

The new standalone checker passed in the research environment. A complete
repository-wide run was not executed there.
