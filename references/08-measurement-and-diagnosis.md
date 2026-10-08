# 08 · Measurement and diagnosis

## Start with: how is it growing today?

> "what i try to do is like to see uh where is there already organic distribution happening. uh so
> that that's like my first kind of overview is like i ask a question how is it growing today?"
> [OOO 1:08:14]

> "The first thing I often do is I ask them to show me the analytics. We look at how people are
> distributing the app today, what is the milestone that a user must hit to become activated and
> what's getting in the way of that?" [LP 1:32:44]

## Walk every step of every funnel

> "the biggest gap i see with uh startups when they try to grow, they're they're not actually
> methodically looking at every part of the funnel uh and there's crazy places that users drop off
> that you wouldn't ever anticipate." [OOO 1:07:29]

"there's really no silver bullet to growth" [OOO 1:04:50]. At X he applied the same method to a
20-year-old app: "we audited every every possible funnel to get into the app." [OOO 9:33]

## Founders must own the analytics

In a 2025 post he says founders must learn Mixpanel themselves, "especially with a very small sample
size", and lists three traps he sees almost every day [X 2025-02-25](https://x.com/nikitabier/status/1894468176584610053):

- an “onboarding problem” that was really caused by the developers' own debugging sessions;
- onboarding that looks fine because logged-out users are not tracked;
- *sharing* that counts attempts, not final send events.

His fix, paraphrased: filter aggressively and audit individual sessions at every apparent drop-off.

## Guardrail metrics and the 50/50 rule

- When X changed how links display, the guardrail was time spent: "the thing we were like really
  mindful of was would it actually lead to less time spent in the app? um and uh it was actually
  flat" [OOO 38:37].
- An algorithm migration was judged the same way: "could engagement stay at least flat after the
  the migration. uh and it did" [OOO 20:45]. **His claims.**
- "as with any feature on x like 50% hate it 50% love it. but the data spoke for itself" [OOO 28:43].
- Product-market fit needs no fine measurement: "if your product's working, you'll know. and if
  there's any uncertainty, it's not working" (Nikita relaying founder Roger Dickey) [LP 36:12].

## Two kinds of growth work

His 2023 half-joke: there are micro-optimising A/B testers and step-function K-factor people, and
each has its place and time.
[X 2023-08-07](https://x.com/nikitabier/status/1688538948514021376)

---

## How to apply it (our reading)

**A one-afternoon diagnosis.**

1. **Clean the data** with `templates/01-instrumentation-checklist.md` (his three traps first).
2. **Attribute installs**: top three sources and the unknown share. If unknown is above about 15%
   (our line), fix attribution before anything else.
3. **Name the activation milestone** in one event (for example *sent first message to a friend*).
4. **Draw the funnel** from store page to that milestone and on to the first invite or share sent.
5. **Watch 10 sessions** at the biggest drop. Write what you saw, not what you guess.
6. **Pick the guardrail** for the next change: the metric that must stay flat or better.

**Worked numbers (invented).** The funnel shows 30% drop at *verify phone*. Filtering out 40 test
devices moves it to 18%. Session replays show the SMS code arriving after the screen times out.
The fix is a longer timeout, not a redesign. This is the "crazy places that users drop off" he
describes [OOO 1:07:29].

**Failure modes.**
- Acting on a funnel that includes your own team's devices.
- Counting *share sheet opened* as a share.
- Shipping a change with no guardrail, then arguing about whether it hurt.
- Using sentiment (replies, reviews) instead of numbers to judge a change. His 50/50 line is the
  reason.

**Limits.** At very small samples a single test cohort can swing rates by tens of points. Read the
sessions, not just the percentages.
