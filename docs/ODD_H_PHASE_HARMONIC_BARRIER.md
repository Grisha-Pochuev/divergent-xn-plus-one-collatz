# Odd-phase harmonic barrier for nonpositive returns

Date: 2026-07-13

## Scope

Use the primary candidate

```text
m=4501,
B=2^4501,
d=349*2^500-347,
X=B-d,
N=2^500-1.
```

Assume a hypothetical nontrivial positive accelerated cycle exists and that the
actual return from the minimum-boundary expanding exit has nonpositive credit.
Then the total cycle credit satisfies

```text
1<=D<=4500.
```

Let `ell_i` be all complete-block lengths, put

```text
h=gcd_i ell_i,
```

and assume in this note that `h` is odd and `h>=3`. Let `p` be the minimal
accelerated period and write `p=h*q`.

This note proves

```text
p>2^(2^4979)
and
L_return>2^(2^4978).
```

Thus the odd-`h>=3` branch reaches the same conditional length frontier as the
previous even-`h` branch. This is not a cycle exclusion and therefore is not yet
a proof of divergence.

## 1. Divisor size per phase

Let

```text
S_h=(B^h-X^h)/d
```

and let `g` be the gcd of all complete-block boundaries. The global block-gcd
theorem gives

```text
S_h/g divides 2^D-1,
```

hence

```text
g>=S_h/gcd(S_h,2^D-1)>S_h/2^D.                    (1)
```

Also

```text
S_h=sum_(k=0)^(h-1) B^(h-1-k)*X^k.
```

Because `B>X`, every summand is at least `X^(h-1)` and at least one is strictly
larger. Therefore

```text
S_h>h*X^(h-1).                                      (2)
```

Combining (1), (2), `D<=4500`, and `h>=3` gives

```text
g/h>X^(h-1)/2^D>=X^2/2^4500.                       (3)
```

The factor `h` in (2) is decisive: it prevents the number of phase classes from
weakening the harmonic estimate.

## 2. The number of phases is bounded by the actual exit

The actual minimum-boundary exit contains at least its terminal ordinary
complete block. Every complete-block length is divisible by `h`. Its total
accelerated length satisfies

```text
L_exit<2^4006.
```

Consequently

```text
h<=ell_terminal<=L_exit<2^4006.                     (4)
```

This uses an actual block in the hypothetical cycle, not an admissible local
word.

## 3. Harmonic packing inside the phase classes

The phase sieve says that, after indexing from a complete-block boundary,

```text
n_t==B^(-j)*S_j (mod g),
j=t mod h.
```

For each phase `j`, let `P_j` be the `q` cycle states whose indices are congruent
to `j mod h`, and let

```text
u_j=min P_j.
```

The period `p` is minimal, so all cycle states are distinct. Within one phase all
states are odd and congruent modulo the odd number `g`. Therefore two distinct
states in that phase differ by at least `2*g`. Sorting the phase gives

```text
sum_(n in P_j) 1/n
 <=1/u_j+H_(q-1)/(2*g).                              (5)
```

The `h` numbers `u_j` are distinct odd cycle values and every cycle value is
greater than `N`. Hence, after sorting the minima,

```text
sum_j 1/u_j
 <=sum_(r=1)^h 1/(N+2*r)
 <(1/2)*ln(1+2*h/N).                                 (6)
```

Using (4), `N>2^499`, and `ln(2)<1`,

```text
1+2*h/N<2^3509
```

and therefore

```text
sum_j 1/u_j<3509/2<2^11.                             (7)
```

Summing (5) over all phases yields

```text
sum_cycle 1/n<2^11+h*H_(q-1)/(2*g).                 (8)
```

## 4. Conditional full-cycle contradiction

Assume for contradiction that

```text
p<=2^(2^4979).                                       (9)
```

Since `q<=p`,

```text
H_(q-1)<1+ln(p)<2^4980.                              (10)
```

Equations (3), (8), and (10) give

```text
sum_cycle 1/n
 <2^11+h*2^4980/(2*g)
 <2^11+2^9479/X^2.                                  (11)
```

On the nonpositive-return branch, the retained one-sided continued-fraction gap
and exact product identity give

```text
2^-4023
 <sum_cycle ln(1+1/(X*n))
 <(1/X)*sum_cycle 1/n.                               (12)
```

Thus any such cycle must satisfy

```text
sum_cycle 1/n>X/2^4023.                              (13)
```

The standalone checker verifies the exact integer inequality

```text
2^11+2^9479/X^2<X/2^4023,                            (14)
```

which is equivalent to

```text
2^4034*X^2+2^13502<X^3.
```

Equations (11), (13), and (14) contradict each other. Therefore

```text
p>2^(2^4979).                                        (15)
```

## 5. Actual return frontier

The full cycle is the actual exit followed by the actual return. Since

```text
L_exit<2^4006
```

and the full period satisfies (15), the return obeys

```text
L_return>2^(2^4978).                                 (16)
```

Together with the even-`h` theorem, every hypothetical nonpositive-return cycle
with `h>=2` now satisfies the same bounds (15)--(16).

The remaining nonpositive branch not covered by the global geometric divisor is

```text
h=1.
```

## 6. Limitations and next target

This theorem gives a much larger finite frontier, not an exclusion of cycles.
The strict prize problem remains open. The useful remaining targets are:

1. prove that `h=1` is incompatible with the actual minimum-boundary return;
2. find a length-independent adjacent-numerator gcd obstruction for `h>=2`;
3. exclude the positive-credit return branch.

A larger finite trajectory or a larger finite cycle cutoff would not address
these targets.

## 7. Verification

Run

```text
python tools/verify_odd_h_phase_harmonic_barrier.py
```

The checker verifies:

```text
the exact primary inequality (14);
the exponent bookkeeping for (7), (10), and (11);
the return subtraction bound;
80 exact phase-spacing regressions;
the h=3 phase residues of 43 -> 27 -> 17 -> 43 for X=5.
```
