# Nikita Bier's Consumer App Virality Playbook

**An unofficial, fully sourced playbook and agent skill for making consumer apps go viral, built from
what Nikita Bier has said and written himself.**

Nikita Bier built 15 apps, 14 of which were duds, then two #1 apps in the US App Store: **tbh**
(acquired by Facebook in 2017) and **Gas** (acquired by Discord in 2023). He spent four years building
zero-to-one apps at Facebook, advised dozens of consumer startups, and was head of product at X from
mid-2025 (announced 30 June 2025) to 5 August 2026.

> "With certainty, if you're good at your job, you can make an app grow and go viral."
> Nikita Bier, Lenny's Podcast, 2024 [LP 1:19:27]

> ⚠️ **Unofficial.** This repo is not written, reviewed or endorsed by Nikita Bier, Lenny's Podcast,
> Lightspeed, TechCrunch or X. It is a summary in our own words with short, credited quotes. Every
> claim links to its source so you can check it. It covers his product and growth methods only.

---

## What's new in v2

- **Accuracy:** every Lenny's Podcast quote and timestamp re-checked against the official
  transcript; dates fixed (joining X, Custom Timelines); misreadings fixed (the X revenue-share
  experiment, the 20% invite heuristic is the host's reading); unmarked trims marked.
- **Copyright hygiene:** no quote over 60 words; posts on X are now mostly paraphrased with short
  quoted phrases; fewer quotes overall.
- **Depth:** every chapter ends with *How to apply it (our reading)*: steps, a worked scenario with
  invented numbers, failure modes and limits. The validation ladder chapter is rebuilt as a method.
- **New:** a one-page [benchmarks table](references/benchmarks.md), chapter 18 (shareable content and
  notifications), chapter 19 (what he learned at Facebook), templates 05 (ladder scorecard) and 06
  (hoax runbook). Chapter 17 (X) is cut to the founder lessons.
- **Guardrails:** explicit notes on rating mechanics, minors and AI companions.

## What's inside

### The playbook (read it like a book)

| # | Chapter | What you'll learn |
|---|---|---|
| ★ | [Benchmarks](references/benchmarks.md) | Every number in the playbook, dated and sourced, on one page |
| 00 | [Who Nikita Bier is](references/00-who-is-nikita-bier.md) | Dated timeline, track record, his own caveats |
| 01 | [Finding the idea](references/01-idea.md) | Latent demand, the Sarahah signal, the positive version of taboo ideas, 3 reasons people download apps |
| 02 | [Choosing the audience](references/02-audience.md) | Why teens, the invite curve, social inflection points, an audience score |
| 03 | [Testing like a scientist](references/03-testing.md) | Reproducible tests, the 48-hour read, removing confounders, against MVPs |
| 04 | [The validation ladder](references/04-validation-ladder.md) | Core flow → spreads → hops → pays, as a step-by-step method |
| 05 | [Activation](references/05-activation.md) | Value in 3 seconds, the Dupe case, predicting conversion, the activation walk |
| 06 | [Social graph, invites and naming](references/06-social-graph-and-invites.md) | Friendfinder, contacts benchmarks, one sign-in protocol, Crush vs Gas, iOS 18 |
| 07 | [Distribution channels](references/07-distribution-channels.md) | The two product channels, TikTok as a press bump, renaming, platform risk |
| 08 | [Measurement and diagnosis](references/08-measurement-and-diagnosis.md) | How is it growing today, instrumentation traps, guardrail metrics |
| 09 | [Breakout scale](references/09-breakout-scale.md) | PMF is binary, geofencing, everything breaks every 3 days, a breakout runbook |
| 10 | [Hoaxes and platform risk](references/10-hoax-and-platform-risk.md) | Make the hoax less viral than your app; being cut off by a platform |
| 11 | [Monetization and economics](references/11-monetization-and-economics.md) | Charge for the top support request, durable vs arbitrage apps, running lean |
| 12 | [Positive by design, and guardrails](references/12-positive-design-and-guardrails.md) | Positivity as the product, thinking like an adversary, the guardrail pass |
| 13 | [Building in public and posting](references/13-building-in-public-and-posting.md) | Audience as distribution, his daily-insight formula, previewing features |
| 14 | [How he advises founders](references/14-how-he-advises-founders.md) | His engagement step by step, a session plan, public case studies |
| 15 | [The AI era](references/15-ai-era.md) | Cheap building, probabilistic products, LLMs and activation, with guardrails |
| 16 | [Non-social, utility and AI apps](references/16-non-social-utility-and-ai-apps.md) | What carries over without a friend graph, and what doesn't |
| 17 | [What he did at X](references/17-what-he-did-at-x.md) | Five founder lessons from running product on a mature app |
| 18 | [Shareable content and notifications](references/18-shareable-content-and-notifications.md) | Spotify Wrapped syndrome, sharing as the main surface, notification loops |
| 19 | [What he learned at Facebook](references/19-lessons-from-facebook.md) | The science of growth, PMs far from the pixels, why new apps are hard inside big companies |

### Templates (fill these in)

| Template | Use it to |
|---|---|
| [01 Instrumentation checklist](templates/01-instrumentation-checklist.md) | Make sure your numbers are real before you act on them |
| [02 48-hour test plan](templates/02-48-hour-test-plan.md) | Design one clean test with YES, NO and UNCLEAR lines agreed in advance |
| [03 K-factor worksheet](templates/03-k-factor-worksheet.md) | Measure your viral coefficient and find the next bit of it |
| [04 Invite flow teardown](templates/04-invite-flow-teardown.md) | Score your friend-finding and invite flow, screen by screen |
| [05 Validation ladder scorecard](templates/05-validation-ladder-scorecard.md) | Find the first unproven rung and stop work above it |
| [06 Hoax response runbook](templates/06-hoax-response-runbook.md) | Be ready for a rumour before it starts |

### Worked example

[A full growth audit, start to finish](examples/01-worked-example-growth-audit.md): a fictional app with
invented numbers, run through the whole method so you can see what the output looks like.

### The agent skill

`SKILL.md` turns the playbook into a growth audit. Give your agent your app, your numbers and your
first 60 seconds of onboarding. It reads the benchmarks, checks your instrumentation, finds the first
unproven rung of the validation ladder, runs the checks for that rung, and returns table stakes, 2 to
3 step-function changes, one clean test and a guardrail pass, each tied to a principle and a source.

## How to use this

There are three ways in. Pick the one that fits how much time you have.

### 1. Run it as an AI skill (10 minutes, the full audit)

**Step 1: install.** Clone it into your agent's skills folder. For Claude Code:

```bash
git clone https://github.com/01ayushgarg/nikita-bier-consumer-app-virality-playbook \
  ~/.claude/skills/nikita-bier-consumer-app-virality-playbook
```

Any agent that reads skill folders (a folder with a `SKILL.md`) works the same way. If yours doesn't,
paste `SKILL.md` into the chat and attach `references/benchmarks.md` plus the `references/` files it
asks for.

**Step 2: give it your app.** The more you give, the sharper the audit. Copy this and fill it in:

```text
Run the Nikita Bier playbook audit on my app.

App: [name + link]
What it does: [one sentence, and the action users repeat]
Who it's for: [who, and their age]
Stage: [idea / prototype / launched / growing]
Numbers (whatever you have):
- installs or sign-ups per day, and where they come from
- sign-up completion %
- contacts and push permission %
- % of new users who invite or share, and how many each
- % of invites or shares that turn into a new user
- day-1 and day-7 retention
First 60 seconds: [every screen a new user sees, in order]
```

No numbers yet? Say so. The skill will audit what it can see, mark what it couldn't measure, and tell
you exactly what to track first.

**Step 3: read the audit.** You get back:

1. **Where you're stuck:** the first unproven step of the ladder (core flow → spreads in a group →
   hops between groups → people pay)
