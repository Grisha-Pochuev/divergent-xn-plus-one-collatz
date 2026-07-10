# Necessary mass of expensive targets below X

This note combines the cheap-transition concentration theorem with the exact
permanent predecessor sieve below one million.

Use

```text
X = 104350542602662257699,
K = 5000,
Hcheap = 781563824454394220933608138645145.
```

For either remaining cycle length, at most

```text
E = 4657855051477692680
```

edges are expensive.  Every cheap target is at least `Hcheap`.

## 1. Baseline decomposition at X

The cheap targets contribute at most

```text
(p-E)/Hcheap.
```

For every expensive target `n`,

```text
1/n <= 1/X                       if n>=X,
1/n = 1/X+(1/n-1/X)              if n<X.
```

Therefore

```text
sum_i 1/n_i
 <= (p-E)/Hcheap + E/X
    + sum_(expensive n_i<X) (1/n_i-1/X).          (1)
```

The exact logarithmic lower bounds for the two remaining lengths force the
last sum in (1) to exceed

```text
0.462148691   for p=177780727155637125193,
0.055297591   for p=177780727155637125195.         (2)
```

Thus small expensive targets are mandatory; a cycle cannot place all of its
reciprocal correction in values at least `X`.

## 2. The harder length needs at least five targets below X

The first permanent-sieve survivors are

```text
25, 163, 169, 499, 529, ...
```

The maximum excess obtainable from any four distinct admissible targets below
`X` is bounded by the four smallest:

```text
sum_(n in {25,163,169,499}) (1/n-1/X)
 < 0.054057.
```

This is below the second threshold in (2).  Hence a hypothetical cycle of
length

```text
177780727155637125195
```

contains at least five distinct expensive targets below `X`.

## 3. The first length needs a large population above one million

The exact permanent/full-predecessor enumeration gives `5824` admissible
targets at most one million.  Even if every one were used, their total excess
above the `1/X` baseline is less than

```text
0.106462.
```

For

```text
p=177780727155637125193,
```

the remaining required excess is greater than

```text
0.355686812.
```

Every additional target in `(1000000,X)` contributes less than

```text
1/1000000-1/X.
```

Consequently at least

```text
355687
```

distinct expensive targets must lie strictly between one million and `X`.

## 4. Significance

The two remaining lengths now have different local obligations:

- `...195` needs at least five distinct expensive targets below `X`;
- `...193` needs a macroscopic set of at least `355687` expensive targets above
  one million but below `X`, even after using every admissible smaller target.

This narrows the next attack to the exact predecessor costs and circulation of
small expensive values.  The result is necessary, not yet contradictory.

Run

```text
python tools/verify_expensive_small_target_mass.py
```

for the exact certificate.
