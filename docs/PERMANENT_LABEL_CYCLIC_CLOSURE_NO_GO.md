# Permanent residue labels are automatically compatible with cyclic closure

## Purpose

This note tests the proposed decisive route: derive an arithmetic contradiction
between the permanent residue labels modulo

```text
M=N*1093^2,
N=2^500-1,
```

and cyclic closure of a hypothetical positive orbit for the primary candidate

```text
X=2^4501-349*2^500+347.
```

The result is a strict no-go at the present label depth.  The permanent labels
strongly restrict occupancy, but **cyclic closure itself imposes no additional
contradiction**: every cyclic valuation-label word satisfying the obvious
Chinese-remainder compatibility already produces a closed cyclic residue word
modulo `M`.

This does not invalidate occupancy or height arguments using the labels.  It
rules out only the strategy of obtaining G3 from bare label closure modulo
`N*1093^2`.

## Setup

Write

```text
q=1093,
h=ord_q(2)=364,
q^2=1194649,
N=2^500-1.
```

The primary multiplier satisfies

```text
N|X,
q||X,
X=q*c,
q does not divide c,
2^h==1 (mod q^2).
```

For an accelerated transition

```text
2^a_i*n_(i+1)=X*n_i+1,                              (1)
```

define the labels

```text
t_i == a_i (mod 500),
1<=t_i<=500,

s_i == a_i (mod 364),
1<=s_i<=364.
```

Since `gcd(500,364)=4`, an integer valuation `a_i` with these two labels exists
if and only if

```text
t_i==s_i (mod 4).                                   (2)
```

## Theorem 1: the `N` coordinate closes for every cyclic label word

Reducing (1) modulo `N` and using `N|X` gives

```text
n_(i+1)==2^(-a_i)==2^(-t_i) (mod N).                (3)
```

Therefore, for an arbitrary cyclic word `t_0,...,t_(p-1)`, define

```text
r^N_(i+1)=2^(-t_i) (mod N).                         (4)
```

Then every transition congruence (1) modulo `N` holds, including the wraparound
transition from index `p-1` to index `0`.  No relation between distinct `t_i`
is forced by cyclic closure.

## Theorem 2: the `q^2` adjacent-label coordinate closes for every cyclic label word

The Wieferich adjacent-label formula gives

```text
n_(i+1)
 ==2^(-s_i)*(1+q*c*2^(-s_(i-1))) (mod q^2).         (5)
```

Take an arbitrary cyclic word `s_0,...,s_(p-1)` and define, with indices modulo
`p`,

```text
r^q_(i+1)
 =2^(-s_i)*(1+q*c*2^(-s_(i-1))) (mod q^2).          (6)
```

Then

```text
r^q_i==2^(-s_(i-1)) (mod q).                        (7)
```

Consequently

```text
X*r^q_i+1
 ==q*c*2^(-s_(i-1))+1
 ==2^s_i*r^q_(i+1)                                  (mod q^2). (8)
```

Because `2^a_i==2^s_i (mod q^2)`, equation (8) is exactly transition (1)
modulo `q^2`.  It also holds at wraparound.  Thus every cyclic `s`-word gives a
closed cyclic residue word modulo `q^2`.

## Theorem 3: combined closure modulo `N*q^2`

Let cyclic label words `(t_i)` and `(s_i)` satisfy (2) for every `i`.  For every
index, combine the two coordinates

```text
r_(i+1)==r^N_(i+1) (mod N),
r_(i+1)==r^q_(i+1) (mod q^2)                         (9)
```

by the Chinese remainder theorem.  Since `gcd(N,q)=1`, this defines one residue
class modulo `M=N*q^2`.

Equations (3) and (8) show that

```text
2^a_i*r_(i+1)==X*r_i+1 (mod M)                      (10)
```

for every index, including wraparound, for any choice of integers `a_i`
realizing the compatible labels.  Hence the combined permanent labels admit a
closed modular cycle for every compatible cyclic label word.

## Exact count recovered

For each ordered pair `(s_(i-1),s_i)` there are exactly

```text
500/gcd(500,364)=125
```

choices of `t_i` satisfying `t_i==s_i (mod 4)`.  Therefore the number of combined
permanent classes is

```text
364^2*125=16562000,
```

exactly the retained class count.

## Consequence for the proof strategy

There is no principle-level contradiction of the form

```text
permanent label constraints + cyclic wraparound = impossible
```

at modulus `N*1093^2`.  Cyclic wraparound is already built into the adjacent
label formulas and is satisfied identically for every compatible cyclic label
word.

Accordingly, the following routes remain viable:

1. occupancy plus height/correction estimates, where repeated classes control
   the sum of `1/n_i` or force large representatives;
2. a deeper lift, such as modulo `1093^3` or a modulus where the unknown
   valuation layer no longer disappears and accumulates nontrivially around the
   cycle;
3. the exact global divisor `g`, which contains information not present in the
   bare permanent class labels;
4. changing the candidate if no deeper arithmetic invariant can couple labels
   globally.

But merely requiring the finite label automaton to close cannot exclude a
cycle for the present candidate.

## Verification

Independent exact checker:

```text
python tools/verify_permanent_label_cyclic_closure_no_go.py
```

The checker verifies the candidate divisibilities, exact orders and Wieferich
condition, all `364^2` adjacent-label transition identities modulo `q^2`, the
`N` coordinate identities, the compatibility count, and cyclic wraparound on
several deterministic regression words.
