# Harmonic packing for the dual-Wieferich candidate

Let

```text
m=3803,
B=2^3803,
d=4162203,
X=B-d.
```

The dual-Wieferich candidate theorem gives exactly

```text
K=17886960
```

permanent odd residue classes modulo

```text
M=3511^2*1093^2=14726582775529.
```

This note converts that permanent sieve and the no-return theorem into a global
reciprocal-sum bound for every hypothetical cycle. It is an infinite-family
inequality: no trajectory cutoff or cycle-length cutoff occurs in the proof.

## 1. Square-sieve base representatives

Because `3511^2|X`, every accelerated output satisfies

```text
n == 2^(-s) (mod Q),
Q=3511^2=12327121,
1<=s<=1755.                                         (1)
```

There are exactly

```text
h=1755
```

classes in (1). For a residue `r`, let `rho(r)` be its least positive odd
representative:

```text
rho(r)=r       if r is odd,
rho(r)=r+Q     if r is even.
```

The orbit from `1` cannot return to `1`. Therefore, for the residue `r=1`, the
least cycle value is not `1` but at least

```text
1+2*Q.
```

Use that shifted value in the definition of `rho(1)`. Exact summation over the
`1755` classes gives

```text
1/2111
 < sum_(r in square classes) 1/rho(r)
 <1/2110.                                            (2)
```

The upper inequality is the part used below.

## 2. Packing lemma for residue classes

Let `R` be any set of `J` odd residue classes modulo an odd modulus `N`. Exclude
`1` if the orbit cannot contain it, and let `rho_j` be the least remaining
positive odd representative of class `j`.

Suppose `p` distinct positive odd integers lie in these classes. If class `j`
contains `c_j` of them, its ordered values are bounded below by

```text
rho_j,
rho_j+2*N,
...,
rho_j+2*N*(c_j-1).
```

Hence, after overcounting one base term for every class,

```text
sum_(values in class j) 1/n
 <=1/rho_j + H_(c_j-1)/(2*N),                       (3)
```

for occupied classes, where `H_0=0` and `H_k=sum_(i=1)^k 1/i`.

The increments of `H_k` decrease with `k`, so for a fixed total number of tail
terms their sum is maximized by distributing them as evenly as possible among
the `J` classes. A convenient uniform consequence is

```text
sum_i 1/n_i
 <=sum_j 1/rho_j
   +J*H_(ceil(p/J))/(2*N).                           (4)
```

This bound remains valid if some classes are empty or if the actual residues
have larger least representatives.

## 3. A certified base bound for the combined classes

Every one of the `K` combined classes is contained in one of the `h` square-
sieve classes from (1). Its least positive odd representative is therefore one
of `K` distinct square-admissible positive odd integers different from `1`.

Apply (4) first to the square sieve with

```text
J=h=1755,
N=Q=12327121,
p=K=17886960,
ceil(K/h)=10192.
```

Using (2), exact rational arithmetic gives

```text
1/2110 + 1755*H_10192/(2*12327121)
 <1/853.                                             (5)
```

Consequently, if `sigma_1,...,sigma_K` are the least allowed positive odd
representatives of the combined classes modulo `M`, then

```text
sum_(j=1)^K 1/sigma_j <1/853.                        (6)
```

No enumeration of the `17,886,960` combined representatives is needed for this
certificate.

## 4. Combined harmonic packing theorem

Apply (4) a second time, now to the combined classes. Any hypothetical positive
cycle of length `p` for the new candidate consists of `p` distinct positive odd
values, all lying in those `K` classes and none equal to `1`. Therefore

```text
sum_(i=0)^(p-1) 1/n_i
 <1/853 + K*H_(ceil(p/K))/(2*M),                     (7)
```

where

```text
K=17886960,
M=14726582775529.
```

The exact tail coefficient satisfies

```text
1/1647000
 <K/(2*M)
 <1/1646000.                                         (8)
```

Thus the reciprocal mass grows only harmonically with cycle length, with a
coefficient below `1/1,646,000`.

## 5. Consequence for the exact cycle correction

For a hypothetical cycle, let `A` be the total valuation and put

```text
D=m*p-A,
delta=log2(B/X).
```

The standard cycle product identity gives

```text
epsilon=p*delta-D
 =sum_i log2(1+1/(X*n_i))
 >0.                                                 (9)
```

Since `log2(1+z)<z/ln(2)`, combining (7) and (9) yields the strict necessary
condition

```text
0<p*delta-D
 <[1/853 + K*H_(ceil(p/K))/(2*M)]/(X*ln(2)).         (10)
```

This is much narrower than the earlier uniform strip

```text
0<p*delta-D<d*p/(2*X*ln(2)),
```

because the new right side grows only like `log p`, not linearly in `p`.

Equation (10) does not by itself exclude all integers `p,D`: exceptionally good
rational approximations to `delta` remain possible. It does, however, reduce
the remaining cycle problem to a precise Diophantine-and-block-credit target:

1. `D` must equal the exact near-power block-credit sum;
2. `p*delta` must lie within the harmonic window (10) above that integer;
3. exceptional blocks must also respect the dual-sieve height floor.

## 6. Next use

The next decisive step should combine (10) with the block ledger rather than
merely enlarge a finite search:

```text
D=sum ordinary deficits-sum exceptional excesses.
```

Promising exact subtargets are:

1. prove that each admissible credit pattern forces a lower bound on
   `p*delta-D` larger than (10);
2. split by the number of exceptional blocks and use their permanent source
   floor;
3. use continued-fraction windows only after the credit pattern has reduced the
   possible numerators, so the computation certifies an infinite structural
   statement rather than a record cutoff.

## 7. Verification

```text
python tools/verify_dual_wieferich_harmonic_packing.py
```

The checker uses exact rational arithmetic for (2), (5), and (8). The packing
lemma and the passage from reciprocal sums to (10) are symbolic inequalities
proved above.
