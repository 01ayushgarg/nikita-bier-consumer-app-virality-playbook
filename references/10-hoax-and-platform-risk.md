# 10 · Hoaxes and platform risk

Nikita: any app that goes viral may get a hoax started about it, partly because warning people
about a *dangerous* app earns the poster attention and followers [LP 1:05:12]. For Gas it was a false
claim that an anonymous polling app “without messaging” was used for human trafficking [LP 1:04:41].
Other founders told him they had had to shut down over the same thing [LP 1:05:35].

TechCrunch, at the time of the Discord deal, called the rumour “completely false” and reported that
Bier told the Washington Post he and his team "received hundreds of graphic death threats" [TC3].

## The rule

> "you really have to make sure the hoax is less viral than your app." [LP 1:09:34]

## Spot it early [LP 1:13:20 to 1:14:42]

The first sign was one support message with a screenshot of a Snapchat story that had already been
re-screenshotted dozens of times, plus one App Store review. Nikita told his team "this is going to
be 10 times bigger tomorrow" [LP 1:14:16]. The next day the reviews had multiplied.

**One support report that has already been re-shared many times is not one report.** Treat it as an
incident.

## What they did [LP 1:06:26 to 1:09:22]

- **Search results:** worked with journalists so the top result for the false claim said it was not
  true; they insisted the Washington Post headline say so [LP 1:06:26].
- **Retractions:** "i called those superintendents, i called those police chiefs and have got them to
  publicly retract it." [LP 1:06:54]
- **Review bombing:** asked Apple to remove the hoax reviews.
- **Platforms:** got TikTok videos spreading the claim removed [LP 1:09:10].
- **The delete flow:** anyone deleting their account could watch a video explaining the truth. At the
  peak 3% of users deleted their accounts per day; "we got it down to 0.1% through relentless,
  relentless effort." [LP 1:07:14 to 1:07:25]
- **Investors:** he told interested investors that unless they could get a celebrity to say it
  wasn't true, he wasn't interested [LP 1:08:42].

## Fight memes with memes

From the Washington Post's reporting on the Gas hoax [WP]:

- "the challenge is that you can only fight memes with memes. if it's not easily screenshotable and
  exciting it's not going to get more visibility than the original message."
- On press: "there's no way to combat that with press," because teenagers "are not reading the
  legacy news."
- What they shipped, per the Post: a push notification to every user about safety and a safety
  center.

## Relaunching under a new name only works once

They renamed and relaunched on the other side of the country. The hoax followed, "and then it was
too late at that point to relaunch again." [LP 1:15:20]

## The other platform risk: losing a channel

A hoax is one way growth stops overnight. A platform cutting you off is the other: Snap removed Gas
from SnapKit a week after a meeting about acquiring it [TC4]. See chapter 07.

---

## How to apply it (our reading)

Use `templates/06-hoax-response-runbook.md`. The sequence:

1. **Detect.** One person owns support, reviews and social search every day. Trigger: any rumour
   seen in more than one place.
2. **Measure the hoax's K-factor**, as he did: how fast is the claim spreading compared with the app?
3. **Answer in the rumour's format** (a screenshot, a short video), inside the product, at the
   moments people decide to leave (the delete screen, a push notification).
4. **Get the sources to retract**: the institutions that posted it, the platforms hosting it, the
   app store reviews.
5. **Own the search result** with a clear headline that names and denies the claim.
6. **Track deletions per day** as the outcome metric.

**Worked numbers (invented).** 400,000 users, deletions jump from 0.2% to 2.5% a day: 10,000 accounts
lost per day. A debunk video on the delete screen that halves deletions saves 5,000 accounts a day,
far more than any press release would reach.

**Failure modes.**
- Treating it as a PR problem and hiring a crisis firm (he found press could not reach teens).
- Answering only on your own blog.
- Relaunching under a new name and hoping. It worked once, briefly.
- Arguing with individual posters instead of the institutions that amplified them.

**Guardrail.** Never answer a safety rumour by minimising safety. Ship real safety features and
reporting first; the debunk only works if it is true.
