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

Every hypothetical cycle satisfies:

```text
N|X and 1093||X;
16562000 permanent classes modulo N*1093^2;
every cycle value>N;
every exceptional source has at least 1505 decimal digits;
no cycle value in the checked window through 10^1201;
at least 245833 ordinary complete blocks.
```

## Complete-block ledger and ballot

For accelerated length `p`, total valuation `A`, and total credit

```text
D=4501*p-A,
```

the canonical complete blocks have ordinary credits `1<=e<=4500` and
exceptional credits `-b`, `b>=1`, with

```text
D=sum ordinary deficits-sum exceptional excesses>=1.
```

For a block of length `ell`, source `n`, endpoint `n'`, and credit `c`,

```text
n'/n
 =2^c*(X/B)^ell
  *[1+((B/X)^ell-1)/(d*n)]
 <2^c.                                                 (1)
```

Rotate the block boundaries

```text
z_0,z_1,...,z_q=z_0
```

so that `z_0` is least, and put `P_j=sum_(i<j)c_i`. From (1),

```text
z_j/z_0<2^P_j.
```

Minimality gives

```text
P_j>=1 for every 1<=j<=q.                             (2)
```

Consequences:

```text
the first block is ordinary;
every exceptional unit has an earlier ordinary sponsor;
exactly D ordinary units remain unmatched;
E_j<=4500*j-1 after the first j ordinary blocks;
an excess b requires j>=ceil((b+1)/4500).
```

Sources:

```text
docs/NEAR_POWER_CYCLE_BLOCK_LEDGER.md
docs/MINIMUM_BLOCK_BOUNDARY_CREDIT_BALLOT.md
tools/verify_minimum_block_boundary_credit_ballot.py
```

## Canonical sponsor arches

For an exceptional block `j`, put `h=P_(j+1)` and choose the last `i<=j` with
`P_i<=h`. Then `i<j`, block `i` is ordinary, and the actual consecutive segment
`i,...,j` has credit

```text
C=P_(j+1)-P_i,
0<=C<c_i<=4500,
0<=C<=4499.                                           (3)
```

Every internal boundary stays strictly above the final credit level:

```text
P_t>h for every i<t<=j.                               (4)
```

Two sponsor arches cannot cross. Hence they are laminar; their maximal members
are disjoint, cover every exceptional block, and leave only ordinary blocks
outside. The cycle is compressed into

```text
maximal sponsor arches: credit 0..4499;
uncovered ordinary blocks: credit 1..4500.
```

Multiplying (1) across an arch gives

```text
arch endpoint / arch source <2^C.                     (5)
```

Every zero-credit arch therefore strictly contracts.

Sources:

```text
docs/EXCEPTIONAL_SPONSOR_ARCH_MACRO_EXIT.md
tools/verify_exceptional_sponsor_arch_macro_exit.py
```

## Sharp local length theorems

For any actual consecutive block segment of net credit `C`, accelerated length
`L`, source `x`, and endpoint `y`, the exact correction estimates give

```text
ln(y/x)
 <C*ln(2)-L*[ln(B/X)-d/(2*X)].                        (6)
```

If `y>=x`, elementary rational logarithmic bounds imply

```text
L < 2*C*B*X/[d*(X-d)] < C*2^3994.                    (7)
```

For `C<=4500`, exact integer comparison also gives

```text
L<2^4006.                                             (8)
```

A new exact rational estimate sharpens the primary drift to

```text
delta=log2(B/X)<2^-3992.                              (9)
```

The proof uses

```text
2^3992*d/X<349/511<11/16<56/81<ln(2),
-ln(1-d/B)<d/X.
```

If a positive-credit segment contracts, its exact equation

```text
log2(y/x)=C-L*delta+K<0,
K>0,
```

gives

```text
C>=1 and y<x  =>  L>C*2^3992.                        (10)
```

Thus every positive-credit macroblock has an explicit height-sign dichotomy:

```text
nondecreasing: L<C*2^3994;
contracting:   L>C*2^3992.
```

Zero-credit sponsor arches always contract, but (10) does not apply to them.

Sources:

```text
docs/PRIMARY_DELTA_TWO_BIT_SHARPENING.md
tools/verify_primary_delta_two_bit_sharpening.py
docs/EXCEPTIONAL_SPONSOR_ARCH_MACRO_EXIT.md
```

## Strongest current exit-return decomposition

Let `z` be the least complete-block boundary. The retained pure-exit theorem
proves that the first block is ordinary with `1<=e<=4500`, ends above `z`, and
leaves return credit `R_0>=1`.

Take as initial macro-exit:

1. the maximal sponsor arch beginning at block `0`, if one exists; or
2. otherwise the first ordinary block.

An arch beginning at block `0` has `0<=C<e` and cannot be the full cycle, because
full closure would give `D=C<e`, while `D=e+R_0>e`. Its endpoint is a proper
boundary above `z`; equation (5) rules out `C=0`.

Therefore

```text
z<y,
1<=C<=4500,
L_macro<2^4006.                                      (11)
```

The macro-exit absorbs the entire maximal nest of early exceptions sponsored
through the first ordinary crossing.

