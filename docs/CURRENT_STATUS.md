# Current status

## Strict target

Find explicit positive odd `X>=5,n0` such that

```text
C_X(n)=(X*n+1)/2^v2(X*n+1)
```

tends to positive infinity.  The strict problem remains open.

## Proof-gate status

For the current structured candidate

```text
X=2^156-9
 =91343852333181432387730302044767688728495783927,
n0=1,
```

the repository has:

```text
explicit pair: closed;
leaves 1 and never returns: closed;
positive bounded-orbit dichotomy: available;
all nontrivial cycles excluded: open;
final end-to-end certificate: open.
```

The project reports proof gates, finite frontiers, and reusable structure rather
than one precise completion percentage.

## Structured hybrid candidate `X=2^156-9`

### No return to `1`

For `q=1093`,

```text
ord_q(2)=364,
2^364==1 (mod q^2),
q divides X exactly once.
```

Any direct predecessor of `1` is divisible by `q`, while every accelerated
output is coprime to `q`.  Hence

```text
C_X^t(1)!=1 for every t>=1.
```

### Exact finite cycle barrier

For a hypothetical cycle of length `p` and total valuation `A`,

```text
D=156*p-A
```

is a positive integer satisfying

```text
D<p*log2(2^156/X).
```

Exact rational logarithm bounds give

```text
p>=7034970411803187993997906985047212163795395135.
```

Thus every positive cycle length through

```text
7034970411803187993997906985047212163795395134
```

is impossible.  This improves the former convenient barrier

```text
6766211283939365362054096447760569535444132142
```

by about `3.97%`.  Cycles above the new finite barrier remain possible.

### Exact initial program

The first `48` accelerated steps have exact valuation word

```text
(3,1,2,2,5,6)^8,
```

with

```text
A_48=152,
v2(n_48-1)=4,
n_48>X^48/2^152.
```

The six-step map is

```text
G(n)=C_X^6(n)
 =[X^6*n+X^5+8*X^4+16*X^3+64*X^2+256*X+8192]/2^19.
```

For `n==1 (mod 2^20)` it has the displayed exact word.  If
`20<=L=v2(n-1)<156`, then

```text
v2(G(n)-1)=L-19.
```

### Sharp nonexceptional block signs

For a complete nonexceptional near-power block, write

```text
9*n-1=2^(156*k+s)*u,
1<=s<=155,
ell=k+1,
e=156-s.
```

Define

```text
L_e=floor(e/log2(2^156/X))+1.
```

Exact rational and modular certificates prove, for every `e=1,...,155`,

```text
ell<L_e   => C_X^ell(n)>n,
ell>=L_e  => C_X^ell(n)<n.
```

The sign is independent of the odd core `u`.  The additive term never rescues a
block after the leading multiplier crosses below `1`.

Files:

```text
docs/NEAR_POWER_SHARP_BLOCK_SIGN.md
tools/verify_near_power_block_sign_threshold.py
```

### Adjacent-label sieve

Two adjacent least valuation labels determine the full residue modulo
`1093^2`.  Exactly

```text
132496
```

classes survive out of `397852` one-step output classes.

### Missing theorem

The initial repeated program ends after eight blocks.  The sharp sign theorem
classifies every later nonexceptional block, but no cycle-wide credit inequality
has yet proved that all contractions are unaffordable.

The leading target is an unbounded height-credit ledger combined with the
permanent `1093^2` class sieve and distinct-value harmonic bounds.

## Larger-barrier hybrid candidate `X=2^260-3`

```text
X=2^260-3,
n0=1.
```

Retained facts:

- return to `1` is impossible;
- every positive cycle length through

```text
411705206177124250394919057808668116811626612144499783251404743139246683164216
```

  is excluded;
- the first `172` steps have exact word `(1,2)^86`;
- `A_172=258`, `v2(n_172-1)=2`, and `n_172>X^172/2^258`;
- a least seed entering a hypothetical cycle lies in a low near-power layer and
  begins with a growing step.

This candidate has the stronger finite barrier, but the `2^156-9` candidate has
the cleaner renewal program and sharper block structure.

## Complete near-power structure

For

```text
X=2^m-d,
d*n-1=2^(m*k+s)*u,
1<=s<=m-1,
```

the exact block endpoint is

```text
C_X^(k+1)(n)=(X^(k+1)*u+2^(m-s))/d.
```

Multiple-of-`m` exceptional blocks are strictly contracting.  Therefore the
least seed entering a hypothetical cycle must satisfy

```text
1<=v2(d*w-1)<m
```

and its first step grows.

## Mersenne branch `X=15,n0=3`

The second complete block of a least hypothetical basin seed cannot be
exceptional.  A contracting second block must increase the terminal type.
Remaining families:

```text
initial type 3: none;
initial type 2: terminal type 3, 10<=k<=20;
initial type 1: terminal type 2, 21<=k<=31,
                or terminal type 3, 10<=k<=31.
```

Later contractions and return to `1` remain open.

## Direct-growth branch `X=9,n0=1`

The sufficient target remains

```text
A_t<=3*t-1 for every t>=1.
```

Large valuations require an exact alternating base-8 suffix.  No amortized proof
for all times is known.

## Previous fixed-candidate frontier

For

```text
X=104350542602662257699,
n0=1,
```

all cycle lengths

```text
p<=177780727155637125192
```

are impossible, and all lengths through

```text
355561454311274250377
```

are excluded except

```text
177780727155637125193,
177780727155637125195.
```

At the first surviving length,

```text
Q<=6241,
```

so `6242` layer totals remain.  This is an independent finite-cycle branch.

## Retractions

The former `10^37` barrier based on

```text
2^A==1 (mod X)
```

is retracted.  The correct cycle congruence is

```text
2^A*product_i(n_i)==1 (mod X).
```

See `docs/RETRACTIONS.md` for all permanent audit rules.

## Not established

- No explicit positive orbit has been proved divergent.
- No candidate has every nontrivial positive cycle excluded.
- A finite cycle barrier, however large, is not divergence.
- The exact initial macroblocks do not repeat indefinitely by a proved ordinary
  integer renewal.
- The sharp block-sign theorem does not yet supply a cycle-wide credit balance.

## Exact next step

1. Partition a hypothetical `X=2^156-9` cycle into complete near-power blocks.
2. Express exceptional contractions and nonexceptional contractions
   `ell>=L_e` in one height-credit unit.
3. Seek an unbounded telescoping potential, not a fixed finite-state potential.
4. Combine the result with the `132496` adjacent-label classes.
5. Keep the `2^260-3`, `X=15`, `X=9`, and old `Q=6241` branches independent.

## Reproduction

```text
python run_checks.py
```
