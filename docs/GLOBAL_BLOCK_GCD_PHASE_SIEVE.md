# Global common-boundary divisor and phase sieve

Date: 2026-07-13

## Scope

Let

```text
B=2^m,
X=B-d,
```

where `m>=3`, `d` is positive odd, and `X>=5`.  Consider a positive accelerated
cycle for `Xn+1`.  Decompose its cyclic valuation word into complete near-power
blocks

```text
W_i=(m,...,m,a_i),  a_i!=m.
```

Write

```text
ell_i = length of W_i,
c_i   = m-a_i,
D     = sum_i c_i,
h     = gcd_i ell_i,
S_j   = (B^j-X^j)/d.
```

Let `b_i` be the cycle values at complete-block boundaries, so that block `i`
runs from `b_i` to `b_(i+1)`.

## Theorem 1: global common-boundary divisor

Put

```text
g=gcd_i b_i.
```

Then for every boundary `b_i`,

```text
g=gcd(b_i,S_h),                                      (1)
S_h/g divides 2^D-1.                                 (2)
```

Equivalently,

```text
S_h/gcd(S_h,2^D-1) divides g divides S_h.            (3)
```

Thus a common divisor of all block lengths forces a common divisor of all block
boundaries unless the complementary part of `S_h` is absorbed by `2^D-1`.

### Proof

The exact complete-block identity is

```text
2^(m*ell_i-c_i)*b_(i+1)=X^ell_i*b_i+S_(ell_i).      (4)
```

Since `h|ell_i`, strong divisibility gives `S_h|S_(ell_i)`, and
`B^ell_i==X^ell_i (mod S_h)`.  All powers of two are units modulo the odd number
`S_h`.  Reducing (4) modulo `S_h` therefore gives

```text
b_(i+1)==2^c_i*b_i (mod S_h),                        (5)
```

where a negative exponent means the corresponding inverse power of two.
Consequently `gcd(b_i,S_h)` is independent of `i`.  Call this common value `g0`.
It divides every boundary, so `g0|g`.

Conversely, every common divisor of `b_i,b_(i+1)` divides `S_(ell_i)` by (4).
Hence `g` divides every `S_(ell_i)`, and strong divisibility gives `g|S_h`.
Since `g|b_i`, this implies `g|gcd(b_i,S_h)=g0`.  Thus `g=g0`, proving (1).

Multiplying the congruences (5) around the cycle gives

```text
(2^D-1)*b_i==0 (mod S_h).                            (6)
```

Write `b_i=g*u` and `S_h=g*v`.  Equation (1) gives `gcd(u,v)=1`, so (6) implies
`v|2^D-1`.  This is (2), and (3) follows prime by prime.

## Theorem 2: endogenous phase sieve

Every cycle state at accelerated index `t` after a chosen block boundary obeys

```text
n_t == B^(-j)*S_j (mod g),
j=t mod h,                                             (7)
```

with `S_0=0`.  Therefore the entire cycle lies in at most `h` explicit residue
classes modulo the endogenous modulus `g`.

### Proof

Every complete-block length is a multiple of `h`.  Starting from a boundary
divisible by `g`, each complete group of `h` accelerated steps has affine
constant `S_h`, whether its last valuation is `m` or is the terminal valuation
of a complete block.  Since `g|S_h`, every phase-zero state is divisible by `g`.
For the next `j<h` steps all valuations are `m`, and the exact identity is

```text
B^j*n_t=X^j*n_(t-j)+S_j.
```

Reduction modulo `g` gives (7).

This is genuinely global.  The previous finite CRT construction can force a
prime through any prescribed finite block list, but it does not supply the
cycle-closing relation (2) or the phase sieve (7).

## Regression: the one-block `5n+1` cycle

For

```text
B=8,
X=5,
cycle 43 -> 27 -> 17 -> 43,
valuation word (3,3,1),
```

there is one complete block of length `h=3` and total credit `D=2`.  Here

```text
S_3=129,
g=43,
S_3/g=3 divides 2^2-1.
```

The phase residues modulo `43` are exactly

```text
0, 27, 17,
```

which are the three cycle states in boundary order.

