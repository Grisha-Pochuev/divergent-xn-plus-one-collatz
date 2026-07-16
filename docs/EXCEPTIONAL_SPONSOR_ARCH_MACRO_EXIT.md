# Canonical exceptional sponsor arches and the bounded initial macro-exit

Date: 2026-07-17

## Scope

Let

```text
B=2^m,
d positive odd,
1<=d<B/2,
X=B-d>=5.
```

Use the accelerated map

```text
C_X(n)=(X*n+1)/2^v2(X*n+1).
```

Assume a nontrivial positive cycle exists and use its canonical complete
near-power block partition.  An ordinary block has positive integer credit
`1<=e<=m-1`; an exceptional block has credit `-b`, `b>=1`.

The earlier minimum-boundary ballot theorem rotates the complete blocks so that,
for prefix credits

```text
P_0=0,
P_j=sum_(i<j)c_i,
```

we have

```text
P_j>=1 for every 1<=j<=q.                              (1)
```

This note turns (1) into an actual consecutive sponsor decomposition.  Every
exceptional block is enclosed by a canonical ordinary-to-exceptional arch of
net credit at most `m-2`.  These arches are laminar.  Their maximal members are
disjoint and compress all exceptional blocks into nonnegative-credit
macroblocks.

For the primary candidate, the maximal arch beginning at the least boundary, if
one exists, can be absorbed into a bounded initial macro-exit.  The remaining
actual return still has positive credit and astronomical length.

## 1. Canonical sponsor arch for one exceptional block

Let block `j` be exceptional, so

```text
c_j=-b<0.
```

Put

```text
h=P_(j+1).
```

By (1), `h>=1`, while

```text
P_j=h+b>h.
```

Define `i=i(j)` to be the last index at or before `j` such that

```text
P_i<=h.                                                (2)
```

Such an index exists because `P_0=0<=h`.  Since `P_j>h`, we have `i<j`.  The
maximality in (2) gives

```text
P_(i+1)>h.
```

Therefore block `i` has positive credit and is ordinary.  The consecutive block
segment

```text
i,i+1,...,j
```

is the canonical sponsor arch of exceptional block `j`.

Its net credit is

```text
C=P_(j+1)-P_i=h-P_i.                                  (3)
```

Because

```text
P_i<=h<P_(i+1)=P_i+c_i,
```

we obtain

```text
0<=C<c_i<=m-1,
0<=C<=m-2.                                             (4)
```

Moreover every proper boundary inside the arch lies strictly above its final
credit level:

```text
P_t>h for every i<t<=j.                               (5)
```

Equivalently, relative to the arch source,

```text
P_t-P_i>C for every i<t<=j,
P_(j+1)-P_i=C.                                         (6)
```

Thus the arch starts with an ordinary sponsor block, stays strictly above its
final credit level, and ends at the chosen exceptional block.

For the primary candidate `m=4501`, every sponsor arch has

```text
0<=C<=4499.                                            (7)
```

## 2. Laminarity

Two canonical sponsor arches cannot cross.

Suppose, for contradiction, that their block intervals satisfy

```text
i<u<=j<v.
```

Let their final credit levels be

```text
h_1=P_(j+1),
h_2=P_(v+1).
```

Because `u` is strictly inside the first arch, (5) gives

```text
P_u>h_1.
```

But `u` is the source of the second arch, so `P_u<=h_2`.  Hence

```text
h_2>h_1.                                               (8)
```

The boundary `j+1` lies strictly inside the second arch.  Applying (5) to that
arch gives

```text
P_(j+1)>h_2.
```

Since `P_(j+1)=h_1`, this contradicts (8).

Therefore any two sponsor arches are either disjoint or one contains the other.
Their maximal members are pairwise disjoint.

Every exceptional block belongs to its own sponsor arch and hence to a maximal
arch.  A block outside all maximal arches cannot be exceptional, so it is
ordinary.  Consequently the cyclic block list decomposes into:

1. pairwise disjoint maximal sponsor arches, each of net credit in
   `[0,m-2]`;
2. uncovered ordinary blocks, each of credit in `[1,m-1]`.

This is an actual consecutive decomposition, not a matching only at the level
of formal credit units.

## 3. Exact height domination for arches

For every complete block of source `n`, endpoint `n'`, length `ell`, and credit
`c`, the retained exact inequality is

```text
n'/n<2^c.                                              (9)
```

Multiplying (9) across a sponsor arch gives

```text
arch endpoint / arch source <2^C.                     (10)
```

In particular, a zero-credit sponsor arch strictly contracts.

The same multiplication shows that every maximal sponsor arch is a legitimate
nonnegative-credit macroblock.  Summing the macroblock credits together with
the uncovered ordinary credits recovers the full cycle credit `D` exactly.

## 4. Local length bound for every nondecreasing segment

There is also a local version of the global block-correction upper bound.
Consider any actual consecutive segment of complete blocks, with

```text
C = net segment credit,
L = total accelerated length,
x = source,
y = endpoint.
```

For block `r`, let

```text
q_r=((B/X)^ell_r-1)/(d*n_r)>0.
```

The exact segment ratio is

