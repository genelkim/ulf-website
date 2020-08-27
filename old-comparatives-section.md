---
title: Comparatives in ULF
author:
  - gene
  - len
categories:
  - Comparatives
  - Type Structure
tags:
  - ULF Version 1.1
---

_NOTE: This post at this point is just digesting my correspondences with Len starting
with the most-recent. This should be cleaned up into a coherent post for
helping annotators._

We are presenting a new procedure for annotating comparatives which preserves
the syntactic structure while allowing us to automatically transform it into a
more explicit degree-comparison structure.

## Direct relations over comparable values

To start off, there are the simple relational comparatives which operate over
directly comparable values using `more.a` or `less.a` with `than.p` supplying
what the subject is being compared against, the _COMPARATIVE CLAUSE_.

- _"5 is more than 3"_

```
(5 ((pres be.v) (more.a (than.p 3))))
```

## Predicate-based comparisons mediated with a copula

Then there are cases where instead of just _"more"_, we have a predicate-based
comparison, such as _"5 is bigger than 3"_. Notice that _"bigger"_ can be thought
of as _"more big"_. For these cases, we will annotate it almost exactly as the
direct comparatives.

- _"5 is bigger than 3"_

```
(5 ((pres be.v) ((-er big.a) (than.p 3))))
```

You can see that here we have the operator `-er`. `-er` and `more.adv` are
aliases of each other. This is actually a shortened form of _"5 is bigger than
3 {is big}"_ so really it is a case of ellipsis. However, since the operating
verb is the copula (_"be"_), which doesn't contribute any semantic content, we
can automatically reconstruct _"3 {is} big"_ from what we have available in
the context of `((-er big.a) (than.p 3))`.

The key components to our comparative shorthand the `(([comp] [pred]) ([than]
X))` construction, where `[comp]` can be some form of _"more"_ or _"less"_
(including _"-er"_), `[pred]` is the comparison predicate, `[than]` is some
form of _"than"_ and `X` is the comparative clause. The post-processing will
recognize this construction and only have access to informtaion within this,
which will motivate the various annotation mechanisms to handle all the forms
of comparison structures. Before moving on the all the variations, let's look
at how this relates to the _"5 is bigger than 3"_ and related examples.

For _"5 is bigger than 3"_, we can use the information available in `((-er
big.a) (than.p 3))` to construct the elided comparative clause _"3 {is} big"_
by recognizing that `3` is a noun phrase, not a sentence so we need to introduce
the predicate to form a sentence for comparison. So we move the `[pred]`, here
`big.a` to form `(3 big.a)` which translates to _"3 {is} big"_.

So I mentioned that this construction is only available when the verb operating
over the comparison. So what happens if we try to do this with _"I eat more
food than John"_? The annotation is `(i.pro ((pres eat.v) ((more.d food.n)
(than.p |John|))))`. This sentence really means _"I eat more food than John
{eats food}"_. It turns out we can't reconstruct the full form from `((more.d
food.n) (than.p |John|))` since we don't have access to _"eats"_ we can't
ignore it like with the with the copula. We consider this a case of a
correlated gap for _"food"_ with an elided verb _"eat"_, which we will discuss
how to handle below.


## Simple High-coverage Cases

Most comparatives (at least in the Brown corpus) are fairly simple relational
comparatives. These will be annotated with `than.p`. For example, _"Five is
more than three"_ is simply annotated

```
(5 ((pres be.v) (more.a (than.p 3))))
```

Some more have gaps, which we'll use the `*h` variable to mark the position and
`than-gap.p` to mark the comparative that the gap corresponds to. A simple
example is _"He's faster than John is"_.

```
(he.pro ((pres be.v) ((-er fast.a)
                      (than-gap.p (|John| ((pres be.v) *h))))))
```

These can be complicated by ellipsis, _"He's faster than John"_,

```
(he.pro ((pres be.v) ((-er fast.a)
                      (than-gap.p (|John| ((pres {be}.v) *h))))))
