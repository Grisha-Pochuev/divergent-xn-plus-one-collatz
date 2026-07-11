# Session checkpoint: dual-Wieferich harmonic frontier

Date: 2026-07-12

The strict prize problem remains open. This session found and certified a new
primary candidate

```text
m=3803,
B=2^3803,
d=4162203,
X=B-d,
n0=1.
```

It replaces `X=2^156-9` as the primary branch because it has a much thinner
permanent residue sieve and a new global harmonic-packing inequality. The old
candidate remains a valid independent fallback.

## 1. Two Wieferich primes in complementary roles

Exact modular arithmetic proves

```text
v_3511(X)=2,
ord_(3511^2)(2)=1755,

v_1093(X)=1,
ord_(1093^2)(2)=364.
```

The factor `1093||X` gives the same no-return mechanism used in the former
primary branch: the orbit leaves `1` immediately and can never return.

The factor `3511^2|X` gives the stronger one-label coordinate

```text
n_(i+1)==2^(-a_i) (mod 3511^2),
```

with only `1755` possible output classes.

## 2. Combined permanent sieve

Combining the `3511^2` one-label coordinate with the `1093^2` adjacent-label
coordinate and the compatibility of the current labels modulo

```text
gcd(1755,364)=13
```

gives exactly

```text
K=17886960
```

permanent classes modulo

```text
M=3511^2*1093^2=14726582775529.
```

Their density is about `1.2146*10^(-6)`, between `91312` and `91313` times
smaller than the `132496/1093^2` density of the former primary candidate.

## 3. Finite cycle barrier and exceptional floor

The elementary near-power product argument excludes every positive cycle length
through

```text
floor(2*X/(3*d)),
```

an exact `1139`-digit integer larger than `10^1138`.

The exceptional condition

```text
v2(d*n-1)=3803
```

is one progression. Combining it with both permanent coordinates and checking
all smaller progression layers proves that the first compatible layer is

```text
T=2350560,
3511-label=40,
1093-label pair=(99,222).
```

Hence every exceptional source in a hypothetical cycle satisfies

```text
n>=(19567017189655*2^3803+1)/4162203.
```

## 4. Global harmonic packing theorem

For the `1755` square-sieve classes, shifting the residue-`1` class because the
orbit cannot contain `1`, exact rational summation gives

```text
sum 1/rho <1/2110.
```

A residue-class packing lemma then bounds the least representatives of all
`K` combined classes by

```text
sum_(j=1)^K 1/sigma_j <1/853.
```

Therefore every hypothetical positive cycle of length `p` obeys

```text
sum_i 1/n_i
 <1/853 + K*H_(ceil(p/K))/(2*M).
```

Writing

```text
delta=log2(2^3803/X),
D=3803*p-A,
```

the exact cycle product identity yields the new infinite-family restriction

```text
0<p*delta-D
 <[1/853 + K*H_(ceil(p/K))/(2*M)]/(X*ln(2)).
```

Its right side grows only like `log(p)`, unlike the earlier linear strip. This
is a structural global theorem, not a finite search result.

## 5. Verification performed

The following standalone checks were run and passed in the chat environment:

```text
python tools/verify_dual_wieferich_square_sieve_candidate.py
python tools/verify_dual_wieferich_harmonic_packing.py
```

The candidate checker exhaustively scans every exceptional progression layer
below `T=2350560`. Both checkers use only the Python standard library and exact
integer or rational arithmetic.

A complete repository-wide `python run_checks.py` run was not executed because
a fresh checkout was unavailable in the chat container. Both new checkers were
added to `run_checks.py`.

## 6. Files and commits

```text
tools/verify_dual_wieferich_square_sieve_candidate.py
docs/DUAL_WIEFERICH_SQUARE_SIEVE_CANDIDATE.md

tools/verify_dual_wieferich_harmonic_packing.py
docs/DUAL_WIEFERICH_HARMONIC_PACKING.md
```

Logical commits:

```text
9eadfc2  Add checker for the dual-Wieferich square-sieve candidate
e612b68  Prove the dual-Wieferich square-sieve candidate structure
b1540c5  Include the dual-Wieferich candidate checker
0496587  Add checker for dual-Wieferich harmonic packing
fed7ce9  Prove harmonic packing for the dual-Wieferich candidate
e5ac8ac  Include the dual-Wieferich harmonic checker
```

## 7. Decisive missing theorem

No theorem yet excludes every cycle above the finite barrier. The next target is
to combine the harmonic window with the exact near-power block ledger:

```text
D=sum ordinary deficits-sum exceptional excesses.
```

The best immediate directions are:

1. split by the number of exceptional blocks and use their permanent source
   floor;
2. derive a credit-pattern-dependent lower bound for `p*delta-D`;
3. use continued fractions only after the block credits restrict the admissible
   numerators, aiming at an infinite structural contradiction rather than a
   larger finite record.
