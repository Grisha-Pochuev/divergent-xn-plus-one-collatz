# Prioritized next steps

The strict prize problem remains open. This file separates proved frontiers from concrete next actions.

## Priority 1: eliminate the six exceptional lengths

Current candidate:

```text
X  = 104350542602662257699,
n0 = 1.
```

Current contiguous barrier:

```text
p <= 177780727155637125184.
```

Current sparse cap:

```text
p <= 355561454311274250377.
```

Within that larger range, only six odd lengths remain:

```text
177780727155637125185
177780727155637125187
177780727155637125189
177780727155637125191
177780727155637125193
177780727155637125195
```

### What is rigorously closed

Do not repeat any search for forbidden finite words using only:

- the `2154` output class labels modulo `2M`;
- exact valuation labels;
- the layer `q=(a-t)/2154`;
- any bounded finite window of those labels.

The bare graph is complete, and every compatible augmented finite exact-valuation path is realized by infinitely many positive starts.

Files:

```text
docs/RESIDUE_TRANSITION_NO_GO.md
docs/AUGMENTED_TRANSITION_NO_GO.md
tools/verify_residue_transition_no_go.py
tools/verify_augmented_transition_no_go.py
```

### Retained quantitative tools

For a hypothetical cycle of length `p`, with class occupancies `c_t`,

```text
sum_t c_t = p,
sum_t t*c_t <= 67p-1.
```

Cycle closure gives exact source/target flow balance. The large divisor

```text
P = 6911089648497401
```

also makes each exact incoming valuation occupy one sparse progression modulo `2P`.

The best current reciprocal envelope for the first exceptional length is approximately

```text
2.527289.
```

This was enough to eliminate the first of the original seven exceptions, but not the next six by the same inequality alone.

### Immediate exact target

For each remaining length `p`, the power-of-two interval fixes the total valuation `A` exactly. Combine that fixed value with the global identities

```text
sum_i (2^a_(i-1)-X)*n_i = p,
```

and

```text
sum_i (2^a_i-X)/n_i
 = sum_i 1/(n_i*n_(i+1)) > 0.
```

Concrete tasks:

1. Split valuations into `a<=66` and `a>=67`; use the fixed total `A` to constrain both counts and total excess.
2. Couple a large valuation spike to its successor height through

```text
n_(i+1) = (X*n_i+1)/2^a_i.
```

3. Derive a rational potential or charging scheme whose sum around a cycle contradicts one of the two global identities.
4. Use exact progression costs modulo the full multiplier `X`, not only modulo `M` or `P`, when a finite set of relevant valuation residues can be isolated.
5. Treat each of the six lengths separately if needed; eliminating the first remaining value immediately raises the contiguous barrier by two.

No long trajectory search is required.

### Secondary Priority 1 target: repeat sparse windows

The first interval crossing shows that difficult lengths occur only in narrow neighborhoods of near-powers of two. Generalize the exact phase argument:

1. locate successive crossings of `p*log(X)` with integer multiples of `log(2)` using rational bounds;
2. prove large safe intervals between crossings;
3. bound the number and width of exceptional windows;
4. seek a uniform argument eliminating every window.

A sequence of sparse windows is not yet a proof of divergence, but it can convert almost all lengths into a structured Diophantine exceptional set.

## Priority 2: combine cycle-height upper and lower bounds

The logarithmic reduction gives

```text
minimum cycle element <= K_X*p^D_X.
```

Needed:

1. make `K_X,D_X` explicit;
2. derive a modular lower bound growing with `p`;
3. prove the lower bound eventually exceeds the polynomial upper bound;
4. use finite exact certificates for the remaining lengths.

A constant lower bound such as `25` cannot finish this route.

## Priority 3: ordinary-integer regenerative chain

For `X=2^m+1`, study

```text
u -> odd_part(X^L*u-1).
```

The unresolved goal is one ordinary positive start supporting infinitely many net-positive complete bursts. Finite programs are already exactly realizable but do not stabilize to one start.

## Priority 4: stabilized low-average valuation code

Construct an actual ordinary positive orbit satisfying

```text
limsup average(a_t) < log2(X).
```

Arbitrary infinite symbolic words are insufficient; eventual stabilization of coding representatives is necessary.

## Priority 5: digital invariant for `X=9, n0=1`

The exact transformed recurrence is

```text
S_0=1,
S_(t+1)=9*S_t+2^v2(S_t),
v2(S_t)=A_t.
```

A proof of `v2(S_t)<=3t-1` for every `t>=1` would imply divergence. This route was not pursued in the present Priority 1 session.

## Lightweight verification tasks

Safe inside a normal chat session:

- exact modular arithmetic;
- symbolic derivations;
- short deterministic residue enumeration;
- rational interval bounds;
- regression checks on known cycles;
- documentation consistency checks.

## Tasks requiring explicit user approval

Do not start automatically:

- multi-hour trajectory scans;
- large parameter searches;
- large GitHub Actions matrices;
- exhaustive high-memory searches;
- repeated numerical work where a symbolic bound is available.

## Acceptance checklist for a final proof

A claimed solution must provide:

1. explicit odd `X>=5` and odd positive `n0`;
2. proof that the orbit cannot enter any positive cycle;
3. proof that it cannot return to a previous value;
4. the positive-integer dichotomy forcing `+infinity`;
5. exact independently runnable verification of every finite certificate;
6. no reliance on random-model assumptions or finite trajectory size.

## Recommended next session

Continue Priority 1 with:

> For the six listed odd lengths, can the fixed total valuation and the global height/reciprocal balance identities force a contradiction, perhaps after charging every `a>=67` spike against neighbouring low-valuation steps?

Do not return to local forbidden-word enumeration.