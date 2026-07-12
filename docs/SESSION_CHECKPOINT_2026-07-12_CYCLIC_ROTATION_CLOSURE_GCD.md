# Session checkpoint: cyclic-rotation closure gcd criterion

Date: 2026-07-12

The strict prize problem remains open. The primary candidate remains

```text
X=2^4501-349*2^500+347,
n0=1.
```

## Retained frontiers

For the actual return from the larger endpoint of the minimum-boundary expanding
segment back to the least ordinary boundary:

```text
positive return credit    => length >2^3990;
nonpositive return credit => length >2^(2^974).
```

The full finite two-sided endpoint-congruence route remains closed by
`FULL_FINITE_TWO_SIDED_WORD_GLUING_NO_GO`: local CRT compatibility does not imply
exact cycle closure.

## New strict theorem

For a complete positive valuation word

```text
U=(a_0,...,a_(p-1)),
A=sum_i a_i,
Delta=2^A-X^p,
```

let `Q_k` be the standard affine numerator of the cyclic rotation beginning at
`a_k`. Then

```text
2^a_k*Q_(k+1)=X*Q_k+Delta,

gcd(Q_0,...,Q_(p-1))=gcd(Q_0,Delta),

gcd(Q_k,Q_(k+1))=gcd(Q_k,Delta).
```

The word closes to an actual positive accelerated cycle if and only if

```text
Delta>0 and Delta|Q_0.
```

Equivalently, exact closure is

```text
gcd(Q_k,Q_(k+1))=Delta
```

for one, hence every, adjacent pair of cyclic numerators. If closure holds, the
cycle states are exactly

```text
n_k=Q_k/Delta.
```

Thus minimum-boundary comparisons transfer without loss to comparisons among
the `Q_k`. For the already proved actual expanding exit, the numerator at the
next ordinary boundary is strictly larger than that at the least ordinary
boundary.

## Relation to the previous closure equation

For a split `U=W followed by V`, exact concatenation gives

```text
Q(U)=X^r*Q_W+2^A_W*Q_V.
```

Therefore the previous equation

```text
[2^(A_W+A_V)-X^(t+r)]*x
  =X^r*Q_W+2^A_W*Q_V
```

is exactly `Delta*x=Q(U)`. The new theorem does not merely restate local endpoint
congruences: it identifies the missing global condition as a maximal common gcd
across cyclic rotations.

## Alternative routes checked

The committed audits of the Santos Mersenne-cycle claim and the Tremblay `5x+1`
divergence claim remain decisive; neither supplies a usable theorem. The retained
dual-Wieferich alternative candidate has a much thinner finite sieve but still
faces the same global cycle-exclusion gate. The exact closure route was therefore
the best current target.

## Verification

The standalone checker passed and reports:

```text
exhaustive small words checked=6820;
closing words reconstructed=17;
known 5n+1 cycles checked=3;
primary-multiplier large word checks=3.
```

It verifies the rotation recurrence, concatenation identity, full and adjacent
gcd identities, exact reconstruction of every closing word found in the grid,
and three large-word identities for the primary enormous multiplier.

Files:

```text
docs/CYCLIC_ROTATION_CLOSURE_GCD.md
tools/verify_cyclic_rotation_closure_gcd.py
```

## Remaining obstruction

The new exact target is to prove that every admissible complete cyclic word under
the minimum-boundary, block-credit, and return-length constraints has at least
one adjacent pair satisfying

```text
gcd(Q_k,Q_(k+1))<Delta.
```

A promising next exact experiment is a complete-block Euclidean-remainder
recurrence: compute or bound the adjacent numerator gcd without materializing an
astronomically long full word. A fixed residue modulus or a longer finite
trajectory cannot prove this condition.
