# Session checkpoint: measured hybrid frontier

Date: 2026-07-11

The strict prize problem remains open. This session replaced unsupported
single-number percentages by explicit proof gates and finite frontiers, then
used those measurements to move away from progress that enlarged only a finite
cycle barrier.

## 1. Objective measurement

The project now reports:

1. strict logical gates;
2. exact finite frontiers;
3. reusable infinite-family structure.

File:

```text
docs/PROGRESS_METRICS.md
```

For the current structured candidate, the explicit-pair gate, no-return gate,
and general bounded-orbit dichotomy are available. The decisive global gate,
exclusion of every nontrivial positive cycle, remains open. These gates are not
equally difficult and are not converted into a percentage.

## 2. Mersenne second-block escalation

For `X=15`, let `w` be the least positive odd seed entering a hypothetical
nontrivial cycle, and write

```text
w=2^s*u+1,
s in {1,2,3}.
```

The second complete block cannot be exceptional. If it contracts, its terminal
type must strictly increase. The exact remaining second-block families are

```text
s=3: none;
s=2: t=3, 10<=k<=20;
s=1: t=2, 21<=k<=31,
     or t=3, 10<=k<=31.
```

Files:

```text
docs/MERSENNE_SECOND_BLOCK_ESCALATION.md
tools/verify_mersenne_second_block_escalation.py
```

This is a genuine finite reduction, but later contractions still require a
global height-credit theorem.

## 3. Hybrid Wieferich near-power family

The new design principle is

```text
X=2^m-d,
1093 divides X exactly once.
```

The factor `1093` is Wieferich to base `2`, so any direct predecessor of `1`
would be divisible by `1093`, while every accelerated output is coprime to
`1093`. Thus a start that leaves `1` can never return.

### Larger-barrier candidate

```text
X=2^260-3,
n0=1.
```

Retained results:

- return to `1` is impossible;
- all positive cycles through

```text
411705206177124250394919057808668116811626612144499783251404743139246683164216
```

  steps are excluded;
- the first `172` accelerated steps have exact word `(1,2)^86`, total valuation
  `258`, and endpoint precision `v2(n_172-1)=2`.

Files:

```text
docs/HYBRID_WIEFERICH_NEAR_POWER_CANDIDATE.md
tools/verify_hybrid_wieferich_near_power_candidate.py
docs/HYBRID_INITIAL_ALTERNATING_MACROBLOCK.md
tools/verify_hybrid_initial_alternating_macroblock.py
```

### Structured candidate

```text
X=2^156-9
 =91343852333181432387730302044767688728495783927,
n0=1.
```

Retained results:

- return to `1` is impossible;
- all positive cycles through

```text
6766211283939365362054096447760569535444132142
```

  steps are excluded;
- the first `48` accelerated steps have the exact word

```text
(3,1,2,2,5,6)^8,
```

  total valuation `152`, endpoint precision `v2(n_48-1)=4`, and
  `n_48>X^48/2^152`.

File pair:

```text
docs/STRUCTURED_WIEFERICH_X156_CANDIDATE.md
tools/verify_structured_wieferich_x156_candidate.py
```

The `2^260-3` candidate has the larger finite barrier. The `2^156-9` candidate
has the cleaner repeated initial program and is preferred for renewal work.

## 4. Complete near-power block theorem

For

```text
X=2^m-d,
d*n-1=2^(m*k+s)*u,
1<=s<=m-1,
```

the complete endpoint is

```text
C_X^(k+1)(n)=(X^(k+1)*u+2^(m-s))/d.
```

Multiple-of-`m` exceptional blocks are strictly contracting. Therefore a least
seed entering a hypothetical cycle must lie in a low layer

```text
1<=v2(d*w-1)<m
```

and its first step grows.

Files:

```text
docs/NEAR_POWER_COMPLETE_BLOCKS_AND_MINIMAL_BASIN.md
tools/verify_near_power_complete_blocks.py
```

## 5. Wieferich adjacent-label sieve

For `q=1093`, `h=ord_q(2)=364`, and either hybrid candidate, every value with two
preceding orbit transitions satisfies

```text
n_(i+1)
 ==2^(-s_i)*(1+q*c*2^(-s_(i-1))) (mod q^2).
```

Thus the residue modulo `1093^2` is determined by two adjacent least labels.
Exactly

```text
364^2=132496
```

classes survive, compared with `364*1093=397852` one-step output classes. This
is a permanent threefold thinning, not a finite trajectory observation.

Files:

```text
docs/WIEFERICH_ADJACENT_LABEL_COORDINATES.md
tools/verify_wieferich_adjacent_label_coordinates.py
```

## 6. Exact next target

Work first on the structured candidate `X=2^156-9`.

1. Use the exact six-step map and the adjacent-label classes to seek a renewal
   theorem returning to `n==1 (mod 2^20)`.
2. If exact renewal fails, construct a height-credit potential: the first eight
   blocks create a large proved reserve, and every later exceptional near-power
   block is strictly contracting with a classified smaller coordinate.
3. Use distinctness and the `132496` classes in a rigorous harmonic bound for
   hypothetical cycles beyond the current finite barrier.
4. Retain `X=2^260-3`, `X=15`, and the old `Q=6241` branch in parallel, but do
   not count a larger finite barrier as a percentage of an infinite proof.

## 7. Verification status

All new checkers are listed in

```text
python run_checks.py
```

The algebraic identities were also tested independently on finite parameter
grids during the session. A full repository run was not executed in the chat
environment because that environment could not resolve the GitHub host for a
fresh checkout. This limitation does not change the committed symbolic proofs,
but it must be stated rather than silently claiming a full run.
