---
name: consumer-virality-playbook
description: Audit and design a consumer app for viral growth using the playbook Nikita Bier (tbh, sold to Facebook; Gas, sold to Discord) described on Lenny's Podcast. Use when someone wants their consumer or social app to grow by itself, asks why their app is not spreading, wants a growth audit, is choosing an app idea or audience, designing onboarding, invites, contact sync or app naming, planning a launch test, handling breakout growth, or fighting a viral rumour about their app. Triggers on "make my app go viral", "growth audit", "why aren't users inviting friends", "how do I test this app idea", "time to value", "activation", "k-factor", "invite flow", "our app is blowing up", "there's a hoax about our app".
---

# Consumer Virality Playbook

A working method for making consumer apps spread, built from Nikita Bier's own account of
building 15 apps, 14 duds, and then two #1 apps in the US App Store (tbh and Gas).

> "With certainty, if you're good at your job, you can make an app grow and go viral." (1:19:21)
> "Retention for consumer social... there's a tremendous amount of randomness." (1:19:00)

**Hold both.** Growth is treated here as a science. Durability is not promised by anything in
this skill. Say so to the user when it matters.

Every principle in `references/` carries a timestamp into the source episode
(see `SOURCES.md`). Quote from there; never attribute anything to Nikita that is not in it.

---

## Step 1: Intake (ask only what you cannot see)

Get, from the user or their materials:

1. **What the app does** in one sentence, and the core action a user repeats.
2. **Who it is for**, with age. Age changes everything here (see `references/02-audience.md`).
3. **Stage:** idea, prototype, launched, or growing.
4. **Numbers they have:** installs per day, % of new users who invite, invites per inviter,
   day-1 core actions per user, activation rate, retention. Missing numbers are a finding, not a blocker.
5. **How users arrive today:** ads, organic, invites, shares, press.
6. **The first 60 seconds:** what a new user sees and taps, screen by screen.

Nikita's own first move with a company: "I ask them to show me the analytics. We look at how
people are distributing the app today, what is the milestone that a user must hit to become
activated and what's getting in the way of that?" (1:32:44)

## Step 2: Place them on the validation ladder

Read `references/04-validation-ladder.md`. Find the FIRST rung that is not yet proven:

```
core flow works  →  spreads inside a group  →  hops between groups  →  people pay
```

Everything in the audit is aimed at that rung. Work on later rungs is scope creep: "execute at
100% for the thing you're trying to validate... and then you can kind of half-ass the rest." (1:11:50)

## Step 3: Run the checks for that rung

| Stuck on | Load these references |
|---|---|
| No idea yet, or idea in doubt | `01-idea.md`, `02-audience.md` |
| Core flow (users don't use it) | `05-activation.md`, `03-testing.md` |
| Spreading inside a group | `06-invites-and-naming.md`, `07-funnel-alignment.md`, `03-testing.md` |
| Hopping between groups | `06-invites-and-naming.md`, `07-funnel-alignment.md` |
| People pay | `10-monetization.md` |
| It's working and breaking | `08-breakout-scale.md` |
| A rumour or hoax is spreading | `09-hoax-defense.md` (treat as urgent, skip the ladder) |

Always also apply `11-guardrails.md`. It is not optional.

## Step 4: Deliver the audit

Use this shape. It mirrors how Nikita describes his own engagements (1:35:03): clear the table
stakes, then name 2 to 3 step-function changes.

```markdown
# Growth audit: [app]

**Rung:** [the first unproven rung] · **Why:** [the evidence, or the missing number]

## Table stakes (fix first)
1. [Specific fix] · principle: [name] · ref: [file]
...

## Step-function changes (pick one, then test it properly)
1. [Fundamental change to the product] · expected effect · how to test it in one clean experiment
2. ...

## The test
- What must be true: [the condition, one rung only]
- Setup that removes confounding variables: [density, support, etc.]
- Signal that says yes / no: [metric and threshold the user agrees in advance]

## What I could not assess
- [Missing data, and what to send next]
```

Rules for the audit:
- **Specific beats general.** "Move contact sync before the profile photo step" not "improve onboarding".
- **Count taps.** Where a flow is in question, count the taps. "Every tap that you get, every single one is so scarce." (14:52)
- **Quote the playbook, cite the timestamp.** Never invent a statistic, benchmark or quote.
- **Date-stamp the dated.** Anything marked `[2024]` in references (App Store thresholds, iOS 18
  contact permissions) must be presented as of 2024 and flagged for re-checking.
- **Say what is luck.** Nikita estimates about half the companies he works with hit big
  success and half fail outright, "because consumer is so random." (1:29:28)

## Refusals

This skill does not help anyone send invites or messages a user did not knowingly send, use
contact data in ways users did not agree to, fake social proof, or build mechanics that harm
minors. See `references/11-guardrails.md`. Nikita's own rule: "if you do the wrong thing by
users, the internet will come back and get even." (1:01:48)