```text
ln(y/x)
 =C*ln(2)-L*ln(B/X)+sum_r ln(1+q_r).                  (11)
```

The retained complete-block estimate gives

```text
q_r<ell_r*d/(2*X^ell_r)<=ell_r*d/(2*X).
```

Therefore

```text
sum_r ln(1+q_r)<L*d/(2*X).                            (12)
```

If the segment is nondecreasing, `y>=x`, equations (11)--(12) imply

```text
L*[ln(B/X)-d/(2*X)]<C*ln(2).                          (13)
```

Using

```text
ln(B/X)>d/B,
ln(2)<1,
d/B-d/(2*X)=d*(X-d)/(2*B*X)>0,
```

we obtain the exact local theorem

```text
L < 2*C*B*X/[d*(X-d)].                                (14)
```

Thus a nondecreasing segment must have `C>=1`.  For the primary candidate and
`C<=4500`, exact integer arithmetic gives

```text
L<2^4006.                                             (15)
```

Unlike the previous harmonic estimate, (14) requires no upper assumption on
`L` and no finite trajectory computation.

## 5. The bounded sponsored macro-exit at the least boundary

Now specialize to

```text
m=4501,
B=2^4501,
d=349*2^500-347,
X=B-d.
```

Let `z` be the least complete-block boundary.  The previous pure-exit theorem
proves that the first block after `z` is ordinary, has deficit

```text
1<=e<=4500,
```

ends at a strictly larger boundary, and leaves a remaining return of credit

```text
R_0>=1.                                                (16)
```

Use the maximal sponsor-arch decomposition from Section 2.

### Case A: no maximal sponsor arch begins at block 0

Take the first ordinary block itself as the initial macro-exit.  Its credit is

```text
C=e.
```

### Case B: a maximal sponsor arch begins at block 0

Take that entire arch as the initial macro-exit.  By (4),

```text
0<=C<e<=4500.                                         (17)
```

The arch cannot be the full cycle.  If it were, then `D=C<e`, whereas (16)
gives

```text
D=e+R_0>e.
```

Hence the arch ends at a proper cycle boundary.  By minimality of `z`, its
endpoint `y` satisfies `y>z`.  Equation (10) then rules out `C=0`.

Thus in both cases the actual initial macro-exit satisfies

```text
z<y,
1<=C<=4500.                                           (18)
```

Applying (15), its accelerated length obeys

```text
L_macro<2^4006.                                       (19)
```

In Case B the macro-exit absorbs the entire maximal nest of early exceptional
blocks sponsored through the first ordinary crossing.  It is therefore a
strictly stronger decomposition than retaining only the first pure block.

## 6. The compressed return remains positive and long

Let

```text
R=D-C
```

be the credit of the remaining actual return from `y` to `z`.

In Case A, `R=R_0>=1`.  In Case B, (16)--(17) give

```text
R=e+R_0-C>=2.
```

Therefore in all cases

```text
R>=1.                                                 (20)
```

The exact return equation is

```text
log2(z/y)=R-L_return*delta+K_return<0,
delta=log2(B/X),
K_return>0.
```

Hence

```text
R<L_return*delta.
```

The retained exact estimate `delta<2^-3990` yields

```text
L_return>2^3990.                                      (21)
```

Finally, let `Q` be the credit of any prefix of this compressed return ending at
a complete-block boundary.  The full prefix from `z` has credit `C+Q`, so the
ballot theorem gives

```text
C+Q>=1,
Q>=1-C>=-4499.                                        (22)
```

Thus every hypothetical cycle now has an actual consecutive decomposition

```text
bounded sponsored macro-exit:
  z<y,
  1<=C<=4500,
  L_macro<2^4006;

remaining return:
  R>=1,
  L_return>2^3990,
  every block-boundary prefix has Q>=-4499.
```

## 7. Meaning and next obstruction

The theorem does not exclude the final positive-credit return.  It does remove
an important ambiguity: an arbitrarily complicated nest of exceptional blocks
immediately sponsored by the first ordinary block can be compressed into one
bounded-credit, bounded-length macro-exit.

The remaining return is still astronomically long.  Its exceptional blocks are
partitioned into disjoint maximal sponsor arches of credit at most `4499`, and
all uncovered blocks are ordinary.  The next useful target is therefore one of:

1. prove that too many contracting maximal arches force an impossible cumulative
   height loss;
2. use the permanent `N` and `1093^2` labels to rule out a maximal arch with the
   required source and endpoint classes;
3. show that every noncontracting maximal arch consumes one of only finitely many
   admissible sponsor classes, forcing repetition on the long return;
4. combine the local bound (14) with the exceptional-source floor to force a
   contradiction for an arch containing a large excess.

## 8. Verification

Run

```text
python tools/verify_exceptional_sponsor_arch_macro_exit.py
```

The checker verifies the canonical construction, laminarity, maximal-arch
coverage, and exact credit decomposition on more than two million positive-prefix
integer ledgers.  It also checks the local segment bound on exact near-power
orbit segments, all three known accelerated `5n+1` cycle regressions, and the
primary comparisons (15), (20)--(22).
