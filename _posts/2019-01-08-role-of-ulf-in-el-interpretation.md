---
layout: post
title: Role of ULF in Comprehensive Semantic Interpretation
author:
- gene
- len
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
<p>
ULFs are underspecified -- loosely structured and ambiguous -- in 
several ways. But their surface-like form, and the type structure they
encode, make them well-suited to reducing underspecification, both 
using well-established linguistic principles and machine learning (ML)
techniques that exploit the distributional properties of language.
Many examples of how ULFs lead systematically to (alternative)
disambiguated representations can be found in the references cited
at the beginning.  The scope of this proposal is not expected to 
encompass much of this further processing, but we want to reiterate 
some reasons for regarding ULFs as a suitable basis.
<p>
We have developed and applied heuristic algorithms that resolve scope 
ambiguities and make event structure explicit. Though these algorithms 
are not sufficiently reliable, they set a baseline for future work 
on disambiguation aided by ML techniques. The following points address
the utility of ULFs as preliminary structures enabling systematic
reduction of underspecification. 
<p>
<b> Word sense disambiguation (WSD):</b> One obvious form of 
underspecification is word sense ambiguity. But while, 
for example, <tt>(weak.a (plur creature.n))</tt> in (4) does 
not specify which of the dozen WordNet senses of <i>weak</i> or 
three senses of <i>creature</i> is intended here, the type structure
is perfectly clear: A predicate modifier is being applied to a nominal
predicate. Certainly standard statistical WSD techniques~\cite{jurafsky2009book} 
can be applied to ULFs, but this should
not in general be done for isolated sentences, since word senses
tend to be used consistently over longer passages. We should mention
here that adjectives appearing in predicative position (e.g., <i>able</i> 
in (2)) or in attributive position (e.g., <i>little</i> in (3)) are
type-distinct, but ULF leaves this distinction to further processing, 
since the semantic type of an adjective is unambiguous from the way 
it appears in ULF.
<p>
<b> Predicate adicity:</b> A slightly subtler issue is the adicity of 
predicates. We do not assume unique adicity of word-derived predicates 
such as <tt>run.v</tt>, since such predicates can have intransitive, simple 
transitive and other variants (e.g., <i>run quickly</i> vs. <i>run 
  an experiment</i>). But adicity of a predicate in ULF is always clear from 
the syntactic context in which it has been placed -- we know that it has 
all its arguments in place, forming a truth-valued formula, when an 
argument (the "subject") is placed on its left, as in English. 
<p>
<b> Scope ambiguity:</b> While some of the underspecification 
in ULFs is deterministically resolvable, <i>unscoped</i> 
constituents can generally "float" to more than one possible 
position. The three types of unscoped elements in ULF are 
<i>determiner phrases</i> derived from noun phrases (such as <i>very 
  few people</i> and <i>the Earth</i> in (6)), the tense operators <tt>pres</tt> 
and <tt>past</tt>, and the coordinators <tt>and.cc, or.cc</tt> and some 
variants of these.  The positions they can "float" to in postprocessing 
are always pre-sentential, and determiner phrases leave behind a variable
that is then bound at the sentential level. This view of scope
ambiguity was first developed in~\cite{schubert1982CL} and
subsequently elaborated in~\cite{hurum1986AI} and reiterated in
various publications by Hwang and Schubert. The accessible positions
are constrained by certain restrictions well-known in linguistics. For 
example, in the sentence <i>"Browder ... claims that every oligarch 
  in Russia was forced to give Putin 50 percent of his wealth"</i>, there 
is no wide-scope reading of <i>every</i>, to the effect <i>"For every 
  oligarch in Russia, Browder claims ... etc."</i>; the subordinate clause 
is a "scope island" for strong quantifiers like <i>every</i> (as well 
as for tense). The important point here is that ULF allows exploitation
of such structural constraints, since it still reflects the surface
syntax. Now, firm linguistic constraints still leave open multiple 
scoping possibilities, and many factors influence preferred choices, with
surface form (e.g., surface ordering) playing a prominent role~\cite{manshadi2013ACL}. So again the proximity of ULF to surface syntax 
should be helpful in applying ML techniques to determining preferred
scopings. <!-- % QUICK EXAMPLE OF SCOPING ALGORITHM OUTPUT? -->

