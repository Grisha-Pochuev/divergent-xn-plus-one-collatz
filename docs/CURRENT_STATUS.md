# Current status

## Strict target

Find explicit positive odd `X>=5,n0` such that the accelerated odd-only orbit

```text
C_X(n)=(X*n+1)/2^v2(X*n+1)
```

tends to positive infinity. The strict problem remains open.

## Proof-gate status

For the current structured candidate:

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

The project no longer reports one precise completion percentage. See
`docs/PROGRESS_METRICS.md`.

## Structured hybrid candidate `X=2^156-9`

### Wieferich no-return theorem

For `q=1093`,

```text
ord_q(2)=364,
2^364==1 (mod q^2),
q divides X exactly once.
```

Any direct predecessor of `1` is divisible by `q`, while every accelerated
output is coprime to `q`. Since the first step is `2^153-1`,

```text
C_X^t(1)!=1 for every t>=1.
```

### Finite cycle barrier

Every positive cycle length through

```text
6766211283939365362054096447760569535444132142
```

is impossible. Cycles above this finite barrier remain possible.

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

The exact six-step map is

```text
G(n)=C_X^6(n)
 =[X^6*n+X^5+8*X^4+16*X^3+64*X^2+256*X+8192]/2^19.
```

For `n==1 (mod 2^20)` it has the displayed exact word. If
`20<=L=v2(n-1)<156`, then

```text
v2(G(n)-1)=L-19.
```

### Adjacent-label sieve

For values with two preceding transitions, two adjacent least valuation labels
determine the full residue modulo `1093^2`. Exactly

```text
132496
```

classes survive out of `397852` one-step output classes.

### Missing theorem

The initial repeated program ends after eight blocks. The leading target is a
renewal or height-credit theorem that controls all later contractions. The
permanent `1093^2` class sieve should be combined with distinct-value harmonic
bounds for hypothetical cycles.

Main files:

```text
docs/STRUCTURED_WIEFERICH_X156_CANDIDATE.md
tools/verify_structured_wieferich_x156_candidate.py
docs/WIEFERICH_ADJACENT_LABEL_COORDINATES.md
tools/verify_wieferich_adjacent_label_coordinates.py
```

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

This candidate has the stronger finite barrier but a less compact renewal
program.

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

Multiple-of-`m` exceptional blocks are strictly contracting. Therefore the
least seed entering a hypothetical cycle must satisfy

```text
1<=v2(d*w-1)<m
```

and its first step grows.

Files:

```text
docs/NEAR_POWER_COMPLETE_BLOCKS_AND_MINIMAL_BASIN.md
tools/verify_near_power_complete_blocks.py
```

## Mersenne branch `X=15,n0=3`

The second complete block of a least hypothetical basin seed cannot be
exceptional. A contracting second block must increase the terminal type.
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

Large valuations require an exact alternating base-8 suffix. No amortized proof
for all times is known.

## Previous fixed-candidate frontier

For

```text
X=104350542602662257699,
n0=1,
```

all lengths through `355561454311274250377` are excluded except two. At the
first surviving length,

```text
Q<=6241,
```

so `6242` layer totals still remain. This branch is retained as an independent
finite-cycle attack.

## Not established

- No explicit positive orbit has been proved divergent.
- No candidate has every nontrivial positive cycle excluded.
- A finite cycle barrier, however large, is not divergence.
- The exact initial macroblocks do not repeat indefinitely by a proved ordinary
  integer renewal.
- The adjacent-label sieve does not by itself make the surviving class set
  finite.

## Exact next step

1. Build a renewal or height-credit inequality for `X=2^156-9`.
2. Combine distinct cycle values with the `132496` residue classes in a rigorous
   logarithmic or harmonic interval bound.
3. Keep the `2^260-3`, `X=15`, `X=9`, and old `Q=6241` branches independent.
4. Report proof gates and exact frontiers instead of unsupported percentages.

## Reproduction

```text
python run_checks.py
```
