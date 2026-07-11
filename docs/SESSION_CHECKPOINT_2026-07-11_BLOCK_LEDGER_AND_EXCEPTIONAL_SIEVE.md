# Session checkpoint: block ledger and exceptional sieve

Date: 2026-07-11

The strict prize problem remains open.  This session continued the primary
candidate

```text
X=2^156-9,
n0=1.
```

It produced three compatible structural advances.

## 1. Sharp signs for all ordinary complete blocks

For each of the `155` possible terminal deficits `e`, the exact threshold

```text
L_e=floor(e/log2(2^156/X))+1
```

separates strict growth from strict contraction:

```text
ell<L_e   => strict growth,
ell>=L_e  => strict contraction.
```

The first threshold is

```text
L_1=7034970411803187993997906985047212163795395135.
```

The additive term never changes the sign after the multiplicative threshold.
This also raises the exact finite cycle barrier to

```text
7034970411803187993997906985047212163795395134.
```

Files:

```text
docs/NEAR_POWER_SHARP_BLOCK_SIGN.md
tools/verify_near_power_block_sign_threshold.py
```

## 2. Exact cycle-wide block ledger

Every hypothetical positive cycle has a canonical partition into complete
near-power blocks.  Assign terminal credit

```text
c=e   for an ordinary block ending below valuation 156,
c=-b  for an exceptional block ending at valuation 156+b.
```

If the cycle has length `p`, total valuation `A`, and

```text
D=156*p-A,
```

then exactly

```text
D=sum c_j
 =sum ordinary deficits-sum exceptional excesses.
```

Every exceptional block contracts by more than `b` binary height units.  Every
block also satisfies one unified exact ratio formula, and summation around a
cycle gives

```text
sum kappa_j=p*log2(2^156/X)-D.
```

A uniform bound on the corrections yields the new cycle strip

```text
p*(delta-9/(2*X*ln(2)))<D<p*delta,
delta=log2(2^156/X).
```

Thus the integer `D` must lie in roughly the upper half of the formerly allowed
interval.

Files:

```text
docs/NEAR_POWER_CYCLE_BLOCK_LEDGER.md
tools/verify_near_power_cycle_block_ledger.py
```

## 3. Exceptional sources combined with the permanent `1093^2` sieve

The exact exceptional condition is

```text
v2(9*n-1)=156
```

and is equivalent to

```text
n=(17*2^156+1)/9+2^157*t,
t>=0.
```

Every value in a hypothetical cycle also belongs to one of the `132496`
adjacent-label classes modulo `1093^2`.  Combining both restrictions by the
Chinese remainder theorem and checking all label pairs gives the exact minimum

```text
n>=(125*2^156+1)/9
 =1268664615738631005385143083955106787895774776889.
```

It is attained by label pair `(61,64)` and progression layer `t=6`.  This is
about `7.35` times the raw exceptional-source floor.

Files:

```text
docs/X156_EXCEPTIONAL_Q2_SIEVE.md
tools/verify_x156_exceptional_q2_sieve.py
```

## 4. Verification

All three new checkers were run independently in the chat environment and
passed.  They are included in

```text
python run_checks.py
```

A complete repository-wide run was not executed locally because the chat
container could not obtain a fresh GitHub checkout.  The standalone exact
checks did run successfully.

## 5. Remaining decisive theorem

The global cycle-exclusion gate is still open.  The next attack should combine:

1. the exact block-credit sum;
2. the roughly half-width integer strip for `D`;
3. the large minimum height of every exceptional source;
4. the `132496` permanent residue classes;
5. distinct-value harmonic packing.

The aim is to prove that the required block corrections cannot sum to
`p*delta-D` around a complete cycle.
