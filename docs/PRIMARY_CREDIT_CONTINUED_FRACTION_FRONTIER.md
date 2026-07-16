# Primary total-credit continued-fraction frontier

Date: 2026-07-17

## Scope

Use the retained primary candidate

```text
N=2^500-1,
B=2^4501,
d=349*2^500-347,
X=B-d.
```

Assume, for contradiction, that a nontrivial positive accelerated `Xn+1` cycle
exists. Write

```text
p = full accelerated length,
A = total valuation,
D = 4501*p-A >= 1.
```

This note removes the sign restriction from the earlier nonpositive-return
continued-fraction argument and pushes its denominator frontier much farther.
It proves that every hypothetical cycle must satisfy the explicit 300-digit
lower bound

```text
D >= Q,
```

where

```text
Q=
924679364903952241768234680715310598867316370441120757898246831506500507205080014535351439406991342585993538327845986892977536682537320095988153612270886695873966778097766981798062925612878469213187733241206117142814414961418054803443235355123715316220902421623921086365374327267387194352877014114959.  (1)
```

## 1. Exact cycle correction

Put

```text
lambda=ln(B/X),
beta=ln(2)/lambda.
```

The exact accelerated cycle product gives

```text
z=p*lambda-D*ln(2)
 =lambda*(p-D*beta)
 =sum_cycle ln(1+1/(X*n_i))>0.                         (2)
```

Thus `p/D` is an upper rational approximation to `beta`. The task is to compare
the mandatory one-sided continued-fraction gap with an upper bound for the full
positive correction `z`.

## 2. One-sided continued-fraction lemma

Use the standard best-upper-approximation fact:

> Let `beta` be irrational, with convergents `p_j/q_j`. For odd `j`, the
> intermediate convergents
> `
> (p_(j-2)+t*p_(j-1))/(q_(j-2)+t*q_(j-1)),
> `
> `1<=t<=a_j`, are the successive best upper approximations of the second kind.
> If the next such denominator is `q_next`, then every integer pair `r,s` with
> `1<=s<q_next` and `r-s*beta>0` has error at least that of the preceding upper
> intermediate convergent.

This is the usual determinant-one continued-fraction lemma. It is not a
probabilistic statement and it does not enumerate cycle trajectories.

The checker constructs rigorous rational intervals for `ln(2)` and
`ln(B/X)`, then verifies that the first `554` continued-fraction coefficients of
`beta` are fixed throughout that interval. At index `553`,

```text
a_553=36.
```

The `t=26` upper intermediate convergent is the final best upper approximation
before the `t=27` denominator, which is exactly `Q` in (1). If its numerator and
denominator are `P_*` and `Q_*`, then for every `1<=D<Q` and every integer `p`
with `p-D*beta>0`,

```text
p-D*beta >= P_*-Q_* beta.                              (3)
```

The exact interval certificate consequently gives a positive rational number
`G` such that

```text
z>G.                                                   (4)
```

The large numerator `P_*` need not be trusted from a printed decimal: the
checker regenerates it from the certified continued fraction and verifies that
consecutive intermediate convergents have determinant `1`.

## 3. A self-consistent length cap below the frontier

The retained global complete-block correction theorem gives every hypothetical
cycle the upper bound

```text
p < 2*D*B*X/[d*(X-d)].                                 (5)
```

Assume `D<Q`. Exact integer arithmetic verifies

```text
2*Q*B*X < 2^4991*d*(X-d).                              (6)
```

Therefore

```text
p<2^4991.                                               (7)
```

This finite cap is not being used as evidence of divergence. It is a conditional
consequence of the assumption `D<Q`, used to obtain a rigorous global correction
upper bound.

## 4. Full correction upper bound

Use the retained actual expanding exit from the least ordinary boundary. It
contains at most `4500` complete blocks. Its correction satisfies

```text
K_exit
 <4500/(X*N)+4500*d/X^2.                               (8)
```

The remaining return consists of distinct cycle values in

```text
16562000
```

permanent classes modulo

```text
M=N*1093^2.
```

Let

```text
S0=(500/N)*[1+H_(364^2/4)/2],
T=16562000/(2*M).
```

The retained harmonic-packing theorem gives, for return length `L`,

```text
sum_return 1/n < S0+T*H_(ceil(L/16562000)).             (9)
```

Under (7), `L<p<2^4991`. Hence

```text
H_(ceil(L/16562000))
 <=1+ln L
 <1+4991*ln(2).                                        (10)
```

Using `ln(1+u)<u`, equations (8)--(10) give the exact rational upper bound

```text
z<K_upper
 =4500/(X*N)+4500*d/X^2
  +[S0+T*(1+4991*ln(2))]/X.                            (11)
```

The checker replaces `ln(2)` in (11) by a rigorous rational upper bound and
verifies

```text
K_upper<G.                                              (12)
```

Equations (4) and (12) contradict each other. Therefore `D<Q` is impossible,
which proves (1).

## 5. Consequences

The frontier has

```text
2^996<Q<2^997.
```

Combining it with the one-over-1007 cycle strip

```text
p>D*2^4002/1008
```

gives

```text
p>2^4988.                                               (13)
```

Also, total ordinary credit is at least `D`, while one ordinary complete block
contributes at most `4500`. Hence every hypothetical cycle contains at least

```text
ceil(Q/4500)
=
205484303311989387059607706825624577526070304542471279532943740334777890490017781007855875423775853907998564072854663753995008151674960021330700802726863710194214839577281551510680650136195215380708385164712470476180981102537345511876274523360825625826867204805315796970083183837197154300639336470
```

ordinary complete blocks. This supersedes the former lower bound `245833`.

## 6. Meaning and limitation

This is an infinite-family exclusion: it rules out every possible cycle with
`1<=D<Q`, not merely a computed range of starting values. It also uses no
assumption that the remaining return has nonpositive credit.

It still does not exclude cycles with `D>=Q`. Gate G3 remains open. The new
frontier is useful because any future source-class or adjacent-label argument may
now assume an enormous amount of unmatched positive credit and a cycle length
above `2^4988`.

## 7. Verification

Run

```text
python tools/verify_primary_credit_continued_fraction_frontier.py
```

The checker uses exact integers and `Fraction` only. It verifies the logarithm
intervals, `554` common continued-fraction coefficients, the `t=26`/`t=27`
one-sided frontier, determinant one, the conditional bound `p<2^4991`, exact
harmonic-packing constants, and the final strict correction-gap contradiction.
