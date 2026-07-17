# Checkpoint: all finite `1093`-adic lifts are saturated

Date: 2026-07-17

## Question

Can the permanent residue labels become incompatible with cyclic closure after
lifting from `1093^2` to `1093^3` or to a higher finite power?

## Result

No.  For the primary candidate,

```text
q=1093,
h=ord_q(2)=364,
v_q(2^h-1)=2,
w=(2^h-1)/q^2 mod q=891.
```

Every compatible cyclic label word modulo `N*q^r` lifts coherently to
`N*q^(r+1)` for every `r>=2`.  The new valuation-layer digit has a nonzero
coefficient `w` and can cancel the new transition defect independently on each
edge, including wraparound, while preserving the modulo-`500` label.

Therefore every finite higher lift is saturated.  The number of allowed classes
modulo `N*q^r` is

```text
16562000*q^(r-2).
```

No finite `1093`-adic label automaton plus cyclic closure can exclude a cycle.

## Strategy decision

The proposed `1093^3` experiment and all finite continuations of it are closed
as a rigorous no-go.  Future work must use nonlocal information:

1. the exact global divisor `g`;
2. occupancy/correction bounds using the informative `q^2` classes;
3. a different prime or candidate whose new valuation digits are not locally
   free;
4. a nonlocal Diophantine estimate.

Detailed theorem and checker:

```text
docs/WIEFERICH_Q_ADIC_LIFT_SATURATION_NO_GO.md
tools/verify_wieferich_q_adic_lift_saturation.py
```

The strict target remains open; G3 is still the sole open proof gate.
