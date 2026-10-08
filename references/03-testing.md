# 03 · Testing like a scientist

## The process beats the idea

> "The most important thing that I often instruct teams to do is to develop a reproducible testing
> process, and that will actually influence the probability of your success more than anything."
> [LP 18:58 to 19:07]

> "If you actually focus more on your process for taking many shots at bat, that's what actually
> reduces the risk more than anything." [LP 19:27]

Their speed improved with practice: the first mobile app took about a year, the last about two
weeks [LP 18:58]. Fifteen apps, 14 “basically duds” [LP 15:03], before tbh.

## Remove confounding variables

He never wants to finish a test and have to wonder whether "maybe the execution was bad" [LP 32:00].
So test the best possible version of the one thing being tested, even with manual work, so that a
*no* really means no. For a social app that means every tester has friends on it: "we would try to
get an entire school to adopt, just to know if everyone had 10 friends, would they actually derive
value from this app?" [LP 32:34]

## The seeding method (for TESTS, not growth)

- People need to see a marketing message “three times or so” before downloading, so saturate one
  area with every kind of marketing [LP 29:54].
- School-targeted ads, plus an Instagram account for that school that followed students, because
  "high schoolers identify their school in their bio" [LP 30:12].
- **His caveat, keep it:** "this is not the way we grew the app. this is how we tested apps." It was
  for the first 100 users [LP 30:46 to 31:13]; "the app should grow by itself after that" [LP 30:54].
- tbh's launch school was the one with "the earliest start date in the united states" [LP 21:15].
  About 40% of that school downloaded it in the first 24 hours [LP 21:26].

## Know within 48 hours

> "we kind of developed a reproducible model to just flood the school with ads. uh, do highly
> relevant marketing." [OOO 55:52]

> "usually within 48 hours we'd know if it if it was working. uh and with with tbh uh we knew that
> night" [OOO 56:46]

## Test for conviction, in stealth

For him the aim of a consumer product experiment "is to get signal" [SOL 2:08]. He works in a
small, stealthy silo until a particular audience responds and he has conviction, and only then
markets widely, which leaves room for big changes to the product [SOL 2:42].

## Assume you're wrong, and build reusable parts

His 2021 advice: assume by default that your idea is wrong, map the likely pivots, and build reusable
blocks such as "the friendfinder, invites, onboarding system".
[X 2021-07-09](https://x.com/nikitabier/status/1413392823630680071) In 2023 he added that the
fastest route to an app that resonates is to keep those blocks and change only "the interaction
model". [X 2023-05-25](https://x.com/nikitabier/status/1661733445163417601)

## Against minimum viable products

In November 2024 he wrote that he had “lost conviction” in MVPs. His argument, paraphrased: don't
ship a bare core flow and declare it dead when aggregate numbers are low. Hold a firm belief about
what people want, keep a steady flow of new users, add components until the value surfaces, and
make each component good enough that there are "no confounding factors that distort the signal."
[X 2024-11-16](https://x.com/nikitabier/status/1857896428317630893)

## Time-box the attempt

His 2023 sketch of a team for a new viral app: full-time, all other plans on hold, and if it
isn't working after four months, “we disband”.
[X 2023-10-01](https://x.com/nikitabier/status/1708513023990645011)

## Simulate the full product before you build it

His 2024 lesson from a map app called Ants: people clustered in the same places every day, so a
second session showed nothing new. He could have learned that by putting realistic data into a
design file first. His principle: simulate "what the experience would be like when it's fully
populated with content and users."
[X 2024-06-21](https://x.com/nikitabier/status/1804214914472644975)

## Pay for the unscalable test that answers the big unknowns

The first Gas prototype at one school cost "$600 in server costs per day" for about 800 users. They
paid it because the open questions were whether the concept would resonate again, whether people
would pay, and whether it would grow. [X 2024-02-06](https://x.com/nikitabier/status/1754896706880127185)

In 2014 he tested a whole-country launch in Malta, the smallest App Store; the app reached number one
"in 48 hours with $500 of ads." [X 2024-01-15](https://x.com/nikitabier/status/1746756081194619066)

## Know when to stop

He says about 95% of founders who come to him show "absolutely devastating metrics", and his answer
is to change the idea. [X 2023-02-01](https://x.com/nikitabier/status/1620821649888264195) And
don't trust a closed beta: he mocks founders citing beta retention from "self-selected people who
jumped through hoops". [X 2024-11-15](https://x.com/nikitabier/status/1857293213624582551)

## Who to have on the team

He rates a designer who can "distill why a user is adopting" above a 10x engineer.
[X 2023-07-15](https://x.com/nikitabier/status/1680336066325393408)

## Live chat support as user research

Put "live chat customer support in your app 24 hours a day" [LP 32:44]. It removes a confounder,
and "it's the best vehicle for getting feedback and doing user research because users will
literally tell you the problem they're having." [LP 33:15]

---

## How to apply it (our reading)

Use `templates/02-48-hour-test-plan.md`. The short version:

1. **One rung only** (chapter 04). Write what must be true in one sentence.
2. **Kill the confounders**: density (seed one real group at once), support (live chat), polish of
   the one flow under test.
3. **Seed** with about three marketing touches per person in that group, all within a day.
4. **Pick the signal and the thresholds before launch**: a YES line, a NO line, and what the band
   in between means.
5. **Read at 24 and 48 hours.** Decide: next rung, change and relaunch, or stop.

**Worked numbers (invented).** A seed group of 400 students. Plan: 3 touches each (ads, an account
that follows them, a flyer or post) inside one day. Our suggested thresholds for a core-flow test:
YES if 50% or more of sign-ups do the core action at least 3 times on day 1; NO if under 20%;
in between is UNCLEAR, which means check density first (did testers have at least 10 friends on
it?) and relaunch once. These lines are ours; the “10 friends” density bar is his [LP 32:34].

**Failure modes.**
- Treating the seeding method as a growth strategy. He says it is not.
- A test that changes three things at once, so a result can't be read.
- Choosing thresholds after seeing the numbers.
- Running it in public, so a weak first version becomes the product's reputation.

**Limits.** *Know within 48 hours* holds for social apps where use is daily and dense. A utility
with weekly use needs a longer read (chapter 16).
