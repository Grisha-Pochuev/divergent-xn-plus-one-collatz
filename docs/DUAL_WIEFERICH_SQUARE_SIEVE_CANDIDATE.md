# Dual-Wieferich square-sieve candidate `X=2^3803-4162203`

This note gives a new explicit candidate for the strict accelerated `Xn+1`
problem. It combines the two known base-2 Wieferich primes in different roles:

1. `3511^2` divides the multiplier and gives a one-label permanent sieve;
2. `1093` divides the multiplier exactly once and forbids return to `1`;
3. the `1093^2` adjacent-label coordinate combines with the square sieve;
4. the near-power form gives a cycle barrier and an exceptional-source floor.

Put

```text
m=3803,
B=2^3803,
d=4162203,
X=B-d,
n0=1.
```

The strict prize problem remains open: cycles above the finite barrier are not
yet excluded. The point of this candidate is that its permanent residue density
is much smaller than for the former primary candidate `X=2^156-9`.

## 1. Exact arithmetic of the two Wieferich divisors

For `q=3511`,

```text
ord_q(2)=ord_(q^2)(2)=1755,
2^3803 == 4162203 (mod q^2).
```

Moreover

```text
v_q(X)=2,
X/q^2 == 1526 (mod q).
```

Thus

```text
3511^2 | X,
3511^3 does not divide X.                           (1)
```

For `r=1093`,

```text
ord_r(2)=ord_(r^2)(2)=364,
2^3803 == 4162203 == 59 (mod r).
```

Also

```text
v_r(X)=1,
X/r == 219 (mod r).                                 (2)
```

All these statements are checked by exact modular arithmetic in the verifier.

## 2. The orbit leaves `1` and never returns

Since

```text
d-1=4162202=2*2081101,
```

we have

```text
v2(X+1)=1,
C_X(1)=(X+1)/2>1.                                  (3)
```

Every accelerated output is coprime to `1093`, because

```text
X*z+1 == 1 (mod 1093),
```

and division by a power of two cannot introduce the odd prime `1093`.

Suppose that a positive odd output `y` mapped directly to `1`. Then

```text
X*y+1=2^a.
```

Modulo `1093`, the exact order forces `364|a`. The Wieferich congruence then
implies

```text
1093^2 | 2^a-1=X*y.
```

Because `1093` divides `X` exactly once, this would force `1093|y`, contradicting
the output-coprimality statement. Hence

```text
C_X^t(1) != 1 for every t>=1.                       (4)
```

This closes the no-return gate for the new candidate.

## 3. One-label permanent sieve modulo `3511^2`

Let an accelerated transition be

```text
2^a_i*n_(i+1)=X*n_i+1.
```

By (1), reduction modulo `3511^2` gives

```text
n_(i+1) == 2^(-a_i) (mod 3511^2).                  (5)
```

Since the order of `2` modulo `3511^2` is `1755`, every orbit output belongs to
one of exactly

```text
1755
```

classes modulo

```text
3511^2=12327121.                                    (6)
```

The class is determined by the current valuation label

```text
1<=s_i<=1755,
a_i==s_i (mod 1755).
```

This is stronger than an adjacent-label sieve: no previous state or unknown
full-order layer occurs.

## 4. Combination with the `1093^2` adjacent-label coordinate

Because `1093||X`, the Wieferich adjacent-label theorem applies modulo `1093^2`.
If

```text
1<=t_i<=364,
a_i==t_i (mod 364),
c=X/1093==219 (mod 1093),
```

then

```text
n_(i+1)
 ==2^(-t_i)*(1+1093*c*2^(-t_(i-1))) (mod 1093^2).  (7)
```

The current labels in (5) and (7) come from the same integer `a_i`. Therefore
they satisfy

```text
s_i==t_i (mod gcd(1755,364)),
gcd(1755,364)=13.
```

There are exactly

```text
lcm(1755,364)=49140
```

compatible current-label pairs. The previous `1093` label has `364` choices.
The Chinese remainder theorem and the injectivity of both coordinate formulas
therefore give exactly

