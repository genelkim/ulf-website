---
title: ULF Intro 3 - Inference with ULFs
author:
  - gene
  - len
categories:
  - Introduction
  - Inference
date: 2019-01-08 03:00:00
---

An important insight of NLog research is that language can be used directly for
inference, requiring only phrase structure analysis and upward/downward
entailment marking (polarity) of phrasal contexts. This means that NLog
inferences are _situated_ inferences, i.e. their meaning is just as dependent
on the utterance setting and discourse state as the linguistic "input" that
drives them. This insight carries over to ULFs, and provides a separate
justification for computing ULFs, apart from their utility in the process of
deriving deep, context-independent, canonicalized meaning representations from
language.

ULFs in principle provide a more reliable and more general basis for situated
inference than phrase structure, because of the coherent semantic type
structure they encode. Greater reliability also leads to the possibility of
spontaneous forward inferencing, as opposed to inference guided by systems
classifying already provided hypotheses as entailments, contradictions, or
neutral in relation to some reference sentence (as in most textual entailment
and NLog studies to date -- e.g. SNLI, MNLI). Forward inference is important
because human language understanding seems to involve continuous forward
inferencing. Imagine reading the following sentence in a paper or newsfeed

> Police reported that the vehicle struck several cars

you will conclude that

(a) the reported event almost certainly happened,

and further,

(b) that the cars involved were all damaged.

Conclusion (a) requires only a small amount of knowledge about communication,
to the effect that _reporting_ (in your preferred media) typically involves
reporting of facts; whereas conclusion (b) depends on very specific world
knowledge. We expect to show ULF utility for forward inference in cases like
conclusion (a), since accumulation of sufficient world knowledge for enabling
such inferences seems practical. In principle, ULF could support inferences
resulting in conclusion (b) -- within the bounds of ULF ambiguity -- but the
necessary world knowledge remains out of reach in the short run. As a whole
it's unreasonable to expect that an inference system will have a set of
alternative hypotheses to choose from. Rather, the system needs to be able to
generate inferences directly.

The rules for generating inference (a) could be as simple as

```
(all_wfulf w
  ((something.pro ((past report.v) (that w)))
   => ((the.d (event-of w)) probably.adv-s (past happen.v))))
```

where `all_wfulf` denotes substitutional quantification over well-formed ULF
formulas. Substitutational quantification quantifies over substitutions of
expressions of a particular category of metavariable. {% cite morbini2008WMR %}
describes the details of this mechanism and how it fits into object level
semantics. We can take the ULF formula for the report above

```
;; "Police reported that the vehicle struck several cars"
((k police.n)
 ((past report.v)
  (that ((the.d vehicle.n) ((past strike.v) (several.d (plur car.n)))))))
```

and conclude

```
;; "The event of 'the vehicle struck several cars' probably happened"
((the.d (event-of ((the.d vehicle.n) ((past strike.v) (several.d (plur car.n))))))
 probably.adv-s (past happen.v))
```

We ended up relying on a non-standard operator `event-of` here for simplicity.
This could be translated into using the _characterizing_ operator `**`, which
is implicit in strict ULF.

### Propositions vs Events

To get more concrete about the role of the semantic types in generating
inferences, consider the distinction between propositions and events.
Propositions are abstract, true or false _information_ objects and as such can
be _asserted, known, believed, disputed, etc._; whereas events are surely real,
temporal entities in the world, often with causal consequences -- without them,
there would be no natural or social world as we know it. Here are two sentences
that demonstrate this distinction,

(1) _Molly barked last night; that woke up the neighbors._

(2) _Molly barked last night; that's what the neighbors assert._

