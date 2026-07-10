# Large-divisor valuation split

For the fixed multiplier

```text
X = 104350542602662257699
```

use the factorization

```text
X = 3*7*719*6911089648497401.
```

Put

```text
P = 6911089648497401,
M = 15099,
H = ord_M(2)=2154,
K = 400000.
```

This note combines the exact incoming valuation with two different divisors of `X`.

## 1. Partition by the incoming exact valuation

For a cycle element `n_i`, let `a_(i-1)` be the exact valuation on the step entering it. Since `P|X`,

```text
2^a*n_i == 1 (mod P).
```

Thus, for each fixed exact valuation `a`, the corresponding outputs occupy one odd residue class modulo `2P`.

Split the cycle elements into:

```text
low:  1<=a<=K,
high: a>=K+1.
```

## 2. The low-valuation part

For every `1<=a<=K`, let `pi_a` be the least admissible positive odd representative of

```text
2^(-a) (mod P)
```

modulo `2P`. If the representative is the forbidden literal value `1`, replace it by `1+2P`.

Distinct low-valuation elements with the same incoming `a` lie in

```text
pi_a, pi_a+2P, pi_a+4P, ...
```

If the whole cycle has length at most `p`, the contribution of this valuation class is at most

```text
1/pi_a + log(1+2P*(p-1)/pi_a)/(2P).
```

The verifier enumerates exactly the first `K=400000` inverse powers. It finds

```text
min_(1<=a<=K) pi_a = 18989746471.
```

The initial reciprocal sum is rounded upward term by term to a common dyadic denominator. The logarithmic tails are then bounded uniformly using this exact minimum.

At the retained barrier, the complete low-part contribution is less than

```text
2.186*10^(-9).
```

This is a short modular enumeration, not a trajectory search.

## 3. The high-valuation part

Let `h` be the number of cycle elements whose incoming valuation is at least `K+1`. The total valuation satisfies

```text
A <= 67p-1,
```

so

```text
h <= floor((67p-1)/(K+1)).
```

Every high element is still in one of the `H=2154` allowed classes modulo `2M`. Let `rho_t` be the least admissible representative of class `t`, with the literal `1` excluded.

For high-class counts `c_t`,

```text
sum c_t <= h.
```

Using

```text
f_t(c)=log(1+2M*c/rho_t)/(2M)
```

and the common tangent slope

```text
mu = H/(2M*h),
```

concavity gives an exact total-occupancy envelope. The logarithms are bounded by the same rational atanh-series certificate used for the balanced occupancy result.

## 4. Combined reciprocal bound

At

```text
p = 176022359338834903234,
```

the exact certificate gives

```text
high contribution < 2.774598819,
low contribution  < 0.000000003,
total              < 2.774598821.
```

This is smaller than the preceding balanced occupancy bound

```text
3.217731.
```

## 5. Improved cycle barrier

Substitution into the retained power-of-two interval test proves that no nontrivial positive accelerated cycle can have length

```text
p <= 176022359338834903234.
```

The next integer

```text
176022359338834903235
```

fails the retained odd-length rational test for this certificate.

Run

```text
python tools/verify_large_divisor_split_barrier.py
```

for the exact verification.

The result is still a finite cycle barrier and therefore not yet a proof of divergence.