<p>
<b> Anaphora:</b> Another important aspect of disambiguation is coreference
resolution. Again there are important linguistic constraints ("binding
constraints") in this task. For example, in <i>"John said that he was
  robbed", he</i> can refer to John; but this is not possible in <i>"He
  said that John was robbed"</i>, because in the latter, <i>he</i> C-commands
<i>John</i>, i.e., in the phrase structure of the sentence, it is a sibling
of an ancestor of <i>John</i>. ULF preserves this structure, allowing use
of such constraints. Preservation of structure also allows application
of ML techniques~\cite{poesio2016book}, but again this should be done
over passages, not individual sentences, since coreference "chains"
can span many sentences.
When coreference relations have been established as far as possible
and operators have been scoped, the resulting LFs are quite
close in form to first-order logic, except for incorporating the
additional expressive devices (generalized quantifiers, modification,
attitudes, etc.) that we have already mentioned and illustrated.
In our writings we call this the <i>indexical logical form</i>, or
ILF.

<p>
<b> Event/situation structure:</b> The most important aspect of logical form 
that remains implicit in ILF is event/situation structure. Much of our 
past work has been concerned with the principles of <i>de-indexing</i>, 
i.e., making events and situations -- <i>episodes</i> in our terminology -- 
explicit~\cite{hwang1992thesis,hwang1994ICTL,schubert2000book2}. The relationship 
to Davidsonian event semantics and Reichenbachian tense-aspect theory is 
explained in these references. Our compositional approach to tense-aspect 
processing leads to construction of a so-called <i>tense tree</i>, and yields 
multiple, related reference events for sentences such as <i>"By 8pm  tonight, 
  all the employees will have been working for 15 hours straight".</i>
The relevant point here is that the compositional constuction and use of
tense-trees is possible only if the logical form being processed reflects
the original clausal structure -- as ULF and ILF indeed do.

<!-- % Our approach to the semantics of tense, aspect, and temporal adverbials differs  -->
<!-- % from the traditional Davidsonian approach in that it associates episodes  -->
<!-- % not only with atomic predications, but also with negated, quantified,  -->
<!-- % and other complex sentences. For example, in ELF there is an explicit -->
<!-- % referent available for the phrase <i>this situation</i> in sentence -->
<!-- % pairs such as <i>"No rain fell for two months. <u>This situation</u> -->
<!-- % led to crop failures"</i>, or <i>"Every theater patron was trying to -->
<!-- % exit through the same door. <u>This situation</u> led to disaster".</i> -->
<!-- % In addition, we regard perfect and progressive aspect, via operators -->
<!-- % <tt>perf} and <tt>prog}, together with the tense operators <tt>pres</tt> -->
<!-- % and <tt>past} and modal auxiliary <tt>will.aux-s</tt>, as contributing  -->
<!-- % to temporal structure compositionally, rather than by enumeration of -->
<!-- % possible tense-aspect combinations. The compositional process is mediated -->
<!-- % by <i>tense trees</i> systematically determined by ILF structure. The -->
<!-- % process deposits, and makes reference to, episode tokens at tense tree -->
<!-- % nodes, relating the various times/episodes referred to in sentences -->
<!-- % such as <i>By 8pm tonight, all the employees will have been working -->
  <!-- % for 15 hours straight".</i> Details are provided in the publications above, -->
<!-- % especially (Hwang \& Schubert 1994).  -->

<p>
<b> Canonicalization:</b> Finally, canonicalization of ELF into "minimal" 
propositions, with top-level Skolemization (and occasionally 
$\lambda$-conversions), is straightforward. A simple example was seen 
in the Introduction, and some more complex examples are 
shown in prior publications~\cite{schubert2000book,schubert2014SP,schubert2015AAAI}. 

<p>
When episodes have been made explicit (and optionally, canonicalized), 
the result is <i>episodic logical form</i> (ELF); i.e., we have sentences 
of Episodic Logic, as described in our previously cited publications. 
These can be employed in our {\sc Epilog} inference engine for reasoning 
that combines linguistic semantic content with world knowledge. 
A variety of complex {\sc Epilog} inferences are reported in~\cite{schubert2013LiLT}, 
and \cite{morbini2011chapter} contained examples of self-aware metareasoning. 
Further in the past, {\sc Epilog} reasoned about snippets from the Little Red 
Riding Hood story: <i>If the wolf tries to eat LRRH when there are 
woodcutters nearby, what is likely to happen?</i>"; answer chain: <i>
The wolf would attack and try to subdue LRRH; this would be noisy; 
the woodcutters would notice, and see that a child is being attacked; 
that is a wicked act, and they would rush to help her, and punish or 
kill the wolf</i>~\cite{hwang1992thesis,schubert2000book}. However, the 
scale of such world-knowledge-dependent reasoning has been limited
by the difficulty of acquiring large amounts of inference-enabling 
knowledge. (The largest experiments, showing the competitiveness
of {\sc Epilog} against state-of-the art theorem provers were limited
to formulas of first-order logic~\cite{morbini2009LFCR}.) In the
proposed work we therefore focus on inferences that are important but
not heavily dependent on world knowledge.

<!-- % The potential of EL reasoning has been extensively demonstrated, making  -->
<!-- % the prospect of effectively mapping language to EL an attractive one.  -->
<!-- % The most complete [language $\rightarrow$ reasoning] system built so  -->
<!-- % far (2012-14) was a system for interpreting captions of family photos  -->
<!-- % (e.g., <i>Alice, with her two grandmothers at her graduation party</i>),  -->
<!-- % then aligning the caption-derived knowledge with image-derived data -->
<!-- % about individuals' apparent age, gend, hair color, eye-wear, etc.,  -->
<!-- % merging the knowledge, and then inferentially answering questions -->
<!-- % (<i>Who graduated?</i>). Unpublished reports (to ONR) on this work -->
<!-- % exist, but further development has been hampered by difficulties in -->
<!-- % obtaining large collections of captioned family photos for scaling up. -->

<p>
Thus ULFs comprise a "primal" logical form whose resemblance to phrase
structure and whose constraints on semantic types provide a basis for
the multi-faceted requirements of deriving less ambiguous, nonindexical,
canonical LFs suitable for reasoning. However, as we have pointed out,
ULFs are themselves inference-enabling, and this will be important for
our evaluation plan.