```

or rightward displacement, _"He's faster now than he was last year"_.

```
(he.pro (rep ((pres be.v) ((-er fast.a) *p) now.adv-e)
              (than-gap.p (he.pro ((past be.v) *h (adv-e (last.a year.n)))))))
```

These gaps are what we will call _invisible subdeletion_ That is, the
subdeletion is in the gapped constituent, for example, the deleted adverbial
modifier for _"fast"_ in the examples above. For comparison, overt subdeletion
looks like _"He is more crafty than he is smart"_. 

```
(he.pro ((pres be.v) ((more.adv crafty.a)
                      (than-subdel.p (he.pro ((pres be.v) (*adv smart.a)))))))
```

Notice that we are using `than-subdel.p` and `*adv` now for _than_ and the
deleted adverbial specifier. `*adv` can also be `*det` or `*adj` if the
specifier is a determiner or an adjective.

Finally, there are also cases where _"more"_ really means "more many" or "more much"
depending on the countability of the noun.

_"More than 5 guests"_ : `((nquan ((more.adv many.a) (than.p 5))) (plur (guest-of.n *ref)))`

_"More than a cup of water"_ : `((nquan ((more.adv much.a) (than.p (a.d cup.n)))) (of.p (k water.n)))`


## Maximality of Degrees

When we have a sentence like _"I bought more apples than oranges"_ we will be
interpreting this into a formula like (ignoring tense and only scoping
quantification over degrees)

```
(the.d d1
  (the.d d2
    ((i.pro (buy.v ((nquan ((to-degree d1) many.a)) (plur apple.n)))) and.cc
     (i.pro (buy.v ((nquan ((to-degree d2) many.a)) (plur orange.n)))) and.cc
     (d1 > d2))))
```
we have a maximality assumption the degree values. For example, if I bought 5
apples and 4 oranges, it's also true that I bought 3 apples. But that
interpretation would cause this formula to be false. The trick here is the
definite-ness of the degree interpretation which forces a maximal reading on
the degree. By using `the.d` this can also be read as _"The many-ness of apples
that I bought is greater than the many-ness of oranges I bought"_ where
_"The many-ness of apples I bought"_ doesn't allow a subset selection. This
also works where the maximized value is less directly tied to the determiner:
_"the apples on the table"_ and _"the money in my pocket"_. Note that I'm using
_"-ness"_ as a way to turn `(to-degree d)` English. This is reminiscent of
Moltmann's __"tropes"__ (TODO: add reference). See section X discusses our
foray into using such an approach for handling scaled values.



## Moltmann's Tropes

TODO: look more into Moltmann's tropes and summarize.

We considered an approach similar to Moltmann's __"tropes"__ as an option for
handling our scaled values (e.g. `(((-ness big.a) (the.d box.n)) > ((-ness
big.a) (the.d box.n)))`). The main benefits for us was the fact that "-ness values"
are unique and avoid the introduction of degree variables. However, we found that
even when using "-ness values" we needed to introduce lambda variables elsewhere,
e.g. `(\lambda x (((-ness big.a) x) = d1))` which puts us back to where we were in
terms of variables. And the uniqueness constraint we handle by using definite
quantification (see [ref to Maximality of Degrees]).


## Comparatives with Gaps

- _"She is faster than I will ever be [fast]"_

```
(she.pro ((pres be.v)
          ((-er fast.a)
           (than-gap.p (i.pro ((pres will.aux-s)
                               ever.adv-e
                               (be.v *h)))))))
```

This will be transformed into the following formula (only scoping degree variables).

```
(the.d d1
  (the.d d2
    ((she.pro ((pres be.v) ((to-degree d1) fast.a))) and.cc
     (i.pro ((pres will.aux-s) ever.adv-e (be.v ((to-degree d2) fast.a)))) and.cc
     (d1 > d2))))
