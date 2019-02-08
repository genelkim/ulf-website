---
title: ULF Intro 1 - Introduction to ULF Type Structure
author: 
  - gene
  - len
categories:
  - Introduction
  - Type Structure
date: 2019-01-08 01:00:00
---

The following six examples provide an idea of the language-like 
syntax of ULFs. The first two are from the Tatoeba database, the next
three are from _The Little Prince_ (which was used for the first 
AMR-annotated corpus), and the last is from the Web:

1. <span class="ex-sent">Could you dial for me?</span>
```
(((pres could.aux-v) you.pro (dial.v {ref1}.pro 
                              (adv-a (for.p me.pro)))) ?)
```
2. <span class="ex-sent">If I were you I would be able to succeed.</span>
```
((if.ps (I.pro ((cf were.v) (= you.pro))))
 (I.pro ((cf will.aux-s) 
         (be.v (able.a (to succeed.v)))))) 
```
3. <span class="ex-sent">He neglected three little bushes</span>
```
(he.pro ((past neglect.v) 
         (three.d (little.a (plur bush.n)))))
```
4. <span class="ex-sent">Flowers are weak creatures</span>
```
((k (plur flower.n)) ((pres be.v) 
                      (weak.a (plur creature.n))))
```
5. <span class="ex-sent">My drawing is not a picture of a hat</span>
```
((my.d drawing.n) ((pres be.v) not
                   (= (a.d (picture-of.n (a.d hat.n))))))
```
6. <span class="ex-sent">Very few people still debate the fact that the earth is heating up</span>
```
(((fquan (very.mod-a few.a)) (plur person.n)) still.adv-s 
  (debate.v (the.d (n+preds fact.n 
                            (= (that ((the.d |Earth|.n) 
                                      ((pres prog) heat_up.v)))))))))
```

As can be seen, ULF structure quite closely reflects phrase structure; 
and the type tags of atomic constituents, such as `.pro`, `.v`, `.p`, `.a`, 
`.d`, `.n`, etc., are intended to echo the part-of-speech origins of these 
constituents, such as _pronoun, verb, preposition, adjective, determiner,
  noun,_ etc., respectively. Originally, ULFs contained some \\(\lambda\\)-abstracts,
for example to form a conjunctive predicate from postmodified nouns,
but we have introduced syntactic sugar elements that relieve annotators
from coding such abstracts. An example is seen in (6): The `n+preds`
macro takes a noun and one or more predicates as complements, and these
are expanded into a \\(\lambda\\)-abstracted conjunctive predicate in
postprocessing. As a result, ULFs are relatively amenable to human
creation and intuitive interpretation. Moreover, as mentioned in the 
Introduction, the proximity to surface structure enables NLog-like
inference and more.

But then isn't parsing into ULF just another variant of syntactic
parsing? The essential difference is that the type tags correspond
to broad semantic categories (certain types of model-theoretic 
functions), and as such enable us to ensure that the type structure 
of ULFs -- their operator-operand combinations -- are semantically 
coherent. Richard Montague's profoundly influential work can be 
viewed as demonstrating the crucial importance of paying attention
to the semantic types of words and phrases, and that doing so leads 
to a view of language as very close to logic; as a result it lends
itself to inference, at least to the extent that we can resolve --
or are prepared to tolerate -- various forms of ambiguity, 
context-dependence and indexicality.

Our semantic types are not as high-order as Montague's, nor as "rigid"
as Montague's, but they suffice for maintaining type coherence. In
particular, quantification is first-order, i.e., it iterates over 
individual entities, not over predicates, etc. -- though through
reification of predicate meanings and sentence meanings, we can "talk
about" kinds of things, kinds of actions, propositions, etc., not just
ordinary objects.

