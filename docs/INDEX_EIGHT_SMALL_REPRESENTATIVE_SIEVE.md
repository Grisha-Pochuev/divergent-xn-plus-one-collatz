# Index-eight small-representative sieve

This note eliminates two more sparse-window exceptional lengths:

```text
177780727155637125187
177780727155637125189
```

## 1. The subgroup modulo the large prime

Write

```text
X = M*P,
M = 15099,
P = 6911089648497401.
```

The exact checker proves that `P` is prime and

```text
ord_P(2) = (P-1)/8 = 863886206062175.
```

Thus the powers of `2 modulo P` form a subgroup of index `8`. An odd integer lying in one of the `2154` allowed classes modulo `2M` represents a full output class modulo `2X` exactly when its reduction modulo `P` lies in this subgroup.

Since

```text
gcd(ord_M(2),ord_P(2)) = 1,
```

the two subgroup conditions combine without further synchronization loss.

## 2. Exact sieve below one million

Set

```text
C = 1000000.
```

There are exactly

```text
71318
```

positive integers at most `C` in the `2154` allowed progressions modulo `2M`, with the forbidden literal value `1` removed.

The verifier tests the exact subgroup condition

```text
n^((P-1)/8) == 1 (mod P)
```

for these candidates. Exactly

```text
8727
```

are genuine full output representatives.

Their reciprocal sum is bounded above, term by term with a common dyadic denominator, by approximately

```text
0.128969418.
```

The former unsieved envelope allowed all `71318` candidates and therefore lost a large amount at the smallest, most important values.

## 3. Number of active full classes

For either target length, the power-of-two interval fixes the total valuation `A` exactly. If `m` full classes are active, activating their distinct valuation labels costs at least

```text
1+2+...+m.
```

The remaining `p-m` steps each cost at least one additional valuation unit. Hence

```text
A >= m*(m+1)/2 + (p-m)
  = p + m*(m-1)/2.
```

For both target lengths this gives

```text
m <= 152608241119.
```

After including all `8727` genuine small representatives, the remaining active representatives are safely replaced by the smallest allowed numbers above `C` in the union of the `2154` progressions. Exact counting gives the common upper threshold

```text
2139491901191.
```

## 4. Reciprocal certificate

The exact dyadic harmonic envelopes give, for both target lengths,

```text
sum_i 1/n_i < 1.169737.
```

This includes a deliberately generous tail allowing repeated elements in every active full class; repetitions in one full class are spaced by `2X`.

The exact logarithmic thresholds are approximately

```text
1.727338607   for p=177780727155637125187,
1.320487507   for p=177780727155637125189.
```

Both exceed the reciprocal bound. Therefore the cycle identity cannot hold at either length.

## 5. Updated frontier

The contiguous barrier rises to

```text
177780727155637125190.
```

Up to

```text
355561454311274250377
```

only three odd lengths remain unexcluded:

```text
177780727155637125191
177780727155637125193
177780727155637125195
```

Run

```text
python tools/verify_index_eight_small_sieve.py
```

for the exact certificate. The sieve contains only `71318` modular membership tests and is not a trajectory search.