```text
364*49140=17886960                                  (8)
```

permanent classes modulo

```text
3511^2*1093^2=14726582775529.                       (9)
```

Their density is

```text
17886960/14726582775529
 =1.214603569...*10^(-6).                          (10)
```

For the former primary candidate `X=2^156-9`, the adjacent-label sieve retained

```text
132496/1194649=0.110907890...
```

of all classes. Thus the new combined sieve is between

```text
91312 and 91313
```

times thinner.

## 5. Elementary finite cycle barrier

Assume that a positive cycle has accelerated length `p` and total valuation
`A`. Since `d>1`, every cycle value satisfies

```text
X+1/n_i < B.
```

Therefore

```text
2^A=product_i(X+1/n_i)<B^p=2^(m*p),
D=m*p-A>=1.                                         (11)
```

On the other hand `2^A>X^p`, so

```text
D<p*log2(B/X)=p*log2(1+d/X).                        (12)
```

Using

```text
ln(1+y)<y,
ln(2)>2/3,
```

we obtain

```text
D<3*p*d/(2*X).                                      (13)
```

Together with `D>=1`, this proves

```text
p>2*X/(3*d).                                        (14)
```

Consequently every positive cycle length through

```text
floor(2*X/(3*d))
```

is impossible. This exact integer has `1139` decimal digits and is larger than

```text
10^1138.                                            (15)
```

This remains a finite barrier, not a proof of divergence.

## 6. Exceptional-source progression

For the near-power coordinates, a source begins an exceptional complete block
exactly when

```text
v2(d*n-1)=m.                                        (16)
```

Equivalently,

```text
d*n == B+1 (mod 2*B).                               (17)
```

Because `d` is odd, (17) gives one progression

```text
n=n_exc+2*B*T,
T>=0.                                               (18)
```

Writing

```text
d*n_exc-1=u0*B
```

with `u0` positive and odd, exact arithmetic gives

```text
u0=1422295.                                         (19)
```

### Square-sieve floor

Combining (18) with the `1755` classes in (5) gives an exact first compatible
layer

```text
T=2377,
s_i=1615,
n == 9391230 (mod 3511^2).
```

Thus the square sieve alone forces every exceptional cycle source to satisfy

```text
n>=(19788535357*B+1)/4162203.                       (20)
```

### Full dual-sieve floor

Now also impose the adjacent-label formula (7) and the compatibility modulo
`13`. Scanning every progression layer below the first compatible layer gives

```text
T=2350560,
3511-label s_i=40,
1093-label pair (t_(i-1),t_i)=(99,222),
n == 11331739 (mod 3511^2),
n == 820246   (mod 1093^2).                         (21)
```

No smaller `T` satisfies all permanent conditions. Hence every exceptional
source in any hypothetical positive cycle obeys the permanent lower bound

```text
n>=(19567017189655*B+1)/4162203.                    (22)
```

Compared with the raw progression floor in (19), the odd-core coefficient has
increased by a factor greater than `13,757,000`.

## 7. Why this candidate is promising

Relative to `X=2^156-9`, the new candidate has:

1. the same closed explicit-pair and no-return gates;
2. a finite cycle barrier beyond `10^1138`;
3. a one-label square-divisor sieve;
4. a combined permanent residue density about `91312` times smaller;
5. an exceptional-source floor using both permanent coordinates;
6. the same general near-power block ledger, with `m=3803,d=4162203`.

The cost is a larger block alphabet (`3802` ordinary terminal deficits). The
decisive theorem is still global: exclude every cycle above the finite barrier.
The intended next step is to rebuild the harmonic-packing and block-credit
inequalities using the much thinner class density and the height floor (22).

## 8. Verification

```text
python tools/verify_dual_wieferich_square_sieve_candidate.py
```

The verifier uses only the Python standard library. It checks the exact orders,
prime-adic valuations, class counts, density comparison, both exceptional
floors, and the elementary cycle barrier. The full exceptional minimum is
certified by scanning all smaller progression layers, not by a floating-point
estimate.
