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

<!-- %``````````````````````````````` -->

<!-- % I'M CONSIDERING KEEPING (SOME OF) THIS: -->
<!-- % As justified in detail in (Schubert 2000), ULF and EL sharply distinguish  -->
<!-- % propositions from events (more generally episodes). Propositions  -->
<!-- % are abstract, true or false <i>information</i> objects and as such can  -->
<!-- % be <i>asserted, known, believed, disputed, etc.</i>; whereas events are  -->
<!-- % surely real, temporal entities in the world, often with causal consequences  -->
<!-- % -/- without them, there would be no natural or social world as we know it.  -->
<!-- % Consider for example,\\[.03in] -->
<!-- % \ind <i>Molly barked last night; <u>that</u> woke up the neighbors.</i>\\ -->
<!-- % \ind <i>Molly barked last night; <u>that</u>'s what the neighbors assert.</i>\\[.03in] -->
<!-- % Note that propositions don't wake neighbors, but events certainly can; -->
<!-- % and events can't be asserted, but propositions certainly can. Events -->
<!-- % can have temporal parts at any scale, and can physically involve many -->
<!-- % entities, but propositions cannot. Propositions and events are easily  -->
<!-- % confused because they are closely related: NL sentences <i>express</i>  -->
<!-- % propositions and at the same time <i>characterize</i> events or situations.  -->
<!-- % But an adequate semantic representation must distinguish them, thus  -->
<!-- % providing distinct referents for the two instances of the anaphoric  -->
<!-- % <i>that</i> in the above sentences. For a full discussion see (Schubert -->
<!-- % 2000) and also (Zucchi 1989). In general, propositions believed (or rejected) -->
<!-- % by people are central to explaining the <i>reasons</i> for their actions,  -->
<!-- % while events interact <i>causally</i>. In EL, the propositional referent  -->
<!-- % in the second sentence is provided simply by applying the sentence reifying  -->
<!-- % operator to the meaning of the sentence. The next paragraph explains how  -->
<!-- % the event (episode) referent in the first sentence is obtained. -->

<p>
An important insight of NLog research is that language can be used
directly for inference, requiring only phrase structure analysis 
and upward/downward entailment marking (polarity) of phrasal contexts. 
This means that NLog inferences are <i>situated</i> inferences, i.e.,
their meaning is just as dependent on the utterance setting and discourse
state as the linguistic ``input" that drives them.

<p>
This insight carries over to ULFs, and provides a separate justification
for computing ULFs, apart from their utility in the process of deriving
deep, context-independent, canonicalized meaning representations from
language. Our evaluation of the English-to-ULF parser that we are proposing
to develop will be formulated in terms of certain classes of situated
inferences enabled by ULFs. 

<p>
ULFs in principle provide a more reliable and more general basis 
for situated inference than mere phrase structure, because of the coherent 
semantic type structure they encode. Greater reliability also leads to 
the possibility of spontaneous forward inferencing, as opposed to 
inference guided by propositions to be confirmed or disconfirmed (as 
in most textual entailment and NLog studies to date). This is important, 
because human language understanding seems to involve continuous forward 
inferencing. As a simple example, if according to your paper or newsfeed 
<i>"Police reported that the vehicle struck several cars"</i>, you will 
conclude that the reported event almost certainly happened, and further, 
that the cars involved were all damaged. Now, the first of these inferences 
requires only a small amount of knowledge about communication, to the 
effect that <i>reporting</i> (in your preferred media) typically involves 
reporting of facts; whereas the latter depends on very specific world 
knowledge. Our demonstration of ULF utility in forward inference will
focus on the former kinds of inference (and related ones), since 
accumulation of sufficient world knowledge for enabling the latter
kinds of inference remains out of reach in the short run.

<p>
Here, briefly, are some kinds of inferences we can expect ULFs to support:
<ul>
 <li> <i>NLog inferences based on generalizations/specializations</i>.
   For example, <i>"Every NATO member sent troops to Afghanistan"</i>, 
   together with the knowledge that France is a NATO member and that 
   Afghanistan is a country entails that <i>France sent troops to
   Afghanistan</i> and that <i>France sent troops to a country</i>.
   Such inferences are within the scope of NLog-based and ULF-based 
   methods, and can help in finding inference paths to candidate 
   entailments; but they will not be our focus as they rarely seem 
   worthwhile as spontaneous forward inferences from sentences in
   discourse (we are particularly interested in dialogue settings).
 <li> <i>NLog inferences based on implicatives</i>. For example, <i>"She
   managed to quit smoking"</i> entails that <i>"She quit smoking"</i> (and
   the negation of the premise leads to the opposite conclusion). We
   already demonstrated such inferences in our framework for various
   headlines {% cite stratos2011KEOD %}, such as the inference from
   <i>Oprah is shocked that Obama gets no respect</i> (Fox News 2011) 
   to <i>Obama gets no respect</i>. Such inferences are surely important
   -- and immediate -- in language understanding, and will be included
   in our evaluations.
 <li> <i>Inferences based on attitudinal and communicative verbs</i>.
   Some such inferences, for instance for <i>knowing-that</i> and <i>
     finding-out-that</i>, fall under the previous heading, but others do
   not. For example, <i>"John denounced Bill as a charlatan"</i>
   entails that <i>John probably believes that Bill is a charlatan</i>,
   that <i>John asserted to his listeners (or readers) that Bill is 
     a charlatan</i>, and that <i>John wanted his listeners (or readers)
     to believe that Bill is a charlatan</i>. Such inferences would be hard
   to capture within NLog, since they are partially probabilistic,
   require structural elaboration, and depend on constituent types.
   <!-- % [GK]: My guess is that the readers won't necessarily grasp why this isn't part of NLog anyway. -->
   <!-- %For example, the variant <i>"Mary denounced Bill as well"</i> might  -->
   <!-- %lead to the inference that <i>Mary believes that Bill is well</i>, -->
   <!-- %if <i>as well</i> is not recognized as a verb phrase adverbial. -->
 <li> <i>Inferences based on counterfactuals</i>. For example, <i>"If
   I were rich, I would pay off your debt"</i> and <i>"I wish I were rich"</i>
   both implicate that <i>the speaker is not rich</i>. This depends 
   on recognition of the counterfactual form, which is distinguished
   in ULF.
 <li> <i>Inferences from questions and requests</i>. For example, <i>
   "When are you getting married"</i> enables the inference that the 
   addressee will get married (in the foreseeable future), and that 
   the questioner wants to know the expected date of the event, and
   expects that the addressee probably knows the answer, and will supply
   it. Similarly an apparent request such as <i>"Could you close the 
     door?"</i> implies that the speaker wants the addressee to close the 
   door, and expects he or she will do so. There are subtleties in the
   distinction between questions and requests that can be captured 
   in ULF and made use of.
</ul>


        <!--
        <div class="deets">
          The ULF Project is aimed at learning a parser for primal logical forms of Episodic Logic (EL)~\ref{..} -- called unscoped logical forms (ULF) -- by obtaining a moderately large hand annotated corpus and training on statistical parser with guidance from knowledge about the formal restrictions of ULFs.
        
          
          <p>
          </p>
        </div>
        -->
  </div>

