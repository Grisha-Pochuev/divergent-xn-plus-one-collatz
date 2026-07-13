# START HERE

Durable entry point for each research session.

## Strict target

Find explicit positive odd `X>=5,n0` such that

```text
C_X(n)=(X*n+1)/2^v2(X*n+1)
```

tends to positive infinity. A cycle, avoidance of `1`, finite growth, or
heuristic drift is not a solution.

## Read first

```text
START_HERE.md
docs/WORKING_PROTOCOL.md
docs/CURRENT_STATUS.md
docs/RETRACTIONS.md
docs/SESSION_CHECKPOINT_2026-07-13_GLOBAL_BLOCK_GCD_PHASE_SIEVE.md
```

Current `main` and committed checkers override chat summaries. Read these startup
files once per chat unless one of them changes. Do not load the full repository
or repeat an unchanged fetch without a concrete need.

## Research protocol

A request to continue authorizes one substantial sprint. Choose the strongest
route, verify it, commit it, and distinguish theorem, certificate, evidence,
refutation, and open target. Literature, exact arithmetic, symbolic methods,
finite searches, SAT/SMT, and theorem provers are allowed. Do not enlarge a
finite record without new information about an infinite orbit or exact closure.

Keep one primary proof target and at most two active exploratory directions. A
third idea may be screened briefly only to discard it or replace an active
branch. Run targeted standalone checks first; reserve the full repository suite
for major milestones, shared-infrastructure changes, or a reliable environment.
Prefer one coherent result commit per sprint. A separate session checkpoint is
needed only when the primary frontier, decisive obstruction, retraction, or
handoff state changes.

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

Retained facts include `N|X`, `1093||X`, `16562000` permanent classes modulo
`N*1093^2`, cycle values above `N`, the `10^1201` cycle window exclusion, and at
least `245833` ordinary complete blocks in every hypothetical cycle.

## Minimum-boundary return frontier

Every hypothetical cycle has an actual consecutive expanding exit from its
least ordinary boundary with

```text
1<=C<=4500,
complete blocks<=4500,
L*log2(B/X)<C,
endpoint y>starting value x.
```

The remaining actual return satisfies

```text
R>=1 => Lr>2^3990,
R<=0 => Lr>2^(2^974).
```

## Exact closure and closed local routes

For a complete cyclic valuation word,

```text
Delta=2^A-X^p,
2^a_k*Q_(k+1)=X*Q_k+Delta.
```

It closes to a positive cycle iff `Delta>0` and `Delta|Q_0`, equivalently iff

```text
gcd(Q_k,Q_(k+1))=Delta
```

for a truly adjacent pair.

For a complete near-power block,

```text
S_ell=(B^ell-X^ell)/d,
gcd(n,n')=gcd(n,S_ell),
gcd(S_r,S_s)=S_gcd(r,s).
```

Local endpoint congruences, full finite word gluing, naive block compression,
and finite repeated-defect arguments are closed: CRT can realize all of them
without supplying exact cyclic source matching.

## Global block-gcd and phase sieve

Let `ell_i` be all complete-block lengths of a hypothetical cycle and put

```text
h=gcd_i ell_i,
D=sum_i(4501-a_i),
S_h=(B^h-X^h)/d,
g=gcd of all complete-block boundaries.
```

Exact closure proves

```text
g=gcd(b_i,S_h) for every boundary b_i,
S_h/g divides 2^D-1,
S_h/gcd(S_h,2^D-1) divides g divides S_h.
```

The entire cycle obeys

```text
n_t==B^(-j)*S_j (mod g),
j=t mod h.
```

On the nonpositive-return branch `1<=D<=4500`, the exact certificate

```text
gcd(S_2,2^D-1)=1 for all 1<=D<=4500
```

implies

```text
h even => full cycle p>2^(2^4979)
          and return Lr>2^(2^4978);
h>=2   => every block boundary shares a divisor >2^4500;
h=1    => no common geometric divisor is forced.
```

Files:

```text
docs/GLOBAL_BLOCK_GCD_PHASE_SIEVE.md
tools/verify_global_block_gcd_phase_sieve.py
```

## Decisive missing theorem

The best next targets are:

1. obtain a harmonic contradiction from the odd-`h` phase classes;
2. prove the actual return forces `h=1` or another impossible length pattern;
3. use the phase sieve to make an adjacent numerator gcd smaller than `Delta`;
4. exclude the positive-credit return branch;
5. find a different candidate or direct divergence invariant.

## Non-negotiable corrections

Do not use `2^A==1 (mod X)`. The correct relation is

```text
2^A*product_i(n_i)==1 (mod X).
```

Do not identify a least possible predecessor with the predecessor actually used
by a cycle. Never present finite computation as divergence.
