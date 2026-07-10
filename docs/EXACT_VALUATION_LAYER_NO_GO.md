# Exact valuation layers do not forbid finite paths

For the fixed multiplier

```text
X = 104350542602662257699,
M = 15099,
H = ord_M(2) = 2154,
```

write every exact halving count uniquely as

```text
a_i = t_i + H*q_i,
1 <= t_i <= H,
q_i >= 0.
```

Here `t_i` is the target residue-class label modulo `M`, and `q_i` is the valuation layer.

## Theorem

Every finite word

```text
(t_0,q_0),...,(t_(L-1),q_(L-1))
```

with `1<=t_i<=H` and `q_i>=0` is followed exactly by infinitely many positive odd starting integers.

## Proof

Set `a_i=t_i+H*q_i`.  The exact finite valuation-word coding theorem gives one residue class

```text
n0 == r  (mod 2^(A+1)),
A=sum_i a_i,
```

whose positive representatives have exact valuations

```text
a_0,...,a_(L-1).
```

There are infinitely many positive representatives of this class.  Since

```text
2^(a_i)*n_(i+1) == 1 (mod M)
```

and `2^H==1 (mod M)`, the successor has class label

```text
t_i = ((a_i-1) mod H)+1.
```

Thus the prescribed layer word is realized exactly.

## Consequence

Neither the `2154` class graph nor the refinement by an arbitrary finite list of exact layers can contain forbidden finite paths.  Any useful obstruction must use a genuinely global cycle condition: closure, flow balance, the total valuation identity, size/descent information, or the affine cycle equation.

This is a negative but decisive result: further local edge enumeration at fixed finite depth cannot solve Priority 1 by itself.
