# START HERE

This file is the durable entry point for every new work session.

## Strict target

Find explicit positive odd integers `X>=5` and `n0>=1` such that

```text
C_X(n)=(X*n+1)/2^v2(X*n+1)
```

satisfies `C_X^t(n0)->+infinity`. A cycle, avoidance of `1`, a finite barrier,
or a huge finite trajectory is not a solution.

## Read first

```text
START_HERE.md
docs/CURRENT_STATUS.md
docs/VALIDATED_RESULTS.md
docs/RETRACTIONS.md
docs/NEXT_STEPS.md
docs/SESSION_CHECKPOINT_2026-07-11_PRIORITY1_C.md
run_checks.py
```

GitHub files are the durable source of truth.

## Main fixed candidate

```text
X  = 104350542602662257699,
n0 = 1.
```

Retained conclusions:

- the orbit leaves `1` and cannot return to `1`;
- every element of a reached nontrivial cycle is at least `25`;
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
177780727155637125193
177780727155637125195.
```

The strict problem remains open.

## Exact full-layer coordinates

Use

```text
O=ord_X(2)=1860810887857924950,
a_i=s_(i+1)+O*q_i,
1<=s_i<=O,
q_i>=0,
Q=sum_i q_i.
```

For either remaining length,

```text
Q<=6257.
```

The exact symmetric edge cost

```text
c_i=(s_i-1)+(s_(i+1)-1)+2*O*q_i
```

satisfies

```text
sum_i c_i=2*(A-p).
```

Possible predecessors of a full representative form an exact progression
modulo `X`, and a reached predecessor must itself be a full output.

## Transition concentration

With threshold `K=5000`, more than `97.38%` of all edges satisfy

```text
q_i=0,
s_i+s_(i+1)<=5001.
```

Every target in that cheap majority is at least

```text
781563824454394220933608138645145,
```

so all cheap targets together contribute less than `2.216*10^(-13)` to the
reciprocal sum. The required correction is concentrated in expensive
zero-layer transitions.

## Strongest retained finite-range bound

A signed-label potential is valid for all `358103` retained targets through
sixty million. The potential telescopes on the actual cycle and does not assume
that the least-cost source is the source chosen by the cycle.

Keeping the integer layer total `Q` and coupling the small and middle ranges
through the same `Q` gives

```text
sum_(n_i<=60000000) 1/n_i <0.086152495.
```

The exact maximizing integer of this finite-range certificate is

```text
Q=5841.
```

Therefore:

```text
p=177780727155637125193:
  values above 60000000 >=25237969,
  zero-layer values there >=25231712;

p=177780727155637125195:
  values above 60000000 >=826903,
  zero-layer values there >=820646.
```

For the first length, at least

```text
22537952
```

distinct expensive zero-layer targets lie in the finite interval

```text
60000000<n<X.
```

## New high-Q exclusion for the first remaining length

The permanent predecessor sieve modulo `3` leaves exactly `4308` refined target
classes modulo

```text
6M=90594.
```

For fixed `Q`,

```text
sum_i(s_i-1)=B-O*Q.
```

Distinct targets below `X` have distinct full labels, so a set of `m` such
targets must satisfy

```text
m*(m-1)/2<=B-O*Q.
```

Combining this cardinality cap with harmonic packing in the `4308` surviving
classes proves

```text
Q=6242,6243,...,6257
```

impossible for

```text
p=177780727155637125193.
```

Hence every remaining cycle of this length satisfies

```text
Q<=6241.
```

At the exact threshold,

```text
packing upper at Q=6241 >0.377086594,
packing upper at Q=6242 <0.375630659,
required finite zero-layer mass >0.375632520964.
```

Certificate files:

```text
docs/HIGH_Q_MOD3_HARMONIC_EXCLUSION.md
tools/verify_high_q_mod3_harmonic_exclusion.py
```

## Other retained structure

One exact zero-layer pair occurs at least

```text
3053943280435589
```

times in one class modulo `2*X^2`. This forces an enormous cycle diameter and a
nonempty exact return segment with

```text
length<=114286,
total valuation<=7771435,
endpoints equal modulo 2*X^2.
```

Higher-power repeated words are retained through modulus `2*X^6`.

If every edge has `q=0`, the inverse minimum sieve gives

```text
p=...193: a_out<=36 and n_next>1518500249*m,
p=...195: a_out<=39 and n_next>189812531*m.
```

These results control height or local valleys but do not yet exclude later
compensating contractions.

## Closed finite-state route

For every `L`, exact valuation-word coding and CRT realize `L` consecutive
edges with

```text
q=0,
source label=target label=1,
edge cost=0.
```

Hence no fixed finite-state quotient can prove a universal positive mean
zero-layer cost by a telescoping potential. Do not return to a finite
positive-minimum-mean automaton.

## Exact next step

The remaining Priority 1 node is global distribution, not local word
exclusion.

1. Combine the `Q`-dependent finite-range dual with harmonic packing instead of
   using uniform worst-case constants.
2. Attack the first still-open integer `Q=6241`; the mod-3 packing relaxation
   misses contradiction only narrowly.
3. Improve the packing density with an explicit large-prime subgroup or
   Fermat-quotient estimate with usable constants.
4. Alternatively construct an unbounded value-dependent height potential.
5. Do not enlarge trajectory or representative cutoffs blindly.

## Critical retractions

Never use

```text
2^A==1 (mod X).
```

The correct cycle relation is

```text
2^A*product_i(n_i)==1 (mod X).
```

Also never identify the least-cost predecessor source label with the actual
cycle source. The old proof is invalid even though some numerical values were
later recovered by a different signed-potential proof.

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
