# N-adic ladder for cycles without exceptional blocks

Use the primary candidate

```text
k=500,
N=2^500-1,
m=4501,
B=2^4501,
d=349*2^500-347=2+349*N,
X=B-d,
q=1093,
Q=q^2.
```

Let a hypothetical positive cycle have cyclic valuation word

```text
2^a_i*n_(i+1)=X*n_i+1,
0<=i<p.
```

Assume every complete near-power block is ordinary. Let `J` be the number of
blocks, let their terminal deficits be `e_1,...,e_J`, and put

```text
D=m*p-A=sum_(j=1)^J e_j.
```

Then

```text
J<=D.                                                (1)
```

The earlier deep-class theorem showed that almost all values lie in one class
modulo `N*Q`. This note proves a stronger fact: every additional consecutive
valuation-`m` step fixes one additional full power of `N`.

## 1. Exact `N`-adic depth of the multiplier

Since

```text
4501=9*500+1,
2^500=1+N,
```

we have modulo `N^2`

```text
B=2*(1+N)^9==2+18*N.
```

Also

```text
d=2+349*N.
```

Therefore

```text
X=B-d==-331*N (mod N^2).                            (2)
```

Exact arithmetic gives

```text
gcd(331,N)=1.
```

Hence

```text
N|X,
gcd(X/N,N)=1.                                      (3)
```

The multiplier is exactly one `N`-adic layer deep.

## 2. Repeated valuation `m` converges to one `N`-adic point

During a valuation-`m` step, write

```text
F(n)=(X*n+1)/B.
```

The rational fixed point of `F` is `1/d`, because `B-X=d`. More precisely,

```text
F(n)-1/d=(X/B)*(n-1/d).                             (4)
```

By (3), multiplication by `X/B` adds one factor of `N` in `N`-adic precision.
Consequently, after `j` consecutive valuation-`m` steps,

```text
y_j==d^(-1) (mod N^j).                              (5)
```

This congruence is independent of the value at the start of the run.

For `j>=2`, the two latest valuation labels are both `m`, so the
`1093^2` adjacent-label coordinate is fixed as well. Thus all depth-`j` values
from all blocks lie in one class modulo

```text
N^j*Q.                                               (6)
```

## 3. Lower bounds for the fixed representatives

Let `r_j` be the least positive residue of `d^(-1)` modulo `N^j`.

At depth one,

```text
r_1=(N+1)/2.                                         (7)
```

It is even, so the least positive odd value in that class is

```text
rho_1=(3*N+1)/2.                                     (8)
```

At depth two, exact lifting gives

```text
r_2=r_1+N*(N-351)/4>N^2/5.                          (9)
```

For every `j>=3`,

```text
r_j>=N^(j-2).                                       (10)
```

Indeed, `d*r_j-1` is a positive multiple of `N^j`. If
`r_j<N^(j-2)`, then because `d<N^2`,

```text
0<d*r_j-1<N^j,
```

which is impossible.

## 4. Terminal outputs

A terminal deficit `e=m-s` gives

```text
n_next==2^(-s)==2^(e-1) (mod N),                    (11)
```

with the exponent reduced modulo `500`.

If `e=1`, the residue is `1`; since the cycle cannot contain `1`, the terminal
output is at least `1+2*N`, and its reciprocal is less than `1/(2*N)`.
If `e>=2`, every cycle value is greater than `N`, so its reciprocal is less than
`1/N<=e/(2*N)`.

Therefore the total reciprocal mass of all terminal outputs is strictly less
than

```text
D/(2*N).                                             (12)
```

## 5. First internal outputs

Every nonempty run has one depth-one output in the single class (7). There are
at most `J` such values, all distinct and spaced by `2*N`. Hence their total
reciprocal mass is less than

```text
2/(3*N+1)+H_J/(2*N).                                (13)
```

## 6. All deeper internal outputs

For each depth `j>=2`, at most `J` blocks reach that depth. By (6), those values
are distinct members of one odd class modulo `N^j*Q`. Their reciprocal mass is
at most

```text
1/r_j+H_J/(2*N^j*Q).                                (14)
```

Summing (14), using (9)--(10), gives

```text
sum_(j>=2) depth-j mass
 <5/N^2+1/(N-1)+H_J/[2*Q*N*(N-1)].                  (15)
```

This bound is independent of the lengths of the runs. A run may contain an
astronomical number of valuation-`m` steps, but its successive values enter
classes modulo `N^2,N^3,...`, so their reciprocal contribution forms a
convergent geometric tail.

## 7. Global reciprocal bound for the no-exceptional case

Combining (12), (13), and (15), then using `J<=D`, gives the exact bound

```text
sum_i 1/n_i
 <D/(2*N)
  +2/(3*N+1)+H_D/(2*N)
  +5/N^2+1/(N-1)
  +H_D/[2*Q*N*(N-1)].                               (16)
```

The elementary inequalities

```text
2/(3*N+1)<2/(3*N),
5/N^2+1/(N-1)<4/(3*N),
1/[2*Q*N*(N-1)]<1/(2*N)
```

simplify (16) to

```text
sum_i 1/n_i
 <[D/2+H_D+2]/N.                                    (17)
```

Unlike the earlier harmonic bounds, (17) has no dependence on the cycle length
`p`. It depends only on the integral credit `D`.

## 8. Sharpened correction window

Let

```text
delta=log2(B/X),
epsilon=p*delta-D.
```

The exact cycle product identity gives

```text
epsilon=sum_i log2(1+1/(X*n_i))>0.
```

Using (17), every no-exceptional positive cycle must satisfy

```text
0<p*delta-D
 <[D/2+H_D+2]/(N*X*ln(2)).                          (18)
```

This is the strongest current necessary condition for a no-exceptional cycle.
It replaces a bound growing like `log(p)` by one controlled only by `D`, even
though `p` may be vastly larger than `D`.

## 9. Remaining arithmetic problem

Equation (18) does not yet give a contradiction. It says that the integer pair
`(p,D)` must approximate `delta` with relative error on the order of

```text
1/(N*X).
```

The next exact step is to combine (18) with the composition

```text
D=e_1+...+e_J
```

and the cyclic order of the deficits. In particular:

1. `D=1` forces the single cyclic word `m^(p-1),(m-1)`;
2. small `D` gives only finitely many deficit compositions;
3. each composition determines the boundary residue classes more precisely than
   the aggregate estimate (12).

The intended route is to exclude whole deficit-composition families, not merely
to extend a denominator search.

## 10. Verification

```text
python tools/verify_no_exceptional_n_adic_ladder.py
```

The checker verifies (2)--(3), the exact residues (7)--(9), sample instances of
(5), and the rational simplifications used in (17).
