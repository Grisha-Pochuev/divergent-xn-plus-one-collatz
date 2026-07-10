# Class-forced height bounds from transition balance

Fix the retained multiplier

```text
X = 104350542602662257699,
M = 15099,
H = 2154.
```

For an allowed cycle element `n`, let `sigma(n)=s` be its residue-class label:

```text
n == 2^(-s) (mod M),  1<=s<=H.
```

## 1. Balance forces an incoming high valuation

If a positive cycle contains an element in class `s`, then its class occupancy
`c_s` is positive. Exact transition balance says that the number of incoming
edges with target label `s` is also `c_s`. Hence some cycle element `m` has

```text
a(m)=v2(X*m+1) == s (mod H),
```

and in particular

```text
a(m)>=s.
```

Therefore

```text
m == -X^(-1) (mod 2^s).                            (1)
```

Let `eta_s` be the least positive odd integer at least `25` satisfying (1).
Every cycle that occupies class `s` has maximum element at least `eta_s`.

This is a deterministic consequence of cycle closure, not a probabilistic
statement.

## 2. Explicit consequence for small possible cycle elements

Exact enumeration of the allowed output classes shows that the only least
admissible representatives below `155` are

```text
25, 29, 37, 65, 107, 113, 121, 137, 149, 151.
```

Their class labels are respectively

```text
904, 1743, 1364, 1559, 1061, 1101, 1904, 1417, 1013, 1252.
```

Thus every such class label is at least `904`. The smallest corresponding
forced height is attained for class `904`:

```text
eta_904 =
24410528407446107700858164813722470259352136467046536651473478311514542857304277156336273282008033218583592373459450897899438310362576656340391995111519006844204739081004693679586482220668806179134076805846579167106170118627024565023917104733854006926827379407158269924469.
```

It has binary length `902`.

Therefore:

> If a hypothetical nontrivial cycle for the fixed orbit has minimum element
> below `155`, then its maximum element is at least `eta_904`.

In particular, a cycle containing the smallest currently allowed value `25`
contains an element at least `eta_904`.

## 3. General form

For any height cutoff `Y`, enumerate all allowed source classes whose least
admissible representative is below `Y`, and take the minimum of their
`eta_s`. This gives an exact implication

```text
cycle minimum < Y  =>  cycle maximum >= H_Y.
```

The result supplies a modular lower bound on cycle height that depends on the
class of a small element. It is intended for later combination with upper
bounds on the ratio of maximum to minimum or with logarithmic cycle-height
reductions.

This note does not by itself exclude all cycles or prove divergence.
