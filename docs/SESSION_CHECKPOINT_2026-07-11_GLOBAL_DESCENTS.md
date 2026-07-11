# Session checkpoint: global descent branches

Date: 2026-07-11

The strict prize problem remains open. This session deliberately moved beyond
Priority 1 after inspecting the current fixed-candidate frontier.

## Starting point

For

```text
X=104350542602662257699,
n0=1,
```

the repository already excluded every cycle length through

```text
355561454311274250377
```

except

```text
177780727155637125193,
177780727155637125195.
```

For the first remaining length, the high-layer total is now restricted to

```text
Q<=6241.
```

That remains the strongest finite cycle-exclusion branch, but it still needs a
global distribution theorem.

## New retained result A: near-power exceptional descent

For

```text
X=2^m-d,
d odd,
```

write

```text
r=v2(d*n-1),
d*n-1=2^r*u.
```

The valuation and output split into three exact cases. In the exceptional case
`r=m`,

```text
n=(2^m*u+1)/d,
v2(X*n+1)=m+v2(X*u+1),
C_X(n)=C_X(u)/d,
u<n.
```

Thus every valuation larger than `m` is recursively represented by the same map
at a strictly smaller auxiliary integer.

The specialization

```text
X=13=16-3
```

is especially clean and is now a serious alternative route to an unbounded
height-dependent potential.

Files:

```text
docs/NEAR_POWER_EXCEPTIONAL_DESCENT.md
tools/verify_near_power_exceptional_descent.py
```

The regression checker covers `1235000` parameter-state triples.

## New retained result B: signed digit descent for Fermat multipliers

For

```text
X=2^m+1
```

introduce the signed maps

```text
T_epsilon(n)=oddpart(X*n+epsilon),
epsilon in {+1,-1}.
```

Whenever

```text
n=2^m*u-epsilon,
```

one has exactly

```text
v2(X*n+epsilon)=m+v2(X*u-epsilon),
T_epsilon(n)=T_(-epsilon)(u).
```

After `k` removals, the input lies in one explicit class modulo `2^(m*k)`.
For `X=9`, a valuation of at least `3k` occurs exactly when the ordinary base-8
suffix has the alternating low-digit pattern

```text
7,0,7,0,...
```

of length `k`.

Files:

```text
docs/FERMAT_SIGNED_DIGIT_DESCENT.md
tools/verify_fermat_signed_digit_descent.py
```

The regression checker covers `59994` signed states.

## Current branch assessment

1. The fixed huge candidate remains closest to excluding all cycles through a
   gigantic finite window, but the remaining obstruction is global and may need
   new distribution theory.
2. `X=9,n0=1` is now the cleanest direct-growth branch. The missing lemma is an
   amortized bound saying that the orbit cannot create the forced alternating
   base-8 suffixes fast enough to make the cumulative valuation reach `3t`.
3. `X=13` is the cleanest near-power branch. The missing lemma is a
   height-dependent potential that charges every exceptional descent to growth
   previously needed to create its smaller auxiliary state.
4. The published Mersenne-cycle theorem remains unusable because its proof has
   a recorded elementary counterexample. The new descent identities may replace
   part of its mechanism, but do not yet establish cycle exclusion.

## Recommended next work

### Route 1: amortized suffix accounting for `X=9`

Let

```text
a_t=3*k_t+r_t,
0<=r_t<=2.
```

Use the exact signed suffix descent to build a stack or potential whose increase
pays for the creation of each `7,0,7,0,...` suffix block and whose decrease pays
for `k_t`. The target inequality is

```text
sum_(j<t) a_j <= 3*t-1.
```

### Route 2: exceptional-depth potential for `X=13`

Define the exceptional depth by repeated integral use of

```text
R(u)=(16*u+1)/3.
```

Seek a potential combining ordinary height and exceptional depth, for example a
piecewise logarithmic quantity, so that every deep exceptional contraction is
charged to the larger state `R^k(u)` that had to exist beforehand.

### Route 3: retain Priority 1 as a parallel branch

The exact refined residue positions may still close `Q=6241`, but this should no
longer block work on the two direct-growth descents above.

## Verification

Both new checkers are included in

```text
python run_checks.py
```

Finite regression checks support the algebra and guard against implementation
errors. They are not themselves proofs of divergence.
