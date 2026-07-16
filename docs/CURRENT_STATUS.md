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

## Exact complete-block ledger

For a hypothetical cycle, let

```text
p = accelerated length,
A = total valuation,
D=4501*p-A.
```

The canonical complete-block partition has ordinary credits `e` with
`1<=e<=4500` and exceptional credits `-b` with `b>=1`. It obeys

```text
D=sum ordinary deficits-sum exceptional excesses>=1.
```

For a complete block of length `ell`, source `n`, endpoint `n'`, and credit `c`,

```text
n'/n
 =2^c*(X/B)^ell
  *[1+((B/X)^ell-1)/(d*n)].
```

Since `d*n>1`, the correction factor is strictly smaller than `(B/X)^ell`.
Therefore

```text
n'/n<2^c.                                             (1)
```

Source:

```text
docs/NEAR_POWER_CYCLE_BLOCK_LEDGER.md
```

## Positive credit ballot at the least block boundary

Let

```text
z_0,z_1,...,z_q=z_0
```

be the complete-block boundaries in cyclic order, rotated so that `z_0` is the
least boundary value. If

```text
P_j=sum_(i<j)c_i,
```

then multiplying (1) gives

```text
z_j/z_0<2^P_j.
```

Minimality gives `z_j/z_0>=1`, hence

```text
P_j>=1 for every 1<=j<=q.                             (2)
```

Consequences retained from the first ballot theorem:

- the first complete block after `z_0` is ordinary;
- every exceptional excess unit is matched to an earlier ordinary deficit unit
  in actual cyclic order;
- the unit matching may be chosen noncrossing by a stack construction;
- exactly `D` ordinary deficit units remain unmatched;
- after the first `j` ordinary blocks,

  ```text
  E_j<=4500*j-1;
  ```

- an exceptional excess `b` cannot occur that early unless

  ```text
  j>=ceil((b+1)/4500).
  ```

Sources:

```text
docs/MINIMUM_BLOCK_BOUNDARY_CREDIT_BALLOT.md
tools/verify_minimum_block_boundary_credit_ballot.py
```

## New theorem: canonical sponsor arches

For an exceptional block `j`, put

```text
h=P_(j+1).
```

Choose the last index `i<=j` with

```text
P_i<=h.
```

Then `i<j`, block `i` is ordinary, and the actual consecutive segment of blocks
`i,...,j` has net credit

```text
C=P_(j+1)-P_i.
```

The defining last-crossing property proves

```text
0<=C<c_i<=4500,
0<=C<=4499,                                           (3)
P_t>h for every i<t<=j.                               (4)
```

This segment is the canonical sponsor arch of exceptional block `j`.

Two canonical sponsor arches cannot cross: if their intervals were

```text
i<u<=j<v,
```

then the first arch would force `P_u>P_(j+1)`, while the second would force
`P_(j+1)>P_(v+1)`, contradicting the source condition `P_u<=P_(v+1)`.
Therefore sponsor arches are laminar: they are disjoint or nested.

Their maximal members are pairwise disjoint, cover every exceptional block, and
leave only ordinary blocks outside. Thus every hypothetical cycle has an actual
consecutive macro-decomposition into:

```text
maximal sponsor arches with credit 0<=C<=4499;
uncovered ordinary blocks with credit 1<=e<=4500.
```

Multiplying (1) across an arch gives

```text
arch endpoint / arch source <2^C.                     (5)
```

In particular, every zero-credit arch strictly contracts.

Sources:

```text
docs/EXCEPTIONAL_SPONSOR_ARCH_MACRO_EXIT.md
tools/verify_exceptional_sponsor_arch_macro_exit.py
```

## New local block-correction bound

Consider any actual consecutive complete-block segment with

```text
C = net credit,
L = accelerated length,
x = source,
y = endpoint.
```

The exact segment identity and the block correction estimate give

```text
ln(y/x)
 <C*ln(2)-L*[ln(B/X)-d/(2*X)].                        (6)
```

If `y>=x`, then

```text
L*[ln(B/X)-d/(2*X)]<C*ln(2).
```

Using

```text
ln(B/X)>d/B,
ln(2)<1,
d/B-d/(2*X)=d*(X-d)/(2*B*X)>0,
```

we obtain the exact local theorem

```text
L < 2*C*B*X/[d*(X-d)].                                (7)
```

Thus every nondecreasing segment has `C>=1`. For the primary candidate,
`C<=4500` implies

```text
L<2^4006.                                             (8)
```

This is a segment theorem, not only a cycle-wide estimate. It has no assumed
upper cutoff on `L`.

## New strongest exit-return decomposition

Let `z` be the least complete-block boundary. The retained pure-exit theorem
proves that the first block is ordinary, has deficit `1<=e<=4500`, ends above
`z`, and leaves a return of credit `R_0>=1`.

Now use the maximal sponsor-arch decomposition.

- If no maximal arch begins at block `0`, take the first ordinary block as the
  initial macro-exit.
- If a maximal arch begins at block `0`, take that whole arch. Its credit is
  `0<=C<e`. It cannot be the full cycle, because full closure would give
  `D=C<e`, while the retained pure-exit theorem gives `D=e+R_0>e`.

