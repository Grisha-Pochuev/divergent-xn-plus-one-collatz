# Giant compensating growth block

Fix either of the two remaining sparse-window lengths.  For odd `p` in this
window the exact total valuation is

```text
A=(133*p+1)/2.
```

Write every valuation as

```text
a_i=s_(i+1)+O*q_i,
O=ord_X(2)=1860810887857924950,
1<=s_i<=O,
q_i>=0.
```

Assume at least one `q_i` is positive.  Let

```text
k=#{i:q_i>=1},
Q=sum_i q_i.
```

Then `1<=k<=Q<=6257`.

## 1. Deficit over the zero-layer blocks

The `k` positive-layer positions split the cyclic sequence into `k` zero-layer
blocks.  For block `j`, let

```text
L_j = its length,
S_j = sum of its exact valuations.
```

On a zero-layer block every valuation equals its least full label.  Define the
twice-half-power deficit

```text
D_j=133*L_j-2*S_j.
```

The total valuation spent at positive-layer positions is at least

```text
k+O*Q.
```

Therefore

```text
sum_j D_j
 = 133*(p-k)-2*sum_j S_j
 >= 2*O*Q-131*k-1
 >= k*(2*O-131)-1.
```

Hence one zero-layer block satisfies the safe integer bound

```text
D_j >= 2*O-132.                                  (1)
```

Since every term `133-2*s_i` is at most `131`, (1) also forces

```text
L_j >= ceil((2*O-132)/131)
     = 28409326532182060.                         (2)
```

## 2. Exact growth along the block

Along this block the step ratios satisfy

```text
n_(t+1)/n_t = (X+1/n_t)/2^s_(t+1) > X/2^s_(t+1).
```

Multiplying and using `X>2^66.5` gives

```text
n_end/n_start
 > X^L/2^S
 > 2^(66.5*L-S)
 = 2^(D_j/2)
 >= 2^(O-66).
```

Thus one consecutive least-layer block increases the orbit by more than

```text
2^1860810887857924884.
```

## 3. Consequence

Any hypothetical remaining cycle has one of two forms:

1. every step lies in the least full-order layer; or
2. it contains a block of at least `28409326532182060` least-layer steps whose
   endpoint exceeds its start by a factor greater than
   `2^1860810887857924884`.

In the second case the cycle maximum-to-minimum ratio is at least that factor.
This is not yet a contradiction because a positive-layer step can produce an
opposing enormous contraction.  It supplies a precise height target for a
future combination with the logarithmic cycle-height or global balance
identities.

Run

```text
python tools/verify_giant_compensating_growth_block.py
```

for the exact arithmetic certificate.
