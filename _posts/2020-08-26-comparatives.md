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

We are presenting a new procedure for annotating comparatives which preserves
the syntactic structure while allowing us to automatically transform it into a
more explicit degree-comparison structure. We are addressing comparatives
including deleted gaps, movement, and ellipsis. We are not addressing
superlatives, excessives, and _enough_-constructions.

## Simple Relational Comparatives

To start off, there are the simple relational comparatives which operate over
directly comparable values using `more.a` or `less.a` with `than.p` supplying
what the subject is being compared against. We'll call the constituent starting
with `than.p` the _COMPARATIVE COMPLEMENT_ and the adjective `more.a` the
_COMPARATIVE HEAD_ in line with some recent linguistics literature (Lechner and
Corver 2017). I'll also refer to them together as the _COMPARATIVE CLAUSE_.
Note that `less.a` can be used in place of `more.a` in all of the following
examples.

- _"5 is more than 3"_
```
(5 ((pres be.v) (more.a (than.p 3))))
```

We have the same construction using _'-er'_ adjectives.

- _"5 is bigger than 3"_
```
(5 ((pres be.v) (bigger.a (than.p 3))))
```

- _"Bob is taller than Ed"_
```
(|Bob| ((pres be.v) (taller.a (than.p |Ed|))))
```

The _comparative clause_ can be used as an adjective phrase more generally.
Below are examples of its use as a post-nominal modifier and as an adverb.

- _"A number bigger than 3"_
```
(a.d (n+preds number.n
                (bigger.a (than.p 3))))
```

- _"She ran further than that"_
```
(she.pro ((past run.v) (adv-a (further.a (than.p that.pro)))))
```

### _"More"_ as a modifier

_"More"_ can also act as an adjective or prepositional modifier. Note that
`less.mod-a` can be used in place `more.mod-a` and at the moment ULF treats
prepositional phrases as adjectives.

- _"Bob is more tolerant than Ed"_
```
(|Bob| ((pres be.v) ((more.mod-a tolerant.a) (than.p |Ed|))))
```

- _"My legs are more in the bag than my arms"_
```
((my.d (plur leg.n)) ((pres be.v)
                        ((more.mod-a (in.p (the.d bag.n)))
                         (than.p (my.d (plur arm.n))))))
```

#### _"More"_ and _"much-er"_

Now we've run into two different but related uses of _"more"_ which are
important to distinguish. We define
```
more.a := (more.mod-a much.a) [for mass nouns]
more.a := (more.mod-a many.a) [for count nouns]
```
and
```
-er := more.mod-a
```

That is, we think of _"5 is more than 3"_ as meaning the same thing as _"5 is
much-er than 3"_. This allows us to unify the underlying constructions of the
examples so far. Here are the expanded versions of the first two examples of
this post.

- _"5 is more than 3"_
```
(5 ((pres be.v) ((more.mod-a much.a) (than.p 3))))
```

- _"5 is bigger than 3"_
```
(5 ((pres be.v) ((-er big.a) (than.p 3))))
```

This unified correspondence simplifies the mapping to the final comparison form
with explicit comparisons of the underlying degrees. We won't get into that
now. I give some examples later on of the expanded forms which will give some
intuition about the annotation format and help with tricky cases.

For the purposes of annotation, we'll just use `more.a` and `bigger.a`
directly, leaving the identification of the underlying predicate, e.g. `big.a`,
as a follow-up resolution/disambiguation step.

### 'More' as a determiner

_"More"_ can also be used as a determiner in front of noun phrases in which case
we annotate it `more.d`. Everything else is the same.

- _"I drank more soda than John"_
```
(i.pro ((past drink.v) ((more.d soda.n)
                          (than.p |John|))))
```

This can actually result in ambiguity in ditransitive verbs where it's not clear
which argument the NP in the comparative complement correponds to.

- _"John gave me more presents than Sam"_

This has the reading that John gave me and Sam presents and I received more.
The other reading is that John and Sam gave me presents and John gave more. Our
annotation will preserve this ambiguity. Pragmatically, this is more likely to
have the first reading since the second reading can be forced with an auxiliary
_"do"_, as in _"John gave me more presents than Sam did"_.


## Correlated Gaps

One very common comparative construction is a _CORRELATED GAP_. This is where
the predicates in the comparative head and the comparative complement are the
same. In this case, English requires the predicate in the comparative
complement to be deleted, leaving a gap. For example, the first sentence below
is the natural sentence and the second in the unfelitious sentence which
includes the second predicate.

- _"Usain is faster than I will ever be"_
- \*_"Usain is faster than I will ever be fast"_

In this case, we use a special form of _"than"_, `than-gap.p`, and use the `*h`
variable to mark the location of the gap. So the sentence above is annotated
as follows.
```
(|Usain| ((pres be.v) (faster.a
                       (than-gap.p (i.pro ((pres will.aux-s) ever.adv-e (be.v *h)))))))
```

