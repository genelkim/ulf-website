---
layout: home
---

## Welcome!

This is the ULF project page! This project is aimed at formulating, annotating,
and parsing so-called _unscoped logical forms_, (ULF) which is representation for naturally
capturing the semantic type structure of language within the framework of Episodic
Logic.

On this site you can learn more about <a href="/ulf/">ULF</a>, access <a
href="/resources/">resources</a> related to the project, take a look at the
<a href="/publications/">publications</a> that came out of our work, or 
learn more about <a href="/about/">the team</a>!

- TODO: add prev and next buttons on intro series
- TODO: add info
- TODO: incorporate codemirror to get ULF syntax and bracket highlighting
- TODO: table formatting

### ULF: A Primal Logical Form for Episodic Logic

Aspects of meaning unrelated to the semantic type structure are largely left
ambiguous in ULFs for resolution in later steps.  The purpose of this is to have a
semantic representation that can be quickly annotated by people and then precisely
parsed using the current state-of-the-art techniques.  Take a look at a couple English
sentences and corresponding ULFs.

- Could you dial for me? 
```
(((pres could.aux-v) you.pro ((dial.v {ref1}.pro) 
                                (adv-a (for.p me.pro)))) ?)
```

- If I were you I would be able to succeed
```
((if.ps (I.pro ((cf were.v) (= you.pro))))
 (I.pro ((cf will.aux-s) (be.v (able.a (to succeed.v))))))
```

The dot-extensions `.n`, `.v`, `.a`, `.p`, `.aux-s`, and `.pro` are named in
relation to their syntactic part-of-speech correspondents (nouns, verbs,
adjectives, etc.).  Furthermore, if you're familiar with constituency tree, you
might have noticed that the general structures of these formulas have a lot in
common with them.  For example, "for me" makes a single constituent, which is a
prepositional phrase in constituency trees.  Similarly, "dial for me", "will be
able to succeed" are both single constituents that correspond to verb phrases.
This sort of correspondence means that we can expect annotating and learning
parsers for ULFs shouldn't be too much of a stretch beyond constituency
parsing, for which research has been very successful.

Despite the surface similarity, ULFs are not syntax.  The underlying Episodic
Logic type system means that there are specific formal meanings and
restrictions to the compositions in these formulas.  `.pro` correspond to
individuals in the domain, whereas `.n`, `.a`, and `.v` correspond to
predicates of varying adicity.  This is why we need operators like `adv-a` are
necessary for shifting the types appropriately.  ULFs are useful both for
further resolution of ambiguity towards full Episodic Logic (as the name ULF
suggests, one of these resolution steps is scoping) and immediate inference
from ULFs.  The closeness of ULF to syntax allows it to be used in Natural
Logic-like inferences, which are inference derived from syntactic structure,
polarity context, and specificity-relations between words and phrases.  The
semantic types of ULFs also allows it to make forward inferences in a manner
similar to Episodic Logic, while attending to the locations of remaining
ambiguity.

Learning a precise parser for ULFs would be a step toward a comprehensive
semantic parser for a rich, model-theoretic semantic representation.  We
expect that a representation like this is necessary for general and robust
understanding and reasoning over natural language.

