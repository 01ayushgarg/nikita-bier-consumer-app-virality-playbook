# 08 · Measurement and diagnosis

## Start with "how is it growing today?"

> "What I try to do is like to see uh where is there already organic distribution happening. Uh so
> that that's like my first kind of overview is like I ask a question how is it growing today? Uh and
> how can we augment that? So that often looks at like trying to attribute traffic where where is
> where are these downloads coming from?" [OOO 1:08:12]

> "The first thing I often do is I ask them to show me the analytics. We look at how people are
> distributing the app today, what is the milestone that a user must hit to become activated and
> what's getting in the way of that?" [LP 1:32:44]

## Walk every step of every funnel

> "The biggest gap I see with uh startups when they try to grow, they're they're not actually
> methodically looking at every part of the funnel uh and there's crazy places that users drop off
> that you wouldn't ever anticipate. Um and uh you you it starts with just instrumentation and uh
> knowing knowing what's happening through the whole thing." [OOO 1:07:29]

> "When it comes down to it there's really no silver bullet to growth. When I start any sort of
> advisory engagement, I'm like, we're going to not leave a single stone unturned. We're going to uh
> you know, juice every surface we can uh to make sure that if people are having a great time on the
> app that they can tell their friends about it." [OOO 1:04:49]

At X the same method, applied to a 20-year-old app: "we audited every every possible funnel to get
into the app. Uh, and we threw every growth hack in the world at it." [OOO 9:33]

## Founders must own the analytics

[X 2025-02-25](https://x.com/nikitabier/status/1894468176584610053):

> "One of the most important skills to learn as a founder is how to use Mixpanel—especially with a
> very small sample size. This is not something you can delegate because only you will be obsessed
> enough to make sure your insights are valid. Almost everyday I see founders get deluded into
> thinking:
> A. They have an onboarding problem—that was actually triggered by internal debugging sessions by
> the devs, or
> B. Their onboarding is working—but they are not properly tracking logged-out users
> C. Users are sharing their app—but they are just tracking attempts and not the final send events
> At the earliest stages, you must be using a patchwork of filters to remove users and constantly be
> auditing individual sessions to see what is actually happening during apparent drop-off."

## Guardrail metrics and the 50/50 rule

- When X changed how links display, the guardrail was time spent: "the thing we were like really
  mindful of was would it actually lead to less time spent in the app? Um and uh it was actually
  flat" [OOO 38:05]. An algorithm migration was judged the same way: "could engagement stay at least
  flat" [OOO 20:42].
- "As with any feature on X like 50% hate it 50% love it. But the data spoke for itself" [OOO 28:36].
- PMF needs no fine measurement: "If your product's working, you'll know. And if there's any
  uncertainty, it's not working" (Nikita relaying founder Roger Dickey) [LP 36:15].

## Two kinds of growth work

[X 2023-08-07](https://x.com/nikitabier/status/1688538948514021376) (half joke):

> "There are two types of growth people in tech:
> 1. Micro-optimizing cocaine-fueled finance-adjacent A/B tester
> 2. Step-function, is right less than half the time, "what's an A/B test?" viral K-factor guy
> There is a place and a time for each."

**Checks to run:**
- Are internal and test users filtered out of every funnel?
- Are logged-out users tracked?
- Is "shared" counted at the final send event, not the attempt?
- Has someone watched individual sessions at the biggest drop-off?
- Where do downloads come from today? Name the source of the top three.
- What guardrail metric must stay flat for the next change to ship?
