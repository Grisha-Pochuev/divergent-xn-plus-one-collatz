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

## New exact transition picture

Use

```text
O=ord_X(2)=1860810887857924950,
a_i=s_(i+1)+O*q_i.
```

For either remaining length,

```text
sum q_i<=6257.
```

The exact symmetric edge cost

```text
c_i=(s_i-1)+(s_(i+1)-1)+2*O*q_i
```

satisfies

```text
sum c_i=2*(A-p).
```

With threshold `K=5000`, more than `97.38%` of all edges are zero-layer edges with adjacent-label sum at most `5001`. Every target in that cheap majority exceeds

```text
781563824454394220933608138645145,
```

and their entire reciprocal contribution is below `2.216*10^(-13)`.

Thus the required correction is concentrated in the remaining expensive edges. At least one expensive target is at most

```text
9190982840926584716   for p=...193,
46609216582838682965  for p=...195.
```

Both are below `X`.

A second threshold forces one exact transition pair to occur at least

```text
3053943280435589
```

times in one class modulo `2*X^2`. It yields a short exact return:

```text
length <=114286,
total valuation <=7771435,
endpoints equal modulo 2*X^2.
```

Repeated words also exist modulo higher powers:

```text
2 edges: >=3114290401257 repetitions modulo 2*X^3
3 edges: >=2918613523 repetitions modulo 2*X^4
4 edges: >=2251677 repetitions modulo 2*X^5
5 edges: >=1500 repetitions modulo 2*X^6.
```

## Closed or unproductive routes

Do not repeat:

- forbidden finite-word searches on the `2154` small classes;
- bounded layer-word enumeration as if it were a global obstruction;
- blind enlargement of trajectory or representative cutoffs;
- the retracted assumption `ord_X(2)|A`;
- comparison of the new maximum-height lower bound with a theorem that only bounds the minimum cycle element.

The local transition graph is complete. The obstruction must be global.

## Immediate target A: expensive small transition

The best concrete node is now the forced target below `X`.

1. Parameterize all full predecessors of a target `n<X`:

```text
m_q=(2^(s+qO)*n-1)/X.
```

2. Combine the target bound with the permanent mod-3 sieve, exact full predecessor delay, and source label.
3. Seek a universal lower cost for every admissible predecessor of such a small target.
4. If that cost exceeds the available edge budget after reciprocal concentration, one of the two lengths is eliminated.

This route should attack `...193` first because its required reciprocal threshold is five times larger.

## Immediate target B: symmetric inverse-window dual

The depth-one symmetric edge dual gives

```text
sum_(n_i<=1000000)1/n_i <0.087543786.
```

The former one-sided depth-two and depth-three bounds remain numerically stronger:

```text
0.085634587
0.085243521.
```

Needed:

1. define the exact minimum sum of symmetric edge costs over a two- or three-edge inverse window;
2. use both the symmetric budget and the endpoint-label budget as separate rational constraints rather than replacing one by the other;
3. construct a two-multiplier fractional dual or a finite-state potential;
4. retain the result only if it improves the depth-three number or directly reduces the large tail.

A simple convex average of the old and new costs was checked and did not improve the depth-two bound. A genuinely two-constraint dual is required.

## Immediate target C: short affine return

For the forced segment

```text
1<=L<=114286,
L<=S<=7771435,
n_L==n_0 (mod 2*X^2),
```

insert the exact affine iterate formula

```text
2^S*n_L=X^L*n_0+B.
```

The terminal two labels alone reproduce a tautology modulo `X^2`; that is not progress. A successful use must retain at least one additional piece of information:

- a third neighbouring label, giving modulus `X^3`;
- a bound on the quotient `(n_L-n_0)/(2X^2)`;
- a signed height/reciprocal potential along the segment;
- or a divisor of `2^S-X^L` imposing a nonlocal condition on `B`.

## Immediate target D: distribution of zero-layer pair classes

Zero-layer pairs form exact classes modulo `2*X^2`. A rigorous counting or discrepancy theorem for their least positive representatives could bound the large zero-delay tail globally.

Needed:

1. express pair representatives as

```text
2^(-v)*(1+X*2^(-u)) (mod X^2);
```

2. count representatives below a variable threshold with explicit error;
3. combine that count with the exact edge-cost budget;
4. beat `0.099934207` without enumerating billions of values.

Asymptotic equidistribution without explicit constants is not a certificate.

## Secondary routes

### Explicit cycle-height route

The repetition ladder forces enormous maxima and diameters, but the retained logarithmic theorem bounds minima. This route needs an explicit max/min comparison or an explicit upper bound on the maximum before the two estimates can interact.

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

> Attack the forced expensive target below X. Couple its exact predecessor label and delay to the reciprocal concentration. In parallel, seek a true two-constraint inverse-window dual. Do not return to local forbidden words or blind cutoff growth.
