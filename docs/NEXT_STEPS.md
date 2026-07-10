# Prioritized next steps

The strict prize problem remains open. This file lists concrete next actions in priority order and separates lightweight symbolic work from optional heavy computation.

## Priority 1: strengthen the fixed-candidate cycle obstruction

Current candidate:

```text
X  = 104350542602662257699,
n0 = 1.
```

Current valid barrier:

```text
p <= 176022359338834903228.
```

### What is now closed

The unaugmented directed graph on the `2154` allowed output classes modulo `2M`, with `M=15099`, is complete. Every edge, loop, and finite class word is realizable by some positive start.

Therefore do **not** repeat either of these searches:

1. forbidden one-step transitions among the bare `2154` labels;
2. forbidden short words among those labels alone.

Any finite-state refinement must retain more information than the output class modulo `2M`.

Files:

```text
docs/RESIDUE_TRANSITION_NO_GO.md
tools/verify_residue_transition_no_go.py
```

### Retained global transition constraints

For a hypothetical cycle of length `p`, with class occupancies `c_t`, the repository proves

```text
sum_t c_t = p,
sum_t t*c_t <= 67p-1.
```

Cycle closure also gives exact source/target flow balance:

```text
#{current elements in class t}
=
#{outgoing steps whose successor enters class t}.
```

The source partition is sparse modulo `2M`, while the outgoing-target partition is sparse modulo `2^t`. These two descriptions use the same count vector.

Files:

```text
docs/RESIDUE_VALUATION_BUDGET.md
tools/verify_residue_valuation_budget.py
docs/TRANSITION_BALANCED_RECIPROCAL_REDUCTION.md
tools/verify_transition_balance.py
```

### Immediate lightweight target

Convert the transition-balanced reciprocal reduction into an exact optimization certificate.

Concrete tasks:

1. For a rational mixing parameter `lambda`, maximize the separable concave envelope

```text
lambda*sum_t R_t(c_t)
+(1-lambda)*sum_t B_t(c_t)
```

under

```text
c_t >= 0 integer,
sum_t c_t = p,
sum_t t*c_t <= 67p-1.
```

2. Replace numerical optimization by rational tangent-line or Lagrange-dual inequalities that a short verifier can check.
3. Determine the exact best reciprocal constant obtainable from the balanced reduction.
4. Record the numerical limitation honestly: for the present multiplier, improving the reciprocal correction alone moves the current power-of-two interval barrier by only a few lengths.

No trajectory search is required.

### More important global target

Because the present interval barrier is controlled mainly by the tiny gap between `X^2` and `2^133`, Priority 1 ultimately needs more than a slightly smaller reciprocal correction.

Search for an augmented transition invariant retaining one or more of:

1. exact valuation `a`, not only `a modulo 2154`;
2. the quotient `q=(a-t)/2154` as a height cost;
3. a binary residue of the source;
4. a potential on source/target classes whose sum telescopes around a cycle;
5. a global closure condition preserving the correct factor `product_i(n_i)`;
6. a height-dependent descent rule capable of crossing infinitely many power-of-two intervals.

A valid result must not assume `ord_X(2)|A`.

### Current numerical certificate

The transition-class cost budget gives

```text
p <= 176022359338834903228.
```

Files:

```text
docs/TRANSITION_BUDGET_CYCLE_BARRIER.md
tools/verify_transition_budget_barrier.py
```

For fair comparison, the old independent-class envelope, saturated under the same rational bounds, reaches `176022359338834903224`; the strict gain from the class-cost information is `4` lengths. The increase from the previously retained round barrier `170000000000000000000` is about `3.54%`.

## Priority 2: combine cycle-height upper and lower bounds

The logarithmic reduction gives

```text
minimum cycle element <= K_X*p^D_X.
```

Needed:

1. make `K_X,D_X` explicit for a carefully chosen fixed multiplier;
2. derive a modular lower bound on the cycle minimum that grows with `p`;
3. prove that the lower bound eventually exceeds the polynomial upper bound;
4. use a finite exact certificate for the remaining lengths.

This route is attractive only if the modular lower bound genuinely grows with cycle length. A constant lower bound such as `25` cannot finish it.

## Priority 3: ordinary-integer regenerative chain

For `X=2^m+1`, study the exact return map

```text
u -> odd_part(X^L*u-1).
```

Goal: construct one ordinary positive integer whose orbit contains infinitely many complete net-positive bursts.

Concrete tasks:

1. derive composition laws for two or more arbitrary-core bursts;
2. identify conditions under which the output core enters another profitable burst class;
3. search symbolically for branching rather than a single nested 2-adic target;
4. prove that at least one branch corresponds to an ordinary positive integer;
5. establish a cumulative growth estimate that survives all exits.

Finite chains are useful reconnaissance but are not a proof. The finite-program realization theorem is recorded in `docs/FINITE_MACROBLOCK_PROGRAMS.md` and shows that any finite chain can be built exactly; the unresolved step is one fixed ordinary start for an infinite chain.

## Priority 4: stabilized low-average valuation code

Every finite exact valuation word is coded by one residue class. The missing object is an infinite word with

```text
limsup average(a_t) < log2(X)
```

whose least coding representatives eventually stabilize at one positive integer.

A key audit observation is that eventual stabilization is very restrictive: once the representative stabilizes, the infinite word is simply the actual valuation sequence of that fixed integer. Thus this route must discover structure in a real orbit, not manufacture an arbitrary infinite word independently.

## Priority 5: digital invariant for `X=9, n0=1`

For the accelerated `9n+1` orbit from `1`, define

```text
A_t = cumulative halving count,
S_t = 2^A_t*n_t.
```

Then exactly

```text
S_0=1,
S_(t+1)=9*S_t+2^v2(S_t),
v2(S_t)=A_t.
```

A proof of

```text
v2(S_t) <= 3*t-1
```

for every `t>=1` would imply

```text
n_t >= 2*(9/8)^t -> +infinity.
```

The stronger bound `v2(S_t)<=3*t-2` holds on the first `10000` exact steps, but this is finite evidence only. The next symbolic task is to find a binary carry invariant or finite-state description preventing a trailing-zero run of length `3t`.

Files:

```text
docs/X9_DIGITAL_INVARIANT_LEAD.md
tools/check_x9_digital_invariant.py
```

## Lightweight verification tasks

These are safe inside a normal chat session:

- exact modular arithmetic for small moduli;
- symbolic derivations;
- short enumeration of residue classes or transition states;
- rational interval bounds;
- regression tests on known cycles;
- checking documentation consistency.

## Tasks requiring explicit user approval

Do not start these automatically:

- multi-hour trajectory scans;
- large parameter searches;
- large GitHub Actions matrices;
- exhaustive searches with high memory use;
- repeated high-precision computation when a symbolic bound is available.

## Acceptance checklist for any claimed breakthrough

A candidate final proof must provide:

1. explicit odd `X>=5` and odd positive `n0`;
2. a proof that the orbit cannot enter any positive cycle;
3. a proof that the orbit cannot return to a previously visited value;
4. the positive-integer dichotomy showing the remaining possibility is `+infinity`;
5. exact, independently runnable verification of every finite certificate;
6. no reliance on random-model assumptions or finite trajectory size.

## Recommended next session

Continue Priority 1 with:

> Can the exact source/target flow balance be certified by rational potentials or tangent inequalities, and can an augmented height-dependent transition state yield a global obstruction rather than only a slightly better finite reciprocal bound?

Do not return to forbidden-edge enumeration on the bare `2154` classes; that abstraction is now rigorously known to be complete.
