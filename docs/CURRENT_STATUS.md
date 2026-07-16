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
 <2^c.                                                  (1)
```

Rotate the complete-block boundaries so that `z_0` is least, and put
`P_j=sum_(i<j)c_i`. Then

```text
P_j>=1 for every nonempty prefix.                       (2)
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
`P_i<=h`. The actual consecutive segment `i,...,j` has credit

```text
0<=C<=4499.                                             (3)
```

Every internal boundary stays strictly above the final credit level. Canonical
arches are laminar; their maximal members are disjoint, cover every exceptional
block, and leave only ordinary blocks outside. The compressed cycle consists of

```text
maximal sponsor arches: credit 0..4499;
uncovered ordinary blocks: credit 1..4500.
```

Every arch satisfies

```text
arch endpoint / arch source <2^C.                      (4)
```

Sources:

```text
docs/EXCEPTIONAL_SPONSOR_ARCH_MACRO_EXIT.md
tools/verify_exceptional_sponsor_arch_macro_exit.py
```

## Floor-sensitive local height theorem

Every hypothetical cycle value is greater than `N`. For a complete block of
length `ell`, its correction parameter satisfies

```text
q<ell/(X*N),
kappa<ell/(X*N*ln(2)).
```

Put

```text
delta=log2(B/X),
epsilon=1/(X*N*ln(2)).
```

The earlier exact estimates remain valid:

```text
delta<2^-3992,
delta-epsilon>997*2^-4002.                             (5)
```

Sources for the earlier bracket:

```text
docs/PRIMARY_DELTA_TWO_BIT_SHARPENING.md
tools/verify_primary_delta_two_bit_sharpening.py
docs/CYCLE_FLOOR_LOCAL_CORRECTION_SHARPENING.md
tools/verify_cycle_floor_local_correction_sharpening.py
```

The new exact atanh-series bracket for `ln(2)` sharpens (5) to

```text
1007*2^-4002 < delta-epsilon,
delta < 1008*2^-4002.                                  (6)
```

For every actual consecutive complete-block segment of credit `C`, length `L`,
source `x`, and endpoint `y`, the exact identity

```text
log2(y/x)=C-L*delta+K,
0<K<L*epsilon
```

therefore gives

```text
log2(y/x)<C-1007*L*2^-4002.                            (7)
```

Consequences for positive-credit segments:

```text
nondecreasing: L<C*2^4002/1007;
contracting:   L>C*2^4002/1008.                        (8)
```

Source:

```text
docs/PRIMARY_ONE_OVER_1007_CYCLE_STRIP.md
tools/verify_primary_one_over_1007_cycle_strip.py
```

## Quantitative zero-credit arches

For a zero-credit sponsor arch, equation (7) gives

```text
log2(source/endpoint)>1007*L*2^-4002,
source/endpoint>2^(1007*L*2^-4002).                    (9)
```

For pairwise disjoint zero-credit arches of total length `Z`, their logarithmic
loss is greater than `1007*Z*2^-4002`. Since all remaining positive-credit
macroblocks have total credit `D`,

```text
Z<D*2^4002/1007.                                      (10)
```

The older retained estimate `Z<D*2^4002/997` remains true but is superseded.

Sources:

```text
docs/ZERO_CREDIT_ARCH_QUANTITATIVE_CONTRACTION.md
tools/verify_zero_credit_arch_quantitative_contraction.py
docs/PRIMARY_ONE_OVER_1007_CYCLE_STRIP.md
tools/verify_primary_one_over_1007_cycle_strip.py
```

## One-over-1007 global cycle strip

Apply (6)--(7) to the full cycle. Since `x=y`, `C=D`, and `L=p`,

```text
D*2^4002/1008
 <p
 <D*2^4002/1007.                                      (11)
```

The upper endpoint divided by the lower endpoint is `1008/1007`. Hence the
relative width is exactly

```text
1/1007<0.1%.                                          (12)
```

This replaces the former retained strip

```text
D*2^3992<p<D*2^4002/997,
```

whose relative width was `27/997<2.71%`. The scalar cycle window is now more
than 27 times narrower.

## Strongest current exit-return decomposition

Let `z` be the least complete-block boundary. Take as initial macro-exit:

1. the maximal sponsor arch beginning with block `0`, if one exists; or
2. otherwise the first ordinary block.

This gives an actual initial macro-exit from `z` to `y` with

```text
z<y,
1<=C<=4500,
L_macro<C*2^4002/1007<2^4005.                         (13)
```

The remaining actual return from `y` to `z`, with credit `R=D-C`, satisfies

```text
R>=1,
L_return>R*2^4002/1008.                               (14)
```

Every return prefix ending at a complete-block boundary has credit `Q` satisfying

```text
C+Q>=1,
Q>=1-C>=-4499.                                        (15)
```

The global strip adds

```text
L_return
 <(C+R)*2^4002/1007
 <=(R+4500)*2^4002/1007.                              (16)
```

Thus G3 is reduced to a positive-credit return whose length per credit lies in
the one-over-1007 near-critical regime after a bounded sponsored macro-exit. All
exceptions on the return lie in disjoint maximal sponsor arches of credit at
most `4499`.

Sources:

```text
docs/EXCEPTIONAL_SPONSOR_ARCH_MACRO_EXIT.md
tools/verify_exceptional_sponsor_arch_macro_exit.py
docs/MINIMUM_BLOCK_BOUNDARY_PURE_ORDINARY_EXIT.md
tools/verify_minimum_block_boundary_pure_ordinary_exit.py
docs/PRIMARY_ONE_OVER_1007_CYCLE_STRIP.md
tools/verify_primary_one_over_1007_cycle_strip.py
```

## Closed nonpositive branch

The retained cycle-wide correction theorem gives

```text
p < 2*D*B*X/[d*(X-d)].
```

A nonpositive return has `1<=D<=4500`, hence `p<2^4006`, while the retained
harmonic theorem gives `p>2^(2^974)`. Therefore every nonpositive return is
impossible and must not be revisited.

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

For complete-block lengths `ell_i`, put

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

Exclude the positive-credit return in (14)--(16). The strongest route is now:

1. use the one-over-1007 global strip (11), not the older coarse length bounds;
2. charge every zero-credit arch by its strengthened height loss (9);
3. apply the adjacent `1007/1008` positive-credit length dichotomy (8) to all
   remaining macroblocks;
4. combine arch endpoints with the permanent `N` and `1093^2` labels and the
   exceptional-source floor;
5. derive either a lower correction bound incompatible with the `1/1007` strip,
   an impossible source-class repetition, or an incompatible adjacent-label lift;
6. exploit `Q>=-4499`, so no return prefix can use an unbounded exceptional
   reserve.

Secondary routes remain the exact global divisor `g` and an explicit
linear-form-in-logarithms estimate, but only if their constants beat the actual
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

The latest relevant standalone checkers passed in the research environment:

```text
python tools/verify_exceptional_sponsor_arch_macro_exit.py
python tools/verify_primary_delta_two_bit_sharpening.py
python tools/verify_cycle_floor_local_correction_sharpening.py
python tools/verify_zero_credit_arch_quantitative_contraction.py
python tools/verify_primary_one_over_1007_cycle_strip.py
```

The new checker verified, using exact integers and rational arithmetic:

```text
842/1215<ln(2)<1910051/2755620;
1007*2^-4002<delta-epsilon;
delta<1008*2^-4002;
D*2^4002/1008<p<D*2^4002/1007;
relative strip width 1/1007<0.1%;
L_macro<2^4005;
L_return>R*2^4002/1008.
```

The new standalone checker passed. A complete repository-wide run was not
executed in this environment.
