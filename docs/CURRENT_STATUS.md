# Current status

Authoritative compact summary of the active mathematical frontier. Detailed
proofs live in the linked theorem files and exact checkers.

## Strict target and candidate

Find explicit positive odd `X>=5,n0` such that

```text
C_X(n)=(X*n+1)/2^v2(X*n+1)
```

tends to positive infinity.

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

The strict problem remains open solely because G3 remains open.

## Global cycle frontiers

Define

```text
Q_credit=
924679364903952241768234680715310598867316370441120757898246831506500507205080014535351439406991342585993538327845986892977536682537320095988153612270886695873966778097766981798062925612878469213187733241206117142814414961418054803443235355123715316220902421623921086365374327267387194352877014114959.
```

Every hypothetical positive cycle satisfies

```text
N|X and 1093||X;
16562000 permanent classes modulo N*1093^2;
every cycle value>N;
every exceptional source has at least 1505 decimal digits;
no cycle value in the checked window through 10^1201;
total credit D>=Q_credit>2^996;
accelerated length p>2^4988;
at least ceil(Q_credit/4500) ordinary complete blocks.
```

The exact ordinary-block lower bound is

```text
205484303311989387059607706825624577526070304542471279532943740334777890490017781007855875423775853907998564072854663753995008151674960021330700802726863710194214839577281551510680650136195215380708385164712470476180981102537345511876274523360825625826867204805315796970083183837197154300639336470.
```

Sources:

```text
docs/PRIMARY_CREDIT_CONTINUED_FRACTION_FRONTIER.md
tools/verify_primary_credit_continued_fraction_frontier.py
```

## Complete-block ledger and ballot

For accelerated length `p`, total valuation `A`, and total credit

```text
D=4501*p-A,
```

the canonical complete blocks have ordinary credits `1<=e<=4500` and
exceptional credits `-b`, `b>=1`.  Their total credit is `D`.

For a complete block of length `ell`, source `n`, endpoint `n'`, and credit `c`,

```text
n'/n
 =2^c*(X/B)^ell
  *[1+((B/X)^ell-1)/(d*n)]
 <2^c.                                                  (1)
```

Rotate the complete-block boundaries so that `z_0` is least.  Every nonempty
cumulative credit prefix satisfies

```text
P_j>=1.                                                 (2)
```

Consequences:

```text
the first block is ordinary;
every exceptional unit has an earlier ordinary sponsor;
exactly D ordinary units remain unmatched;
E_j<=4500*j-1 after the first j ordinary blocks.
```

Every exceptional block lies in a canonical sponsor arch with total credit

```text
0<=C<=4499.
```

The arches are laminar. Their maximal members are pairwise disjoint, cover all
exceptional blocks, and leave only ordinary blocks outside.

Sources:

```text
docs/NEAR_POWER_CYCLE_BLOCK_LEDGER.md
docs/MINIMUM_BLOCK_BOUNDARY_CREDIT_BALLOT.md
tools/verify_minimum_block_boundary_credit_ballot.py
docs/EXCEPTIONAL_SPONSOR_ARCH_MACRO_EXIT.md
tools/verify_exceptional_sponsor_arch_macro_exit.py
```

## Floor-sensitive height and global strip

Put

```text
delta=log2(B/X),
epsilon=1/(X*N*ln(2)).
```

Exact arithmetic proves

```text
1007*2^-4002 < delta-epsilon,
delta < 1008*2^-4002.                                  (3)
```

Every actual consecutive complete-block segment of credit `C`, length `L`,
source `x`, and endpoint `y` satisfies

```text
log2(y/x)<C-1007*L*2^-4002.                            (4)
```

For positive-credit segments:

```text
nondecreasing: L<C*2^4002/1007;
contracting:   L>C*2^4002/1008.                        (5)
```

A zero-credit sponsor arch has strict logarithmic contraction

```text
log2(source/endpoint)>1007*L*2^-4002.                  (6)
```

For a full cycle,

```text
D*2^4002/1008
 <p
 <D*2^4002/1007.                                      (7)
```

The relative width is exactly

```text
1/1007<0.1%.
```

Sources:

```text
docs/PRIMARY_DELTA_TWO_BIT_SHARPENING.md
tools/verify_primary_delta_two_bit_sharpening.py
docs/CYCLE_FLOOR_LOCAL_CORRECTION_SHARPENING.md
tools/verify_cycle_floor_local_correction_sharpening.py
docs/ZERO_CREDIT_ARCH_QUANTITATIVE_CONTRACTION.md
tools/verify_zero_credit_arch_quantitative_contraction.py
docs/PRIMARY_ONE_OVER_1007_CYCLE_STRIP.md
tools/verify_primary_one_over_1007_cycle_strip.py
```

## Continued-fraction frontier

Put

```text
lambda=ln(B/X),
beta=ln(2)/lambda,
z=p*lambda-D*ln(2)>0.
```

The exact cycle identity is

```text
z=lambda*(p-D*beta)
 =sum_cycle ln(1+1/(X*n_i)).                           (8)
```

A rigorous interval computation fixes the first `554` continued-fraction
coefficients of `beta`.  The final certified one-sided denominator frontier is
`Q_credit`.  Combining its mandatory gap with the full correction bound proves

```text
D>=Q_credit.                                            (9)
```

