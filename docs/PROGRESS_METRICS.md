# Objective progress metrics

Research effort is not a linear fraction of a proof. Checkpoints therefore
report:

1. strict logical gates;
2. exact finite frontiers;
3. reusable infinite-family structure;
4. the decisive missing theorem.

## A. Strict prize gates

For the primary candidate

```text
X=2^4501-349*2^500+347,
n0=1:
```

| Gate | Meaning | Status |
|---|---|---|
| G1 | explicit odd `X>=5` and positive odd `n0` | closed |
| G2 | orbit leaves `1` and never returns | closed |
| G3 | every nontrivial positive cycle is excluded | open |
| G4 | bounded positive orbit implies eventual cycle | closed as a general lemma |
| G5 | independent verification covers the final proof | partial; waits for G3 |

G3 is the decisive global theorem and may contain most of the remaining
difficulty. The table must not be converted mechanically into a proof
percentage.

## B. Primary candidate measurements

```text
k=500,
N=2^500-1,
m=4501,
d=349*2^500-347,
X=2^4501-349*2^500+347,
n0=1.
```

### Exact finite frontiers

- every positive cycle length `p` must satisfy

```text
p>2*X/(3*d),
10^1201<floor(2*X/(3*d))<10^1202;
```

- every hypothetical cycle value satisfies

```text
n_i>2^500-1;
```

- every exceptional cycle source satisfies

```text
n>=(u_min*2^4501+1)/(349*2^500-347),
```

  where

```text
u_min=
141554173562669451979142234479211407387695161061947663158036275475013035570532072821977692485924548874811696146286209742307923384940182399969083204712328957713629782297601610389067903491331197096456313288013542743720638224927691460837892079910386115268969408753656537834465197519183303759432510875217219;
```

- the exceptional-source lower bound has `1505` decimal digits.

### Permanent residue structure

- `N=2^500-1` divides `X`;
- `1093` divides `X` exactly once;
- every output belongs to exactly `500` classes modulo `N`;
- the `1093^2` adjacent-label coordinate combines with them into exactly

```text
K=16562000
```

  classes modulo

```text
M=(2^500-1)*1093^2;
```

- the current labels modulo `500` and `364` agree modulo `4`.

### Reusable infinite-family structure

- the Wieferich mechanism forbids return to `1`;
- the Mersenne-divisor family constructs such candidates for every `k` not
  divisible by `364` after choosing a suitable `t`;
- the combined permanent density decreases exponentially in `k`;
- every near-power complete block has the general exact credit ledger

```text
D=m*p-A
 =sum ordinary deficits-sum exceptional excesses;
```

- the primary harmonic constants satisfy

```text
10^(-148)<C0<10^(-147),
10^(-150)<K/(2*M)<10^(-149),
```

  where

```text
C0=(500/(2^500-1))*(1+H_33124/2);
```

- every hypothetical cycle obeys

```text
0<p*delta-D
 <[C0+K*H_(ceil(p/K))/(2*M)]/(X*ln(2)),
delta=log2(2^4501/X).
```

### Still open

- cycles above the finite barrier remain infinite in number;
- an arbitrarily thin permanent sieve does not itself exclude all cycles;
- no lower bound for `p*delta-D` yet matches the harmonic upper window;
- the cases of zero, one, and multiple exceptional blocks remain to be closed.

## C. Main conceptual advance

The Mersenne-divisor family proves that both

```text
finite barrier size
```

and

```text
permanent residue density
```

can be improved without limit by changing the constructed candidate. Therefore
new record parameters alone are no longer counted as meaningful progress.

The decisive object is now a dynamic theorem coupling:

1. compatible valuation-label sequences;
2. block credits;
3. source heights;
4. the correction mass `p*delta-D`.

## D. Independent fallback branches

### `X=2^3803-4162203,n0=1`

- `17886960` permanent classes modulo `14726582775529`;
- cycle barrier greater than `10^1138`;
- exceptional floor `(19567017189655*2^3803+1)/4162203`;
- harmonic base constant `1/853`.

### `X=2^156-9,n0=1`

- all positive cycle lengths through

```text
7034970411803187993997906985047212163795395134
```

  are excluded;
- the first ordinary-block threshold is

```text
7034970411803187993997906985047212163795395135;
```

- every exceptional source is at least

```text
1268664615738631005385143083955106787895774776889;
```

- the first `48` steps have exact word `(3,1,2,2,5,6)^8`.

### `X=2^260-3,n0=1`

Return to `1` is impossible, all positive cycle lengths through approximately
`4.117*10^77` are excluded, and the first `172` steps have exact word
`(1,2)^86`.

### `X=15,n0=3`

Complete Mersenne blocks and second-block escalation are classified. The later
height theorem and avoidance of a nontrivial cycle remain open.

### `X=9,n0=1`

The sufficient target is still

```text
A_t<=3*t-1 for every t>=1.
```

### Previous fixed candidate

All cycle lengths through `355561454311274250377` are excluded except

```text
177780727155637125193,
177780727155637125195.
```

At the first surviving length, `6242` layer totals remain.

## E. Honest approximate wording

A subjective planning estimate may be stated only as a broad research-maturity
range, never as a measured probability that the proof is nearly complete.

Current honest wording:

```text
strict target: open;
three of four mathematical proof gates available;
decisive remaining gate: global exclusion of every nontrivial positive cycle;
main uncertainty: whether the block-credit/harmonic coupling is strong enough.
```

A single global lemma could finish the proof, or could contain most of the
remaining work.
