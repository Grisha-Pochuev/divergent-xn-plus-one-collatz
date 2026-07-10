# Global transition balance identities

Let

```text
2^a_i*n_(i+1) = X*n_i+1
```

be a positive accelerated cycle, with indices taken modulo its length `p`.
Arbitrary finite valuation words are locally realizable, but a closed cycle must satisfy the following two exact global identities.

## 1. Incoming-valuation height balance

Summing all step equations gives

```text
sum_i 2^a_i*n_(i+1) = X*sum_i n_i + p.
```

Reindexing the first sum yields

```text
sum_i (2^a_(i-1)-X)*n_i = p.                 (H)
```

Thus the values reached after large-valuation steps and the values reached after small-valuation steps must cancel with exact residual `p`.

## 2. Outgoing-valuation reciprocal balance

Divide the `i`-th step equation by `n_i*n_(i+1)`:

```text
2^a_i/n_i - X/n_(i+1) = 1/(n_i*n_(i+1)).
```

Summing and cyclically reindexing the second term gives

```text
sum_i (2^a_i-X)/n_i
 = sum_i 1/(n_i*n_(i+1)) > 0.                (R)
```

This is a strict signed balance on the same reciprocal quantities used in the cycle barrier.

## 3. Immediate consequences for the fixed multiplier

For

```text
2^66 < X < 2^67,
```

identity `(R)` implies that some outgoing valuation satisfies

```text
a_i >= 67.
```

The cycle identity also gives `A<=67p-1`, so not every valuation can be at least `67`; hence some valuation satisfies

```text
a_j <= 66.
```

Every hypothetical cycle therefore contains both a growing transition and a shrinking transition.

More importantly, `(H)` and `(R)` couple a valuation spike to the actual neighbouring heights. They are not consequences of residue-class counts alone and survive the augmented finite-path no-go theorem.

## 4. Role in the six exceptional lengths

For each of the six remaining sparse-window lengths, the total valuation `A` is fixed exactly. The next attack should combine that fixed total with `(H)` or `(R)` and the large-divisor progression bounds. A contradiction would eliminate an exceptional length without enlarging the modular enumeration.

Run

```text
python tools/verify_global_transition_identities.py
```

for exact regression checks on known cycles and generated finite closed examples.