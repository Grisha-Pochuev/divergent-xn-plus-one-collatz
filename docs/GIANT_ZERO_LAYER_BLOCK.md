# Giant zero-layer block in either remaining cycle

Fix either remaining sparse-window length

```text
p = 177780727155637125193
```

or

```text
p = 177780727155637125195.
```

For every incoming valuation write

```text
a_i=s_(i+1)+O*q_i,
O=ord_X(2)=1860810887857924950,
1<=s_i<=O,
q_i>=0.
```

The full-label occupancy identity gives

```text
sum_i q_i<=6257.
```

## 1. Number of positive-layer positions

Let

```text
k=#{i:q_i>=1}.
```

Every positive `q_i` contributes at least one to the sum, so

```text
k<=6257.                                         (1)
```

If `k=0`, the entire cycle consists of least-layer steps.

Assume `k>=1`.  The `k` positive-layer positions divide the cyclic sequence
into `k` intervening blocks of zero-layer positions.  Their total length is
`p-k`.  Therefore one block has length at least

```text
ceil((p-k)/k).
```

The right-hand side is minimized over `1<=k<=6257` at `k=6257`.  For both
remaining values of `p`, exact integer arithmetic gives

```text
ceil((p-6257)/6257)
 = 28413093679980362.                             (2)
```

## 2. Rigorous conclusion

Every hypothetical cycle at either remaining length satisfies one of the two
alternatives:

1. every step has `q_i=0`; or
2. the cycle contains at least

```text
28413093679980362
```

consecutive steps with `q_i=0`.

On such a block every exact valuation is its least full output label:

```text
a_i=s_(i+1),
1<=a_i<=O.
```

## 3. Significance

This theorem turns the residual Priority 1 problem into a long-block problem.
Any final obstruction may focus on least-layer inverse dynamics over a block of
more than `2.84*10^16` consecutive steps.  Local forbidden-word enumeration is
still unavailable: arbitrary fixed finite words are realizable.  What is
needed is a quantitative potential, discrepancy bound, or height inequality
whose effect grows with the block length.

Run

```text
python tools/verify_giant_zero_layer_block.py
```

for the exact arithmetic certificate.