We can automatically post-process this to fill the gap by taking the predicate
from the comparative head and fill the specifier appropriately using the form
of `more`. In this example, we don't have an explicit _"more"_ in the
comparative head, but we know that all _-er_ adjectives are derived from an
adjective predicate so _"more"_ would have to be `more.mod-a`.

Of course, we can have the same with `more.d`.

- _"Usain has run more miles than I will ever traverse"_
```
(|Usain| ((pres perf)
            (run.v (adv-a ({for}.p ((more.d (plur mile.n))
                                    (i.pro ((pres will.aux-s) ever.adv-e
                                            (traverse.v (adv-a ({for}.p *h)))))))))))
```

## Specifier Subdeletion

In cases where the two predicates that are being compared differ, we have a
phenomenon called _"SPECIFIER SUBDELETION"_. This is where the degree specifier
of the comparative complement is deleted. For example, _"He is more crafty than
he is {so and so much} smart"_ doesn't have the actual degree (e.g. _"{so and
so much}"_) for _"more"_ to operate over. In fact, in English this is never
overt.  In this case, we use `than-subdel.p` for _"than"_ and still use `*h` to
mark the location of the deleted element.

- _"He is more crafty than he is smart"_
```
(he.pro ((pres be.v) ((more.mod-a crafty.a)
                        (than-subdel.p (he.pro ((pres be.v) (*h smart.a)))))))
```

- _"More cats than dogs were at the park"_
```
(((more.d (plur cat.n))
    (than-subdel.p (*h (plur dog.n))))
   ((past be.v) (at.p (the.d park.n))))
```

In this case, since we're using `than-subdel.p` we know to fill the deleted
element with the specifier, not the predicate. If the _comparative complement_
contains the same type of constituent as the _comparative head_  (e.g. the dogs
and cats example) and is simply a replacement within the context, we can leave
it be without filling any information (as we would do for ellipsis). We can
post-process the substitution.  This is not an adjective versus noun
distinction. Here's a shortened version of the adjective example.

- _"He is more crafty than smart"_
```
(he.pro ((pres be.v) ((more.mod-a crafty.a)
                        (than-subdel.p (*h smart.a)))))
```

And though it sounds awkward, the longer version of the noun example, with
a bracket of the constituency to help parse it.

- _"More cats than [dogs were at the park] were at the park"_
```
(((more.d (plur cat.n))
    (than-subdel.p ((*h (plur dog.n))
                    ((past be.v) (at.p (the.d (park.n)))))))
   ((past be.v) (at.p (the.d park.n))))
```

A more natural way to say this is _"More cats were at the park than dogs were
at the park"_, but that involves rightward displacement of the comparative
clause, which we haven't discussed yet.


### Tricky examples for distinguishing simple relational comparatives from specifier subdeletion

Sometimes determiner specifier subdeletion can look deceivingly similar to
relational comparatives. In relational comparatives, the noun phrase in the
comparative complement corresponds to the subject argument of the embedding
sentence. In determiner specifier subdeletion, the comparative complement
corresponds to the predicate in the comparative head.

- _"I drank more soda than John"_
```
(i.pro ((past drink.v)
          ((more.d soda.n) (than.p |John|))))
```

- _"I drank more soda than water"_
```
(i.pro ((past drink.v)
          ((more.d soda.n) (than-subdep.p (*h water.n)))))
```

And this can only be resolved through reasoning about world knowledge in the
most general case.

- _"Dogs eat more food than grass"_
```
((k (plur dog.n)) ((pres eat.v)
                     ((more.d food.n) (than-subdel.p (*h grass.n)))))
```

- _"Dogs eat more food than cats"_
```
((k (plur dog.n)) ((pres eat.v)
                     ((more.d food.n) (than.p (k (plur cat.n))))))
```

## Templates of Comparative Constructions

Now that we've covered all of the comparative-specific constructions (not
including displacement and ellipsis which are more universal tools in ULF),
here they all are in template form for reference. The `(more.mod-a <adj/pp>)`
includes _-er_ adjectives and `more.a`. And of course we have the _"more"_ to
_"less"_ substitutions.

First, the basic relational comparison where `<np>` is being compared to the
argument of this whole phrase.

- `((more.mod-a <adj/pp>) (than.p <np>))`, `((more.d <noun>) (than.p <np>))`

Now the case of a correlated gap.

- `((more.mod-a <adj/pp>) (than-gap.p <sent containing *h>))`, `((more.d <noun>) (than-gap.p <sent containing *h>))`

The general case of specifier subdeletion.

- `((more.mod-a <adj/pp>) (than-subdel.p <sent containing *h>))`, `((more.d <noun>) (than-subdel.p <sent containing *h>))`

