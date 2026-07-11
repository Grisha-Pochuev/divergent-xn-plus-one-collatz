# Session checkpoint: no-exceptional block frontier

Date: 2026-07-12

The strict prize problem remains open. The primary candidate remains

```text
k=500,
N=2^500-1,
m=4501,
B=2^4501,
d=349*2^500-347,
X=B-d=2^4501-349*2^500+347,
n0=1.
```

This checkpoint supersedes the earlier same-day family checkpoint as the startup
frontier. The main advance is the first large infinite structural exclusion for
cycles without exceptional complete blocks.

## 1. Previously retained gates

The following remain proved:

- the orbit leaves `1` and never returns;
- all positive cycle lengths through a number between `10^1201` and `10^1202`
  are impossible;
- every exceptional source has at least `1505` decimal digits;
- every output lies in the permanent Mersenne-divisor/Wieferich residue system;
- the global harmonic window holds;
- the general Mersenne-divisor Wieferich family is available.

## 2. Deep-class concentration

For a no-exceptional cycle, let `J` be the number of complete ordinary blocks
and let

```text
D=4501*p-A=sum_(i=1)^J e_i,
1<=e_i<=4500.
```

Then `J<=D`. More than a fraction `1-10^(-1200)` of all cycle values lie in one
fixed combined class whenever the coarse `N*1093^2` coordinate is used.

File:

```text
docs/NO_EXCEPTIONAL_DEEP_CLASS_CONCENTRATION.md
```

## 3. N-adic and X-adic ladders

Every additional consecutive valuation-`4501` step fixes one additional power
of a modulus.

The first version used `N=2^500-1` and proved

```text
sum_i 1/n_i<[D/2+H_D+2]/N.
```

The stronger full-multiplier version uses

```text
F(n)=(X*n+1)/B,
F(n)-1/d=(X/B)*(n-1/d).
```

After `j` consecutive valuation-`4501` steps,

```text
d*F^j(n)==1 (mod X^j).
```

Exact checking of all `4500` terminal deficit classes proves

```text
rho_e>X/(3*e).
```

Therefore every no-exceptional cycle satisfies

```text
sum_i 1/n_i
 <3*D/X+[d+H_D/2]/(X-1),
```

and hence

```text
0<p*delta-D
 <{3*D/X+[d+H_D/2]/(X-1)}/[X*ln(2)].
```

Files:

```text
docs/NO_EXCEPTIONAL_N_ADIC_LADDER.md
tools/verify_no_exceptional_n_adic_ladder.py

docs/NO_EXCEPTIONAL_X_ADIC_LADDER.md
tools/verify_no_exceptional_x_adic_ladder.py
```

## 4. Complete exclusion of one and two ordinary blocks

For one ordinary block with deficit `e`, exact closure gives

```text
[2^(4501*p-e)-X^p]*u=2^e-1.
```

Exact rational logarithmic bounds prove that at the first positive-gap length
the left gap already exceeds `2^4501`; it then increases strictly. Thus no
ordinary one-block cycle exists for any

```text
1<=e<=4500
```

or any cycle length.

For two ordinary blocks, cyclically choose the second as the shorter block. Its
entire additive numerator is less than

```text
2*B^(floor(p/2)+1),
```

while the positive cycle gap is larger. Exact certification covers every total
deficit

```text
2<=D<=9000.
```

Thus no ordinary two-block cycle exists.

Files:

```text
docs/NO_EXCEPTIONAL_ONE_BLOCK_ALL_CREDITS.md
tools/verify_no_exceptional_one_block_all_credits.py

docs/NO_EXCEPTIONAL_TWO_BLOCK_ALL_CREDITS.md
tools/verify_no_exceptional_two_block_all_credits.py
```

## 5. General block-count frontier

For `J` ordinary blocks, choose a longest block `ell_1`. Exact elimination of
all block cores gives

```text
Delta_D(p)*u_1=R,
Delta_D(p)=2^(4501*p-D)-X^p,
R<J*B^(p-ell_1+1).
```

Let

```text
beta=1/delta=ln(2)/ln(B/X).
```

Exact rational bounds certify the continued-fraction tail

```text
[1,1,145062,23,1,4,1,12,2].
```

The last upper semiconvergent before the next upper convergent has denominator

```text
573867416,
```

and the next upper convergent denominator is

```text
1106246945.
```

The one-sided best-approximation theorem gives a uniform positive logarithmic
gap for every

```text
D<1106246945.
```

Combining this with the longest-block estimate proves:

```text
Any no-exceptional positive cycle must contain at least 245833 complete blocks.
```

Block lengths remain unrestricted. This is not a trajectory cutoff or a cycle-
length cutoff.

Files:

```text
docs/NO_EXCEPTIONAL_BLOCK_COUNT_FRONTIER.md
tools/verify_no_exceptional_block_count_frontier.py
```

## 6. Verification performed

The exact calculations underlying the new checkers were run in the chat Python
environment:

- all `4500` one-block deficit thresholds;
- all `8999` two-block total-deficit thresholds;
- all `4500` terminal classes modulo `X`;
- the exact continued-fraction interval and convergents;
- the deep-class and ladder identities.

The new checkers are included in `run_checks.py`. A complete repository-wide
run was not executed because the chat container could not resolve GitHub and did
not have a fresh checkout. Do not report a full-suite pass until a checkout or
GitHub Actions run completes.

## 7. Decisive remaining cases

The cycle problem is now split into three strict branches:

1. no exceptional blocks, at least `245833` ordinary blocks;
2. exactly one exceptional block;
3. at least two exceptional blocks.

The next primary target is branch 2. Use the exact exceptional source floor and
write the cycle as one exceptional contraction followed by an ordinary segment.
The ordinary segment should be controlled by the `X`-adic ladder and the general
block-core closure.

For branch 1, further continued-fraction denominators alone are not the desired
advance. The target is a many-block population theorem using repeated terminal
deficits and their exact classes modulo `X`.
