---
title: ULF Intro 2 - Role of ULF in Comprehensive Semantic Interpretation
author:
  - gene
  - len
categories:
  - Introduction
  - Semantic Interpretation Process
date: 2019-01-08 02:00:00
---

<!-- %```````````````````````````````````````````````````````````````` -->
<!-- % Points:  -->
<!-- %   How ULFs encode possible meanings: -->
<!-- %  -  The set of unscoped elements corresponds to a fixed set of possibilities; -->
<!-- %  -  Deindexing of tense, temporal adverbials leads to a fixed set of -->
<!-- %     possible temporal relationships; (Hwang & Schubert 1994) -->
<!-- % -->
<!-- %   Linguistic phrase structure provides important clues to disambiguation -->
<!-- %   of scope, coreference, elided material, presupposed material, temporal -->
<!-- %   relations. By retaining the essential structure of the input, ULFs  -->
<!-- %   support use of these cues (whether by algorithmic or ML methods). -->
<!-- %   E.g.: The possible positions for unscoped pres/past/quantifiers/and/or -->
<!-- %         are unambiguously determined by their context of appearance in -->
<!-- %         ULF (see Schubert & Pelletier 1982). Further, structural properties -->
<!-- %         bias choices of these scopes (order of appearance, modal embedding, -->
<!-- %         relative wide-scoping tendencies) -\- e.g., Hurum; Hafezi-Manshadi -->
<!-- %   E.g.: Intrasentential anaphora resolution is known to be constrained by  -->
<!-- %         C-command relations and reflexive binding constraints; ULF preserves  -->
<!-- %         the relevant information; -->
<!-- %   E.g., E.g., Ellipsis resolution depends on structural context: "She has  -->
<!-- %         as many books as I". -->
<!-- % -->
<!-- %   Subsequent scoping and deindexing, followed by canonicalization (Skolemization, -->
<!-- %   conjunction splitting, etc.) typically leads to sets of predications not -->
<!-- %   unlike those often posited in approaches that seek to derive canonical -->
<!-- %   LFs directly from surface strings. Perhaps human language understanding also -->
<!-- %   leads to canonical "Mentalese" forms, and perhaps the appeal of semantic -->
<!-- %   representations in terms of "triples" derives from this. But we contend -->
<!-- %   that starting with a surface-oriented representations and working towards -->
<!-- %   a canonical, factored representation offers compelling advantages. -->
<!-- % -->
<!-- % Another point: Retaining some ambiguity in sentence LFs is desirable, even -->
<!-- %   necessary, because complete disambiguation often requires a broader context.  -->
<!-- %   E.g., Resolving indexicality and deixis (I, you, this, here, now, ...) -->
<!-- %         is clearly context dependent; also, -->
<!-- %         whether a pronoun corefers inter- or intrasententially depends -->
<!-- %         on prior sentences. E.g., "The boy thought he was going to die" -->
<!-- %         may well mean the boy thought this about himself, but not if the  -->
<!-- %         preceding sentence is "Billy's dad was badly wounded". -->
<!-- %   E.g., Word senses depend on broader context. For example "car" can -->
<!-- %         mean automobile throughout one lengthy passage, and railroad car -->
<!-- %         in another (or even "first element" in Lisp documentation). -->
<!-- %   E.g., Some utterances are radically ambiguous without prior context, -->
<!-- %         such as "How about you?", with prior statements "I'm a sophomore", -->
<!-- %         or "I like seafood". -->

ULFs are underspecified -- loosely structured and ambiguous -- in 
several ways. But their surface-like form, and the type structure they
encode, make them well-suited to reducing underspecification, both 
using well-established linguistic principles and machine learning
techniques that exploit the distributional properties of language.
The image below shows a diagram of the interpretation process from
an English sentence to full-fledged Episodic Logic and highlights
where ULF fits into it. The structural dependencies in the diagram
are shown with solid black arrows and information flow is shown with
dashed blue arrows. The backwards arrows exist because the optimal
choice at a particular step depends on the overall coherence of the
final formula and such coherence information can be used to make
decisions in structurally preceding steps. Word sense disambiguation
and anaphoric resolution don't interact with the general structure
of the formula so they can be incorporated at any point in the process.
The yellow highlighting shows the components of the formula that changed
from the previous structurally dependent step in the process.

