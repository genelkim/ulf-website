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

## Predicate Modification

EL semantic types represent predicate modifiers as functions from _monadic_
predicates to _monadic_ predicates, i.e. (\\(({{ dom }} \rightarrow {{ tru }})
\rightarrow ({{ dom }} \rightarrow {{ tru }})\\)).  This enables handling of
non-intersective modifiers, e.g._nearly_, _fake_, _almost_.  These are further
distinguished between temporal and atemporal predicates, since those are
distinct semantic types.

- _atemporal_: `(fake.attr diamond.n)`
- _temporal_: `(nearly.adv-a fall.v)`

`.attr` reflects the linguistic category of attributive adjectives and `.adv-a`
reflects that the modifier comes from an adverb, further specifying  that this
is an action or attribute modifier, as distinct from an event modifier,
frequency modifier, or sentential (propositional) modifier. For example,
"He thought *deeply*{:.ul}" refers to an action whose agent evinced
depth of thought, rather than to a deep event. Actions, experiences, and
attributes  in EL are agent-episode pairs, and modifiers of type-`.adv-a`
applied to verbal  predicates express a constraint on both the agent (more
generally, subject) of  a sentence and the episode it characterizes. Actions
are not explicitly represented  in ULF but rather are derived during deindexing
when event variables are introduced.  A modifier of type-`.adv-a`  applied to
an adjectival predicate, as in  "*deeply*{:.ul} flawed", simply
modifies a property of individuals,  rather than of agent-episode pairs.

The modifier forming operators in ULF with example annotations and formal
types.  \\( \mathcal{N}\_{t} \\) is the type of a temporal (monadic) predicate and
\\(\mathcal{N}\_{a}\\) is the type for an atemporal (monadic) predicate.  

| _Name_ | _Example_ | _Formal Type_ |
|-----------|-----------|---------------|
| `attr`  | `((attr (very.adv-a happy.a)) dog.n)`   | \\(\mathcal{N}\_{t} \rightarrow (\mathcal{N}\_{a} \rightarrow \mathcal{N}\_{a})\\) |
| `adv-a` | `(play.v (adv-a (with.p (a.d dog.n))))` | \\(\mathcal{N}\_{t} \rightarrow (\mathcal{N}\_{t} \rightarrow \mathcal{N}\_{t})\\) |
| `nn`    | `((nn pizza.n) box.n)`                  | \\(\mathcal{N}\_{a} \rightarrow (\mathcal{N}\_{a} \rightarrow \mathcal{N}\_{a})\\) |
| `nnp`   | `((nnp |Seattle|) skyline.n)`           | \\({{ dom }} \rightarrow (\mathcal{N}\_{a} \rightarrow \mathcal{N}\_{a})\\) |

These modifiers can also be derived from predicates, most commonly
prepositional phrases, thus ULF also has modifier-forming operators that
correspond to  each of the type extensions (`attr`, `adv-a`), as well as some
that don't  have lexical correspondents (`nn`, `nnp`).
Table \ref{table:pred-mod-formers} lists these operators, examples of their
usage, and their formal types.  The formal types are defined in terms of
\\(\mathcal{N}\_{t}\\) for temporal (monadic) predicates and \\(\mathcal{N}\_{a}\\) for
atemporal (monadic) predicates.\footnote{You may notice that while three of the
operators form atemporal modifiers, only one forms a temporal modifier.  Within
the type structure we could very well define temporal variants of `nn` and
`nnp`, but it turns out not to really appear in English.} 

