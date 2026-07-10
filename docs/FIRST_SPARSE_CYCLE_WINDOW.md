# First sparse cycle window

For the fixed multiplier

```text
X = 104350542602662257699
```

put

```text
E = X^2/2^133 = 1+epsilon,
eta = log(E)>0.
```

The sharp-log barrier stops immediately before the first odd length at which `X^p` comes extremely close to the next power of two. It does not follow that all later lengths are difficult: after `X^p` crosses that power, the gap to the following power jumps back to almost `log(2)`.

This note makes that observation rigorous using the retained large-divisor reciprocal bound.

## 1. Uniform correction bound

Let

```text
CAP = 355561454311274250377.
```

Evaluate the large-divisor reciprocal certificate at `CAP`. Its construction gives a valid uniform upper bound for every cycle length `p<=CAP`:

```text
Lambda = A*log(2)-p*log(X) <= C,
C = R(CAP)/X.
```

The verifier obtains

```text
R(CAP) approximately 2.824749479.
```

All logarithms below use exact rational lower and upper bounds from the positive atanh series, including a geometric upper bound for the omitted tail.

## 2. Even lengths

For `p=2r`,

```text
p*log(X)=133r*log(2)+r*eta.
```

As long as `r*eta<log(2)`, the gap to the next power of two is

```text
log(2)-r*eta.
```

The exact certificate proves that this gap is greater than `C` for every even

```text
p <= 355561454311274250376.
```

Therefore every even cycle length up to that value is impossible.

## 3. Odd lengths and the first crossing

For odd `p=2r+1`,

```text
p*log(X)
 = (133r+66.5)*log(2) + (p/2)*eta.
```

Before the first crossing, the gap to the next power is

```text
[log(2)-p*eta]/2.
```

The last odd length for which the exact lower bound on this gap exceeds `C` is

```text
177780727155637125181.
```

The only odd lengths not excluded before the crossing are

```text
177780727155637125183
177780727155637125185
177780727155637125187
177780727155637125189
177780727155637125191
177780727155637125193
177780727155637125195
```

There are exactly seven of them.

Starting at

```text
177780727155637125197,
```

`X^p` has crossed that power of two. Until the next odd crossing, the gap to the following power is

```text
[3*log(2)-p*eta]/2.
```

This gap is decreasing in `p`, but even at `CAP` its exact rational lower bound is still greater than `C`. Hence every odd length from

```text
177780727155637125197
```

through `CAP` is impossible.

## 4. Rigorous sparse-window conclusion

Every nontrivial positive accelerated cycle with length

```text
p <= 355561454311274250377
```

is impossible, except possibly for the seven explicitly listed odd lengths.

This is stronger than a contiguous barrier: it crosses the first power-of-two interval and reduces an additional range of about

```text
1.78*10^20
```

lengths to seven isolated candidates.

Run

```text
python tools/verify_first_sparse_cycle_window.py
```

for the exact certificate.

The seven exceptional lengths are not proved to occur. They are merely the lengths not excluded by the current interval and reciprocal inequalities. Excluding those seven values would immediately raise the contiguous cycle barrier to the displayed `CAP`.