![ULF in the EL interpretation process]({{ site.baseurl }}/assets/img/ulf_interpretation_process_xbig_cropped.png)

Let's walk through this diagram.  We start of with the sentence

_She wants to eat the cake_

which is interpreted into the following ULf

`(she.pro ((pres want.v) (to (eat.v (the.d cake.n)))))`

After tense and determiner scoping (lifting up `pres` and `the.d`) it becomes

`(pres (the.d (x cake.n) (she.pro (want.v (to (eat.v x))))))`

This is then deindexed, Skolemized, and canonicalized (if you don't understand
these terms, read the subsections below) to

`(|E|.sk at-about.p |Now17|)`, <br>
`((the.d x (x cake.n) (she.pro (want.v (to (eat.v (the.d cake.n)))))) ** |E|.sk)`

`|E|.sk` is a Skolemized episode variable, which is characterized by the sentence
via the `**` operator. Once we've resolved who _she_ is and what _the cake_ is, 
we can appropriately substitute for them. Say this is the third cake introduced
to the domain of discourse and we know that _she_ is referring to "Chell".  Then 
we resolve those conclusions to get

`(|E|.sk at-about.p |Now17|)`, <br>
`((|Chell| (want.v (to (eat.v |Cake3|)))) ** |E|.sk)`

We can wrap up by performing word sense disambiguation on all the predicates to get

`(|E|.sk at-about.p |Now17|)`, <br>
`((|Chell| (want1.v (to (eat1.v |Cake3|)))) ** |E|.sk)`

We have developed and applied heuristic algorithms that resolve scope 
ambiguities and make event structure explicit. Though these algorithms 
are not sufficiently reliable, they set a baseline for future work. 
We now discuss each of these resolutions steps in more detail and how
ULF supports these later resolutions steps.

## Word sense disambiguation (WSD)

__Is "bass" a fish or instrument?__

(1) _I went fishing for some sea bass_

(2) _The bass line is too weak_

One obvious form of underspecification is word sense ambiguity. But while, for
example, `(weak.a (plur creature.n))` does not specify which of the dozen
WordNet senses of _weak_ or three senses of _creature_ is intended here, the
type structure is perfectly clear: A predicate modifier is being applied to a
nominal predicate. Certainly standard statistical WSD techniques {% cite
jurafsky2009book %} can be applied to ULFs, but this should not in general be
done for isolated sentences, since word senses tend to be used consistently
over longer passages. It should be noted that adjectives appearing in
predicative position (e.g., _able_ in _able to succeed_ -- `(be.v (able.a (to
succeed.v))`) or in attributive position (e.g., _little_ in _three little
bushes_ -- `(three.d (little.a (plur bush.n))`) are type-distinct in EL, but
ULF leaves this distinction to further processing, since the semantic type of
an adjective is unambiguous from the way it appears in ULF.

## Predicate adicity

__How many arguments does a predicate take?__

A slightly subtler issue is the adicity of predicates. We do not assume unique
adicity of word-derived predicates such as `run.v`, since such predicates can
have intransitive, simple transitive and other variants (e.g., _run quickly_
vs. _run an experiment_). But adicity of a predicate in ULF is always clear
from the syntactic context in which it has been placed -- we know that it has
all its arguments in place, forming a truth-valued formula, when an argument
(the "subject") is placed on its left, as in English. It is for this reason
that arguments that are implicit in the surface sentence are introduced in 
ULFs, such as in example 1 from ULF Intro 1,

_Could you dial for me?_
```
(((pres could.aux-v) you.pro (dial.v {ref1}.pro
                                     (adv-a (for.p me.pro)))) ?)
```

In this example, `{ref1}.pro` is not in the surface sentence, but a known
necessary argument of _dial_ for this sentence to make sense.

## Scope ambiguity

_Every dog sees a bone_

__Does every dog see the same bone?__

The sentence above has two possible relative scopings of the two determiners,
_every_ and _a_, which give distinct readings of the sentence.  Either,
there can be _a bone_ with respect to each of _every dog_ as in the following

`(every.d x: (x dog.n) (a.d y: (y bone.n) (x ((pres see.v) y))))`

