# Current status

## Strict target

Find explicit positive odd `X>=5,n0` such that

```text
C_X(n)=(X*n+1)/2^v2(X*n+1)
```

tends to positive infinity.  The strict problem remains open.

## Proof gates for the primary candidate

```text
X=2^156-9
 =91343852333181432387730302044767688728495783927,
n0=1.
```

```text
G1 explicit pair: closed;
G2 leaves 1 and never returns: closed;
G3 every nontrivial positive cycle excluded: open;
G4 positive bounded-orbit dichotomy: closed as a general lemma;
G5 final independently checked certificate: partial, waiting for G3.
```

## Retained structure for `X=2^156-9`

### No return

The Wieferich prime `1093` divides `X` exactly once and satisfies

```text
ord_1093(2)=364,
2^364==1 (mod 1093^2).
```

The orbit from `1` leaves immediately and can never return to `1`.

### Exact initial program

The first `48` accelerated steps have word

```text
(3,1,2,2,5,6)^8,
```

with total valuation `152`, endpoint precision `v2(n_48-1)=4`, and

```text
n_48>X^48/2^152.
```

### Sharp ordinary-block signs

For every complete nonexceptional block, with terminal deficit
`e=156-s`, the exact threshold

```text
L_e=floor(e/log2(2^156/X))+1
```

satisfies

```text
ell<L_e   => strict growth,
ell>=L_e  => strict contraction.
```

All `155` terminal deficits are covered.  The first threshold is

```text
L_1=7034970411803187993997906985047212163795395135.
```

Therefore every positive cycle length through

```text
7034970411803187993997906985047212163795395134
```

is impossible.  This remains a finite barrier.

### Exact cycle-wide block ledger

Every hypothetical cycle has a canonical partition into complete near-power
blocks.  If

```text
D=156*p-A,
```

then

```text
D=sum ordinary terminal deficits-sum exceptional excess valuations.
```

Every exceptional block ending at valuation `156+b` contracts by more than `b`
binary height units.  Exact block ratios yield

```text
sum kappa_j=p*delta-D,
delta=log2(2^156/X),
```

and the uniform estimate

```text
p*(delta-9/(2*X*ln(2)))<D<p*delta.
```

Thus `D` is restricted to roughly the upper half of its old interval.

### Permanent adjacent-label sieve

Two adjacent least valuation labels determine every cycle value modulo
`1093^2`.  Exactly

```text
132496
```

classes survive out of `397852` one-step output classes.

### Exceptional-source combined sieve

The exact exceptional condition is

```text
v2(9*n-1)=156.
```

Combining its single progression modulo `2^157` with all permanent classes
modulo `1093^2` proves that every exceptional source in a hypothetical cycle
satisfies

```text
n>=(125*2^156+1)/9
 =1268664615738631005385143083955106787895774776889.
```

The minimum corresponds to adjacent labels `(61,64)`.  It is approximately
`7.35` times the unsieved exceptional-source floor.

Main new files:

```text
docs/NEAR_POWER_SHARP_BLOCK_SIGN.md
tools/verify_near_power_block_sign_threshold.py

docs/NEAR_POWER_CYCLE_BLOCK_LEDGER.md
tools/verify_near_power_cycle_block_ledger.py

docs/X156_EXCEPTIONAL_Q2_SIEVE.md
tools/verify_x156_exceptional_q2_sieve.py
```

## Decisive missing theorem

No result yet excludes every cycle above the finite barrier.  The next target is
to show that distinct values in the `132496` permanent classes cannot supply
the exact block correction mass

```text
p*delta-D.
```

The intended attack combines:

1. the new integer strip for `D`;
2. exact ordinary and exceptional block credits;
3. the exceptional-source floor above `1.268*10^48`;
4. distinct-value harmonic packing;
5. an unbounded height-dependent potential.

## Independent fallback branches

### `X=2^260-3,n0=1`

- return to `1` is impossible;
- all positive cycle lengths through approximately `4.117*10^77` are excluded;
- the first `172` steps have exact word `(1,2)^86`.

### `X=15,n0=3`

Complete Mersenne blocks and the second-block escalation are classified.  Later
contractions and return to `1` remain open.

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

is retracted.  The correct cycle congruence is

```text
2^A*product_i(n_i)==1 (mod X).
```

See `docs/RETRACTIONS.md`.

## Verification

The three new standalone checkers pass and are included in

```text
python run_checks.py
```

A complete repository-wide run was not executed in the chat container because
a fresh GitHub checkout was unavailable there.