```

To perform this transformation, let the than-complement be notated \\( \phi
\\) and the head of the comparative be notated \\( \sigma \\). So for this
example, \\( \phi = \\) `(i.pro ((pres will.aux-s) ever.adv-s (be.v *h)))`
and \\( \sigma = \\) `(-er fast.a)`. We create a variant of the comparative
\\( \sigma'\_{d1} \\) using `to-degree`, `((to-degree d1) fast.a)`. Then we
can create the expanded than-complement by applying \\( \sigma'\_{d2} \\) to
a lambda-abstracted \\( \phi \\), we will notate this \\( \psi \\). Explicitly,
\\( \psi = ((\lambda \text{ \*h } \phi) \; \sigma'\_{d2}) \\). If we expand this out,

\\( \psi = \\) `((lambda *h (i.pro ((pres will.aux-s) ever.adv-e
(be.v *h)))) ((to-degree d2) fast.a))`

\\( = \\) `(i.pro ((pres will.aux-s) ever.adv-e (be.v ((to-degree d2)
fast.a))))`.

Then let \\( \pi\_{\kappa} \\) be the predicate internal to the comparative head
(`fast.a` in this example). Finally we construct the comparative predicates (`and.cc` is replaced with \\( \wedge \\)).
\\[ 
  \pi\_{K} = (\lambda x \; (\text{the.d } d1 \; (\text{the.d } d2 \; ((x \; ((\text{to-degree } d1) \; \pi\_{\kappa})) \wedge \psi \wedge (d1 > d2))))) 
\\]
Concretely, \\( \pi\_{K} = \\)
```
(lambda x
  (the.d d1
    (the.d d2
      ((x ((pres be.v) ((to-degree d1) fast.a))) and.cc
       (i.pro ((pres will.aux-s) ever.adv-e (be.v ((to-degree d2) fast.a)))) and.cc
       (d1 > d2)))))
```

Then this is applied to the subject to get the entire sentence presented above.


- _"walks faster than I can run [fast]"_

This case is very similar to the last, but with an adverbial rather than
predicate head (_"is faster than"_ vs _"walks faster than"_). This turns out to
have almost the exact same handling, but with the addition of the `adv-a`
type-shifter to transform the predicates associated with the compared degrees
to adverbs.

Annotated ULF
```
((pres walk.v)
 ((adv-a (-er fast.a))
  (than-gap.p (i.pro ((pres can.aux-v) (run.v *h))))))
```

The head of the comparative is handled the same way, while keeping the `adv-a`
type-shifter. \\( \sigma' \\) in this case includes the type-shifter,
so \\( \sigma'\_{d2} = \\) `(adv-a ((to-degree d2) fast.a))`. Putting this all
together, we get the following comparative-expanded verb phrase fragment.
```
(lambda x
  (the.d d1
    (the.d d2
      ((x ((pres walk.v) (adv-a ((to-degree d1) fast.a)))) and.cc
       (i.pro ((pres can.aux-v) (run.v (adv-a ((to-degree d2) fast.a))))) and.cc
       (d1 > d2)))))
```


- _"has a bigger house than I have [a big house]"_

In this case, the gap is the noun phrase, the same as the head of the
comparative. So we can handle this in just the same way as the previous
examples, where the degree-overt comparative head is used to fill the gap.

Annotated ULF
```
((pres have.v)
 ((a.d ((-er big.a) house.n))
  (than-gap.p (i.pro ((pres have.v) *h)))))
```

\\( \sigma = \\) `(a.d ((-er big.a) house.n))`

\\( \sigma'\_d = \\) `(a.d (((to-degree d) big.a) house.n))`

Comparative-expanded verb phrase fragment.
```
(lambda x
  (the.d d1
    (the.d d2
      ((x ((pres have.v) (a.d (((to-degree d1) big.a) house.n)))) and.cc
       (i.pro ((pres have.v) (a.d (((to-degree d2) big.a) house.n)))) and.cc
       (d1 > d2)))))
