# Two-generation reciprocal bound through sixty million

This note strengthens the exact transition-priced reciprocal certificate for
the hardest remaining sparse-window length

```text
p = 177780727155637125195.
```

Its total valuation is fixed by the power-of-two interval:

```text
A = 11822418355849868825468.
```

## 1. Exact modular population

Use the already retained cutoff

```text
C = 60000000.
```

Among the `2154` allowed progressions modulo `2*15099`, there are exactly

```text
4279760
```

positive candidates at most `C`.  The index-eight subgroup test modulo

```text
P = 6911089648497401
```

leaves exactly

```text
536735
```

genuine full output representatives.

The permanent mod-3 predecessor sieve removes

```text
178632
```

of them.  Hence exactly

```text
358103
```

representatives survive the first-generation reachability condition.

For each survivor the exact full label `s` is recovered by Pohlig--Hellman, and
the finite `45297`-state predecessor automaton supplies the delay `d`.  Every
cycle occurrence therefore spends at least

```text
w(n)=s+ord_X(2)*d
```

units of total valuation.

## 2. Exact fractional dual

Distinctness and the cycle valuation budget imply

```text
sum_n w(n)*x_n <= A,
0<=x_n<=1.
```

For every rational `lambda>0`,

```text
sum_n x_n/n
 <= lambda*A + sum_n max(0,1/n-lambda*w(n)).
```

Ordering the `358103` items by `1/(n*w(n))`, the fractional boundary occurs
after exactly

```text
5941
```

complete items.  The unique boundary item is

```text
n = 108791,
s = 1416690312052110223,
d = 9,
w = 18163988302773434773.
```

Taking `lambda=1/(n*w)` for that item and evaluating the dual with exact
rational arithmetic proves

```text
sum_(cycle elements n<=60000000) 1/n
 < 0.099476202.                                    (1)
```

## 3. Residual required above the cutoff

For the target length, exact positive atanh-series bounds give

```text
X*Lambda > 0.099934206,
```

where

```text
Lambda=A*log(2)-p*log(X).
```

Combining this with the cycle identity

```text
X*Lambda <= sum_i 1/n_i
```

and (1) gives the strict residual

```text
sum_(n_i>60000000) 1/n_i > 0.000458.              (2)
```

Every value above the cutoff contributes less than `1/60000000`.  Thus (2)
forces at least

```text
27481
```

distinct cycle elements above sixty million whose reciprocal contribution is
necessary.

## 4. Meaning

This still does not eliminate the final exceptional length: sufficiently many
larger values could in principle supply the residual.  It does show that the
last case cannot be supported by a small collection of exceptional tiny
representatives.  Any surviving cycle must carry a quantitatively large tail,
and that tail must also obey source/target circulation and the global height
identities.

Run

```text
python tools/verify_two_generation_sixty_million_bound.py
```

for the exact deterministic certificate.  The modular pass is over the same
`4279760` finite candidates already used by the retained sixty-million subgroup
sieve; it is not a trajectory search.
