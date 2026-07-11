# Coupled-Q split-range reciprocal dual

This note improves the common reciprocal bound through sixty million by using
the same integer full-layer total

```text
Q=sum_i q_i
```

in both value ranges.  Previous split-range bounds safely granted each range an
independent worst-case budget.  The present argument couples them through the
actual common `Q`.

Fix

```text
0<=Q<=6257.
```

## 1. Small-range piecewise certificate

The integral-layer certificate below one million gives two exact affine upper
bounds.

- For `0<=Q<=6152`, the left certificate is increasing in `Q`.
- For `6153<=Q<=6257`, the right certificate is decreasing in `Q`.

At the useful transition point,

```text
U_small(5841) < 0.084967191.
```

## 2. Middle-range piecewise certificate

For

```text
1000000<n<=60000000,
```

the global signed-label potential gives the `Q`-independent exact bound

```text
U_middle < 0.001185304.                            (1)
```

A second valid dual keeps the target-label budget separate from the signed
potential.  It uses the two boundary targets

```text
1250453,
1454471.
```

Its exact rational multipliers are nonnegative.  The coefficient of `Q` is
strictly negative, so this bound decreases with `Q`.  At `Q=6153`, it is
approximately

```text
0.000595182928732590.
```

The decreasing bound crosses the constant bound (1) between the integers

```text
Q=5841 and Q=5842.
```

Thus:

- for `Q<=5841`, use the constant middle-range certificate;
- for `Q>=5842`, use the decreasing two-resource certificate.

## 3. Global maximum over all Q

For `Q<=5841`, the small bound increases and the middle bound is constant, so
the maximum is at `Q=5841`.

For `5842<=Q<=6152`, the increase of the small left certificate is smaller than
the decrease of the middle certificate, so their sum decreases.

For `Q>=6153`, both selected certificates decrease.

Exact rational evaluation of all `6258` integer values confirms that the global
maximum occurs at

```text
Q=5841.
```

The resulting uniform bound is

```text
sum_(n_i<=60000000) 1/n_i
 < 0.086152495.                                    (2)
```

This strictly improves the previous common upper bound `0.086411887`.

## 4. Updated mandatory tails

Using the exact logarithmic thresholds, (2) forces:

```text
p=177780727155637125193:
  values above 60000000 >=25237969,
  zero-layer values there >=25231712;

p=177780727155637125195:
  values above 60000000 >=826903,
  zero-layer values there >=820646.
```

Relative to the previous coupled-independent-range result, this adds

```text
15563
```

mandatory zero-layer targets at each remaining length.

## 5. Verification

Run

```text
python tools/verify_coupled_q_split_range_dual.py
```

The integration verifier executes the two exact component certificates,
captures their exact rational objectives, constructs the second middle-range
dual, and checks all integer values `Q=0,...,6257`.
