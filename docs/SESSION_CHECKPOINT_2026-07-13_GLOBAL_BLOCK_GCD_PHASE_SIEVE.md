# Session checkpoint: global block gcd and phase sieve

Date: 2026-07-13

The strict prize problem remains open. The primary candidate remains

```text
X=2^4501-349*2^500+347,
n0=1.
```

## New global theorem

Let `ell_i` be all complete-block lengths of a hypothetical cycle,
`h=gcd_i ell_i`, `c_i=4501-a_i`, `D=sum_i c_i`, and

```text
S_h=(B^h-X^h)/d.
```

If `b_i` are all complete-block boundaries and `g=gcd_i b_i`, then

```text
g=gcd(b_i,S_h) for every i,
S_h/g divides 2^D-1,
S_h/gcd(S_h,2^D-1) divides g divides S_h.
```

Moreover the entire cycle lies in the `h` explicit phase classes

```text
n_t==B^(-j)*S_j (mod g),  j=t mod h.
```

This is a global closure consequence and is not reproduced by the previous
finite CRT persistence construction.

## Primary nonpositive-return specialization

On `R<=0`, one has `1<=D<=4500`. The exact certificate verifies

```text
gcd(S_2,2^D-1)=1 for all 1<=D<=4500,
S_2=B+X.
```

Therefore an even gcd of the complete-block lengths forces `S_2` to divide every
block boundary. The whole cycle then lies in two odd residue classes modulo
`2*S_2`. Exact harmonic packing and the retained `2^-4023` continued-fraction
gap prove

```text
full cycle length p>2^(2^4979),
actual return length Lr>2^(2^4978).
```

This strictly improves the previous `2^(2^974)` nonpositive-return frontier on
the entire even-`h` subcase.

For every nonpositive-return cycle with `h>=2`, all complete-block boundaries
share a divisor greater than `2^4500`, coprime to `(2^500-1)*1093^2`.

## Verification

The standalone checker passed:

```text
4500 exact gcd checks;
exact inverse-residue and harmonic inequalities;
exit length bound L_exit<2^4006;
3 generated small near-power cycles;
X=5 regression 43 -> 27 -> 17 -> 43.
```

Files:

```text
docs/GLOBAL_BLOCK_GCD_PHASE_SIEVE.md
tools/verify_global_block_gcd_phase_sieve.py
```

A complete repository-wide run was not executed.

## Next exact target

Analyze the odd-`h` phase sieve. Either bound the reciprocal mass in its explicit
phase residues, or prove that the actual minimum-boundary return forces `h=1`.
The even-`h` branch is not excluded, but its nonpositive return is now beyond
`2^(2^4978)`.
