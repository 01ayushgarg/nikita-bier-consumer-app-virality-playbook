# Consumer Virality Playbook

An agent skill that audits a consumer app for viral growth using the playbook
**Nikita Bier** described on [Lenny's Podcast](https://www.youtube.com/watch?v=bhnfZhJWCWY)
(August 2024): 15 apps, 14 duds, then two #1 apps in the US App Store, tbh (sold to Facebook)
and Gas (sold to Discord).

> "With certainty, if you're good at your job, you can make an app grow and go viral."
> Nikita Bier

## What it does

Give your agent your app, your numbers and your first 60 seconds of onboarding. The skill:

1. **Places you on the validation ladder:** core flow works → spreads inside a group →
   hops between groups → people pay. Only the first unproven rung gets worked on.
2. **Runs the checks for that rung:** latent demand, audience and the invite curve, test design,
   time to value, invite flow and naming, funnel alignment, breakout scale, hoax defense, monetization.
3. **Returns an audit:** table stakes to fix first, then 2 to 3 step-function changes and one
   clean test to run, each tied to a principle and a timestamp in the source.

## What's inside

```
SKILL.md                         the workflow the agent follows
references/
  01-idea.md                     latent demand, the 3 reasons people download apps
  02-audience.md                 why teens, the 20%-per-year invite curve, density
  03-testing.md                  reproducible testing, removing confounding variables, seeding
  04-validation-ladder.md        the four rungs, 100% on one thing
  05-activation.md               value in 3 seconds, 10,000 taps vs one, the Dupe case
  06-invites-and-naming.md       Crush vs Gas, invites users send knowingly, iOS 18 contacts
  07-funnel-alignment.md         marketing and product are one funnel
  08-breakout-scale.md           PMF is binary, geofencing, everything breaks every 3 days
  09-hoax-defense.md             make the hoax less viral than your app
  10-monetization.md             charge for the most-requested thing
  11-guardrails.md               by the book, positive-only design, what the skill refuses
SOURCES.md                       the source and how claims are cited
```

## Install

Copy the folder into your agent's skills directory, for example for Claude Code:

```bash
git clone https://github.com/01ayushgarg/consumer-virality-playbook ~/.claude/skills/consumer-virality-playbook
```

Then ask: *"Run a growth audit on my app"*, *"why aren't my users inviting friends?"*, or
*"there's a rumour spreading about our app, what do we do?"*

## How it stays honest

- Every principle cites a timestamp in the episode. Nothing is attributed to Nikita that he did not say.
- Lenny's figures and lines Nikita relays from others are labelled as such.
- Dated advice (App Store #1 thresholds, iOS 18 contact permissions) is marked `[2024]`.
- Nikita's own caveat is kept: growth can be a science, durability is mostly luck.

## Credit

All ideas belong to Nikita Bier ([@nikitabier](https://x.com/nikitabier)), from his conversation
with Lenny Rachitsky on Lenny's Podcast. This is an independent, unofficial summary in our own
words with short attributed quotes. It is not endorsed by Nikita Bier or Lenny's Podcast.
Watch the full episode; it is worth it.

## License

MIT for the skill text and structure. Quotes remain the words of their speakers.
