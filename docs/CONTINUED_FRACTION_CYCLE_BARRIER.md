# RETRACTED: continued-fraction cycle barrier

The former claim in this file that all nontrivial positive cycles of length at most `10^37` are excluded is **retracted**.

The proof used the assertion

```text
2^A == 1 (mod X)
```

for a cycle with total halving count `A`. This is false.

For a cycle

```text
2^(a_i) n_(i+1) = X n_i + 1,
```

multiplication gives, with `P=product_i n_i`,

```text
2^A P = product_i (X n_i+1).
```

Therefore the correct congruence is

```text
2^A P == 1 (mod X),
```

not `2^A==1 (mod X)`.

The accelerated `5n+1` cycle

```text
13 -> 33 -> 83 -> 13
```

is an immediate counterexample to the discarded assertion: its valuations are `(1,1,5)`, hence `A=7`, while

```text
2^7 == 3 (mod 5).
```

The continued-fraction reduction `A=ord_X(2)*q` consequently has no valid basis. Increasing precision or checking more convergents cannot repair this logical gap.

See `docs/AUDIT_INVALID_ORDER_CONDITION.md` for the full audit.

The earlier direct finite barrier

```text
148557456445856651509
```

from `ULTRA_STRONG_CANDIDATE.md` does not use this invalid congruence and remains the strongest fixed barrier retained by the project.
