# Exact coding of valuation words

Fix an odd integer `X >= 5` and the accelerated map

```text
C_X(n) = (X*n+1)/2^v2(X*n+1)
```

on positive odd integers.

This note gives an exact inverse description of every finite sequence of halving counts. It separates the easy local part of the divergence problem from the genuinely global obstruction.

## 1. A finite valuation word

Let

```text
a = (a_0,...,a_(N-1)),   a_i >= 1,
A_j = a_0+...+a_(j-1),
A = A_N,
B = sum_(j=0)^(N-1) X^(N-1-j) * 2^A_j.
```

If an orbit follows this exact word, then

```text
2^A*n_N = X^N*n_0 + B.                         (1)
```

Since `n_N` must be odd, equation (1) is equivalent to

```text
X^N*n_0+B == 2^A  (mod 2^(A+1)).                (2)
```

Because `X` is odd, `X^N` is invertible modulo `2^(A+1)`.

## 2. Exact coding theorem

**Theorem.** There is exactly one residue class

```text
r(a)  (mod 2^(A+1))
```

whose positive representatives follow the exact valuation word `a`. It is

```text
r(a) == (2^A-B) * (X^N)^(-1)  (mod 2^(A+1)).    (3)
```

**Proof.** Equation (2) has exactly one solution modulo `2^(A+1)` because `X^N` is odd. It remains to prove that the resulting congruence forces every intermediate valuation exactly.

Work backwards. Equation (2) says that the final quotient in (1) is odd. Hence the last division removes exactly `a_(N-1)` powers of two. Removing that last relation gives the same odd-quotient condition for the prefix of length `N-1`. Repeating backwards proves that every prescribed valuation is exact. Conversely, any orbit following the word satisfies (1) with odd `n_N`, hence satisfies (2). QED.

Equivalently, all positive starts realizing the word are

```text
n_0 = r(a) + q*2^(A+1),
```

with integers `q` chosen so that `n_0>0`.

Thus **every finite valuation word is realized by infinitely many positive odd integers**.

## 3. Every positive-drift finite word gives genuine net growth

Put

```text
D = X^N-2^A.
```

Subtract `n_0` from (1):

```text
n_N-n_0 = (D*n_0+B)/2^A.                        (4)
```

Here `B>0`. Therefore:

**Corollary.** If

```text
A/N < log2(X),
```

or equivalently `D>0`, then every positive representative of the coding class satisfies

```text
n_N > n_0.
```

So any finite low-average word, no matter how long, has infinitely many positive starts exhibiting rigorous net growth across the whole word.

This proves that arbitrarily long finite growth is not exceptional evidence for an infinite divergent orbit: it is an automatic consequence of finite congruence coding.

## 4. Nested prefixes and the one true global obstruction

Let

```text
a_0,a_1,a_2,...
```

be an infinite sequence of positive valuations. For each prefix of length `N`, let

```text
r_N mod 2^(A_N+1)
```

be its unique coding class.

The classes are compatible:

```text
r_(N+1) == r_N  (mod 2^(A_N+1)).                 (5)
```

Therefore they define one 2-adic integer

```text
r_* in Z_2.
```

The infinite word is the valuation sequence of an ordinary nonnegative integer exactly when the least nonnegative representatives `r_N` eventually stabilize.

**Proposition.** The following are equivalent:

1. `r_*` is an ordinary nonnegative integer `n_0`;
2. for all sufficiently large `N`, the least representative `r_N` equals `n_0`;
3. one ordinary positive start follows every finite prefix of the word.

The proof is immediate because the moduli `2^(A_N+1)` tend to infinity.

Most infinite valuation words therefore describe only a 2-adic starting point, not a positive ordinary integer.

## 5. Exact reformulation of the exponential-divergence target

A sufficient and exact coding target is now:

Construct an infinite valuation word such that

```text
limsup_(N->infinity) A_N/N < log2(X),            (6)
```

and whose compatible coding residues `r_N` eventually stabilize at a positive integer `n_0`.

Then `n_0` follows the word, and the standard iterate bound gives

```text
n_N >= n_0 * X^N / 2^A_N,
```

so the orbit grows exponentially.

This is not yet a solution, but it identifies the missing step without ambiguity:

- finite positive-drift words are always realizable;
- compatible infinite words always determine a 2-adic start;
- the hard part is forcing that 2-adic start to be an ordinary positive integer while keeping positive average drift.

## 6. Computational consequence

Search should not rank candidates merely by the length or gain of a finite trajectory. For each growing prefix it should also track

```text
r_N = (2^A_N-B_N) * (X^N)^(-1) mod 2^(A_N+1).
```

A possible route to a proof would exhibit an aperiodic low-average word for which these residues stop changing. A negative result can instead quantify how new high bits are forced to appear, proving that a proposed regenerative scheme converges only to a nonintegral 2-adic start.