Note that propositions don't wake neighbors, but events certainly can; and
events can't be asserted, but propositions certainly can. As such _that_ in the
two sentences must refer to distinct entities (_that_ in (1) refers to an event
and _that_ in (2) refers to proposition). Events can have temporal parts at any
scale, and can physically involve many entities, but propositions cannot.
Propositions and events are easily confused because they are closely related:
natural language sentences _express_ propositions and at the same time _characterize_ events
or situations. But an adequate semantic representation must distinguish them,
thus providing distinct referents for the two instances of the anaphoric _that_
in the above sentences. For a full discussion see {% cite schubert2000book %}
and also {% cite zucchi1989phd %}. In general, propositions believed (or
rejected) by people are central to explaining the _reasons_ for their actions,
while events interact _causally_. In EL, the propositional referent in the
second sentence is provided simply by applying the sentence reifying operator,
`that` to the meaning of the sentence, whereas the event is generated during the
deindexing process. Basing inferences on sharp distinctions of propositions and
episodes as described is justified in detail in {% cite schubert2000book %}.

Of course the other semantic types: various subcategories of predicates, kinds
of actions, kinds of events, general kinds, numbers, collections, predicate
modifiers, etc. also make distinctions important to inference. The most crucial
aspect of ULF in supporting justified inferences, however, is the coherent semantic
composition. So long as antecedents of inference rules operate over fragments
of well-formed ULF and consequents respect the semantic types during any
restructuring, we can be certain that conclusions will have coherent semantic
structures.

Here are some kinds of inferences we can expect ULFs to support:

### NLog inferences based on generalizations/specializations

The sentence _"Every NATO member sent troops to Afghanistan"_, together with
the knowledge that France is a NATO member and that Afghanistan is a country
entails that _France sent troops to Afghanistan_ and that _France sent troops
to a country_.

```
((every.d (member-of.n |NATO|))
 ((past send.v) (k (plur troop.n))
                (to.p-arg |Afghanistan|)))
```
`(|France| ((pres be.v) (member-of.n |NATO|)))`, `(|Afghanistan| ((pres be.v) (= (a.d country.n))))`

We won't get into the details of computing contextual polarity here, but simply
state that _NATO member_ is in positive context and _Afghanistan_ is in negative
context. Positive context allow specializations, whereas negative contexts allow
generalization of the predicates while retaining truth conditions. So we can
resolve the right side of `(|France| ((pres be.v) (member-of.n |NATO|)))` into
the sentence to get

```
((every.d (= |France|))
 ((past send.v) (k (plur troop.n))
                (to.p-arg |Afghanistan|)))
```

then resolve the left hand side of `(|Afghanistan| ((pres be.v) (= (a.d
country.n))))` to get

```
((every.d (= |France|))
 ((past send.v) (k (plur troop.n))
                (to.p-arg (a.d country.n))))
```

Right now we get the awkward, but not incorrect sentence of _Everything that is
France sent troops to a country_. We can simplify to just _France sent troops to
a country_ with an intuitive inference rule `(all x (every.d (= x)) x)`. Simply
put, if we're quantifying over everything that is logically equal to a particular
entity, it's just going to be that entity. We can use it to clean up the formula.

```
(|France| ((past send.v) (k (plur troop.n)) (to.p-arg (a.d country.n))))
```

Such inferences are within the scope of NLog-based and ULF-based methods, and
can help in finding inference paths to candidate entailments; but they will not
be our focus as they rarely seem worthwhile as spontaneous forward inferences
from sentences in discourse (we are particularly interested in dialogue
settings).

### NLog inferences based on implicatives

_"She managed to quit smoking"_ entails that _She quit smoking_ (and the
negation of the premise leads to the opposite conclusion). We already
demonstrated such inferences using fully-resolved Episodic Logic for various
headlines {% cite stratos2011KEOD %}, such as the inference from _Oprah is
shocked that Obama gets no respect_ (Fox News 2011) to _Obama gets no respect_.
Such inferences are surely important -- and immediate -- in language
understanding. Here is a simplified walk through of generating these inference
in ULF to give an idea of how this is handled.

We have the formula

(F1) `(she.pro ((past manage.v) (to (quit.v (ka smoke.v)))))`

and an inference rule for _manage_, which we'll call (R1)
```
(all_ulfvp w
  (all x
    ((x ((past manage.v) (to w)))
     => (past (x w)))))
```

We can resolve the term `she.pro` in (F1) to `x` in (R1) and the ULF VP
predicate `(quit.v (ka smoke.v))` in (F1) to `w` in (R1).  When we run (R1)
with this resolution, we conclude

`(past (she.pro (quit.v (ka smoke.v))))`

