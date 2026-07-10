# Second sparse cycle window

For the fixed multiplier

```text
X = 104350542602662257699
```

put

```text
eta = log(X^2/2^133)>0.
```

The first sparse-window theorem crossed the first odd near-power-of-two event. This note crosses the following even event and extends the exact sparse obstruction to

```text
CAP = 533342181466911375570.
```

## 1. Uniform reciprocal correction

Evaluate the retained large-divisor reciprocal certificate at `CAP`. It gives one exact rational upper bound `R(CAP)` valid for every cycle length at most `CAP`:

```text
sum_i 1/n_i <= R(CAP),
R(CAP) approximately 2.853671.
```

Thus

```text
Lambda = A*log(2)-p*log(X) <= R(CAP)/X.
```

All phase comparisons use finite rational atanh-series bounds with rigorous tails.

## 2. The even crossing

For even `p=2r`,

```text
p*log(X)=133r*log(2)+r*eta.
```

The first even crossing occurs strictly between

```text
355561454311274250390
```

and

```text
355561454311274250392.
```

The only even lengths not excluded in the small pre-crossing window are

```text
355561454311274250378
355561454311274250380
355561454311274250382
355561454311274250384
355561454311274250386
355561454311274250388
355561454311274250390.
```

After the crossing, the gap to the following power of two is

```text
2*log(2)-p*eta/2.
```

It decreases with `p`, but its exact lower bound at `CAP` still exceeds `R(CAP)/X`. Therefore every even length from `355561454311274250392` through `CAP` is impossible.

## 3. Odd lengths between the crossings

After the first odd crossing and before the next one, the odd-length gap is

```text
[3*log(2)-p*eta]/2.
```

This also decreases with `p`. At the largest odd value below `CAP`, its exact lower bound still exceeds the uniform correction. Hence there are no new odd exceptions below `CAP`.

The next odd exceptional window starts only after the displayed cap.

## 4. Combined conclusion

Using the already retained elimination of five of the original seven odd exceptions, every nontrivial positive cycle length through

```text
533342181466911375570
```

is impossible except:

```text
177780727155637125193
177780727155637125195
355561454311274250378
355561454311274250380
355561454311274250382
355561454311274250384
355561454311274250386
355561454311274250388
355561454311274250390.
```

Thus an additional interval of about `1.78*10^20` lengths is reduced to seven new isolated even candidates.

Run

```text
python tools/verify_second_sparse_cycle_window.py
```

for the exact certificate. This remains a sparse finite obstruction, not a proof of divergence.