# Latest valid progress

The former `10^37` claim remains retracted. All current results preserve the correct cycle identity.

For

```text
X  = 104350542602662257699,
n0 = 1,
```

the current contiguous cycle barrier is

```text
177780727155637125192.
```

More strongly, every length through

```text
355561454311274250377
```

is impossible except

```text
177780727155637125193
177780727155637125195.
```

## Progress in this Priority 1 attack

The first sparse-window theorem originally left seven isolated odd lengths. They were reduced as follows:

1. midpoint harmonic and large-divisor split: removed `...183`;
2. full-modulus activation cost: removed `...185`;
3. index-eight subgroup sieve below `10^6`: removed `...187` and `...189`;
4. subgroup sieve below `6*10^7`: removed `...191`.

Only two remain.

Key new exact facts:

```text
ord_X(2)=1860810887857924950,
ord_P(2)=(P-1)/8,
A >= p + m*(m-1)/2
```

for `m` active full output classes.

Primary latest files:

```text
docs/FULL_MODULUS_ACTIVATION_BOUND.md
tools/verify_full_modulus_activation_bound.py
docs/INDEX_EIGHT_SMALL_REPRESENTATIVE_SIEVE.md
tools/verify_index_eight_small_sieve.py
docs/THIRD_EXCEPTION_SUBGROUP_SIEVE.md
tools/verify_third_exception_subgroup_sieve.py
```

No Collatz trajectory scan was used. The largest recent certificate performs about `4.28` million subgroup-membership checks on small modular candidates.

The strict prize problem remains open. The next step is an exact activation-price or global neighbour-height certificate for the two displayed lengths.