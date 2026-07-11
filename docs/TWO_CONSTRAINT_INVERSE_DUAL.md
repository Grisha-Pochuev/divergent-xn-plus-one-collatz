# Two-constraint inverse-window reciprocal dual

This note combines two independent exact budgets for selected cycle values
below one million at the harder remaining length

```text
p = 177780727155637125195.
```

Put

```text
B=A-p=11644637628694231700273.
```

## 1. The two valid item costs

For a target `n` with full label `s`, let `h_3(n)` be the minimum total
full-order layer in an admissible three-edge inverse window.  The retained
depth-three cost is

```text
C_3(n)=3*(s-1)+O*h_3(n),
sum C_3(n_i)<=3*B.                                (1)
```

Let `u` be the source label of the least-layer admissible full predecessor and
`d_X(n)` its layer.  The symmetric one-edge cost is

```text
C_E(n)=u-1+s-1+2*O*d_X(n),
sum C_E(n_i)<=2*B.                                (2)
```

Neither constraint implies the other.

## 2. Exact combined dual

Take the rational normalized weight

```text
theta=23/25
```

on (1), and `2/25` on (2).  Clearing denominators gives the valid combined
item cost and budget

```text
C(n)=46*C_3(n)+6*C_E(n),
sum C(n_i)<=150*B.                                (3)
```

Apply the exact fractional-selection dual to all `5824` permanent-sieve
survivors below one million.  The boundary occurs after `203` complete items.
The boundary target is

```text
n=18439,
full label=1588577149097258286,
h_3=140,
C_3=265279255747401267855,
C_E=259745073615874626969,
C=13761316206075706083144.
```

The resulting exact rational bound is

```text
sum_(cycle values n<=1000000) 1/n
 < 0.085239095.                                   (4)
```

This strictly improves the former depth-three value

```text
0.085243521.
```

## 3. Consequence for the large tail

The exact cycle interval requires

```text
sum_i 1/n_i > 0.099934206877...
```

so (4) leaves a residual greater than

```text
0.014695112.
```

Every distinct value above one million contributes less than `10^(-6)`.
Therefore at least

```text
14696
```

distinct cycle values above one million are necessary.  The previous
single-constraint depth-three certificate required `14691`.

## 4. Significance

The gain is numerically small, but it proves that source/target edge costs add
information not captured by deeper layer charging alone.  Future work should
use genuinely independent dual multipliers; replacing the two budgets by a
single naive average can miss the improvement.

Run

```text
python tools/verify_two_constraint_inverse_dual.py
```

for the exact certificate.
