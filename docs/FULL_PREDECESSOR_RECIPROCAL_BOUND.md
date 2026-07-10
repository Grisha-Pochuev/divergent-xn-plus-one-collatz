# Full-predecessor reciprocal bound

This note applies the full-modulus predecessor delay and the exact full-label
occupancy budget to the hardest remaining sparse-window length

```text
p = 177780727155637125195.
```

The fixed total valuation and incremental budget are

```text
A = 11822418355849868825468,
B = A-p = 11644637628694231700273.
```

## 1. Correct incremental cost

For a possible cycle value `n`, let

```text
s(n) = least full output label,
d_X(n) = full-modulus predecessor delay.
```

Every occurrence spends at least

```text
s(n)+O*d_X(n)
```

units of total valuation, where `O=ord_X(2)`.  The other `p-1` cycle positions
still spend at least one unit each.  Thus the correct item cost above the
universal baseline is

```text
c(n)=s(n)-1+O*d_X(n),
sum_(selected n) c(n) <= B.                       (1)
```

For every rational `lambda>0`, distinctness and (1) give the exact fractional
dual

```text
sum_(selected n) 1/n
 <= lambda*B + sum_n max(0,1/n-lambda*c(n)).       (2)
```

## 2. Complete bound below one million

The exact modular list contains `8727` genuine full representatives.  The
permanent predecessor sieve removes `2903`, leaving `5824` values with exact
full delays between `0` and `347`.

Sorting by `1/(n*c(n))`, the fractional boundary occurs after `564` complete
items.  The boundary item is

```text
n = 33223,
s = 549750138304358466,
d_X = 25,
c = 47070022334752482215.
```

Using `lambda=1/(n*c)` in (2) gives, by exact rational arithmetic,

```text
sum_(cycle elements n<=1000000) 1/n
 < 0.087551912.                                    (3)
```

The exact logarithmic requirement is greater than `0.099934206`, so every
hypothetical cycle of this length must have

```text
sum_(n_i>1000000) 1/n_i > 0.012382.               (4)
```

In particular at least `12383` distinct values above one million are needed.

## 3. Complete bound through sixty million

The retained finite modular pass through `60000000` contains

```text
4279760 allowed-progression candidates,
536735 genuine full representatives,
358103 permanent-sieve survivors.
```

Their exact full predecessor delays range from `0` through `558`; only `9462`
have delay zero.  The sum of all listed delays is `12752005`.

With the same exact dual, the fractional boundary occurs after `1115` complete
items.  The boundary item is

```text
n = 14165,
s = 1859575580472366337,
d_X = 58,
c = 109786607076232013436.
```

The resulting bound is

```text
sum_(cycle elements n<=60000000) 1/n
 < 0.087618737.                                    (5)
```

Consequently

```text
sum_(n_i>60000000) 1/n_i > 0.012315.              (6)
```

The exact residual forces at least

```text
738929
```

distinct values above sixty million whose reciprocal contribution is needed.

## 4. Meaning

The hardest remaining length can no longer obtain its correction from a small
collection of cheap tiny values.  The full predecessor condition leaves a
large, quantitatively necessary tail.  This is still not a contradiction:
large values in zero-delay full classes might in principle supply that tail.
The next target is therefore a transition-circulation bound on the zero-delay
tail, rather than a larger unstructured cutoff scan.

Run

```text
python tools/verify_full_predecessor_reciprocal_bound.py
```

for the exact deterministic certificate.  The sixty-million pass reuses the
same finite modular range as the retained subgroup sieve and is not a trajectory
search.
