---
title: Some Thoughts on the Atemporal/Temporal Distinction
author:
  - gene
categories:
  - Half-baked
  - Type Structure
---

TODO: add the FOL\*\* distinction to the document since that problem still exists.
TODO: ask Len about the distinction between situations, events, and episodes
with regard to the EL ontology.  Are they equivalent?  Or is there some amount
of subtlety to it that led him to say that types are D->E->2 rather than
D->S->2?  If they're equivalent, I'm not sure which name I prefer.  I like that
situation is most distinct from stuff like Davidsonian semantics, but I suppose
there's situation semantics that we'd clash terms with.  Also, since we have
event variables, maybe we should just call them events?  Just make it clear
that due to the underlying theory, it's not the same as Davidsonian events (I
remember seeing somethign like this already in the document).
TODO: we should probably still have a distinction between adv-a as an action modifier
and one for a predicate modifier.  Since the type for an action is (D,E)->2, and a 
predicate modifier is (D->S->2)->(D->S->2).

{% assign dom = "\mathcal{D}" %}
{% assign sit = "\mathcal{S}" %}
{% assign tru = "\mathcal{2}" %}

NB: Although this post is written be me (Gene), it's based on discussion with Len, and honestly most of these ideas are from Len.  BUT, any postitions taken in the post are mine, not Len's.

Up to this point we've been thinking of the temporal/atemporal distinction in EL as being roughly equivalent to Greg's stage-level vs individual-level predicates and been formalizing the atemporal distinction in EL in the following ways.

_For FOL\*\* (FOL-like subset of EL)_

- atemporal: \\({{ dom }}^n \rightarrow {{ tru }}\\)
- temporal: \\({{ dom }}^n \rightarrow ({{ sit }} \rightarrow {{ tru }})\\)

That is, atemporal predicates take individuals and return a truth value, whereas temporal predicates need to also be supplied a situation, which is associated with a temporal timespan, to return a truth value.

_For EL (as currently proposed at the time of writing)_

- atemporal: \\({{ dom }}^n \rightarrow ({{ sit }} \rightarrow {{ tru }})\\)
- temporal: \\({{ dom }}^n \rightarrow ({{ sit }} \rightarrow {{ tru }})\\)

That is, _all_ predicates take a situation in order to return a truth value.  This is done with
a trick of saying that atemporal sentences characterized empty situations.  So atempral
predicates take \\(n\\) individuals and return either \\(0\_\epsilon\\) or \\(1\_\epsilon\\),
where these functions respectively return \\(0\\) and \\(0\\) when applied to \\(\epsilon\\),
the empty situation, and are otherwise _undefined_.  So this captures timelessness of atemporal
predicates while still having the same type.  From the position of ULF, then we don't actually
need to make a distinction between these two things.

However, in making this distinction, Len and I both had the thought that
perhaps all nouns (and maybe even adjectives) are in fact atemporal but then 
the copula acts as a mediator to turn this into a temporal statement.  Given 
this sort of analysis `human.n` is atemporal so `(|John| human.n)` means that
the individual is timelessly human whereas`(|John| ((pres be.v) human.n))` 
is temporal and may only be true for a limited segment of time.  This may
seem a bit ridiculous, but it's based on some examples that Greg has brought
up before, where seemingly temporal nouns are allowed outside of their 
intuitively restricted temporal span.  For example, 

_"After an emergency landing of the plane this morning, all the passengers are now safely at home."_

Strictly speaking, they are no longer passengers, but this is still an acceptable
sentence.  So it seems then, that nouns are in some sense timelessly true, but pragmatically
non-sensical in certain contexts.  It turns out that this approach comes across some problems. 

1. As defined, there aren't very many atemporal predicates in natural language.
2. Once we look more closely, we find that the temporal/atemporal distinction
   we've made isn't really the same thing as what Greg what getting at in the
   individual- and stage- level predicates.
3. Considering nouns to be atemporal -- turned temporal via the copula -- is untenable
   when considering other syntactic contexts in which nouns appear.

There are other approaches that allow us to handle nouns taht seem to be referenced
outside of their temporal restricted context, without resorting to treating nouns
as atemporal.  This in combinations with the problems that I listed seem to indicate
that there's a better, simpler alternative.  Well, simpler for the ULF project.  Now,
I'm going to go into each of what I said in more detail.

## Atemporal Predicates in Natural Language?

So truly atemporal predicates seem to basically be non-existent in natural language.
Perhaps abstract notions like mathematical classes (e.g. `number.n`, `even.a`,
`odd.a`, `set.n`) can be atemporal, but all _things_ in the world are
temporally bound in their existence.  We'll need to make sure that if we're treating
many predicates as atemporal, that some mechanism ensures that the real-world 
temporal restrictions are somehow maintained.

