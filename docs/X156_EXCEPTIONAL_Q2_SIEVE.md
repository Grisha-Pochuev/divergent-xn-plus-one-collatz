# Exceptional-source sieve for `X=2^156-9`

Put

```text
m=156,
B=2^m,
d=9,
X=B-d,
q=1093,
h=ord_q(2)=364.
```

This note combines the exact exceptional near-power condition with the permanent
adjacent-label sieve modulo `q^2`.

## 1. Exact exceptional progression

A source `n` begins an exceptional complete block exactly when

```text
v2(9*n-1)=156.
```

Since `B==1 (mod 9)`, write

```text
9*n-1=B*u.
```

The integer `u` must be positive, odd, and satisfy

```text
u==8 (mod 9).
```

Hence

```text
u=17+18*t,
t>=0,
```

and every exceptional source lies in the single progression

```text
n=n_exc+2*B*t,
n_exc=(17*B+1)/9.                                  (1)
```

Conversely every value in (1) has exact valuation `156`, because
`17+18*t` is odd.  Thus (1) is an if-and-only-if description.

Without any further orbit information, the least exceptional source is

```text
n_exc
=172538387740453816732379459417894523153825369657.
```

## 2. Permanent orbit classes modulo `q^2`

Because `q` is Wieferich to base `2`, every value with two preceding orbit
transitions has residue

```text
n_i
 ==2^(-s_(i-1))
   *(1+q*c*2^(-s_(i-2))) (mod q^2),                 (2)
```

where

```text
c=X/q (mod q)=151,
1<=s_(i-2),s_(i-1)<=364.
```

The ordered label pair determines the residue injectively.  Therefore exactly

```text
364^2=132496
```

residue classes modulo

```text
q^2=1194649
```

can occur in a cycle.

## 3. Chinese-remainder combination

The moduli

```text
2*B and q^2
```

are coprime.  Combining (1) with each of the `132496` residues in (2) gives one
exceptional-source class modulo

```text
2*B*q^2
=218247683691965730041139235214959349143617519566716928.
```

Exact enumeration of the label pairs proves that the smallest positive
representative occurs for

```text
(s_(i-2),s_(i-1))=(61,64),
residue modulo q^2=1097740,
t=6.
```

Consequently every exceptional source belonging to a hypothetical positive
cycle satisfies

```text
n>=(125*B+1)/9
 =1268664615738631005385143083955106787895774776889. (3)
```

The factor `125` appears because `17+18*6=125`.

This is approximately `7.35` times the raw exceptional lower bound in (1).
Unlike a finite trajectory observation, (3) applies permanently to every
exceptional source in every hypothetical cycle for this multiplier.

## 4. Meaning for the height-credit route

Every exceptional complete block contracts by more than `b` binary height
units, where `b` is its excess terminal valuation.  The combined sieve now says
that such a contraction cannot even begin below the explicit height in (3).

This does not yet exclude all cycles.  Its use is to combine:

1. the cycle-wide block-credit identity;
2. the very large minimum height of every exceptional source;
3. the `132496` permanent adjacent-label classes;
4. distinct-value harmonic packing.

## 5. Verification

```text
python tools/verify_x156_exceptional_q2_sieve.py
```
