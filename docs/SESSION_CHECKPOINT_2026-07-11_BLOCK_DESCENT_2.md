# Session checkpoint: complete block descents and literature audit

Date: 2026-07-11

The strict prize problem remains open.  This session continued the direct-growth
and infinite-descent branches rather than returning immediately to the fixed
candidate's `Q=6241` boundary.

## 1. Complete `X=13` block theorem

For

```text
3*n-1=2^(4*k+s)*u,
u odd,
s in {1,2,3},
```

the next exact valuation block is

```text
4,...,4,s
```

and its endpoint is

```text
C_13^(k+1)(n)=(13^(k+1)*u+2^(4-s))/3.
```

Every such block is universally growing through

```text
s=1: r<=37,
s=2: r<=22,
s=3: r<=11.
```

The first possible nonexceptional contractions occur only at

```text
r=41,26,15,
```

respectively.  Multiple-of-four tails reduce to the same `13n+1` rule on a
strictly smaller auxiliary integer.

Files:

```text
docs/X13_COMPLETE_VALUATION_BLOCKS.md
tools/verify_x13_complete_valuation_blocks.py
```

The checker covers `1913` parameter cases.

## 2. Complete Mersenne block theorem

For

```text
X=2^m-1,
n-1=2^(m*k+s)*u,
1<=s<=m-1,
```

the exact endpoint is

```text
C_X^(k+1)(n)=X^(k+1)*u+2^(m-s).
```

For the exceptional case `s=0`, put `w=X^(k-1)*u`.  Then

```text
C_X^k(n)=C_X(w),
w<n.
```

Thus the exceptional state and the smaller ordinary integer have literally the
same future tail after the displayed offsets.

For `X=15`, every nonexceptional block below the first thresholds

```text
r=43,86,129
```

is rigorously increasing.  The smallest possible input of an ordinary
contracting block is at least

```text
2^43+1=8796093022209.
```

Files:

```text
docs/MERSENNE_COMPLETE_VALUATION_BLOCKS.md
tools/verify_mersenne_complete_valuation_blocks.py
```

The checker covers `33616` parameter cases.

## 3. Minimal-basin consequence

If a nontrivial Mersenne cycle exists and `w` is the least positive odd integer
whose orbit enters it, then

```text
1<=v2(w-1)<m
```

and

```text
C_X(w)>w.
```

Long-zero contractions and exceptional identical-tail contractions are now
excluded at the well-founded bottom of a hypothetical basin.  For `X=15`, only
the entrance types `v2(w-1)=1,2,3` remain.

File:

```text
docs/MERSENNE_MINIMAL_BASIN_LEMMA.md
```

## 4. Tremblay `5x+1` claim audited

The claimed `17%` divergent proportion in arXiv:2104.10681 cannot be used.  The
paper counts endpoint growth as if it implied that every intermediate iterate
remained above the start.

The smallest counterexample is

```text
2 -> 1 -> 3 -> 8.
```

There are two odd steps among three, so

```text
5^2>2^3
```

and the endpoint is larger than the start, but the stopping time is already
`1`.  At length three the endpoint criterion selects starts `1,2,5,7` modulo
`8`, while the true finite-stopping-time survivors are only `1,5,7`.

Files:

```text
docs/LITERATURE_AUDIT_TREMBLAY_5X1.md
tools/verify_tremblay_5x1_audit.py
```

## 5. Current assessment

1. `X=15,n0=3` is now the cleanest infinite-descent candidate.  Exceptional
   contractions have an exact smaller ordinary replacement, unlike the `X=13`
   branch where a factor `1/3` remains.
2. The missing Mersenne lemma has been reduced to the three low-tail entrance
   types at the minimal basin seed and to ruling out the extremely deep
   nonexceptional contractions later in the orbit.
3. `X=9,n0=1` remains the cleanest cumulative-valuation candidate, but the
   required amortized suffix inequality is still unproved.
4. The huge fixed candidate remains the strongest finite cycle barrier, with
   the first remaining length restricted to `Q<=6241`.

## 6. Exact next targets

### Target A: strengthen the Mersenne minimal-basin lemma

For `X=15`, let `w` be the least seed entering a hypothetical nontrivial cycle.
Use the three exact forms

```text
w=2*u+1,
w=4*u+1,
w=8*u+1
```

and their first images to construct a smaller seed entering the same cycle, or
force a nonexceptional tail of depth at least `43`.

A proof of either alternative for all three cases would close the Mersenne cycle
branch.

### Target B: rule out return to `1` for one explicit Mersenne seed

Once nontrivial cycles are excluded, it is enough to prove that a chosen seed,
preferably `(X,n0)=(15,3)`, never reaches the trivial fixed point.  The backward
tree of `1` consists first of base-16 repunits and should be combined with the
same block descent, not with a raw trajectory scan.

### Target C: retain the independent branches

Continue the `X=9` signed-suffix accounting and the fixed candidate's exact
`Q=6241` packing improvement in parallel.  Do not treat finite trajectory
height as a proof.

## Verification

The new arithmetic checkers are included in

```text
python run_checks.py
```
