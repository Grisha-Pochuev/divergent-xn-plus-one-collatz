# Full-modulus activation bound

This note eliminates the next sparse-window exceptional length

```text
p = 177780727155637125185.
```

The argument uses the complete multiplicative order of `2` modulo the fixed multiplier, not only the `2154` classes modulo `15099`.

## 1. Full output classes

For

```text
X = 104350542602662257699
```

the exact checker proves

```text
O = ord_X(2) = 1860810887857924950.
```

If a cycle step has exact valuation `a`, its output satisfies

```text
2^a*n' == 1 (mod X).
```

Thus `a modulo O` determines one odd output residue class modulo `2X`.
Distinct labels in `{1,...,O}` determine distinct full output classes.

## 2. Activation cost

Suppose a hypothetical cycle uses `m` different full output classes. For each active class, choose the least positive valuation label `s` in `{1,...,O}` producing it.

The `m` labels are distinct, and at least one cycle step is needed to activate each class. Therefore the total valuation `A` satisfies

```text
A >= sum(active s) >= 1+2+...+m = m*(m+1)/2.       (1)
```

For the target length, the power-of-two interval fixes

```text
A = 133*(p-1)/2 + 67
  = 11822418355849868824803.
```

Hence (1) gives

```text
m <= 153768776777.
```

This is a global closure restriction: a cycle may contain about `1.78*10^20` elements, but it can activate at most about `1.54*10^11` different full residue classes.

## 3. First representatives of active classes

Every full output class reduces modulo

```text
2M = 30198,
M = 15099,
```

to one of the `2154` allowed classes. The first admissible representatives of the active full classes are distinct positive integers in the union of these `2154` arithmetic progressions. The literal value `1` is excluded because the fixed orbit cannot return to `1`.

To maximize the reciprocal sum, it is safe to replace the unknown active representatives by the `m` smallest integers in this larger union.

An exact counting threshold gives

```text
T = 2155761151909,
```

and exactly `m` allowed integers are at most `T`.

Summing the `2154` harmonic progression envelopes with exact rational logarithm upper bounds yields

```text
sum(first representatives)^(-1)
 < 1.906957437.
```

## 4. Repetitions inside a full class

Distinct elements in one full output class differ by multiples of `2X`. Even allowing every active class as many as `p` elements gives the safe total tail bound

```text
< 0.000000067.
```

Therefore every hypothetical cycle of the target length satisfies

```text
sum_i 1/n_i < 1.906957504.                         (2)
```

## 5. Contradiction with the exact interval gap

For this odd target length the exact cycle product forces the total valuation displayed above. The logarithmic gap to the required power of two is

```text
Lambda = [log(2)-p*log(X^2/2^133)]/2.
```

Exact atanh-series bounds prove

```text
X*Lambda > 2.134189706.
```

But the cycle identity gives

```text
Lambda
 = sum_i log(1+1/(X*n_i))
 <= (1/X)*sum_i 1/n_i
 < 1.906957504/X,
```

contradicting the lower bound.

Thus the target length is impossible.

## 6. Updated frontier

The contiguous cycle barrier rises to

```text
177780727155637125186.
```

Up to the sparse cap

```text
355561454311274250377
```

the only lengths not yet excluded are now

```text
177780727155637125187
177780727155637125189
177780727155637125191
177780727155637125193
177780727155637125195
```

Run

```text
python tools/verify_full_modulus_activation_bound.py
```

for the exact certificate.