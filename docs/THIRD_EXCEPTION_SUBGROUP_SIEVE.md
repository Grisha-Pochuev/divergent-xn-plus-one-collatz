# Third-exception subgroup sieve

This note eliminates the sparse-window length

```text
p = 177780727155637125191.
```

It extends the exact index-eight subgroup sieve while keeping the same proof structure.

## 1. Cutoff and subgroup membership

Use

```text
P = 6911089648497401,
ord_P(2) = (P-1)/8,
C = 60000000.
```

Among the `2154` allowed progressions modulo `2*15099`, there are exactly

```text
4279760
```

positive candidates at most `C`. Testing

```text
n^((P-1)/8) == 1 (mod P)
```

leaves exactly

```text
536735
```

genuine full output representatives.

Their reciprocal sum is accumulated with upward dyadic rounding.

## 2. Remaining active full classes

The fixed total valuation and the mandatory cost of the remaining cycle steps give

```text
number of active full classes <= 152608241119.
```

After taking all genuine representatives below the cutoff, the remaining active representatives are safely replaced by the smallest members above `C` in the larger union of the `2154` progressions. The exact threshold is

```text
2139543499307.
```

Repeated elements in one full class are again spaced by `2X`.

## 3. Exact reciprocal comparison

The complete exact envelope gives

```text
sum_i 1/n_i < 0.913331.
```

For the target length, exact rational logarithm bounds give the required threshold

```text
X*Lambda > 0.913636406.
```

Thus

```text
Lambda = sum_i log(1+1/(X*n_i))
       <= (1/X)*sum_i 1/n_i
```

is impossible.

## 4. Updated frontier

The contiguous cycle barrier rises to

```text
177780727155637125192.
```

Up to the sparse cap

```text
355561454311274250377
```

only two lengths remain:

```text
177780727155637125193
177780727155637125195
```

Run

```text
python tools/verify_third_exception_subgroup_sieve.py
```

for the exact certificate. The scan is a deterministic membership verification of `4279760` small modular candidates, not a trajectory search.