# Symmetric edge-cost reciprocal dual

Fix either remaining sparse-window length.  For every cycle edge
`n_(i-1) -> n_i`, write

```text
a_(i-1)=s_i+O*q_(i-1),
O=ord_X(2).
```

Let `s_(i-1)` be the full label of the predecessor.  Assign the exact symmetric
incremental edge cost

```text
c_i=(s_(i-1)-1)+(s_i-1)+2*O*q_(i-1).             (1)
```

## 1. Exact global budget

Every full label occurs once as a source label and once as a target label.
Therefore

```text
sum_i c_i=2*(A-p).                                (2)
```

For a possible target value `n`, let `d_X(n)` be its least full-predecessor
layer.  Because increasing the layer by one adds `2O`, while a full label lies
between `1` and `O`, the least feasible layer also minimizes (1).  If `u(n)` is
the full label of that least-layer predecessor and `s(n)` the target label, the
minimum edge cost is exactly

```text
c(n)=u(n)-1+s(n)-1+2*O*d_X(n).                    (3)
```

Thus for any selected set of distinct cycle values,

```text
sum c(n)<=2*(A-p).                                (4)
```

## 2. Exact certificate below one million

The retained modular enumeration gives

```text
8727 genuine full representatives,
2903 permanent predecessor rejections,
5824 surviving targets.
```

For every survivor the verifier computes `d_X(n)`, the corresponding full
predecessor, its label `u(n)`, and the exact cost (3).

Applying the rational fractional dual to (4), the boundary occurs after

```text
562
```

complete items.  The boundary item is

```text
n = 33223,
s(n) = 549750138304358466,
d_X(n) = 25,
u(n) = 111144508941716432,
c(n) = 93701439040142322396.
```

For either remaining length the resulting exact bound is

```text
sum_(cycle values n<=1000000) 1/n
 < 0.087543786.                                   (5)
```

The former one-sided full-predecessor cost gave `0.087551912`; (5) is a strict
improvement obtained solely from the source label and the second copy of the
full-order layer cost.

## 3. Meaning

Equation (2) is the correct edge-level budget for transition-circulation
arguments.  It avoids treating a target label independently of its predecessor.
The numerical improvement at depth one is small, so it does not eliminate the
last two lengths.  Its main role is to provide the correct cost functional for
longer inverse-window or circulation duals.

Run

```text
python tools/verify_symmetric_edge_cost_dual.py
```

for the exact certificate.