In either case the macro-exit ends at a proper boundary `y>z`. Equation (5)
rules out zero credit, so

```text
z<y,
1<=C<=4500.                                           (9)
```

The local theorem (8) gives

```text
L_macro<2^4006.                                      (10)
```

If the first ordinary block sponsors a nested family of early exceptional
blocks, the entire maximal nest is absorbed into this bounded macro-exit.

Let

```text
R=D-C
```

be the credit of the remaining actual return from `y` to `z`.

- for a one-block macro-exit, `R=R_0>=1`;
- for an arch macro-exit, `R=e+R_0-C>=2`.

Therefore

```text
R>=1.                                                 (11)
```

The exact return equation and `log2(B/X)<2^-3990` yield

```text
L_return>2^3990.                                      (12)
```

For any prefix of the compressed return ending at a complete-block boundary,
write `Q` for its credit. The ballot theorem gives

```text
C+Q>=1,
Q>=1-C>=-4499.                                       (13)
```

Thus the strongest current form of G3 is:

```text
bounded sponsored macro-exit:
  z<y,
  1<=C<=4500,
  L_macro<2^4006;

remaining actual return:
  R>=1,
  L_return>2^3990,
  every block-boundary prefix has Q>=-4499;

all return exceptions:
  contained in disjoint maximal sponsor arches of credit <=4499.
```

Sources:

```text
docs/EXCEPTIONAL_SPONSOR_ARCH_MACRO_EXIT.md
tools/verify_exceptional_sponsor_arch_macro_exit.py
docs/MINIMUM_BLOCK_BOUNDARY_PURE_ORDINARY_EXIT.md
tools/verify_minimum_block_boundary_pure_ORDINARY_EXIT.py
```

## Closed nonpositive-return branch

For any near-power multiplier

```text
B=2^m,
X=B-d,
0<d<B/2,
```

the exact block-correction identity proves

```text
p < 2*D*B*X/[d*(X-d)].                               (14)
```

For the primary candidate, a nonpositive return gives `1<=D<=4500`, hence

```text
p<2^4006.
```

The retained permanent-class harmonic theorem gives

```text
p>2^(2^974),
```

so all nonpositive returns are excluded. Former `h=1` and `h>=2` subdivisions
remain valid conditional results, but their common hypothesis is impossible.

Sources:

```text
docs/NONPOSITIVE_RETURN_BLOCK_CORRECTION_EXCLUSION.md
tools/verify_nonpositive_return_block_correction_exclusion.py
```

## Exact cyclic closure and retained global divisor

For a cyclic valuation word and rotated affine numerators `Q_k`,

```text
Delta=2^A-X^p,
2^a_k*Q_(k+1)=X*Q_k+Delta.
```

The word closes to a positive cycle iff `Delta>0` and `Delta|Q_0`. Equivalently,
a truly adjacent pair satisfies

```text
gcd(Q_k,Q_(k+1))=Delta.
```

For complete block lengths `ell_i`, put

```text
h=gcd_i ell_i,
S_h=(B^h-X^h)/d,
g=gcd of all complete-block boundaries.
```

Exact closure gives

```text
g=gcd(b_i,S_h) for every boundary b_i,
S_h/g divides 2^D-1,
S_h/gcd(S_h,2^D-1) divides g divides S_h,
n_t==B^(-j)*S_j (mod g),  j=t mod h.
```

Fixed local endpoint congruences, finite two-sided word gluing, naive block
compression, finite repeated-defect persistence, arbitrary finite same-deficit
runs, and any fixed finite `N`-adic depth do not force exact cyclic source
matching. Exact valuation-word coding and CRT realize those local constraints at
infinitely many positive starts.

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

Exclude the positive-credit return in (11)--(13), after the bounded initial
sponsor nest has been removed. The strongest current route is:

1. work with the disjoint maximal sponsor arches on the return;
2. use (7) to show that every noncontracting arch has accelerated length below
   `2^4006`;
3. combine each arch's source and endpoint with the permanent `N` and `1093^2`
   labels and the exceptional-source floor;
4. prove that the return cannot contain enough contracting arches without an
   impossible height loss, exact source-class repetition, incompatible
   adjacent-label lift, or excessive harmonic correction;
5. exploit `Q>=-4499` so no prefix can use an unbounded exceptional reserve.

Secondary routes are the exact global divisor `g` and a linear-form-in-logarithms
estimate, but only if their constants beat the actual correction terms.

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

The new standalone checker passed in the research environment:

```text
python tools/verify_exceptional_sponsor_arch_macro_exit.py
```

It verified:

- `2123272` positive-prefix integer ledgers;
- canonical sponsor construction, laminarity, maximal-arch coverage, and exact
  macro-credit conservation;
- `113288` exact local near-power segment cases;
- all three known accelerated `5n+1` positive-cycle regressions;
- the primary bound `L_macro<2^4006`;
- positive compressed-return credit, `L_return>2^3990`, and prefix debt
  `Q>=-4499`.

The related retained standalone checkers are

```text
python tools/verify_minimum_block_boundary_credit_ballot.py
python tools/verify_minimum_block_boundary_pure_ordinary_exit.py
python tools/verify_nonpositive_return_block_correction_exclusion.py
```

A complete repository-wide run was not executed in this environment.
