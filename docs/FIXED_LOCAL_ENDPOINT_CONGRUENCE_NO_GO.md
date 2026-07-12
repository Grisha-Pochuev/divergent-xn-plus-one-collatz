# Fixed local endpoint congruences cannot obstruct a return

Use a general near-power multiplier

```text
B=2^m,
d odd,
1<=d<B/2,
X=B-d.
```

This note closes one local version of the remaining endpoint-congruence route.
It proves that a fixed incoming complete block and a fixed finite outgoing
valuation prefix are always compatible at infinitely many positive odd boundary
values. In particular, comparing only finitely many local labels modulo `X^2`
or any other fixed power `X^h` cannot by itself exclude a return.

The theorem does **not** rule out a global argument using the whole return word,
a depth growing with the return length, exact cycle closure, or minimum-height
information.

## 1. Exact coding of a finite outgoing word

Fix a finite positive valuation word

```text
W=(a_0,...,a_(t-1)),
A=sum_i a_i.
```

The accelerated recurrence gives

```text
2^A*n_t=X^t*n_0+Q_W,
Q_W=sum_(j=0)^(t-1) X^(t-1-j)*2^(a_0+...+a_(j-1)).
```

Requiring the endpoint `n_t` to be odd is equivalent to

```text
X^t*n_0+Q_W==2^A (mod 2^(A+1)).
```

Since `X` is odd, this determines one odd residue class

```text
n_0==r_W (mod 2^(A+1)).                            (1)
```

Every positive representative of (1) has exact successive valuations `W`.
This is the finite valuation-word coding already used elsewhere in the project.

## 2. Actual ordinary incoming block

Fix an ordinary complete block of length `ell>=1` and deficit

```text
1<=e<=m-1.
```

Its terminal valuation word is

```text
m,...,m,m-e
```

with `ell-1` copies of `m`. If its odd core is `u`, its endpoint `x` satisfies

```text
d*x-2^e=X^ell*u.                                    (2)
```

Thus every such endpoint lies in the class

```text
x==2^e*d^(-1) (mod X^ell).                           (3)
```

Conversely, choose `x` simultaneously from (1) and (3). The moduli
`2^(A+1)` and `X^ell` are coprime, so the Chinese remainder theorem gives one
class modulo their product and therefore infinitely many positive odd choices.
Choose one large enough that `d*x>2^e` and put

```text
u=(d*x-2^e)/X^ell.
```

The integer `u` is positive and odd. Define

```text
n=(B^ell*u/2^e+1)/d.                                 (4)
```

Because `B==X (mod d)`, equation (2) implies that (4) is an integer. Moreover

```text
d*n-1=B^ell*u/2^e,
```

so

```text
v2(d*n-1)=m*ell-e=m*(ell-1)+(m-e).
```

Therefore `n` starts an actual ordinary complete block of length `ell` and
deficit `e`, its endpoint is exactly `x`, and the forward orbit from `x` begins
with the prescribed word `W`.

## 3. Actual exceptional incoming block

Fix an exceptional complete block of length `ell>=1` and excess `b>=1`. Its
endpoint `x` satisfies

```text
d*2^b*x-1=X^ell*u.                                   (5)
```

Choose `x` simultaneously from (1) and

```text
x==(d*2^b)^(-1) (mod X^ell).                          (6)
```

Again CRT gives infinitely many positive odd choices. Put

```text
u=(d*2^b*x-1)/X^ell,
n=(B^ell*u+1)/d.
```

Then `u` and `n` are positive odd integers,

```text
d*n-1=B^ell*u,
X^ell*u+1=d*2^b*x,
```

and hence the block valuations are

```text
m,...,m,m+b.
```

Thus this is an actual exceptional complete block of length `ell` and excess
`b`, ending at `x`, followed by the prescribed exact word `W`.

## 4. The no-go theorem

For every finite outgoing valuation word `W` and every fixed incoming complete
block of either type, there exist infinitely many positive odd boundary values
which realize both pieces exactly.

Consequently no contradiction can be obtained solely from:

1. finitely many labels in the incoming final block;
2. finitely many labels in the outgoing exit prefix; and
3. the residue of their common endpoint modulo `X^2` or any fixed `X^h`.

This remains true after imposing any fixed finite lower height bound, because the
CRT class has arbitrarily large positive representatives.

What remains potentially useful is necessarily nonlocal: the full return word,
`X`-adic depth that grows with that word, exact equality of the returning
endpoint with the original value, or global minimum and credit constraints.

## 5. Verification

```text
python tools/verify_fixed_local_endpoint_congruence_no_go.py
```

The checker constructs actual incoming ordinary and exceptional blocks together
with independently prescribed outgoing valuation words. It checks `1984` small
near-power cases and five large constructions for the primary candidate.