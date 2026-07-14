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

On the nonpositive-return branch, `1<=D<=4500`.

- `h` even: `gcd(S_2,2^D-1)=1` forces the two-phase sieve.
- `h` odd and `h>=3`: `S_h>h*X^(h-1)` gives
  `g/h>X^2/2^4500`; phase-wise harmonic packing then gives the same frontier.

Therefore every nonpositive-return cycle with `h>=2` satisfies

```text
full cycle p>2^(2^4979),
actual return Lr>2^(2^4978).
```

The signed complete-block elimination theorem and the small credit range now also
force enormous ordinary-block populations:

```text
any nonpositive return:
  ordinary blocks J>2^(2^973-7),
  one deficit type repeats >2^(2^973-20) times;

nonpositive with h>=2:
  ordinary blocks J>2^(2^4978-7),
  one deficit type repeats >2^(2^4978-20) times.
```

A new exact no-go proves that every finite list of same-deficit complete blocks,
with arbitrary prescribed lengths, is realized by infinitely many positive exact
segments. For the primary candidate, even the endpoint classes modulo every
fixed finite power `N^s` remain locally realizable. Thus finite repetition and
finite `N`-adic depth cannot by themselves close G3.

Detailed sources:

```text
docs/GLOBAL_BLOCK_GCD_PHASE_SIEVE.md
tools/verify_global_block_gcd_phase_sieve.py
docs/ODD_H_PHASE_HARMONIC_BARRIER.md
tools/verify_odd_h_phase_harmonic_barrier.py
docs/NONPOSITIVE_RETURN_ORDINARY_BLOCK_EXPLOSION.md
tools/verify_nonpositive_return_ordinary_block_explosion.py
docs/SAME_DEFICIT_FINITE_PERSISTENCE_NO_GO.md
tools/verify_same_deficit_finite_persistence.py
```

## Surviving branches and next target

```text
positive credit: Lr>2^3990;
nonpositive, h>=2: Lr>2^(2^4978) and J>2^(2^4978-7), still not excluded;
nonpositive, h=1: Lr>2^(2^974) and J>2^(2^973-7).
```

Primary next target: turn the doubly exponential repeated population into a
genuinely global correction. The proof must use exact cyclic source matching,
force a harmonic or height contribution from the repeated type, or exploit an
interaction with exceptional blocks that arbitrary finite word coding cannot
reproduce. Do not pursue the same residue class plus any fixed finite `N`-adic
ladder as a standalone contradiction. Secondary target: exclude the
positive-credit return branch.

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