2. **Tracking gaps** to fix before trusting your numbers
3. **Table stakes:** the basic fixes first
4. **2 to 3 step-function changes:** the bigger bets
5. **One clean test** with YES, NO and UNCLEAR lines agreed before you run it
6. **A guardrail pass** on every recommendation
7. **What it couldn't assess**, and what to send next

Every recommendation cites the chapter and the source it comes from. Thresholds that are ours, not
his, are labelled. See the [worked example](examples/01-worked-example-growth-audit.md).

**Other things you can ask it:**

- *Why aren't my users inviting friends?*
- *How should I test this app idea in 48 hours?*
- *Score my invite flow.*
- *Calculate my K-factor from these numbers.*
- *Should I rename my app?*
- *Our share feature spiked once and died. Why?*
- *There's a rumour spreading about our app. What do we do?*
- *My app isn't social. What still applies?*

### 2. Use the templates (30 minutes, no AI needed)

Work through them in order, on your own or with your team:

1. [Instrumentation checklist](templates/01-instrumentation-checklist.md): make sure your numbers are real
2. [Validation ladder scorecard](templates/05-validation-ladder-scorecard.md): find the rung you're stuck on
3. [Invite flow teardown](templates/04-invite-flow-teardown.md): score your flow out of 24
4. [K-factor worksheet](templates/03-k-factor-worksheet.md): measure how much your users bring in others
5. [48-hour test plan](templates/02-48-hour-test-plan.md): design one test for your biggest gap

