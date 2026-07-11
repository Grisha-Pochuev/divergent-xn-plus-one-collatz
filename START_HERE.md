# START HERE

This file is the durable entry point for every new work session.

## Strict target

Find explicit positive odd integers `X>=5` and `n0>=1` such that

```text
C_X(n)=(X*n+1)/2^v2(X*n+1)
```

satisfies

```text
C_X^t(n0)->+infinity.
```

A cycle, avoidance of `1`, a finite cycle barrier, arbitrarily long finite
growth, a heuristic drift, or a huge finite trajectory is not a solution.

## Read first

```text
START_HERE.md
docs/PROGRESS_METRICS.md
docs/CURRENT_STATUS.md
docs/VALIDATED_RESULTS.md
docs/RETRACTIONS.md
docs/SESSION_CHECKPOINT_2026-07-11_BLOCK_LEDGER_AND_EXCEPTIONAL_SIEVE.md
docs/SESSION_CHECKPOINT_2026-07-11_SHARP_BLOCK_SIGN.md
run_checks.py
```

GitHub files are the durable source of truth.

## Measurement rule

Do not turn closed preparatory gates into one precise proof percentage.  Report:

1. strict proof gates;
2. exact finite frontiers;
3. reusable infinite-family structure.

For the primary candidate, the explicit-pair gate, no-return gate, and general
positive-orbit dichotomy are available.  The decisive global gate, exclusion of
every nontrivial positive cycle, remains open.

## Branch A: primary structured candidate

```text
X=2^156-9
 =91343852333181432387730302044767688728495783927,
n0=1.
```

### Closed: no return to `1`

For `q=1093`,

```text
ord_q(2)=364,
2^364==1 (mod q^2),
q divides X exactly once.
```

The first step leaves `1`, and the Wieferich predecessor argument proves

```text
C_X^t(1)!=1 for every t>=1.
```

### Closed: exact initial program

The first `48` accelerated steps have valuation word

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

For `n==1 (mod 2^20)`, its word is `(3,1,2,2,5,6)`.  If
`20<=L=v2(n-1)<156`, then

```text
v2(G(n)-1)=L-19.
```

### Closed: sharp signs of all ordinary complete blocks

For

```text
9*n-1=2^(156*k+s)*u,
1<=s<=155,
ell=k+1,
e=156-s,
```

define

```text
L_e=floor(e/log2(2^156/X))+1.
```

Exact rational logarithm bounds and modular certificates prove, for all `155`
terminal deficits,

```text
ell<L_e   => the complete block strictly grows,
ell>=L_e  => the complete block strictly contracts.
```

The additive term never reverses this sign.  In particular,

```text
L_1
 =7034970411803187993997906985047212163795395135.
```

Therefore every positive cycle length through

```text
7034970411803187993997906985047212163795395134
```

is impossible.  This is a finite barrier, not divergence.

Files:

```text
docs/NEAR_POWER_SHARP_BLOCK_SIGN.md
tools/verify_near_power_block_sign_threshold.py
```

### Closed: canonical cycle block ledger

Every hypothetical cycle has a canonical partition into complete near-power
blocks.  Give an ordinary block terminal credit `e=156-s>0` and an exceptional
block ending at valuation `156+b` credit `-b`.

If the cycle has length `p`, total valuation `A`, and

```text
D=156*p-A,
```

then exactly

```text
D=sum ordinary deficits-sum exceptional excesses.
```

Every exceptional block contracts by more than `b` binary height units.  A
unified exact block-ratio formula gives

```text
sum kappa_j=p*delta-D,
delta=log2(2^156/X),
```

and the uniform correction bound implies

```text
p*(delta-9/(2*X*ln(2)))<D<p*delta.
```

Thus the integer `D` must lie in roughly the upper half of the formerly allowed
interval.

Files:

```text
docs/NEAR_POWER_CYCLE_BLOCK_LEDGER.md
tools/verify_near_power_cycle_block_ledger.py
```

### Closed: permanent `1093^2` adjacent-label sieve

Every value with two preceding transitions satisfies

```text
n_(i+1)
 ==2^(-s_i)*(1+1093*c*2^(-s_(i-1))) (mod 1093^2).
```

Two adjacent least labels determine the full residue modulo `1093^2`.  Exactly

```text
364^2=132496
```

classes survive, versus `397852` one-step output classes.

Files:

```text
docs/WIEFERICH_ADJACENT_LABEL_COORDINATES.md
tools/verify_wieferich_adjacent_label_coordinates.py
```

### Closed: exceptional sources plus the `1093^2` sieve

An exceptional source satisfies exactly

