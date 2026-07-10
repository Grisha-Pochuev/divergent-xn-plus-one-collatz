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

## Retained Priority 1 results

### Local transition no-go

The graph on the `2154` output classes modulo `2*15099` is complete. Every compatible finite exact-valuation word, including arbitrary finite valuation layers, is realizable by infinitely many starts. Local forbidden-edge and forbidden-word enumeration cannot supply the missing proof.

### Global class constraints

For small-class occupancies `c_t`,

```text
sum c_t=p,
sum t*c_t<=67p-1.
```

Cycle closure forces exact source/target flow balance.

For the full classes modulo `2X`, write every valuation as

```text
a_i=s_(i+1)+O*q_i,
O=ord_X(2)=1860810887857924950.
```

Then exactly

```text
A=sum_i s_i+O*sum_i q_i,
1<=s_i<=O.
```

For either remaining length,

```text
sum_i q_i<=6257.
```

Thus all but at most `6257` cycle steps use the least full-order layer; larger layer numbers reduce that count further.

### Permanent predecessor sieve

Because `X==3 (mod 9)`, one of the three compatible lifts of every small output class modulo `6M` has every predecessor divisible by `3`. Such a value cannot be an accelerated output from the fixed orbit.

Exactly

```text
2154 refined classes are dead,
4308 refined classes survive.
```

The surviving mod-3 transition types also obey the exact circulation balance

```text
N_(1->2)=N_(2->1).
```

### Full predecessor progression

For a genuine full representative `n` with least label `s`, every possible predecessor is

```text
m_q=(2^(s+qO)*n-1)/X.
```

Modulo `X`, these states form the exact progression

```text
m_q == m_0+q*63726582940809041391 (mod X).
```

A predecessor in a reached cycle must itself belong to the full output subgroup. The first `q` for which this happens is the full predecessor delay `d_X(n)`, and every cycle satisfies

```text
sum_i d_X(n_i)<=6257.
```

Below one million:

```text
8727 genuine full representatives,
2903 permanent-sieve rejections,
5824 survivors,
133 zero-delay survivors,
maximum full delay 347.
```

Through sixty million:

```text
536735 genuine full representatives,
178632 permanent-sieve rejections,
358103 survivors,
9462 zero-delay survivors,
maximum full delay 558.
```

### Exact reciprocal bounds for the hardest length

For

```text
p=177780727155637125195,
A=11822418355849868825468,
A-p=11644637628694231700273,
```

the exact cycle interval requires

```text
sum_i 1/n_i > 0.099934206.
```

Using full predecessor delays and a rational fractional-selection dual gives

```text
sum_(n_i<=1000000) 1/n_i < 0.087551912,
sum_(n_i<=60000000) 1/n_i < 0.087618737.
```

Therefore a hypothetical cycle must obtain more than `0.012315` of its reciprocal sum from values above sixty million. At least

```text
738929
```

such distinct values are necessary.

### Finite inverse-window charging

Let `h_L(n)` be the minimum sum of full-order layers in an admissible `L`-step inverse chain ending at `n`. For any selected cycle positions,

```text
sum h_L(n_i)<=L*sum q_i.
```

This gives the exact scaled item cost

```text
L*(s-1)+O*h_L.
```

Below one million the retained bounds improve with depth:

```text
L=1: reciprocal contribution <0.087551912
L=2: reciprocal contribution <0.085634587
L=3: reciprocal contribution <0.085243521
```

The improvement is strict but does not yet control the large zero-delay tail.

### Other retained tools

- exact transition progressions and finite truncation to `428646` non-negligible small-modulus cells;
- index-eight subgroup sieve modulo `P=6911089648497401`;
- global height and reciprocal closure identities;
- exact sparse-window interval certificates.

## Main certificate files

```text
docs/PERMANENT_PREDECESSOR_MOD3_SIEVE.md
tools/verify_permanent_predecessor_mod3_sieve.py
docs/FULL_LABEL_OCCUPANCY_BUDGET.md
tools/verify_full_label_occupancy_budget.py
docs/FULL_PREDECESSOR_DELAY.md
tools/verify_full_predecessor_delay.py
docs/FULL_PREDECESSOR_RECIPROCAL_BOUND.md
tools/verify_full_predecessor_reciprocal_bound.py
docs/FINITE_INVERSE_WINDOW_CHARGING.md
tools/verify_finite_inverse_window_charging.py
```

The earlier sparse-window and subgroup certificates remain part of `run_checks.py`.

## Not established

- No explicit orbit is proved divergent.
- The two displayed lengths are not excluded.
- Cycles beyond the sparse cap remain possible.
- The large zero-delay tail is not yet bounded sharply enough.
- Finite certificates do not prove divergence.

## Exact next step

Do not extend the cutoff blindly. Seek a global certificate for the zero-delay tail:

1. a rational potential or minimum-mean argument for long inverse windows;
2. a rigorous distribution bound for the initial sequence of full classes `2^(-s) mod X`;
3. a source/target circulation inequality coupling full predecessor states to the global height identities.

## Retraction

The former `10^37` claim remains retracted because it assumed `2^A==1 mod X`. The correct congruence retains `product(n_i)`.

## Reproduction

```text
python run_checks.py
```
