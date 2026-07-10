# Periodic valuation tails cannot diverge

Let

```text
C_X(n) = (X*n + 1) / 2^v2(X*n + 1)
```

on positive odd integers, with odd `X >= 5`.

This note proves a structural obstruction that narrows the search for a divergent orbit: an orbit whose exact halving counts are eventually periodic must itself be eventually periodic. In particular, a divergent positive orbit must have a genuinely aperiodic valuation sequence.

## One valuation block

Fix a nonempty block

```text
a = (a_0, ..., a_(p-1)),   a_i >= 1.
```

Put

```text
A_0 = 0,
A_j = a_0 + ... + a_(j-1),
A   = a_0 + ... + a_(p-1),
B   = sum_(j=0)^(p-1) X^(p-1-j) * 2^A_j.
```

Whenever an orbit follows this block for `p` accelerated steps, its block endpoint is

```text
F(n) = (X^p*n + B) / 2^A.
```

Define

```text
P = X^p,
D = P - 2^A.
```

Both `D` and `B` are odd. The affine map has the rational fixed point

```text
r = -B / D.
```

The key identity is

```text
D*F(n) + B = P*(D*n + B) / 2^A.
```

After `k` repetitions,

```text
D*F^k(n) + B = P^k*(D*n + B) / 2^(k*A).
```

## Finite repetition bound

**Proposition.** Suppose the exact valuation block `a` repeats `k` consecutive times from a positive odd integer `n`. If `D*n+B != 0`, then

```text
k <= floor((v2(D*n+B) - 1) / A).
```

Here `v2` is applied to the absolute value when `D*n+B` is negative.

**Proof.** After `k` complete blocks, `F^k(n)` is again an odd integer. Since `D` and `B` are odd,

```text
D*F^k(n) + B
```

is even, so its 2-adic valuation is at least `1`. The displayed identity and the oddness of `P=X^p` give

```text
v2(D*n+B) - k*A >= 1.
```

Rearranging proves the bound. QED.

If `D*n+B=0`, then `n=r` and `F(n)=n`; the block closes into a `p`-step cycle, provided its internal exact valuations are indeed the stated block.

## Main corollary

**Corollary.** If the exact sequence

```text
v2(X*n_t+1)
```

is eventually periodic, then the integer orbit is eventually periodic. Therefore no orbit tending to positive infinity can have an eventually periodic valuation tail.

**Reason.** Start at the beginning of the periodic tail and repeat its period block arbitrarily many times. The finite repetition bound can hold for every `k` only when `D*n+B=0`. Hence the state is fixed by the corresponding block map and lies on a cycle.

There is an especially clear sign obstruction in the expanding case. If

```text
X^p > 2^A,
```

then `D>0`, while `B>0`, so the only infinitely repeating 2-adic fixed point is

```text
r = -B/D < 0.
```

Thus a positive integer cannot follow a positive-drift valuation block forever.

## Recovery of the finite-growth construction

Take

```text
X = 2^m + 1
```

and the one-symbol block `(m)`. Then

```text
p=1, A=m, B=1, D=X-2^m=1, r=-1.
```

The repetition bound becomes

```text
number of exact m-blocks <= floor((v2(n+1)-1)/m).
```

For

```text
n = 2^(m*L)-1,
```

this gives exactly `L-1` repetitions. This explains, in a single general formula, why the repository's arbitrarily long increasing construction is necessarily finite: it shadows the negative 2-adic fixed point `-1`, and the available 2-adic precision is exhausted after `L-1` blocks.

## Consequences for the search

This rules out the simplest proposed certificate: a deterministic finite-state machine that assigns one exact valuation to each state along a single orbit. Such a machine would eventually repeat a state, hence eventually repeat its valuation pattern, and therefore could only certify a cycle.

A successful finite certificate must instead do at least one of the following:

1. certify inequalities over a branching family of possible valuations rather than prescribe one exact periodic word;
2. use an unbounded numerical quantity such as capital, height, or 2-adic precision;
3. prove an aperiodic chain of different growth blocks whose accumulated gain dominates every exit loss.

The third option suggests a sharper computational target: search for **regenerative block chains**, not endlessly repeated motifs. For each observed block, the rational center `-B/D` and the quantity `v2(D*n+B)` measure exactly how long that block can continue.