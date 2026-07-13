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

Every hypothetical cycle contains an actual consecutive exit from the least
ordinary boundary `x` to the next ordinary boundary `y>x` with

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

Files:

```text
docs/MINIMUM_BOUNDARY_ACTUAL_EXPANDING_SEGMENT.md
docs/MINIMUM_BOUNDARY_RETURN_CREDIT_DICHOTOMY.md
docs/MINIMUM_BOUNDARY_NONPOSITIVE_RETURN_HARMONIC_BARRIER.md
```

## Exact cyclic closure

For a cyclic valuation word, with rotations `U_k` and affine numerators `Q_k`,

```text
Delta=2^A-X^p,
2^a_k*Q_(k+1)=X*Q_k+Delta.
```

The word closes to a positive cycle iff `Delta>0` and `Delta|Q_0`, equivalently
iff a truly adjacent pair satisfies

```text
gcd(Q_k,Q_(k+1))=Delta.
```

## Closed local approaches

For a complete block of length `ell`,

```text
S_ell=(B^ell-X^ell)/d,
gcd(n,n')=gcd(n,S_ell),
gcd(S_r,S_s)=S_gcd(r,s).
```

Finite endpoint congruences, full finite two-sided word gluing, naive block
compression, and finite repeated-defect arguments do not supply exact cycle
closure. CRT realizes their local constraints at infinitely many positive starts.

Files:

```text
docs/FIXED_LOCAL_ENDPOINT_CONGRUENCE_NO_GO.md
docs/FULL_FINITE_TWO_SIDED_WORD_GLUING_NO_GO.md
docs/COMPLETE_BLOCK_GCD_COMPRESSION_NO_GO.md
docs/GEOMETRIC_FACTOR_STRONG_DIVISIBILITY_PERSISTENCE_NO_GO.md
```

## Global common-boundary divisor theorem

Let `ell_i` be all complete-block lengths of a hypothetical cycle. Put

```text
h=gcd_i ell_i,
D=sum_i(4501-a_i),
S_h=(B^h-X^h)/d,
g=gcd of all complete-block boundaries b_i.
```

Exact cyclic closure gives

```text
g=gcd(b_i,S_h) for every boundary b_i,               (1)
S_h/g divides 2^D-1,                                 (2)
S_h/gcd(S_h,2^D-1) divides g divides S_h.            (3)
```

It also gives the endogenous phase sieve

```text
n_t==B^(-j)*S_j (mod g),
j=t mod h.                                            (4)
```

Thus the full cycle lies in at most `h` explicit residue classes modulo a common
boundary divisor forced by closure. This is stronger than the previous finite
CRT persistence result.

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

Files:

```text
docs/GLOBAL_BLOCK_GCD_PHASE_SIEVE.md
tools/verify_global_block_gcd_phase_sieve.py
```

## Even-h nonpositive-return frontier

On `R<=0`, total cycle credit satisfies `1<=D<=4500`. For the primary candidate,
the exact certificate proves

```text
gcd(S_2,2^D-1)=1 for every 1<=D<=4500,
S_2=B+X.
```

If `h` is even, then `S_2|g`. Equation (4) reduces the cycle to two odd residue
classes modulo `2*S_2`. Exact harmonic packing in those classes and the retained
continued-fraction gap prove

```text
full cycle p>2^(2^4979),
actual return Lr>2^(2^4978),
L_exit<2^4006.
```

This strictly improves the general `2^(2^974)` nonpositive frontier on the
entire even-`h` subcase. It is still a frontier, not a cycle exclusion.

For every nonpositive-return cycle with `h>=2`, all complete-block boundaries
share a divisor greater than `2^4500`. It is coprime to the permanent-sieve
modulus `(2^500-1)*1093^2`.

## Surviving branches

```text
positive credit: Lr>2^3990;
nonpositive, h even: Lr>2^(2^4978);
nonpositive, odd h>=3: large h-phase divisor sieve remains to exploit;
nonpositive, h=1: no common geometric divisor is forced.
```

The best next targets are:

1. obtain a harmonic contradiction from the odd-`h` phase classes;
2. prove the actual return forces `h=1` or another impossible length pattern;
3. turn the phase sieve into an adjacent-numerator gcd obstruction;
4. exclude the positive-credit return branch;
5. find a different candidate or direct divergence invariant.

## Retractions

Do not use `2^A==1 (mod X)`. The correct cycle congruence is

```text
2^A*product_i(n_i)==1 (mod X).
```

Do not identify a least admissible predecessor with the predecessor actually
used by a cycle. Finite computation is not divergence.

## Verification

The new standalone checker passed and is included in `run_checks.py`:

```text
python tools/verify_global_block_gcd_phase_sieve.py
```

It verifies all `4500` primary gcd cases, exact harmonic and exit inequalities,
three independently generated small cycles, and the `X=5` regression. A complete
repository-wide run was not executed in the research chat environment.
