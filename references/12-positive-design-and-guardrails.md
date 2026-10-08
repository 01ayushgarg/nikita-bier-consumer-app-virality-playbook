# 12 · Positive by design, and the guardrails (always applied)

## Nikita's own rules

> "i always do things by the book when it comes to operating legally within the compliance
> framework." [LP 1:00:34]

He tells founders that growth tricks outside the rules will "cause way more trouble down the line"
and “burn users too” [LP 1:00:53]. The patterns he names: apps that "in the background use user data
in ways that it shouldn't be used" and "invite people on your behalf" [LP 1:01:05].

**The internet defends itself.** He compares it to the Gaia hypothesis: "if you do the wrong thing by
users, the internet will come back and get even and defend itself." [LP 1:01:28 to 1:01:46]

## Design so nobody is left out

tbh and Gas only allowed positive things, through polls the team wrote [LP 27:19]. Gas also made
sure people who had not been picked recently showed up in polls more often: "we wanted to spread the
love in every way possible" [LP 1:04:03].

He recalls Gas receiving messages from users saying they had "reconsidered suicide or other forms of
self-harm" [LP 1:03:17], and says "we were entirely focused on making teens feel better." [LP 1:03:45]

## Positivity was the product, from the start

From TechCrunch's 2017 reporting on tbh:

- Bier: "If we're improving the mental health of millions of teens, that's a success to us." [TC1]
- Bier: the aim was not to say whatever you want "but to be able to say what you feel to others."
  [TC1]
- The team: "We worked backwards from the content we wanted to see" [TC1].
- A built-in limit, in TechCrunch's description: the app "only allows you to answer 12 per hour, so
  you never get sick of it and always want more." [TC1]

In 2026 he described the brief the same way: earlier anonymous apps "most of them actually had to
shut down because of bullying", so the question was how to keep their value “and still make sure”
that people weren't bullied [OOO 52:52].

## Constraints can be the big idea

In a 2025 post he argues that the “big idea” of an app is sometimes a constraint that feels onerous
but protects the community. For Gas, pre-set positive messages removed bullying and, he says,
multiplied messages sent. His conclusion: the idea that resonates "may just be giving them less
freedom." [X 2025-05-24](https://x.com/nikitabier/status/1926295017619939743)

## Think like an adversary

> "it also taught me how to think like an adversary, which is very critical when you're building
> consu like consumer internet software." [OOO 3:28]

At X he asked of every feature: "how might people manipulate this feature?" [TBS 40:44] And a rule for
AI: "a machine should not be talking to a human unprompted" [TBS 25:26]; otherwise "that is
effectively spam" [TBS 25:41].

## This skill's refusals

The skill will not help with:
- Sending invites, texts or messages a user did not knowingly send.
- Using contact or other personal data beyond what the user understood and agreed to.
- Fake social proof, fake users or fake activity.
- Anonymous mechanics that allow bullying, rating of appearance, or negative messages about real
  people.
- Any mechanic aimed at minors that relies on pressure, shame, fear of missing out, or deception.
- AI companions or chatbots aimed at minors, or designed to create dependence (chapter 15).

---

## How to apply it: the guardrail pass (our reading)

Run this on every recommendation before it leaves the audit.

| Check | Pass if |
|---|---|
| Consent | The user sees exactly what is sent, to whom, and taps send themselves |
| Data | Contact or profile data is used only for what the prompt said |
| Content | Users can only send things that cannot be used to hurt someone, or there is moderation that can keep up |
| Inclusion | Nobody is systematically left out or ranked low in public |
| Minors | Age checks fit the risk; no paid reveals; no pressure loops; no AI companion features; local children's privacy and messaging law reviewed by a lawyer |
| Abuse | You have written down how a bad actor would use the feature, and what stops them |
| Honesty | The growth loop would still work if users understood it fully |

**Worked example (invented).** A team proposes *notify a contact when they're mentioned in a poll,
even if they're not on the app*. Consent fails (the person never asked), Data fails (contacts used
to message non-users), Minors fails if users are teens. He calls this kind of thing “egregiously
illegal” [LP 58:47]. Replace it with an invite the user chooses to send.

**Limits.** This chapter is not legal advice. Laws on children's data, messaging and AI differ by
country and change often.
