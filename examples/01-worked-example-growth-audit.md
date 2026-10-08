# Worked example · A full growth audit, start to finish

> ⚠️ **Illustrative.** *Crewmate* is a **fictional app** and every number below is **invented** to
> show how the skill works, step by step. Nothing here is a claim about a real company. The
> principles and quotes cited are real and sourced (see `SOURCES.md`).

## The founder's brief (what they gave the agent)

> *Crewmate helps first-year college students find study groups for their classes. You sign up, add
> your classes, and it matches you into a group chat with classmates. We launched at 4 universities 6
> weeks ago, have 9,200 sign-ups, and growth has stalled. We're spending $3k a week on TikTok creators.
> Why aren't people inviting their friends?*

### Numbers they shared (last 4 weekly cohorts)

| Metric | Value |
|---|---|
| Installs per week | 1,500 (down from 2,600 at launch) |
| Install sources | 61% TikTok creator videos, 22% unknown, 12% invites, 5% App Store search |
| Sign-up completion | 58% |
| Sign-up methods offered | Apple, Google, email, phone |
| Notifications permission | 71% |
| Contacts permission | Not asked |
| Adds a class (first action) | 49% of sign-ups |
| Matched into a group (aha moment) | 31% of sign-ups |
| Users who sent an invite | 9% |
| Invites per inviter | 2.1 |
| Invite → new user (7 days) | 18% |
| Day-7 retention | 14% |

### First 60 seconds (as described)

Open → 3 intro slides → choose sign-in method → name, year, major → *add your classes* (search by
course code) → a 30-second voice note, *introduce yourself to your group* (required) → wait for a
match (can take hours) → group chat.

---

## The audit (the skill's output)

# Growth audit: Crewmate

**Rung:** core flow is not yet proven (step 1 of the ladder) · **Graph:** friend graph (classmates)
· **Why:** only 31% of sign-ups ever reach a group, and matching can take hours, so most users never
see the product work. Invites (9%) are a symptom of that, not the cause. [`04-validation-ladder.md`]

## Instrumentation gaps (fix before trusting the numbers)
- **22% of installs have an unknown source.** Attribute them before deciding the TikTok spend works
  ("how is it growing today?" [OOO 1:08:14]). · `templates/01`
- **Check whether *sent an invite* counts taps or final sends.** Nikita: founders are often
  “just tracking attempts and not the final send events” [X 2025-02-25]. If it counts taps, the real 9% is lower.
- **Filter out team and test devices**; at 4 universities a few test accounts distort small cohorts.

## Table stakes (fix first)
1. **Remove the required voice note from onboarding.** He estimates that requiring sound or voice
   in sign-up costs a “60% tax” on growth [X 2025-05-21] · ch. 05
2. **Use one sign-in method, phone number, paired with SMS invites and contact-based friend
   finding.** Four methods corrupt the graph so users “can't find each other” [X 2023-05-26] · ch. 06
3. **Cut the 3 intro slides.** Value has to show in about three seconds [LP 1:27:31] · ch. 05
4. **Staff live chat support during the next test** to hear why people drop [LP 32:44] · ch. 03

## Step-function changes (pick one, then test it properly)
1. **Instant group on sign-up.** Don't make users wait hours for a match. Pre-create a group for every
   course section and drop the user in at once, showing classmates already there. "The first night you
   have to see all of your friends on the app and experience it, otherwise you'll churn."
   [LP 1:27:43] Expected effect: *matched* rises from 31% toward the class-added rate (49%).
2. **Contacts-based friend finding, ranked.** Ask for contacts right after the user adds a class
   (*see which friends are in BIO 101*). Rank classmates not yet on the app by how many of their
   friends are [LP 1:30:59]. His 2021 benchmark: under 70% contacts permission is “dead on arrival” for a
   social app [X 2021-06-11]. Expected effect: more inviters (b) and more invites per inviter (c).
3. **Invite that names the class.** *Join BIO 101 Section 4 on Crewmate. 11 classmates are in.*
   The community in the ad, the app and the invite should match [LP 1:33:09]. Expected effect:
   higher invite → new-user conversion (d).

## The test (template 02)

Rung check with template 05 first: rung 1 is unproven, so the test targets rung 1 only.
- **What must be true:** *If a first-year joins, they land in a live group of their own classmates
  within one minute, and send at least one message that day.*
- **Setup that removes confounders:** one dorm or one large intro course at one university, seeded
  all at once [OOO 55:52]. Instant groups only, no other change. Live chat staffed.
- **Signal, agreed in advance (our thresholds, not his):** primary metric is the share of sign-ups
  who send a group message on day 1.
  - YES: 60% or more, and 25% or more invite someone.
  - NO: under 40%.
  - UNCLEAR: 40% to 59%, or 60%+ with fewer than 25% inviting. Check density first (did most
    testers have about 10 classmates in the group? [LP 32:34]), fix it, and relaunch once in a second
    course. A second UNCLEAR counts as NO for this design.
  - Read within 48 hours [OOO 56:46].

## K-factor now (template 03)

K = 9% inviting × 2.1 invites × 18% conversion = **0.034**. Effectively no viral growth: almost every
user is bought. That matches the 61% TikTok share, which Nikita would call “a press bump”, not
product-led growth [OOO 1:06:14].

## What I could not assess
- Real reasons for drop-off at *add your classes* (needs session recordings).
- Whether TikTok users retain better or worse than invited users (send day-7 retention by source).
- Whether the brand name helps or hurts invites (run a name test only after the core flow holds).

## Reality check
About half the startups he advises hit big success and half fail outright, "because consumer is so
random" [LP 1:29:37]. This audit raises the odds; it can't promise the outcome.
