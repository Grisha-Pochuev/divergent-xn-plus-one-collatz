# RETRACTED: continued-fraction method ceiling

This file previously analyzed the numerical ceiling of a claimed continued-fraction cycle barrier.

That analysis is no longer mathematically relevant because the underlying reduction assumed the false cycle congruence

```text
2^A == 1 (mod X).
```

The correct congruence is

```text
2^A * product_i(n_i) == 1 (mod X).
```

Therefore one cannot conclude that `ord_X(2)` divides `A`, and the rational approximation variable used in the former argument was not justified.

See

```text
docs/AUDIT_INVALID_ORDER_CONDITION.md
```

for the explicit counterexample and correction.

No cycle-length theorem should be inferred from the continued-fraction computations formerly recorded here.
