# Audit of the claimed Mersenne-cycle theorem in Santos (2020)

Robert Santos, *On the Collatz general problem qn+1* (arXiv:2005.00346), claims that when

```text
q = 2^m-1
```

there is only the trivial positive cycle. If valid, that statement would be extremely useful: combined with an orbit known not to reach `1`, it could produce a divergent example.

The proof cannot be used as written, because a key lemma has an elementary counterexample.

## The stated lemma

Lemma 13 of the paper states, in substance:

> If `q=2^m-1` divides `k*2^c-1`, for rational `k` satisfying the stated size condition, then `k` must be a power of two.

## Counterexample

Take

```text
m = 3,
q = 2^3-1 = 7,
k = 9,
c = 2.
```

Then

```text
k*2^c-1 = 9*4-1 = 35,
```

and therefore

```text
7 | 35.
```

But

```text
k=9
```

is not a power of two. The counterexample even uses an integer `k`, so allowing rational `k` cannot repair the statement.

## Where the descent breaks

The proof repeatedly divides a quantity by `2^m` and then continues to use divisibility notation as if the new quantity remained an integer. After the first division this need not be true. Ordinary integer divisibility

```text
q | K-1
```

is not preserved when `K` has become a nonintegral rational number.

The example above exposes exactly this failure.

## Consequence

This audit does **not** prove that the claimed Mersenne-cycle theorem is false. It proves only that the supplied proof does not establish it.

Therefore the project must not combine the Santos theorem with another lemma and announce a divergent orbit. A new independent proof of Mersenne cycle exclusion would still solve an important part of the problem, but it remains unavailable here.

This is recorded to prevent the same tempting but invalid shortcut from being reused.

## Reference

R. Santos, *On the Collatz general problem qn+1*, arXiv:2005.00346 (2020), especially Lemma 13 and the subsequent Mersenne-cycle theorem.