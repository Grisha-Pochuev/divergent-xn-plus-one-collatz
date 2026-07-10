# Balanced occupancy dual bound

Consider the fixed multiplier

```text
X = 104350542602662257699
```

and

```text
M = 15099,
H = ord_M(2) = 2154,
d = 2M.
```

This note strengthens the residue-crowding estimate by enforcing that a cycle of length `p` contains only `p` elements in total. The earlier class-by-class envelope safely allowed nearly `p` elements in each of the `H` classes at once.

## 1. Class occupancies

For `1<=t<=H`, let `rho_t` be the least admissible positive representative of class `t` modulo `d`; in the class containing the literal value `1`, use the next representative because the fixed orbit cannot return to `1`.

Let `c_t` be the number of cycle elements in class `t`. Then

```text
sum_t c_t = p,
sum_t t*c_t <= A <= 67p-1.
```

Distinct elements in class `t` lie in

```text
rho_t, rho_t+d, rho_t+2d, ...
```

and therefore their reciprocal contribution is at most

```text
0                                                    if c_t=0,
1/rho_t + log(1+d*(c_t-1)/rho_t)/d                  if c_t>=1.
```

Put

```text
y_t = max(c_t-1,0).
```

If `m` classes are occupied, then

```text
sum_t y_t = p-m,
sum_t t*y_t <= 67p-1,
0<=m<=H.
```

Thus

```text
sum_i 1/n_i
 <= S0 + sum_t f_t(y_t),
S0 = sum_t 1/rho_t,
f_t(y)=log(1+d*y/rho_t)/d.
```

The unused terms `1/rho_t` for empty classes only make this an upper bound.

## 2. Rational dual certificate

Choose

```text
alpha = -32,
beta  = 33,
mu_t  = (alpha+beta*t)/(d*p).
```

Since `alpha+beta*t>0` for every `t>=1`, concavity gives, for all `y>=0`,

```text
f_t(y) <= mu_t*y + K_t,
```

where

```text
K_t = [log(1/(rho_t*mu_t))-1+rho_t*mu_t]/d.
```

All displayed logarithm arguments exceed `1` at the retained barrier.

Summing the tangent inequalities and using `m<=H` gives the exact safe bound

```text
sum_t mu_t*y_t
 <= alpha/d - alpha*H/(d*p)
    + beta*(67p-1)/(d*p).
```

The term `-alpha*H/(d*p)` is needed because `alpha<0` and `sum y_t=p-m` rather than exactly `p`.

The logarithms in `K_t` are certified without floating point. Each positive rational `q` is written as

```text
q = 2^k*u,  1<=u<2,
```

and `log(2)` and `log(u)` are bounded above by the finite atanh series

```text
log(z)=2*(w+w^3/3+w^5/5+...),
w=(z-1)/(z+1),
```

with the omitted tail bounded geometrically. Each result is rounded upward to a common dyadic denominator `2^70` before summation.

## 3. Certified reciprocal envelope

For the barrier in the companion verifier, the resulting exact rational bound satisfies

```text
sum_i 1/n_i < 3.217731.
```

This is substantially smaller than the previous transition-budget envelope, approximately

```text
3.820166.
```

The gain comes from using both global occupancy conditions simultaneously:

```text
sum c_t=p,
sum t*c_t<=67p-1.
```

No orbit search is involved.

## 4. New finite barrier

Substitution into the retained even- and odd-length power-of-two interval tests proves that no nontrivial positive accelerated cycle can have length

```text
p <= 176022359338834903230.
```

The next integer

```text
176022359338834903231
```

fails the retained odd-length rational interval test for this certificate.

Run

```text
python tools/verify_balanced_occupancy_barrier.py
```

for the exact check.

This remains a finite cycle obstruction, not a proof of divergence.