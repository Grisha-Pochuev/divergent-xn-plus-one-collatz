# Prioritized next steps

The strict prize problem remains open.

## Priority 1: eliminate the final two lengths in the first sparse window

Current candidate:

```text
X  = 104350542602662257699,
n0 = 1.
```

Current contiguous barrier:

```text
p <= 177780727155637125192.
```

Current sparse cap:

```text
p <= 355561454311274250377.
```

Only two lengths remain in that larger range:

```text
177780727155637125193
177780727155637125195.
```

### Closed routes

Do not repeat searches for forbidden finite words using residue labels, exact valuations, finite height layers, or bounded windows of them. Every compatible finite path is realizable by infinitely many positive starts.

Do not merely enlarge the small subgroup sieve to billions of candidates. The last two exact interval thresholds are approximately

```text
0.506785307
0.099934207,
```

so a qualitatively stronger coupling is needed.

### Retained tools

For a hypothetical cycle:

```text
sum c_t=p,
sum t*c_t<=67p-1,
A >= p + m*(m-1)/2,
```

where `m` is the number of active full output classes modulo `2X`.

Every cycle also satisfies

```text
sum_i (2^a_(i-1)-X)*n_i = p,
```

and

```text
sum_i (2^a_i-X)/n_i
 = sum_i 1/(n_i*n_(i+1)) > 0.
```

The exact group data are

```text
ord_M(2)=2154,
ord_P(2)=(P-1)/8,
ord_X(2)=1860810887857924950.
```

### Immediate target A: exact activation-price certificate

For every genuine small full representative `n`, compute its exact minimum activation label `s` satisfying

```text
n == 2^(-s) (mod X).
```

Then solve or bound the weighted selection problem:

```text
maximize sum 1/n
subject to
sum activation_cost <= A
and at most p selected occurrences.
```

Use a rational Lagrange-dual inequality, not a large combinatorial search. The exact order factorization is smooth enough for Pohlig-Hellman discrete logarithms.

### Immediate target B: neighbour-height charging

Use the fixed total valuation and the two global transition identities to charge every `a>=67` step against neighbouring low-valuation steps. Seek a telescoping potential or signed inequality that bounds the reciprocal sum more sharply than independent full-class activation.

### Secondary target: next sparse window

Generalize the rational phase argument beyond the first crossing. Locate later narrow exceptional windows and prove safe intervals between them. This does not solve divergence but structures almost all lengths into sparse Diophantine windows.

## Other routes

### Cycle-height route

Make the polynomial upper bound on the minimum cycle element explicit and combine it with a modular lower bound that grows with length.

### Regenerative-chain route

For `X=2^m+1`, construct one ordinary positive start supporting infinitely many net-positive complete bursts.

### Stabilized valuation-code route

Find one actual positive orbit with eventual average valuation below `log2(X)`.

### `X=9` digital invariant

A proof of `v2(S_t)<=3t-1` for the transformed `9n+1` recurrence would imply divergence. This route is outside the present Priority 1 session.

## Restrictions

No long trajectory scans, large parameter searches, or large Actions matrices without explicit approval. Exact modular checks and compact deterministic certificates are allowed.

## Final-proof checklist

A valid prize solution must provide an explicit pair, exclude every positive cycle, exclude repetition, invoke the positive-orbit dichotomy, and supply independently runnable exact certificates.

## Recommended next session

> Eliminate `177780727155637125193` and `177780727155637125195` using exact full-class activation prices or a global neighbour-height potential. Do not return to local transition words or brute-force cutoff growth.