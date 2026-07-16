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
Therefore every complete block satisfies the exact height-credit domination

```text
n'/n<2^c.                                             (1)
```

Source:

```text
docs/NEAR_POWER_CYCLE_BLOCK_LEDGER.md
```

## New theorem: positive credit ballot from the least block boundary

Let

```text
z_0,z_1,...,z_q=z_0
```

be the complete-block boundaries in cyclic order, rotated so that `z_0` is the
least boundary value. If

```text
P_j=sum_(i<j)c_i
```

is the cumulative credit of the first `j` complete blocks, multiplying (1) gives

```text
z_j/z_0<2^P_j.
```

Minimality gives `z_j/z_0>=1`, hence

```text
P_j>=1 for every 1<=j<=q.                             (2)
```

Consequences:

- the first complete block after `z_0` is ordinary;
- every exceptional excess unit is matched to an earlier ordinary deficit unit
  in actual cyclic order;
- the matching may be chosen noncrossing by a stack construction;
- exactly `D` ordinary deficit units remain unmatched after the full cycle;
- after the first `j` ordinary blocks, cumulative exceptional excess satisfies

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

## New strongest exit-return decomposition

Let `z` be the least complete-block boundary and let `z'` be the endpoint of the
first complete block.

By (1) and minimality, that first block cannot be exceptional. It is one pure
ordinary block with

```text
1<=e<=4500.
```

The retained one-sided continued-fraction gap and the sharper one-block
correction bound prove

```text
L_exit*log2(B/X)<e,
z'>z.
```

Thus the actual first exit is consecutive, contains no exceptional block, and
its base multiplier already expands.

Write `R` and `L_return` for the credit and accelerated length of the remaining
actual return from `z'` to `z`. If `R<=0`, then

```text
1<=D=e+R<=4500.
```

The permanent-class harmonic estimate forces

```text
L_return>2^(2^974),
```

while the global block-correction theorem forces

```text
p<2^4006.
```

This is impossible. Therefore the only surviving return satisfies

```text
R>=1,
L_return>2^3990.                                      (3)
```

The ballot theorem also controls every return prefix ending at a complete-block
boundary. If its return-prefix credit is `Q`, then

```text
e+Q>=1,
Q>=1-e>=-4499.                                       (4)
```

So the surviving return cannot hide an arbitrarily large exceptional debt at its
front. This is the strongest current structural form of G3.

Sources:

```text
docs/MINIMUM_BLOCK_BOUNDARY_PURE_ORDINARY_EXIT.md
tools/verify_minimum_block_boundary_pure_ordinary_exit.py
```

## Closed nonpositive-return branch

For any near-power multiplier

```text
B=2^m,
X=B-d,
0<d<B/2,
```

the exact block-correction identity proves the cycle-wide upper bound

```text
p < 2*D*B*X/[d*(X-d)].                               (5)
```

For the primary candidate, every nonpositive return gives `1<=D<=4500`, hence

```text
p<2^4006.
```

The retained harmonic theorem gives `p>2^(2^974)`, so all nonpositive returns are
excluded. Former `h=1` and `h>=2` subdivisions remain valid conditional results,
but their common hypothesis is impossible.

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

Exclude the positive-credit return in (3), using the prefix control (4). The
strongest current route is:

1. use the noncrossing ballot matching to assign every exceptional excess unit
   to an earlier ordinary deficit unit;
2. combine each sponsor-exception pair with the permanent `N` and `1093^2`
   labels and the exceptional-source floor;
3. prove that a valid sponsor either repeats an exact source class, violates an
   adjacent-label lift, or contributes too much harmonic correction;
4. exploit `Q>=-4499` so no return prefix can use an unbounded exceptional
   reserve.

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

The two new standalone checkers passed in the research environment:

```text
python tools/verify_minimum_block_boundary_credit_ballot.py
python tools/verify_minimum_block_boundary_pure_ordinary_exit.py
```

They verified:

- `251994` exact complete-block domination cases;
- all three known accelerated `5n+1` positive-cycle regressions;
- `699337` small positive-prefix stack-matching ledgers;
- the primary bounds `E_j<=4500*j-1` and `Q>=-4499`;
- the continued-fraction gap and one-block exit correction;
- the harmonic return bound and global length contradiction.

A complete repository-wide run was not executed in this environment.
