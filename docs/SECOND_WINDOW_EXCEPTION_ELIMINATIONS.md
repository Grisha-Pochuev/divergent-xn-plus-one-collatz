# Elimination of five second-window exceptions

The second sparse-window theorem introduced seven possible even lengths near the first even power-of-two crossing. This note eliminates the first five:

```text
355561454311274250378
355561454311274250380
355561454311274250382
355561454311274250384
355561454311274250386.
```

## 1. Exact total valuation

For each target `p=2r`, the crossing certificate proves

```text
X^p < 2^(133r+1)
```

and the standard reciprocal correction is too small to reach the following power. Therefore a hypothetical cycle would have the exact total valuation

```text
A = 133r+1.
```

If `m` full output classes modulo `2X` are active, their distinct minimum activation labels and the remaining `p-m` positive valuations imply

```text
A >= p + m*(m-1)/2.
```

For all five targets,

```text
m <= 215820644320.
```

## 2. Index-eight subgroup sieve

Use

```text
P=6911089648497401,
ord_P(2)=(P-1)/8.
```

A candidate in one of the `2154` allowed progressions represents a genuine full output class only when

```text
n^((P-1)/8) == 1 (mod P).
```

### First four targets

The exact sieve below

```text
C=1000000
```

contains `71318` candidates and `8727` genuine full representatives. Combining them with the full-class activation cap and a safe harmonic envelope above the cutoff gives

```text
sum_i 1/n_i < 1.194457.
```

The exact required thresholds for the first four targets decrease from approximately `2.640975` to `1.420422`, all strictly above this bound.

### Fifth target

For

```text
p=355561454311274250386,
```

the larger already-retained cutoff

```text
C=60000000
```

contains `4279760` candidates and `536735` genuine representatives. The resulting exact reciprocal bound is

```text
sum_i 1/n_i < 0.938051,
```

while the required threshold is approximately

```text
1.013571.
```

Thus this target is also impossible.

## 3. Updated second sparse window

Every cycle length through

```text
533342181466911375570
```

is now impossible except the four values

```text
177780727155637125193
177780727155637125195
355561454311274250388
355561454311274250390.
```

Run

```text
python tools/verify_second_window_exception_eliminations.py
```

for the exact certificate. The checker performs one deterministic subgroup scan through `60000000` and reuses it for all five targets; it is not a trajectory search.