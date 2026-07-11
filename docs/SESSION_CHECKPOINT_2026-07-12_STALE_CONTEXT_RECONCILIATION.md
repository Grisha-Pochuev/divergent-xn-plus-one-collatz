# Session checkpoint: mixed-block rederivation and frontier reconciliation

Date: 2026-07-12

## 1. Why this checkpoint exists

This chat resumed from an in-chat summary whose active frontier was older than the
current `main` branch.  The chat therefore started to rederive the branch with one
exceptional block and at least two ordinary blocks.

Before recording a new theorem, the current repository state was fetched.  The
repository already contains the strictly stronger results

```text
docs/ONE_EXCEPTION_BLOCK_COUNT_FRONTIER.md
docs/GLOBAL_ORDINARY_BLOCK_COUNT_FRONTIER.md
```

and the current durable frontier is

```text
Every hypothetical nontrivial positive cycle has at least 245833 ordinary
complete blocks, for every number of exceptional complete blocks.
```

Consequently, the calculations below are retained as an independent algebraic
cross-check, not claimed as a new strengthening of the current frontier.

## 2. Exact three-block mixed closure recovered in this chat

Use

```text
m=4501,
B=2^4501,
X=B-d,
d=349*2^500-347.
```

Consider exactly three complete blocks in cyclic order:

1. one exceptional block of length `k` and excess `b`;
2. one ordinary block of length `ell_1` and deficit `e_1`;
3. one ordinary block of length `ell_2` and deficit `e_2`.

Put

```text
q_i=2^(m*ell_i-e_i),
c_i=2^e_i-1,
c_b=2^b-1,
p=k+ell_1+ell_2,
D=e_1+e_2-b,
Delta_D(p)=2^(m*p-D)-X^p.
```

Let `v` be the exceptional source core and `u_1,u_2` the two ordinary
source cores.  The exact source relations are

```text
2^b*q_1*u_1=X^k*v-c_b,
q_2*u_2=X^ell_1*u_1+c_1,
B^k*v=X^ell_2*u_2+c_2.                                  (1)
```

Eliminating the other two cores gives the following three equivalent closure
equations:

```text
Delta_D(p)*u_1
 =X^k*(X^ell_2*c_1+q_2*c_2)-B^k*q_2*c_b,                (2)

Delta_D(p)*v
 =2^b*q_1*(X^ell_2*c_1+q_2*c_2)
  -X^(ell_1+ell_2)*c_b,                                  (3)

Delta_D(p)*u_2
 =X^(k+ell_1)*c_2+2^b*B^k*q_1*c_1
  -B^k*X^ell_1*c_b.                                      (4)
```

These identities display the same signed structure used in the current global
block theorem: ordinary blocks contribute positive additive terms and the
exceptional block contributes one negative additive term.

## 3. Independent three-block exclusion check

Choose the equation corresponding to a longest one of the three block lengths.
That longest length is at least `ceil(p/3)`, so every remaining length exponent
is at most `floor(2*p/3)`.  Equations (2)--(4), together with

```text
q_i<B^ell_i,
c_i<B,
c_b<B,
2^b*q_1<B^(ell_1+1),
```

give the uniform crude upper bound

```text
0<Delta_D(p)*core<3*B^(floor(2*p/3)+2).                  (5)
```

For this branch

```text
1<=D<=8999.
```

The exact rational logarithmic certificate already used elsewhere in the
repository gives, whenever `Delta_D(p)>0`,

```text
Delta_D(p)>2^(4500*p-22206).                             (6)
```

In this chat, all `D=1,...,8999` were checked at their first positive gap length,
with exact rational inequalities around the logarithmic threshold.  The integer
exponent comparison

```text
4500*p-22206
 >2+4501*(floor(2*p/3)+2)                                (7)
```

held in every case.  Since `3<4`, equations (5)--(7) contradict one another.
Thus the independently rederived special-case conclusion is

```text
No positive cycle consists of exactly one exceptional block and exactly two
ordinary blocks.
```

This conclusion is already subsumed by the stronger current theorem requiring
at least `245833` ordinary blocks.

## 4. Checks actually run in this chat

The following checks completed locally in the chat environment:

1. symbolic elimination with SymPy verified equations (2), (3), and (4)
   identically;
2. exact rational logarithmic threshold certification was run for every
   `D=1,...,8999`;
3. the uniform exponent comparison (7) was checked for every such threshold.

The exact threshold loop completed for all 8999 credits.  No complete
repository-wide `python run_checks.py` run was performed in this chat.

## 5. Correct next target

Do not resume from the obsolete split

```text
one exceptional block + at least two ordinary blocks.
```

The current correct remaining frontier is

```text
at least 245833 ordinary complete blocks,
with an arbitrary number of exceptional complete blocks.
```

The next useful target remains a genuine many-block population theorem using:

1. only 4500 possible ordinary terminal deficits;
2. repeated boundary classes modulo `X` and `2^500-1`;
3. the exceptional credit budget;
4. the full `X`-adic ladder inside long valuation-4501 runs;
5. a height-dependent descent or shorter positive-credit segment.

Merely repeating fixed-small-block exclusions or enlarging a finite barrier is
not the next priority.
