# Checkpoint: permanent labels versus cyclic closure

Date: 2026-07-17

## Question tested

Does a principle-level arithmetic contradiction arise solely from combining the
permanent residue labels modulo `N*1093^2` with cyclic wraparound of a
hypothetical positive cycle for the primary candidate?

## Result

No.  The contradiction is not merely absent from the current computation; at
this modulus it is impossible in principle.

For every cyclic valuation-label word satisfying the necessary compatibility
between residues modulo `500` and `364`, the existing `N` coordinate and the
Wieferich adjacent-label `1093^2` coordinate construct a residue word that
satisfies every accelerated transition congruence, including wraparound.  The
Chinese remainder theorem combines them into a closed cyclic residue word
modulo `N*1093^2`.

Thus the retained `16,562,000` permanent classes are an occupancy/height sieve,
not a bare cycle-closure obstruction.

Detailed theorem and checker:

```text
docs/PERMANENT_LABEL_CYCLIC_CLOSURE_NO_GO.md
tools/verify_permanent_label_cyclic_closure_no_go.py
```

## Strategy decision

Do not continue trying to contradict cyclic closure using only the present
finite labels.  The next arithmetic attempt must add genuinely global
information.  The best immediate route is to derive the first nontrivial
`1093^3` lift, where the hidden valuation layer `k_i=(a_i-s_i)/364` reappears,
and test whether its accumulated cyclic condition couples to total credit
`D` or to the exact global divisor `g`.

If that lift again closes identically after adding finitely many local labels,
then the candidate should be deprioritized in favor of either:

1. a candidate whose prime-power lift has a nontrivial global obstruction; or
2. a different strategy based on occupancy/correction rather than closure.

The strict prize target remains open; G3 remains the sole open proof gate.