or there could be _a bone_ that is seen by _every dog_ which would be resolved
as below.

`(a.d y: (y bone.n) (every.d x: (x dog.n) (x ((pres see.v) y))))`

This sort of ambiguity can arise from the three types of unscoped elements in
ULF, which are _determiner phrases_ derived from noun phrases (such as _very
few people_ and _the Earth_ -- `((nquan (very.mod-a few.a)) (plur person.n)`
and `(the.d |Earth|.n)`, respectively), the tense operators `pres` and `past`,
and the coordinators `and.cc`, `or.cc` and some variants of these.  The
positions they can "float" to in postprocessing are always pre-sentential, and
determiner phrases leave behind a variable (e.g. `x` and `y` in the motivating
example about the dog and the bone above) that is then bound at the sentential
level. This view of scope ambiguity was first developed in {% cite
schubert1982CL %} and subsequently elaborated in {% cite hurum1986AI %} and
reiterated in various publications by Hwang and Schubert. 

The accessible positions are constrained by certain restrictions well-known in
linguistics.  For example, in the sentence 

_"Browder ... claims that every oligarch in Russia was forced to give Putin half of his wealth"_, 

there is no wide-scope reading of _every_, to the effect _"For every oligarch in
Russia, Browder claims ... etc."_; the subordinate clause is a "scope island"
for strong quantifiers like _every_ (as well as for tense). The ULF allows
exploitation of such structural constraints, since it still reflects the
surface syntax. Firm linguistic constraints still leave open multiple scoping
possibilities, and many factors influence preferred choices, with surface
form (e.g., surface ordering) playing a prominent role {% cite
manshadi2013ACL %}. So again the proximity of ULF to surface syntax will be
helpful in applying ML techniques to determining preferred scopings. 

<!-- %QUICK EXAMPLE OF SCOPING ALGORITHM OUTPUT? -->


## Anaphora

_John saw Bob and told him he had to go home_

__Who are "him" and "he"?__

