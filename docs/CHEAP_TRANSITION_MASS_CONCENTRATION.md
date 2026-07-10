# Cheap-transition mass concentration

This note strengthens the transition-class argument for the two remaining
sparse-window lengths.

Use

```text
X = 104350542602662257699,
O = ord_X(2) = 1860810887857924950,
K = 5000.
```

For every edge `n_i -> n_(i+1)`, write

```text
a_i = s_(i+1)+O*q_i
```

and assign the exact edge cost

```text
c_i=(s_i-1)+(s_(i+1)-1)+2*O*q_i.
```

As proved in the repeated-transition theorem,

```text
sum_i c_i=2*(A-p).                                (1)
```

## 1. At least 97.38 percent of edges are cheap

For either remaining length, (1) gives

```text
#{i:c_i>=5000}
 <= floor(2*(A-p)/5000)
 = 4657855051477692680.
```

Therefore at least

```text
173122872104159432513
```

edges are cheap for the first remaining length, and at least

```text
173122872104159432515
```

are cheap for the second.  This is more than `97.38%` of all edges.

Since `5000<2*O`, every cheap edge has

```text
q_i=0,
s_i+s_(i+1)<=5001.                               (2)
```

There are exactly

```text
5000*5001/2 = 12502500
```

ordered pairs satisfying (2).

## 2. Exact lower bound for every cheap target

A zero-layer pair `(u,v)` determines one odd target class modulo `2*X^2`:

```text
n' == 2^(-v)*(1+X*2^(-u)) (mod X^2).
```

The exact certificate enumerates all `12502500` pairs with `u+v<=5001` and
proves that their least positive odd representatives are distinct.  The
smallest one is

```text
781563824454394220933608138645145,
```

attained at

```text
(u,v)=(2395,2209).
```

Hence every cheap target satisfies

```text
n_i >= 781563824454394220933608138645145.         (3)
```

The total reciprocal contribution of all cheap targets is therefore less than

```text
2.216*10^(-13).                                   (4)
```

No harmonic or floating-point estimate is needed for (4): it follows by
multiplying the number of cheap edges by the reciprocal of the exact integer in
(3).

## 3. A small expensive transition is mandatory

For the remaining lengths, exact rational logarithm bounds give

```text
sum_i 1/n_i > 0.506785306
```

when

```text
p=177780727155637125193,
```

and

```text
sum_i 1/n_i > 0.099934206
```

when

```text
p=177780727155637125195.
```

Subtracting the exact cheap-target bound and using the maximum number of
expensive edges proves that an expensive edge must have target at most

```text
9190982840926584716
```

for the first length, and at most

```text
46609216582838682965
```

for the second length.

Thus any remaining hypothetical cycle contains a transition whose target is
strictly below `X`, and whose edge satisfies at least one of

```text
q_i>=1
```

or

```text
s_i+s_(i+1)>=5002.
```

For the harder second length the forced target is below `0.447*X`; for the
first it is below `0.089*X`.

## 4. Significance

Almost all cycle positions are now proved to lie extremely high and to
contribute essentially nothing to the reciprocal correction.  The whole
required correction must be concentrated in at most `2.62%` expensive
transitions, one of which is explicitly forced below the multiplier `X`.

This does not yet eliminate the two lengths, but it converts the large
zero-delay tail into a concentration statement: any final contradiction may
focus on small expensive transitions and their neighbours rather than on the
entire cycle.

Run

```text
python tools/verify_cheap_transition_mass_concentration.py
```

for the exact certificate.
