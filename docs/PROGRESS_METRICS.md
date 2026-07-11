# Objective progress metrics

Research effort is not a linear fraction of a proof.  Checkpoints therefore
report:

1. strict logical gates;
2. exact finite frontiers;
3. reusable infinite-family structure.

## A. Strict prize gates

For the primary candidate `X=2^156-9,n0=1`:

| Gate | Meaning | Status |
|---|---|---|
| G1 | explicit odd `X>=5` and positive odd `n0` | closed |
| G2 | orbit leaves `1` and never returns | closed |
| G3 | every nontrivial positive cycle is excluded | open |
| G4 | bounded positive orbit implies eventual cycle | closed as a general lemma |
| G5 | independent verification covers the final proof | partial; waits for G3 |

G3 is the decisive global theorem and may contain most of the remaining
difficulty.  The table must not be converted mechanically into `60% solved`.

## B. Primary candidate measurements

```text
X=2^156-9
 =91343852333181432387730302044767688728495783927,
n0=1.
```

### Exact finite frontiers

- all positive cycle lengths through

```text
7034970411803187993997906985047212163795395134
```

  are excluded;
- the first `48` accelerated steps are exactly

```text
(3,1,2,2,5,6)^8;
```

- the permanent adjacent-label sieve leaves exactly

```text
132496
```

  classes modulo `1093^2`;
- every exceptional source in a hypothetical cycle is at least

```text
1268664615738631005385143083955106787895774776889.
```

### Reusable infinite-family structure

- the Wieferich mechanism forbids return to `1`;
- every near-power complete block is classified exactly;
- all `155` ordinary terminal deficits have sharp growth/contraction thresholds;
- every hypothetical cycle has a canonical complete-block partition;
- its exact credit balance is

```text
D=156*p-A
 =sum ordinary deficits-sum exceptional excesses;
```

- every exceptional block ending at `156+b` loses more than `b` binary height
  units;
- the exact block correction identity and its uniform bound force

```text
p*(delta-9/(2*X*ln(2)))<D<p*delta,
delta=log2(2^156/X).
```

This restricts `D` to roughly the upper half of the old interval.

### Still open

- cycles above the finite barrier remain infinite in number;
- the initial eight macroblocks do not have a proved infinite renewal;
- no harmonic or height-credit contradiction yet excludes all cycles;
- the exact correction mass `p*delta-D` has not yet been proved impossible.

## C. Independent fallback branches

### `X=2^260-3,n0=1`

Return to `1` is impossible, all positive cycle lengths through approximately
`4.117*10^77` are excluded, and the first `172` steps have exact word
`(1,2)^86`.

### `X=15,n0=3`

Complete Mersenne blocks and second-block escalation are classified.  The later
height theorem and avoidance of `1` remain open.

### `X=9,n0=1`

The sufficient target is still

```text
A_t<=3*t-1 for every t>=1.
```

### Previous fixed candidate

All cycle lengths through `355561454311274250377` are excluded except

```text
177780727155637125193,
177780727155637125195.
```

At the first surviving length, `6242` layer totals remain.

## D. Honest approximate wording

A rough planning estimate may be stated only as a range:

```text
research maturity: about 30-40%;
strict target: open;
decisive remaining gate: global exclusion of every nontrivial positive cycle.
```

This range describes accumulated structure, not a measured probability of
success.  A single global lemma could finish the proof, or could contain most
of the remaining work.
