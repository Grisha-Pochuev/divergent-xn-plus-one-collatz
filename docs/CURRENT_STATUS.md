# Current status

## Strict target

Find explicit positive odd `X>=5,n0` such that

```text
C_X(n)=(X*n+1)/2^v2(X*n+1)
```

tends to positive infinity. The strict problem remains open.

## Primary candidate and proof gates

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
G4 bounded positive orbit implies eventual cycle: closed;
G5 final independent certificate: partial, waiting for G3.
```

## Permanent arithmetic structure

The following are proved exactly:

- `N|X`;
- `1093||X`;
- the orbit from `1` leaves `1` and never returns;
- every output lies in one of `500` classes modulo `N`;
- combining them with the `1093^2` adjacent-label coordinate gives exactly

```text
K=16562000
```

  classes modulo

```text
M=(2^500-1)*1093^2;
```

- every hypothetical cycle value is greater than `N`;
- the harmonic constants satisfy

```text
C0<10^(-147),
K/(2*M)<10^(-149),
```

  and every cycle obeys

```text
0<p*delta-D
 <[C0+K*H_(ceil(p/K))/(2*M)]/(X*ln(2)).
```

Files:

```text
docs/MERSENNE_DIVISOR_WIEFERICH_FAMILY.md
tools/verify_mersenne_divisor_wieferich_family.py
```

## Exact finite cycle barrier

For a hypothetical cycle,

```text
D=4501*p-A>=1.
```

The product inequality gives

```text
p>2*X/(3*d),
```

with

```text
10^1201<floor(2*X/(3*d))<10^1202.
```

This is a finite barrier, not a divergence proof.

## Exact exceptional-source floor

Every exceptional source satisfies

```text
v2(d*n-1)=4501.
```

Combining its progression with both permanent coordinates gives the first
compatible labels

```text
N-label=495,
1093-label pair=(161,311).
```

The exact odd-core coefficient is

```text
u_min=
141554173562669451979142234479211407387695161061947663158036275475013035570532072821977692485924548874811696146286209742307923384940182399969083204712328957713629782297601610389067903491331197096456313288013542743720638224927691460837892079910386115268969408753656537834465197519183303759432510875217219.
```

Thus every exceptional source satisfies

```text
n>=(u_min*2^4501+1)/(349*2^500-347).
```

The right side has `1505` decimal digits.

File:

```text
docs/MERSENNE_DIVISOR_EXCEPTIONAL_FLOOR.md
```

## No-exceptional cycles: exact block ledger

Suppose every complete block is ordinary. Let `J` be the number of blocks and
let their terminal deficits be `e_i`:

```text
1<=e_i<=4500,
D=4501*p-A=sum_(i=1)^J e_i,
J<=D.
```

### Full X-adic ladder

For a valuation-`4501` step,

```text
F(n)=(X*n+1)/2^4501,
F(n)-1/d=(X/2^4501)*(n-1/d).
```

After `j` consecutive such steps,

```text
d*F^j(n)==1 (mod X^j).
```

All `4500` terminal classes satisfy

```text
rho_e>X/(3*e).
```

Therefore every no-exceptional cycle obeys

```text
sum_i 1/n_i
 <3*D/X+[d+H_D/2]/(X-1),
```

and the stronger correction window

```text
0<p*delta-D
 <{3*D/X+[d+H_D/2]/(X-1)}/[X*ln(2)].
```

Files:

```text
docs/NO_EXCEPTIONAL_X_ADIC_LADDER.md
tools/verify_no_exceptional_x_adic_ladder.py
```

### One and two blocks are completely excluded

For one block, exact closure is

```text
[2^(4501*p-e)-X^p]*u=2^e-1.
```

Exact rational logarithmic bounds prove that the first positive gap already
exceeds the additive term for every

```text
1<=e<=4500.
```

Hence no ordinary one-block cycle exists for any length.

For two blocks, choose one as the shorter block. The complete additive numerator
is less than

```text
2*B^(floor(p/2)+1),
```

while the positive gap is strictly larger for every total deficit

```text
2<=D<=9000.
```

Hence no ordinary two-block cycle exists.

Files:

```text
docs/NO_EXCEPTIONAL_ONE_BLOCK_ALL_CREDITS.md
tools/verify_no_exceptional_one_block_all_credits.py

