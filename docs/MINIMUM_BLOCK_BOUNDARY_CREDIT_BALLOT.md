# The least complete-block boundary forces a positive credit ballot

Date: 2026-07-17

## Scope

Let

```text
B=2^m,
d positive odd,
1<=d<B/2,
X=B-d>=5.
```

Use the accelerated map

```text
C_X(n)=(X*n+1)/2^v2(X*n+1).
```

Assume a nontrivial positive cycle exists and partition its cyclic valuation word
into the canonical complete near-power blocks. An ordinary block has positive
credit

```text
c=e,  1<=e<=m-1,
```

and an exceptional block has negative credit

```text
c=-b,  b>=1.
```

This note proves that, when the complete blocks are read from the least
complete-block boundary, every nonempty prefix has strictly positive cumulative
credit. Thus every exceptional excess unit has an earlier ordinary deficit unit
which pays for it, and the payment can be chosen in the actual cyclic order.

## 1. Exact height-credit domination for one block

For a complete block of accelerated length `ell`, source `n`, endpoint `n'`, and
credit `c`, the exact ratio identity is

```text
n'/n
 =2^c*(X/B)^ell
  *[1+((B/X)^ell-1)/(d*n)].                         (1)
```

Put

```text
q=((B/X)^ell-1)/(d*n)>0.
```

Because `d*n>1`,

```text
q<(B/X)^ell-1,
```

and therefore

```text
1+q<(B/X)^ell.                                      (2)
```

Substituting (2) into (1) gives the strict exact inequality

```text
n'/n<2^c.                                            (3)
```

No logarithmic approximation, trajectory cutoff, or candidate-specific
constant is used.

## 2. Prefix theorem at the least complete-block boundary

Let the complete-block boundary values of the hypothetical cycle be

```text
z_0,z_1,...,z_(q-1),z_q=z_0,
```

in actual orbit order, and choose the cyclic rotation for which

```text
z_0=min(z_0,...,z_(q-1)).                            (4)
```

Let block `i` carry credit `c_i`, and define the cumulative prefix credit

```text
P_j=sum_(i=0)^(j-1)c_i,  1<=j<=q.                   (5)
```

Multiplying (3) over the first `j` blocks gives

```text
z_j/z_0<2^P_j.                                       (6)
```

By (4), `z_j/z_0>=1`. Hence

```text
1<=z_j/z_0<2^P_j.
```

The credit `P_j` is an integer, so

```text
P_j>=1  for every 1<=j<=q.                           (7)
```

This includes the full cycle, where `P_q=D=m*p-A>=1`, but is stronger: no
proper complete-block prefix from the least boundary can have zero or negative
credit.

## 3. Ordered matching of exceptional excess to ordinary deficit

Read the credits from `z_0`. Replace every ordinary credit `e` by `e` positive
units and every exceptional credit `-b` by `b` negative units. Maintain a stack
of unmatched positive units. On a negative unit, match it to and remove the
latest unmatched positive unit.

Condition (7) says that the stack never underflows and never becomes empty after
a nonempty block prefix. Consequently:

1. every exceptional excess unit is matched to an earlier ordinary deficit unit;
2. the matching is noncrossing in cyclic order when implemented by the stack;
3. exactly

   ```text
   D=sum ordinary deficits-sum exceptional excesses
   ```

   ordinary units remain unmatched after the full cycle;
4. the first block after `z_0` must be ordinary.

This is an actual-order placement theorem, not only the global ledger inequality
that total ordinary deficit exceeds total exceptional excess.

## 4. Quantitative placement bounds

Suppose the first `j` ordinary blocks encountered after `z_0` have total ordinary
deficit `O_j`, and let `E_j` be all exceptional excess accumulated through the
same complete-block prefix ending immediately after the `j`-th ordinary block.
Equation (7) gives

```text
O_j-E_j>=1.                                          (8)
```

Since each ordinary deficit is at most `m-1`,

```text
E_j<=O_j-1<=j*(m-1)-1.                               (9)
```

Thus an exceptional block of excess `b` cannot appear before enough ordinary
credit has accumulated. In particular, if it occurs no later than the prefix
ending at the `j`-th ordinary block, then

```text
j>=ceil((b+1)/(m-1)).                                (10)
```

For the primary candidate `m=4501`, this becomes

```text
E_j<=4500*j-1,
j>=ceil((b+1)/4500).                                 (11)
```

## 5. Consequence for the surviving positive-credit return

Retain the minimum ordinary boundary notation from
`MINIMUM_BOUNDARY_ACTUAL_EXPANDING_SEGMENT.md`. Let the first actual exit from
that boundary have credit

```text
1<=C<=4500.
```

For the least ordinary boundary, every later ordinary boundary is no smaller.
Applying (3) to the complete-block prefix ending there proves that its cumulative
credit from the least ordinary boundary is at least `1`. Therefore every prefix
of the return after the initial exit has return-prefix credit `Q` obeying

```text
C+Q>=1,
Q>=1-C>=-4499.                                       (12)
```

So the astronomically long surviving return cannot borrow an arbitrarily large
amount of exceptional credit before repaying it: at every ordinary boundary its
net credit debt is at most `4499`.

At the finer complete-block level, choosing the least complete-block boundary
produces the stronger zero-debt ballot (7). These two anchors need not be the
same boundary, but both are available in every hypothetical cycle.

## 6. What this closes and what remains open

The theorem closes the possibility that the positive-credit return hides all of
its ordinary compensation after an arbitrarily large initial exceptional debt.
It supplies the forced placement pattern requested by the current proof plan:
exceptional excess must be paid in actual cyclic order by earlier ordinary
deficits.

It does not yet exclude the surviving branch. The remaining target is to combine
the ordered matching with at least one height-sensitive fact, for example:

1. pair each exceptional source floor with the earlier ordinary unit which pays
   for it;
2. prove that repeated matched pairs force too much harmonic correction or an
   impossible source-class repetition;
3. use the permanent `N` and `1093^2` labels to restrict which ordinary boundary
   can sponsor a given exceptional excess;
4. derive a cycle-wide contradiction from the `D` unmatched ordinary units.

## 7. Verification

Run

```text
python tools/verify_minimum_block_boundary_credit_ballot.py
```

The checker verifies exact block domination on a grid of near-power multipliers,
all three known accelerated `5n+1` positive cycles, the ordered stack matching on
all small positive-prefix ledgers in its test range, and the primary numerical
corollaries (11)--(12).
