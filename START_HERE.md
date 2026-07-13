# START HERE

Compact durable entry point for each research session.

## Strict target

Find explicit positive odd `X>=5,n0` such that

```text
C_X(n)=(X*n+1)/2^v2(X*n+1)
```

tends to positive infinity. A cycle, avoidance of `1`, finite growth, a finite
barrier, or heuristic drift is not a solution.

## Read at startup

Read exactly these files, once per chat unless one changes:

```text
START_HERE.md
docs/WORKING_PROTOCOL.md
docs/CURRENT_STATUS.md
```

File roles:

- `START_HERE.md`: routing, current candidate, decisive obstruction;
- `docs/WORKING_PROTOCOL.md`: operating and verification rules;
- `docs/CURRENT_STATUS.md`: authoritative mathematical frontier;
- theorem documents and checkers: detailed proofs and certificates;
- `docs/RETRACTIONS.md`: audit history, read only when a related argument arises;
- session checkpoints and `docs/archive/`: historical handoffs, not startup memory.

Current `main` and committed checkers override chat summaries. Do not load the
whole repository or fetch an unchanged file repeatedly without a concrete need.

## Primary candidate and proof gates

```text
N=2^500-1,
B=2^4501,
d=349*2^500-347,
X=B-d=2^4501-349*2^500+347,
n0=1.
```

```text
G1 explicit pair: closed;
G2 leaves 1 and never returns: closed;
G3 all nontrivial positive cycles excluded: open;
G4 bounded positive orbit implies eventual cycle: closed;
G5 final certificate: waits for G3.
```

The strict problem remains open because G3 remains open.

## Current frontier

Retained global facts include `N|X`, `1093||X`, `16562000` permanent classes,
cycle values above `N`, exclusion through the `10^1201` window, and at least
`245833` ordinary complete blocks in every hypothetical cycle.

For the actual return from the minimum-boundary expanding exit:

```text
R>=1 => Lr>2^3990,
R<=0 => Lr>2^(2^974).
```

For complete-block lengths `ell_i`, put

```text
h=gcd_i ell_i,
D=sum_i(4501-a_i),
S_h=(B^h-X^h)/d,
g=gcd of all complete-block boundaries.
```

Exact cyclic closure proves

```text
S_h/g divides 2^D-1,
n_t==B^(-j)*S_j (mod g),  j=t mod h.
```

On the nonpositive-return branch, the exact certificate

```text
gcd(S_2,2^D-1)=1 for 1<=D<=4500
```

gives

```text
h even => full cycle p>2^(2^4979)
          and actual return Lr>2^(2^4978);
h>=2   => every block boundary shares a divisor >2^4500;
h=1    => no common geometric divisor is forced.
```

Detailed source:

```text
docs/GLOBAL_BLOCK_GCD_PHASE_SIEVE.md
tools/verify_global_block_gcd_phase_sieve.py
```

## Surviving branches and next target

```text
positive credit: Lr>2^3990;
nonpositive, h even: Lr>2^(2^4978), not excluded;
nonpositive, odd h>=3: phase-divisor sieve remains to exploit;
nonpositive, h=1: no common geometric divisor is forced.
```

Primary next target: turn the odd-`h` phase classes into a harmonic or adjacent-
numerator gcd contradiction. Secondary targets are forcing `h=1` into an
impossible return pattern and excluding the positive-credit branch.

## Non-negotiable corrections

Do not use `2^A==1 (mod X)`. The correct relation is

```text
2^A*product_i(n_i)==1 (mod X).
```

Do not identify a least admissible predecessor with the predecessor actually used
by a cycle. Never present finite computation as divergence.

## Continue instruction

A request to continue authorizes one substantial research sprint. Choose the
strongest route, verify it, save a rigorous theorem, certificate, or strict no-go,
and commit the result. Keep chat updates short; keep detailed mathematics in the
repository.