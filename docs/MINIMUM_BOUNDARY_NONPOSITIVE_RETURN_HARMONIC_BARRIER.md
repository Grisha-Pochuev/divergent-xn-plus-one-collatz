# Nonpositive minimum-boundary returns are doubly exponentially long

Use the primary candidate

```text
m=4501,
B=2^4501,
d=349*2^500-347,
X=B-d,
N=2^500-1.
```

Assume a hypothetical nontrivial positive cycle exists. Let `x` be the least
cycle value immediately following an ordinary complete block, and let `y>x` be
the next such boundary. The actual segment from `x` to `y` supplied by
`MINIMUM_BOUNDARY_ACTUAL_EXPANDING_SEGMENT.md` has

```text
1<=exit credit C<=4500
```

and at most `4500` complete blocks.

Follow the remaining actual orbit from `y` back to `x`. Write

```text
R = return ordinary-deficit sum - return exceptional-excess sum,
L = accelerated length of the return.
```

This note proves

```text
R<=0  =>  L>2^(2^974).                                  (1)
```

This is a theorem about the actual return segment. It is not a finite orbit
calculation.

## 1. A nonpositive return leaves a small total cycle credit

Let the total cycle credit be

```text
D=C+R.
```

Every positive cycle satisfies `D>=1`. If `R<=0`, then

```text
1<=D<=C<=4500.                                           (2)
```

Let `p` be the full accelerated cycle length and put

```text
z=p*ln(B/X)-D*ln(2).
```

The exact accelerated-step product identity gives

```text
z=sum_cycle ln(1+1/(X*n_i))>0.                            (3)
```

The one-sided continued-fraction certificate used for the minimum-boundary
segment applies to every integer `1<=D<=4500`. It gives

```text
z>2^-4023.                                                (4)
```

Thus it is enough to prove that the correction on the exit plus the correction
on the return is smaller than `2^-4023`.

## 2. Correction on the short expanding exit

The actual exit contains at most `4500` complete blocks. Every cycle value is
greater than `N`. The complete-block correction bounds therefore give

```text
K_exit
 <4500/(X*N)+4500*d/X^2.                                  (5)
```

The exact checker below verifies, much more strongly than needed, that the
right side of (5) is below `2^-4024`.

## 3. Harmonic packing on the return

Every accelerated cycle value lies in

```text
K=16562000
```

permanent classes modulo

```text
M=N*1093^2.
```

For any `L` distinct values in these classes, the harmonic-packing theorem gives

```text
sum_return 1/n
 < S0 + T*H_(ceil(L/K)),                                  (6)
```

where the explicit primary-candidate constants satisfy

```text
S0<2^-488,
T=K/(2*M)<2^-497.                                         (7)
```

Assume for contradiction that

```text
L<=2^(2^974).                                              (8)
```

Since `ceil(L/K)<=L`, `H_s<=1+ln(s)`, and `ln(2)<3/4`,

```text
H_(ceil(L/K))<2^974.                                      (9)
```

For each accelerated source `n`,

```text
ln(1+1/(X*n))<1/(X*n).
```

Therefore (6)--(9) give

```text
K_return
 <[S0+T*2^974]/X.                                         (10)
```

The exact rational comparison in the checker proves

```text
[S0+T*2^974]/X <2^-4024.                                  (11)
```

Combining (5) and (11),

```text
K_exit+K_return<2^-4023,                                  (12)
```

contradicting the mandatory gap (4). This proves (1).

## 4. Combined return theorem

Together with `MINIMUM_BOUNDARY_RETURN_CREDIT_DICHOTOMY.md`, every hypothetical
return from `y>x` to the least ordinary boundary `x` satisfies

```text
R>=1  => L>2^3990,
R<=0  => L>2^(2^974).                                     (13)
```

In particular every hypothetical return has length greater than `2^3990`, and
any return of length at most `2^(2^974)` would have to carry positive integer
credit.

This is not yet a cycle exclusion. The remaining branch is a positive-credit
return longer than `2^3990`, together with the formally possible nonpositive
return beyond the double-exponential barrier. The next useful target is an
inverse `X`-adic or endpoint-congruence obstruction that does not weaken as the
return length grows.

## 5. Verification

```text
python tools/verify_minimum_boundary_nonpositive_return_harmonic_barrier.py
```

The checker independently verifies the continued-fraction gap, the permanent
harmonic constants, the tower-length harmonic estimate, both correction bounds,
and the final strict contradiction using exact rational arithmetic.