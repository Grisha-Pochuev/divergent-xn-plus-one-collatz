# Every hypothetical cycle needs at least 245833 ordinary blocks

Use the primary candidate

```text
m=4501,
B=2^4501,
d=349*2^500-347,
X=B-d.
```

This note proves the global cycle-length-independent theorem

```text
Every nontrivial positive cycle contains at least 245833
ordinary complete blocks.                                      (1)
```

The theorem allows an arbitrary number of exceptional blocks and arbitrary
block lengths.

## 1. General signed block system

Suppose a hypothetical cycle has `J>=1` ordinary blocks and `R>=0` exceptional
blocks.  For an ordinary block put

```text
1<=e_i<=4500,
h_i=2^e_i,
r_i=1,
a_i=h_i-1.
```

For an exceptional block of excess `b_i>=1` put

```text
h_i=1,
r_i=2^b_i,
a_i=-(2^b_i-1).
```

For every block source `n_i`, length `ell_i`, and positive odd core `u_i`, write

```text
d*n_i-1=B^ell_i*u_i/h_i.                            (2)
```

The exact complete-block formula is

```text
r_i*B^ell_(i+1)*u_(i+1)
 =h_(i+1)*X^ell_i*u_i+h_(i+1)*a_i.                  (3)
```

Put

```text
E=sum ordinary deficits,
F=sum exceptional excesses,
D=E-F,
p=sum all block lengths.
```

Cycle closure gives

```text
D>=1,
Delta_D(p)=2^(m*p-D)-X^p>0.                          (4)
```

Since every ordinary deficit is at most `4500`,

```text
D<=E-1<=4500*J-1,                                   (5)
R<=F<=E-1<=4500*J-1.                                (6)
```

## 2. Signed elimination identity

Choose any block as block `0`, and define

```text
A_i=r_i*B^ell_(i+1),
C_i=h_(i+1)*X^ell_i,
f_i=h_(i+1)*a_i.
```

Eliminating all cores other than `u_0` from (3) yields

```text
[(product A_i)-(product C_i)]*u_0
 =sum_j f_j*(product_(i<j)A_i)*(product_(i>j)C_i).   (7)
```

Now

```text
product A_i=2^F*B^p,
product C_i=2^E*X^p,
```

and `E=F+D`.  Therefore

```text
2^E*Delta_D(p)*u_0=signed additive sum.              (8)
```

Every ordinary block contributes a positive term.  Every exceptional block
contributes a negative term.  Dropping all negative terms gives a rigorous
upper bound.

## 3. Bounds for selected ordinary and exceptional blocks

### Selected ordinary block

Let the selected ordinary block have length `L` and deficit `e_0`.  In each
positive term of (8), the `B`- and `X`-length factors contain every block length
except `L`.  After division by `2^E`, the remaining power-of-two coefficient is
less than

```text
2^(F+e_0)<B^(J+1),                                   (9)
```

because `F<=4500J-1` and `e_0<=4500`.  There are exactly `J` positive terms, so

```text
0<Delta_D(p)*u_0<J*B^(p-L+J+1).                     (10)
```

### Selected exceptional block

Let the selected exceptional block have length `k`.  Here `h_0=1`, so there is
no duplicated ordinary factor.  Every positive coefficient after division by
`2^E` is less than

```text
2^F<B^J.                                             (11)
```

Hence

```text
0<Delta_D(p)*u_0<J*B^(p-k+J).                       (12)
```

These bounds hold for every ordinary or exceptional block individually.

## 4. Continued-fraction gap

The exact continued-fraction certificate already established for the primary
candidate depends only on `(p,D)`.  It proves:

```text
0<D<1106246945 and Delta_D(p)>0
 => Delta_D(p)>2^(m*p-D-22206).                      (13)
```

Assume for contradiction that

```text
J<=245832.
```

Then (5) gives

```text
D<=1106243999<1106246945,                            (14)
```

so (13) applies.

## 5. Every block is short

Choose a longest ordinary block.  If its length satisfies

```text
L>=2*J+7,
```

then the exponent advantage of (13) over (10) is at least

```text
m*(2J+7)-(4500J-1)-22206-m*(J+1)
 =J+4801.                                            (15)
```

Since `2^(J+4801)>J`, equations (10) and (13) contradict one another.  Thus

```text
Every ordinary block has length at most 2J+6.        (16)
```

Now select any exceptional block.  If its length satisfies

```text
k>=2*J+6,
```

then the exponent advantage of (13) over (12) is again

```text
m*(2J+6)-(4500J-1)-22206-m*J
 =J+4801.                                            (17)
```

Therefore

```text
Every exceptional block has length at most 2J+5.     (18)
```

## 6. Final contradiction

By (6), (16), and (18), the total cycle length satisfies

```text
p
 <=J*(2J+6)+(4500J-1)*(2J+5).                       (19)
```

At the largest excluded value `J=245832`, the right side is

```text
544026748963771<10^15.                               (20)
```

But the independently proved elementary cycle barrier gives

```text
p>2*X/(3*d)>10^1201.                                 (21)
```

This contradiction proves (1).

## 7. Meaning

The earlier three-way split is no longer needed at small block count.  Regardless
of how many exceptional contractions occur, a hypothetical cycle must contain
at least

```text
245833 ordinary complete blocks.
```

The next target is therefore a genuine many-block theorem: use repeated ordinary
deficits, their exact classes modulo `X`, and the exceptional credit budget to
exclude arbitrarily large ordinary-block populations.

## 8. Verification

```text
python tools/verify_global_ordinary_block_count_frontier.py
```

The checker verifies the continued-fraction frontier, both universal block-length
bounds, the maximum possible exceptional-block population, the resulting cycle-
length upper bound, and the comparison with the existing `10^1201` barrier.