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
docs/SESSION_CHECKPOINT_2026-07-11_MEASURED_HYBRID_FRONTIER.md
run_checks.py
```

GitHub files are the durable source of truth.

## Measurement rule

Do not report one precise completion percentage. Report instead:

1. strict proof gates;
2. exact finite frontiers;
3. reusable infinite-family structure.

For the current structured candidate, the explicit-pair gate, no-return gate,
and general positive-orbit dichotomy are available. The decisive global gate,
exclusion of every nontrivial positive cycle, remains open.

## Branch A: structured hybrid candidate

Current primary working candidate:

```text
X=2^156-9
 =91343852333181432387730302044767688728495783927,
n0=1.
```

### Closed facts

Let `q=1093`. Then

```text
ord_q(2)=364,
2^364==1 (mod q^2),
q divides X exactly once.
```

The first step leaves `1`, and the Wieferich predecessor argument proves

```text
C_X^t(1)!=1 for every t>=1.
```

Every positive cycle length through

```text
6766211283939365362054096447760569535444132142
```

is impossible.

The first `48` accelerated steps have the exact valuation word

```text
(3,1,2,2,5,6)^8,
```

with

```text
A_48=152,
v2(n_48-1)=4,
n_48>X^48/2^152.
```

The six-step map is exact:

```text
G(n)=C_X^6(n)
 =[X^6*n+X^5+8*X^4+16*X^3+64*X^2+256*X+8192]/2^19.
```

For `n==1 (mod 2^20)`, its exact valuation word is
`(3,1,2,2,5,6)`. If `20<=L=v2(n-1)<156`, then

```text
v2(G(n)-1)=L-19.
```

Files:

```text
docs/STRUCTURED_WIEFERICH_X156_CANDIDATE.md
tools/verify_structured_wieferich_x156_candidate.py
```

### Permanent q-adic sieve

For every value with two preceding transitions,

```text
n_(i+1)
 ==2^(-s_i)*(1+1093*c*2^(-s_(i-1))) (mod 1093^2).
```

Thus two adjacent least labels determine the full residue modulo `1093^2`.
Exactly

```text
364^2=132496
```

classes survive, versus `364*1093=397852` one-step output classes.

Files:

```text
docs/WIEFERICH_ADJACENT_LABEL_COORDINATES.md
tools/verify_wieferich_adjacent_label_coordinates.py
```

### Missing theorem

The exact initial program ends after eight blocks. Prove either:

1. a renewal theorem recreating `n==1 (mod 2^20)` often enough; or
2. a height-credit inequality showing that all later contractions are paid for
   by earlier proved growth; or
3. a global harmonic contradiction using distinct cycle values and the
   `132496` surviving classes.

No current result excludes every cycle above the finite barrier.

## Branch B: larger-barrier hybrid candidate

```text
X=2^260-3,
n0=1.
```

Closed facts:

- return to `1` is impossible;
- every positive cycle length through

```text
411705206177124250394919057808668116811626612144499783251404743139246683164216
```

  is impossible;
- the first `172` accelerated steps have exact word `(1,2)^86`;
- `A_172=258`, `v2(n_172-1)=2`, and `n_172>X^172/2^258`;
- a least seed entering a hypothetical cycle satisfies
  `1<=v2(3*w-1)<=259` and begins with a growing step.

Files:

```text
docs/HYBRID_WIEFERICH_NEAR_POWER_CANDIDATE.md
tools/verify_hybrid_wieferich_near_power_candidate.py
docs/HYBRID_INITIAL_ALTERNATING_MACROBLOCK.md
tools/verify_hybrid_initial_alternating_macroblock.py
```

This candidate has the stronger finite barrier. Branch A has the cleaner
repeated macroblock and is preferred for renewal work.

## General near-power theorem

For

```text
B=2^m,
X=B-d,
d odd,
d*n-1=2^(m*k+s)*u,
1<=s<=m-1,
```

the exact complete endpoint is

```text
C_X^(k+1)(n)=(X^(k+1)*u+2^(m-s))/d.
```

Multiple-of-`m` exceptional blocks are strictly contracting. Hence a least
positive seed entering a hypothetical nontrivial cycle must satisfy

```text
1<=v2(d*w-1)<m
```

and its first step is strictly growing.

Files:

```text
docs/NEAR_POWER_COMPLETE_BLOCKS_AND_MINIMAL_BASIN.md
tools/verify_near_power_complete_blocks.py
```

## Branch C: Mersenne descent

Candidate:

```text
X=15,
n0=3.
```

Retained structure:

- complete Mersenne valuation blocks are classified;
- every exceptional block has a strictly smaller ordinary seed with the
  identical future tail;
- a least seed entering a hypothetical cycle has `v2(w-1) in {1,2,3}`;
- the second block cannot be exceptional;
- if the second block contracts, its terminal type strictly increases.

Exact remaining contracting second-block families:

```text
initial type 3: none;
initial type 2: terminal type 3, 10<=k<=20;
initial type 1: terminal type 2, 21<=k<=31,
                or terminal type 3, 10<=k<=31.
```

Files:

```text
docs/MERSENNE_COMPLETE_VALUATION_BLOCKS.md
tools/verify_mersenne_complete_valuation_blocks.py
docs/MERSENNE_MINIMAL_BASIN_LEMMA.md
docs/MERSENNE_SECOND_BLOCK_ESCALATION.md
tools/verify_mersenne_second_block_escalation.py
```

The later-block height theorem and avoidance of `1` remain open.

## Branch D: `X=9,n0=1`

Define

```text
A_t=sum_(j<t)v2(9*n_j+1),
S_t=2^A_t*n_t.
```

Then

```text
S_(t+1)=9*S_t+2^v2(S_t),
v2(S_t)=A_t.
```

A proof of

```text
A_t<=3*t-1
```

for every `t>=1` would imply divergence. Large valuations require the exact
alternating base-8 suffix `7,0,7,0,...`. The missing step is an amortized suffix
bound.

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

For the first remaining length,

```text
Q<=6241,
```

so `6242` integer layer totals still remain. This branch is retained, but a
larger finite barrier is not counted as a fraction of the infinite proof.

## Literature audits

Do not use:

- the Santos Mersenne-cycle proof; its divisibility lemma has an explicit
  counterexample;
- the Tremblay `5x+1` divergent-proportion claim; endpoint growth was confused
  with finite stopping-time survival.

Files:

```text
docs/LITERATURE_AUDIT_SANTOS.md
docs/LITERATURE_AUDIT_TREMBLAY_5X1.md
```

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
- treat finite trajectory height as divergence;
- return to forbidden finite-word searches on the old `2154` classes;
- use a fixed finite-state positive-minimum-mean zero-layer potential;
- treat arbitrary finite growing programs as an ordinary infinite orbit;
- enlarge raw cutoffs without a theorem they are intended to test.

## Exact next work

1. Work first on renewal or height credit for `X=2^156-9`.
2. Combine the adjacent-label `1093^2` sieve with a distinct-value harmonic
   cycle bound.
3. Retain the `2^260-3`, `X=15`, `X=9`, and `Q=6241` branches as independent
   fallbacks.
4. Commit every theorem and decisive refutation separately.
5. Continue to report proof gates and exact frontiers, not unsupported
   percentages.

## Reproduction

```text
python run_checks.py
```