As soon as we take semantic types seriously in ULFs like the above,
we see that certain type-shifting operators are needed to maintain type
coherence. For example, in sentence (1) the phrase _for me_ is coded
as `(adv-a (for.p me.pro))`, rather than simply `(for.p me.pro)`.
That is because it is functioning here as a _predicate modifier_,
semantically operating on the verbal predicate `(dial.v {ref1}.pro)`
(_dial a certain thing_). Without the `adv-a` operator the 
prepositional phrase is just a 1-place predicate. Its use as a predicate 
is apparent in contexts like _"This puppy is for me"_. Note that
semantically the 1-place predicate `(for.p me.pro)` is formed by 
applying the 2-place predicate `for.p` to the (individual-denoting) 
term `me.pro`. (Viewing \\(n\\)-place predicates as successively applied 
to their arguments, each time reducing the adicity, is in keeping with 
the traditions of Schönfinkel, Church, Curry, Montague, and others -- 
hence "curried" predicates.) If we apply `(for.p me.pro)` to another 
argument, such as `|Snoopy|` (the name of a puppy), we obtain a truth 
value. So semantically, `adv-a` is a _type-shifting operator_
of type (_predicate_ \\(\rightarrow\\) (_predicate_ \\(\rightarrow\\)
_predicate_))), where the predicates are 1-place and thus of type 
(_entity_ \\(\rightarrow\\) _truth value_). Of course, the name 
`adv-a` is intended to suggest "adverbial", in recognition of the 
grammatical distinction between predicative and adverbial uses of 
prepositional phrases.

Then there is the issue of _intensionality_. For example,
(2) is a counterfactual conditional, and the consequent clause _"I
  would be able to succeed"_ is not evaluated in the actual world, but
in a possible world where the (patently false) antecedent is imagined
to be true. ULF and deeper LFs derived from it are based on a semantics
where sentences are evaluated in _possible situations (episodes)_,
whose maxima are possible worlds. Details about syntactic forms and 
semantic types in the Episodic Logic approach to LF have been provided in many
past publications {% cite hwang1992thesis hwang1994ICTL schubert2000book %}.
This project website also contains separate posts that describe the syntax and
semantic types in depth.

We don't want to dive too deep for this introduction, but we note some further
type-shifting operators in the examples to clarify the role of type-shifters in
ULF.  `to` (synonym: `ka`) in (2) shifts a verbal predicate to a _kind (type)
of action or attribute_, which is an abstract individual; `k` in (4) shifts a
nominal predicate to a _kind_ of thing (so the subject here is the abstract
kind, flowers, whose instances consist of sets of flowers; and `that` in (6)
produces a reified _proposition_ (again an abstract individual) from a sentence
meaning. Through these type shifts, we are able to maintain a simple, classical
view of predication, while allowing greater expressivity than the most widely
employed logical forms, for example enabling generalized quantification (as in
(6)), modification, reification, and other forms of intensionality.

The positioning of `(adv-a (for.p me.pro))` within the verbal predicate
it modifies, rather than in prefix-operator position, already indicates
a certain looseness in the ULF syntax, as opposed to the rigidity of formal
logic. This is unproblematic because we restrict the way operators may
combine with operands so that type consistency is assured  -- and in fact 
in subsequent processing, any `(adv-a (...))` constituents of a verbal 
predicate are moved so as to immediately precede that predicate. There
are a number of further kinds of looseness in ULFs, but we defer further
discussion to separate posts.

To wrap up this introductory discussion, we note a general concern that might
be raised about ULFs.  Since they largely conform with surface syntax, they are
clearly language-specific. Isn't the point of semantics to get at the deeper
meanings underlying the surface forms or language, and shouldn't these be
somewhat uniform across languages? Our answer is two-fold: First, from a
semantic perspective, the ULFs for different languages will have certain
essential commonalities, namely, means to express predication, truth-functional
and other connectives, generalized quantifiers, predicate and sentence
modification, predicate and sentence reification, implicit and explicit
reference to events/situations, comparatives, and a few other devices. Surface
order is less important than these semantic commonalities. Second, we do think
that sentence meanings should be factored into (as far as possible) minimal,
separately usable, canonical propositions. This seems plausible both from
speculations in cognitive science about "Mentalese", and from a practical
perspective, since canonicalization ensures that connections between ideas can
be quickly recognized and used for inference. This canonicalization is the topic
of the next post of the ULF introduction.  Of course the meaning of sentences
"in the wild" can be much more complex and subtle. Our hypothesis is that we
can conquer those complexities effectively by starting with a type-coherent
surface form, and systematically deriving canonical forms, bringing to bear
many different kinds of influential factors.  The next subsection elaborates on
this view.

[Next: ULF Intro 2]({{ site.baseurl }}/2019/01/07/ulf-intro-2-role-of-ulf-in-el-interpretation)

