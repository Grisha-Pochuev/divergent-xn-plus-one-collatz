# Sharp logarithmic interval certificate

This note keeps the large-divisor transition bound unchanged and sharpens only the rigorous lower bounds for the gaps between adjacent powers of two.

For the fixed multiplier

```text
X = 104350542602662257699
```

let

```text
epsilon = X^2/2^133 - 1 > 0.
```

The large-divisor valuation split gives an exact rational upper bound `R(p)` for

```text
sum_i 1/n_i.
```

Hence every hypothetical cycle satisfies

```text
Lambda = A*log(2)-p*log(X) <= R(p)/X.
```

## 1. Exact lower logarithm series

For every rational `z>1`, put

```text
y=(z-1)/(z+1).
```

Then

```text
log(z)=2*(y+y^3/3+y^5/5+...).
```

All terms are positive, so every finite partial sum is a rigorous lower bound.
The certificate uses the first `14` terms for

```text
log(2)
```

and

```text
log(2^67/X).
```

No floating-point logarithm is used in the proof.

The former odd-length certificate used only the first term

```text
2*(q-1)/(q+1),
q=2^67/X.
```

The extra positive terms recover most of the previously discarded gap.

## 2. Even lengths

For `p=2r`, the identity

```text
X^(2r)=2^(133r)*(1+epsilon)^r
```

and `log(1+epsilon)<=epsilon` show that a cycle is impossible whenever

```text
r*epsilon + R(p)/X < log(2).
```

The right side is replaced by its exact 14-term rational lower sum.

## 3. Odd lengths

For `p=2r+1`, the next possible power of two is separated from `X^p` by

```text
log(2^67/X)-r*log(1+epsilon).
```

Thus a cycle is impossible whenever

```text
r*epsilon + R(p)/X < log(2^67/X).
```

Again the right side is replaced by the exact 14-term rational lower sum.

## 4. Improved barrier

Combining the sharp logarithm bounds with the retained large-divisor reciprocal envelope proves that no nontrivial positive accelerated cycle can have length

```text
p <= 177780727155637125182.
```

The next integer

```text
177780727155637125183
```

fails the odd-length inequality for this exact certificate.

This raises the preceding barrier

```text
176022359338834903234
```

by

```text
1758367816802221948
```

accelerated steps, approximately `0.999%`.

Run

```text
python tools/verify_sharp_log_barrier.py
```

for the exact check.

The result remains finite and therefore is not yet a proof that the fixed orbit diverges.