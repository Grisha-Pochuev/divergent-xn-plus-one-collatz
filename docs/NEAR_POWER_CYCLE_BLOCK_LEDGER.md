# Near-power cycle block ledger

Let

```text
B=2^m,
d odd,
1<=d<B/2,
X=B-d>=5,
C_X(n)=(X*n+1)/2^v2(X*n+1).
```

This note gives a canonical complete-block partition of every hypothetical
positive cycle and an exact height-credit identity.

## 1. Canonical cyclic block partition

For each positive odd state put

```text
r(n)=v2(d*n-1).
```

The near-power trichotomy says:

```text
r<m  => the next valuation is r<m;
r>m  => the next valuation is m and r decreases by m;
r=m  => the next valuation is m+b for some b>=1.
```

A positive cycle cannot have valuation `m` at every step, because every
`r>m` step strictly decreases the current value.  Therefore its cyclic
valuation word contains at least one entry different from `m`.

Partition the cyclic word into maximal strings

```text
m,m,...,m,a
```

whose terminal valuation satisfies `a!=m`.  This partition is canonical up to a
cyclic rotation.

There are two block types.

### Ordinary terminal block

If the terminal valuation is

```text
a=s<m,
```

and it is preceded by `k` copies of `m`, then

```text
ell=k+1,
r_start=m*k+s,
e=m-s,
```

and the block has terminal credit

```text
c=e>0.
```

### Exceptional terminal block

If the terminal valuation is

```text
a=m+b,
b>=1,
```

and it is preceded by `k-1` copies of `m`, then

```text
ell=k,
r_start=m*k,
```

and the block has terminal credit

```text
c=-b<0.
```

Every exceptional complete block strictly contracts.  In fact, if

```text
d*n-1=B^ell*u,
u odd,
```

then its endpoint `n'` satisfies

```text
n'/n
 =(X^ell*u+1)/(2^b*(B^ell*u+1))
 <2^(-b).                                             (1)
```

Thus an exceptional excess valuation of `b` loses more than `b` binary height
units.

## 2. Exact valuation-credit balance

Let a hypothetical cycle have accelerated length `p`, total valuation `A`, and
complete blocks indexed by `j`.  Put

```text
D=m*p-A.
```

Since each block contains `ell_j-1` entries equal to `m` and one terminal entry,

```text
D=sum_j c_j.                                         (2)
```

Equivalently,

```text
D
 =sum_(ordinary blocks)(m-s_j)
  -sum_(exceptional blocks)b_j.                      (3)
```

The cycle product gives

```text
1<=D<p*delta,
delta=log2(B/X).                                    (4)
```

Therefore all exceptional excess valuations must be paid for by ordinary
terminal deficits, with at least one unit left over:

```text
sum_(ordinary)(m-s_j)
 >=1+sum_(exceptional)b_j.                            (5)
```

This is an exact cycle-wide accounting law, not a probabilistic estimate.

## 3. Unified complete-block ratio

Consider one complete block of length `ell`, source `n`, endpoint `n'`, and
terminal credit `c`.

For an ordinary block, write

```text
d*n-1=B^ell*u/2^e,
c=e.
```

For an exceptional block, write

```text
d*n-1=B^ell*u,
c=-b.
```

Both cases satisfy the same exact ratio identity:

```text
n'/n
 =2^c*(X/B)^ell
  *[1+((B/X)^ell-1)/(d*n)].                           (6)
```

The final factor is strictly greater than `1`.  Define its logarithmic
correction

```text
kappa(n,ell)
 =log2(1+((B/X)^ell-1)/(d*n))>0.                      (7)
```

Then

```text
log2(n'/n)=c-ell*delta+kappa(n,ell).                  (8)
```

Summing around a cycle and using (2) gives the exact block correction identity

```text
sum_j kappa(n_j,ell_j)=p*delta-D.                     (9)
```

Equivalently, without logarithms,

```text
product_j [1+((B/X)^ell_j-1)/(d*n_j)]
 =B^p/(2^D*X^p).                                     (10)
```

This compresses every run of valuation-`m` steps into one positive correction
term at its block source.

## 4. Uniform correction bound

For either block type, its coordinate has the form

```text
d*n-1=B^ell*u/H,
```

where

```text
H=2^e<=B/2  for an ordinary block,
H=1<=B/2    for an exceptional block.
```

Hence

```text
1/(d*n)<1/(2*B^(ell-1)).                              (11)
```

Also

```text
B^ell-X^ell<ell*d*B^(ell-1).                         (12)
```

Combining (11)--(12),

```text
0<((B/X)^ell-1)/(d*n)<ell*d/(2*X^ell).               (13)
```

Since `log2(1+z)<z/ln(2)`, every block obeys

```text
0<kappa(n,ell)<ell*d/(2*X^ell*ln(2)).                 (14)
```

Using `sum ell_j=p` and `X^ell_j>=X`, (9) gives the global strip

```text
0<p*delta-D<d*p/(2*X*ln(2)),                          (15)
```

or

```text
p*(delta-d/(2*X*ln(2)))<D<p*delta.                   (16)
```

The lower coefficient is positive because

```text
ln(1+d/X)>d/(X+d)=d/B>d/(2X).
```

Thus a hypothetical near-power cycle cannot place `D/p` anywhere below the
roughly half-width strip in (16).  This is stronger than the earlier condition
`1<=D<p*delta`, although it does not yet exclude every integer `D`.

## 5. Specialization to `X=2^156-9`

For the primary candidate,

```text
m=156,
d=9,
X=2^156-9.
```

The two coefficients in (16) are approximately

```text
delta
 =1.4214700865297345588*10^(-46),

delta-9/(2*X*ln(2))
 =7.1073504326486727939*10^(-47).
```

So every hypothetical positive cycle must satisfy an exact integer constraint
in a strip whose lower edge is approximately half its upper edge.

For exceptional sources, `B==1 (mod 9)` forces the odd core to satisfy

```text
u==8 (mod 9).
```

The least positive odd choice is `u=17`.  Hence every one-step exceptional
source satisfies

```text
n>=(17*2^156+1)/9
 =172538387740453816732379459417894523153825369657.   (17)
```

More generally, an exceptional complete block of length `ell` starts at

```text
n>=(17*2^(156*ell)+1)/9.                              (18)
```

This supplies an explicit height cost for every exceptional contraction.

## 6. Use in the remaining proof

The sharp block-sign theorem classifies ordinary blocks as growing or
contracting.  The present ledger now adds:

1. exact payment of every exceptional excess `b` by ordinary deficits;
2. more than `b` bits of height loss for each exceptional block;
3. one correction term per complete block rather than per accelerated step;
4. the global deficit strip (16);
5. the explicit exceptional-source height floor (18).

The remaining task is to combine these facts with the permanent `1093^2`
adjacent-label sieve and distinct cycle values to prove that the corrections in
(9) cannot support a complete cycle.

## 7. Verification

```text
python tools/verify_near_power_cycle_block_ledger.py
```
