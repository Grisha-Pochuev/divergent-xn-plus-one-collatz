# Binary-weight and zero-bit route for `X=31, n0=3`

Date: 2026-07-21

## Status

This note records an exact reduction and a promising but **unproved** sufficient
inequality. It is not a divergence proof and must not be presented as a solution
to the Althöfer prize problem.

The exact finite checker is

```text
tools/check_x31_binary_weight.py
```

## 1. Orbit and notation

Use the accelerated map

```text
C_31(n)=(31*n+1)/2^v2(31*n+1)
```

with

```text
n_0=3.
```

Write

```text
a_t=v2(31*n_t+1),
A_t=a_0+...+a_(t-1),
A_0=0,
```

and let `s_2(n)` denote the number of `1` bits in the binary expansion of `n`.
The first accelerated values are

```text
3 -> 47 -> 729 -> 2825 -> 10947 -> 169679 -> 2630025 -> ...
```

## 2. Exact conditional divergence criterion

The affine iteration identity gives

```text
n_t > 3*31^t/2^A_t.                                  (1)
```

Therefore the estimate

```text
A_t+s_2(n_t)<=4*t+2                                  (2)
```

would imply, since every positive odd `n_t` has `s_2(n_t)>=1`,

```text
A_t<=4*t+1.
```

Substitution into (1) would give

```text
n_t >(3/2)*(31/16)^t -> +infinity.                   (3)
```

Thus proving (2) for every `t>=1` would be a complete explicit solution with

```text
X=31,
n0=3.
```

## 3. Exact one-step carry identity

Every accelerated transition satisfies

```text
31*n_t+1=2^a_t*n_(t+1).
```

Hence

```text
31*n_t
 =2^a_t*n_(t+1)-1
 =2^a_t*(n_(t+1)-1)+(2^a_t-1).
```

The two terms on the final line occupy disjoint binary positions. Consequently

```text
s_2(31*n_t)=a_t+s_2(n_(t+1)-1).                      (4)
```

This is an exact carry identity. A proof of (2) must control how multiplication
by

```text
31=(11111)_2
```

creates and destroys binary carries over many consecutive steps. A naive
one-step monotonicity argument is insufficient because `s_2(n_t)` can increase
sharply on individual steps.

## 4. Exact zero-bit reformulation

Let

```text
L_t=bit_length(n_t),
w_t=s_2(n_t),
z_t=L_t-w_t,
```

so that `z_t` is the number of zeroes among the `L_t` binary digits of `n_t`.
Define the one-step length defect

```text
delta_t=L_t+5-bit_length(31*n_t+1).                  (5)
```

Since an `L_t`-bit positive integer satisfies

```text
2^(L_t-1)<=n_t<2^L_t,
```

and `31` has five binary digits, `31*n_t+1` has either `L_t+4` or `L_t+5`
bits. Therefore

```text
delta_t in {0,1}.                                    (6)
```

Division by `2^a_t` removes exactly `a_t` trailing zeroes. Hence

```text
L_(t+1)=L_t+5-a_t-delta_t.                           (7)
```

Put

```text
Delta_t=sum_(j<t) delta_j.
```

Since `L_0=2`, summing (7) gives

```text
L_t=2+5*t-A_t-Delta_t.                               (8)
```

Using `w_t=L_t-z_t` in (8) yields the exact identity

```text
4*t+2-(A_t+s_2(n_t))=z_t+Delta_t-t.                 (9)
```

Thus the desired binary-weight estimate (2) is **equivalent** to

```text
z_t+Delta_t>=t for every t>=1.                       (10)
```

This is a genuine simplification of the missing lemma: each step must be paid
for either by a zero digit currently present in `n_t` or by a previous
one-bit loss in the product length.

## 5. Stronger sufficient zero-count conjecture

A simpler but stronger sufficient statement is

```text
z_t>=t for every t>=1.                               (11)
```

Because `Delta_t>=0`, (11) implies (10), hence (2), and therefore the explicit
divergence conclusion (3).

Statement (11) is not known for all `t`. It should be treated as a focused
research target, not as a theorem.

## 6. Exact finite evidence

The command

```text
python tools/check_x31_binary_weight.py --steps 300000
```

was run with exact Python integer arithmetic. It verified at every checked step:

```text
original slack = 4*t+2-(A_t+s_2(n_t))
               = z_t+Delta_t-t,
```

and returned the following final data:

```text
steps_checked:                    300000
final_orbit_value_bits:           888152
final_cumulative_halvings:        598109
final_binary_weight:              444348
final_zero_bits:                  443804
final_cumulative_length_defects:  13741
minimum_original_slack:           0 at t=1
minimum_strong_zero_slack:        0 at t=1
first_original_failure_step:      none
first_strong_zero_failure_step:   none
```

At the final checked step the stronger zero-count inequality has slack

```text
z_t-t=143804.
```

This is finite evidence only. It does not exclude a later failure.

## 7. Exact missing lemma

This route is completed by either of the following:

1. prove the equivalent inequality

```text
z_t+Delta_t>=t
```

for every `t>=1`; or

2. prove the stronger and simpler inequality

```text
z_t>=t
```

for every `t>=1`.

A useful strengthening would construct a nonnegative, possibly unbounded carry
potential `P(n)` and prove a telescoping inequality of the form

```text
A_t+s_2(n_t)+P(n_t)<=4*t+constant.
```

Any proposed potential must be tested against the existing no-go results for
fixed finite-state positive-mean certificates. It may need unbounded digital
information rather than only a fixed residue class.

## 8. Verification discipline

Run

```text
python tools/check_x31_binary_weight.py --steps 300000
```

The checker reports the first failure of either conjectural inequality, verifies
the exact slack identity (9), and explicitly marks its output as not being an
infinite proof.