```

__Note on generalization.__ For gaps where the gap is the same as the
comparative head without the comparison word/morpheme ('more', '-er', 'less',
etc.), we simply use \\( \sigma' \\) to create the degree-overt versions for
the comparative head and gap and then use the comparison word/morpheme for the
degree comparison.


- _"has a bigger garage than I have a [big] house"_

For this the deleted element is not the same as the comparative head. In that
sense, this seems to be a case of _specifier subdeletion_. However, notice that
_"big"_ is not a specifier for the comparison (e.g. _"much"_, _"many"_). So
what we have is a construction that in form looks a lot like specifier
subdeletion, but the deleted element includes both the specifier and the
predicate. Regardless, at this point, we will simply treat these in the same
way as specifier subdeletion, but with the \*adj gap marking which will let us
know to grab a different portion of the comparative head.

Annotated ULF
```
((pres have.v)
 ((a.d ((-er big.a) garage.n))
  (than-subdel.p (i.pro ((pres have.v) (a.d (\*adj house.n)))))))
```

This will find the comparison atom and first check that the predicate it
operates over is an adjective. Then, it forms the gap filler from that,
in this case `(to-degree big.a)`

Comparative-expanded
```
(lambda x
  (the.d d1
    (the.d d2
      ((x ((pres have.v) (a.d (((to-degree d1) big.a) garage.a)))) and.cc
       (i.pro ((pres have.v) (a.d (((to-degree d2) big.a) house.n)))) and.cc
       (d1 > d2)))))
```

__ALTERNATIVELY__, we could treat this as an instance of rightward displacement.
That is, we can consider this to be a displaced version of _"has a bigger than 
I have a house garage"_. In such a case, we could treat this the exact same way
as normal comparative deletion.

Annotated ULF
```
((pres have.v)
 (a.d (rep (((-er big.a) *p) garage.n)
           (than-gap.p (i.pro ((pres have.v) (a.d (*h house.n))))))))
```

Obviously, this will expand into the same comparative-expanded fragment by
design. But this will happen in the same manner as the simple gapped examples
we started with, but after resolving the `rep` displacement operator. 


- _"saw more bears than he could count [how-many bears]"_

The annotation for this is very straightfoward. Exactly how you would expect
from other ULF annotations and simple comparative gap handling.

Annotated ULF
```
((past see.v)
 ((more.d (plur bear.n))
  (than-gap.p (he.pro ((past can.aux-v) (count.v *h))))))
```

What is trickier here, is that there is no predicate to have a degree
comparison over. We end up treating `more.d` as `(nquan (-er many.a))` (i.e.
_"many-er"_) to get access to the underlying predicate. Once we've done that the
treatment is the same as other comparative deletion gaps.

Comparative-expanded
```
(lambda x
  (the.d d1
    (the.d d2
      ((x ((past see.v) ((nquan ((to-degree d1) many.a)) (plur bear.n)))) and.cc
       (i.pro ((past can.aux-v) (count.v ((nquan ((to-degree d2) many.a)) (plur bear.n))))) and.cc
       (d1 > d2)))))
```

- _"More food that I can eat is on the plate"_

This is almost exactly the same as the previous example. `more.d` from _"More
food"_ is treated as `(fquan (-er much.a))` instead of `(nquan (-er many.a))`
since _"food"_ is a mass noun.

Annotated ULF
```
(((more.d food.n)
  (than-gap.p (i.pro ((pres can.aux-v) (eat.v *h)))))
 ((pres be.v) (on.p (the.d plate.n))))
```

Comparative-expanded
```
(the.d d1
  (the.d d2
    ((((fquan ((to-degree d1) much.a)) food.n) ((pres be.v) (on.p (the.d plate.n)))) and.cc
     (i.pro ((pres can.aux-v) (eat.v ((fquan ((to-degree d2) much.a)) food.n)))) and.cc
     (d1 > d2))))
```


- _"More people than he had invited [how-many people] showed up"_

This is the same as the _"more bears"_ example.

Annotated ULF
```
(((more.d (plur person.n))
  (than-gap.p (he.pro ((past perf) (invite.v *h)))))
 (past show_up.v))
```

Comparative-expanded
```
(the.d d1
  (the.d d2
    ((((nquan ((to-degree d1) many.a)) (plur person.n)) (past show_up.v)) and.cc
     (i.pro ((past perf) (invite.v ((nquan ((to-degree d2) many.a)) (plur person.n))))) and.cc
     (d1 > d2))))
