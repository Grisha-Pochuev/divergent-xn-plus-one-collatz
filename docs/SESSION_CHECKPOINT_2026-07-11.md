# Priority 1 checkpoint — 2026-07-11

The strict prize problem remains open.  For

```text
X  = 104350542602662257699,
n0 = 1,
```

the only cycle lengths not excluded through

```text
355561454311274250377
```

are

```text
177780727155637125193
177780727155637125195.
```

## Retained global coordinates

Let

```text
O=ord_X(2)=1860810887857924950,
a_i=s_(i+1)+O*q_i.
```

For either remaining length,

```text
sum q_i<=6257.
```

The exact symmetric edge cost

```text
c_i=(s_i-1)+(s_(i+1)-1)+2*O*q_i
```

satisfies

```text
sum c_i=2*(A-p).
```

## Retained transition concentration

With threshold `K=5000`, more than `97.38%` of all edges are zero-layer edges with adjacent-label sum at most `5001`.  Every target in that cheap majority is at least

```text
781563824454394220933608138645145,
```

so the entire cheap majority contributes less than `2.216*10^(-13)` to the reciprocal sum.

Consequently:

- at length `...195`, at least five distinct expensive targets lie below `X`;
- at length `...193`, at least `355687` distinct expensive targets lie in `(10^6,X)`;
- since at most `6257` positions have positive layer, at least `349430` of those first-length targets are zero-layer targets;
- the retained split-range certificate for `...195` requires at least `799470` values above sixty million, of which at least `793213` are zero-layer targets.

## Retained repetition and height structure

One exact zero-layer transition pair occurs at least

```text
3053943280435589
```

times in one class modulo `2*X^2`.  This gives:

```text
cycle diameter >=
66508995066170702555770104858896894988802023536957800776,
```

and a nonempty exact return segment with

```text
length <=114286,
total valuation <=7771435,
endpoints equal modulo 2*X^2.
```

The higher-power repetition ladder is

```text
2-edge word: >=3114290401257 repetitions modulo 2*X^3
3-edge word: >=2918613523 repetitions modulo 2*X^4
4-edge word: >=2251677 repetitions modulo 2*X^5
5-edge word: >=1500 repetitions modulo 2*X^6.
```

## Retained all-zero-layer minimum sieve

If every cycle edge has `q=0`, the four-generation inverse sieve proves:

```text
p=...193: a_out<=36 and n_next>1518500249*m,
p=...195: a_out<=39 and n_next>189812531*m,
```

where `m` is the cycle minimum.  This is not yet a contradiction because later contractions remain possible.

## Strongest retained reciprocal bounds

For the harder length `p=...195`, the exact cycle identity requires

```text
sum_i 1/n_i >0.099934206.
```

The signed-label potential, combined with depth-three inverse charging, rigorously proves

```text
sum_(n_i<=1000000) 1/n_i <0.085226905.
```

This numerical value was previously claimed using an invalid endpoint-identification argument.  The old proof remains retracted; the value is now independently re-established by a different telescoping potential proof in

```text
docs/SIGNED_LABEL_POTENTIAL_DUAL.md
tools/verify_signed_label_potential_dual.py
```

The strongest retained bound through sixty million remains

```text
sum_(n_i<=60000000) 1/n_i <0.086609720,
```

which forces at least `799470` values above sixty million.  The stronger figures

```text
0.086412209,
811320,
805063
```

remain retracted and must not be reused.

## Main retained additions from this work session

```text
docs/EXPENSIVE_SMALL_TARGET_MASS.md
tools/verify_expensive_small_target_mass.py

docs/DEEP_ZERO_LAYER_MINIMUM_SIEVE.md
tools/verify_deep_zero_layer_minimum_sieve.py

docs/TWO_CONSTRAINT_INVERSE_DUAL.md
tools/verify_two_constraint_inverse_dual.py

docs/SPLIT_RANGE_RECIPROCAL_DUAL.md
tools/verify_split_range_reciprocal_dual.py

docs/FORCED_ZERO_LAYER_POPULATIONS.md
tools/verify_forced_zero_layer_populations.py

docs/SIGNED_LABEL_POTENTIAL_DUAL.md
tools/verify_signed_label_potential_dual.py
```

## Exact next proof node

Do not enlarge trajectory or residue cutoffs blindly.  The next useful step is to extend the valid signed-label potential to a larger target range while keeping every admissible layer logically separate, or to construct a finite-state potential on zero-layer predecessor carries.  A successful certificate must couple the mandatory zero-layer populations to a contradiction in the global reciprocal or height balance.

A finite barrier, an enormous maximum, or a long growing block is not divergence.
