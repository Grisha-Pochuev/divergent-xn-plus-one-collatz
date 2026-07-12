# Geometric-factor strong divisibility and persistent-defect no-go

Date: 2026-07-13

## Scope

Let

```text
B=2^m,
X=B-d,
```

where `m>=3`, `d` is positive odd, and `X>=5`. For a complete near-power
block of accelerated length `ell`, define

```text
S_ell=(B^ell-X^ell)/d
     =B^(ell-1)+B^(ell-2)X+...+X^(ell-1).
```

The previous complete-block theorem gives, for an exact block from positive odd
source `n` to endpoint `n'`,

```text
2^A*n'=X^ell*n+S_ell,
gcd(n,n')=gcd(n,S_ell).
```

This note determines the arithmetic shared by the factors `S_ell` and proves a
new finite local obstruction to block-boundary gcd arguments.

## Theorem 1: strong divisibility

For all positive integers `r,s`,

```text
gcd(S_r,S_s)=S_gcd(r,s).                              (1)
```

Moreover, for every `ell>=1`,

```text
S_ell is odd,
gcd(S_ell,B*X)=1,
gcd(S_ell,d)=gcd(ell,d).                               (2)
```

### Proof

Because `B` is a power of two and `X,d` are odd,

```text
gcd(B,X)=gcd(B,d)=gcd(X,d)=1.
```

The standard difference-of-powers Euclidean identity for coprime `B,X` is

```text
gcd(B^r-X^r,B^s-X^s)=B^g-X^g,
g=gcd(r,s).
```

Since `B^j-X^j=d*S_j`, cancellation of the common positive factor `d` gives
(1).

The displayed sum for `S_ell` gives

```text
S_ell == X^(ell-1) (mod B),
S_ell == B^(ell-1) (mod X),
```

so `S_ell` is odd and coprime to `B*X`. Finally `B==X (mod d)`, hence

```text
S_ell == ell*X^(ell-1) (mod d).
```

Since `gcd(X,d)=1`, this implies `gcd(S_ell,d)=gcd(ell,d)`.

## Corollary 1: overlap of boundary defects is length-controlled

For complete blocks with lengths `ell_i`, put

```text
g_i=gcd(n_i,n_(i+1))=gcd(n_i,S_(ell_i)).
```

For every nonempty index set `I`,

```text
gcd(g_i : i in I) divides S_gcd(ell_i : i in I).      (3)
```

In particular, if the selected block lengths have gcd `1`, their boundary gcd
defects have no common prime.

If an odd prime `q` not dividing `d` divides one of these common defects, then

```text
ord_q(B*X^(-1)) divides gcd(ell_i : i in I).
```

If `q|d`, then (2) instead forces `q` to divide every selected block length.
Thus reuse of a defect prime imposes a precise divisibility condition on the
block lengths.

## Theorem 2: persistent defect primes are locally realizable

Let `ell_1,...,ell_t` be any finite list of positive complete-block lengths with

```text
h=gcd(ell_1,...,ell_t)>=2.
```

Choose arbitrary positive terminal valuations `a_i!=m`, and let the concatenated
exact valuation word be

```text
W=(m,...,m,a_1)(m,...,m,a_2)...(m,...,m,a_t),
```

where block `i` has length `ell_i`. Let `q` be any odd prime divisor of `S_h`.
Then there are infinitely many positive odd starts whose exact valuation word is
`W` and for which `q` divides every block boundary:

```text
q|n_0,n_1,...,n_t.                                    (4)
```

Consequently,

```text
q|gcd(n_(i-1),n_i)
```

for every block in the list.

### Proof

Finite exact valuation-word coding fixes one odd source class

```text
n_0==c (mod 2^(sum(W)+1)).
```

By (1), `S_h|S_(ell_i)` for every `i`, so `q|S_(ell_i)`. The odd moduli `q` and
`2^(sum(W)+1)` are coprime. The Chinese remainder theorem therefore gives
infinitely many positive odd solutions of

```text
n_0==c (mod 2^(sum(W)+1)),
n_0==0 (mod q).
```

The first congruence realizes `W` exactly. If `q|n_(i-1)`, the complete-block
equation

```text
2^A_i*n_i=X^(ell_i)*n_(i-1)+S_(ell_i)
```

has right side divisible by `q`. Since `q` is odd, `q|n_i`. Induction proves
(4).

## Explicit regression

For

```text
B=8,
X=5,
d=3,
lengths=(2,4,6),
terminal valuations=(1,2,1),
h=2,
q=13|S_2,
```

the exact CRT construction gives

```text
n_0=2620090395,
```

and block boundaries

```text
2620090395,
4093891243,
1249356459,
297869793.
```

All four are divisible by `13`. The three block-boundary gcd defects are

```text
13, 13, 39.
```

Thus the same prime can survive through several consecutive complete-block
compressions in a non-cyclic finite segment.

## Primary-candidate specialization

For the retained candidate

```text
N=2^500-1,
B=2^4501,
d=349*2^500-347,
X=B-d,
1093||X,
```

(2) gives

```text
gcd(S_ell,N*1093^2)=1                                (5)
```

for every `ell`, because both `N` and `1093` divide `X`. More explicitly,

```text
S_ell == 2^(ell-1)          (mod N),
S_ell == B^(ell-1)          (mod 1093).
```

Therefore a block-boundary defect factor is automatically supported outside the
prime support of the permanent sieve modulus `N*1093^2`. The permanent sieve
may still constrain the actual source residue, but it cannot eliminate the
extra geometric gcd by claiming that `S_ell` contains one of the sieve primes.

## Strategic consequence

The new result closes the following local proof shortcut:

```text
a nontrivial gcd defect cannot persist through many complete blocks,
so repeated block compression eventually recovers adjacent coprimality.
```

That statement is false without genuinely global cycle information. Whenever
the selected block lengths have a common divisor greater than one, exact word
coding and CRT produce arbitrarily long finite block lists with one prime at
every boundary.

A surviving global gcd route must therefore prove at least one of:

1. a strategically selected set of actual cycle block lengths has gcd `1`;
2. every prime allowed by `S_gcd(lengths)` is excluded from the corresponding
   actual cycle boundaries by the return word, minimum boundary, or permanent
   sieve;
3. a truly adjacent accelerated pair is retained instead of complete-block
   boundary compression.

The theorem does not exclude a global argument of these types and does not
prove divergence.

## Verification

Run

```text
python tools/verify_geometric_factor_strong_divisibility.py
```

The standalone checker verifies:

```text
71136 strong-divisibility pair cases;
1990 exact complete blocks;
116 persistent-boundary CRT constructions;
24 primary-candidate lengths;
the explicit X=5 three-block regression above.
```

The proof is elementary and self-contained. The terminology “strong
divisibility sequence” is standard for Lucas-type sequences; no external
literature result is used as an unverified dependency.