Specifier subdeletion with a correlation to the comparative head predicate.

- `((more.mod-a <adj/pp>) (than-subdel.p (*h <adj/pp>)))`, `((more.d <noun>) (than-subdel.p (*h <noun>)))`


## Rightward Displacement

Comparative structures often have rightward displacement, which can make it
a bit tricky to find the correct underlying semantic structure.

- _"More people showed up than we had chairs"_
```
(rep (((more.d (plur person.n)) *p) (past show_up.v))
       (than-subdel.p (we.pro ((past have.v) (*h (plur chair.n))))))
```

This is actually a displaced version of _"More people than we had chairs showed
up"_. And here's the dogs and cats example again.

- _"More cats were at the park than dogs were at the park"_
```
(rep (((more.d (plur cat.n)) *p) ((past be.v) (at.p (the.d park.n))))
       (than-subdel.p ((*h (plur dog.n)) ((past be.v) (at.p (the.park.n))))))
```

The key to reconstructing the right form is to find the comparative head (which
includes _"more"_, _"less"_,or  _"-er"_) and the comparative complement (the
constituent headed by _"than"_) that fit together to make sense.


## Ellipsis

Beyond correlated gaps and specifier subdeletion, there are several categories
of ellipsis for comparative structures. Since in ULF ellipsis is just manually
restored with curly-brackets to indicate the restoration, we don't have to
concern ourselves with these variants, though being comfortable with them may
help if identifying how to restore the elided material. Here are annotations
with elision. The examples below are from Lechner and Corver (2017).

- __Gapping__

_"John bought more apples than Bill pears."_
```
(|John| ((past buy.v)
         ((more.d (plur apple.n))
          (than-subdel.p (|Bill| ((past {buy}.v) (*h (plur pear.n))))))))
```

- __Pseudo-gapping__

_"John bought more apples than Bill did pears."_
```
(|John| ((past buy.v)
         ((more.d (plur apple.n))
          (than-subdel.p (|Bill| ((past do.aux-s) ({buy}.v (*h (plur pear.n)))))))))
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
          (than.p |Bill|))))
```

Notably, we consider the case of __comparative ellipsis__ case of the simple
relational comparison. We're considering a mechanism to handle VP-deletion (and
other single constituent deletion), but we haven't converged on that yet.


## Full Derivations (Comparatives with Gaps)

This is just a section where I worked through the examples that Len sent in an
email. This will be the basis for the section on describing how our surface
forms map to explicit degree meaning.

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

To perform this transformation, let the comparative complement without `that.p`
be notated \\( \phi \\) and the head of the comparative be notated \\( \sigma
\\). So for this example, \\( \phi = \\) `(i.pro ((pres will.aux-s) ever.adv-s
(be.v *h)))` and \\( \sigma = \\) `(-er fast.a)`. We create a variant of the
comparative head \\( \sigma'\_{d1} \\) using `to-degree`, `((to-degree d1)
fast.a)`. Then we can create the expanded comparative complement by applying
\\( \sigma'\_{d2} \\) to a lambda-abstracted \\( \phi \\), we will notate this
\\( \psi \\). Explicitly, \\( \psi = ((\lambda \text{ \*h } \phi) \;
\sigma'\_{d2}) \\). If we expand this out,

\\( \psi = \\) `((lambda *h (i.pro ((pres will.aux-s) ever.adv-e
(be.v *h)))) ((to-degree d2) fast.a))`

\\( = \\) `(i.pro ((pres will.aux-s) ever.adv-e (be.v ((to-degree d2)
fast.a))))`.

Then let \\( \pi\_{\kappa} \\) be the predicate internal to the comparative
head (`fast.a` in this example). Finally we construct the meaning of the full
comparative phrase (`and.cc` is replaced with \\( \wedge \\)).
\\[
  \pi\_{K} = (\lambda x \; (\text{the.d } d1 \; (\text{the.d } d2 \; ((x \; ((\text{to-degree } d1) \; \pi\_{\kappa})) \wedge \psi \wedge (d1 > d2)))))
\\]
Concretely, \\( \pi\_{K} = \\)
```
(lambda x
  (the.d d1
    (the.d d2
      ((x ((to-degree d1) fast.a)) and.cc
       (i.pro ((pres will.aux-s) ever.adv-e (be.v ((to-degree d2) fast.a)))) and.cc
       (d1 > d2)))))
```

Then this is can be the non-subject argument of the copula.


- _"walks faster than I can run [fast]"_

This case is very similar to the last, but with an adverbial rather than
predicate head (_"is faster than"_ vs _"walks faster than"_). This turns out to
have almost the exact same handling, but with the addition of the `adv-a`
type-shifter to transform the predicates associated with the compared degrees
to adverbs.

Annotated ULF
```
((pres walk.v)
 (adv-a ((-er fast.a)
         (than-gap.p (i.pro ((pres can.aux-v) (run.v (adv-a *h))))))))