Another important aspect of disambiguation is coreference
resolution. Again there are important linguistic constraints ("binding
constraints") in this task. For example, in _"John said that he was
  robbed", he_ can refer to John; but this is not possible in _"He
  said that John was robbed"_, because in the latter, _he_ C-commands
_John_, i.e., in the phrase structure of the sentence, it is a sibling
of an ancestor of _John_. ULF preserves this structure, allowing use
of such constraints. In the ULF for these sentences,

`(|John| ((past say.v) (that (he.pro (past (pasv rob.v))))))`

`(he.pro ((past say.v) (that (|John| (past (pasv rob.v))))))`

we see that in the former formula, `|John|` is the sibling of the verb
phrase `((past say.v) (that (he.pro (past (pasv rob.v)))))`, which
indeed is an ancestor of `he.pro`. Similarly, in the latter formula,
we get the opposite since `he.pro` and `|John|` are in opposite positions.

Preservation of structure also allows application of ML techniques {% cite
poesio2016book %}, but again this should be done over passages, not individual
sentences, since coreference "chains" can span many sentences. When
coreference relations have been established as far as possible and operators
have been scoped, the resulting LFs are quite close in form to first-order
logic, except for incorporating the additional expressive devices (generalized
quantifiers, modification, attitudes, etc.) that we have already mentioned and
illustrated. In our writings we call this the _indexical logical form_, or
ILF. ILF doesn't appear in the intepretation process diagram due to the
particular decomposition of steps we show in the diagram. The anaphora
resolution is shown as a structurally independent step from the core structural
changes. However, it is required for the final EL interpretation.

## Event/situation structure

__What are the events in the sentence and how do they relate?__

The critical aspect of episodic logical form is event/situation structure. Much
of the past work in EL has been concerned with the principles of _de-indexing_,
i.e., making events and situations -- _episodes_ in our terminology -- explicit
{% cite hwang1992thesis hwang1994ICTL schubert2000book2 %}. The relationship to
Davidsonian event semantics and Reichenbachian tense-aspect theory is explained
in these references. Their compositional approach to tense-aspect processing
leads to construction of a so-called _tense tree_, and yields multiple, related
reference events for sentences such as _"By 8pm  tonight, all the employees
will have been working for 15 hours straight"._ The compositional constuction
and use of tense-trees is possible only if the logical form being processed
reflects the original clausal structure -- as ULF indeed does. This step is
merged with the following, canonicalization step in the diagram above.

The EL approach to the semantics of tense, aspect, and temporal adverbials differs
from the traditional Davidsonian approach in that it associates episodes not
only with atomic predications, but also with negated, quantified, and other
complex sentences. For example, in ELF there is an explicit referent available
for the phrase _this situation_ in sentence pairs such as _"No rain fell for
two months. *This situation* led to crop failures"_, or _"Every theater
patron was trying to exit through the same door. *This situation* led to
disaster"._ In addition, we regard perfect and progressive aspect, via
operators `perf` and `prog`, together with the tense operators `pres` and
`past` and modal auxiliary `will.aux-s`, as contributing to temporal
structure compositionally, rather than by enumeration of possible
tense-aspect combinations. The compositional process is mediated by _tense
trees_ systematically determined by ULF structure. The process deposits, and
makes reference to, episode tokens at tense tree nodes, relating the various
times/episodes referred to in sentences such as _By 8pm tonight, all the
employees will have been working for 15 hours straight"._ Details are
provided in the publications above, especially {% cite hwang1994ICTL %}. 

## Canonicalization

Finally, canonicalization of ELF into "minimal" propositions, with top-level
Skolemization (and occasionally \\(\lambda\\)-conversions), is straightforward.
Some complex examples are shown in prior publications {% cite schubert2000book
schubert2014SP schubert2015AAAI %}. 

When episodes have been made explicit (and optionally, canonicalized), the
result is _episodic logical form_ (ELF); i.e., we have sentences of Episodic
Logic, as described in our previously cited publications.  These can be
employed in our *Epilog*{:.sc} inference engine for reasoning that combines
linguistic semantic content with world knowledge.  A variety of complex
*Epilog*{:.sc} inferences are reported in {% cite schubert2013LiLT %}, and {%
cite morbini2011chapter %} contained examples of self-aware metareasoning.
Further in the past, *Epilog*{:.sc} reasoned about snippets from the Little Red
Riding Hood story: _If the wolf tries to eat LRRH when there are woodcutters
nearby, what is likely to happen?_"; answer chain: _The wolf would attack and
try to subdue LRRH; this would be noisy; the woodcutters would notice, and see
that a child is being attacked; that is a wicked act, and they would rush to
help her, and punish or kill the wolf_ {% cite hwang1992thesis schubert2000book
%}. However, the scale of such world-knowledge-dependent reasoning has been
limited by the difficulty of acquiring large amounts of inference-enabling
knowledge. (The largest experiments, showing the competitiveness of
*Epilog*{:.sc} against state-of-the art theorem provers were limited to
formulas of first-order logic {% cite morbini2009LFCR %}.) In the proposed work
we therefore focus on inferences that are important but not heavily dependent
on world knowledge.

The potential of EL reasoning has been extensively demonstrated, making 
the prospect of effectively mapping language to EL an attractive one. 
The most complete [language \\(\rightarrow\\) reasoning] system built so 
far (2012-14) was a system for interpreting captions of family photos 
(e.g., _Alice, with her two grandmothers at her graduation party_), 
then aligning the caption-derived knowledge with image-derived data 
about individuals' apparent age, gender, hair color, eye-wear, etc., 
merging the knowledge, and then inferentially answering questions 
(_Who graduated?_). Unpublished reports (to ONR) on this work 
exist, but further development has been hampered by difficulties in 
obtaining large collections of captioned family photos for scaling up. 

Thus ULFs comprise a "primal" logical form whose resemblance to phrase
structure and whose constraints on semantic types provide a basis for
the multi-faceted requirements of deriving less ambiguous, nonindexical,
canonical LFs suitable for reasoning. However, as we have pointed out,
ULFs are themselves inference-enabling, and this will be important for
our evaluation plan.

[Prev: ULF Intro 1]({{ site.baseurl }}/2019/01/07/ulf-intro-1-introduction-to-ulf-type-structure/)

[Next: ULF Intro 3]({{ site.baseurl }}/2019/01/07/ulf-intro-3-inference-with-ulfs/)

