# Session checkpoint: sharp block signs for `X=2^156-9`

Date: 2026-07-11

The strict prize problem remains open.  This session produced one new structural
theorem and one exact finite improvement for the primary candidate

```text
X=2^156-9,
n0=1.
```

## 1. Sharp sign theorem

For a complete nonexceptional near-power block, write

```text
9*n-1=2^(156*k+s)*u,
1<=s<=155,
ell=k+1,
e=156-s.
```

The exact displacement is

```text
C_X^ell(n)-n
 =[-Delta_e(ell)*u+(2^e-1)]/9,
Delta_e(ell)=2^(156*ell-e)-X^ell.
```

Define

```text
L_e=floor(e/log2(2^156/X))+1.
```

Exact rational logarithm bounds and modular certificates modulo `2^312` prove,
for every `e=1,...,155`, that

```text
ell<L_e   => the complete block strictly grows,
ell>=L_e  => the complete block strictly contracts.
```

Thus the positive additive term can never rescue a block after its leading
multiplicative factor crosses below `1`.  The sign is independent of the odd
core `u`.

Files:

```text
docs/NEAR_POWER_SHARP_BLOCK_SIGN.md
tools/verify_near_power_block_sign_threshold.py
```

## 2. Improved exact finite cycle barrier

The first threshold is

```text
L_1=7034970411803187993997906985047212163795395135.
```

For a hypothetical cycle, the positive integer

```text
D=156*p-A
```

satisfies

```text
1<=D<p*log2(2^156/X).
```

Therefore

```text
p>=L_1.
```

All positive cycle lengths through

```text
7034970411803187993997906985047212163795395134
```

are excluded.  The previous convenient barrier was

```text
6766211283939365362054096447760569535444132142.
```

The new barrier is about `3.97%` larger.  It is still finite and is not counted
as a fraction of the missing infinite theorem.

## 3. Verification

The new checker was run independently in the chat environment and passed.  It
is also included in

```text
python run_checks.py
```

A complete repository-wide run was not performed in the chat environment,
because the environment has no GitHub CLI and cannot resolve the GitHub host for
a local checkout.

## 4. Exact remaining target

The decisive gate is unchanged:

```text
exclude every nontrivial positive cycle.
```

The sharp block theorem improves the height-credit route.  Future work should:

1. partition a hypothetical cycle into complete near-power blocks;
2. charge every exceptional contraction and every nonexceptional block with
   `ell>=L_e` against earlier proved growth;
3. combine this block accounting with the permanent `1093^2` adjacent-label
   sieve;
4. seek an unbounded height potential rather than another raw finite cutoff.
