# Finite inverse-window charging

Fix the hardest remaining length

```text
p = 177780727155637125195
```

and write every incoming valuation as

```text
a_i=s_(i+1)+O*q_i,
O=ord_X(2).
```

The full-label occupancy theorem gives

```text
sum_i (s_i-1)+O*Q=A-p,
Q=sum_i q_i<=6257.
```

## 1. Minimum inverse-window layer cost

For a genuine possible cycle value `n`, define `h_L(n)` to be the minimum
possible sum of full-order layers over an inverse chain of `L` consecutive
accelerated steps ending at `n`, under the necessary condition that every
intermediate value is itself a full output residue modulo `X`.

Thus

```text
h_1(n)=d_X(n),
```

where `d_X` is the full predecessor delay.  For `L>=2`, the exact finite
recursion is

```text
h_L(n)=min_q [q+h_(L-1)(m_q)],
```

where the minimum ranges over layer numbers `q` for which the predecessor

```text
m_q=(2^(s+qO)*n-1)/X
```

is a full output residue.

The recursion is evaluated modulo `X^(L+1)`, which retains exactly the carry
information needed for `L` inverse divisions by `X`.

## 2. Global window charging

For the actual cycle, the `L`-edge inverse window ending at `n_i` has layer sum
at least `h_L(n_i)`.  If `S` is any selected set of cycle positions, summing
these windows counts each actual `q_j` at most `L` times.  Therefore

```text
sum_(i in S) h_L(n_i) <= L*Q.
```

Combining this with the label budget gives the exact incremental selection
constraint

```text
sum_(i in S) [L*(s_i-1)+O*h_L(n_i)]
 <= L*(A-p).                                      (1)
```

This is valid even though selected windows overlap.

## 3. Exact depth-two certificate below one million

For all `5824` permanent-sieve survivors below one million, the exact recursion
finds

```text
0 <= h_2 <= 490,
sum h_2 = 478043.
```

Using the item cost

```text
c_2(n)=2*(s(n)-1)+O*h_2(n)
```

and the exact fractional dual from (1), the boundary occurs after `258`
complete items.  The boundary item is

```text
n = 48497,
s = 1548519004723674501,
h_2 = 35,
c_2 = 68225419084474722250.
```

The rigorous reciprocal bound is

```text
sum_(cycle elements n<=1000000) 1/n
 < 0.085634587.
```

Hence the reciprocal contribution above one million must exceed

```text
0.014299
```

and at least `14300` larger values are necessary.

## 4. Exact depth-three certificate below one million

The same finite recursion at depth three gives

```text
0 <= h_3 <= 519,
sum h_3 = 685875.
```

With

```text
c_3(n)=3*(s(n)-1)+O*h_3(n),
```

the fractional boundary occurs after `205` complete items.  Its item is

```text
n = 17669,
s = 618223181506832115,
h_3 = 157,
c_3 = 294001978938214713492.
```

The resulting rigorous bound is

```text
sum_(cycle elements n<=1000000) 1/n
 < 0.085243521.
```

Thus the required contribution above one million is greater than

```text
0.014690
```

and at least `14691` larger values are necessary.

## 5. Meaning

The strict bound improves from depth one to two and again from two to three.
This shows that the inverse-chain route contains information not captured by a
single predecessor delay.  It does not yet exclude the last length because the
large zero-delay tail remains uncontrolled.

The next mathematical target is either:

1. prove a positive lower mean layer cost for all sufficiently long inverse
   windows; or
2. construct a dual potential on the finite carry states that bounds the
   zero-delay tail directly.

Run

```text
python tools/verify_finite_inverse_window_charging.py
```

for the exact depth-two and depth-three certificates.
