# Legacy progress snapshot before the near-power candidate

This file preserves the former contents of `docs/LATEST_VALID_PROGRESS.md`.
It describes an older candidate and is not current project memory. The current
mathematical frontier is in `docs/CURRENT_STATUS.md`.

The former `10^37` claim remains retracted. All results below preserved the
correct cycle identity at the time this snapshot was active.

For

```text
X  = 104350542602662257699,
n0 = 1,
```

the contiguous cycle barrier was

```text
177780727155637125192.
```

More strongly, every length through

```text
355561454311274250377
```

was impossible except

```text
177780727155637125193
177780727155637125195.
```

## Transition progress retained in this legacy branch

Let

```text
O=ord_X(2)=1860810887857924950.
```

Every incoming valuation had the unique form

```text
a_i=s_(i+1)+O*q_i,
1<=s_i<=O.
```

The exact occupancy identity was

```text
A=sum_i s_i+O*sum_i q_i.
```

At either remaining length,

```text
sum_i q_i<=6257.
```

Additional retained results were:

1. A permanent predecessor sieve removed exactly `2154` of the `6462` refined classes modulo `6*15099`.
2. Possible predecessors of a full representative formed an exact linear progression modulo `X`.
3. Requiring the predecessor itself to be a full output gave a pointwise full-layer delay.
4. Below `10^6`, only `133` of `5824` surviving representatives had zero delay; the maximum delay was `347`.
5. Through `6*10^7`, only `9462` of `358103` surviving representatives had zero delay; the maximum was `558`.
6. For the harder remaining length,

```text
sum_(n_i<=60000000) 1/n_i < 0.087618737,
```

while the exact cycle threshold was greater than `0.099934206`.
7. Therefore more than `0.012315` of the reciprocal correction had to come from at least `738929` distinct values above sixty million.
8. Finite inverse-window bounds improved strictly at depths one, two, and three.
9. Any hypothetical remaining cycle was either entirely least-layer, or contained at least `28413093679980362` consecutive least-layer steps.
10. If a positive layer occurred, one least-layer block grew by more than

```text
2^1860810887857924884.
```

This snapshot remains only for audit and historical comparison.