For the remaining actual return from `y` to `z`, put `R=D-C`. Then

```text
R>=1.                                                 (12)
```

Applying the sharpened drift estimate (9) to this contracting return gives

```text
L_return>R*2^3992>=2^3992.                            (13)
```

Every return prefix ending at a block boundary has credit `Q` satisfying

```text
C+Q>=1,
Q>=1-C>=-4499.                                       (14)
```

Thus G3 is reduced to an astronomically long positive-credit return after a
bounded sponsored macro-exit. All exceptions on that return lie in disjoint
maximal arches of credit at most `4499`.

Sources:

```text
docs/EXCEPTIONAL_SPONSOR_ARCH_MACRO_EXIT.md
tools/verify_exceptional_sponsor_arch_macro_exit.py
docs/PRIMARY_DELTA_TWO_BIT_SHARPENING.md
tools/verify_primary_delta_two_bit_sharpening.py
docs/MINIMUM_BLOCK_BOUNDARY_PURE_ORDINARY_EXIT.md
tools/verify_minimum_block_boundary_pure_ordinary_exit.py
```

## Closed nonpositive branch

The cycle-wide block-correction theorem gives

```text
p < 2*D*B*X/[d*(X-d)].                               (15)
```

A nonpositive return has `1<=D<=4500`, hence `p<2^4006`. The retained
permanent-class harmonic theorem gives `p>2^(2^974)`. Therefore every
nonpositive return is impossible. Do not revisit its former `h=1` or `h>=2`
subdivisions as live branches.

Sources:

```text
docs/NONPOSITIVE_RETURN_BLOCK_CORRECTION_EXCLUSION.md
tools/verify_nonpositive_return_block_correction_exclusion.py
```

## Exact cyclic closure retained

For a cyclic valuation word and rotated affine numerators `Q_k`,

```text
Delta=2^A-X^p,
2^a_k*Q_(k+1)=X*Q_k+Delta.
```

Closure is equivalent to `Delta>0` and `Delta|Q_0`; for an adjacent pair,

```text
gcd(Q_k,Q_(k+1))=Delta.
```

For complete-block lengths `ell_i`, let

```text
h=gcd_i ell_i,
S_h=(B^h-X^h)/d,
g=gcd of all complete-block boundaries.
```

Then

```text
g=gcd(b_i,S_h) for every boundary b_i,
S_h/g divides 2^D-1,
S_h/gcd(S_h,2^D-1) divides g divides S_h,
n_t==B^(-j)*S_j (mod g),  j=t mod h.
```

Finite local endpoint congruences, finite word gluing, repeated finite patterns,
and fixed finite `N`-adic ladders do not force exact source matching; the
repository contains explicit no-go theorems for those routes.

Sources:

```text
docs/CYCLIC_ROTATION_CLOSURE_GCD.md
docs/GLOBAL_BLOCK_GCD_PHASE_SIEVE.md
docs/FIXED_LOCAL_ENDPOINT_CONGRUENCE_NO_GO.md
docs/FULL_FINITE_TWO_SIDED_WORD_GLUING_NO_GO.md
docs/COMPLETE_BLOCK_GCD_COMPRESSION_NO_GO.md
docs/GEOMETRIC_FACTOR_STRONG_DIVISIBILITY_PERSISTENCE_NO_GO.md
docs/SAME_DEFICIT_FINITE_PERSISTENCE_NO_GO.md
```

## Decisive next target

Exclude the return in (12)--(14). The strongest route is:

1. use the disjoint maximal sponsor arches on the return;
2. apply the length dichotomy (7), (10) to every positive-credit arch;
3. isolate zero-credit arches, which always contract and are now the only
   contracting macroblocks without a credit-proportional length lower bound;
4. combine arch endpoints with the permanent `N` and `1093^2` labels and the
   exceptional-source floor;
5. prove that the long return requires an impossible height loss, exact
   source-class repetition, incompatible adjacent-label lift, or excessive
   harmonic correction;
6. exploit `Q>=-4499`, so no prefix can use an unbounded exceptional reserve.

Secondary routes are the exact global divisor `g` and an explicit
linear-form-in-logarithms estimate, only if their constants beat the actual
correction terms.

## Critical corrections

Do not use

```text
2^A==1 (mod X).
```

The correct relation is

```text
2^A*product_i(n_i)==1 (mod X).
```

Do not identify a least admissible predecessor with the predecessor actually
used by a cycle. Finite computation is not divergence.

## Verification state

The new standalone checkers passed in the research environment:

```text
python tools/verify_exceptional_sponsor_arch_macro_exit.py
python tools/verify_primary_delta_two_bit_sharpening.py
```

They verified:

```text
2123272 positive-prefix integer ledgers;
canonical arches, laminarity, maximal coverage, and credit conservation;
113288 exact local near-power segment cases;
all three known accelerated 5n+1 positive-cycle regressions;
L_macro<2^4006;
exact delta<2^-3992;
contracting positive-credit bound L>C*2^3992;
return bound L_return>R*2^3992;
nondecreasing bound L<C*2^3994.
```

Both checkers are included in `run_checks.py`. A complete repository-wide run
was not executed in this environment.