This gives us the meaning we're looking for of _She quit smoking_. The `past`
is placed at the sentence level for simplicity (and it's not incorrect since
`past` is actually a sentence level operator anyway), but the tense can also be
automatically inserted into the VP where it would normally appear in ULF using
a more complicated pattern matching procedure in the inference rule.

### Inferences based on attitudinal and communicative verbs

This category of inferences intersects a bit with inferences from implicatives
that we just described. For example, we can conclude from both of the sentences

> We know that coffee is a fruit

> They found out that coffee is a fruit

that the proposition _coffee is a fruit_ is true in a way that is very similar
to what was shown for "manage" in the previous section. However, attitudinal
and communicative verbs can also involve probabilistic reasoning, structural
elaboration, and depend of constituent types -- all of which would be difficult
to capture within NLog. Consider the sentence

> John denounced Bill as a charlatan

(F2)
```
(|John| ((past denounce.v)
         |Bill|
         (as.p-arg (= (a.d charlatan.n)))))
```

We can conclude from this sentence that (a) _John probably believes that Bill
is a charlatan_, (b) _John asserted to his listeners (or readers) that Bill
is  a charlatan_, and (c) _John wanted his listeners (or readers) to believe that
Bill is a charlatan_. Notice that these inferences go beyond just relating embedded
events and propositions with truth values, but relate the arguments in more complex
ways.

Inference (a) could be captured with a simple lexical inference rule like the
following

(R2)
```
(all_ulfpred w
  (all x (all y
    ((x ((past denounce.v) y (as.p-arg w)))
     => (x probably.adv-s ((pres believe.v) (that (y ((pres be.v) w)))))))))
```

By resolving `|John|`, `|Bill|` and `(= (a.d charlatan.n))` in (F2) to `x`,
`y`, and `w` in (R2), respectively, we conclude the formula for

> John probably believes that Bill is a charlatan

```
(|John| probably.adv-s
 ((pres believe.v)
  (that (|Bill| ((pres be.v) (= (a.d charlatan.n)))))))
```

With some additional complexity, this could be generalized to other communicative verbs
that use the [verb]-[direct object]-[p-arg] construction (e.g. declare).

Inference (b) and (c) can be captured with a rules which can be generalized to just about
any communicative verb.

(R3)
```
(all_ulfpred w
  (all x (all y
    ((x ((past denounce.v) y (as.p-arg w)))
     => (x ((past assert.v)
            (adv-a (to.p ((x 's) ((plur reader.n) or.cc (plur listener.n)))))
            (that (y ((pres be.v) w)))))))))
```

(R4)
```
(all_ulfpred w
  (all x (all y
    ((x ((past denounce.v) y (as.p-arg w)))
     => (x ((past want.v)
            ((x 's) ((plur reader.n) or.cc (plur listener.n)))
            (to (believe.v (that (y ((pres be.v) w)))))))))))
```

By again resolving `|John|`, `|Bill|`, and `(= (a.d charlatan.n))` to `x`, `y`, and `w`, respectively
in each of (R3) and (R4), we conclude inferences (b) and (c).

> John asserted to his readers or listeners that Bill is a charlatan

```
(|John| ((past assert.v)
         (adv-a (to.p ((|John| 's) ((plur reader.n) or.cc (plur listener.n)))))
         (that (|Bill| ((pres be.v) (= (a.d charlatan.n)))))))
```

> John wanted his readers or listeners that Bill is a charlatan

```
(|John| ((past want.v)
         ((|John| 's) ((plur reader.n) or.cc (plur listener.n)))
         (to (believe.v (that (|Bill| ((pres be.v) (= (a.d charlatan.n)))))))))
```

(R3) and (R4) could be generalized so that `denounce.v` is replaced by any
other communicative verb that occurs in this argument context. Or by generalizing
`past` to the different tenses.

(R2) gives us a good opportunity to highlight the importance of the types in
generating inferences. Given a sentence like _"Mary denounced Bill as well"_,
we wouldn't want to infer that _Mary believes that Bill is well_. Here's the
ULF annotation of this sentence.

