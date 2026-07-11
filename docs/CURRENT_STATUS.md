# Current status

## Strict target

Find explicit positive odd `X>=5,n0` such that

```text
C_X(n)=(X*n+1)/2^v2(X*n+1)
```

tends to positive infinity. The strict problem remains open.

## Proof gates for the primary candidate

```text
m=3803,
B=2^3803,
d=4162203,
X=B-d,
n0=1.
```

```text
G1 explicit pair: closed;
G2 leaves 1 and never returns: closed;
G3 every nontrivial positive cycle excluded: open;
G4 positive bounded-orbit dichotomy: closed as a general lemma;
G5 final independently checked certificate: partial, waiting for G3.
```

This candidate replaced `X=2^156-9` on 2026-07-12 because its permanent
residue density is more than `91312` times smaller and it supports a global
harmonic-packing inequality. The former primary branch remains valid and is
retained below.

## Retained structure for `X=2^3803-4162203`

### Complementary Wieferich divisors

Exact modular arithmetic proves

```text
ord_(3511^2)(2)=1755,
v_3511(X)=2,

ord_(1093^2)(2)=364,
v_1093(X)=1.
```

Thus `3511^2|X` supplies a one-label permanent coordinate, while `1093||X`
supplies the no-return argument and an adjacent-label coordinate.

### No return to `1`

The first accelerated step has valuation `1`, so the orbit leaves `1`.
Every accelerated output is coprime to `1093`. If an output `y` mapped to `1`,
then

```text
X*y+1=2^a.
```

The exact order and Wieferich congruence force `1093^2|X*y`; because
`1093||X`, this would give `1093|y`, a contradiction. Therefore

```text
C_X^t(1) != 1 for every t>=1.
```

### One-label and combined permanent sieves

Because `3511^2|X`, every accelerated output satisfies

```text
n_(i+1)==2^(-a_i) (mod 3511^2).
```

There are exactly `1755` possible output classes modulo

```text
3511^2=12327121.
```

Combining this coordinate with the `1093^2` adjacent-label coordinate and the
compatibility of current valuation labels modulo

```text
gcd(1755,364)=13
```

gives exactly

```text
K=17886960
```

permanent classes modulo

```text
M=3511^2*1093^2=14726582775529.
```

Their density is approximately

```text
1.214603569*10^(-6),
```

between `91312` and `91313` times smaller than the former primary sieve density
`132496/1093^2`.

### Finite cycle barrier

For a hypothetical positive cycle of length `p` and total valuation `A`, put

```text
D=3803*p-A.
```

The cycle product gives `D>=1` and

```text
D<3*p*d/(2*X).
```

Hence every positive cycle length through

```text
floor(2*X/(3*d))
```

is impossible. This exact barrier has `1139` decimal digits and is greater than

```text
10^1138.
```

It remains a finite barrier, not a proof of divergence.

### Exceptional-source combined sieve

The exact exceptional condition is

```text
v2(d*n-1)=3803.
```

It is one progression modulo `2^3804`. Combining that progression with both
permanent residue coordinates and checking every smaller layer proves that the
first compatible layer is

```text
T=2350560,
3511-label=40,
1093-label pair=(99,222).
```

Consequently every exceptional source in any hypothetical positive cycle
satisfies

```text
n>=(19567017189655*2^3803+1)/4162203.
```

The raw exceptional odd-core coefficient is only `1422295`; the permanent sieve
increases it by a factor greater than `13757000`.

### Global harmonic packing

For the `1755` square-sieve classes, exact rational summation of their least
allowed positive odd representatives gives

```text
sum 1/rho <1/2110.
```

A two-level residue-class packing argument proves that the least representatives
of all `K` combined classes satisfy

```text
sum_(j=1)^K 1/sigma_j <1/853.
```

Therefore every hypothetical positive cycle of length `p` obeys

```text
sum_i 1/n_i
 <1/853 + K*H_(ceil(p/K))/(2*M).
```

Let

```text
delta=log2(2^3803/X).
```

The exact cycle product then gives the infinite-family restriction

```text
0<p*delta-D
 <[1/853 + K*H_(ceil(p/K))/(2*M)]/(X*ln(2)).
```

The right side grows only logarithmically with `p`, rather than linearly. This
is the strongest global cycle restriction currently available in the project.

Main files:

```text
docs/DUAL_WIEFERICH_SQUARE_SIEVE_CANDIDATE.md
tools/verify_dual_wieferich_square_sieve_candidate.py

docs/DUAL_WIEFERICH_HARMONIC_PACKING.md
tools/verify_dual_wieferich_harmonic_packing.py
```

## Decisive missing theorem

No result yet excludes every cycle above the finite barrier. The remaining
target is to combine the logarithmic harmonic window with the exact near-power
block ledger

```text
D=sum ordinary terminal deficits-sum exceptional excess valuations.
```

The intended attack is:

1. split by the number of exceptional blocks;
2. use the exceptional-source floor to charge every exceptional contraction;
3. derive a block-credit-dependent lower bound for `p*delta-D`;
4. compare that lower bound with the harmonic upper window;
5. use continued-fraction or exact rational windows only after the credit
   patterns restrict the admissible integer pairs `(p,D)`.

## Independent fallback branches

### Former primary: `X=2^156-9,n0=1`

Retained strict results:

```text
X=91343852333181432387730302044767688728495783927.
```

- `1093` divides `X` exactly once, so the orbit leaves `1` and never returns;
- the first `48` steps have word `(3,1,2,2,5,6)^8` and total valuation `152`;
- all positive cycle lengths through

```text
7034970411803187993997906985047212163795395134
```

  are impossible;
- the first ordinary-block threshold is

```text
7034970411803187993997906985047212163795395135;
```

- exactly `132496` permanent adjacent-label classes modulo `1093^2` survive;
- every exceptional cycle source satisfies

```text
n>=1268664615738631005385143083955106787895774776889.
```

This branch has a much smaller block alphabet (`155` deficits) but a far denser
permanent sieve.

### `X=2^260-3,n0=1`

- return to `1` is impossible;
- all positive cycle lengths through approximately `4.117*10^77` are excluded;
- the first `172` steps have exact word `(1,2)^86`.

### `X=15,n0=3`

Complete Mersenne blocks and the second-block escalation are classified. Later
contractions and return to a nontrivial cycle remain open.

### `X=9,n0=1`

The sufficient target remains

```text
A_t<=3*t-1 for every t>=1.
```

### Previous fixed candidate

For

```text
X=104350542602662257699,
n0=1,
```

all lengths through `355561454311274250377` are excluded except

```text
177780727155637125193,
177780727155637125195.
```

The first surviving length still allows `6242` integer layer totals.

## Retractions

The former `10^37` argument based on

```text
2^A==1 (mod X)
```

is retracted. The correct cycle congruence is

```text
2^A*product_i(n_i)==1 (mod X).
```

Do not identify a least admissible predecessor source with the source actually
used by a cycle. See `docs/RETRACTIONS.md`.

## Verification

The two new standalone checkers passed in the chat environment and are included
in

```text
python run_checks.py
```

The exceptional-source checker exhaustively verifies all progression layers
below `T=2350560`. The harmonic checker uses exact rational arithmetic.

A complete repository-wide run was not executed in the chat container because
a fresh GitHub checkout was unavailable there.