```text
v2(9*n-1)=156
```

and hence

```text
n=(17*2^156+1)/9+2^157*t.
```

Combining this progression with all `132496` permanent adjacent-label classes
by the Chinese remainder theorem gives

```text
n>=(125*2^156+1)/9
 =1268664615738631005385143083955106787895774776889
```

for every exceptional source in a hypothetical cycle.  The minimum is attained
by label pair `(61,64)` and progression layer `t=6`.  It is about `7.35` times
the raw exceptional-source floor.

Files:

```text
docs/X156_EXCEPTIONAL_Q2_SIEVE.md
tools/verify_x156_exceptional_q2_sieve.py
```

### Missing theorem

The exact initial program ends after eight macroblocks.  All ordinary complete
blocks now have exact signs, exceptional blocks have an exact credit cost and a
large source-height floor, but no global contradiction has yet excluded every
cycle.

The next target is to prove that the required correction sum

```text
sum kappa_j=p*delta-D
```

cannot be achieved by distinct cycle values constrained to the `132496`
permanent residue classes.

Promising ingredients:

1. the roughly half-width integer strip for `D`;
2. more than `b` bits lost by each exceptional block;
3. the exceptional-source floor above `1.268*10^48`;
4. distinct-value harmonic packing;
5. an unbounded height-dependent potential, not a fixed finite-state one.

## Branch B: larger-barrier hybrid candidate

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

  is impossible;
- the first `172` steps have exact word `(1,2)^86`;
- `A_172=258`, `v2(n_172-1)=2`, and `n_172>X^172/2^258`;
- a least seed entering a hypothetical cycle starts in a low near-power layer
  and first grows.

This candidate has the stronger finite barrier.  Branch A remains primary
because it has the cleaner repeated macroblock and stronger block structure.

## General near-power theorem

For

```text
B=2^m,
X=B-d,
d*n-1=2^(m*k+s)*u,
1<=s<=m-1,
```

the exact complete endpoint is

```text
C_X^(k+1)(n)=(X^(k+1)*u+2^(m-s))/d.
```

Multiple-of-`m` exceptional blocks strictly contract.  A least positive seed
entering a hypothetical nontrivial cycle must satisfy

```text
1<=v2(d*w-1)<m
```

and its first step grows.

## Branch C: Mersenne descent

```text
X=15,
n0=3.
```

Retained structure:

- complete blocks are classified;
- exceptional blocks have a strictly smaller ordinary seed with identical
  future tail;
- a least basin seed has `v2(w-1) in {1,2,3}`;
- the second block cannot be exceptional;
- a contracting second block strictly increases terminal type.

Remaining contracting second-block families:

```text
initial type 3: none;
initial type 2: terminal type 3, 10<=k<=20;
initial type 1: terminal type 2, 21<=k<=31,
                or terminal type 3, 10<=k<=31.
```

Later contractions and avoidance of `1` remain open.

## Branch D: `X=9,n0=1`

A proof of

```text
A_t<=3*t-1
```

for every `t>=1` would imply divergence.  Large valuations require an exact
alternating base-8 suffix.  The missing step is an amortized suffix bound.

## Branch E: old fixed-candidate frontier

```text
X=104350542602662257699,
n0=1.
```

All cycle lengths through `355561454311274250377` are excluded except

```text
177780727155637125193,
177780727155637125195.
```

For the first remaining length, `Q<=6241`, so `6242` layer totals remain.  This
branch is retained independently.

## Critical retractions and closed routes

Never use

```text
2^A==1 (mod X).
```

The correct cycle congruence is

```text
2^A*product_i(n_i)==1 (mod X).
```

Also never:

- identify the least admissible predecessor source with the actual cycle source;
- treat finite trajectory height or a finite barrier as divergence;
- return to finite-word searches on the old `2154` classes;
- use a fixed finite-state positive-minimum-mean zero-layer potential;
- treat arbitrary finite growing programs as an ordinary infinite orbit;
- enlarge raw cutoffs without a theorem they test.

## Exact next work

1. Convert the block correction identity into a rigorous harmonic packing
   inequality over the `132496` permanent classes.
2. Separate ordinary and exceptional block sources and exploit the exceptional
   floor `(125*2^156+1)/9`.
3. Use the integer strip for `D` to restrict admissible cycle lengths and total
   block credits.
4. Seek an unbounded height-credit potential; fixed finite-state potentials are
   ruled out.
5. Keep the `2^260-3`, `X=15`, `X=9`, and old `Q=6241` branches independent.
6. Commit every theorem and decisive refutation separately.

## Reproduction

```text
python run_checks.py
```
