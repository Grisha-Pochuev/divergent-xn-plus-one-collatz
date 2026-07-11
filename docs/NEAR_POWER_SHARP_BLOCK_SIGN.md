# Sharp nonexceptional block signs for `X=2^156-9`

Put

```text
m=156,
B=2^m,
d=9,
X=B-d.
```

This note removes the additive ambiguity in every complete nonexceptional
near-power block for the structured candidate.

## 1. Block displacement in deficit coordinates

Suppose

```text
d*n-1=2^(m*k+s)*u,
k>=0,
1<=s<=m-1,
u odd and positive.
```

Write

```text
ell=k+1,
e=m-s.
```

The complete-block formula gives

```text
C_X^ell(n)=(X^ell*u+2^e)/d.
```

Since

```text
n=(2^(m*ell-e)*u+1)/d,
```

the exact displacement is

```text
C_X^ell(n)-n
 =[-Delta_e(ell)*u+(2^e-1)]/d,                       (1)
```

where

```text
Delta_e(ell)=2^(m*ell-e)-X^ell.                     (2)
```

The leading multiplicative comparison alone does not normally decide the sign
when `Delta_e(ell)>0`, because the positive additive term `2^e-1` might in
principle compensate for a small gap.  For this particular `X`, that never
happens.

## 2. Exact threshold

Let

```text
delta=log2(B/X)=log2(1+9/X)
```

and, for `1<=e<=155`, define

```text
L_e=floor(e/delta)+1.
```

Then

```text
Delta_e(ell)<=0  for ell<L_e,
Delta_e(ell)>0   for ell>=L_e.                       (3)
```

The threshold is certified without floating-point assumptions.  The checker
uses exact rational upper and lower bounds for

```text
ln(1+9/X)
```

from its alternating series and for `ln(2)` from

```text
ln(2)=2*atanh(1/3).
```

For every `e`, these bounds prove

```text
(L_e-1)*ln(1+9/X) < e*ln(2) < L_e*ln(1+9/X).        (4)
```

In particular,

```text
L_1   =7034970411803187993997906985047212163795395135,
L_155 =1090420413829494139069675582682317885388286245793.
```

The `155` thresholds are strictly increasing.

## 3. The additive term never rescues a block

At the first contracting length `L_e`, put

```text
G_e=Delta_e(L_e)>0.
```

Because `m*L_e-e>=2m`, the power-of-two term in (2) vanishes modulo `B^2`, so

```text
G_e == -X^L_e (mod B^2).                             (5)
```

For all `e=1,...,155`, exact modular exponentiation proves that the least
nonnegative residue on the right side of (5) is strictly larger than

```text
2^e-1.                                               (6)
```

Since `G_e` is positive, (5)--(6) imply

```text
G_e>2^e-1.                                           (7)
```

Moreover

```text
Delta_e(ell+1)=B*Delta_e(ell)+d*X^ell,               (8)
```

so `Delta_e` is strictly increasing after it becomes positive.  Therefore

```text
Delta_e(ell)>2^e-1  for every ell>=L_e.              (9)
```

Substitution into (1) gives the sharp dichotomy:

```text
ell<L_e   => C_X^ell(n)>n,
ell>=L_e  => C_X^ell(n)<n.                            (10)
```

Thus the sign of every complete nonexceptional block depends only on its length
`ell` and terminal deficit `e=m-s`.  There is no exceptional small-gap case and
no dependence on the odd core `u`.

## 4. Exact cycle-length improvement

For a hypothetical positive accelerated cycle of length `p` and total valuation
`A`, let

```text
D=m*p-A.
```

As before,

```text
1<=D<p*delta.
```

Hence necessarily

```text
p>1/delta,
```

and (4) for `e=1` gives the exact integral barrier

```text
p>=L_1.
```

Therefore every positive cycle length through

```text
7034970411803187993997906985047212163795395134
```

is impossible.  This replaces the earlier convenient but weaker bound

```text
floor(2*X/27)
=6766211283939365362054096447760569535444132142.
```

The improvement is finite and does not by itself exclude cycles of all lengths.
Its main structural value is (10): all later nonexceptional contractions now
have a fully classified astronomical run-length threshold.

## 5. Verification

```text
python tools/verify_near_power_block_sign_threshold.py
```
