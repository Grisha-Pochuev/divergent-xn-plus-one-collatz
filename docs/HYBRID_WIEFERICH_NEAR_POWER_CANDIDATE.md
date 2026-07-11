# Hybrid Wieferich near-power candidate

This note introduces a new explicit candidate that combines two independent
mechanisms:

1. a Wieferich divisor forbids every return to `1`;
2. extreme closeness to a power of two gives a huge elementary cycle-length
   barrier.

Put

```text
B  = 2^260,
X  = B-3
   = 1852673427797059126777135760139006525652319754650249024631321344126610074238973,
n0 = 1.
```

The strict prize problem is not solved by this note, because cycles above the
finite barrier remain possible.

## 1. Exact arithmetic at the Wieferich prime

Let

```text
q=1093.
```

The exact certificates are

```text
ord_q(2)=364,
2^364 == 1 (mod q^2),
2^260 == 3 (mod q),
2^260 == 1023051 (mod q^2).
```

Therefore

```text
X == 0       (mod q),
X == 1023048 (mod q^2),
1023048=936*q,
```

so

```text
q divides X exactly once.                              (1)
```

## 2. The orbit leaves `1`

Since

```text
X+1=2^260-2=2*(2^259-1),
```

the first accelerated step is

```text
C_X(1)=2^259-1
      =926336713898529563388567880069503262826159877325124512315660672063305037119487,
```

which is not `1`.

## 3. No later return to `1`

Suppose that a positive odd integer `y` maps directly to `1`.  Then

```text
X*y+1=2^a                                             (2)
```

for some positive integer `a`.  Reducing (2) modulo `q` gives

```text
2^a==1 (mod q).
```

Because `ord_q(2)=364`, write `a=364*k`.  The Wieferich congruence then gives

```text
2^a==1 (mod q^2).
```

Thus `q^2` divides `X*y`.  By (1), `q` must divide `y`.

On the other hand, every accelerated output is coprime to `q`: for every odd
positive `z`,

```text
X*z+1==1 (mod q),
```

and division by a power of two cannot introduce the odd factor `q`.

Every orbit value after the starting value is an accelerated output.  Hence no
later orbit value can be a direct predecessor of `1`.  Since the first value is
not `1`,

```text
C_X^t(1) != 1 for every t>=1.                         (3)
```

This closes the no-return gate for this explicit candidate.

## 4. Elementary cycle barrier

Assume that a positive accelerated cycle of length `p` exists, with exact
valuation total `A`.  Multiplying its cycle equations gives

```text
2^A=product_i (X+1/n_i).                              (4)
```

Every factor in (4) is strictly smaller than

```text
X+1=B-2<B.
```

Therefore

```text
A<260*p.
```

Set the positive integer

```text
D=260*p-A>=1.                                         (5)
```

Equation (4) also gives `2^A>X^p`, so

```text
D < p*log2(B/X)
  = p*log2(1+3/X).                                    (6)
```

Use the standard strict inequalities

```text
ln(1+y)<y  for y>0,
ln(2)>2/3.
```

Then

```text
log2(1+3/X)<9/(2*X).
```

Combining with (6),

```text
D<9*p/(2*X).                                          (7)
```

If

```text
p<=floor(2*X/9),
```

then (7) gives `D<1`, contradicting (5).  Consequently every positive cycle
must have length greater than

```text
411705206177124250394919057808668116811626612144499783251404743139246683164216.
```

Thus all positive cycles through approximately `4.117*10^77` accelerated odd
steps are rigorously excluded.

## 5. Near-power structure

The candidate also belongs to the exact family

```text
X=2^m-d,
m=260,
d=3.
```

Therefore the near-power exceptional-descent theorem applies with

```text
r=v2(3*n-1).
```

All steps split into the exact cases recorded in

```text
docs/NEAR_POWER_EXCEPTIONAL_DESCENT.md.
```

This gives a structured route for attacking cycles beyond the finite barrier,
rather than treating the huge candidate as a black-box trajectory.

## 6. Current dichotomy

By positivity and discreteness, the orbit from `1` either tends to positive
infinity or eventually enters a positive cycle.  Sections 3--4 prove the
strict alternative

```text
the orbit tends to +infinity,
or it enters a nontrivial positive cycle longer than
411705206177124250394919057808668116811626612144499783251404743139246683164216.
```

The second alternative remains open and must not be omitted.

Independent checker:

```text
python tools/verify_hybrid_wieferich_near_power_candidate.py
```