Keep [the hoax runbook](templates/06-hoax-response-runbook.md) filled in and on file.

### 3. Read it (an hour)

Start with [the benchmarks](references/benchmarks.md) and [00 Who Nikita Bier is](references/00-who-is-nikita-bier.md),
then read the chapter for your problem:

| If your problem is... | Read |
|---|---|
| *I don't know what to build* | 01, 02 |
| *People sign up but don't stick* | 05, 04 |
| *Nobody invites anyone* | 06, 07 |
| *Nobody shares anything* | 18, 07 |
| *I don't know if it's working* | 08, 03 |
| *It's working and everything is breaking* | 09 |
| *There's a hoax about us* | 10 |
| *How do I make money from it?* | 11 |
| *My app isn't social* | 16 |
| *We're a big company starting something new* | 19, 17 |

**A word of caution from the man himself:** about half the startups he advises hit big success and
half fail outright, "because consumer is so random." [LP 1:29:37] Use this to raise your odds, not to
promise an outcome.

## How it stays honest

- **Every claim cites a source** by ID, with a timestamp for audio and video and a link for posts.
- **What was checked, and how.** Before release we downloaded every source's text (the official
  Lenny's Podcast transcript, YouTube auto-captions for the other videos, post text from the public
  fxtwitter API, and the articles) and ran two scripts over the repo: one checks that every quoted
  passage is an exact substring of that text, allowing only quote-mark and whitespace differences
  (and `...` between exact fragments); the other checks that each quote is found in the specific
  source its ID points to and that timestamps are within about 20 seconds. Those scripts depend on our
  local copies of the sources, so they are not shipped; anyone can repeat the check by hand from the
  links in `SOURCES.md`.
- **Auto-captions are labelled as such.** About a quarter of the citations (Out of Office, Where It
  Happens, TBS, Solana Stories, the SCET clip) rest on YouTube auto-captions. Quotes match those
  captions, but the captions were not checked against the audio. Obvious caption errors are marked
  `[sic]`.
- **No quote is over 60 words**, and short works such as posts on X are mostly paraphrased.
- **Who said it is labelled:** Nikita, the interviewer, someone Nikita is quoting, or *the team*.
- **Ours is labelled as ours.** Methods, thresholds and example numbers in the *How to apply it*
  sections are marked *our reading*, *our suggestion* or *invented*.
- **Dated advice is tagged** (`[2021]`, `[2024]`, `[2026]`) so you know what to re-check.
- **Conflicts are shown, not resolved silently.** For example, three different figures for Gas
  revenue. See `SOURCES.md`.
- **His unverified results are labelled as his claims.**
- **Second-hand summaries are excluded.** No blogs, Reddit threads, LinkedIn posts or *lessons from*
  videos. Reporting is used for facts and is labelled as secondary.

---

## Sources

Accessed 3 to 7 October 2026. Full details, caveats, labelling rules and the conflicts table are in
[`SOURCES.md`](SOURCES.md).

### Interviews and talks (Nikita in his own words)

1. **Lenny's Podcast**: How to consistently go viral: Nikita Bier's playbook for winning at consumer
   apps, with Lenny Rachitsky, 25 Aug 2024. Official transcript:
   https://www.lennysnewsletter.com/p/how-to-consistently-go-viral-nikita-bier · Video:
   https://www.youtube.com/watch?v=bhnfZhJWCWY
2. **Out of Office (Lightspeed)**: Nikita Bier Is Out Of Office, with Michael Mignano, 10 Feb 2026
   (auto-captions). https://www.youtube.com/watch?v=tF4j4LB-2rk
3. **Where It Happens** (Greg Isenberg, Sahil Bloom): Will Meta Bounce Back? (with Nikita Bier), Feb
   2022 (auto-captions). https://www.youtube.com/watch?v=Rql6GZakVTI