docs/NO_EXCEPTIONAL_TWO_BLOCK_ALL_CREDITS.md
tools/verify_no_exceptional_two_block_all_credits.py
```

### General block-count frontier

For `J` blocks, choose a longest block `ell_1`. Exact core elimination gives

```text
Delta_D(p)*u_1=R,
Delta_D(p)=2^(4501*p-D)-X^p,
R<J*B^(p-ell_1+1).
```

Exact logarithmic intervals certify the continued-fraction tail of

```text
beta=ln(2)/ln(B/X)
```

as

```text
[1,1,145062,23,1,4,1,12,2].
```

The last relevant upper semiconvergent has denominator

```text
573867416,
```

and the next upper convergent denominator is

```text
1106246945.
```

The one-sided best-approximation theorem and the longest-block bound prove:

```text
Any no-exceptional positive cycle must contain at least 245833 blocks.
```

Block lengths are unrestricted. This is not a cycle-length cutoff.

Files:

```text
docs/NO_EXCEPTIONAL_BLOCK_COUNT_FRONTIER.md
tools/verify_no_exceptional_block_count_frontIER.py
```

The filename in the repository uses lower-case `frontier`:

```text
tools/verify_no_exceptional_block_count_frontier.py
```

## Decisive remaining split

Every still-possible cycle belongs to one of three branches:

```text
A. no exceptional blocks and at least 245833 ordinary blocks;
B. exactly one exceptional block;
C. at least two exceptional blocks.
```

The primary next target is branch B. Write the cycle as one exceptional
contraction followed by an ordinary segment, then combine:

1. the 1505-digit exceptional-source floor;
2. the exact exceptional descent coordinate;
3. the full `X`-adic ladder on the ordinary segment;
4. a block-core closure inequality depending on the exceptional excess.

For branch A, the next useful theorem must use many-block populations and
repeated terminal deficits. Merely extending the continued-fraction denominator
is not a priority.

## Reusable family theorem

For

```text
N=2^k-1,
m==r (mod k),
d=2^r+t*N,
X=2^m-d,
```

with `364` not dividing `k`, a parity-correct `t<2*1093^2` can be chosen so
that `1093||X`. This yields an infinite family with no return to `1`, an
exponentially thin permanent sieve, and arbitrarily large finite barriers.

## Independent fallback branches

### `X=2^3803-4162203,n0=1`

- `17886960` permanent classes modulo `14726582775529`;
- finite barrier above `10^1138`;
- exceptional floor `(19567017189655*2^3803+1)/4162203`;
- harmonic base constant `1/853`.

### `X=2^156-9,n0=1`

- no return to `1`;
- all cycle lengths through

```text
7034970411803187993997906985047212163795395134
```

  are excluded;
- first ordinary-block threshold

```text
7034970411803187993997906985047212163795395135;
```

- exceptional floor

```text
1268664615738631005385143083955106787895774776889.
```

Other retained branches:

```text
X=2^260-3,
X=15,
X=9,
X=104350542602662257699.
```

For the last fixed candidate, all lengths through `355561454311274250377` are
excluded except

```text
177780727155637125193,
177780727155637125195.
```

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
used by a cycle.

## Verification

The exact calculations underlying the new checkers were run in the chat Python
environment. All new checkers are listed in `run_checks.py`.

A complete repository-wide run was not executed because the chat container had
no fresh checkout and could not resolve GitHub. Do not report a full-suite pass
until a checkout or GitHub Actions run completes.
