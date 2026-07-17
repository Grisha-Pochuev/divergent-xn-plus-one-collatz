# All finite `1093`-adic label lifts are cyclically saturated

## Purpose

The previous permanent-label closure theorem ruled out a contradiction modulo

```text
N*1093^2.
```

This note proves the stronger statement needed for strategy selection: **no
higher finite power `1093^r` can create a bare cyclic-closure contradiction
either**.  Every compatible cyclic residue-label word lifts coherently through
all powers `1093^r`, while preserving its `N` coordinate.

Thus the present candidate cannot be completed by adding finitely many deeper
`1093`-adic valuation labels and then asking the finite automaton to close.

## Setup

Put

```text
q=1093,
h=ord_q(2)=364,
m=500/gcd(500,364)=125,
N=2^500-1,
X=2^4501-349*2^500+347=q*c.
```

The exact arithmetic facts are

```text
q does not divide c,
2^h==1 (mod q^2),
2^h!=1 (mod q^3),
v_q(2^h-1)=2.
```

Write

```text
g=2^h,
w=(g-1)/q^2 (mod q).
```

For the primary candidate,

```text
w=891!=0 (mod 1093).                                 (1)
```

For a transition

```text
2^a_i*n_(i+1)=X*n_i+1,                              (2)
```

write

```text
a_i=s_i+h*k_i,
1<=s_i<=h,
```

and let

```text
t_i==a_i (mod 500),
1<=t_i<=500.
```

The pair `(s_i,t_i)` is realizable exactly when

```text
s_i==t_i (mod 4).                                   (3)
```

When (3) holds, `k_i` is fixed modulo `m=125`.

## Base level `q^2`

For every cyclic `s`-word, the adjacent-label formula gives

```text
n_(i+1)
 ==2^(-s_i)*(1+q*c*2^(-s_(i-1))) (mod q^2).         (4)
```

With cyclic indices, (4) satisfies every transition (2) modulo `q^2`, including
wraparound.  The formula is independent of `k_i`, because `g==1 (mod q^2)`.

Choose the unique `k_i (mod 125)` compatible with `(s_i,t_i)`.  This gives the
base cyclic solution while also fixing the permanent `N` label.

## One-step lifting lemma

Assume for some `r>=2` that a cyclic residue word and valuation layers satisfy

```text
2^(s_i+h*k_i)*n_(i+1)==X*n_i+1 (mod q^r),           (5)
```

and that each `k_i` has its required residue modulo `125`.

Choose arbitrary next digits `z_i (mod q)` and seek lifts

```text
n_i'=n_i+q^r*z_i,

k_i'=k_i+125*q^(r-2)*u_i.                            (6)
```

The second formula preserves `k_i (mod 125)` and hence preserves
`a_i (mod 500)`.

Since `g=1+q^2*w+O(q^3)`, the binomial theorem gives

```text
g^(125*q^(r-2)*u_i)
 ==1+125*w*u_i*q^r (mod q^(r+1)).                   (7)
```

The source lift in (6) disappears from the right side modulo `q^(r+1)` because
`q|X`:

```text
X*(q^r*z_i)==0 (mod q^(r+1)).                       (8)
```

Let the old transition defect be

```text
2^(s_i+h*k_i)*n_(i+1)-(X*n_i+1)==q^r*E_i (mod q^(r+1)).
```

After applying (6)--(8), the new digit condition is

```text
E_i
 +2^(s_i+h*k_i)
  *(z_(i+1)+125*w*u_i*n_(i+1))
 ==0 (mod q).                                       (9)
```

All coefficients multiplying `u_i` are nonzero modulo `q`: `125`, `w`, powers
of `2`, and every orbit residue are units.  Therefore, for every chosen
`z_(i+1)`, equation (9) has a unique solution `u_i (mod q)`.

Crucially, (9) contains no new source digit `z_i`.  Each edge lifts
independently, including the wraparound edge.

## Theorem: saturation through every finite power

Let `(s_i,t_i)` be any finite cyclic label word satisfying (3) at every index.
Then for every `r>=2` there exist

```text
k_i (mod 125*q^(r-2)),
n_i (mod q^r),
```

such that

```text
a_i=s_i+h*k_i,
a_i==t_i (mod 500),
2^a_i*n_(i+1)==X*n_i+1 (mod q^r)                    (10)
```

cyclically at every edge.

Moreover, every lift of each existing residue from modulo `q^r` to modulo
`q^(r+1)` can be selected freely: choose `z_(i+1)` first, then solve uniquely
for `u_i` by (9).  Thus each adjacent-label class modulo `q^2` acquires all

```text
q^(r-2)
```

lifts modulo `q^r`.

The exact number of allowed `q^r` classes is therefore

```text
364^2*q^(r-2).                                      (11)
```

After including the `125` compatible `N` labels, the combined permanent class
count modulo `N*q^r` is

```text
16,562,000*q^(r-2).                                 (12)
```

The proportion of allowed lifts does not improve with `r`; higher prime powers
are completely saturated above the informative `q^2` level.

## Preservation of the `N` coordinate

Changing `k_i` in (6) changes `a_i` by

```text
h*125*q^(r-2)*u_i=45500*q^(r-2)*u_i,
```

which is divisible by `500`.  Therefore `2^a_i (mod N)` and the permanent
`N`-coordinate transition remain unchanged at every lift.

The Chinese remainder theorem combines the cyclic solutions modulo `N` and
`q^r`.  Hence every compatible cyclic label word closes modulo

```text
N*q^r
```

for every finite `r>=2`.

## Consequence

There is no possible proof of G3 based only on:

```text
finite N labels
+ finitely many 1093-adic valuation layers
+ cyclic wraparound.
```

The failure is structural, not computational.  A finite deeper lift merely
introduces a new freely adjustable valuation digit which cancels the new
transition defect edge by edge.

This does **not** rule out:

1. occupancy and height estimates using the original `q^2` class compression;
2. the exact global source divisor `g`;
3. an arithmetic invariant at a different prime where the valuation layer is
   not locally free;
4. changing the candidate;
5. a nonlocal Diophantine estimate coupling total credit and correction terms.

It does rule out the proposed `1093^3` experiment and every finite continuation
of the same local-label strategy.

## Verification

Independent exact checker:

```text
python tools/verify_wieferich_q_adic_lift_saturation.py
```

It verifies all candidate constants, exhausts the `364^2` base classes, checks
`w=891`, and constructs coherent cyclic lifts through `q^10` for deterministic
regression words while preserving all modulo-`500` labels.
