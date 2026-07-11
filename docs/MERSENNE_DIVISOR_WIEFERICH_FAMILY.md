# Mersenne-divisor Wieferich family

This note constructs an infinite family of explicit accelerated `Xn+1`
candidates with three simultaneous features:

1. the orbit from `1` leaves `1` and can never return;
2. every accelerated output lies in a very thin one-label residue family;
3. the cycle correction admits a harmonic-packing upper bound whose constants
   become exponentially small as the construction parameter grows.

The theorem does not by itself prove divergence. Its value is that the thin
permanent sieve is constructed algebraically, rather than found by a finite
search.

## 1. Construction

Fix

```text
q=1093,
h=ord_(q^2)(2)=364,
```

so that `q` is a base-2 Wieferich prime.

Choose an integer `k>=2` such that

```text
364 does not divide k.
```

Put

```text
N=2^k-1.
```

Then `q` does not divide `N`, because the exact order of `2` modulo `q` is
`364`.

Choose integers `m>k` and `r` with

```text
m==r (mod k),
0<=r<k.
```

Choose a positive integer `t` and put

```text
d=2^r+t*N,
B=2^m,
X=B-d.                                               (1)
```

Assume

```text
d is odd,
d<B/2,
q divides X exactly once.                            (2)
```

The parity condition means `t` is odd when `r>=1`, and `t` is even when `r=0`.

Because

```text
B==2^r==d (mod N),
```

we have

```text
N|X.                                                 (3)
```

The pair under study is

```text
(X,n0)=(2^m-2^r-t*(2^k-1),1).                       (4)
```

## 2. Such parameters always exist

For fixed admissible `k,m,r`, the condition `q|X` is one linear congruence for
`t` modulo `q`:

```text
t*N==B-2^r (mod q).                                 (5)
```

Since `q` does not divide `N`, (5) has one solution modulo `q`. Adding `q`
changes the parity, so a lift with the parity required in (2) exists below
`2*q`.

Among the parity-preserving lifts

```text
t=t_0+2*q*j,
0<=j<q,
```

exactly one at most can make `q^2|X`, because `2*N` is invertible modulo `q`.
Choosing any other lift gives

```text
q||X
```

with

```text
0<t<2*q^2.                                          (6)
```

Finally, increasing `m` within its congruence class modulo `k` makes `B` large
enough that `d<B/2`. Thus the family contains infinitely many explicit
candidates for every `k` not divisible by `364`.

## 3. The orbit leaves `1` and never returns

By `d<B/2`,

```text
B/2<X+1<B.
```

There is no power of two strictly between `B/2` and `B`. Therefore

```text
C_X(1)>1.                                           (7)
```

Every accelerated output is coprime to `q`, because `q|X` gives

```text
X*z+1==1 (mod q),
```

and division by a power of two cannot introduce an odd prime factor.

If an accelerated output `y` mapped to `1`, then

```text
X*y+1=2^a.
```

Modulo `q`, the exact order forces `h|a`. The Wieferich congruence then gives

```text
q^2|2^a-1=X*y.
```

Since `q||X`, this would force `q|y`, contradicting output coprimality. Hence

```text
C_X^j(1)!=1 for every j>=1.                          (8)
```

## 4. Exact one-label sieve modulo `N=2^k-1`

For an accelerated transition

```text
2^a_i*n_(i+1)=X*n_i+1,
```

reduction modulo `N`, using (3), gives

```text
n_(i+1)==2^(-a_i) (mod N).                          (9)
```

The order of `2` modulo `N` is exactly `k`. Indeed, `2^k==1 (mod N)`, while for
`0<j<k` the positive integer `2^j-1` is smaller than `N` and cannot be divisible
by `N`.

Consequently every accelerated output belongs to exactly one of

```text
k
```

classes modulo `N`, indexed by the current valuation label

```text
1<=s_i<=k,
a_i==s_i (mod k).                                  (10)
```

This is a permanent infinite-family sieve.

## 5. Combination with the `1093^2` adjacent-label coordinate

Because `q||X`, the adjacent-label theorem modulo `q^2` gives `h^2` classes
indexed by

```text
(a_(i-1) mod h, a_i mod h).
```

The current labels modulo `k` and `h` come from the same integer `a_i`; they
must agree modulo

```text
g=gcd(k,h).
```

There are exactly

```text
lcm(k,h)
```

compatible current-label pairs, and `h` independent choices for the previous
`q`-label. By the Chinese remainder theorem, every hypothetical cycle value
therefore lies in exactly

```text
K=h*lcm(k,h)                                        (11)
```

classes modulo

