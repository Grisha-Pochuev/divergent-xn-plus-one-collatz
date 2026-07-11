# No ordinary two-block cycle exists

Use the primary candidate

```text
m=4501,
B=2^4501,
d=349*2^500-347,
X=B-d.
```

This note excludes every hypothetical positive cycle consisting of exactly two
complete ordinary near-power blocks. Both block lengths and both terminal
deficits are unrestricted:

```text
ell_1,ell_2>=1,
1<=e_1,e_2<=4500.
```

## 1. Exact block-core recurrences

For block `i`, put

```text
q_i=2^(m*ell_i-e_i),
c_i=2^e_i-1.
```

If `u_i` is its positive odd source core, exact complete-block closure gives

```text
q_2*u_2=X^ell_1*u_1+c_1,
q_1*u_1=X^ell_2*u_2+c_2.                             (1)
```

Eliminating `u_2`,

```text
Delta_D(p)*u_1
 =X^ell_2*c_1+q_2*c_2,                              (2)
```

where

```text
p=ell_1+ell_2,
D=e_1+e_2,
2<=D<=9000,
Delta_D(p)=2^(m*p-D)-X^p.                           (3)
```

Cycle closure requires `Delta_D(p)>0`.

## 2. Rotate so that the second block is shorter

The two blocks may be cyclically relabelled. Choose the labelling so that

```text
ell_2<=floor(p/2).                                  (4)
```

Since

```text
c_i<B,
q_2<B^ell_2,
X<B,
```

the additive numerator in (2) obeys

```text
X^ell_2*c_1+q_2*c_2
 <2*B^(ell_2+1)
 <=2*B^(floor(p/2)+1).                              (5)
```

## 3. Uniform lower bound for every positive cycle gap

Put

```text
delta=log2(B/X).
```

For each `D=2,...,9000`, let

```text
L_D=floor(D/delta)+1.                               (6)
```

Exact rational logarithmic bounds, constructed as in the one-block theorem,
certify all `8999` thresholds:

```text
(L_D-1)*ln(B/X)<D*ln(2)<L_D*ln(B/X).                (7)
```

For every `p>=L_D`, set

```text
z=p*ln(B/X)-D*ln(2)>0.
```

At the first threshold, and therefore at every later `p`, exact rational
certification gives

```text
z>2^(-22206).                                       (8)
```

Consequently

```text
Delta_D(p)
 =X^p*(exp(z)-1)
 >X^p*z
 >2^(4500*p-22206),                                 (9)
```

because `X>2^4500`.

Every certified threshold has `p>=12`, and exact integer comparison gives

```text
4500*p-22206
 >1+4501*(floor(p/2)+1).                            (10)
```

Combining (5), (9), and (10),

```text
Delta_D(p)
 >2*B^(floor(p/2)+1)
 >X^ell_2*c_1+q_2*c_2.                              (11)
```

Since `u_1>=1`, equation (2) is impossible.

## 4. Theorem

```text
For X=2^4501-349*2^500+347,
there is no positive cycle consisting of exactly two ordinary complete blocks.
```

This holds for every pair of terminal deficits and every pair of positive block
lengths. It is an infinite structural exclusion, not a finite search.

Together with the one-block theorem, every hypothetical cycle without
exceptional blocks must contain at least three complete blocks.

## 5. Next extension

For `J` ordinary blocks, choosing one longest block gives a block-core closure
whose additive numerator contains `J` terms and omits that longest block from
every exponent. The same comparison should exclude all sufficiently small
fixed `J`.

The genuinely global difficulty appears when `J` itself is unbounded. Then the
number of boundary terms grows, and the proof must combine:

1. the exact credit bound `J<=D`;
2. the N-adic ladder inside every long block;
3. deficit-specific residue classes at the boundaries.

## 6. Verification

```text
python tools/verify_no_exceptional_two_block_all_credits.py
```

The checker certifies every `D=2,...,9000` with exact rational inequalities and
verifies the uniform exponent comparison (10). Decimal arithmetic proposes the
thresholds; exact rational comparisons certify them.