<!--
%GENE: I changed some
temporal versus atemporal wording above to be about verbal versus %
adjectival predicates. I've tended to think of some adjectives as temporal
(e.g., %   angry, drunk) and others as atemporal (e.g., intelligent, plaid,
distant, flawed) --  %   more or less in line with Greg's stage- vs
individual-level predicates. Yet  %   '(very.adv-a angry.a)' seems to involve
just straightforward transformation of %   a predicate over individuals, not
pairs. %      But I'm wondering if perhaps you had it right, and even 'angry'
is atemporal, and just %   becomes temporal when you apply "be" to it ("is
angry"). I've wondered about this before %   in connection with sentences like
"Every drunk customer was expelled from the bar", %   where we want to regard
the restrictor predicate, "drunk customer" as no different %   in terms of
semantic type from an unmodified nominal ("Every customer was expelled  %
from the bar"); i.e., if "customer" is atemporal, then surely so is "underage,
drunk  %   customer"; o/w the semantics of quantification becomes exceedingly
tricky. I do talk %   about this in my "book", I think, opting for a Renate
Musan-like analysis in terms  %   of maximal temporal chunks of individuals
(sub-individuals, one might say) that have  %   the restrictor property over
the temporal span they occupy... %
-->

<!--
%TODO: introduce operators corresponding to `nn` and `nnp` for temporal
predicates: %      "dirt brown", "feather light", "razer sharp", "crystal
clear", "Atlanta hot", %      Actually, this seems to just be adjective
modification, not any atemporal predicate. %      I can't think of any examples
where the modified constituent is a verb... maybe %      "cheetah run",
"feather fall"? % %      This seems to indicate a distinction that isn't just
temporal-atemporal, %      but a noun-adj-verb distinction.  If that's the
case, why do we allow %      `adv-a` to take adjectives and verbs, and modify
adjectives and %      verbs?  Also how do prepositional phrases fit into this?
I generally %      think of prepositions as relational adjectives, but I can't
think of any noun %      premodification of prepositional phrases. % %      I
think we might have let the *.adv-a extension get a bit overused at this point.
%      It doesn't seem to have a coherent type.  We've allowed it to capture
all %      adjective/verb/preposition-adjective/verb/preposition modification.
I think we %      probably should be distinguishing between modifiers that
actually happen at action-level %      and those that are actually intensional
predicate modifiers.  So %        (he.pro ((past leave.v) politely.adv-a)) %
is fine, but %        (he.pro ((pres be.v) (very.adv-a happy.a))) %      seems
strange.  We definitely don't want this latter example to turn into: %
((he.pro ((pres be.v) happy.a)) ** e1), ([he.pro | e1] very.adv-a) %
Rather, we seems to want something like 'very.adv/a' (along the lines of %
your previous suggestion of a/n for adjective-noun modifiers), so we'd have %
(he.pro ((pres be.v) (very.adv/a happy.a))) %      Similarly we'd introduce
n/n, a/n, n/a, a/a, adv/a, n/v.  I would suggest including %      monadic
prepositional phrases into adjective categories because of examples like %
"I am very in the zone", "He is almost in the forest" % %      This would
explicitly separate action modification from predicate modification. %      For
action modification, we use `adv-a` which takes any predicate any can be %
used to modify the action -- often an adjective and can be rewritten as -ly.
This %      would capture all the manner adverbials as well as co-occurring
actions. % %      For predicate modification, we would be fully explicit about
the syntactic type %      combinations since the ULF combinations are in fact
the way the types are going %      to combine (no post-processed lifting to
actions).  So we need to make sure the %      types combine properly. %
a/n : light feather (also attr) %        a/v : ? %        a/a : burning hot %
n/n : melting pot %        n/v : cheetah run? %        n/a : feather light
v/n : ? -- frequently returning member, sleeping beauty, running man, the never
running man %        v/v : ? -- adv-a for all these probably %        v/a : ? %
adv/n : ? %        adv/v : nearly run %        adv/a : very happy %      I'm
not sure why the categories organize in this way... From an engineering
perspective %      that doesn't matter so much, we just include this systematic
procedure for simplicity %      even though not every category is used.  From a
linguistic perspective, though I'm curious %      why the combinations exist
the way they do...

%TODO: write this section based on above notes for now and ask Len for feedback when he's back. %If he disagrees we might take it back to a previous version...
-->

Notice from the examples in Table~\ref{table:pred-mod-formers} that the
operators  aren't necessarily prefixed in ULFs, rather they appear in the
surface word order.  In EL, monadic operators are prefixed, whereas operators
with more arguments are infixed.  In ULF, we leave them in place since the
operator and operand can be inferred from the types of the constituents.
Consider the types for `play.v` and `(adv-a (with.p (the.d dog.n)))`.  Since
the former is an atemporal predicate and the latter is an atemporal predicate
modifier, we can be certain that `(adv-a (with.p (the.d dog.n)))` is the
operator while `play.v` is the operand.

In practice, we're able to drop many of these predicate modifier type-shifters
during annotation.  Since noun-noun and adjective-noun combinations don't have
valid composition in ULF~(they are all predicates over individuals), when we
come across such combinations we can automatically insert the appropriate
type-shifter to make the  composition valid.  We assume in these cases that the
prefixed predicate is the operator,  which reflects a common pattern in
English.  Thus, "burning hot melting pot" would be  hand annotated as

`((burning.a hot.a) (melting.n pot.n))`

which would be post-processed to

`((attr ((adv-a burning.a) hot.a)) ((nn melting.n) pot.n))`

While the prefixed predicate modification allows us to formally model
non-intersective modification, it does not necessarily indicate that the
modification is non-intersective. For example, we would annotate "triangular
container" as `((attr triangular.a) container.n)`, but since this relation is
intersective, given the correct background knowledge, we would infer that this
has the same meaning as `(lambda x ((x triangular.a) and.cc (x
container.n)))`. There are some constructions in English that really seem to
indicate an intersective interpretation via the grammar, for which we annotate
them as such. This includes post-nominal modification and  appositives.  We
would annotate "The buildings in the city" as

```
(The.d (n+preds (plur building.n)                        
                (in.p (the.d city.n))))
```

which is equivalent to

```
(The.d (lambda x ((x (plur building.n)) and.cc
                  (x (in.p (the.d city.n))))))
```

Thus we distinguish grammatical constructions that indicate intersective modification,  but ULFs do not distinguish all intersective vs. non-intersective modification.


## Sentence Modification

The EL type system also makes the distinction between intensional and
extensional modification for sentence modifiers.  This is in terms of whether
the modifiers predicate over the episodes (e.g. "in the forest", "after
dinner")  or map sentence intensions to sentence intensions (e.g. "probably",
"according to the report"). These are annotated using `adv-e` and `adv-s`
operators for extensional and intensional modification, respectively.  Both
have lexical and modifier forming variants just like `adv-a`.  Formally, both
these operators act  at sentence-level, but they often appear mid-sentence,
e.g. "John probably went home".   Since the `-e` and `-s` extensions make it
unambiguous that these are  sentence-level operators, these are annotated in
place in ULFs.

The relative scoping of these operators are left ambiguous at the ULF stage,
just as with quantifiers and tense.  {% cite kim2017SemBEaR %} introduced this
approach to sentence modification annotation and provides further details and
examples.  They also discuss methods to handle tense and aspect annotation,
which are closely related to sentence modification.  We adopt their approach in
our work.  The primary difference between the approach described by~{% cite
kim2017SemBEaR %} and our work is that they use different types of brackets to
distinguish types of compositions whereas we rely on the type system or named
operators, such as `n+preds`.

<!--
%ULF semantic types distinguish between predicate modification and sentence modification and between intensional and extensional modification. %{% cite kim2017SemBEaR %} describe methods of annotating perfect and progressive aspect, modal auxiliaries, and verb-level vs. sentence-level modifiers in the context of ULF.  We adopt %the same approach with a few changes... TODO: look over paper and write any changes to the guidelines.
-->

We consider negation to be an intensional sentence modifier and annotate it in
the same way as we would other `adv-s` operators.  Due to how common it is, we
allow it to be represented simply as `not`, without the type-extension, as  in
`(|Clifford| ((pres be.v) not green.a))`

## Flat Bracketing & Localized Modification

We generalize the flat bracketing technique of sentence-level operators
described by {% cite kim2017SemBEaR %} to verb phrases in order to eliminate
word reordering when annotating sentences like "Sally gave a book quickly to
John".  All non-subject arguments and modifiers of a verb are supplied as
constituents at the same level.  The modifiers can then be lifted to the
expected prefix position in post-processing and arguments are supplied to the
verb in the provided order.  Consider the example "Alice delivered the artifact
carefully to the curator today", which can be annotated as

<!--
% TODO: for some reason the formatting for this file is causing misalignment in the numCharTab and the first indented line...     \ulf{(|Alice| ((past deliver.v) (the.d artifact.n) carefully.adv-a\\     \numCharTab{30}(to.p-arg (the.d curator.n)) today.adv-e))}
-->

 With explicit modifier scoping and fully curried arguments we get

```
(today.adv-e (|Alice| (carefully.adv-a 
    (((past deliver.v) (the.d artifact.n)) (to.p-arg (the.d curator.n))))))
```

The flat version allows simpler bracketing structures while preserving word order.

TODO: localized modification -- the surprisingly happy man VP vs surprisingly the happy man VP