```text
M=N*q^2.                                            (12)
```

The retained density is

```text
K/M
 =h*lcm(k,h)/[(2^k-1)*q^2],                         (13)
```

which decreases exponentially with `k`.

## 6. Exact odd representatives of the one-label classes

The residues in (9) are especially simple:

```text
2^(-s) ==2^(k-s) (mod N).
```

For `1<=s<k`, this is the even residue `2^(k-s)`, whose least positive odd
representative is

```text
N+2^(k-s).
```

For `s=k`, the residue is `1`. A hypothetical cycle cannot contain `1` by (8),
so its least allowed positive odd representative in that class is

```text
1+2*N.
```

Thus every hypothetical cycle value satisfies

```text
n_i>N.                                               (14)
```

Moreover the exact base reciprocal sum satisfies

```text
S_k
 =1/(1+2*N)+sum_(j=1)^(k-1)1/(N+2^j)
 <k/N.                                               (15)
```

## 7. Harmonic packing

The residue-class packing lemma says that `p` distinct positive odd integers in
`J` odd classes modulo an odd modulus `L` satisfy

```text
sum_i 1/n_i
 <=sum_(j=1)^J 1/rho_j
   +J*H_(ceil(p/J))/(2*L),                           (16)
```

where `rho_j` are the least allowed positive odd representatives.

Apply (16) first to the `k` classes modulo `N` and to the `K` least combined
representatives. Since

```text
K/k=h^2/g,
```

(15) gives

```text
sum_(j=1)^K 1/sigma_j
 <(k/N)*[1+H_(h^2/g)/2].                             (17)
```

Apply (16) again to an arbitrary hypothetical cycle in the `K` combined classes
modulo `M`:

```text
sum_i 1/n_i
 <(k/N)*[1+H_(h^2/g)/2]
  +K*H_(ceil(p/K))/(2*M).                            (18)
```

For

```text
delta=log2(B/X),
D=m*p-A,
```

the exact cycle product identity and `log2(1+z)<z/ln(2)` yield

```text
0<p*delta-D
 <{(k/N)*[1+H_(h^2/g)/2]
    +K*H_(ceil(p/K))/(2*M)}
   /(X*ln(2)).                                       (19)
```

Both coefficients outside the final harmonic number decay exponentially in
`k`.

## 8. Elementary cycle barrier

The standard near-power product argument gives

```text
D>=1,
D<3*p*d/(2*X).
```

Therefore every positive cycle must have

```text
p>2*X/(3*d).                                        (20)
```

By increasing `m-k` while keeping `t` bounded as in (6), the finite barrier in
(20) can also be made arbitrarily large.

This is a construction theorem for simultaneously obtaining an arbitrarily thin
permanent sieve and an arbitrarily large finite barrier. Neither fact alone is a
proof of divergence.

## 9. Explicit balanced example

Take

```text
k=500,
m=4501,
r=1,
t=349,
N=2^500-1,
d=2+349*N=349*2^500-347,
X=2^4501-349*2^500+347,
n0=1.                                                (21)
```

Exact verification gives

```text
1093||X,
gcd(500,364)=4,
K=16562000,
M=(2^500-1)*1093^2.                                 (22)
```

For this example:

```text
combined base reciprocal sum <10^(-147),
K/(2*M)<10^(-149),                                  (23)
```

and the permanent class density is between `10^143` and `10^144` times smaller
than for the earlier candidate `X=2^3803-4162203`.

The elementary cycle barrier satisfies

```text
10^1201<floor(2*X/(3*d))<10^1202.                   (24)
```

Thus this family member improves both the finite barrier and the permanent
harmonic constants, while using a structured difference `d`.

## 10. Meaning and limitation

The family theorem shows that neither a huge finite barrier nor an extremely
thin permanent residue density is, by itself, the missing final idea: both can
be strengthened without limit by construction.

Its useful contribution is the exact global framework (19). The remaining task
is still to connect the narrow harmonic window to the integral block-credit
identity

```text
D=sum ordinary deficits-sum exceptional excesses.
```

A successful proof must exploit more than the raw size of the sieve. Promising
additional structure includes:

1. restrictions on which valuation labels can follow one another;
2. exceptional-source arithmetic inside the Mersenne-divisor classes;
3. a height-dependent lower bound for the correction associated with each
   admissible credit pattern.

## 11. Verification

```text
python tools/verify_mersenne_divisor_wieferich_family.py
```

The checker verifies the explicit example, exact divisibilities and orders,
class counts, representative formulas, rational harmonic bounds, density
comparison, and cycle barrier using only the Python standard library.
