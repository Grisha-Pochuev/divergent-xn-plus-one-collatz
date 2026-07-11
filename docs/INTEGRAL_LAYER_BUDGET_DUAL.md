# Integral full-layer budget dual

This note strengthens the retained small-value reciprocal bound for the harder
remaining length

```text
p = 177780727155637125195.
```

The improvement comes from retaining the unknown total full-order layer count
as an integer instead of eliminating it immediately.

Put

```text
B=A-p=11644637628694231700273,
O=ord_X(2)=1860810887857924950,
Q=sum_i q_i.
```

The exact full-label decomposition gives

```text
0<=Q<=6257,
sum_i (s_i-1)=B-O*Q.                              (1)
```

## 1. Three independent selected-item constraints

For each retained target `n<=1000000`, define

```text
l(n)=s(n)-1,
h(n)=h_3(n),
F(n)=signed-label potential cost.
```

Here `h_3(n)` is the minimum layer sum in a three-edge inverse window and
`F(n)` is the valid cost from `SIGNED_LABEL_POTENTIAL_DUAL`:

```text
F(n)=2*(u(n)+s(n)-2)+2*O*d(n).
```

For any selected set of actual cycle values, the exact global identities imply

```text
sum l(n) <= B-O*Q,                                 (2)
sum h(n) <= 3*Q,                                   (3)
sum F(n) <= 2*B.                                   (4)
```

The previous certificate combined these resources before optimizing.  The
present certificate keeps all three constraints separate.

## 2. Fractional dual for fixed Q

For nonnegative rational multipliers `alpha,beta,gamma`, every fractional
selection satisfies

```text
sum x_n/n
 <= alpha*(B-O*Q)+beta*(3*Q)+gamma*(2*B)
    + sum_n max(0,1/n-alpha*l(n)-beta*h(n)-gamma*F(n)).   (5)
```

There are `5824` retained items.  The verifier constructs two exact rational
triples of multipliers by solving three equality equations at selected boundary
items.

### Certificate A

Boundary targets:

```text
821125,
92383,
14771.
```

Its coefficient of `Q` in (5) is strictly positive.  Therefore its upper bound
is increasing in `Q` and covers every integer

```text
0<=Q<=6152
```

by evaluation at `Q=6152`.  The exact value there is approximately

```text
0.08522632265683308.
```

### Certificate B

Boundary targets:

```text
108397,
14771,
21779.
```

Its coefficient of `Q` is strictly negative.  Therefore its upper bound is
decreasing in `Q` and covers every integer

```text
6153<=Q<=6257
```

by evaluation at `Q=6153`.  The exact value there is approximately

```text
0.08522658245832886.
```

The two ranges cover every possible integer `Q`.  Consequently

```text
sum_(n_i<=1000000) 1/n_i
 < 0.085226583.                                    (6)
```

This is a strict improvement over the previous signed-label value
`0.085226905`.

## 3. Updated split-range consequence

The independently retained signed-label middle-range bound is

```text
sum_(1000000<n_i<=60000000) 1/n_i
 < 0.001185304.
```

Granting the two disjoint value ranges separate full budgets is safe, so (6)
gives

```text
sum_(n_i<=60000000) 1/n_i
 < 0.086411887.                                    (7)
```

The exact cycle interval requires a total greater than
`0.099934206877...`.  Therefore at least

```text
811340
```

distinct cycle values exceed sixty million.  Since at most `6257` positions
have positive full-order layer, at least

```text
811340-6257 = 805083
```

of them are zero-layer targets.

## 4. Scope

The gain is numerically modest, but it is structurally useful: the integrality
and exact allocation of the layer budget contain information lost by the single
combined cost.  The certificate covers all possible `Q` with two exact rational
duals and does not assume a probabilistic distribution.

Run

```text
python tools/verify_integral_layer_budget_dual.py
```

for the exact certificate.
