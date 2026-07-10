# Transition-budget improvement of the fixed cycle barrier

Consider the fixed multiplier

```text
X = 104350542602662257699
```

and its accelerated odd-only map. This note strengthens the retained finite cycle obstruction by using the minimum valuation cost of each of the `2154` allowed residue classes.

## 1. Residue classes and their valuation costs

Let

```text
M = 15099,
H = ord_M(2) = 2154.
```

For `1<=t<=H`, class `t` is the unique odd class modulo `2M` reducing to

```text
2^(-t) (mod M).
```

If a step enters class `t`, its exact halving count is

```text
a = t + H*q
```

for some `q>=0`. Thus every occurrence of class `t` consumes at least `t` units of total valuation.

If a hypothetical positive cycle has length `p`, class counts `c_t`, and total halving count `A`, then

```text
sum_t c_t = p,
sum_t t*c_t <= A.
```

The exact cycle identity gives

```text
2^A = product_i (X+1/n_i).
```

Since `X+1<2^67`,

```text
A <= 67p-1.
```

Therefore

```text
c_t <= floor((67p-1)/t).                       (1)
```

This is the transition-class budget absent from the previous independent-class envelope.

## 2. Distinctness inside each class

Let `rho_t` be the least admissible positive representative of class `t`; in the class containing the literal value `1`, use `1+2M` because the fixed orbit cannot return to `1`.

The cycle elements in class `t` are distinct and lie in

```text
rho_t, rho_t+2M, rho_t+4M, ...
```

If the cycle has length `p<=B`, then by (1)

```text
c_t <= C_t(B),
C_t(B) = min(B, floor((67B-1)/t)).
```

Hence the reciprocal contribution of class `t` is at most

```text
1/rho_t
+ log(1+2M*(C_t(B)-1)/rho_t)/(2M).
```

For exact certification, choose the least integer `k_t` satisfying

```text
1+2M*(C_t(B)-1)/rho_t <= 2^k_t.
```

Using `log(2)<7/10`, the total reciprocal sum is bounded by the exact rational number

```text
S_budget(B)
 = sum_t 1/rho_t
   + (7/(20M))*sum_t k_t.                      (2)
```

For the barrier below, the exact verifier obtains

```text
sum_t k_t = 141246,
S_budget(B) approximately 3.820165970485471.
```

The corresponding independent-class envelope is approximately

```text
4.440611033072398.
```

## 3. Power-of-two interval test

Write

```text
epsilon = X^2/2^133 - 1 > 0.
```

For every cycle,

```text
Lambda
 = A*log(2)-p*log(X)
 = sum_i log(1+1/(X*n_i))
 <= S_budget(B)/X.
```

### Even lengths

For `p=2r<=B`,

```text
r*epsilon + S_budget(B)/X < log(2)
```

is certified using `log(2)>2/3`. Therefore the cycle product lies strictly between consecutive powers of two.

### Odd lengths

For `p=2r+1<=B`,

```text
r*epsilon + S_budget(B)/X < log(2^67/X)
```

is certified using

```text
log(q) > 2*(q-1)/(q+1),
q=2^67/X>1.
```

Again the product lies strictly between consecutive powers of two.

## 4. Exact improved barrier

The exact certificate proves that no nontrivial positive accelerated cycle can have length

```text
p <= 176022359338834903228.
```

The next integer

```text
176022359338834903229
```

already fails the retained odd-length rational interval test. Since every term in that test is nondecreasing with the length cap, the displayed barrier is maximal for this particular class-budget envelope and the retained rational logarithm bounds.

Run

```text
python tools/verify_transition_budget_barrier.py
```

for the exact certificate.

## 5. Fair comparison with the previous envelope

The previously recorded project barrier was the round value

```text
170000000000000000000.
```

However, if the old independent-class envelope is pushed to its own exact limit with the same rational logarithm bounds, it reaches

```text
176022359338834903224.
```

The transition-budget envelope reaches

```text
176022359338834903228.
```

Therefore two comparisons must be kept separate:

1. against the previously retained project barrier, the certified increase is about `3.54%`;
2. against a fully saturated version of the old independent-class certificate, the new transition information adds exactly `4` further cycle lengths.

The structural gain is real: the reciprocal upper bound drops from about `4.44061` to about `3.82017`. Its numerical effect on this particular barrier is small because the reciprocal correction is divided by the enormous multiplier `X`; the limiting term is the exceptionally small gap between `X^2` and `2^133`.

## 6. Rigorous conclusion for the fixed orbit

For

```text
(X,n0)=(104350542602662257699,1),
```

the orbit cannot return to `1`, and it cannot enter any nontrivial positive cycle of accelerated length at most

```text
176022359338834903228.
```

Therefore it either tends to positive infinity or enters a nontrivial positive cycle longer than this finite barrier.

This remains a finite obstruction, not a proof of divergence. The stronger transition-balance reduction in `docs/TRANSITION_BALANCED_RECIPROCAL_REDUCTION.md` is the next route for improving the reciprocal envelope further, although any improvement of the reciprocal correction alone can move this particular interval barrier by only a few additional lengths.
