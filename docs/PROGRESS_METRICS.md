# Objective progress metrics

This file replaces unsupported single-number progress estimates.  A percentage
of research effort is not the same thing as a percentage of a proof.

## Reporting rule

Future checkpoints should report three separate things:

1. **strict proof gates**: which logically necessary gates are closed;
2. **frontier counts**: concrete finite quantities that decreased;
3. **research infrastructure**: reusable exact lemmas and checkers.

Do not turn these three measurements into one precise percentage unless a
weighting rule has been stated in advance.

## A. Strict prize gates

A complete solution needs all of the following.

| Gate | Meaning | Status |
|---|---|---|
| G1 | explicit odd `X>=5` and odd positive `n0` | closed for several candidates |
| G2 | orbit leaves the trivial fixed behavior and never returns to it | open for the current `X=15,n0=3` branch |
| G3 | every possible nontrivial positive cycle is excluded | open |
| G4 | bounded-orbit dichotomy is invoked correctly | closed as a general lemma |
| G5 | exact certificates and independent verification cover the final argument | infrastructure ready; final certificate open |

The prize is not solved until G2, G3, and G5 are all closed for the same
explicit pair.

## B. Current `X=15,n0=3` branch

### Closed structure

- complete valuation blocks are classified;
- every exceptional Mersenne block has a strictly smaller ordinary seed with
  the identical future tail;
- a least seed entering a hypothetical nontrivial cycle must have
  `v2(w-1) in {1,2,3}`;
- the second block cannot be exceptional;
- if the second block contracts, its terminal type must strictly increase.

### Remaining cycle subfrontier

For a least basin seed with initial type `s`:

```text
s=3:
  no contracting second block remains;

s=2:
  only terminal type 3 with 10<=k<=20 remains at the second block;

s=1:
  terminal type 2 with 21<=k<=31,
  or terminal type 3 with 10<=k<=31,
  remains at the second block.
```

This is a real reduction, but it does not control contractions after further
net-growing blocks.  The central missing cycle lemma is now a record-height or
height-credit argument that can be iterated indefinitely.

### Other open gate

The backward tree of `1` has not yet been excluded for the start `n0=3`.

## C. Huge fixed-candidate frontier

For

```text
X=104350542602662257699,
n0=1,
```

all cycle lengths through

```text
355561454311274250377
```

are excluded except two lengths.

For the first remaining length, the layer total originally allowed

```text
Q=0,...,6257.
```

The current theorem excludes only

```text
Q=6242,...,6257,
```

so the exact remaining count is

```text
6242 possible Q values.
```

This explains why the apparent progress slowed: a gigantic finite length
barrier was obtained, but the latest local improvement removed `16` of `6258`
possible layer totals at the first surviving length.  Moreover cycle lengths
above the finite barrier remain infinite in number.

## D. `X=9,n0=1` direct-growth frontier

The exact sufficient target is

```text
A_t<=3*t-1 for every t>=1.
```

The stronger inequality

```text
A_t<=3*t-2
```

has finite verification only.  Finite checked steps are evidence and must not
be counted as a fraction of an infinite proof.

## E. Recommended status wording

Use wording such as:

```text
strict prize gates closed: 2 of 5, with 3 still open;
X=15 second-block contracting families: reduced from all types to 3 finite
parameter families, but the later-block height lemma remains global;
huge-candidate first-length Q frontier: 6242 values remain;
strict problem: open.
```

A rough research-maturity estimate may still be given separately, but it must
be labeled subjective.  It must not be presented as the probability that the
proof is almost finished.
