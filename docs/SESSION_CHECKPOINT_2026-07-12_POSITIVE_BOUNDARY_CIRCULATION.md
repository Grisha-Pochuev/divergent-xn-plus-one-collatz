# Session checkpoint: positive boundary circulation

Date: 2026-07-12

The strict prize problem remains open. The primary candidate is unchanged:

```text
X=2^4501-349*2^500+347,
n0=1.
```

## 1. Global block frontier retained

Every hypothetical nontrivial positive cycle contains at least

```text
245833 ordinary complete blocks.
```

This holds for arbitrary exceptional-block populations and arbitrary lengths.

## 2. New bounded positive circulation

For every ordinary terminal deficit type `e` occurring in a hypothetical cycle,
choose the smallest cycle boundary value `x_e` of that type. Follow the actual
orbit to the next ordinary boundary of type `f(e)` and value `y_e`. Minimality
gives

```text
y_e>=x_(f(e)).
```

The finite functional graph on at most `4500` types contains a directed cycle.
Multiplication around it gives a collection of disjoint orbit intervals with
actual height product at least `1`.

Let `q` be the number of selected ordinary intervals, `C` their total net block
credit, `L` their total accelerated length, and `T` their total number of
complete blocks. Exact block corrections and continued-fraction separation
prove

```text
q<=4500,
1<=C<=20250000,
T<=20254499,
L*log2(B/X)<C.
```

Thus the selected formal concatenation has strict base expansion

```text
2^C*(X/B)^L>1.
```

Files:

```text
docs/MINIMUM_BOUNDARY_POSITIVE_CIRCULATION.md
tools/verify_minimum_boundary_positive_circulation.py
```

The standalone checker passed and is included in `run_checks.py`.

## 3. Exact remaining obstruction

The selected intervals need not occur consecutively in the original orbit.
Their endpoints and the next selected starts have the same ordinary boundary
type modulo `X`, but need not match as integers or in the full two-adic word
cylinder.

The next theorem must resolve this splicing gap by proving one of:

1. compatible boundary intervals can be concatenated into an admissible growing
   orbit segment;
2. a nonzero mismatch produces a strict height descent;
3. the mismatch is impossible after lifting the boundary equation modulo `X^2`
   or a higher power.

A larger finite barrier or a longer continued-fraction prefix is not the current
priority.