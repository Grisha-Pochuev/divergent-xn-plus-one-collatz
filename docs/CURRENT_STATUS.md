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

## Actual minimum-boundary exit and return

Every hypothetical cycle contains an actual consecutive expanding exit from its
least ordinary boundary `x` to the next ordinary boundary `y>x` with

```text
1<=C<=4500,
exceptional excess<=4499,
complete blocks<=4500,
L*log2(B/X)<C.
```

The remaining actual return satisfies

```text
R>=1 => Lr>2^3990,
R<=0 => Lr>2^(2^974).
```

Sources:

```text
docs/MINIMUM_BOUNDARY_ACTUAL_EXPANDING_SEGMENT.md
docs/MINIMUM_BOUNDARY_RETURN_CREDIT_DICHOTOMY.md
docs/MINIMUM_BOUNDARY_NONPOSITIVE_RETURN_HARMONIC_BARRIER.md
```

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
compression, and finite repeated-defect persistence do not force exact cyclic
source matching; CRT realizes those local constraints at infinitely many starts.

Sources:

```text
docs/CYCLIC_ROTATION_CLOSURE_GCD.md
docs/FIXED_LOCAL_ENDPOINT_CONGRUENCE_NO_GO.md
docs/FULL_FINITE_TWO_SIDED_WORD_GLUING_NO_GO.md
docs/COMPLETE_BLOCK_GCD_COMPRESSION_NO_GO.md
docs/GEOMETRIC_FACTOR_STRONG_DIVISIBILITY_PERSISTENCE_NO_GO.md
```

## Global block-gcd and phase sieve

Let `ell_i` be all complete-block lengths of a hypothetical cycle and put

```text
h=gcd_i ell_i,
D=sum_i(4501-a_i),
S_h=(B^h-X^h)/d,
g=gcd of all complete-block boundaries b_i.
```

Exact closure proves

```text
g=gcd(b_i,S_h) for every b_i,
S_h/g divides 2^D-1,
S_h/gcd(S_h,2^D-1) divides g divides S_h.
```

Every cycle state also obeys the endogenous phase sieve

```text
n_t==B^(-j)*S_j (mod g),
j=t mod h.
```

Thus the entire cycle lies in at most `h` explicit residue classes modulo a
common boundary divisor forced by global closure.

Regression:

```text
X=5,
43 -> 27 -> 17 -> 43,
h=3,
D=2,
S_3=129,
g=43,
S_3/g=3 divides 2^2-1.
```

Sources:

```text
docs/GLOBAL_BLOCK_GCD_PHASE_SIEVE.md
tools/verify_global_block_gcd_phase_sieve.py
```

## Nonpositive-return specialization

On `R<=0`, total credit satisfies `1<=D<=4500`. For the primary candidate,

```text
gcd(S_2,2^D-1)=1 for every 1<=D<=4500,
S_2=B+X.
```

If `h` is even, then `S_2|g`. The phase sieve reduces the entire cycle to two odd
residue classes modulo `2*S_2`. Exact harmonic packing and the retained
continued-fraction gap prove

```text
full cycle p>2^(2^4979),
actual return Lr>2^(2^4978),
L_exit<2^4006.
```

This improves the general `2^(2^974)` nonpositive frontier on the even-`h`
subcase, but does not exclude that subcase.

For every nonpositive-return cycle with `h>=2`, all complete-block boundaries
share a divisor greater than `2^4500`, coprime to
`(2^500-1)*1093^2`.

## Surviving branches

```text
positive credit: Lr>2^3990;
nonpositive, h even: Lr>2^(2^4978), still not excluded;
nonpositive, odd h>=3: large phase-divisor sieve remains to exploit;
nonpositive, h=1: no common geometric divisor is forced.
```

Decisive next target: derive a harmonic or adjacent-numerator gcd contradiction
from the odd-`h` phase classes. Secondary targets are forcing the actual return
into `h=1` or another impossible length pattern, and excluding positive credit.
A different candidate or a direct divergence invariant remains allowed if these
routes stall.

## Critical corrections

Do not use `2^A==1 (mod X)`. The correct cycle congruence is

```text
2^A*product_i(n_i)==1 (mod X).
```

Do not identify a least admissible predecessor with the predecessor actually used
by a cycle. Finite computation is not divergence. Full history is in
`docs/RETRACTIONS.md`.

## Verification state

The standalone checker

```text
python tools/verify_global_block_gcd_phase_sieve.py
```

passed all `4500` primary gcd cases, exact harmonic and exit inequalities, three
independently generated small cycles, and the `X=5` regression. It is included in
`run_checks.py`. A complete repository-wide run was not executed in the research
chat environment.