# X-adic ladder for cycles without exceptional blocks

Use the primary candidate

```text
m=4501,
B=2^4501,
d=349*2^500-347,
X=B-d.
```

Assume a hypothetical positive cycle has only ordinary complete near-power
blocks. Let its block deficits be `e_1,...,e_J`, and put

```text
D=e_1+...+e_J=4501*p-A.
```

Then

```text
J<=D.                                                (1)
```

The earlier `N`-adic ladder used `N=2^500-1`. The present theorem works modulo
the full multiplier `X` and is therefore much stronger.

## 1. Repeated valuation `m` fixes one class modulo `X^j`

During an exact valuation-`m` step,

```text
F(n)=(X*n+1)/B.
```

Because `B-X=d`,

```text
F(n)-1/d=(X/B)*(n-1/d).                             (2)
```

After `j` consecutive valuation-`m` steps,

```text
d*F^j(n)-1=(X^j/B^j)*(d*n-1).                      (3)
```

The left side is an integer, so

```text
d*F^j(n)==1 (mod X^j).                              (4)
```

Thus every depth-`j` internal output from every block lies in the single class

```text
d^(-1) (mod X^j).                                  (5)
```

Since `1<d<X`, the least positive representative `r_j` of that class satisfies

```text
r_j>=(X^j+1)/d.                                     (6)
```

Indeed, `d*r_j-1` is a positive multiple of `X^j`.

## 2. Terminal classes modulo `X`

A terminal deficit `e=m-s` has terminal valuation `s=m-e`. The output class is

```text
n_next==2^(-s) (mod X).                             (7)
```

Using `2^m=B==d (mod X)`,

```text
2^(-s)==2^e*d^(-1) (mod X).                        (8)
```

For each `e=1,...,4500`, let `rho_e` be the least allowed positive odd
representative of (8), excluding `1` because the orbit cannot return to `1`.
Exact modular arithmetic proves the uniform inequality

```text
rho_e>X/(3*e).                                      (9)
```

The worst coefficient occurs at `e=7`; even there

```text
X/(e*rho_e)<3.
```

Consequently the total reciprocal mass of all terminal outputs is strictly
less than

```text
sum_(i=1)^J 1/rho_(e_i)
 <3*D/X.                                             (10)
```

## 3. Internal outputs of all depths

At a fixed depth `j`, at most `J` blocks reach that depth. Those values are
distinct positive odd integers in one class modulo `X^j`, so their spacing is
at least `2*X^j`.

By (6), their reciprocal mass is at most

```text
d/X^j+H_J/(2*X^j).                                  (11)
```

Summing over every depth `j>=1`,

```text
sum_(all internal outputs) 1/n
 <[d+H_J/2]/(X-1).                                  (12)
```

Since `J<=D`, (10)--(12) give the global no-exceptional bound

```text
sum_i 1/n_i
 <3*D/X+[d+H_D/2]/(X-1).                            (13)
```

This bound is independent of the cycle length and of the individual block
lengths.

## 4. Sharpened correction window

Let

```text
delta=log2(B/X),
epsilon=p*delta-D.
```

The exact cycle product identity gives

```text
epsilon
 =sum_i log2(1+1/(X*n_i))
 >0.                                                 (14)
```

Using `log2(1+z)<z/ln(2)` and (13), every cycle without exceptional blocks must
satisfy

```text
0<p*delta-D
 <{3*D/X+[d+H_D/2]/(X-1)}/[X*ln(2)].               (15)
```

The dominant scale is now `D/X^2`, rather than `D/(N*X)` from the previous
`N`-adic ladder. Since `X/N` is roughly `2^4001`, this is an enormous
strengthening.

## 5. Relation to the block exclusions

The one-block and two-block theorems completely exclude `J=1` and `J=2`.
Equation (15) applies to every remaining no-exceptional cycle, which must have

```text
J>=3.
```

The next global target is to combine (15) with the exact block-core closure for
`J` blocks. Choosing a longest block removes that block from every additive
exponent; the `X`-adic ladder should then control the remaining `J` boundary
terms.

## 6. Verification

```text
python tools/verify_no_exceptional_x_adic_ladder.py
```

The checker verifies all `4500` terminal classes, the uniform bound (9), sample
instances of the depth congruence (4), and the exact geometric sums used in
(12).
