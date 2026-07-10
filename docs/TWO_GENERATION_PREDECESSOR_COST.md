# Two-generation predecessor cost

Fix

```text
X = 104350542602662257699,
M = 15099,
O = ord_X(2) = 1860810887857924950,
R = 3M = 45297.
```

The permanent mod-3 sieve removes a value if every direct predecessor is
divisible by `3`.  This note strengthens it: even when a coprime predecessor
exists, several full periods of the order `O` may be required before that
predecessor is itself an admissible accelerated output.

## 1. Direct-predecessor progression

Let `n` be an accelerated output, and let `s` be its least positive full label:

```text
1 <= s <= O,
2^s*n == 1 (mod X).
```

All possible incoming exact valuations are

```text
a = s+kO,  k>=0,
```

and their direct predecessors are

```text
m_k = (2^(s+kO)*n-1)/X.
```

Put

```text
U = 2^O,
C = (U-1)/X.
```

Then exactly

```text
m_(k+1) = U*m_k+C.
```

The exact certificate proves

```text
U == 1 (mod R),
C == 22062 (mod R).
```

Therefore

```text
m_k == m_0+22062*k (mod 45297).                 (1)
```

Since

```text
gcd(22062,45297)=3,
```

(1) has one cycle of length `15099` in each residue class modulo `3`.

## 2. Admissible predecessor states

A residue `m modulo R` is called one-generation admissible when:

1. `m modulo M` is one of the `2154` output residues `2^(-t)`;
2. its own permanent mod-3 predecessor test is not dead.

There are exactly

```text
4308
```

such states: `2154` with residue `1 modulo 3` and `2154` with residue `2 modulo
3`.  There are none with residue `0 modulo 3`.

For a state `r`, define `d(r)` as the least `k>=0` for which

```text
r+22062*k (mod R)
```

is one-generation admissible.  If no such `k` exists, put `d(r)=infinity`.

The finite exact state calculation gives:

```text
d(r)=infinity exactly for the 15099 states r==0 (mod 3),
0 <= d(r) <= 41 for every other state.
```

The maximum finite distance `41` is attained.

## 3. Pointwise cycle cost

Suppose `n` belongs to a cycle reached from `1`.  Its actual predecessor is
some `m_k`.  That predecessor is itself an accelerated output and must therefore
be one-generation admissible.  By the definition of `d`,

```text
k >= d(m_0 mod R).
```

Consequently the incoming exact valuation of `n` satisfies the pointwise bound

```text
a >= s+O*d(m_0 mod R).                          (2)
```

If `d=infinity`, the value is unreachable, recovering the permanent mod-3
sieve.  Otherwise (2) can add as many as `41` complete order periods to the
minimum valuation cost of a small reciprocal contributor.

This cost may be summed over distinct cycle elements because every cycle
element has its own incoming valuation and the total of those valuations is
exactly the cycle total `A`.

## 4. Explicit examples

For the genuine full representatives

```text
n=25:   s=1208196370322173126, d=13,
n=163:  s=1014347647263805892, d=1,
n=547:  s=1820296293532601562, d=0,
n=457:  d=infinity.
```

Thus `457` is removed already by the permanent sieve, while a cycle occurrence
of `25` costs at least

```text
1208196370322173126 + 13*1860810887857924950
```

units of total valuation, not merely its least full label.

## 5. Significance and limitation

This is the first retained transition constraint that charges an actual value
using two consecutive generations of the inverse orbit.  It is stronger than
independent activation prices and does not use a long trajectory search.

It is still a necessary condition rather than a complete cycle exclusion.  A
next certificate should combine (2) with reciprocal values and the fixed total
valuation at the two remaining sparse-window lengths.

Run

```text
python tools/verify_two_generation_predecessor_cost.py
```

for the finite exact state certificate.
