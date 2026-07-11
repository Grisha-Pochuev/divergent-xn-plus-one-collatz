# Deep inverse sieve for all-zero-layer cycle minima

This note strengthens both all-zero-layer branches by following the unique
least-layer predecessor chain for up to four generations.

For exact outgoing valuation `a`, a possible minimum satisfies

```text
m == (2^a-1)*X^(-1) (mod 2^(a+1)).
```

The verifier first combines this class by CRT with the `2154` allowed classes
modulo `M=15099`, then tests the exact subgroup condition modulo
`P=6911089648497401`.  For every full target it repeatedly forms the unique
`q=0` predecessor modulo the required increasing power of `X`.  Every value in
an all-zero-layer cycle must survive every predecessor generation.

## 1. First remaining length

Use the retained minimum bound

```text
m <= 5106101578294348744.
```

For outgoing valuations `a=38,...,49`, the exact counts are listed as

```text
(a, small-class candidates, full targets,
     survive 1 predecessor, survive 2, survive 3, survive 4)

38: 1325003, 165762, 2910, 58, 0, 0
39:  662514,  83254, 1553, 32, 1, 0
40:  331257,  41211,  750, 14, 0, 0
41:  165610,  20705,  392,  7, 0, 0
42:   82809,  10390,  179,  2, 0, 0
43:   41388,   5396,   96,  2, 0, 0
44:   20705,   2580,   48,  1, 0, 0
45:   10354,   1251,   20,  0, 0, 0
46:    5182,    680,   15,  0, 0, 0
47:    2590,    312,   10,  0, 0, 0
48:    1302,    160,    6,  1, 0, 0
49:     654,     75,    1,  0, 0, 0
```

No candidate survives four generations.  Together with the earlier exclusion
of `a=50,...,66`, every all-zero-layer cycle of length

```text
177780727155637125193
```

satisfies

```text
a_out <= 37,
n_next > X*m/2^37 > 759250124*m.                 (1)
```

## 2. Second remaining length

Use

```text
m <= 25894009212734490968.
```

For `a=40,...,51` the exact counts are

```text
40: 1679845, 210393, 3735, 70, 0, 0
41:  839908, 105252, 1901, 28, 0, 0
42:  419959,  52518,  869, 16, 0, 0
43:  209966,  26716,  436,  8, 1, 0
44:  104989,  13104,  237,  5, 0, 0
45:   52510,   6524,  101,  2, 0, 0
46:   26235,   3349,   66,  0, 0, 0
47:   13141,   1644,   34,  1, 0, 0
48:    6560,    820,   16,  1, 0, 0
49:    3280,    394,   11,  0, 0, 0
50:    1644,    214,    2,  0, 0, 0
51:     814,    104,    3,  0, 0, 0
```

Again none survives four generations.  Combining with the earlier high-
valuation sieve gives

```text
a_out <= 39,
n_next > X*m/2^39 > 189812531*m                 (2)
```

for every all-zero-layer cycle of length

```text
177780727155637125195.
```

## 3. Significance

The two all-zero-layer branches now have unconditional growth from their cycle
minimum by factors above `7.59*10^8` and `1.89*10^8`.  The proof is a finite
inverse-class certificate, not a trajectory scan.  It still does not exclude
later compensating contractions.

The verifier is deliberately standalone because it performs several million
exact subgroup tests.  Run

```text
python tools/verify_deep_zero_layer_minimum_sieve.py
```

for full reproduction.
