# Exceptional-source floor for the balanced Mersenne-divisor candidate

Use the explicit family member

```text
k=500,
N=2^500-1,
m=4501,
B=2^4501,
d=349*2^500-347=2+349*N,
X=B-d,
n0=1.
```

The Mersenne-divisor family theorem proves

```text
N|X,
1093||X,
```

and gives two permanent coordinates for every hypothetical cycle value:

1. one valuation label modulo `500` determines the value modulo `N`;
2. two adjacent valuation labels modulo `364` determine the value modulo
   `1093^2`.

This note combines those coordinates with the exact exceptional progression.

## 1. Exact exceptional progression

A source begins an exceptional complete near-power block exactly when

```text
v2(d*n-1)=4501.                                     (1)
```

Since `d` is odd, (1) is one progression modulo `2*B`:

```text
n=n_exc+2*B*T,
T>=0,                                               (2)
```

where

```text
n_exc==(B+1)*d^(-1) (mod 2*B),
0<n_exc<2*B.
```

Writing

```text
d*n_exc-1=u0*B,
```

exact arithmetic gives the positive odd coefficient

```text
u0=
937578593120856832981657775299654199170120439926424550439880178791932328513240962911286104786705519512179141903420156424601516442564181262667387896197461.  (3)
```

Every progression layer has

```text
d*n-1=(u0+2*d*T)*B.                                (4)
```

## 2. Reduction modulo `N=2^500-1`

Because

```text
B==d==2 (mod N),
2*B==4 (mod N),
```

and every cycle value satisfies

```text
n==2^(-s) (mod N),
1<=s<=500,                                          (5)
```

each label `s` determines one progression layer `T_s` modulo `N`:

```text
T_s
 ==[2^(-s)-n_exc]*4^(-1) (mod N),
0<=T_s<N.                                           (6)
```

Sorting the `500` exact values in (6), the first four are

```text
T_498=T0,
T_497=T0+1,
T_496=T0+3,
T_495=T0+7,                                         (7)
```

where

```text
T0=
61954010346953194280268210363239484986876566228377936770699541902501039174574265692694166166505377887473274781450979884806889457995961777808814539620.  (8)
```

Their residues modulo `N` are respectively

```text
4, 8, 16, 32.
```

Every other label has `T_s>T0+7`.

## 3. The `1093^2` adjacent-label test

Let `Q=1093^2`. For adjacent labels

```text
1<=a,b<=364,
```

the permanent coordinate gives one residue `r_(a,b)` modulo `Q`. Since the
progression step `2*B` is invertible modulo `Q`, it gives one layer

```text
T_(a,b)
 ==[r_(a,b)-n_exc]*(2*B)^(-1) (mod Q).              (9)
```

The map from ordered label pairs to layers in (9) is injective.

For the four layers in (7), exact enumeration of the `364^2` adjacent-label
pairs gives

```text
T0     mod Q=625816: no adjacent-label lift;
T0+1   mod Q=625817: no adjacent-label lift;
T0+3   mod Q=625819: no adjacent-label lift;
T0+7   mod Q=625823: unique pair (161,311).          (10)
```

The current labels are compatible because

```text
495==311 (mod gcd(500,364)),
gcd(500,364)=4.                                     (11)
```

The corresponding value residue is

```text
n==209910 (mod 1093^2).                             (12)
```

## 4. Exact minimality

Every combined progression layer is a Chinese-remainder solution

```text
T=T_s+N*z,
z>=0.                                               (13)
```

The candidate `T0+7` is smaller than `N`. Hence any smaller combined layer
would have to have `z=0` and be one of the smaller `N`-layers in (7). The first
three are ruled out by (10), and all other `N`-layers are already larger.
Therefore the exact first compatible exceptional layer is

```text
T_min=T0+7
=
61954010346953194280268210363239484986876566228377936770699541902501039174574265692694166166505377887473274781450979884806889457995961777808814539627.  (14)
```

It has labels

```text
N-label=495,
1093-label pair=(161,311).                          (15)
```

## 5. Permanent exceptional-source floor

Substitution into (4) gives

```text
u_min=
141554173562669451979142234479211407387695161061947663158036275475013035570532072821977692485924548874811696146286209742307923384940182399969083204712328957713629782297601610389067903491331197096456313288013542743720638224927691460837892079910386115268969408753656537834465197519183303759432510875217219.  (16)
```

Consequently every exceptional source in every hypothetical positive cycle for
this multiplier satisfies

```text
n>=(u_min*2^4501+1)/(349*2^500-347).                (17)
```

The integer on the right has `1505` decimal digits. Compared with the raw
coefficient `u0`, the permanent sieve increases the odd-core floor by a factor
strictly between `10^149` and `10^150`.

This is an infinite-family orbit restriction: it applies to every exceptional
source in any hypothetical cycle, not only to a computed initial trajectory.
It does not by itself exclude all cycles.

## 6. Verification

```text
python tools/verify_mersenne_divisor_wieferich_family.py
```

The checker proves minimality by enumerating the `500` one-label layers and the
`364^2` adjacent-label layers. It does not enumerate the full product of
`16,562,000` combined classes.
