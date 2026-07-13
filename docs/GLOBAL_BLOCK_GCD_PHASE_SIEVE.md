# Global common-boundary divisor and phase sieve

Date: 2026-07-13

## Scope

Let

```text
B=2^m,
X=B-d,
```

where `m>=3`, `d` is positive odd, and `X>=5`. Consider a positive accelerated
cycle for `Xn+1`. Decompose its cyclic valuation word into complete near-power
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

Let `b_i` be the cycle values at complete-block boundaries.

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

### Proof

The exact complete-block identity is

```text
2^(m*ell_i-c_i)*b_(i+1)=X^ell_i*b_i+S_(ell_i).      (4)
```

Since `h|ell_i`, strong divisibility gives `S_h|S_(ell_i)`, and
`B^ell_i==X^ell_i (mod S_h)`. Reducing (4) modulo `S_h` gives

```text
b_(i+1)==2^c_i*b_i (mod S_h).                        (5)
```

Thus `gcd(b_i,S_h)` is independent of `i`; call it `g0`. It divides every
boundary, so `g0|g`. Conversely, every common divisor of consecutive boundaries
divides `S_(ell_i)` by (4), hence `g|S_h`. Therefore `g|g0`, proving (1).

Multiplying (5) around the cycle gives

```text
(2^D-1)*b_i==0 (mod S_h).
```

Writing `b_i=g*u` and `S_h=g*v`, equation (1) gives `gcd(u,v)=1`, so
`v|2^D-1`. This proves (2)--(3).

## Theorem 2: endogenous phase sieve

Every cycle state at accelerated index `t` after a chosen block boundary obeys

```text
n_t==B^(-j)*S_j (mod g),
j=t mod h.                                             (6)
```

Therefore the entire cycle lies in at most `h` explicit residue classes modulo
the endogenous modulus `g`.

### Proof

Every complete-block length is a multiple of `h`. Starting from a boundary
divisible by `g`, each complete group of `h` accelerated steps has affine
constant `S_h`. Hence every phase-zero state is divisible by `g`. For the next
`j<h` steps all valuations are `m`, and

```text
B^j*n_t=X^j*n_(t-j)+S_j.
```

Reduction modulo `g` gives (6).

This is genuinely global. A finite CRT construction can force a prime through
any prescribed finite block list, but it does not supply the cycle-closing
relation (2) or the phase sieve (6).

## Regression: the one-block 5n+1 cycle

For

```text
B=8,
X=5,
cycle 43 -> 27 -> 17 -> 43,
valuation word (3,3,1),
```

there is one complete block of length `h=3` and total credit `D=2`. Here

```text
S_3=129,
g=43,
S_3/g=3 divides 2^2-1.
```

The phase residues modulo `43` are exactly

```text
0, 27, 17.
```

## Primary specialization: even h

For the retained candidate

```text
m=4501,
B=2^4501,
d=349*2^500-347,
X=B-d,
S_2=B+X,
```

and a nonpositive minimum-boundary return,

```text
1<=D<=4500.
```

The exact finite certificate verifies

```text
gcd(S_2,2^D-1)=1 for every 1<=D<=4500.             (7)
```

If `h` is even, then `S_2|S_h`; equations (2) and (7) force `S_2|g`. The phase
sieve reduces the cycle to two odd residue classes modulo `2*S_2`. Exact
harmonic packing and the retained continued-fraction gap prove

```text
full cycle p>2^(2^4979),
actual return L_return>2^(2^4978).                  (8)
```

## Follow-up specialization: odd h>=3

The companion theorem

```text
docs/ODD_H_PHASE_HARMONIC_BARRIER.md
```

uses the same global divisor and phase sieve. Since

```text
S_h>h*X^(h-1),
```

equation (3) gives

```text
g/h>X^2/2^4500.
```

Phase-wise harmonic packing then proves exactly the same conditional frontier
(8) for every odd `h>=3`. Therefore every nonpositive-return cycle with `h>=2`
satisfies (8). The only nonpositive branch not covered by a common geometric
divisor frontier is `h=1`.

For every nonpositive-return cycle with `h>=2`, all complete-block boundaries
also share a divisor greater than `2^4500`, coprime to
`(2^500-1)*1093^2`.

## Strategic consequence

The surviving branches are

```text
positive credit: L_return>2^3990;
nonpositive, h>=2: L_return>2^(2^4978), not excluded;
nonpositive, h=1: only the general L_return>2^(2^974) barrier applies.
```

The next useful target is to prove that the actual minimum-boundary return cannot
have `h=1`, or to obtain a length-independent adjacent-numerator gcd
contradiction for `h>=2`. The strict prize problem remains open.

## Verification

Run

```text
python tools/verify_global_block_gcd_phase_sieve.py
python tools/verify_odd_h_phase_harmonic_barrier.py
```

The first checker verifies all `4500` gcds in (7), the inverse residue and exact
even-phase harmonic inequality, three independently generated small cycles, the
global-divisor and phase-sieve identities, and the explicit `43 -> 27 -> 17`
regression. The second verifies the odd-phase harmonic frontier and its exact
primary inequality.
