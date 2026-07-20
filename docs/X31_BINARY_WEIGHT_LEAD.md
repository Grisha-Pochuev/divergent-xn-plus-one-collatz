# Conjectural binary-weight route for `X=31, n0=3`

Date: 2026-07-20

## Status

This note records a promising but **unproved** route. It is not a divergence
proof and must not be presented as a solution to the Althöfer prize problem.
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

Therefore the conjectural estimate

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

## 3. Exact one-step binary identity

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

## 4. Exact finite evidence

The command

```text
python tools/check_x31_binary_weight.py --steps 100000
```

was run with exact Python integer arithmetic. It returned

```text
steps_checked:                 100000
finite_inequality_holds:       true
minimum_slack:                 0
minimum_slack_step:            1
final_orbit_value_bits:        296182
final_cumulative_halvings:     199240
final_binary_weight:           147795
is_proof_of_infinite_divergence: false
```

Here

```text
slack_t=4*t+2-(A_t+s_2(n_t)).
```

Thus (2) holds on the first `100000` accelerated steps, with equality at the
first step. This is finite evidence only. It does not exclude a later failure.

## 5. Exact missing lemma

The route is completed by proving:

> For the accelerated `31n+1` orbit starting from `n_0=3`, prove
> `A_t+s_2(n_t)<=4*t+2` for every integer `t>=1`.

A useful strengthening would construct a nonnegative carry potential `P(n)` and
prove a telescoping inequality of the form

```text
A_t+s_2(n_t)+P(n_t)<=4*t+constant.
```

Any proposed potential must be tested against the existing no-go results for
fixed finite-state positive-mean certificates: it may need unbounded digital
information rather than only a fixed residue class.

## 6. Verification

Run

```text
python tools/check_x31_binary_weight.py --steps 100000
```

The checker reports the first failure if one occurs and explicitly marks its
output as not being an infinite proof.
