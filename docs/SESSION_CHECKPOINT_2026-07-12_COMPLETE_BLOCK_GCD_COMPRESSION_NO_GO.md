# Session checkpoint: complete-block gcd compression no-go

Date: 2026-07-12

The strict prize problem remains open. The primary candidate remains

```text
X=2^4501-349*2^500+347,
n0=1.
```

The exact cyclic-rotation closure criterion remains

```text
gcd(Q_k,Q_(k+1))=Delta
```

for adjacent accelerated numerators, where `Delta=2^A-X^p`.

## New exact complete-block theorem

For a near-power multiplier

```text
B=2^m,
X=B-d,
```

a complete block of length `ell` has word

```text
W=(m,...,m,a),  a!=m,
```

and universal affine constant

```text
S_ell=(B^ell-X^ell)/d.
```

Every exact block from `n` to `n'` satisfies

```text
2^A_W*n'=X^ell*n+S_ell,
gcd(n,n')=gcd(n,S_ell).
```

For cyclic numerators at the two block boundaries,

```text
2^A_W*Q_j=X^ell*Q_i+Delta*S_ell,
gcd(Q_i,Q_j)=gcd(Q_i,Delta*S_ell).
```

If the full word closes, then

```text
gcd(Q_i,Q_j)=Delta*gcd(n_i,S_ell).
```

Thus the sharp adjacent gcd does not survive naive complete-block compression.

## New strict local no-go

Exact word coding fixes one odd source class modulo `2^(A_W+1)`. Since `S_ell`
is odd, CRT can simultaneously impose `S_ell|n`. Therefore, for every complete
block length, infinitely many exact positive blocks satisfy

```text
gcd(n,n')=S_ell.
```

For `ell>=2`,

```text
S_ell>X^(ell-1),
```

so the extra block-boundary gcd can grow exponentially with the block length.

Regression:

```text
X=5,
W=(3,1),
91 -> 57 -> 143,
gcd(91,143)=13=(8^2-5^2)/3.
```

Consequently the proposed proof architecture

```text
compress every complete block to one edge
and force boundary gcd=Delta from local block data
```

is closed. A successful cyclic-gcd proof must retain an adjacent accelerated
pair inside the block or prove a genuinely global coprimality condition
`gcd(n_i,S_ell)=1` for the actual cycle source.

## Verification

The standalone exact checker passed:

```text
exact block lifts checked=13212;
full geometric-factor CRT blocks checked=3303;
cyclic compression cases checked=7056;
closing cyclic cases checked=8;
regression=91 -> 57 -> 143 with gcd 13.
```

Files:

```text
docs/COMPLETE_BLOCK_GCD_COMPRESSION_NO_GO.md
tools/verify_complete_block_gcd_compression_no_go.py
```

A complete repository-wide run was not executed.

## Next exact target

The next useful route must keep the sharp adjacent relation while exploiting the
near-power block structure. One concrete target is to select a distinguished
terminal accelerated edge in every ordinary block and derive a global bound on

```text
gcd(n_i,S_ell)
```

from the permanent sieve, minimum-boundary constraints, or the actual return
word. Replacing the block by its two boundary numerators alone is now ruled out.
