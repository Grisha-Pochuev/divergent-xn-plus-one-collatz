# The Open Mathematics Project

## Divergent accelerated `Xn+1` orbit

For odd `X>=5`, define

```text
C_X(n)=(X*n+1)/2^v2(X*n+1)
```

on positive odd integers. The strict target is one explicit pair `(X,n0)` whose
orbit tends to positive infinity. A cycle, avoidance of `1`, a long finite
trajectory, or a finite cycle barrier is not a solution.

## Start here

```text
START_HERE.md
docs/CURRENT_STATUS.md
docs/RETRACTIONS.md
docs/SESSION_CHECKPOINT_2026-07-12_MERSENNE_DIVISOR_FAMILY_FRONTIER.md
run_checks.py
```

## Strongest current branch

The strict problem is not solved. The primary candidate is

```text
X=2^4501-349*2^500+347,
n0=1.
```

Put

```text
N=2^500-1,
d=349*2^500-347.
```

The repository proves:

- `N|X` and `1093||X`;
- the orbit leaves `1` and never returns;
- every hypothetical cycle value is greater than `N`;
- every output lies in `500` one-label classes modulo `N`;
- after combining with the `1093^2` adjacent-label coordinate, exactly
  `16562000` permanent classes remain modulo `(2^500-1)*1093^2`;
- every positive cycle length `p` must satisfy

```text
p>2*X/(3*d),
10^1201<floor(2*X/(3*d))<10^1202;
```

- the combined harmonic base constant is below `10^(-147)` and the tail
  coefficient is below `10^(-149)`;
- every exceptional cycle source is at least

```text
(u_min*2^4501+1)/(349*2^500-347),
```

  where the exact `u_min` is recorded in
  `docs/MERSENNE_DIVISOR_EXCEPTIONAL_FLOOR.md`; the lower-bound source has
  `1505` decimal digits.

These are necessary structural constraints, not yet a proof of divergence.

## Reusable construction theorem

For

```text
N=2^k-1,
m==r (mod k),
d=2^r+t*N,
X=2^m-d,
```

one can choose suitable parity-correct `t` with `1093||X`. This produces an
infinite family with:

- no return to `1` from `n0=1`;
- only `k` output classes modulo `N`;
- exponentially thin combined residue density;
- arbitrarily large finite cycle barriers.

Therefore simply making the modulus or barrier larger is no longer the central
research target. The missing theorem must couple valuation-label transitions,
near-power block credits, and height-dependent correction bounds.

Main files:

```text
docs/MERSENNE_DIVISOR_WIEFERICH_FAMILY.md
tools/verify_mersenne_divisor_wieferich_family.py
docs/MERSENNE_DIVISOR_EXCEPTIONAL_FLOOR.md
```

## Current exact target

For a hypothetical cycle of length `p`, total valuation `A`, let

```text
D=4501*p-A,
delta=log2(2^4501/X).
```

The project has an exact block ledger

```text
D=sum ordinary deficits-sum exceptional excesses
```

and a harmonic upper window

```text
0<p*delta-D
 <[C0+K*H_(ceil(p/K))/(2*M)]/(X*ln(2)),
C0<10^(-147).
```

The next proof step splits hypothetical cycles into zero, one, or multiple
exceptional blocks and seeks a matching lower bound for `p*delta-D` in each
case.

## Independent fallback results

The repository retains several separately verified branches, including:

```text
X=2^3803-4162203,
X=2^156-9,
X=2^260-3,
X=15,
X=9.
```

For the older fixed candidate

```text
X=104350542602662257699,
n0=1,
```

all positive cycle lengths through

```text
177780727155637125192
```

are excluded, and all lengths through

```text
355561454311274250377
```

are excluded except

```text
177780727155637125193,
177780727155637125195.
```

These older frontiers remain reproducible but are no longer the primary branch.

## Important retraction

The former `10^37` barrier is retracted. It incorrectly assumed

```text
2^A==1 (mod X).
```

The correct congruence is

```text
2^A*product_i(n_i)==1 (mod X).
```

The accelerated `5n+1` cycle `13 -> 33 -> 83 -> 13` is the regression
counterexample.

## Reproduction

No external Python packages are required.

```bash
python run_checks.py
```

The modular sieves are deterministic certificate checks, not Collatz trajectory
searches.

## Repository layout

```text
START_HERE.md   Durable entry point.
docs/           Proof notes, status, audits, and roadmap.
tools/          Exact verification scripts.
tests/          Independent tests and regressions.
results/        Exploratory outputs, never treated as proof.
```

## License

MIT.
