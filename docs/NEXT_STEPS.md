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
p <= 170000000000000000000.
```

### Immediate symbolic target

Use not only the set of allowed output classes modulo `2M`, but also the transition relation between consecutive classes.

For a step with valuation `a_i`,

```text
2^a_i*n_(i+1) == 1 (mod M).
```

The present residue-crowding bound treats the allowed classes independently. A stronger argument should exploit that the class of `n_i`, the valuation `a_i`, and the class of `n_(i+1)` are linked by the exact step equation.

Concrete tasks:

1. Derive the exact finite transition graph modulo a small divisor of `X`, retaining all required information.
2. Prove which transitions or short transition words are impossible.
3. Convert those restrictions into a smaller upper bound for

```text
sum_i 1/n_i
```

than the current independent-class envelope.
4. Check whether the improved correction can cross more power-of-two intervals, not merely enlarge the first finite interval.

No long trajectory search is needed for these steps.

### Global completion target

Find a modular or descent invariant that excludes every possible cycle while preserving the correct factor

```text
product_i(n_i)
```

in the cycle congruence.

A valid result must not assume `ord_X(2)|A`.

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

Finite chains are useful reconnaissance but are not a proof.

## Priority 4: stabilized low-average valuation code

Every finite exact valuation word is coded by one residue class. The missing object is an infinite word with

```text
limsup average(a_t) < log2(X)
```

whose least coding representatives eventually stabilize at one positive integer.

A key audit observation is that eventual stabilization is very restrictive: once the representative stabilizes, the infinite word is simply the actual valuation sequence of that fixed integer. Thus this route must discover structure in a real orbit, not manufacture an arbitrary infinite word independently.

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

Start with Priority 1 and ask:

> Can the exact transition structure among the 2154 allowed classes force a stricter reciprocal-sum bound or exclude whole parity classes of hypothetical cycle lengths?

This is the closest continuation of the current strongest valid result and does not require heavy CPU work.
