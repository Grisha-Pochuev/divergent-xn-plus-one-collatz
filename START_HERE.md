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
growth, a positive-drift heuristic, or a huge finite trajectory is not a
solution.

## Read first

```text
START_HERE.md
docs/CURRENT_STATUS.md
docs/VALIDATED_RESULTS.md
docs/RETRACTIONS.md
docs/NEXT_STEPS.md
docs/SESSION_CHECKPOINT_2026-07-11_BLOCK_DESCENT_2.md
run_checks.py
```

GitHub files are the durable source of truth.

## Current branch ranking

The strict problem remains open.  Work is no longer restricted to the old
Priority 1 branch.

### Branch A: Mersenne descent, currently the cleanest direct alternative

Main working candidate:

```text
X=15,
n0=3.
```

No divergence or avoidance-of-`1` theorem is proved for this pair.

For every Mersenne multiplier

```text
X=2^m-1,
n-1=2^r*u,
u odd,
```

the dynamics has an exact complete block decomposition.

If

```text
r=m*k+s,
1<=s<=m-1,
```

then the next `k+1` valuations are

```text
m,...,m,s
```

and

```text
C_X^(k+1)(n)=X^(k+1)*u+2^(m-s).
```

If instead

```text
r=m*k,
k>=1,
```

put

```text
w=X^(k-1)*u.
```

Then

```text
C_X^k(n)=C_X(w),
w<n.
```

Thus every exceptional Mersenne block has literally the same future tail as a
strictly smaller ordinary integer.

For `X=15`, the first possible contracting nonexceptional blocks occur only at

```text
r=43,86,129
```

for residue tails `s=3,2,1`, respectively.  Therefore every smaller
nonexceptional block is strictly increasing, and the smallest possible input of
an ordinary contracting block is at least

```text
2^43+1=8796093022209.
```

If a nontrivial Mersenne cycle exists and `w` is the least positive odd seed
whose orbit enters it, then

```text
1<=v2(w-1)<m
```

and its first step is strictly increasing.  For `X=15`, only the three entrance
types `v2(w-1)=1,2,3` remain at the well-founded bottom of a hypothetical
basin.

Files:

```text
docs/MERSENNE_COMPLETE_VALUATION_BLOCKS.md
tools/verify_mersenne_complete_valuation_blocks.py
docs/MERSENNE_MINIMAL_BASIN_LEMMA.md
```

### Branch B: digital invariant for `X=9,n0=1`

Define

```text
A_t=sum_(j<t)v2(9*n_j+1),
S_t=2^A_t*n_t.
```

Then exactly

```text
S_0=1,
S_(t+1)=9*S_t+2^v2(S_t),
v2(S_t)=A_t.
```

A proof of

```text
A_t<=3*t-1
```

for every `t>=1` would imply

```text
n_t>=2*(9/8)^t->+infinity.
```

Large valuations are now described exactly: a valuation at least `3k` requires
the alternating low base-8 suffix

```text
7,0,7,0,...
```

of length `k`, read from the least significant digit.  The missing lemma is an
amortized proof that the orbit cannot create these suffixes fast enough for the
cumulative valuation to reach `3t`.

Files:

```text
docs/X9_DIGITAL_INVARIANT_LEAD.md
docs/FERMAT_SIGNED_DIGIT_DESCENT.md
tools/check_x9_digital_invariant.py
tools/verify_fermat_signed_digit_descent.py
```

### Branch C: near-power descent for `X=13`

For

```text
3*n-1=2^(4*k+s)*u,
u odd,
s in {1,2,3},
```

the exact endpoint is

```text
C_13^(k+1)(n)=(13^(k+1)*u+2^(4-s))/3.
```

The first possible nonexceptional contractions occur at

```text
s=1: r=41,
s=2: r=26,
s=3: r=15.
```

Multiple-of-four tails reduce to the same `13n+1` rule on a strictly smaller
auxiliary integer, but with a remaining division by `3`.  This makes the branch
slightly less clean than the Mersenne branch.

Files:

```text
docs/NEAR_POWER_EXCEPTIONAL_DESCENT.md
tools/verify_near_power_exceptional_descent.py
docs/X13_COMPLETE_VALUATION_BLOCKS.md
tools/verify_x13_complete_valuation_blocks.py
```

