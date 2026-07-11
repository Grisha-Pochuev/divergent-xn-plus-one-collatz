# Session checkpoint: Mersenne-divisor family frontier

Date: 2026-07-12

The strict prize problem remains open. This checkpoint supersedes the earlier
same-day dual-Wieferich checkpoint as the startup frontier.

The new primary candidate is

```text
k=500,
N=2^500-1,
m=4501,
B=2^4501,
d=349*2^500-347=2+349*N,
X=B-d=2^4501-349*2^500+347,
n0=1.
```

It belongs to a newly proved infinite Mersenne-divisor Wieferich family.

## 1. General construction theorem

For `N=2^k-1`, choose `m==r (mod k)` and

```text
d=2^r+t*N,
X=2^m-d.
```

Then `N|X`. If `1093||X`, `d` is odd, and `d<2^(m-1)`, the orbit from `1`
leaves `1` and never returns. Such parity-correct `t` with `1093||X` always
exists after increasing `m` in its congruence class.

Every accelerated output lies in exactly `k` classes modulo `N`:

```text
n_(i+1)==2^(-a_i) (mod N).
```

Combining this with the `1093^2` adjacent-label coordinate gives

```text
K=364*lcm(k,364)
```

permanent classes modulo

```text
M=N*1093^2.
```

Both the permanent density and the harmonic-packing coefficients decrease
exponentially with `k`, while the finite cycle barrier can be increased
independently by increasing `m-k`.

Files:

```text
docs/MERSENNE_DIVISOR_WIEFERICH_FAMILY.md
tools/verify_mersenne_divisor_wieferich_family.py
```

## 2. Exact primary-candidate arithmetic

For the balanced example,

```text
N=2^500-1,
1093||X,
gcd(500,364)=4,
K=16562000,
M=(2^500-1)*1093^2.
```

The first step leaves `1`, and the Wieferich argument forbids every later return.
The permanent one-label classes have residues

```text
1,2,4,...,2^499 (mod N).
```

Because cycle values are odd and cannot equal `1`, every hypothetical cycle
value satisfies

```text
n_i>N=2^500-1.
```

## 3. Harmonic packing

The least allowed odd representatives of the `500` one-label classes satisfy

```text
S_500<500/N.
```

After combining with the adjacent-label coordinate, exact rational arithmetic
proves

```text
combined base reciprocal sum <10^(-147),
K/(2*M)<10^(-149).
```

For a hypothetical cycle of length `p`, total valuation `A`,

```text
D=4501*p-A,
delta=log2(2^4501/X),
C0=(500/N)*(1+H_33124/2),
```

the exact cycle product gives

```text
0<p*delta-D
 <[C0+K*H_(ceil(p/K))/(2*M)]/(X*ln(2)),
C0<10^(-147).
```

The permanent class density is between `10^143` and `10^144` times smaller
than for the earlier candidate `X=2^3803-4162203`.

## 4. Finite cycle barrier

The standard near-power product argument gives

```text
p>2*X/(3*d).
```

For the primary candidate,

```text
10^1201<floor(2*X/(3*d))<10^1202.
```

This remains a finite barrier, not a divergence proof.

## 5. Exact exceptional-source floor

The exceptional condition

```text
v2(d*n-1)=4501
```

is one progression. Combining it with the one-label and adjacent-label
coordinates proves that the first compatible layer has

```text
N-label=495,
1093-label pair=(161,311),
```

and odd-core coefficient

```text
u_min=
141554173562669451979142234479211407387695161061947663158036275475013035570532072821977692485924548874811696146286209742307923384940182399969083204712328957713629782297601610389067903491331197096456313288013542743720638224927691460837892079910386115268969408753656537834465197519183303759432510875217219.
```

Therefore every exceptional source satisfies

```text
n>=(u_min*2^4501+1)/(349*2^500-347).
```

The right side has `1505` decimal digits. Minimality needs only the `500`
one-label layers and the `364^2` adjacent-label layers; the full product of
`16,562,000` combined classes is not enumerated.

File:

```text
docs/MERSENNE_DIVISOR_EXCEPTIONAL_FLOOR.md
```

## 6. Verification performed

The following standalone checks were run in the chat environment and passed:

```text
python tools/verify_dual_wieferich_square_sieve_candidate.py
python tools/verify_dual_wieferich_harmonic_packing.py
python tools/verify_mersenne_divisor_wieferich_family.py
```

The family checker uses exact integer and rational arithmetic. Its exceptional
minimum certificate checks `500+364^2` modular cases, not `16,562,000` product
cases.

All three checkers are included in `run_checks.py`. A complete repository-wide
run was not executed because the chat container did not have a fresh checkout.

## 7. Main conceptual conclusion

The family theorem proves that two formerly impressive quantities can be made
arbitrarily strong by construction:

1. the finite cycle barrier;
2. the permanent residue density and its harmonic constants.

Therefore simply choosing a larger `k` or `m` is no longer counted as meaningful
progress. The decisive missing theorem must exploit dynamic structure that the
raw sieve does not see.

## 8. Exact next target

Use the primary candidate and combine:

1. the integral near-power block ledger

```text
D=sum ordinary deficits-sum exceptional excesses;
```

2. the harmonic upper window for `p*delta-D`;
3. the 1505-digit floor for every exceptional source;
4. the exact congruence between the `500`-label and `364`-label sequences.

The first subproblem is to split hypothetical cycles into:

```text
no exceptional blocks;
exactly one exceptional block;
at least two exceptional blocks,
```

and derive a separate lower bound for the correction mass in each case. The
proof must use transition or height information, not merely a larger modulus.
