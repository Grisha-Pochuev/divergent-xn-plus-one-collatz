# Cycle-floor sharpening of local block corrections

Date: 2026-07-17

## Scope

Let

```text
B=2^m,
d positive odd,
1<=d<B/2,
X=B-d,
```

and consider a hypothetical positive accelerated `Xn+1` cycle, partitioned into
canonical complete near-power blocks. Suppose every cycle value is strictly
larger than a known integer floor `M>=1`.

For a complete block of length `ell`, source `n`, endpoint `n'`, and credit `c`,
write

```text
q(n,ell)=((B/X)^ell-1)/(d*n),
kappa(n,ell)=log2(1+q(n,ell)).
```

The retained local formula is

```text
log2(n'/n)=c-ell*delta+kappa(n,ell),
delta=log2(B/X).
```

This note uses the global cycle-value floor to sharpen the correction term for
short complete blocks. For the primary candidate it improves the local
nondecreasing length coefficient from `2^3994` to the exact rational
`2^4002/997`, and improves the bounded initial macro-exit from `2^4006` to
`2^4005`.

## 1. Floor-sensitive correction bound

The exact expression for `q` is

```text
q(n,ell)=(B^ell-X^ell)/(X^ell*d*n).                    (1)
```

When `ell=1`, `B-X=d`, so

```text
q(n,1)=1/(X*n)<1/(X*M).                               (2)
```

For every `ell>=2`, the retained complete-block coordinate estimate gives

```text
q(n,ell)<ell*d/(2*X^ell)
            <=ell*d/(2*X^2).                          (3)
```

Therefore, with

```text
u=max(1/(X*M), d/(2*X^2)),                            (4)
```

every complete block obeys

```text
0<q(n,ell)<ell*u.                                     (5)
```

Since `log2(1+q)<q/ln(2)`, any actual consecutive segment of complete blocks,
with total accelerated length `L` and total correction `K`, satisfies

```text
0<K<L*epsilon,
epsilon=u/ln(2).                                      (6)
```

This is much sharper than replacing every block by the older uniform
coefficient `d/(2*X*ln(2))`: the older coefficient treats a length-one block as
if its source were near the smallest coordinate-compatible value, whereas a
hypothetical primary cycle has every source above the much larger global floor
`M=N`.

## 2. Sharpened nondecreasing-segment theorem

Let an actual consecutive complete-block segment have

```text
C = net credit,
L = accelerated length,
x = source,
y = endpoint.
```

Summing the exact block formulas gives

```text
log2(y/x)=C-L*delta+K.                                (7)
```

If `y>=x`, then (6)--(7) imply

```text
0<=C-L*delta+K
  <C-L*(delta-epsilon).                               (8)
```

Hence, whenever `delta>epsilon`, every nondecreasing segment has `C>=1` and

```text
L<C/(delta-epsilon).                                  (9)
```

The theorem is length-independent and applies equally to uncovered ordinary
blocks, positive-credit maximal sponsor arches, and any larger actual segment
formed from consecutive complete blocks.

## 3. Primary exact coefficient

Specialize to

```text
N=2^500-1,
B=2^4501,
d=349*2^500-347,
X=B-d,
M=N.
```

The retained global theorem proves that every value of a hypothetical cycle is
strictly larger than `N`. Exact integer comparison gives

```text
2*X>d*N.                                              (10)
```

Thus

```text
1/(X*N)>d/(2*X^2),
u=1/(X*N),
epsilon=1/(X*N*ln(2)).                               (11)
```

Now

```text
delta-epsilon
 =[-ln(1-d/B)-1/(X*N)]/ln(2)
 >[d/B-1/(X*N)]/ln(2).                                (12)
```

The elementary exact bound

```text
ln(2)<7/10                                            (13)
```

follows from

```text
exp(7/10)>1+7/10+(7/10)^2/2+(7/10)^3/6>2.
```

The standalone checker verifies the exact rational comparison

```text
(10/7)*(d/B-1/(X*N))>997/2^4002.                     (14)
```

Combining (9), (12), and (14), every positive-credit nondecreasing segment in a
hypothetical primary cycle satisfies

```text
L<C*2^4002/997.                                       (15)
```

In particular,

```text
L<C*2^3993.                                           (16)
```

This replaces the previous coarse theorem

```text
L<C*2^3994.
```

The previously proved contracting-side estimate remains

```text
y<x and C>=1  =>  L>C*2^3992.                        (17)
```

Thus the primary positive-credit height-sign dichotomy is sharpened to

```text
nondecreasing: L<C*2^4002/997<C*2^3993;
contracting:   L>C*2^3992.                            (18)
```

## 4. Improved bounded initial macro-exit

The retained sponsor-arch theorem constructs an actual initial macro-exit from
the least complete-block boundary with

```text
z<y,
1<=C<=4500.
```

It is therefore nondecreasing, so (15) gives

```text
L_macro<4500*2^4002/997<2^4005.                      (19)
```

This improves the previous uniform bound

```text
L_macro<2^4006.
```

The remaining return still has positive credit and contracts. Its retained
lower bound

```text
L_return>R*2^3992
```

is unchanged.

## 5. Strategic meaning and limitation

The result removes almost all of the formerly dominant local correction term:
for the primary candidate it is controlled by `1/(X*N)` rather than `d/(2*X)`.
Consequently every nondecreasing positive-credit macroblock has length only
slightly above the exact drift scale `C/delta`.

This does not yet exclude the final return. It sharpens the remaining
alternative:

1. a positive-credit macroblock contracts and therefore has length above
   `C*2^3992`; or
2. contraction is supplied by zero-credit sponsor arches, which remain the only
   macroblocks without a credit-proportional lower length bound.

The next useful target is to combine (18) with the exact endpoint labels or to
obtain a quantitative length/height theorem for zero-credit arches.

## 6. Verification

Run

```text
python tools/verify_cycle_floor_local_correction_sharpening.py
```

The checker uses only exact integer and rational arithmetic. It verifies:

```text
ln(2)<7/10;
2*X>d*N;
u=1/(X*N);
delta-epsilon>997*2^-4002;
2^4002/997<2^3993;
4500*2^4002/997<2^4005;
```

and checks the floor-sensitive `q` bound and complete-block identity on the
known accelerated `5n+1` cycles

```text
13 -> 33 -> 83 -> 13,
17 -> 43 -> 27 -> 17.
```