## Primary specialization: even block-length gcd

Now use the retained candidate

```text
m=4501,
B=2^4501,
d=349*2^500-347,
X=B-d,
S_2=B+X.
```

On the nonpositive-return branch, the total cycle credit satisfies

```text
1<=D<=4500.                                           (8)
```

The exact finite certificate verifies

```text
gcd(S_2,2^D-1)=1  for every 1<=D<=4500.             (9)
```

If `h` is even, then `S_2|S_h`.  Equations (2) and (9) force

```text
S_2|g.                                                (10)
```

Thus, after indexing from a block boundary, every even-index cycle state is
`0 mod S_2`.  Every even-to-odd transition has valuation `m`, so every odd-index
state is

```text
rho=B^(-1) (mod S_2).                                (11)
```

The least positive odd representative `rho` satisfies, by exact integer
calculation,

```text
S_2/2<rho<S_2.                                       (12)
```

Hence the full cycle lies in two extremely sparse odd residue classes modulo
`2*S_2`.

## Conditional cycle and return frontier

Let `p` be the full accelerated cycle length and `q=p/2`.  The `q` even-phase
values are distinct odd multiples of `S_2`; the `q` odd-phase values are distinct
numbers `rho mod 2*S_2`.  Therefore

```text
sum_cycle 1/n
 < 1/S_2 + 1/rho + H_(q-1)/S_2
 < (4+ln p)/S_2.                                    (13)
```

For `1<=D<=4500`, the retained one-sided continued-fraction certificate and the
exact product identity give

```text
2^-4023
 < sum_cycle ln(1+1/(X*n))
 < (1/X)*sum_cycle 1/n.                              (14)
```

If

```text
p<=2^(2^4979),
```

then `ln p<2^4979`.  The checker verifies the exact integer inequality

```text
(2^4979+4)*2^4023 < X*S_2.                           (15)
```

Equations (13)--(15) contradict each other.  Therefore every hypothetical
nonpositive-return cycle whose complete-block lengths have even gcd satisfies

```text
p>2^(2^4979).                                        (16)
```

The actual minimum-boundary expanding exit has length `L_exit` satisfying
`L_exit*log2(B/X)<4500`.  Since

```text
d>2^508,
log2(B/X)>d/B>2^-3993,
4500<2^13,
```

one has

```text
L_exit<2^4006.                                       (17)
```

Consequently its remaining actual return satisfies the simpler strict frontier

```text
L_return>2^(2^4978).                                 (18)
```

This improves the retained `2^(2^974)` nonpositive-return frontier on the entire
even-`h` subcase.  It does not exclude an even-`h` cycle of still greater length.

## Further primary consequence

For every nonpositive-return cycle with `h>=2`, all block boundaries have a
common divisor greater than `2^4500`:

- if `h` is even, (10) gives `g>=S_2>B=2^4501`;
- if `h` is odd, then `h>=3`, and (3), `D<=4500`, and `S_h>X^(h-1)` give

```text
g>S_h/2^D>X^2/2^4500>2^4500.
```

This common divisor is coprime to the permanent-sieve modulus
`(2^500-1)*1093^2`, because it divides `S_h`.

## Strategic consequence

The nonpositive-return branch now splits further:

```text
h even:
  return length >2^(2^4978);

h odd and h>=3:
  every complete-block boundary shares a divisor >2^4500,
  and the whole cycle obeys an h-phase residue sieve modulo that divisor;

h=1:
  no common geometric divisor is forced.
```

The next useful target is the odd-`h` phase sieve.  One should either obtain a
harmonic-packing bound from its explicit residues, or prove that the actual
minimum-boundary return forces `h=1`.  Merely extending a local CRT construction
cannot address (2).

## Verification

Run

```text
python tools/verify_global_block_gcd_phase_sieve.py
```

The standalone checker verifies:

```text
all 4500 gcds in (9);
the inverse residue and inequality (12);
the exact harmonic contradiction (15);
the exit-length exponent bounds;
three independently generated small near-power cycles;
the complete global-divisor and phase-sieve identities on those cycles;
the explicit 43 -> 27 -> 17 regression.
```

The strict prize problem remains open.