The scalar continued-fraction route has reached this explicit 300-digit
frontier.  Further progress needs a stronger correction bound or genuinely new
nonlocal arithmetic.

Source:

```text
docs/PRIMARY_CREDIT_CONTINUED_FRACTION_FRONTIER.md
tools/verify_primary_credit_continued_fraction_frontier.py
```

## Strongest exit-return decomposition

Let `z` be the least complete-block boundary.  The maximal sponsor arch starting
at `z`, or otherwise the first pure ordinary block, gives an actual initial
macro-exit from `z` to `y` with

```text
z<y,
1<=C<=4500,
L_macro<C*2^4002/1007<2^4005.                         (10)
```

The remaining return from `y` to `z`, with `R=D-C`, satisfies

```text
R>=Q_credit-4500,
L_return>R*2^4002/1008,
L_return<(R+4500)*2^4002/1007.                        (11)
```

Every return prefix ending at a complete-block boundary has credit

```text
Q>=1-C>=-4499.                                        (12)
```

Thus G3 is reduced to an enormous positive-credit return in the narrow
`1007/1008` critical strip after a bounded sponsored macro-exit.

The nonpositive-return branch is completely excluded and must not be revisited.

Sources:

```text
docs/EXCEPTIONAL_SPONSOR_ARCH_MACRO_EXIT.md
tools/verify_exceptional_sponsor_arch_macro_exit.py
docs/MINIMUM_BLOCK_BOUNDARY_PURE_ORDINARY_EXIT.md
tools/verify_minimum_block_boundary_pure_ordinary_exit.py
docs/NONPOSITIVE_RETURN_BLOCK_CORRECTION_EXCLUSION.md
tools/verify_nonpositive_return_block_correction_exclusion.py
```

## Exact cyclic divisor retained

For a cyclic valuation word and rotated affine numerators `Q_k`,

```text
Delta=2^A-X^p,
2^a_k*Q_(k+1)=X*Q_k+Delta.
```

Closure is equivalent to `Delta>0` and `Delta|Q_0`, and adjacent numerators
satisfy

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
n_t==B^(-j)*S_j (mod g),  j=t mod h.                 (13)
```

This exact global divisor contains information not present in finite local
endpoint labels and remains an active route.

Sources:

```text
docs/CYCLIC_ROTATION_CLOSURE_GCD.md
docs/GLOBAL_BLOCK_GCD_PHASE_SIEVE.md
```

## Permanent-label and prime-power closure no-go

The permanent labels modulo `N*1093^2` are automatically compatible with cyclic
wraparound.  More strongly, let

```text
q=1093,
h=ord_q(2)=364,
w=(2^h-1)/q^2 (mod q)=891.
```

Since `w!=0`, every compatible cyclic label word modulo `N*q^r` lifts from
`r` to `r+1`: the new valuation-layer digit cancels the new transition defect
independently on each edge while preserving the modulo-`500` label.

Therefore every compatible cyclic label word closes modulo

```text
N*1093^r
```

for every finite `r>=2`.  The exact number of combined allowed classes is

```text
16562000*1093^(r-2).                                  (14)
```

Higher `1093`-adic lifts are completely saturated above the informative `q^2`
level.  Hence no proof of G3 can come from a finite deeper `1093`-adic label
automaton plus bare cyclic closure.

This is a strict structural no-go, not merely a failed search.

Sources:

```text
docs/PERMANENT_LABEL_CYCLIC_CLOSURE_NO_GO.md
tools/verify_permanent_label_cyclic_closure_no_go.py
docs/WIEFERICH_Q_ADIC_LIFT_SATURATION_NO_GO.md
tools/verify_wieferich_q_adic_lift_saturation.py
```

## Decisive next target

Exclude the positive-credit return in (11)--(12).

The local `1093`-adic closure route is exhausted.  The strongest remaining
route for the primary candidate is now:

1. combine the 300-digit credit frontier with the `1/1007` global strip;
2. charge zero-credit arches by (6);
3. apply the `1007/1008` length dichotomy to all remaining positive-credit
   macroblocks;
4. use the `N*1093^2` classes only for global occupancy and correction bounds;
5. test whether the exact global divisor `g` in (13) conflicts with the forced
   297-digit population of ordinary blocks;
6. exploit `Q>=-4499`, so exceptional prefixes have only bounded reserve.

In parallel, screen alternative multipliers for a prime-power invariant whose
new valuation digits are not locally free.  If the global-divisor route also
fails to couple the labels, the primary candidate should be deprioritized rather
than extended by more local residue layers.

Do not use finite same-type windows, finite word gluing, a fixed finite
`N`-adic ladder, any finite `1093`-adic lift, or long finite trajectories as a
standalone contradiction.

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
used by a cycle.  Finite computation is not divergence.

## Verification state

The new standalone checker passed in the research environment:

```text
python tools/verify_wieferich_q_adic_lift_saturation.py
```

It verified with exact integer arithmetic:

```text
ord_1093(2)=364;
v_1093(2^364-1)=2;
w=891;
132496 distinct adjacent q^2 classes;
16562000 combined N*q^2 classes;
coherent cyclic lifts through q^10 on deterministic regression words;
preservation of all modulo-500 labels.
```

The relevant earlier standalone checkers for the credit frontier, sponsor arches,
height strip, and permanent-label closure also passed.  A complete
repository-wide run was not executed in this environment.
