# Session checkpoint: nonpositive return harmonic barrier

Date: 2026-07-12

The strict prize problem remains open. The primary candidate remains

```text
X=2^4501-349*2^500+347,
n0=1.
```

## Retained frontiers

- every hypothetical cycle has at least `245833` ordinary complete blocks;
- the least ordinary boundary starts an actual consecutive segment ending at a
  larger ordinary boundary;
- that exit has credit `1<=C<=4500`, exceptional excess at most `4499`, and at
  most `4500` complete blocks.

## Return-credit results

Let `R` and `L` be the net credit and accelerated length of the actual remaining
orbit from the larger endpoint back to the least ordinary boundary.

The previously proved dichotomy gives

```text
R>=1 => L>2^3990.
```

The new harmonic-packing theorem gives

```text
R<=0 => L>2^(2^974).
```

The proof combines:

1. `D=C+R`, so a nonpositive return forces total cycle credit `1<=D<=4500`;
2. the continued-fraction gap `p*ln(B/X)-D*ln(2)>2^-4023`;
3. the `16562000` permanent classes modulo `(2^500-1)*1093^2`;
4. harmonic packing of at most `2^(2^974)` distinct return values;
5. the existing independent correction bound for the short expanding exit.

The exact checker obtains

```text
correction upper * 2^4023 = 0.433233945702880...,
gap lower        * 2^4023 = 1.718676385119249....
```

Files:

```text
docs/MINIMUM_BOUNDARY_NONPOSITIVE_RETURN_HARMONIC_BARRIER.md
tools/verify_minimum_boundary_nonpositive_return_harmonic_barrier.py
```

Both return checkers are included in `run_checks.py`. The new standalone checker
passed in the chat environment. A complete repository-wide run was not executed.

## Remaining obstruction

A hypothetical cycle can now survive only through an actual return satisfying
one of:

```text
positive credit and L>2^3990;
nonpositive credit and L>2^(2^974).
```

The next target should not be another finite cutoff. It should be a
length-independent obstruction, preferably inverse `X`-adic descent through the
positive-credit return word or an endpoint incompatibility modulo `X^2` or a
higher power.