4. **TBS CROSS DIG with Bloomberg**: interview with Nikita Bier as X head of product, 6 Jun 2026
   (auto-captions). https://www.youtube.com/watch?v=2fAIZ0tlQZc
5. **Solana Stories**: Crash Course on Building Viral Consumer Apps featuring Nikita Bier, 22 Sep 2025
   (auto-captions). https://www.youtube.com/watch?v=8AGz4TC5a50
6. **SCET Berkeley**: Nikita Bier, Feb 2018 (2-minute clip, captions). https://www.youtube.com/watch?v=flFOFtFQJmM

### Reporting (secondary)

7. **UC Berkeley SCET**, Jessica Lynn: How to build a viral app: TBH founder gives startup advice at UC
   Berkeley, 2 Feb 2018. https://scet.berkeley.edu/how-to-build-a-viral-app-tbh-founder-gives-advice-at-berkeley/
8. **TechCrunch**, Josh Constine: How tbh hit #1 by turning anonymity positive, 22 Sep 2017.
   https://techcrunch.com/2017/09/22/tbh-app/
9. **TechCrunch**, Josh Constine: Facebook acquires anonymous teen compliment app tbh, will let it run,
   16 Oct 2017. https://techcrunch.com/2017/10/16/facebook-acquires-anonymous-teen-compliment-app-tbh-will-let-it-run/
10. **Washington Post**, Taylor Lorenz: How a viral teen app became the center of a sex trafficking
    hoax, 9 Nov 2022. Archive: https://web.archive.org/web/20230101030921/https://www.washingtonpost.com/technology/2022/11/09/debunking-gap-app-sex-trafficking-rumor/
11. **TechCrunch**, Amanda Silberling: Discord acquires Gas, a compliments-based social media app for
    teens, 17 Jan 2023. https://techcrunch.com/2023/01/17/discord-acquires-gas-a-compliments-based-social-media-app-for-teens/
12. **TechCrunch**, Ivan Mehta: Creator of Gas and tbh makes an app for disappearing photos via
    iMessage, 15 Jan 2025. https://techcrunch.com/2025/01/15/creator-of-gas-and-tbh-makes-an-app-for-disappearing-photos-via-imessage/
13. **TechCrunch**, Amanda Silberling: Nikita Bier joins X as head of product, 1 Jul 2025.
    https://techcrunch.com/2025/07/01/nikita-bier-joins-x-as-head-of-product-ive-officially-posted-my-way-to-the-top/
14. **Sources** (Alex Heath): X wants its haters back, 12 Dec 2025 (free intro only).
    https://sources.news/p/x-wants-its-haters-back
15. **TechCrunch**: Nikita Bier steps down as X's head of product, 5 Aug 2026.
    https://techcrunch.com/2026/08/05/nikita-bier-steps-down-as-xs-head-of-product/
16. **MediaPost**, Colin Kirkland: X Head Of Product Steps Down, Becomes Advisor, 6 Aug 2026.
    https://www.mediapost.com/publications/article/417079/x-head-of-product-steps-down-becomes-advisor.html

### Founders he advised, in their own words

