---
title: Modification in ULF
author:
  - gene
  - len
categories:
  - Modification
  - Type Structure
tags:
  - ULF Version 1.0
---

{% assign dom = "\mathcal{D}" %}
{% assign sit = "\mathcal{S}" %}
{% assign tru = "\mathcal{2}" %}
{% assign prd = "\mathcal{N}" %}
{% assign rar = "\rightarrow" %}

### Prerequisite Knowledge

Understanding the crux of this post requires
- basic knowledge of EL semantic types and associated notation,
- basic knowledge of ULF syntax,
- basic knowledge of the EL interpretation process,
- familiarity with English syntax terminology, and
- familiarity with terminology such as 'predicate' and 'intensional' from logic.

Some details also require knowledge of
- Skolemization,
- lambda functions, and 
- the EL charaterizing operator `**`.


## Predicate Modification

EL semantic types represent predicate modifiers as functions from _monadic_
predicates to _monadic_ predicates, i.e. (\\(({{ dom }} {{ rar }} {{ tru }})
{{ rar }} ({{ dom }} {{ rar }} {{ tru }})\\)).  This enables handling of
non-intersective modifiers, e.g._nearly_, _fake_, _almost_.  These are further
distinguished by the syntactic category of the predicate being modified.

- _noun modification_: `(fake.mod-n diamond.n)`
- _adjective modification_: `(very.mod-a happy.a)`
- _verb modification_: `(nearly.adv-a fall.v)`