### Branch D: strongest finite cycle barrier

Fixed candidate:

```text
X=104350542602662257699,
n0=1.
```

Retained conclusions:

- the orbit leaves `1` and cannot return to `1`;
- every reached nontrivial cycle element is at least `25`;
- every cycle length

```text
p<=177780727155637125192
```

is impossible;
- every length through

```text
355561454311274250377
```

is impossible except

```text
177780727155637125193,
177780727155637125195.
```

Use

```text
O=ord_X(2)=1860810887857924950,
a_i=s_(i+1)+O*q_i,
Q=sum_i q_i.
```

For the first remaining length, harmonic packing in the `4308` surviving
classes modulo `90594` proves

```text
Q<=6241.
```

The boundary is narrow:

```text
packing upper at Q=6241 >0.377086594,
packing upper at Q=6242 <0.375630659,
required finite zero-layer mass >0.375632520964.
```

This remains the strongest finite cycle-exclusion branch, but it needs a global
distribution theorem and is not a divergence proof.

Files:

```text
docs/HIGH_Q_MOD3_HARMONIC_EXCLUSION.md
tools/verify_high_q_mod3_harmonic_exclusion.py
```

## Literature audits

Do not use the published Mersenne-cycle theorem in Santos (2020).  Its proof
contains a false divisibility lemma, with the recorded counterexample

```text
m=3,
q=7,
k=9,
c=2,
7 | 9*2^2-1=35,
```

although `9` is not a power of two.

Do not use the claimed `17%` divergent proportion for `5x+1` in Tremblay
(2021).  Endpoint growth does not imply that all intermediate values stayed
above the start.  The smallest counterexample is

```text
2 -> 1 -> 3 -> 8.
```

It has two odd steps among three, so `5^2>2^3` and the endpoint grows, but its
stopping time is already `1`.

Files:

```text
docs/LITERATURE_AUDIT_SANTOS.md
docs/LITERATURE_AUDIT_TREMBLAY_5X1.md
tools/verify_tremblay_5x1_audit.py
```

## Closed or invalid routes

Do not repeat:

- the false condition `2^A==1 (mod X)`;
- identifying the least-cost predecessor source with the actual cycle source;
- finite trajectory height as evidence of divergence;
- forbidden finite-word searches on the `2154` small classes;
- a fixed finite-state positive-minimum-mean zero-layer potential;
- arbitrary finite growing macroblock programs without an ordinary infinite
  realization;
- blind enlargement of trajectory or representative cutoffs.

Arbitrarily long realizable zero-cost finite words show that the obstruction
must be global or value-dependent.

## Exact next work

### First target: close the Mersenne basin descent

For `X=15`, let `w` be the least seed entering a hypothetical nontrivial cycle.
Only

```text
w=2*u+1,
w=4*u+1,
w=8*u+1
```

remain.  Use their exact first images and the identical-tail replacement to
prove one of the following:

1. a strictly smaller positive seed enters the same cycle; or
2. the orbit is forced into a nonexceptional tail of depth at least `43`.

Closing all three entrance types would substantially advance, and may close,
the Mersenne cycle branch.

### Second target: exclude return to `1`

If nontrivial Mersenne cycles are excluded, prove that one explicit seed,
preferably `(X,n0)=(15,3)`, never reaches the trivial fixed point.  Analyze the
backward tree of `1`, whose first layer consists of base-16 repunits, together
with the complete block descent.  Do not substitute a long forward scan.

### Parallel targets

- build an amortized signed-suffix potential for `X=9,n0=1`;
- improve the exact `Q=6241` packing boundary for the huge fixed candidate;
- seek an unbounded height-dependent potential, not a fixed finite-state one.

## Critical retractions

Never use

```text
2^A==1 (mod X).
```

The correct cycle relation is

```text
2^A*product_i(n_i)==1 (mod X).
```

Also never identify the least admissible predecessor source label with the
source selected by the actual cycle.

## Working rules

- Separate theorems from evidence.
- Test every theorem against known cycles or an explicit regression example.
- Add an exact checker where practical.
- Short symbolic and modular computations are allowed; large searches require
  explicit approval.
- Commit every rigorous result or decisive refutation separately.
- A finite or sparse barrier is not divergence.

## Reproduction

```text
python run_checks.py
```
