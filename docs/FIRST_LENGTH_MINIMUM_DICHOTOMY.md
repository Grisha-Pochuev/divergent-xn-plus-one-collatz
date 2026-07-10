# Minimum dichotomy for the first remaining length

Continue with

```text
p = 177780727155637125193,
m <= 5106101578294348744.
```

The refined valley theorem already proves that the outgoing valuation at the
cycle minimum satisfies `a<=56`.

## 1. Exact classes a=55 and a=56

For exact outgoing valuation `a`,

```text
m == (2^a-1)*X^(-1) (mod 2^(a+1)).
```

Below the displayed minimum bound there are exactly

```text
71 candidates for a=55,
35 candidates for a=56.
```

Testing the exact full-output subgroup conditions proves:

- no `a=55` candidate is a full output;
- exactly one `a=56` candidate is a full output:

```text
m_* = 1672312375827977333.                        (1)
```

The value in (1) survives the permanent predecessor sieve.  Its least full
output label is

```text
s(m_*) = 992055915950997467.
```

The exact full-predecessor progression first reaches another full output at

```text
q=33,
predecessor residue = 26970074936991792008 (mod X),
source label = 1684217191177655995.
```

Thus any cycle using (1) as its minimum spends at least `33` of its total
full-order layer budget on the edge entering the minimum.

## 2. Rigorous dichotomy

Every hypothetical cycle of length `...193` satisfies exactly one of:

### Exceptional minimum case

```text
m = 1672312375827977333,
a_out = 56,
q_in >= 33.
```

### Strong expansion case

Since `a=55` is impossible and `a<=56`, all other cases have

```text
a_out<=54,
n_next > X*m/2^54 > 5792*m.
```

## 3. Meaning

The remaining first length no longer has an unconstrained local minimum.
Either it passes through one explicit integer with a costly incoming full-order
layer, or its minimum is followed by growth greater than a factor `5792`.

This is not yet a contradiction.  The exceptional integer may still have a
long nonperiodic forward orbit, and a large local expansion can be balanced by
later contractions.  The dichotomy gives two concrete branches for the next
global height or predecessor argument.

Run

```text
python tools/verify_first_length_minimum_dichotomy.py
```

for the exact certificate.
