# Session checkpoint: geometric-factor persistence no-go

Date: 2026-07-13

The strict prize problem remains open. The primary candidate remains

```text
X=2^4501-349*2^500+347,
n0=1.
```

The two surviving return branches remain

```text
positive credit with Lr>2^3990;
nonpositive credit with Lr>2^(2^974).
```

## New exact theorem

For

```text
S_ell=(B^ell-X^ell)/d,
B=2^m,
X=B-d,
```

the complete-block geometric factors form a strong divisibility sequence:

```text
gcd(S_r,S_s)=S_gcd(r,s).
```

They also satisfy

```text
gcd(S_ell,B*X)=1,
gcd(S_ell,d)=gcd(ell,d).
```

For block-boundary defects

```text
g_i=gcd(n_i,n_(i+1))=gcd(n_i,S_(ell_i)),
```

any prime common to several `g_i` is restricted by the gcd of the corresponding
block lengths.

## New strict local no-go

The restriction above does not itself restore coprimality. For any prescribed
finite list of complete blocks whose lengths have common divisor `h>=2`, choose
an odd prime `q|S_h`. Exact valuation-word coding and CRT give infinitely many
positive odd finite orbit segments for which `q` divides every block boundary.
Thus the same defect prime can persist through arbitrarily many prescribed
complete-block compressions.

Regression:

```text
X=5,
lengths=(2,4,6),
q=13,
boundaries=
2620090395 -> 4093891243 -> 1249356459 -> 297869793,
boundary gcd defects=(13,13,39).
```

This closes the local shortcut that repeated block compression should
necessarily wash out the extra geometric gcd. A successful proof now needs
actual global information forcing suitable block-length gcd `1`, excluding all
allowed persistent primes, or retaining a truly adjacent accelerated pair.

## Primary specialization

For the retained multiplier,

```text
gcd(S_ell,(2^500-1)*1093^2)=1
```

for every `ell`. Hence the geometric defect has no prime from the permanent
sieve modulus; any interaction with that sieve must be through the actual source
classes, not direct factor overlap.

## Verification

The standalone checker passed:

```text
lucas pair checks=71136;
exact complete blocks=1990;
persistent boundary constructions=116;
primary specialization lengths=24;
X=5 regression verified exactly.
```

An independent brute-force check verified unique exact word residues in `30`
small cases. A complete repository-wide run was not executed.

Files:

```text
docs/GEOMETRIC_FACTOR_STRONG_DIVISIBILITY_PERSISTENCE_NO_GO.md
tools/verify_geometric_factor_strong_divisibility.py
```

## Next exact target

Use the strong-divisibility classification on the **actual** minimum-boundary
segment or return word. The next useful question is whether the permanent-sieve
classes and exact return closure force a selected family of actual complete
block lengths to have gcd `1`, or exclude every prime divisor of
`S_gcd(lengths)`. Purely local concatenation cannot do this.
