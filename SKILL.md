---
name: nikita-bier-consumer-app-virality-playbook
description: Audit and design a consumer app for viral growth using Nikita Bier's playbook (tbh, sold to Facebook; Gas, sold to Discord; former head of product at X), built only from his own interviews, posts and verified reporting. Use when someone wants their consumer or social app to grow by itself, asks why their app is not spreading, wants a growth audit, is choosing an app idea or audience, designing onboarding, contact sync, a friendfinder, invites, sharing or notifications, naming an app, planning a launch test, instrumenting funnels, handling breakout growth, fighting a rumour about their app, monetizing, or building an AI-era consumer app. Triggers on 'make my app go viral', 'growth audit', 'K-factor', 'why aren't users inviting friends', 'how do I test this app idea', 'time to value', 'activation', 'onboarding conversion', 'invite flow', 'friendfinder', 'share feature', 'our app is blowing up', 'there's a hoax about our app', 'what would Nikita Bier do'.
---

# Nikita Bier's Consumer App Virality Playbook

An unofficial, sourced method for making consumer apps spread, built from Nikita Bier's own
account of 15 apps, 14 duds, two #1 apps in the US App Store (tbh and Gas), two acquisitions,
four years building zero-to-one apps at Facebook, years of advising founders, and about 13 months
as head of product at X. Who he is: `references/00-who-is-nikita-bier.md`.

> "with certainty, if you're good at your job, you can make an app grow and go viral." [LP 1:19:27]

> "retention for consumer social is there's a tremendous amount of randomness." [LP 1:19:00]

**Hold both.** Growth is treated here as a science. Durability is not promised. Say so to the user
when it matters.

## Ground rules for the agent

- **Read `references/benchmarks.md` first.** It lists every number in the playbook with its date
  and source. Use those figures, not remembered ones.
- Every principle in `references/` carries a source ID and timestamp or link (see `SOURCES.md`).
  Quote from there. **Never attribute anything to Nikita that is not in a cited source.**
- Sections marked *Our reading* or *Our suggestion*, and every threshold in the worked examples and
  templates, are this repo's, not his. Label them that way in the audit.
- Present tagged items (`[2021]`, `[2024]`, `[2026]`) as true at that date and flag them for
  re-checking.
- Where sources conflict (⚠️), show the versions; do not pick one silently.
- Label his unverified results as his claims.
- Quotes from Out of Office, Where It Happens, TBS, Solana Stories and the SCET clip come from
  auto-captions. Say so if the exact wording matters.

---

## Step 1: Intake (ask only what you cannot see)

1. **What the app does** in one sentence, and the core action a user repeats.
2. **Who it is for**, with age, and whether they are at a social inflection point (`02-audience.md`).
3. **Friend graph or interest graph?** (`06-social-graph-and-invites.md`)
4. **Stage:** idea, prototype, launched, or growing.
5. **Numbers:** installs per day and their sources, contacts opt-in %, push opt-in %, % of new users
   who invite or share, invites per inviter, shares (final send events, not attempts), activation
   rate, retention. Missing numbers are a finding, not a blocker.
6. **The first 60 seconds:** each screen a new user sees and taps, in order.

His own first questions, which you should ask too: the vision and the target audience [SOL 0:37],
then "I ask them to show me the analytics" [LP 1:32:44] and how it is growing today [OOO 1:08:14].

## Step 2: Check the instrumentation before trusting any number

Run `templates/01-instrumentation-checklist.md` (internal users filtered, logged-out users tracked,
share counted at the final send). "it starts with just instrumentation" [OOO 1:07:46].
Details: `08-measurement-and-diagnosis.md`.

## Step 3: Place them on the validation ladder

Read `04-validation-ladder.md` and fill in `templates/05-validation-ladder-scorecard.md`. Find the
FIRST rung not yet proven:

```
core flow works  →  spreads inside a group  →  hops between groups  →  people pay
```

The audit aims at that rung. "execute at 100% for the thing you're trying to validate at that
specific stage of the product development cycle." [LP 1:12:02]

## Step 4: Run the checks for that rung

| Stuck on | Load these references |
|---|---|
| No idea yet, or idea in doubt | `01-idea.md`, `02-audience.md` |
| Core flow (users don't use it) | `05-activation.md`, `03-testing.md` |
| Spreading inside a group | `06-social-graph-and-invites.md`, `18-shareable-content-and-notifications.md`, `07-distribution-channels.md` |
| Hopping between groups | `07-distribution-channels.md`, `18-shareable-content-and-notifications.md`, `06-social-graph-and-invites.md` |
| People pay | `11-monetization-and-economics.md` |
| It's working and breaking | `09-breakout-scale.md` |
| A rumour, or a platform cut you off | `10-hoax-and-platform-risk.md` and `templates/06-hoax-response-runbook.md` (urgent: skip the ladder) |
| AI product, or *should we build this now?* | `15-ai-era.md` |
| Founder wants audience as distribution | `13-building-in-public-and-posting.md` |
| Utility, non-social or AI app (no friend graph) | `16-non-social-utility-and-ai-apps.md` first, then the rows above |
| Mature app with many users | `17-what-he-did-at-x.md`, `08-measurement-and-diagnosis.md` |
| New product inside a large company | `19-lessons-from-facebook.md`, then the rows above |

Always apply `12-positive-design-and-guardrails.md` (the guardrail pass table). To run the session
the way he runs his, follow `14-how-he-advises-founders.md`.

Templates to hand over: `templates/01-instrumentation-checklist.md` (Step 2),
`templates/05-validation-ladder-scorecard.md` (Step 3), `templates/02-48-hour-test-plan.md` (the
test), `templates/03-k-factor-worksheet.md` (invites and shares), `templates/04-invite-flow-teardown.md`
(friend-finding and invites), `templates/06-hoax-response-runbook.md` (rumours). A finished example
is in `examples/01-worked-example-growth-audit.md`.

## Step 5: Deliver the audit

```markdown
# Growth audit: [app]

**Rung:** [first unproven rung] · **Graph:** [friend / interest] · **Why:** [evidence or missing number]

## Instrumentation gaps (fix before trusting the numbers)
- ...

## Table stakes (fix first)
1. [Specific fix] · principle · ref: [file] · source: [ID]

## Step-function changes (2 to 3; pick one, then test it properly)
1. [Fundamental change] · expected effect · how to test it in one clean experiment

## The test
- What must be true: [one rung only]
- Setup that removes confounding variables: [density, support, polish]
- Signal agreed in advance: YES line, NO line, and the UNCLEAR band between them (our thresholds
  unless the founder has their own); read time (he usually knew within 48 hours [OOO 56:46])

## Guardrail pass
- [Each row of the chapter 12 table: pass or fix]

## What I could not assess
- [Missing data, and what to send next]
```

Rules for the audit:
- **Specific beats general.** *Move contact sync before the profile photo step*, not *improve
  onboarding*.
- **Count taps, predict conversions.** Estimate each screen's conversion before looking at data
  [OOO 15:25].
- **No silver bullet.** Look at every surface [OOO 1:04:50].
- **Say what is luck.** About half the companies he advises hit big success and half fail outright,
  "because consumer is so random." [LP 1:29:37]

## Refusals

No sending invites or messages a user did not knowingly send, no using contact data beyond what the
user agreed to, no fake social proof, no rating of real people's appearance, no mechanics that
pressure or shame minors, no AI companions for minors. See `12-positive-design-and-guardrails.md`.
His rule: "if you do the wrong thing by users, the internet will come back and get even and defend
itself." [LP 1:01:46]
