# Multi-edge repetition ladder

For either remaining sparse-window length, assign to each edge the exact cost

```text
c_i=(s_i-1)+(s_(i+1)-1)+2*O*q_i,
sum_i c_i=2*(A-p).
```

An edge is `K`-cheap when `c_i<K`.  Since every chosen threshold below is much
smaller than `2O`, a cheap edge has `q_i=0` and its adjacent labels satisfy

```text
s_i+s_(i+1)<=K+1.
```

## 1. Number of all-cheap windows

At most

```text
E_K=floor(2*(A-p)/K)
```

edges are not cheap.  A bad edge belongs to at most `m` cyclic windows of `m`
consecutive edges.  Therefore at least

```text
p-m*E_K
```

cyclic `m`-edge windows are entirely cheap.

Let `W_m(K)` be the number of positive label words

```text
(u_0,...,u_m)
```

satisfying

```text
u_(j-1)+u_j<=K+1
```

for every adjacent pair.  The exact dynamic recurrence is

```text
F_0(v)=1,
F_j(v)=sum_(u=1)^(K+1-v) F_(j-1)(u),
W_m(K)=sum_v F_m(v).
```

Pigeonhole then forces one word to occur at least

```text
ceil((p-m*E_K)/W_m(K))
```

times.

## 2. Exact optimized ladder

The following thresholds give the retained common lower bounds for both
remaining lengths:

| edges `m` | threshold `K` | admissible words `W_m(K)` | forced repetitions |
|---:|---:|---:|---:|
| 2 | 349 | 14,230,475 | 3,114,290,401,257 |
| 3 | 491 | 12,157,734,961 | 2,918,613,523 |
| 4 | 629 | 13,180,060,652,871 | 2,251,677 |
| 5 | 762 | 16,650,853,633,108,401 | 1,500 |

No trajectory enumeration is involved; these numbers follow from the exact
cost identity and the finite recurrence above.

## 3. A word fixes a class modulo a higher power of X

A zero-layer label word of `m` edges determines its terminal value modulo

```text
X^(m+1).
```

Indeed, the exact affine iterate formula depends on the starting value only
through `X^m*n_0`, so its residue modulo `X^(m+1)` needs only the starting full
class modulo `X`.  The target is odd, giving one odd lift modulo
`2*X^(m+1)`.

Different label words give different classes.  From the terminal class one
recovers the final label modulo `X`; applying the exact inverse step recovers
the preceding class modulo `X^m`, and repeating recovers the whole word.

Thus the repeated words above force distinct cycle values in one arithmetic
progression of step `2*X^(m+1)`.

## 4. Height consequences

The strongest four exact diameter bounds are:

```text
m=2:
7077391788339522082878518496985204893557388703844566593307772732359784688

m=3:
692126427931979192228790418011743147969714364959656132701343054118705629843703466512831844

m=4:
55719787664457027479737747699827589970881363580579180213349939166117827517013940621066136776234942443748648

m=5:
3870792567252275975939498201310492491155314740805796060324781763695205605253434152368864087556133785129469874414691399795398
```

The last number is a forced cycle diameter from only `1500` repetitions of one
five-edge word modulo `2*X^6`.

## 5. Meaning

The remaining hypothetical cycles must exhibit a hierarchy of repeated exact
transition words at successively higher powers of the full modulus.  This does
not contradict local realizability, but it supplies a modular-height ladder for
combination with explicit cycle-height upper bounds or a future circulation
potential.

Run

```text
python tools/verify_multi_edge_repetition_ladder.py
```

for the exact certificate.
