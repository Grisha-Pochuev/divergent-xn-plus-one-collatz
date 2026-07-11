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

Proof gates:

```text
G1 explicit pair: closed;
G2 leaves 1 and never returns: closed;
G3 every nontrivial positive cycle excluded: open;
G4 bounded positive orbit implies eventual cycle: closed;
G5 final certificate: waits for G3.
```

## Retained arithmetic structure

- `N|X` and `1093||X`;
- the orbit from `1` leaves `1` and never returns;
- every output lies in `500` classes modulo `N`;
- the combined `N` and `1093^2` sieve leaves exactly `16562000` classes;
- every cycle value is greater than `N`;
- every exceptional source has at least `1505` decimal digits;
- every cycle length through a number between `10^1201` and `10^1202` is
  impossible;
- every cycle obeys the harmonic correction window from
  `MERSENNE_DIVISOR_WIEFERICH_FAMILY.md`.

## X-adic structure

For a valuation-`4501` step,

```text
F(n)=(X*n+1)/2^4501,
F(n)-1/d=(X/2^4501)*(n-1/d).
```

Thus after `j` consecutive such steps,

```text
d*F^j(n)==1 (mod X^j).
```

All `4500` ordinary terminal classes satisfy

```text
rho_e>X/(3*e).
```

## Local infinite exclusions

The following are completely excluded for all admissible lengths:

- one ordinary block;
- two ordinary blocks;
- one exceptional block plus one ordinary block.

## Global ordinary-block frontier

Let

```text
J = number of ordinary complete blocks,
R = number of exceptional complete blocks,
E = sum ordinary deficits,
F = sum exceptional excesses,
D = E-F = 4501*p-A.
```

Exact signed elimination of all block cores gives

```text
2^E*Delta_D(p)*u_0=signed additive sum,
Delta_D(p)=2^(4501*p-D)-X^p.
```

Ordinary blocks contribute positive terms and exceptional blocks contribute
negative terms. Dropping all negative terms proves:

```text
selected ordinary length L:
Delta_D(p)*u<J*B^(p-L+J+1);

selected exceptional length k:
Delta_D(p)*v<J*B^(p-k+J).
```

The exact continued-fraction certificate gives, for
`0<D<1106246945`,

```text
Delta_D(p)>2^(4501*p-D-22206).
```

If `J<=245832`, then `D<=4500J-1`, so comparison forces

```text
every ordinary block length <=2J+6;
every exceptional block length <=2J+5;
R<=4500J-1.
```

Consequently

```text
p<=544026748963771<10^15,
```

contradicting the retained barrier `p>10^1201`.

Therefore:

```text
Every hypothetical nontrivial positive cycle contains at least
245833 ordinary complete blocks.
```

This allows arbitrary exceptional-block populations and arbitrary lengths. It
is not a finite trajectory or cycle-length cutoff.

Files:

```text
docs/GLOBAL_ORDINARY_BLOCK_COUNT_FRONTIER.md
tools/verify_global_ordinary_block_count_frontier.py
```

## Decisive missing theorem

There are only `4500` ordinary terminal deficits. Hence every surviving cycle
contains one deficit at least `55` times.

The next target is a many-block population theorem using:

1. repeated boundary classes modulo `X` and `N`;
2. the exceptional credit budget `F=E-D`;
3. the full `X`-adic ladder;
4. a short positive-credit segment, height descent, or impossible closure
   congruence between repeated terminal types.

Do not merely enlarge the continued-fraction denominator or finite barrier.

## Reusable family theorem

For

```text
N=2^k-1,
m==r (mod k),
d=2^r+t*N,
X=2^m-d,
```

with `364` not dividing `k`, one can choose parity-correct
`t<2*1093^2` with `1093||X`. This gives no return to `1`, an exponentially
thin permanent sieve, and an arbitrarily large finite barrier.

## Retractions

Do not use

```text
2^A==1 (mod X).
```

The correct cycle congruence is

```text
2^A*product_i(n_i)==1 (mod X).
```

Do not identify a least admissible predecessor source with the source actually
used by a cycle.

## Verification

The new standalone checkers passed in the chat environment and are included in
`run_checks.py`. A complete repository-wide run was not executed.