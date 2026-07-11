# Deep-class concentration when no exceptional block occurs

Use the primary candidate

```text
k=500,
N=2^500-1,
m=4501,
B=2^4501,
d=349*2^500-347,
X=B-d,
q=1093,
Q=q^2,
M=N*Q.
```

For a hypothetical positive cycle, write its cyclic valuation word as

```text
2^a_i*n_(i+1)=X*n_i+1,
0<=i<p.
```

This note treats the case in which every complete near-power block is ordinary:
there is no terminal valuation larger than `m`.

## 1. Complete blocks and terminal count

Let

```text
J=#{i: a_i!=m}.
```

The cyclic word splits into `J` complete blocks. Each block consists of zero or
more copies of `m`, followed by one terminal valuation

```text
s_i<m.
```

Put

```text
e_i=m-s_i,
1<=e_i<=m-1.
```

Since there are no exceptional blocks, the exact block ledger is

```text
D=m*p-A=sum_(i=1)^J e_i.                            (1)
```

Therefore

```text
J<=D.                                                (2)
```

The cycle product gives

```text
1<=D<p*delta,
delta=log2(B/X).                                    (3)
```

## 2. Two consecutive `m` labels fix one complete residue class

The one-label coordinate modulo `N` is

```text
n_(i+1)==2^(-a_i) (mod N).                          (4)
```

The adjacent-label coordinate modulo `Q` depends only on

```text
(a_(i-1) mod 364,a_i mod 364).                      (5)
```

Thus whenever

```text
a_(i-1)=a_i=m,                                      (6)
```

the value `n_(i+1)` lies in one fixed class modulo the full product `M`.

For the primary parameters,

```text
m==1   (mod 500),
m==133 (mod 364),
X/1093==334 (mod 1093).
```

The two coordinates of the fixed class are

```text
n_(i+1)==2^499 (mod N),
n_(i+1)==1041489 (mod 1093^2).                      (7)
```

The Chinese remainder theorem gives one even residue modulo `M`. Its least
positive odd representative is

```text
rho=
7319679475870985225735478685516495292058492637108610843267824819215970272214337044630080944136385337319533553121241051964811350229730788630140247134779072813.  (8)
```

Every value produced after two consecutive valuation-`m` steps therefore lies
in

```text
rho (mod 2*M).                                      (9)
```

## 3. Almost all values are in that one class

Consider one run of `r` consecutive `m` labels before a terminal label. It
contains

```text
max(r-1,0)
```

adjacent pairs `(m,m)`. Summing over the `J` runs gives at least

```text
c>=p-2*J                                             (10)
```

cycle values in the fixed class (9). This is a purely cyclic combinatorial
inequality; consecutive terminal labels are allowed.

Using (2),

```text
c>=p-2*D.                                            (11)
```

From the elementary estimate

```text
delta<3*d/(2*X)
```

and the certified barrier `2*X/(3*d)>10^1201`, we also get

```text
2*D/p<2*delta<10^(-1200).                            (12)
```

Hence more than a fraction

```text
1-10^(-1200)
```

of all cycle values must lie in the single class (9).

This is much stronger than saying that values lie in `16,562,000` possible
classes.

## 4. Sharpened reciprocal packing

The `c` distinct positive odd values in (9) are bounded below by

```text
rho,
rho+2*M,
...,
rho+2*M*(c-1).
```

Therefore

```text
sum_(deep values) 1/n
 <=1/rho+H_(c-1)/(2*M)
 <1/rho+H_p/(2*M).                                  (13)
```

At most `2*J<=2*D` values are not counted in (13). Every cycle value is greater
than `N`, so

```text
sum_(boundary values) 1/n<2*D/N.                    (14)
```

Combining (13)--(14) gives the no-exceptional reciprocal bound

```text
sum_(i=0)^(p-1) 1/n_i
 <1/rho+H_p/(2*M)+2*D/N.                            (15)
```

The harmonic tail in (15) has coefficient `1/(2*M)`, improving the previous
uniform coefficient `K/(2*M)` by the exact factor

```text
K=16562000.
```

## 5. Sharpened cycle-correction window

The exact cycle product identity gives

```text
epsilon=p*delta-D
 =sum_i log2(1+1/(X*n_i))
 >0.                                                 (16)
```

Using `log2(1+z)<z/ln(2)` and (15), every no-exceptional cycle must satisfy

```text
0<p*delta-D
 <[1/rho+H_p/(2*M)+2*D/N]/(X*ln(2)).                (17)
```

This is the first correction bound in the project that uses the actual block
transition pattern rather than only the set of globally allowed residue
classes.

The term `2*D/N` comes from the at most two boundary values per complete block.
Closing the no-exceptional case now reduces to controlling those boundary
values more sharply or proving that the integral credit sum in (1) cannot fit
the narrow interval (17).

## 6. What remains

Equation (17) is not yet a contradiction: very accurate rational approximation
to `delta` is still arithmetically possible. The next exact refinements are:

1. split the `2*J` boundary values by terminal deficit `e_i`;
2. use their known one-label classes `1-e_i (mod 500)`;
3. exploit that each long block has only one first-internal boundary value and
   one terminal output;
4. combine the deficit sum `sum e_i=D` with class-specific reciprocal floors.

This is now a finite-dimensional optimization over deficit populations, not a
uniform `16,562,000`-class packing problem.

## 7. Verification

```text
python tools/verify_no_exceptional_deep_class_concentration.py
```

The checker verifies the fixed Chinese-remainder class and exhaustively checks
the cyclic counting inequality through length `12`. The proof of (10) for all
lengths is the run decomposition above.
