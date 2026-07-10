# Latest valid progress

The previously claimed `10^37` cycle barrier was retracted because it relied on the false condition `ord_X(2) | A` for a cycle. The current work proceeds only from retained valid statements.

For

```text
X  = 104350542602662257699,
n0 = 1,
```

the orbit cannot return to `1`.

A new residue-crowding argument uses:

- the `2154` possible odd output residue classes modulo `15099`;
- distinctness of elements in a nontrivial cycle;
- an exact logarithmic bound for the sum of reciprocals of all possible cycle elements;
- rational inequalities only.

It proves that every nontrivial positive cycle of accelerated length at most

```text
170000000000000000000
```

is impossible.

Therefore the fixed orbit from `1` either tends to positive infinity or enters a nontrivial cycle longer than that barrier.

This improves the previous retained valid barrier

```text
148557456445856651509
```

by about 14.4 percent.

The proof and exact lightweight verifier are in:

```text
docs/RESIDUE_CROWDING_CYCLE_BARRIER.md
tools/verify_residue_crowding_barrier.py
```

No long trajectory computation or heavy CPU search is used.

The strict prize problem remains open: cycles longer than the new finite barrier have not yet been excluded.
