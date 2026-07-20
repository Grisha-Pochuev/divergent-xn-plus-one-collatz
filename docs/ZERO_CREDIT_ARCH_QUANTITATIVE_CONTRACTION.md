# Quantitative contraction of zero-credit sponsor arches

Date: 2026-07-17

## Scope

Use the retained primary candidate

```text
N=2^500-1,
B=2^4501,
d=349*2^500-347,
X=B-d.
```

Assume, for contradiction, that a nontrivial positive accelerated `Xn+1` cycle
exists.  Partition it into canonical complete near-power blocks.  For any actual
consecutive segment of complete blocks write

```text
C = net block credit,
L = accelerated length,
x = source,
y = endpoint.
```

The retained exact segment formula is

```text
log2(y/x)=C-L*delta+K,
delta=log2(B/X),
K=sum kappa_j>0.                                      (1)
```

Every cycle value is strictly larger than `N`.  The cycle-floor correction theorem
therefore gives

```text
K<L*epsilon,
epsilon=1/(X*N*ln(2)),
delta-epsilon>1007*2^-4002.                           (2)
```

This note records the consequences for zero-credit sponsor arches and for the
whole hypothetical cycle.

## 1. Unified quantitative height budget

Put

```text
alpha=1007*2^-4002.                                   (3)
```

Equations (1)--(2) imply, for every actual consecutive complete-block segment,

```text
log2(y/x)
 =C-L*delta+K
 <C-L*(delta-epsilon)
 <C-alpha*L.                                          (4)
```

Thus the same exact inequality handles positive, zero, and negative net credit.
It uses neither a finite trajectory cutoff nor a probabilistic drift model.

## 2. Zero-credit sponsor arches contract at a quantified rate

Let a canonical sponsor arch have net credit `C=0`.  From (4),

```text
log2(y/x)<-alpha*L,                                   (5)
```

and hence

```text
y/x<2^(-alpha*L),
x/y>2^(alpha*L).                                     (6)
```

This strengthens the previous qualitative statement `y<x`.

In particular, if

```text
L>=2^4002,
```

then

```text
alpha*L>=1007,
x>2^1007*y>2^1007*N.                                 (7)
```

More generally, whenever

```text
1007*L>=k*2^4002,
```

one has

```text
x>2^k*y.                                              (8)
```

Therefore a very long zero-credit arch is possible only if its source is
correspondingly high above its endpoint.

## 3. Product loss for disjoint zero-credit arches

Let pairwise disjoint zero-credit sponsor arches have total accelerated length

```text
Z=sum L_i.
```

Summing (5) over the arches gives

```text
sum_i log2(y_i/x_i)<-alpha*Z,
product_i(y_i/x_i)<2^(-alpha*Z).                      (9)
```

In the maximal sponsor-arch decomposition, all remaining macroblocks have
positive credit and their credits sum to the full cycle credit `D`.  Their total
possible logarithmic gain is strictly less than `D`.  Since the full cyclic
product is `1`, equation (9) forces

```text
alpha*Z<D,
Z<D*2^4002/1007.                                      (10)
```

Thus zero-credit arches cannot occupy an arbitrary amount of accelerated length
for fixed total cycle credit.

## 4. Near-critical global cycle-length window

Apply (4) to the full cycle.  There `x=y`, `C=D`, and `L=p`, so

```text
0<D-alpha*p,
p<D/alpha=D*2^4002/1007.                             (11)
```

The retained exact identity also has `K>0`, hence

```text
0=D-p*delta+K>D-p*delta,
D<p*delta.                                            (12)
```

Using the retained upper bound

```text
delta<1008*2^-4002,
```

we obtain

```text
p>D*2^4002/1008.                                      (13)
```

Combining (11) and (13), every hypothetical primary cycle lies in the exact
near-critical strip

```text
D*2^4002/1008
 <p
 <D*2^4002/1007.                                      (14)
```

The relative width above the lower endpoint is

```text
1008/1007-1=1/1007<0.001.                             (15)
```

So `p/D` is confined to a window of relative width below `0.1%`.

## 5. Return specialization

For the retained initial macro-exit and remaining return, write

```text
D=C+R,
1<=C<=4500,
R>=1,
p=L_macro+L_return.
```

The existing contracting-return theorem gives

```text
L_return>R*2^4002/1008.                               (16)
```

Equation (11) now adds

```text
L_return
 <p
 <(C+R)*2^4002/1007
 <=(R+4500)*2^4002/1007.                              (17)
```

This does not yet exclude the return, because `R` is not bounded.  It does show
that the surviving return and the full cycle must both stay in a sharply
controlled length-per-credit regime.

## 6. Strategic meaning and limitation

Zero-credit arches are no longer merely known to contract: their binary height
loss is at least `alpha*L`, proportional to their accelerated length.  The
surviving obstruction is therefore more precise:

1. the full cycle has only a `1/1007` relative length window;
2. the total length of all zero-credit arches is below `D/alpha`;
3. an individual zero-credit arch of length at least `2^4002` loses more than
   `1007` binary height units;
4. all positive-credit nondecreasing macroblocks have the retained upper length
   bound, while contracting positive-credit macroblocks have the retained lower
   length bound.

The theorem does not bound the total credit `D`.  The next useful step is to
combine the near-critical strip (14) and the zero-arch loss (6) with the permanent
`N` and `1093^2` endpoint labels, or to obtain a lower bound on the positive
correction `K` incompatible with the narrow interval in (14).

## 7. Verification

Run

```text
python tools/verify_zero_credit_arch_quantitative_contraction.py
```

The checker uses exact integer and rational arithmetic.  It verifies the primary
constant `alpha`, the `1008/1007` strip ratio, the `1/1007` relative width, the
initial-exit comparison, and the canonical zero-credit sponsor arch

```text
33 -> 83 -> 13
```

inside the accelerated `5n+1` cycle `13 -> 33 -> 83 -> 13`.
