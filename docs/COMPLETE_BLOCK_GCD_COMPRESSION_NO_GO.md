# Complete-block gcd compression and its local obstruction

Let

```text
B=2^m,
d odd,
3<=d<B/2,
X=B-d>=5.
```

Use the accelerated map

```text
C_X(n)=(X*n+1)/2^v2(X*n+1).
```

This note follows the cyclic-rotation closure-gcd theorem. It derives the exact
Euclidean recurrence across a complete near-power block and records the precise
reason why replacing adjacent accelerated numerators by complete-block boundary
numerators does not by itself exclude cycle closure.

## 1. The universal complete-block numerator

A complete block of accelerated length `ell>=1` has valuation word

```text
W=(m,m,...,m,a),
```

with `ell-1` copies of `m` and terminal valuation `a!=m`. Put

```text
A_W=m*(ell-1)+a,
c=m-a,
S_ell=(B^ell-X^ell)/d.
```

The usual affine word constant is independent of the terminal valuation:

```text
Q_W
 =X^(ell-1)+B*X^(ell-2)+...+B^(ell-1)
 =S_ell.                                             (1)
```

Thus every exact positive block from source `n` to endpoint `n'` satisfies

```text
2^A_W*n'=X^ell*n+S_ell.                              (2)
```

The same formula covers ordinary blocks (`a<m`, `c>0`) and exceptional blocks
(`a>m`, `c<0`).

## 2. Exact endpoint gcd

Since `n` is odd, every common divisor of `n` and `2^A_W*n'` is also a common
divisor of `n` and `n'`. Equation (2) therefore gives the exact identity

```text
gcd(n,n')=gcd(n,S_ell).                              (3)
```

Consequently complete-block endpoints need not be coprime. The only possible
extra common divisor is the geometric factor `S_ell`, but that factor is real
and can be very large:

```text
S_ell>X^(ell-1)  for ell>=2.                         (4)
```

## 3. Every divisor of the geometric factor is locally realizable

Exact valuation-word coding gives one odd source class

```text
n==r_W (mod 2^(A_W+1))                               (5)
```

whose positive representatives realize `W` exactly.

The number `S_ell` is odd. Therefore, for every divisor `g|S_ell`, the Chinese
remainder theorem combines (5) with

```text
n==0 (mod g).                                        (6)
```

There are infinitely many positive sources satisfying both conditions. For
each of them, (3) gives

```text
g|gcd(n,n').
```

Taking `g=S_ell` gives infinitely many exact positive complete blocks with

```text
gcd(n,n')=S_ell.                                     (7)
```

Thus the common divisor of two block boundaries can grow exponentially with
the block length even when the complete valuation word and positivity are
enforced exactly.

## 4. Regression example

Take

```text
X=5,
B=8,
d=3,
W=(3,1),
ell=2,
A_W=4,
S_ell=(8^2-5^2)/3=13.
```

The exact source class is

```text
n==27 (mod 32).
```

Combining it with `13|n` gives the least positive source `n=91`. The exact
accelerated block is

```text
91 --a=3--> 57 --a=1--> 143,
```

and

```text
gcd(91,143)=13=S_ell.
```

This is a small regression against any claim that exact complete-block
endpoints must be coprime.

## 5. Cyclic-numerator compression

Let a proposed complete cyclic word have closure coefficient

```text
Delta=2^A-X^p,
```

and let `Q_i,Q_j` be the cyclic affine numerators at the source and endpoint of
one complete block of length `ell`. Iterating the rotation recurrence across
the block gives

```text
2^A_W*Q_j=X^ell*Q_i+Delta*S_ell.                     (8)
```

Hence

```text
gcd(Q_i,Q_j)=gcd(Q_i,Delta*S_ell).                   (9)
```

If the full word really closes, so that `Q_i=Delta*n_i`, then

```text
gcd(Q_i,Q_j)=Delta*gcd(n_i,S_ell).                  (10)
```

For adjacent accelerated states the gcd is exactly `Delta`, because the local
word constant is `1`. At complete-block boundaries an additional factor from
`S_ell` is unavoidable unless one proves a new global coprimality statement.

## 6. Exact no-go conclusion

The proposed complete-block Euclidean compression is valid, but the following
proof architecture is closed:

```text
replace every long block by one boundary edge,
then try to force boundary gcd=Delta from the local block word and positivity.
```

Local exact data cannot force that equality. Every divisor of `S_ell`, including
the full exponentially large `S_ell`, occurs as an endpoint gcd on infinitely
many exact positive blocks.

This does not close the global cyclic-gcd route. It says that a successful use
of complete blocks must retain at least one of:

1. an adjacent accelerated pair inside the block;
2. a global argument proving `gcd(n_i,S_ell)=1` for the actual cycle source;
3. minimum-boundary, permanent-sieve, or return constraints that are not local
   consequences of the complete word.

Merely materializing the Euclidean algorithm at block boundaries loses exactly
the coprimality information that made the adjacent criterion sharp.

## 7. Verification

```text
python tools/verify_complete_block_gcd_compression_no_go.py
```

The checker uses exact integer arithmetic. It verifies the block numerator,
endpoint gcd identity, CRT realization of the full geometric factor, cyclic
numerator compression, and the explicit `91 -> 57 -> 143` regression.