## Atemporal/temporal vs stage/individual

At first glance it would seem that the atemporal/temporal distinction is doing the
same thing as stage/individual level predicate distinction right?  Afterall, if 
a predicate is true of an individual over its lifetime, then it's basically atemporal,
that is true of that individual at all times.  

However, individual level predicates aren't necessary unchangeable.  It's
simply that they are longer-term and there are differences in acceptability of
syntactic contexts that reflect these differences.  I've already mentioned one
of the differences, which is with individual level predicates can be used to
refer to an individual even when it doesn't seem to hold anymore.  So even
though we can have a sentence like "Bob is a student now, but won't be a student
next year" indicating that it's changeable we also have sentences like
"The student is now a doctor", where presumeably, the student is not continuing
to be a student while practicing as a doctor.  This seems to show that in some way
"student" can still be truthfully applied to this individual.

I mentioned already that we may consider this to be handled via the copula.  So
in "Bob is a student now, but won't be a student next year", "student" is atemporal,
BUT "is a student" is not.  But what happens in uses without a copula like appositives?
*"John, a student, already graduated" is not acceptable, and there's no copula there
to make it temporal.  So the copula handling doesn't seem to be able to capture
all the cases where these atemporal predicates are being used with temporal 
restrictions.  

Other than examples like these, it 

## 

TODO: finish this...

I agree that we probably can't maintain that the temporal/atemporal distinction
corresponds to the stage/individual level predicates,
I'm not sure if it's completely untenable to maintain the temporal/atemparal
distinction with the copula as the mediator between the atemporal and temporal
uses of a noun.  That is, the predicate "student" is atemporal, but when used
with the copula has a temporal restriction.  All the quantification examples
would be handled by this from the fact that due to the predicates being
atemporal (and without a copula), the temporal relationship between when it
actually holds for the restrictor and the time of the matrix is not relevant
since the semantics don't say anything about when it actually holds for the
restrictor.  Arguably, this approach can explain the issue with 

 "The fugitives crying for joy are now in jail"

Since "fugitives" is atemporal, the actual time that this applied is pragmatically
inferred, whereas "crying for joy" is temporal, so it gets tied to the matrix.
This also seems to explain the two readings of "crying fugitives" in
  
  "The crying fugitives are now in jail"

Either we get a reading similar to the above example where "crying fugitive" is
read intersectively and thus "crying" is tied to the matrix predicate time.  Or
we get "crying fugitive" as a specific type of fugitive, where "crying" is
non-intersectively modifying "fugitives".  Then the "crying" time is independent
of the time of the matrix event.  I can imagine either an instance where the
fugitives, whenever they were spotted, were crying so they got dubbed 
"the crying fugitives" or a case where during a particularly noteworthy event,
the fugitives were crying so they got dubbed "the crying fugitives".

I think all the other examples you gave could be handled with the copula-assisted
temporal interpretation of atemporal predicates.  Perhaps this is an unsatisfying 
analysis though, in which the temporal relationship between the actual time when
the restrictor predicate applies to the individual is ignored on a technicality
and then resolved using pragmatics and world knowledge.  For example, the creation/
destruction examples reduce knowing that most predicates, including individual level
nouns aren't 

This really seems to be
an issue of nouns though, not all individual level predicates since we can't 
quantify over individual predicates that aren't nouns (e.g. the loyal are here
-> the loyal (people) are here).

The biggest problem with this approach to me seems post-nominal modifiers that
clearly restrict the temporal scope without using the copula. 
*"John, a student, already graduated" is not acceptable, and there's no copula there.
We would have to interpret appositives as having an elided copula in order to
get the right meaning.  This isn't impossible, but it seems messy.  This isn't
to say that I think this approach is what we should do.  I just don't necessarily
think it's impossible to maintain this approach.

I'm not sure if we should talk about the temporal-atemporal distinction at
all.  If in EL the types are unified into a single type, then why should
we make a distinction in ULF?

Considering this, I think we should clean up our predicate modifiers.  First
of all, I want to make a distinction between action modifiers, e.g. manners, 
adjective modifiers (e.g. very happy) since the latter really aren't action
modifiers and seem to be a different semantic type.  Furthermore, I want to either
fully incorporate the syntactic types to the type system or not at all.  So either, have
one predicate modifier forming type (and eliminate attr, nn). or fully
distinguish them (e.g. adv-adj, adv-v, kind of thing).  It just seems really strange to
me that we make the effort to distinguish 'nn', from 'attr', but then all the other
predicate modifiers are formed using 'adv-a'.  

