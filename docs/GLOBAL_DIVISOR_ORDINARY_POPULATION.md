# Global-divisor ordinary-boundary population

Date: 2026-07-20

## Scope

Use the retained primary candidate

```text
N=2^500-1,
q=1093,
M=N*q^2,
B=2^4501,
d=349*2^500-347,
X=B-d.
```

Assume, for contradiction, that a nontrivial positive accelerated `Xn+1`
cycle exists.  Let its canonical complete blocks have lengths `ell_i` and put

```text
h=gcd_i ell_i,
S_h=(B^h-X^h)/d,
g=gcd of all complete-block boundary values.
```

The retained global-divisor theorem gives

```text
g divides S_h.                                        (1)
```

This note couples that endogenous divisor to the 300-digit ordinary-block
population and the permanent classes modulo `M`.

## 1. The endogenous and permanent moduli are coprime

Because `N|X`, while

```text
B==2 (mod N),
d==2 (mod N),
```

the geometric factor satisfies

```text
S_h==2^(h-1) (mod N).                                 (2)
```

This is a unit modulo the odd number `N`.  Likewise `q|X`, while both `B` and
`d` are units modulo `q`, so

```text
S_h==B^(h-1) (mod q).                                 (3)
```

Thus

```text
gcd(S_h,M)=1.
```

Together with (1), this proves

```text
gcd(g,M)=1.                                          (4)
```

Every complete-block boundary is divisible by `g` and belongs to one of the
retained `16,562,000` permanent classes modulo `M`.  By (4), each permanent
class has exactly one simultaneous lift with boundary residue `0 modulo g`.
Therefore all complete-block boundaries occupy at most

```text
16,562,000
```

explicit joint classes modulo `g*M`.  The global divisor adds spacing without
increasing the number of available boundary classes.

## 2. A repeated ordinary boundary type

Let `D=4501*p-A` be the total cycle credit and let `J` be the number of
ordinary complete blocks.  Each ordinary block contributes at most `4500`
positive credit, whereas exceptional blocks contribute negative credit.  Hence

```text
J>=ceil(D/4500).                                     (5)
```

The retained continued-fraction frontier gives `D>=Q_credit`, so

```text
J>=J_min=ceil(Q_credit/4500).
```

Attach to every ordinary block the pair

```text
(its terminal credit e in {1,...,4500},
 its source-boundary joint class modulo g*M).
```

There are at most

```text
4500*16,562,000=74,529,000,000                       (6)
```

such types.  The pigeonhole principle therefore forces one type to occur at
least

```text
R_min=ceil(J_min/74,529,000,000)>2^947               (7)
```

times.  All these occurrences have the same ordinary terminal credit and their
distinct source boundaries lie in one arithmetic progression of step `g*M`.

Consequently the largest and smallest sources among these occurrences satisfy

```text
max source-min source >=(R_min-1)*g*M
                      >g*2^1466.                    (8)
```

Here the last comparison uses `R_min-1>=2^947`, `N>2^499`, and `q^2>2^20`.

## 3. Meaning and limitation

This is the first direct quantitative coupling of the exact global divisor
`g` with the new 300-digit credit frontier.  The divisor cannot thin the
ordinary-boundary population by splitting it into additional residue classes:
it only enlarges the common progression step.  A single same-credit boundary
type must already occur more than `2^947` times.

The result does not yet exclude a cycle.  The remaining target is to charge the
height spread (8), or the reciprocal mass of this repeated progression, against
the narrow `1007/1008` length strip and the bounded-prefix reserve.  In
particular, a final global-divisor contradiction must use more than bare class
counting, because arbitrarily high representatives of the progression remain
possible.

## 4. Verification

Run

```text
python tools/verify_global_divisor_ordinary_population.py
```

The checker verifies the candidate congruences, coprimality formulas, exact
population ceilings, the `2^947` repetition bound, and the `g*2^1466` diameter
bound using exact integer arithmetic.
