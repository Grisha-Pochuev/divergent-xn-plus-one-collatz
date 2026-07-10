# Residue-crowding improvement for the fixed cycle barrier

Consider the fixed multiplier

```text
X = 104350542602662257699
```

and its accelerated odd-only map. This note gives a valid improvement of the retained finite cycle barrier without using the retracted condition `ord_X(2) | A`.

## 1. Allowed residue classes

Let

```text
M = 15099 = 3*7*719.
```

Since `M | X`, every accelerated output `n'` with halving count `a` satisfies

```text
2^a*n' == 1 (mod M).
```

The order of `2` modulo `M` is

```text
h = 2154.
```

Therefore every cycle element lies in one of the `h` odd residue classes represented by

```text
rho(a) = least positive odd integer congruent to 2^(-a) (mod M).
```

The orbit cannot return to `1`, so in the residue class `1 mod M` we replace the forbidden representative `1` by the next positive odd representative `1+2M`.

The least allowed representative is `25`.

## 2. Distinctness gives a logarithmic reciprocal bound

The elements of a nontrivial cycle are distinct. In one allowed odd residue class with least allowed representative `rho`, its possible positive elements are

```text
rho, rho+2M, rho+4M, ...
```

If a cycle has length `p`, then the reciprocal contribution of this class is at most

```text
1/rho + integral_0^(p-1) dx/(rho+2M*x)
= 1/rho + log(1+2M*(p-1)/rho)/(2M).
```

Summing over all `h` classes and using `rho>=25` gives

```text
sum_i 1/n_i
<= S0 + h*log(1+2M*(p-1)/25)/(2M),
```

where `S0` is the exact rational sum of the reciprocals of the `2154` least allowed representatives.

For every cycle,

```text
Lambda = A*log(2)-p*log(X)
       = sum_i log(1+1/(X*n_i))
       <= (1/X)*sum_i 1/n_i.
```

Thus the correction is logarithmic in `p`, rather than the earlier crude linear bound `p/(25X)`.

## 3. Exact finite barrier

Put

```text
B = 170000000000000000000.
```

For `p<=B`, the exact verifier uses only rational inequalities:

1. `log(2) < 7/10`;
2. `log(2) > 2/3`;
3. for `q>1`, `log(q) > 2*(q-1)/(q+1)`;
4. `log(1+z) <= k*log(2)` whenever `1+z<=2^k`.

At this `B`, the required exponent is `k=78`. Let

```text
epsilon = X^2/2^133 - 1.
```

For even `p=2r`, the verifier proves

```text
r*epsilon + reciprocal_bound/X < log(2),
```

so the product around a cycle lies strictly between consecutive powers of two.

For odd `p=2r+1`, it proves

```text
r*epsilon + reciprocal_bound/X < log(2^67/X),
```

again placing the cycle product strictly between consecutive powers of two.

Therefore no nontrivial positive cycle of accelerated length at most

```text
170000000000000000000
```

can occur for this fixed multiplier.

## 4. Significance

This raises the valid retained barrier from

```text
148557456445856651509
```

to

```text
170000000000000000000.
```

The improvement is modest in percentage but principled: it replaces a worst-case bound that allowed every cycle element to equal `25` by the exact fact that cycle elements are distinct and distributed among only `2154` allowed odd residue classes.

The proof remains finite. It does not exclude cycles of all lengths and therefore does not yet prove divergence.