So the type extensions `.mod-n` and `.mod-a` are noun and adjective premodifier 
types, respectively.  `.adv-a` is the VP adverbial type, which corresponds to
monadic verb modifiers.  Ultimately, these become action modifiers in EL semantics,
hence the `-a` extension.  Since actions aren't explicitly represented in ULF,
`.adv-a` modifiers are represented as intensional monadic verb modifiers.
(See [Actions, Experiences, and Attributes](#actions-experiences-and-attributes) for
more details).

There are type-shifters that form operators of each of these types from monadic
predicates.  The operator names borrow from the extensions that accompany the
lexical versions of these modifiers.  So `mod-a`, `mod-n`, and `adv-a` (note,
no dot preceding them) are type-shifters that shift monadic predicates to 
adjective modifiers, noun modifiers, and VP modifiers, respectively.  Here are
some examples

`((mod-n wooden.a) shoe.n)`, `((mod-n ice.n) pick.n)`, `(fake.mod-n ruby.n)`,<br/> 
`((mod-n worldly.a) wise.a)`, `(very.mod-a fit.a)`, `(slyly.adv-a grin.v)`

In English there's also common noun premodification by a proper noun, e.g. 
_"Seattle skyline"_.  For this case we also introduce a type-shifter from 
a proper noun to a nominal modifier, `nnp`.

`((nnp |Seattle|) skyline.n)`

Here is a table of each of the type-shifters introduced so far along wth an example 
and the formal type.

<a name="tab:pred-mod-formers"></a>__Table of Predicate Modifier Forming Operators__

| _Name_ | _Example_ | _Formal Type_ |
|-----------|-----------|---------------|
| `mod-a` | `((mod-a worldly.a) wise.a)`            | \\({{ prd }} {{ rar }} ( {{ prd }}\_{ADJ} {{ rar }} {{ prd }}\_{ADJ} ) \\) |
| `mod-n` | `((mod-a (very.mod-a happy.a)) dog.n)`  | \\({{ prd }} {{ rar }} ( {{ prd }}\_{N} {{ rar }} {{ prd }}\_{N} ) \\) |
| `adv-a` | `(play.v (adv-a (with.p (a.d dog.n))))` | \\({{ prd }} {{ rar }} ( {{ prd }}\_{V} {{ rar }} {{ prd }}\_{V} ) \\) |
| `nnp`   | `((nnp |Seattle|) skyline.n)`           | \\({{ dom }} \rightarrow ( {{ prd }}\_{N} {{ rar }} {{ prd }}\_{N} ) \\) |

Since in ULF there are no valid adjective-adjective, adjective-noun, noun-noun,
noun-adjective compositions without this sort of type-shifting, we can often
omit `mod-a` and `mod-n` type-shifters and introduce them in post-processing.
For example, _"burning hot melting pot"_ is hand annotated as 

```
((burning.a hot.a) (melting.n pot.n))
```

which gets post-processed to

```
((mod-n ((mod-a burning.a) hot.a)) ((mod-n melting.n) pot.n))
```

Therefore, when there's a (ADJ ADJ), (ADJ N), (N N), or (N ADJ) structure we infer
that the first argument is a modifier and the second is being modified.

This cannot be done when the modifier is a verb -- _"running man"_,
_"sleeping beauty"_, _"frequently returning member"_, annotated `((mod-n run.v)
man.n)`, `((mod-n sleep.v) beauty.n)`, and `((mod-n (frequently.adv-f
return.v)) (member-of.n *ref))`, respectively.  The _-ing_ morpheme here seems
to be acting as an indication that this is a modifier, rather than marking a
progressive or turning the verb into a noun.  This also occurs for verb-verb
modification, e.g. _"He ran in the forest, looking at the trees"_ becomes 

```
(he.pro 
  ((past run.v) (adv-e (in.p (the.d forest.n))) 
                (adv-a (look.v (at.p-arg (the.d (plur tree.n)))))))
```

The subsection on [Participial Phrases](#participial-phrases) discusses such verb phrase
modifiers in more detail.  Verbs need explicit type-shifters because some verbs can
take predicate arguments so it would be ambiguous whether the noun or adjective following
a verb is an argument or if the verb is acting as a predicate modifier.  An example of 
a predicate argument is _sad_ in _"He looks sad"_.  _sad_ is a predicate argument to 
_looks_ in this case.  This is the same reason that verb modifiers (i.e. of `adv-a` type)
always require the type-shifter explicitly.




<!--
GENE: I changed some temporal versus atemporal wording above to be about verbal
versus adjectival predicates. I've tended to think of some adjectives as
temporal (e.g., angry, drunk) and others as atemporal (e.g., intelligent,
plaid, distant, flawed) -  more or less in line with Greg's stage- vs
individual-level predicates. Yet  '(very.adv-a angry.a)' seems to involve just
straightforward transformation of a predicate over individuals, not pairs.  But
I'm wondering if perhaps you had it right, and even 'angry' is atemporal, and
just becomes temporal when you apply "be" to it ("is angry"). I've wondered
about this before in connection with sentences like "Every drunk customer was
expelled from the bar", where we want to regard the restrictor predicate,
"drunk customer" as no different in terms of semantic type from an unmodified
nominal ("Every customer was expelled  from the bar"); i.e., if "customer" is
atemporal, then surely so is "underage, drunk  customer"; o/w the semantics of
quantification becomes exceedingly tricky. I do talk about this in my "book", I
think, opting for a Renate Musan-like analysis in terms  of maximal temporal
chunks of individuals (sub-individuals, one might say) that have  the
restrictor property over the temporal span they occupy... 
-->

<!--
TODO: introduce operators corresponding to `nn` and `nnp` for temporal predicates:
      "dirt brown", "feather light", "razer sharp", "crystal clear", "Atlanta hot",
      Actually, this seems to just be adjective modification, not any atemporal predicate.
      I can't think of any examples where the modified constituent is a verb... maybe
      "cheetah run", "feather fall"?

      This seems to indicate a distinction that isn't just temporal-atemporal,
      but a noun-adj-verb distinction.  If that's the case, why do we allow
      `adv-a` to take adjectives and verbs, and modify adjectives and
      verbs?  Also how do prepositional phrases fit into this? I generally
      think of prepositions as relational adjectives, but I can't think of any noun
      premodification of prepositional phrases.

      I think we might have let the *.adv-a extension get a bit overused at this point.
      It doesn't seem to have a coherent type.  We've allowed it to capture all
      adjective/verb/preposition-adjective/verb/preposition modification. I think we
      probably should be distinguishing between modifiers that actually happen at action-level
      and those that are actually intensional predicate modifiers.  So
        (he.pro ((past leave.v) politely.adv-a))
      is fine, but
        (he.pro ((pres be.v) (very.adv-a happy.a)))
      seems strange.  We definitely don't want this latter example to turn into:
       ((he.pro ((pres be.v) happy.a)) ** e1), ([he.pro | e1] very.adv-a)
 Rather, we seems to want something like 'very.adv/a' (along the lines of
 your previous suggestion of a/n for adjective-noun modifiers), so we'd have
 (he.pro ((pres be.v) (very.adv/a happy.a)))
      Similarly we'd introduce n/n, a/n, n/a, a/a, adv/a, n/v.  I would suggest including
      monadic prepositional phrases into adjective categories because of examples like
 "I am very in the zone", "He is almost in the forest"

      This would explicitly separate action modification from predicate modification.
      For action modification, we use `adv-a` which takes any predicate any can be
 used to modify the action - often an adjective and can be rewritten as -ly.
 This would capture all the manner adverbials as well as co-occurring actions.

      For predicate modification, we would be fully explicit about the syntactic type
      combinations since the ULF combinations are in fact the way the types are going
      to combine (no post-processed lifting to actions).  So we need to make sure the
      types combine properly.
 a/n : light feather (also attr)
        a/v : ?
        a/a : burning hot
 n/n : melting pot
        n/v : cheetah run?
        n/a : feather light
 v/n : ? - frequently returning member, sleeping beauty, running man, the never running man
        v/v : ? - adv-a for all these probably
        v/a : ?
        adv/n : ?
        adv/v : nearly run
        adv/a : very happy
      I'm not sure why the categories organize in this way... From an engineering perspective
      that doesn't matter so much, we just include this systematic procedure for simplicity
      even though not every category is used.  From a linguistic perspective, though I'm curious
      why the combinations exist the way they do...
-->

Notice from the examples in [the table of predicate modifier forming operators](#table:pred-mod-formers) 
that the operators aren't necessarily prefixed in ULFs, rather they appear in
the surface word order.  In EL, monadic operators are prefixed, whereas
operators with more arguments are infixed.  In ULF, we leave them in place
since the operator and operand can be inferred from the types of the
constituents.  Consider the types for `play.v` and `(adv-a (with.p (the.d
dog.n)))`.  Since the former is an verbal monadic predicate and the latter is
an verbal monadic predicate modifier, we can be certain that `(adv-a (with.p
(the.d dog.n)))` is the operator while `play.v` is the operand.

Premodification of adjectives and nouns in English tend to allow
non-intersective readings, though this isn't always the case. The formal type
of the modifiers described so far as intensional predicate modifiers (i.e. 
\\({{ prd }} {{ rar }} {{ prd }}\\) allows us to handle both cases.
An example of and intersective reading for premodification is _"triangular container"_ 
which we annotate as `((mod-n triangular.a) container.n)`. Since this relation is
intersective, given the correct background knowledge, we would infer that this
has the same meaning as `(lambda x ((x triangular.a) and.cc (x container.n)))`.
There are some constructions in English that really seem to always
indicate an intersective interpretation via the grammar, for which we annotate
them as such. This includes post-nominal modification and appositives.  For
example, we would annotate _"The buildings in the city"_ as (see the post
on macros for details of the `n+preds` macro)

```
(The.d (n+preds (plur building.n)                        
                (in.p (the.d city.n))))
```

which is equivalent to

```
(The.d (lambda x ((x (plur building.n)) and.cc
                  (x (in.p (the.d city.n))))))
```

Thus we distinguish grammatical constructions that indicate intersective
modification,  but ULFs do not distinguish all intersective vs.
non-intersective modification.


### Actions, Experiences, and Attributes

In the general description, we glanced over what actions -- and more generally,
experiences and attributes -- are (i.e. what `.adv-a` type predicate modifiers
ultimately act over in EL).  Here we describe them a bit more carefully.  
Adverbial modifiers of the sort `.adv-a` intuitively modify actions, experiences,
or attributes, which are a category of individuals in the EL ontology distinct from 
events and situations.  It's designed to deal with semantic subtleties such as:

1. _"He lifted the child easily"_ -- which refers to an action that was easy for the agent, rather than to an easy event;
2. _"He fell painfully"_ -- which refers to a painful experience rather than to a painful event; and 
3. _"He excels intellectually"_ -- which refers to an intellectual attribute rather than to an intellectual event or situation.

Actions, experiences, and attributes in EL are individuals comprised of
agent-episode pairs and this allows modifiers of the sort `.adv-a` to
express a constraint on both the agent (more generally, subject) of a sentence
and the episode it characterizes.  No sharp or exhaustive classification of
such pairs into actions, experiences, and attributes is presupposed by this --
the point is just to make the subject of sentences available in working out
entailments of VP-modification.  Since actions are derived, in part, from
explicit episodes and such episodes are implicit in ULFs until deindexing,
actions are also implicit in ULFs.  Formally, actions have the semantic type
\\({{ act }} \subset {{ dom }}\\), where \\({{ act }}\\) is the range of a
pairing function, `pair`, of type \\(({{ dom }} \times {{ sit }}) {{ rar }} 
{{ dom }}\\). These action-based constraints are derived from `.adv-a` 
predicate modifiers via meaning postulate inference rules.  So the formula 
(used in the main discussion)

`(|John| (play.v (adv-a (with.p (the.d dog.n)))))`

after event deindexing and canonicalization could become the formula

`[[|John| (play.v (adv-a (with.p (the.d dog.n))))] ** E1.sk]`

where `E1.sk` is a Skolemized episode variable.  From this we can infer

`[[|John| play.v] ** E1.sk]`,<br/> 
`[(pair |John| E1.sk) with.p (the.d dog.n)]`

The pairing function can also be written with the pipe shorthand, `(pair X Y)`
\\( \equiv \\) `[X | Y]`.  So the second formula above can be rewritten as 
`[[|John| | E1.sk] with.p (the.d dog.n)]`.  Lexical `.adv-a` modifiers are similarly
derived into predications over actions.  _"They escape quickly"_ (ignoring
tense) has the raw ULF representation

`(they.pro (escape.v quickly.adv-a))`

which after event deindexing, event canonicalization, and `.adv-a` inference results in

`[[they.pro escape.v] ** E1.sk]` and `[[they.pro | E1.sk] quick.a]`

Note the conversion of `quickly.adv-a` to `quick.a`, since a predication over actions
is inferred from the verb modification.  


### Participial Phrases  

In case you're unfamiliar, partiples are verbs are used as adjectives (_working woman_, _running man_) 
or nouns (_the exquisite cleaning_).  As you may have noticed, for simple cases we simply change the
suffix marking of the word to the POS that it is acting as; e.g. `(working.a woman.n)`, 
`(running.a man.n)`, and `(the.d (exquisite.a cleaning.n))`.  However, for complex participial phrases,
this no longer works because the verb may take arguments in ways don't fit into formal interpretation
of adjectives and nouns.  Consider for example, 

- I greeted the __frequently returning__ member
- We're required to submit a __carefully written__ notice
- Kenneth nervously watched the woman, __alarmed by her gun__
- I went back to sleep, __having heard this before__

It seems that we can make arbitrarily complex verb phrases into paritipial phrases, including
those that have passivization and perfect aspect.  All cases that initially looked tensed turned
out to be passivization as far as I've seen so far.  Participial phrases also don't 
allow progressives, since the _-ing_ morpheme is already in use.  It can get confusing
though since in many cases participles have a concurrent interpretation, but
this isn't always the case, e.g.

- _Lifting weights for two hours, Ron developed sore muscles_
- _The student scoring the highest grade on the exam will receive an award_

We consider the concurrent vs. non-concurrent interpretation to be a pragmatic
issue and therefore leave it ambiguous in the ULF representation of paritipial
phrases.

In ULF we don't have a single category for participial phrases since the
semantic type structure can vary.  When the verb is acting as a predicate
modifying adjective, we will treat complex participial phrases as untensed verb
phrases which may include `perf` and `pasv` which are type-shifted to the
appropriate predicate modifier.  For how we handle nominal participial phrases,
please refer to the __Derived Nominals__ section of the annotation guidelines.
Here are some concrete examples of complex predicate modifying participial
phrase annotations in ULF.

1. I greeted the __frequently returning__ member
```
(i.pro ((past greet.v) 
        (the.d ((mod-n (frequently.adv-f return.v)) 
                (member-of.n *ref)))))
```
2. We're required to submit a __carefully written__ notice
```
(we.pro ((pres (pasv require.v)) 
         (to (submit.v 
              (a.d ((mod-n (carefully.adv-a (pasv write.v))) 
                    notice.n))))))
```
3. Kenneth nervously watched the woman, __alarmed by her gun__
```
(|Kenneth| 
  (nervously.adv-a 
    ((past watch.v) (the.d woman.n)
                    (adv-a ((pasv alarm.v) (by.p-arg (her.d gun.n)))))))
```
4. I went back to sleep, __having heard this before__
```
(i.pro ((past go.v) back.adv-a (to.p-arg (k sleep.n))
                    (adv-a (perf (hear.v this.pro before.adv-e)))))
```
5. __Lifting weights for two hours__, Ron developed sore muscles
```
(sub 
  (adv-a (lift.v (k (plur weight.n)) 
                 (adv-e (for.p (two.d (plur hour.n))))))
  (|Ron| ((past develop.v) (k (sore.a (plur muscle.n))) *h)))
```
6. Any student __scoring a good grade on the exam__ will receive an award
```
((any.d (n+preds student.n
                 (score.v (a.d (good.a grade.n)) 
                          (on.p-arg (the.d exam.n)))))
 ((pres will.aux-s) (receive.v (an.d award.n))))
```


### Comparison of Modifier Notation Against Stanford Dependencies

The Stanford dependency parser indicates the lexical category of the modifier, not the operand.  

- `amod` - adjectival modifier
- `nmod` -- nominal modifier
- `advmod` -- adverbial modifier
- `partmod` -- participal modifier (e.g. _"recorded message"_)
- `tmod` -- temporal modifier (e.g. _"said today"_)
- etc.

If we regard their amod, nmod, partmod labels as of type monadic predicate to monadic-predicate, 
we have a kind of equivalence to what we're doing for N-premodification. But the ULF notation is 
more informative concerning adverbs, because their `advmod` is ambiguous between adjective-modifying, 
VP-modifying and S-modifying. The their notation is slightly more informative than ULF for 
noun premodification -- they make distinctions like premodifying (ordinary) adjective vs. premodifying 
participle.


## Sentence Modification

A formula or nonatomic verbal predicate in ULF may contain sentential modifiers
of type \\(({{ sit }} {{ rar }} {{ tru }}) {{ rar }} ({{ sit }} {{ rar }} {{ tru }})\\):
divided corresponding to their EL semantic differences into sorts `.adv-s`,
`.adv-e`, and `.adv-f`. Again there are type-shifting operators that create
these sorts of modifiers from monadic predicates. Sentential modifiers of the
sort `.adv-s` are usually modal (and thus opaque), e.g., 

  `perhaps.adv-s`, `(adv-s (without.p (a.d doubt.n)))`;

however, negation is transparent in the usual sense -- the truth value of a
negated sentence depends only of the truth value of the unnegated sentence.

Modifiers of sort `.adv-e` are transparent, typically implying temporal or
locative constraints, e.g.,
  
  `today.adv-e`, `(adv-e (during.p (the.d drought.n)))`, `(adv-e (in.p |Rome|))`;

these constraints are ultimately cashed out as predications about episodes
characterized by the sentence being modified. (This is also true for the `past`
and `pres` tense operators.)  


Similarly any modifier of sort `.adv-f` is transparent and implies the
existence of a multi-episode (characterized by the sentence as a whole) whose
temporally disjoint parts each have the same characterization
{% cite hwang1994ICTL %}; e.g.,

  `regularly.adv-f`, `(adv-f ({at}.p (three.d (plur time.n))))`.

The relative scoping of these operators are left ambiguous at the ULF stage,
just as with quantifiers and tense.  {% cite kim2017SemBEaR %} introduced this
approach to sentence modification annotation and provides further details and
examples.  They also discuss methods to handle tense and aspect annotation,
which are closely related to sentence modification.  We adopt their approach in
our work.



## Flat Bracketing & Localized Modification

In describing predicate and sentence modification, we've loosely described the
relaxations for operator positioning.  Here we discuss the subtleties in operator
positioning, motivate the relaxations, and specify the exact constraints.

We refine and generalize the operator-lifting technique of sentence-level
operators described by {% cite kim2017SemBEaR %} to verb phrases in order to
eliminate word reordering when annotating sentences like _"Mary undoubtedly
spoke up"_.  To summarize the approach from {% cite kim2017SemBEaR %},
sentence-level operators (e.g. `.adv-e`, `.adv-s`, etc.) located in the middle
of the sentence, e.g. `(|Mary| (undoubtedly.adv-s (past speak_up.v)))`,
can be automatically lifted to sentence-level since the semantic type makes
its necessary position clear.  The example just given would lift `undoubtedly.adv-s`
to sentence level resulting in the formula
`(undoubtedly.adv-s (|Mary| (past speak_up.v)))`. (The same would be done for `past`
when fully processing the sentence).

There are a few refinements need to be made for the approach described by
{% cite kim2017SemBEaR %}.  

1. We need to add restrictions of lifting the operators to the nearest distinct
   predications such as within embedded sentences and type-shifters.
2. We need to introduce a mechanism for sentence-level operators scoped over
   non-sentence contexts.
3. A similar lifting operation is necessary for verb modifiers that can occur
   in constituent, rather than premodifying position.

I'll discuss these in order.
 
### Refinement 1: Restrictions of lifting the operators to the nearest distinct predication

Notice that in the following sentences  

  (1) _I know that he didn't go home_, <br/>
  (2) _I saw the boy that didn't take the ice cream_, and <br/>
  (3) _I like to not stay up late_ 

the negations are all restricted to their respective clauses and shouldn't be
lifted to modify the top-level sentence. That is, (1) is equivalent to saying
_I know that it is not the case that he went home_. If we were to lift the
negation all the way to the top we get a meaning that we definitely don't want:
\*_It is not the case that I know that he went home_. (1) and (2) are cases
where the negation is restricted to an embedded sentence. (3) however restricts
it to a verb phrase. This seems to happen due to the reification of the verb
phrase via the `ka` operator. Notice this holds for _I like to bake cakes
regularly_. The liking is happening regularly, it's the baking that is regular.
Therefore, during the lifting phase, the lifting will only happen to the
nearest sentence or type-shifter. Here we list the raw ULF interpretations for
each of the sentences just discussed and the transformed versions after
lifting.  You may notice that there is still some discrepancy in the annotation
of sentence-level operators against {% cite kim2017SemBEaR %}. This will be
cleared up in the discussion of the other refinedments.

(1) _I know that he didn't go home_ <br>
raw ULF
```
(i.pro ((pres know.v) 
        (that (he.pro ((past do.aux-s) not 
                       (go.v (adv-a ({to}.p (k home.n)))))))))
```
post-lifted ULF
```
(i.pro ((pres know.v) 
        (that (not (he.pro ((past do.aux-s) 
                            (go.v (adv-a ({to}.p (k home.n))))))))))
```


(2) _I saw the boy that didn't take the ice cream_ <br>
raw ULF
```
(i.pro ((past see.v) 
        (the.d (n+preds boy.n 
                        (that.rel ((past do.aux-s) not 
                                   (take.v (the.d (ice.n cream.n)))))))))
```
post-lifted ULF
```
(i.pro ((past see.v) 
        (the.d (n+preds boy.n 
                        (not (that.rel ((past do.aux-s) 
                                        (take.v (the.d (ice.n cream.n))))))))))
```

(3) _I like to not stay up late_ <br>
raw ULF
```
(i.pro ((pres like.v) (to (not (stay_up.v late.adv-e)))))
```
post-lifted ULF
```
(i.pro ((pres like.v) (to (not (late.adv-e stay_up.v)))))
```


(4) _I like to bake cakes regularly_ <br>
raw ULF
```
(i.pro ((pres like.v) (to (bake.v (k (plur cake.n)) regularly.adv-f))))
```
post-lifted ULF
```
(i.pro ((pres like.v) (to (regularly.adv-f (bake.v (k (plur cake.n)))))))
```

The type compositions don't work out for the kind-of-action restriction of the
sentence-level operator, as in `(to (regularly.adv-f (bake.v (k (plur
cake.n)))))` since `regularly.adv-f` is a sentence modifier 
(\\(({{ sit }} {{ rar }} {{ tru }}) {{ rar }} ({{ sit }} {{ rar }} {{ tru }})\\))
whereas `(bake.v (k (plur cake.n)))` is a monadic verbal predicate
(\\({{ prd }}\_{V}\\) or 
 \\(({{ dom }} {{ rar }} {{ sit }} {{ rar }} {{ tru }})\_{V}\\)).
How this is handled will be clarified when we discuss the next refinement. We
need to generate an appropriate lambda expression to capture this.

The sentence-level operator will be restricted by the following contexts:

1. Reification operators (e.g. examples (3) and (4))
2. The predicate-argument boundary (e.g. _not_ in _The railing helps me not fall over_ evaluates over _fall over_, not the whole verb phrase)
3. Type shifters (e.g. _surprisingly_ in _The surprisingly happy man walked in_ evaluates over the scope of _happy_, not the main verb)

What all this reduces to is that a sentence-level operator lifts up the most
restrictive complete predication to act over. Reification results in a completely
separate predication between the predication in the reification context and the 
predication resulting from the main verb of the sentence. Similarly, when a
predicate is an argument of the main verb, the main verb causes some modification to
or comments on the predication resulting from its argument, but the main verb overall
makes a separate predication. Consider the example above, _The railing helps me
not fall over_. _help_ operates over _me_ and _not fall over_, in that the
subject of _help_ assists _me_ to realize the predicate _not fall over_, but
the actual predication of _help_ (described by the complete sentence) is
distinct from the predication resulting from the argument: _me not falling
over_. In a sense 1) is a special case of 2). We know that once we reify something,
the predicate within can't be forming the main verb, so the reified result must
be used as an argument somewhere.


### Refinement 2: Mechanism for sentence-level operators scoped over non-sentence contexts

The lifting restrictions from refinement 1 leads to the problem that sentence
level operators now scope over non-sentence objects, e.g. `(ka (not
fall_over.v))`. This is problematic to the idea of composition through
semantic types which ULF holds at its core. We assume an implicit expansion to 
the necessary type with additional unspecified constituents. Within ULF these 
constituents are fully unspecified, but would be fully resolved upon deindexing 
the specific predication. Then an implicit lambda expression wraps around the 
sentence-level operator with these unspecified arguments as the variables. This
preserves the type of the predicate. For example, `(ka (not (fall_over.v)))` has
the implicit lambda expression `(ka (lambda x (not (x fall_over.v))))`. Below
are a few examples of this.

(3) _I like to not stay up late_ <br>
post-lifted ULF
```
(i.pro ((pres like.v) (to (not (late.adv-e stay_up.v)))))
```
showing implicit lambdas
```
(i.pro ((pres like.v) (to (lambda x (not (late.adv-e (x stay_up.v)))))))
```

(4) _I like to bake cakes regularly_ <br>
post-lifted ULF
```
(i.pro ((pres like.v) (to (regularly.adv-f (bake.v (k (plur cake.n)))))))
```
showing implicit lambda
```
(i.pro ((pres like.v) 
        (to (lambda x (regularly.adv-f (x (bake.v (k (plur cake.n)))))))))
```

(5) _The railing helps me not fall over_ <br>
post-lifted ULF
```
((the.d railing.n) ((pres help.v) me.pro (not fall_over.v)))
```
showing implicit lambdas
```
((the.d railing.n) ((pres help.v) me.pro (lambda x (not (x fall_over.v)))))
```

(6) _The surprisingly happy man walked in_ <br>
post-lifted ULF
```
((the.d ((surprisingly.adv-s happy.a) man.n)) ((past walk.v) in.adv-a))
```
showing implicit lambdas
```
((the.d ((lambda x (surprisingly.adv-s (x happy.a))) 
         man.n)) 
 ((past walk.v) in.adv-a))
```

### Refinement 3: Lifting functionality for verb modifiers

Although at first we expected to be able to handle verb modifier placement by
simply allowing arbitrary order, this isn't sufficient for ditransitive verbs
since the modifier can be interleaved between the arguments, e.g. _Sally gave a
book quickly to John_. Therefore, what we've settled on is that all
non-subject arguments and modifiers of a verb are supplied as constituents at
the same level. The modifiers can then be lifted to the expected prefix
position in post-processing and arguments are supplied to the verb in the
provided order. Consider the annotation of the following sentence.

(7)_Alice delivered the artifact carefully to the curator today_
```
(|Alice| ((past deliver.v) (the.d artifact.n)
                           carefully.adv-a
                           (to.p-arg (the.d curator.n))
                           today.adv-e))
```

Notice that we can combine the relaxed context of verbal and sentence
modifiers. This flat form of supplying arguments and modifiers allows us to
mostly preserve word order and simplify the bracketing structures. After
lifting the modifiers, _carefully.adv-a_ and _today.adv-e_, we get

```
(today.adv-e (|Alice| (carefully.adv-a 
                       ((past deliver.v) (the.d artifact.n)
                                         (to.p-arg (the.d curator.n))))))                 
```

Here is the same thing for the other example given above

(8) _Sally gave a book quickly to John_
```
(|Sally| ((past give.v) (a.d book.n)
                        quickly.adv-a
                        (to.p-arg |John|)))
```
After lifting
```
(|Sally| (quickly.adv-a ((past give.v) (a.d book.n) 
                                       (to.p-arg |John|))))
```

Just as with sentence-level operators, these verb modifiers can also be
supplied in a manner that doesn't require lifting. That is, scoped over the
whole verb phrase. For example, 

(9) _Jenn quickly wrote the report_
```
(|Jenn| (quickly.adv-a ((past write.v) (the.d report.n))))
```

(10) _Jim declined the request politely_
```
(|Jim| (((past decline.v) (the.d request.n)) politely.adv-a))
```

For the motivating examples (7) and (8), this would require changing the word
order. Since the verb modifiers are interleaved with the direct objects and
indirect objects, they cannot scope around the full verb phrase in the given
positions. For reference, the flattened versions of those ULFs would be

(9') `(|Jenn| (quickly.adv-a (past write.v) (the.d report.n)))`

(10') `(|Jim| ((past decline.v) (the.d request.n) politely.adv-a))`

Note that the order of constituents in these flattened phrases are important.
Although the modifiers are lifted out of the given position and moved to the
verb phrase, the first verb when scanned left to right is considered the acting
verb and the following arguments are interpreted in the English word order.
So for example, `(quickly.adv-a (the.d report.n) (past write.v))` is not valid
since after lifting we get `(quickly.adv-a ((the.d report.n) (past write.v)))`
which looks like we're trying to apply a verb modifier to a sentence. (Left
supplied verb arguments are assumed to be the subject).

## Summary

- Intensional predicate modification is done through functions from monadic predicates to monadic predicates,
\\({{ prd }} {{ rar }} {{ prd }}\\), which have suffix types `.mod-a`, `.mod-n`, and `.adv-a` for adjective,
noun, and VP modification, respectively.
- Predicate modifiers can be formed via type-shifters from monadic predicates (`mod-a`, `mod-n`, `adv-a`) or 
individuals (`nnp`).
- `mod-a` and `mod-n` type-shifters can be omitted if their first argument is not a verb and the resulting
modifier is premodifying the other noun (e.g. `(happy.a dog.n)` omits `mod-n`, but `((mod-n (carefully.adv-a (pasv write.v))) notice.n)`
cannot omit the `mod-n`).
- When the types are explicit in ULF, the operator position can be either prefixed or infixed.
- Intersective modification such as noun post-modification is handled through macros that map to equivalent lambda expressions.
- Sentence-level operators are lifted to the nearest predication.
- Verb modifiers can be interleaved with non-subject arguments and automatically lift to prefix position.

