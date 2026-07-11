# Audit of the claimed `5x+1` divergence proof in Tremblay (2021)

Robert Tremblay, *The 3x+1 and 5x+1 Problems* (arXiv:2104.10681),
claims that more than `17%` of positive integers start divergent `5x+1`
trajectories.

The paper uses the one-halving map

```text
T_5(n)=n/2          if n is even,
T_5(n)=(5*n+1)/2    if n is odd.
```

For a parity word of length `k`, let `k_2` be the number of odd steps.  The
linear coefficient of the resulting affine iterate is

```text
5^k_2/2^k.
```

The paper correctly observes that

```text
5^k_2>2^k
```

forces the final value after `k` steps to exceed the starting value.  It then
uses this condition in a Pascal-triangle count for integers whose stopping time
is greater than `k`, which requires **every** one of the first `k` values to
remain at least the starting value.

That implication is false.

## Explicit counterexample

Take

```text
n=2,
k=3.
```

The exact trajectory is

```text
2 -> 1 -> 3 -> 8.
```

Its parity word is

```text
even, odd, odd,
```

so

```text
k_2=2,
5^k_2=25>8=2^k.
```

The final value does satisfy

```text
T_5^3(2)=8>2.
```

However the first iterate is

```text
T_5(2)=1<2.
```

Hence the stopping time of `2` is `1`, not greater than `3`.

The condition based only on the total number of odd steps therefore counts the
parity word `even,odd,odd` as finally expanding although it does not represent a
trajectory staying above its starting value for all intermediate times.

For the complete residue block `n=1,...,8` at `k=3`, the condition
`5^k_2>2^k` selects four starts:

```text
1,2,5,7.
```

Only three of them,

```text
1,5,7,
```

actually remain above their start for all three iterations.  Thus the claimed
binomial count already overcounts at the smallest nontrivial example.

## Second logical obstruction

Even a correct positive count of finite prefixes at every length would not by
itself produce a fixed positive integer with infinite stopping time.  The
surviving residue class may change with `k`; nested compatible classes can
converge to a nonordinary `2`-adic integer rather than stabilize at one ordinary
positive integer.

This is the same finite-versus-infinite obstruction recorded in this project
for valuation words and Fermat macroblock programs: every finite program may be
realizable while no one ordinary integer realizes the infinite continuation.

## Consequence

The paper's endpoint inequality is valid, but its use as a stopping-time count
is invalid.  Therefore the claimed positive proportion of divergent `5x+1`
trajectories is not established by the supplied argument and cannot be used as
a solution of the Althofer prize problem.

This audit does not prove that no divergent `5x+1` trajectory exists.  It only
identifies a concrete failure in the proposed proof.

Independent checker:

```text
python tools/verify_tremblay_5x1_audit.py
```

Reference:

R. Tremblay, *The 3x+1 and 5x+1 Problems*, arXiv:2104.10681 (2021).
