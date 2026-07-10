# Current status

## Strict target

Find explicit odd positive `X>=5,n0` whose accelerated odd-only orbit tends to positive infinity. The strict problem is not solved.

## Main candidate

```text
X  = 104350542602662257699,
n0 = 1.
```

The repository proves:

1. the orbit cannot return to `1`;
2. every element of a reached nontrivial cycle is at least `25`;
3. every cycle length

```text
p <= 177780727155637125192
```

is impossible;
4. every length through

```text
355561454311274250377
```

is impossible except

```text
177780727155637125193
177780727155637125195.
```

## Full-label structure for the last two lengths

Put

```text
O=ord_X(2)=1860810887857924950.
```

For every cycle edge write

```text
a_i=s_(i+1)+O*q_i,
1<=s_i<=O,
q_i>=0.
```

Then exactly

```text
A=sum_i s_i+O*sum_i q_i,
sum_i q_i<=6257.
```

Thus all but at most `6257` edges use the least full-order layer. A permanent predecessor sieve modulo `9` leaves `4308` of the `6462` refined small classes. Possible predecessors of a full representative satisfy

```text
m_q == m_0+q*63726582940809041391 (mod X).
```

Below one million there are `5824` survivors, only `133` with zero full delay and maximum delay `347`. Through sixty million there are `358103` survivors, only `9462` with zero delay and maximum delay `558`.

## Reciprocal bounds retained from inverse charging

For the harder remaining length

```text
p=177780727155637125195
```

the cycle identity requires

```text
sum_i 1/n_i > 0.099934206.
```

The retained exact bounds are

```text
n<=1000000, depth 1: <0.087551912
n<=1000000, depth 2: <0.085634587
n<=1000000, depth 3: <0.085243521
n<=60000000:          <0.087618737.
```

Hence at least `738929` distinct values above sixty million are still required.

## Exact symmetric edge budget

Assign to edge `i` the nonnegative cost

```text
c_i=(s_i-1)+(s_(i+1)-1)+2*O*q_i.
```

Cycle closure gives the exact identity

```text
sum_i c_i=2*(A-p).                                (E)
```

This is the correct transition-level cost: it pays both endpoint labels and two copies of every full-order layer.

Using the least feasible full predecessor for every target below one million and an exact fractional dual gives

```text
sum_(n_i<=1000000) 1/n_i < 0.087543786.
```

This is a strict depth-one improvement over the former `0.087551912`, although the older depth-two and depth-three window bounds remain numerically stronger.

## Cheap-transition mass concentration

With threshold

```text
K=5000,
```

identity `(E)` proves that at most

```text
4657855051477692680
```

edges have `c_i>=5000`. Therefore more than `97.38%` of every remaining hypothetical cycle has

```text
q_i=0,
s_i+s_(i+1)<=5001.
```

There are `12502500` such ordered label pairs. Exact enumeration proves that every corresponding target is at least

```text
781563824454394220933608138645145.
```

Consequently the whole cheap part contributes less than `2.216*10^(-13)` to `sum 1/n_i`.

The required reciprocal correction must therefore be concentrated in the expensive transitions. At least one expensive transition has target at most

```text
9190982840926584716
```

for length `...193`, and at most

```text
46609216582838682965
```

for length `...195`. Both are strictly below `X`.

## Massive repeated transition class

Using the sharper threshold `K=197`, at least

```text
59561055798335280522
```

edges are zero-layer edges with adjacent-label sum at most `198`. Only `19503` ordered pairs are possible, so one exact pair occurs at least

```text
3053943280435589
```

times.

A zero-layer pair determines one odd target class modulo `2*X^2`; distinct pairs determine distinct classes. Hence every remaining hypothetical cycle has diameter at least

```text
66508995066170702555770104858896894988802023536957800776.
```

## Short exact return

The repeated occurrences divide the cycle into cyclic gaps. Averaging both gap length and total valuation proves that one nonempty segment satisfies

```text
length L <= 114286,
total valuation S <= 7771435,
```

and its endpoints lie in the same odd class modulo `2*X^2`. Both endpoints are occurrences of the same cheap transition pair.

This is now a bounded exact-return witness inside either enormous hypothetical cycle.

## Multi-edge repetition ladder

The exact edge budget also forces repeated all-cheap words:

```text
2-edge word: >=3114290401257 repetitions, same class mod 2*X^3
3-edge word: >=2918613523 repetitions, same class mod 2*X^4
4-edge word: >=2251677 repetitions, same class mod 2*X^5
5-edge word: >=1500 repetitions, same class mod 2*X^6.
```

The five-edge result alone forces cycle diameter at least

```text
3870792567252275975939498201310492491155314740805796060324781763695205605253434152368864087556133785129469874414691399795398.
```

These are lower bounds on the maximum/diameter, not on the minimum. They therefore do not yet contradict the retained logarithmic theorem, which currently bounds the minimum cycle element.

## Main new certificate files

```text
docs/MASSIVE_REPEATED_TRANSITION_CLASS.md
tools/verify_massive_repeated_transition_class.py
docs/CHEAP_TRANSITION_MASS_CONCENTRATION.md
tools/verify_cheap_transition_mass_concentration.py
docs/SHORT_FULL_CLASS_RETURN.md
tools/verify_short_full_class_return.py
docs/SYMMETRIC_EDGE_COST_DUAL.md
tools/verify_symmetric_edge_cost_dual.py
docs/MULTI_EDGE_REPETITION_LADDER.md
tools/verify_multi_edge_repetition_ladder.py
```

The earlier sparse-window, predecessor-delay, inverse-window, zero-layer-block, and subgroup certificates remain part of `run_checks.py`.

## Not established

- No explicit orbit is proved divergent.
- The two displayed cycle lengths are not excluded.
- Cycles beyond the sparse cap remain possible.
- The cheap/high mass and the expensive/small mass have not yet been coupled into a contradiction.
- The modular height ladder bounds maxima, while the effective logarithmic ceiling currently bounds minima.
- Finite certificates do not prove divergence.

## Exact next step

The best current target is the expensive/small part, not a larger raw cutoff.

1. Use the exact symmetric edge cost on inverse windows of depth at least two, or a two-constraint rational dual combining endpoint and circulation costs.
2. Couple the forced target below `X` to its exact full predecessor delay and the global height identities.
3. Exploit the short return modulo `2*X^2` through the affine iterate formula; a useful result must add information beyond the terminal labels, which alone are tautological.
4. Seek a rigorous distribution bound for zero-layer pair classes modulo `X^2`, rather than enumerating more trajectory values.

## Retraction

The former `10^37` claim remains retracted because it assumed `2^A==1 mod X`. The correct congruence retains `product(n_i)`.

## Reproduction

```text
python run_checks.py
```
