# Second-block escalation for the Mersenne candidate `X=15`

Let

```text
C(n)=(15*n+1)/2^v2(15*n+1).
```

Assume, only for this note, that a nontrivial positive cycle exists, and let `w`
be the least positive odd integer whose orbit enters that cycle.  By the
minimal-basin lemma,

```text
w=2^s*u+1,
1<=s<=3,
u odd,
```

and the first step is

```text
y=C(w)=15*u+2^(4-s)>w.                            (1)
```

This note controls the complete valuation block beginning at `y`.

## 1. Exceptional second blocks are impossible

Suppose first that

```text
v2(y-1)=4*k,
k>=1,
y=16^k*v+1,
v odd.
```

The complete Mersenne exceptional-block identity gives the smaller ordinary
seed

```text
z=15^(k-1)*v
```

with

```text
C^k(y)=C(z).
```

Hence `z` enters the same cycle.  But from (1),

```text
y=15*u+2^(4-s)<16*(2^s*u+1)=16*w,
```

and therefore

```text
z<16^(k-1)*v=(y-1)/16<w.
```

This contradicts the defining minimality of `w`.  Thus the second block cannot
be exceptional.

## 2. Exact nonexceptional coordinates

Write the remaining case as

```text
y-1=2^(4*k+t)*v,
1<=t<=3,
k>=0,
v odd.                                           (2)
```

After the first `k` valuation-`4` steps, the state immediately before the final
valuation-`t` step is

```text
p=2^t*15^k*v+1.                                   (3)
```

Solving (1)--(2) for the original least basin seed gives

```text
w=(2^(4*k+t+s)*v+2^s-1)/15.                       (4)
```

Consequently `p<w` is equivalent to

```text
2^t*(2^(4*k+s)-15^(k+1))*v > 16-2^s.              (5)
```

For `s=1,2,3`, define the first coefficient-contraction indices

```text
K_1=32,
K_2=21,
K_3=10.
```

They are the least integers `k` satisfying

```text
15^(k+1)<2^(4*k+s).
```

At `k=K_s` inequality (5) already holds for every `t in {1,2,3}` and every
positive odd `v`; its left side only increases with `k` and `v`.  Therefore
minimality forces

```text
k<K_s.                                             (6)
```

## 3. Escalation consequence

A nonexceptional block of terminal type `t` can contract only when

```text
k>=K_t.
```

Combining this with (6), a contracting second block must satisfy

```text
K_t<=k<K_s.
```

Since

```text
K_1>K_2>K_3,
```

this forces

```text
t>s.                                               (7)
```

Thus the complete list is:

```text
initial s=3:
  the second block is always strictly growing;

initial s=2:
  a contracting second block must have t=3 and 10<=k<=20;

initial s=1:
  a contracting second block must have
    t=2 and 21<=k<=31,
  or
    t=3 and 10<=k<=31.
```

Every other second block either is impossible by minimality or grows from its
own starting state.

## 4. Meaning and limitation

This is a strict reduction of the three minimal-basin entrance types.  In
particular, the hardest entrance type `s=3` now has two consecutive complete
blocks that are forced to grow.

The lemma does not yet exclude a later contracting block, because after a
number of growing blocks the current height may be much larger than `w`.  The
next task is to iterate the same comparison with a height credit or record-ratio
potential.

Independent checker:

```text
python tools/verify_mersenne_second_block_escalation.py
```
