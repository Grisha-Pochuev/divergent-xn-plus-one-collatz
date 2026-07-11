# Objective progress metrics

This file replaces unsupported single-number progress estimates. A percentage
of research effort is not the same thing as a percentage of a proof.

## Reporting rule

Future checkpoints report three separate things:

1. **strict proof gates**: which logically necessary gates are closed;
2. **finite frontiers**: exact quantities that were reduced;
3. **structural depth**: reusable infinite-family lemmas and independent checks.

Do not combine these into one precise percentage. The last global theorem may
contain most of the mathematical difficulty even when many preparatory gates are
closed.

## A. Strict prize gates

A complete solution needs the following for one explicit pair.

| Gate | Meaning | Current structured candidate `X=2^156-9,n0=1` |
|---|---|---|
| G1 | explicit odd `X>=5` and positive odd `n0` | closed |
| G2 | orbit leaves `1` and can never return to it | closed |
| G3 | every nontrivial positive cycle is excluded | open |
| G4 | positive bounded-orbit dichotomy is applied correctly | closed as a general lemma |
| G5 | exact independent verification covers the final proof | partial; final certificate waits for G3 |

Thus three logical gates are available, but the decisive global cycle gate G3
is still open. These gates are not equally difficult and must not be converted
to `60% solved`.

## B. Structured hybrid candidate

```text
X=2^156-9
 =91343852333181432387730302044767688728495783927,
n0=1.
```

### Closed

- `1093` divides `X` exactly once;
- the Wieferich mechanism proves that the orbit never returns to `1`;
- all positive cycles of length at most

```text
6766211283939365362054096447760569535444132142
```

  are excluded;
- every near-power valuation block is classified exactly;
- the first `48` accelerated steps have the exact word

```text
(3,1,2,2,5,6)^8
```

  and total valuation `152`;
- after that program, `v2(n_48-1)=4` and
  `n_48>X^48/2^152`.

### Open

- cycles above the finite barrier remain infinite in number;
- the exact repeated initial program ends after eight blocks;
- no renewal or height-credit theorem yet forces another long program;
- therefore G3 remains one global theorem, not a finite list nearing zero.

## C. Larger-barrier hybrid candidate

```text
X=2^260-3,
n0=1.
```

Closed measurements:

- return to `1` is impossible;
- all positive cycle lengths through approximately `4.117*10^77` are excluded;
- the first `172` accelerated steps have the exact word `(1,2)^86` and total
  valuation `258`;
- a least seed entering a hypothetical cycle must satisfy
  `1<=v2(3*w-1)<=259` and its first step grows.

This candidate has the stronger finite barrier. The `2^156-9` candidate has the
cleaner repeated six-step program and is currently preferred for renewal work.

## D. `X=15,n0=3` Mersenne branch

Closed structure:

- complete valuation blocks are classified;
- exceptional blocks have a strictly smaller ordinary seed with the identical
  future tail;
- a least seed entering a hypothetical cycle has `v2(w-1) in {1,2,3}`;
- the second block cannot be exceptional;
- if the second block contracts, its terminal type strictly increases.

Remaining contracting second-block families:

```text
initial type 3: none;
initial type 2: terminal type 3, 10<=k<=20;
initial type 1: terminal type 2, 21<=k<=31,
                or terminal type 3, 10<=k<=31.
```

The later-block height theorem and avoidance of `1` remain open.

## E. Huge fixed-candidate frontier

For

```text
X=104350542602662257699,
n0=1,
```

all cycle lengths through `355561454311274250377` are excluded except two.
For the first surviving length, the layer total originally allowed
`Q=0,...,6257`; only `Q=6242,...,6257` have been removed. Therefore

```text
6242 possible Q values remain.
```

This was the clearest reason the old percentage began moving slowly: the latest
strict local improvement removed `16` of `6258` layer totals, while lengths
above the finite barrier remain unbounded.

## F. `X=9,n0=1` direct-growth frontier

The exact sufficient target remains

```text
A_t<=3*t-1 for every t>=1.
```

Finite checked prefixes are evidence only and are never counted as a fraction
of an infinite theorem.

## G. Recommended status wording

Use wording such as:

```text
strict target: open;
G1, G2 and the general dichotomy are closed for X=2^156-9;
decisive remaining gate: exclusion of every nontrivial positive cycle;
finite barrier: 6.766*10^45 steps;
exact initial program: 48 steps in eight proved macroblocks;
research maturity: high, but proof completion has no defensible percentage.
```
