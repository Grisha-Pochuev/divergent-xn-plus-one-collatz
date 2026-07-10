# Complete macroblocks and 2-adic regeneration for `X = 2^m + 1`

This note advances the finite-growth construction for the accelerated map

```text
C_X(n) = (X*n+1) / 2^v2(X*n+1)
```

with

```text
X = 2^m + 1,   m >= 2.
```

The earlier construction stopped immediately before its exceptional exit. Here we compute that exit exactly, prove that the whole block can still have net growth, and show that the precision transferred to the next block is governed by a 2-adic isometry.

## 1. The complete macroblock

Let `L >= 1` and start at

```text
n_0 = 2^(m*L) - 1.
```

For `0 <= j <= L-1`, the first part of the orbit is

```text
n_j = 2^(m*(L-j)) * X^j - 1.
```

For `0 <= j < L-1`, the exact valuation is `m`. At the last state,

```text
n_(L-1) = 2^m * X^(L-1) - 1,
```

and therefore

```text
X*n_(L-1)+1 = 2^m * (X^L - 1).
```

Write

```text
k = v2(L).
```

The lifting-the-exponent lemma gives

```text
v2(X^L - 1) = m + k.
```

Hence the last valuation is `2m+k`, and after all `L` accelerated steps the exact endpoint is

```text
E_m(L) = (X^L - 1) / 2^(m+k).                 (1)
```

This includes the exceptional exit instead of stopping one step before it.

## 2. The accumulated growth can survive the exit

Put

```text
delta_m = log2(X / 2^m) = log2(1 + 2^(-m)) > 0.
```

**Proposition.** If

```text
L*delta_m > m + v2(L) + 1,                    (2)
```

then

```text
E_m(L) > n_0.
```

**Proof.** Since `X^L > 2`,

```text
X^L - 1 > X^L / 2.
```

Using (1),

```text
E_m(L)
  > X^L / 2^(m+k+1)
  = 2^(mL) * 2^(L*delta_m-m-k-1).
```

Condition (2) makes the final factor larger than `1`, so

```text
E_m(L) > 2^(mL) > 2^(mL)-1 = n_0.
```

QED.

Thus the exceptional division does not always erase the accumulated gain. Since the left side of (2) grows linearly in `L`, while `v2(L)` grows at most logarithmically, there are arbitrarily large complete finite macroblocks whose endpoint is already larger than their start.

Example:

```text
m=2, X=5, L=7
n_0 = 2^14-1 = 16383
E_2(7) = (5^7-1)/4 = 19531 > n_0.
```

## 3. First precision-transfer congruence

Write

```text
L = 2^k * u,   u odd,
A = X^(2^k),
c = (A-1) / 2^(m+k).
```

Then `c` is odd and

```text
E_m(L) = c * (1 + A + ... + A^(u-1)).         (3)
```

The endpoint satisfies the sharp congruence

```text
E_m(L) == u                    (mod 2^m),  if k=0,
E_m(L) == u + 2^(m-1)          (mod 2^m),  if k>=1.       (4)
```

**Proof.** We have `A == 1 (mod 2^m)`, so the geometric sum in (3) is congruent to `u` modulo `2^m`.

If `k=0`, then `c=1`. If `k>=1`, expand

```text
(1+2^m)^(2^k)-1
```

and divide by `2^(m+k)`. The linear term is `1`; the quadratic term is

```text
(2^k-1) * 2^(m-1) == 2^(m-1)  (mod 2^m).
```

For degree `r>=3`, the standard estimate

```text
v2(binomial(2^k,r)) >= k-v2(r)
```

shows that the divided term has valuation at least

```text
m*(r-1)-v2(r) >= m.
```

Therefore

```text
c == 1+2^(m-1)  (mod 2^m)
```

when `k>=1`. Multiplication by odd `u` leaves the added `2^(m-1)` unchanged modulo `2^m`, proving (4). QED.

Consequently, a large new precision

```text
v2(E_m(L)+1)
```

requires the odd part `u` of `L` to lie in a thin congruence class. It is not produced freely by making `L` large.

## 4. Exact 2-adic isometry

Fix `m` and `k`, and vary the positive odd part `u`. Keep

```text
A = X^(2^k),
c = (A-1) / 2^(m+k).
```

Equation (3) defines `E_(m,k)(u)`.

**Isometry theorem.** For distinct positive odd integers `u` and `v`,

```text
v2(E_(m,k)(u) - E_(m,k)(v)) = v2(u-v).        (5)
```

**Proof.** Assume `u>v`. From (3),

```text
E(u)-E(v)
  = c * A^v * (A^(u-v)-1)/(A-1).
```

Both `c` and `A` are odd. Since `A == 1 (mod 4)`, the lifting-the-exponent lemma gives

```text
v2(A^(u-v)-1) = v2(A-1) + v2(u-v).
```

After division by `A-1`, equation (5) follows. QED.

This is much stronger than a statistical observation: changing `u` by exactly `2^s` changes the endpoint by exactly the same 2-adic precision `2^s`.

## 5. A unique regeneration target at every precision

For every `S >= 1`, there is exactly one odd residue class

```text
u_S  (mod 2^S)
```

such that

```text
E_(m,k)(u_S) == -1  (mod 2^S),
```

or equivalently

```text
v2(E_(m,k)(u_S)+1) >= S.                      (6)
```

Indeed, the isometry theorem makes the map on odd residue classes modulo `2^S` injective. The domain and the odd codomain each contain `2^(S-1)` classes, so the map is bijective. Therefore `-1` has exactly one preimage.

The classes `u_S` lift uniquely as `S` increases and define one odd 2-adic target `u_*`. This target is not any ordinary integer.

To see this, the continuous 2-adic extension of (3) can be written

```text
E(u) = (A^u-1) / 2^(m+k).
```

If an ordinary integer `U` satisfied `E(U)=-1`, then, as an equality of rational numbers,

```text
A^U = 1-2^(m+k).
```

The right side is negative, while `A^U` is positive for every ordinary integer `U`, including negative `U`. This is impossible.

So arbitrary finite regeneration is possible, but exact infinite regeneration follows a genuinely nonintegral 2-adic target.

## 6. Reproducible examples

For `m=3`, `k=0`, and precision `S=17`, the unique least positive representative is

```text
u_17 = 599.
```

Thus, for `X=9` and `L=599`,

```text
v2(E_3(599)+1) = 17,
```

and the complete macroblock has strong net growth: its start has 1797 bits while its endpoint has 1896 bits.

For `m=4`, `k=1`, and `S=10`, the target odd part is

```text
u_10 = 39,
L = 2*u_10 = 78,
```

and

```text
v2(E_4(78)+1) = 10.
```

Both examples are independently reproduced by

```text
python tools/analyze_fermat_macroblock.py --m 3 --L 599 --k 0 --precision 17
python tools/analyze_fermat_macroblock.py --m 4 --L 78 --k 1 --precision 10
```

## 7. Consequence for the main search

The old finite construction established arbitrarily long increasing prefixes. The present result adds two new facts:

1. the exceptional exit can be included while retaining net growth;
2. the endpoint can regenerate any prescribed finite amount of `v2(n+1)` precision, but only along one uniquely determined 2-adic target class.

This turns regenerative block chaining into an exact lifting problem rather than a blind trajectory search.

It still does **not** prove an infinite divergent positive orbit. The unresolved step is to turn the nested finite regeneration targets into one ordinary positive starting integer, or to find a different certificate whose growth survives indefinitely without following one fixed nonintegral 2-adic target.