```


- _"It's more beautiful than I can put into words {that it is} [how beautiful]"_

I've already sort of given away the solution to this in providing the elided
and gapped material, but if you imagine that the bracketed information isn't
there, you might first conclude that the sentence is a gapped version of _"It's
more beautiful than I can put *its beauty* into words"_. However, once we try
to provided the information for such a gap from the comparative head, we'll
find that we don't have what we need. The gap wants a noun phrase, but the
comparative head is an adjective phrase. Rather, this is a case of the
beginning of the complement "that it is" being elided. 

Annotated ULF
```
(it.pro
 ((pres be.v)
  ((more.adv beautiful.a)
   (than-gap.p (i.pro ((pres can.aux-v) (put.v (into.p-arg (k (plur word.n)))
                                               (tht ({it}.pro ((pres {be}.v *h)))))))))))
```

Comparative-expanded
```
(the.d d1
  (the.d d2
    ((it.pro ((pres be.v) ((to-degree d1) beautiful.a))) and.cc
     (i.pro ((pres can.aux-v) (put.v (into.p-arg (k (plur word.n)))
                                     (tht ({it}.pro ((pres ({be}.v ((to-degree d2) beautiful.a))))))))))))
```


__ALTERNATIVE__

I wonder if this is a case relating to how comparatives can act a lot like
coordination. I can't find a sentence of a similar construction where the
elided information isn't part of the sentence scoping outside of the
comparative construction. A simple example that is very different but seems
to require the coordination-like distribution is _"It is more scary than
dangerous"_. Where this needs to expand to _"It is more scary than it is
dangerous"_. Similarly, _"It is more beautiful than I can put into words"_
can be thought of as distributing _"It is more beautiful"_ into the
_than_-clause. But this doesn't seem to be the case. After looking more into
it, this sort of coordinated gapping is not allowed in embedded clauses.
For example ((137b) from Lechner and Corver 2017) 

_"Felix knows more Greek than (*I believe that) Max ... Latin"_

But this brings up another issue. It seems these coordinated constructs. I
suppose we could just treat these as cases where we need to manually fill in
the elided content?

```
(|Felix| ((pres know.v) 
          ((more.d |Greek|.n)
           (than-subdel.p (|Max| ((pres {know}.v) (*det |Latin|.n)))))))
```
TODO: wait I don't think |Greek| and |Latin| are nouns...

Another example. _"I pet more dogs than you cats"_

Also, there's the issue of multiple CSD?

_"More women ate more sandwiches than men ate bananas"_

## Forms of Ellipsis

Beyond comparative deletion and subdeletion, there are several categories of
ellipsis for comparative structures. Since in ULF ellipsis is just manually
restored with curly-brackets to indicate the restoration, we don't have to
concern ourselves with these variants, though being comfortable with them may
help if identifying how to restore the elided material. Here are annotations
with elision. The examples below are from Lechner and Corver (2017).

- __Gapping__

_"John bought more apples than Bill pears."_
```
(|John| ((past buy.v)
         ((more.d (plur apple.n))
          (than-subdel.p (|Bill| ((past {buy}.v) (*det (plur pear.n)))))))) 
```

- __Pseudo-gapping__

_"John bought more apples than Bill did pears."_
```
(|John| ((past buy.v)
         ((more.d (plur apple.n))
          (than-subdel.p (|Bill| ((past do.aux-s) ({buy}.v (*det (plur pear.n)))))))))
```

- __VP-deletion__

_"John bought more apples than Bill did."_
```
(|John| ((past buy.v)
         ((more.d (plur apple.n))
          (than-gap.p (|Bill| ((past do.aux-s) ({buy}.v *h)))))))
```

- __Comparative Ellipsis__

_"John bought more apples than Bill."_
```
(|John| ((past buy.v)
         ((more.d (plur apple.n))
          (than-gap.p (|Bill| ((past {buy}.v) *h))))))
```