```

The head of the comparative is handled the same way, so \\( \sigma'\_{d2} = \\)
`((to-degree d2) fast.a)`. Putting this all together, we get the following
comparative-expanded verb phrase fragment.
```
(lambda x
  (the.d d1
    (the.d d2
      ((x ((pres walk.v) (adv-a ((to-degree d1) fast.a)))) and.cc
       (i.pro ((pres can.aux-v) (run.v (adv-a ((to-degree d2) fast.a))))) and.cc
       (d1 > d2)))))
```


- _"has a bigger house than I have [a big house]"_

In this case, the gap is the noun phrase, but the head of the comparative is _"bigger"_.
So we need to add in the elided information. We might be able to introduce a more generalized
correlated gap handling so that NPs like this can be treated directly, but we haven't fully
defined that yet.

Annotated ULF
```
((pres have.v)
 (rep (a.d (((-er big.a) *p) house.n))
      (than-gap.p (i.pro ((pres have.v) ({a}.d (*h {house}.n)))))))
```

\\( \sigma = \\) `(-er big.a)`

\\( \sigma'\_d = \\) `((to-degree d) big.a)`

Comparative-expanded verb phrase fragment.
```
(lambda x
  (the.d d1
    (the.d d2
      ((x ((pres have.v) (a.d (((to-degree d1) big.a) house.n)))) and.cc
       (i.pro ((pres have.v) ({a}.d (((to-degree d2) big.a) {house}.n)))) and.cc
       (d1 > d2)))))
```

__Note on generalization.__ For gaps where the gap is the same as the
comparative head without the comparison word/morpheme ('more', '-er', 'less',
etc.), we simply use \\( \sigma' \\) to create the degree-overt versions for
the comparative head and gap and then use the comparison word/morpheme for the
degree comparison.


- _"has a bigger garage than I have a [big] house"_

For this the deleted element is embedded in an NP. In that sense, this seems to
be a case of _specifier subdeletion_. However, notice that _"big"_ is not a
specifier for the comparison (e.g. _"much"_, _"many"_), rather it is the
predicate. So what we have is a construction that in form looks a lot like
specifier subdeletion, but the deleted element includes both the specifier and
the predicate.

By reading this as a case of rightward displacement, we can annotate it like
other correlated gaps. That is, we can consider this to be a displaced version
of _"has a bigger than I have a house garage"_.

Annotated ULF
```
((pres have.v)
 (a.d (rep (((-er big.a) *p) garage.n)
           (than-gap.p (i.pro ((pres have.v) (a.d (*h house.n))))))))
```

Comparative-expanded
```
(lambda x
  (the.d d1
    (the.d d2
      ((x ((pres have.v) (a.d (((to-degree d1) big.a) garage.a)))) and.cc
       (i.pro ((pres have.v) (a.d (((to-degree d2) big.a) house.n)))) and.cc
       (d1 > d2)))))
```


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
  ((more.mod-a beautiful.a)
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


## Additional issues

This is just a section with issues that I (Gene) ran into while reading up on
the linguistics literature on comparatives.

_"Felix knows more Greek than (*I believe that) Max ... Latin"_

But this brings up another issue. It seems these coordinated constructs. I
suppose we could just treat these as cases where we need to manually fill in
the elided content?

```
(|Felix| ((pres know.v)
          ((more.d |Greek|.n)
           (than-subdel.p (|Max| ((pres {know}.v) (*h |Latin|.n)))))))
```
TODO: wait I don't think |Greek| and |Latin| are nouns...

Another example. _"I pet more dogs than you cats"_

Also, there's the issue of multiple CSD?

_"More women ate more sandwiches than men ate bananas"_

## Equatives

It turns out we can handle equatives (e.g. _"I am as fast as my dog"_) in
exactly the same manner as comparatives by treating the first _"as"_ in the
same way as _"more"_/_"-er"_ in comparatives and the second _"as"_ in the same
way as _"than"_.

- _"I am as fast as my dog"_
```
(i.pro ((pres be.v)
          ((as.adv fast.a)
           (as.p (my.d dog.n)))))
```

- _"I run as fast as my dog"_
```
(i.pro ((pres run.v)
          ((as.adv fast.a)
           (as-gap.p ((my.d dog.n) ((pres {run}.v) *h))))))
```

- _"As many bears showed up as people"_
```
(rep ((((nquan (as.adv many.a)) (plur bear.n)) *p)
        (past show_up.v))
       (as-subdel.p ((*h (plur person.n)) (past {show_up}.v))))
```

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

## Nominal "more"

TODO: "more than money" example

## Adverbial "more than"

TODO: "more than happy" example

## Related phenomena that are not handled

- superlatives
- excessives
- _enough_-constructions

