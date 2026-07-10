# Audit: the claimed cycle order condition is invalid

A previous branch of this repository claimed that a positive cycle with total halving count `A` must satisfy

```text
2^A == 1 (mod X).
```

That claim is false.

## Correct reduction

For a cycle

```text
2^(a_i) n_(i+1) = X n_i + 1,
```

multiply all `p` equations. Since the cycle permutes the same elements, with

```text
P = product_i n_i,
A = sum_i a_i,
```

we obtain

```text
2^A P = product_i (X n_i + 1).
```

Reducing modulo `X` gives

```text
2^A P == 1 (mod X),
```

not

```text
2^A == 1 (mod X).
```

All cycle elements are coprime to `X`, so `P` is invertible modulo `X`, but there is no reason for `P` to be congruent to `1`.

## Elementary counterexample

For the accelerated `5n+1` cycle

```text
13 -> 33 -> 83 -> 13,
```

the exact valuations are

```text
(1,1,5),
```

so `A=7`. However,

```text
2^7 == 3 (mod 5),
```

not `1`. The product is

```text
P=13*33*83 == 2 (mod 5),
```

and the correct relation holds:

```text
2^7 * P == 3*2 == 1 (mod 5).
```

## Consequence

The continued-fraction barrier that set

```text
A = ord_X(2) * q
```

is not proved. Therefore the claimed exclusion of cycles through `10^37` is retracted.

The earlier ultra-strong finite barrier

```text
148557456445856651509
```

was obtained by a different direct power-of-two interval argument and does not use this invalid order condition. It remains the strongest fixed cycle-length barrier currently retained by the project, subject to its independent checks.

This audit is intentionally explicit: computational verification of a consequence cannot repair a false mathematical premise.
