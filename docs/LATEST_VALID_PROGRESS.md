# Latest valid progress

The former `10^37` claim remains retracted. All results below preserve the correct cycle identity.

For

```text
X  = 104350542602662257699,
n0 = 1,
```

the orbit cannot return to `1`.

## New Priority 1 frontier

The current contiguous cycle barrier is

```text
177780727155637125184.
```

More strongly, every length up to

```text
355561454311274250377
```

is impossible except six odd values:

```text
177780727155637125185
177780727155637125187
177780727155637125189
177780727155637125191
177780727155637125193
177780727155637125195
```

The previous retained barrier was

```text
176022359338834903228.
```

Thus the contiguous barrier increased by about `0.999%`. The sparse-window theorem covers roughly twice that range, leaving only six isolated lengths.

## What produced the improvement

1. The bare `2154`-class graph, and even every finite exact-valuation augmentation of it, has no forbidden compatible finite words.
2. Global occupancy and valuation-cost constraints yield a rational dual reciprocal bound.
3. The large divisor `6911089648497401` separates low exact valuations into very sparse output progressions.
4. Sharp rational logarithm bounds expose the first near-power-of-two crossing and the large safe interval after it.
5. A midpoint harmonic estimate with `K=5000000` eliminates the first of the original seven exceptional odd lengths.
6. Two exact global transition-balance identities are now available for attacking the remaining six.

Primary files:

```text
docs/BALANCED_OCCUPANCY_DUAL_BOUND.md
tools/verify_balanced_occupancy_barrier.py
docs/AUGMENTED_TRANSITION_NO_GO.md
tools/verify_augmented_transition_no_go.py
docs/LARGE_DIVISOR_VALUATION_SPLIT.md
tools/verify_large_divisor_split_barrier.py
docs/SHARP_LOG_INTERVAL_BARRIER.md
tools/verify_sharp_log_barrier.py
docs/FIRST_SPARSE_CYCLE_WINDOW.md
tools/verify_first_sparse_cycle_window.py
docs/FIRST_EXCEPTION_ELIMINATION.md
tools/verify_first_exception_elimination.py
docs/GLOBAL_TRANSITION_BALANCE_IDENTITIES.md
tools/verify_global_transition_identities.py
```

No long trajectory computation was used. The longest new deterministic certificate enumerates five million inverse powers modulo one divisor of `X`; it is a short linear modular check rather than an orbit or parameter search.

The strict prize problem remains open. The exact next task is to eliminate the six listed lengths using their fixed total valuation and the global transition-balance identities.