```
(|Mary| ((past denounce.v) |Bill| as_well.adv-s))
```

Since "as well" in this sentence is an adverbial, not an argument, the
antecedent of (R2) won't be able to unify with this sentence.


### Inferences based on counterfactuals

_"If I were rich, I would pay off your debt"_ and _"I wish I were rich"_ both
implicate that _the speaker is not rich_. This depends on recognition of the
counterfactual form, which is distinguished in ULF. Consider, for example,
the ULF for the first sentence.

(F3)
```
((if.ps (i.pro ((cf were.v) rich.a)))
 (i.pro ((cf will.aux-s) pay_off.v (your.d debt.n))))
```

`cf` is the counterfactual marker that sits in the same position as the tense
marker in the sentence. We can then write inferences over sentences like this
by identifying the counterfactual marker and asserting the negation of the
sentence it operates over. These inference rules must interact with ULF syntax
analysis so we will use predicates over ULF syntax, `embedded-within?`
and functions over the syntax, `tense-of!` and `with-tense!`.

(R5)
```
(all_wfulf w1
  (all_wfulf w2
    (((embedded-within? w1 w2) and.cc ((tense-of! w1) = cf))
     => (not (with-tense! w1 pres)))))
```

`embedded-within?` returns true if the first argument is embedded within the
second argument. For example, `(i.pro ((cf were.v) rich.a))` in the formula
(F3). `tense-of!` returns the tense of the given ULF formula. `with-tense!`
returns the ULF formula of the first argument modified to have the tense
given in the second argument.

We can unify (F3) to `w2` in (R5) and `(i.pro ((cf were.v) rich.a))` to `w1`
in (F3) to run the inference rule. We just described why `(embedded-within? w1
w2)` is true, and clearly `(tense-of! w1)` will be `cf`. If we replace the tense
in `w1` with `pres` and negate it as described in (R5), we conclude

```
(not (i.pro ((pres were.v) rich.a)))
```

We can either add some post-processing or add some complexity to the (R5) to
deal with the fact that `were.v` is only possible in counterfactual form and
should be mapped to `be.v`.


### Inferences from questions and requests

_"When are you getting married?"_ enables the inference that the addressee will
get married (in the foreseeable future), and that the questioner wants to know
the expected date of the event, and expects that the addressee probably knows
the answer, and will supply it. Similarly an apparent request such as _"Could
you close the door?"_ implies that the speaker wants the addressee to close the
door, and expects he or she will do so. There are subtleties in the distinction
between questions and requests that can be captured in ULF and made use of.

We'll walk through a simple example with _"Who did you see yesterday?"_. From
this we infer the presupposed knowledge that you did meet someone yesterday.
Let's start with the ULF of the sentence.

(F4)
```
((sub who.pro ((past do.aux-s) you.pro (see.v *h yesterday.adv-e))) ?)
```

All the wh-phrases in English can be modified to make a statement with using
"some". _who_ corresponds to _someone_, _where_ corresponds to _somewhere_,
_why_ correpsonds to _for some reason_, etc. So again, we assume the existence
of a predicate `wh-sent?` and functions `wh-sent-to-some-sent!` and
`uninvert-sent!` over the ULF syntax.

(R6)
```
(all_wfulf w
  (((w ?) and (wh-sent? w))
   => (uninvert-sent! (wh-sent-to-some-sent w))))
```

The predicate and function over the syntax of ULF is used because wh-words can
occur in many places in the sentence.  This means a syntactic analysis rather
than a case-by-case inference system is better suited for this problem.

Running (R6) over (F4) gives us
```
(sub someone.pro (you.pro ((past do.aux-s) (see.v *h yesterday.adv-e))))
```

in English, "Someone you did see yesterday". We can get a more natural reading
by applying the `sub` macro and running an inference rule for eliminating the
`do.aux-s`, which is an auxiliary almost solely used for question inversions
with minimal semantic influence.

```
(you.pro ((past see.v) someone.pro yesterday.adv-e))
```
in English, "You saw someone yesterday".

[Prev: ULF Intro 2]({{ site.baseurl }}/2019/01/07/ulf-intro-2-role-of-ulf-in-el-interpretation)

