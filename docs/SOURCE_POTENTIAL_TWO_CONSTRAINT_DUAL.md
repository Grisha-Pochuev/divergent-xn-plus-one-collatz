# Source-potential two-constraint inverse dual

This note gives a valid circulation improvement for the harder remaining
length

```text
p = 177780727155637125195.
```

It replaces the retracted endpoint-completion argument by a genuine
telescoping potential.

Put

```text
B=A-p=11644637628694231700273,
O=ord_X(2)=1860810887857924950.
```

## 1. Potential-shifted edge cost

For an actual cycle edge with source full label `u`, target label `s`, and full
layer `q`, the symmetric incremental cost is

```text
C_E=(u-1)+(s-1)+2*O*q.
```

Add the telescoping potential

```text
s-u.
```

Summing it around a cycle gives zero, so the shifted cost

```text
C_U=C_E-(s-u)=2*(u-1)+2*O*q                     (1)
```

satisfies exactly

```text
sum_i C_U(i)=2*B.                                (2)
```

For a fixed target, let `q_0` be its least admissible predecessor layer and
`u_0` the corresponding source label.  Any higher admissible layer `q>=q_0+1`
adds at least `2O`, while the source term `2(u-1)` can decrease by less than
`2O`.  Therefore

```text
2*(u_0-1)+2*O*q_0
```

is a valid lower bound for every actual edge entering that target.  Unlike the
retracted argument, this does not identify `u_0` with the actual endpoint; it
uses only the scalar minimum of the potential-shifted cost.

## 2. Independent depth-three cost

For every target `n<=1000000`, let `h_3(n)` be the least total full-layer sum
in an admissible three-edge inverse window.  The retained valid cost is

```text
C_3(n)=3*(s(n)-1)+O*h_3(n),
sum_i C_3(n_i)<=3*B.                              (3)
```

## 3. Exact combined dual

Use weight `23/25` on the normalized depth-three constraint and `2/25` on the
normalized source-potential constraint.  Clearing denominators gives

```text
C(n)=46*C_3(n)+6*C_U(n),
sum_i C(n_i)<=150*B.                              (4)
```

Over the `5824` permanent-sieve survivors below one million, the exact
fractional-selection boundary occurs after `203` complete items.  The boundary
item is

```text
n = 17669,
target label = 618223181506832115,
h_3 = 157,
C_3 = 294001978938214713492,
least layer = 37,
least-layer source label = 1114349115318026335,
C(n) = 14363663254750611814440.
```

The resulting rational bound is

```text
sum_(cycle values n<=1000000) 1/n
 < 0.085238902.                                   (5)
```

This strictly improves the previous valid two-constraint value
`0.085239095`.

## 4. Consequence

The exact interval requires total reciprocal mass greater than
`0.099934206877...`, so (5) leaves more than `0.014695304` for values above one
million.  Distinctness still forces at least

```text
14696
```

such values.  The integer count does not yet increase, but the potential shift
is a rigorously validated circulation ingredient.

## 5. Significance

The earlier invalid flow charge tried to treat the least-cost source label as
the actual source endpoint.  The present argument avoids that mistake: the
source label appears only inside a telescoping potential, and the minimum over
all admissible layers is proved to occur at the least layer.

More general potentials on full labels may strengthen this route further, but
they must be evaluated on every admissible layer choice.

Run

```text
python tools/verify_source_potential_two_constraint_dual.py
```

for the exact certificate.
