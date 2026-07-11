# Current status

## Strict target

Find explicit positive odd `X>=5,n0` such that

```text
C_X(n)=(X*n+1)/2^v2(X*n+1)
```

tends to positive infinity. The strict problem remains open.

## Proof gates for the primary candidate

```text
k=500,
N=2^500-1,
m=4501,
B=2^4501,
d=349*2^500-347=2+349*N,
X=B-d=2^4501-349*2^500+347,
n0=1.
```

```text
G1 explicit pair: closed;
G2 leaves 1 and never returns: closed;
G3 every nontrivial positive cycle excluded: open;
G4 positive bounded-orbit dichotomy: closed as a general lemma;
G5 final independently checked certificate: partial, waiting for G3.
```

This candidate replaced `X=2^3803-4162203` on 2026-07-12. It has both a
larger finite cycle barrier and exponentially smaller harmonic-packing
constants, while keeping an exact exceptional-source certificate.

## General Mersenne-divisor Wieferich family

Let

```text
N=2^k-1,
m==r (mod k),
d=2^r+t*N,
X=2^m-d.
```

If `d` is odd, `d<2^(m-1)`, `364` does not divide `k`, and `1093||X`, then:

- `N|X`;
- the orbit from `1` leaves `1` and never returns;
- every output lies in exactly `k` classes modulo `N`;
- after combining with the `1093^2` adjacent-label coordinate, every cycle
  value lies in exactly

```text
K=364*lcm(k,364)
```

  classes modulo

```text
M=N*1093^2;
```

- the retained density and harmonic coefficients decrease exponentially with
  `k`;
- the elementary finite barrier can be made arbitrarily large by increasing
  `m-k`.

For every admissible `k,m,r`, a parity-correct `t<2*1093^2` with `1093||X`
exists after avoiding at most one lift modulo `1093^2`.

This is a reusable infinite-family theorem. It also proves that merely enlarging
the modulus or finite barrier is not the missing final idea.

Files:

```text
docs/MERSENNE_DIVISOR_WIEFERICH_FAMILY.md
tools/verify_mersenne_divisor_wieferich_family.py
```

## Retained structure for the primary candidate

### No return to `1`

The inequalities

```text
2^4500<X+1<2^4501
```

show that the first accelerated step leaves `1`. Every accelerated output is
coprime to `1093`. If an output `y` mapped to `1`, then

```text
X*y+1=2^a.
```

The exact order `364` and the Wieferich congruence modulo `1093^2` force
`1093^2|X*y`. Since `1093||X`, this would imply `1093|y`, a contradiction.

### Exact one-label sieve

Because

```text
N=2^500-1
```

divides `X`, every accelerated output satisfies

```text
n_(i+1)==2^(-a_i) (mod N).
```

The order of `2` modulo `N` is exactly `500`, so only the `500` classes

```text
1,2,4,...,2^499 (mod N)
```

can occur. Since cycle values are odd and cannot equal `1`, their least allowed
representatives are

```text
1+2*N,
N+2,
N+4,
...,
N+2^499.
```

In particular every hypothetical cycle value satisfies

```text
n_i>N=2^500-1.
```

### Combined permanent sieve

The current valuation labels modulo `500` and `364` must agree modulo

```text
gcd(500,364)=4.
```

Combining the one-label coordinate with the `1093^2` adjacent-label coordinate
gives exactly

```text
K=16562000
```

permanent classes modulo

```text
M=(2^500-1)*1093^2.
```

Their density is between `10^143` and `10^144` times smaller than for the
previous candidate `X=2^3803-4162203`.

### Global harmonic packing

The least allowed representatives of the `500` one-label classes satisfy

```text
S_500<500/N.
```

Let

```text
C0=(500/N)*(1+H_33124/2).
```

Exact rational arithmetic proves

```text
10^(-148)<C0<10^(-147),
10^(-150)<K/(2*M)<10^(-149).
```

Every hypothetical positive cycle of length `p` therefore obeys

```text
sum_i 1/n_i
 <C0+K*H_(ceil(p/K))/(2*M).
```

With

```text
D=4501*p-A,
delta=log2(2^4501/X),
```

the exact cycle product gives the infinite-family restriction

```text
0<p*delta-D
 <[C0+K*H_(ceil(p/K))/(2*M)]/(X*ln(2)).
```

### Finite cycle barrier

The standard near-power product inequalities give

```text
D>=1,
D<3*p*d/(2*X),
```

and hence

```text
p>2*X/(3*d).
```

For the primary candidate,

```text
10^1201<floor(2*X/(3*d))<10^1202.
```

This remains a finite barrier, not a proof of divergence.

### Exact exceptional-source floor

The exceptional condition

```text
v2(d*n-1)=4501
```

is one progression modulo `2^4502`. Combining it with both permanent
coordinates proves that the first compatible layer has labels

```text
N-label=495,
1093-label pair=(161,311).
```

The exact odd-core coefficient is

```text
u_min=
141554173562669451979142234479211407387695161061947663158036275475013035570532072821977692485924548874811696146286209742307923384940182399969083204712328957713629782297601610389067903491331197096456313288013542743720638224927691460837892079910386115268969408753656537834465197519183303759432510875217219.
```

Therefore every exceptional cycle source satisfies

```text
n>=(u_min*2^4501+1)/(349*2^500-347).
```

The right side has `1505` decimal digits. Minimality is certified using only the
`500` one-label layers and `364^2` adjacent-label layers.

File:

```text
docs/MERSENNE_DIVISOR_EXCEPTIONAL_FLOOR.md
```

## Decisive missing theorem

No theorem yet excludes every cycle above the finite barrier. The family theorem
shows that raw sieve density and barrier size can be strengthened without limit,
so further record construction is not a priority.

The remaining target is to connect the dynamic block ledger

```text
D=sum ordinary terminal deficits-sum exceptional excess valuations
```

with the harmonic upper window. The first exact split is:

```text
no exceptional blocks;
exactly one exceptional block;
at least two exceptional blocks.
```

For each case the project needs a lower bound for `p*delta-D` that uses:

1. the sequence of compatible `500`- and `364`-labels;
2. the length and credit of every complete near-power block;
3. the 1505-digit floor for exceptional sources;
4. height dependence, not a fixed finite-state positive-mean potential.

## Independent fallback branches

### Previous primary: `X=2^3803-4162203,n0=1`

Retained strict results:

```text
m=3803,
d=4162203,
X=2^3803-4162203.
```

- `3511^2|X` and `1093||X`;
- the orbit leaves `1` and never returns;
- exactly `17886960` permanent classes survive modulo
  `14726582775529`;
- every cycle length through a `1139`-digit barrier greater than `10^1138` is
  impossible;
- every exceptional source satisfies

```text
n>=(19567017189655*2^3803+1)/4162203;
```

- every cycle obeys the harmonic window with base constant `1/853`.

### Former primary: `X=2^156-9,n0=1`

Retained strict results:

```text
X=91343852333181432387730302044767688728495783927.
```

- `1093||X`, so the orbit leaves `1` and never returns;
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

### `X=2^260-3,n0=1`

Return to `1` is impossible, all positive cycle lengths through approximately
`4.117*10^77` are excluded, and the first `172` steps have exact word
`(1,2)^86`.

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

The following new standalone checkers passed in the chat environment and are
included in `python run_checks.py`:

```text
tools/verify_dual_wieferich_square_sieve_candidate.py
tools/verify_dual_wieferich_harmonic_packing.py
tools/verify_mersenne_divisor_wieferich_family.py
```

A complete repository-wide run was not executed in the chat container because
a fresh GitHub checkout was unavailable there.
