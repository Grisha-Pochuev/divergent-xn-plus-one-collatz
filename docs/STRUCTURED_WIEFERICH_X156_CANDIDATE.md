# Structured Wieferich candidate `X=2^156-9`

This candidate combines three exact features:

1. a Wieferich divisor forbids return to `1`;
2. near-power coordinates classify every valuation block;
3. the orbit from `1` begins with eight identical six-step macroblocks.

Put

```text
B=2^156,
X=B-9
 =91343852333181432387730302044767688728495783927,
n0=1.
```

The strict prize problem remains open because nontrivial cycles above the finite
barrier are not excluded.

## 1. No return to `1`

For `q=1093`,

```text
ord_q(2)=364,
2^364 == 1 (mod q^2),
2^156 == 9      (mod q),
2^156 == 165052 (mod q^2).
```

Therefore

```text
X == 165043 == 151*q (mod q^2),
```

so `q` divides `X` exactly once.

The first accelerated step is

```text
C_X(1)=(X+1)/8=2^153-1
 =11417981541647679048466287755595961091061972991,
```

which is not `1`.

If a positive odd `y` mapped directly to `1`, then

```text
X*y+1=2^a.
```

Modulo `q`, this forces `364|a`; the Wieferich congruence then gives
`q^2|(2^a-1)=X*y`.  Since `q` divides `X` exactly once, `q|y`.
But every accelerated output is coprime to `q`, because `X*z+1==1 (mod q)` and
dividing by a power of two cannot introduce the odd factor `q`.  Hence

```text
C_X^t(1) != 1 for every t>=1.                       (1)
```

## 2. Forced six-step block

Assume

```text
n == 1 (mod 2^20).
```

Since `m>=20`, `X==-9 (mod 2^20)`.  Define the scaled numerators

```text
N_0=n,
N_(j+1)=X*N_j+2^A_j,
```

where `A_j` is the cumulative valuation before step `j+1`.
For `n=1`, exact reduction modulo `2^20` gives

```text
j   a_j   A_j after step   N_j mod 2^20
1    3          3             1048568
2    1          4                  80
3    2          6             1047872
4    2          8                6400
5    5         13              991232
6    6         19              524288
```

The displayed residues have exact two-adic valuations

```text
3,4,6,8,13,19.
```

For any `n==1 (mod 2^20)`, every `N_j(n)` differs from `N_j(1)` by
`X^j*(n-1)`, a multiple of `2^20`.  Therefore the exact accelerated valuation
word is

```text
(3,1,2,2,5,6),                                     (2)
```

with total valuation `19`.

The exact six-step map is

```text
G(n)=C_X^6(n)
    =[X^6*n+X^5+8*X^4+16*X^3+64*X^2+256*X+8192]/2^19.   (3)
```

## 3. Precision transfer

Subtracting `1` in (3) gives

```text
G(n)-1=[X^6*(n-1)+B*P(B)]/2^19,                     (4)
```

where

```text
P(B)=B^5-53*B^4+1178*B^3-14042*B^2
     +94645*B-341825.
```

Because `B` is even and the constant term of `P` is odd, `P(B)` is odd.
Consequently:

- for `n=1`, `v2(G(1)-1)=m-19`;
- if `20<=L=v2(n-1)<m`, then

```text
v2(G(n)-1)=L-19.                                    (5)
```

Thus every complete six-step block removes exactly `19` zeroes from `n-1`.

Set

```text
J=floor((m-1)/19).
```

Starting from `1`, the first `J` blocks are forced.  For `m=156`,

```text
J=8,
accelerated steps=48,
valuation word=(3,1,2,2,5,6)^8,
total valuation=152,
v2(n_48-1)=4.                                       (6)
```

Since every additive term in (3) is positive,

```text
G(n)>X^6*n/2^19.
```

Therefore

```text
n_48>X^48/2^152.                                    (7)
```

## 4. Finite cycle barrier

For a hypothetical positive cycle of length `p` and total valuation `A`,

```text
2^A=product_i(X+1/n_i)<B^p.
```

Hence the integer

```text
D=156*p-A
```

satisfies `D>=1`.  Also `2^A>X^p`, so

```text
D<p*log2(B/X)=p*log2(1+9/X).
```

Using `ln(1+y)<y` and `ln(2)>2/3`,

```text
D<27*p/(2*X).
```

Thus all positive cycle lengths through

```text
floor(2*X/27)
=6766211283939365362054096447760569535444132142
```

are impossible.

## 5. Comparison with `X=2^260-3`

The `2^260-3` candidate has the much larger finite barrier.  The present
candidate has a shorter near-power depth and an exact repeating six-step initial
program.  It is therefore the cleaner candidate for attempts to prove a
renewal or height-credit theorem.

## 6. Limitation

At step `48`, `v2(n_48-1)=4`, so another full six-step block is no longer forced.
The missing theorem is to show that later dynamics recreates enough of the
`n==1 (mod 2^20)` precision, or to convert the accumulated height into a global
barrier against every later contraction.

Independent checker:

```text
python tools/verify_structured_wieferich_x156_candidate.py
```