17. **Top Founders with Nathan Latka**: Sid Bendre of Oleve, 15 Jul 2025 (second-hand account of
    Nikita's pricing advice). https://www.youtube.com/watch?v=6b33IBE50Mo

### Reference

18. **Wikipedia**: Tbh (dates only). https://en.wikipedia.org/wiki/Tbh
19. **Wikipedia**: Gas (app) (dates only). https://en.wikipedia.org/wiki/Gas_%28app%29
20. **Intro**: Nikita Bier's advisory listing. https://intro.co/NikitaBier

### Nikita's posts on X (@nikitabier), 55 posts, oldest first

- 2018-05-30 · https://x.com/nikitabier/status/1001666968917757952
- 2019-03-19 · https://x.com/nikitabier/status/1107871174413803520
- 2019-04-02 · https://x.com/nikitabier/status/1112886629910241280
- 2020-06-18 · https://x.com/nikitabier/status/1273437328866832384
- 2021-06-11 · https://x.com/nikitabier/status/1403498766737444865
- 2021-07-09 · https://x.com/nikitabier/status/1413392823630680071
- 2021-08-13 · https://x.com/nikitabier/status/1426229686175027201
- 2022-08-02 · https://x.com/nikitabier/status/1554491978112389121
- 2022-08-09 · https://x.com/nikitabier/status/1557132295714222080
- 2023-01-23 · https://x.com/nikitabier/status/1617590526353764353
- 2023-02-01 · https://x.com/nikitabier/status/1620821649888264195
- 2023-04-18 · https://x.com/nikitabier/status/1648324047111847936
- 2023-05-25 · https://x.com/nikitabier/status/1661733445163417601
- 2023-05-26 · https://x.com/nikitabier/status/1662100378500866049
- 2023-07-15 · https://x.com/nikitabier/status/1680336066325393408
- 2023-08-07 · https://x.com/nikitabier/status/1688538948514021376
- 2023-10-01 · https://x.com/nikitabier/status/1708513023990645011
- 2023-11-29 · https://x.com/nikitabier/status/1729676931858153501
- 2023-12-16 · https://x.com/nikitabier/status/1736067506442326102
- 2023-12-23 · https://x.com/nikitabier/status/1738688024253493290
- 2023-12-25 · https://x.com/nikitabier/status/1739083277053620418
- 2024-01-15 · https://x.com/nikitabier/status/1746756081194619066
- 2024-01-25 · https://x.com/nikitabier/status/1750592825060921353
- 2024-02-06 · https://x.com/nikitabier/status/1754896706880127185
- 2024-04-16 · https://x.com/nikitabier/status/1780307682475549154
- 2024-04-18 · https://x.com/nikitabier/status/1780967619199467685
- 2024-06-21 · https://x.com/nikitabier/status/1804214914472644975
- 2024-07-03 · https://x.com/nikitabier/status/1808546435836883032
- 2024-07-21 · https://x.com/nikitabier/status/1815130311963168831
- 2024-08-16 · https://x.com/nikitabier/status/1824491565622104552
- 2024-09-19 · https://x.com/nikitabier/status/1836612494938509664
- 2024-10-24 · https://x.com/nikitabier/status/1849291216166289772
- 2024-11-15 · https://x.com/nikitabier/status/1857293213624582551
- 2024-11-16 · https://x.com/nikitabier/status/1857896428317630893
- 2025-02-08 · https://x.com/nikitabier/status/1888375654850453743
- 2025-02-18 · https://x.com/nikitabier/status/1891685562412675284
- 2025-02-25 · https://x.com/nikitabier/status/1894468176584610053
- 2025-05-10 · https://x.com/nikitabier/status/1921278141122887970
- 2025-05-11 · https://x.com/nikitabier/status/1921708920181055975
- 2025-05-15 · https://x.com/nikitabier/status/1922864090277392756
- 2025-05-21 · https://x.com/nikitabier/status/1925179335180197902
- 2025-05-24 · https://x.com/nikitabier/status/1926295017619939743
- 2025-06-30 · https://x.com/nikitabier/status/1939723101723574703
- 2025-09-04 · https://x.com/nikitabier/status/1963498520805007470
- 2025-09-09 · https://x.com/nikitabier/status/1965421715732759000
- 2025-10-19 · https://x.com/nikitabier/status/1979994223224209709
- 2026-01-20 · https://x.com/nikitabier/status/2013410692444102793
- 2026-02-21 · https://x.com/nikitabier/status/2025092951014301841
- 2026-04-21 · https://x.com/nikitabier/status/2046736181002645520
- 2026-04-25 · https://x.com/nikitabier/status/2047909972990927255
- 2026-07-01 · https://x.com/nikitabier/status/2072203879479910490
- 2026-07-07 · https://x.com/nikitabier/status/2074341886333157582
- 2026-07-28 · https://x.com/nikitabier/status/2082140254237241588
- 2026-08-05 · https://x.com/nikitabier/status/2085105586966827343
- 2026-09-20 · https://x.com/nikitabier/status/2101763620954894647

---

## License

- **Our text** (the chapters, the skill and the structure) is licensed under
  [Creative Commons Attribution 4.0 (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).
  Share and adapt it with credit.
- **Quotes** remain the words of their speakers (Nikita Bier and others) and the publications that
  recorded them. They are included as short, credited excerpts for commentary and are **not** covered
  by this license.
- Names and trademarks belong to their owners.

See [`LICENSE`](LICENSE).

## Corrections

If you spot a misquote, a wrong date or a broken link, open an issue with the source. Accuracy is the
point of this repo.
