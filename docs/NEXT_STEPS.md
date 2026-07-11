# Prioritized next steps

The strict prize problem remains open.

## Priority 1: eliminate the final two lengths

Current candidate:

```text
X  = 104350542602662257699,
n0 = 1.
```

Current contiguous barrier:

```text
p <= 177780727155637125192.
```

Current sparse cap:

```text
p <= 355561454311274250377.
```

Only two lengths remain:

```text
177780727155637125193
177780727155637125195.
```

Their exact reciprocal thresholds are approximately

```text
0.506785307
0.099934207.
```

## Current exact picture

Use

```text
O=ord_X(2)=1860810887857924950,
a_i=s_(i+1)+O*q_i,
sum q_i<=6257.
```

The exact edge cost

```text
c_i=(s_i-1)+(s_(i+1)-1)+2*O*q_i
```

satisfies

```text
sum c_i=2*(A-p).
```

More than `97.38%` of every remaining hypothetical cycle is forced into zero-layer transitions with adjacent-label sum at most `5001`, and every target in this majority is at least

```text
781563824454394220933608138645145.
```

Hence the reciprocal correction is concentrated in a comparatively small expensive part.

Mandatory populations:

```text
p=...193:
  at least 355687 expensive targets in (10^6,X),
  at least 349430 of them zero-layer;

p=...195:
  at least 5 expensive targets below X,
  at least 799470 targets above 60000000,
  at least 793213 of those zero-layer.
```

The strongest retained small-value bound for `...195` is

```text
sum_(n_i<=1000000)1/n_i <0.085226905,
```

proved by the signed-label potential plus depth-three inverse charging.

The strongest retained bound through sixty million remains

```text
sum_(n_i<=60000000)1/n_i <0.086609720.
```

Do not use the retracted figures `0.086412209`, `811320`, or `805063`.

## Immediate target A: extend the signed-label potential

The valid potential assigns extremal signed values to two disjoint full-label sets and telescopes around the actual cycle.  It avoids the invalid step of identifying a least-cost predecessor with the actual source.

Next tasks:

1. extend the target set beyond one million;
2. for every included target, prove that its least admissible layer minimizes the potential-shifted cost among all admissible layers;
3. maintain nonnegative modified edge costs globally;
4. combine the resulting constraint with depth-three inverse charging in a rational dual;
5. seek an improvement of the retained sixty-million bound `0.086609720`.

A successful extension must treat label-set collisions explicitly.  If target and source sets cease to be disjoint, solve the resulting finite potential feasibility problem rather than silently assigning conflicting values.

## Immediate target B: finite-state zero-layer potential

At least hundreds of thousands of mandatory tail targets are zero-layer targets.  Build a finite quotient retaining enough carry information for the exact predecessor map.

Seek a rational inequality

```text
cost(edge) >= delta + Phi(next)-Phi(current)
```

with `delta>0` on every projected zero-layer cycle.  Summing around a real cycle would then conflict with the global layer or reciprocal budget.

The quotient is valid only if every real zero-layer transition projects correctly.  Small-class labels alone are insufficient because the local transition graph is complete.

## Immediate target C: use the all-zero-layer minimum valley

The four-generation inverse sieve proves

```text
p=...193: a_out<=36 and n_next>1518500249*m,
p=...195: a_out<=39 and n_next>189812531*m.
```

Needed:

1. derive a forced compensating contraction after this initial jump;
2. charge that contraction against a positive layer or an expensive full label;
3. combine with `sum q_i<=6257` or the reciprocal identity;
4. avoid merely proving a larger maximum, which is not contradictory by itself.

## Immediate target D: short affine return

One segment satisfies

```text
1<=L<=114286,
L<=S<=7771435,
n_L==n_0 (mod 2*X^2).
```

Insert the exact affine iterate formula

```text
2^S*n_L=X^L*n_0+B.
```

Endpoint labels alone reproduce a tautology.  A useful result must retain additional information such as a third neighbouring label, a quotient bound, or a signed potential along the segment.

## Closed or unproductive routes

Do not repeat:

- forbidden finite-word searches on the `2154` small classes;
- bounded layer-word enumeration as if it were a global obstruction;
- blind enlargement of trajectory or representative cutoffs;
- the retracted assumption `ord_X(2)|A`;
- identification of a least-cost predecessor source label with the actual cycle source;
- comparison of a maximum-height lower bound with a theorem that only bounds the minimum.

## Restrictions

No long trajectory scans, large parameter searches, or large Actions matrices without explicit approval. Exact modular checks, smooth-order discrete logarithms, and compact deterministic certificates are allowed.

## Final-proof checklist

A valid prize solution must provide an explicit pair, exclude every positive cycle, exclude repetition, invoke the positive-orbit dichotomy, and supply independently runnable exact certificates.

## Recommended next session

> Extend the signed-label potential beyond one million, treating all label collisions and all admissible layers rigorously. In parallel, search for a finite-state potential on the mandatory zero-layer tail. Do not return to local forbidden words or blind cutoff growth.
