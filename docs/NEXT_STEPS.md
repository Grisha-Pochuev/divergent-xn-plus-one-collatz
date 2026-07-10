# Prioritized next steps

The strict prize problem remains open.

## Priority 1: eliminate the final two lengths in the first sparse window

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

Only two lengths remain in that larger range:

```text
177780727155637125193
177780727155637125195.
```

Their exact reciprocal thresholds are approximately

```text
0.506785307
0.099934207.
```

## Newly retained transition structure

Let

```text
O=ord_X(2)=1860810887857924950.
```

For every cycle value, write its incoming valuation as

```text
a=s+O*q,
1<=s<=O.
```

Then

```text
A=sum s+O*sum q.
```

For either remaining length,

```text
sum q<=6257.
```

Thus almost every cycle edge must lie in the least full-order layer.

For a full representative `n`, its possible predecessors form the exact progression

```text
m_q == m_0+q*63726582940809041391 (mod X).
```

The predecessor must itself lie in the full output subgroup. The minimum admissible `q` is the full predecessor delay `d_X(n)`, and

```text
sum d_X(n_i)<=6257.
```

Finite inverse windows give stronger necessary costs `h_L(n)` with

```text
sum h_L(n_i)<=L*6257.
```

At the harder length, the exact full-predecessor dual proves

```text
sum_(n_i<=60000000) 1/n_i < 0.087618737,
```

so more than `0.012315` must come from at least `738929` distinct values above sixty million.

## Closed or unproductive routes

Do not repeat:

- forbidden-edge or forbidden-finite-word searches on the `2154` small classes;
- bounded exact-valuation-layer word searches;
- blind enlargement of the small representative cutoff;
- the retracted assumption `ord_X(2)|A`;
- treating a finite cycle barrier as divergence.

The local transition graph is complete, and every compatible finite word is realizable. The obstruction must be global.

## Immediate target A: zero-delay inverse-window potential

The depth-one, depth-two, and depth-three exact reciprocal bounds below one million are

```text
0.087551912
0.085634587
0.085243521.
```

The strict improvement with depth suggests constructing a potential on inverse carry states.

Concrete tasks:

1. Define a finite quotient retaining enough carry information for zero-layer predecessor transitions.
2. Compute or prove a positive minimum mean full-order layer cost for every directed cycle in that quotient.
3. Convert the potential into a rational inequality of the form

```text
h_L(n) >= L*delta + Phi(next)-Phi(current).
```

4. Sum around a hypothetical cycle. Any fixed `delta>0` would contradict `sum q<=6257` for lengths near `1.78*10^20`.

A quotient is useful only if every real zero-layer transition projects correctly. A false deterministic reduction must not be inferred from the small class alone.

## Immediate target B: distribution of initial full classes

The cheap full labels correspond to the initial segment

```text
2^(-s) mod X,
1<=s<=about 1.53*10^11.
```

A sufficiently strong rigorous discrepancy estimate for this multiplicative orbit would bound the zero-delay representatives without enumerating them.

Concrete tasks:

1. Express the reciprocal selection dual as a weighted counting problem for an initial geometric progression modulo `P` and `X`.
2. Determine whether an explicit incomplete exponential-sum or character-sum theorem is numerically strong at the actual parameters.
3. Record the route only if all constants are explicit and the resulting inequality beats `0.099934207`.

General asymptotic equidistribution without usable constants is not a certificate.

## Immediate target C: full source/target circulation

Combine:

```text
sum_i (2^a_(i-1)-X)*n_i = p,
```

and

```text
sum_i (2^a_i-X)/n_i
 = sum_i 1/(n_i*n_(i+1)) > 0
```

with the full predecessor progression and the mod-3 balance

```text
N_(1->2)=N_(2->1).
```

Seek a signed rational potential that charges the necessary large zero-delay tail against neighbouring high-valuation steps.

## Secondary target: the other remaining length

The length

```text
177780727155637125193
```

has a larger required threshold, about `0.506785307`. The same full-predecessor machinery applies, but the present finite cutoff bounds are not yet close enough. Work first on a global zero-delay theorem that can address both lengths.

## Other routes

### Cycle-height route

Make the polynomial upper bound on the minimum cycle element explicit and combine it with a modular lower bound growing with a long zero-layer run.

### Regenerative-chain route

For `X=2^m+1`, construct one ordinary positive start supporting infinitely many net-positive complete bursts.

### Stabilized valuation-code route

Find one actual positive orbit with eventual average valuation below `log2(X)`.

### `X=9` digital invariant

A proof of `v2(S_t)<=3t-1` for the transformed `9n+1` recurrence would imply divergence. This route is outside the present Priority 1 session.

## Restrictions

No long trajectory scans, large parameter searches, or large Actions matrices without explicit approval. Exact modular checks, smooth-order discrete logarithms, and compact deterministic certificates are allowed.

## Final-proof checklist

A valid prize solution must provide an explicit pair, exclude every positive cycle, exclude repetition, invoke the positive-orbit dichotomy, and supply independently runnable exact certificates.

## Recommended next session

> Work only on the large zero-delay tail for the two remaining lengths. Try a rigorous inverse-window potential or a numerically explicit distribution theorem for the initial full-class orbit. Do not return to local words or blind cutoff growth.
