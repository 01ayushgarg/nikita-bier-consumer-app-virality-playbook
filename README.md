# Nikita Bier's Consumer App Virality Playbook

**An unofficial, fully sourced playbook and agent skill for making consumer apps go viral, built from
what Nikita Bier has said and written himself.**

Nikita Bier built 15 apps, 14 of which were duds, then two #1 apps in the US App Store: **tbh**
(acquired by Facebook in 2017) and **Gas** (acquired by Discord in 2023). He spent four years building
zero-to-one apps at Facebook, advised dozens of consumer startups, and was head of product at X from
July 2025 to August 2026.

> "With certainty, if you're good at your job, you can make an app grow and go viral."
> Nikita Bier, Lenny's Podcast, 2024

> ⚠️ **Unofficial.** This repo is not written, reviewed or endorsed by Nikita Bier, Lenny's Podcast,
> Lightspeed, TechCrunch or X. It is a summary in our own words with short, credited quotes. Every
> claim links to its source so you can check it.

---

## What's inside

### The playbook (read it like a book)

| # | Chapter | What you'll learn |
|---|---|---|
| 00 | [Who Nikita Bier is](references/00-who-is-nikita-bier.md) | Dated timeline, track record, his own caveats |
| 01 | [Finding the idea](references/01-idea.md) | Latent demand, the Sarahah signal, taboo ideas, 3 reasons people download apps |
| 02 | [Choosing the audience](references/02-audience.md) | Why teens, the 20%-per-year invite curve, "adults have no friends", social inflection points |
| 03 | [Testing like a scientist](references/03-testing.md) | Reproducible tests, the 48-hour read, removing confounders, against MVPs, time-boxed teams |
| 04 | [The validation ladder](references/04-validation-ladder.md) | Core flow → spreads → hops → pays; 100% on one thing |
| 05 | [Activation](references/05-activation.md) | Value in 3 seconds, the Dupe case, the "60% tax", predicting conversion |
| 06 | [Social graph, invites and naming](references/06-social-graph-and-invites.md) | Friendfinder, 70% contacts benchmark, one auth protocol, Crush vs Gas, iOS 18, interest graphs |
| 07 | [Distribution channels](references/07-distribution-channels.md) | The only two product channels, TikTok as a press bump, renaming, platform risk, App Store rank |
| 08 | [Measurement and diagnosis](references/08-measurement-and-diagnosis.md) | "How is it growing today?", instrumentation traps, guardrail metrics |
| 09 | [Breakout scale](references/09-breakout-scale.md) | PMF is binary, geofencing, everything breaks every 3 days |
| 10 | [Hoaxes and platform risk](references/10-hoax-and-platform-risk.md) | Make the hoax less viral than your app; being cut off by a platform |
| 11 | [Monetization and economics](references/11-monetization-and-economics.md) | Charge for the top support request, God Mode, running lean, platform fees |
| 12 | [Positive by design, and guardrails](references/12-positive-design-and-guardrails.md) | Positivity as the product, thinking like an adversary, what this skill refuses |
| 13 | [Building in public and posting](references/13-building-in-public-and-posting.md) | Audience as distribution, his daily-insight formula, previewing features |
| 14 | [How he advises founders](references/14-how-he-advises-founders.md) | His engagement step by step, pricing, public case studies |
| 15 | [The AI era](references/15-ai-era.md) | Cheap building, probabilistic products, LLMs as the new contact sync |
| 16 | [Non-social, utility and AI apps](references/16-non-social-utility-and-ai-apps.md) | What carries over when you don't have a friend graph, and what doesn't |
| 17 | [What he did at X](references/17-what-he-did-at-x.md) | xAI adviser, head of product (onboarding, links, country of origin, bots, creators, XChat, the rebuild), stepping back |

### Templates (fill these in)

| Template | Use it to |
|---|---|
| [01 Instrumentation checklist](templates/01-instrumentation-checklist.md) | Make sure your numbers are real before you act on them |
| [02 48-hour test plan](templates/02-48-hour-test-plan.md) | Design one clean test that gives a yes or no fast |
| [03 K-factor worksheet](templates/03-k-factor-worksheet.md) | Measure your viral coefficient and find the next bit of it |
| [04 Invite flow teardown](templates/04-invite-flow-teardown.md) | Score your friend-finding and invite flow, screen by screen |

### Worked example

[A full growth audit, start to finish](examples/01-worked-example-growth-audit.md): a fictional app with
invented numbers, run through the whole method so you can see what the output looks like.

### The agent skill

`SKILL.md` turns the playbook into a growth audit. Give your agent your app, your numbers and your
first 60 seconds of onboarding. It checks your instrumentation, finds the first unproven rung of the
validation ladder, runs the checks for that rung, and returns table stakes, 2 to 3 step-function
changes and one clean test, each tied to a principle and a source. See the worked example above.

## Install

Clone into your agent's skills folder. For Claude Code:

```bash
git clone https://github.com/01ayushgarg/nikita-bier-consumer-app-virality-playbook \
  ~/.claude/skills/nikita-bier-consumer-app-virality-playbook
```

Then ask: *"Run a growth audit on my app"*, *"why aren't my users inviting friends?"*, *"how should I
test this app idea?"*, or *"there's a rumour spreading about our app, what do we do?"*

Or just read the chapters above.

## How it stays honest

- **Every claim cites a source** by ID, with a timestamp for video and a link for posts.
- **Quotes are verbatim**, including his punctuation. Auto-caption errors are marked `[sic]`.
- **Who said it is labelled:** Nikita, the interviewer, someone Nikita is quoting, or "the team".
- **Dated advice is tagged** (`[2024]`, `[2025]`, `[2026]`) so you know what to re-check.
- **Conflicts are shown, not resolved silently.** For example, three different figures for Gas
  revenue. See `SOURCES.md`.
- **His unverified results are labelled as his claims.**
- **Second-hand summaries are excluded.** No blogs, Reddit threads, LinkedIn posts or "lessons from"
  videos.

---

## Sources

All accessed on 3 October 2026. Full details, labelling rules and the conflicts table are in
[`SOURCES.md`](SOURCES.md).

### Interviews and talks (Nikita in his own words)

1. **Lenny's Podcast**: "How to consistently go viral: Nikita Bier's playbook for winning at consumer
   apps", with Lenny Rachitsky, 25 Aug 2024. https://www.youtube.com/watch?v=bhnfZhJWCWY
2. **Out of Office (Lightspeed)**: "Nikita Bier Is Out Of Office", with Michael Mignano, 10 Feb 2026.
   https://www.youtube.com/watch?v=tF4j4LB-2rk
3. **Where It Happens** (Greg Isenberg, Sahil Bloom): "Will Meta Bounce Back? (with Nikita Bier)", Feb
   2022. https://www.youtube.com/watch?v=Rql6GZakVTI
4. **TBS CROSS DIG with Bloomberg**: interview with Nikita Bier as X head of product, 6 Jun 2026.
   https://www.youtube.com/watch?v=2fAIZ0tlQZc
5. **Solana Stories**: "Crash Course on Building Viral Consumer Apps featuring Nikita Bier", 22 Sep 2025.
   https://www.youtube.com/watch?v=8AGz4TC5a50
6. **SCET Berkeley**: "Nikita Bier", 7 Feb 2018 (2-minute clip). https://www.youtube.com/watch?v=flFOFtFQJmM

### Reporting

7. **TechCrunch**, Josh Constine: "How tbh hit #1 by turning anonymity positive", 22 Sep 2017.
   https://techcrunch.com/2017/09/22/tbh-app/
8. **TechCrunch**, Josh Constine: "Facebook acquires anonymous teen compliment app tbh, will let it run",
   16 Oct 2017. https://techcrunch.com/2017/10/16/facebook-acquires-anonymous-teen-compliment-app-tbh-will-let-it-run/
9. **Washington Post**, Taylor Lorenz: "How a viral teen app became the center of a sex trafficking hoax",
   9 Nov 2022. https://www.washingtonpost.com/technology/2022/11/09/debunking-gap-app-sex-trafficking-rumor/
10. **TechCrunch**, Amanda Silberling: "Discord acquires Gas, a compliments-based social media app for
    teens", 17 Jan 2023. https://techcrunch.com/2023/01/17/discord-acquires-gas-a-compliments-based-social-media-app-for-teens/
11. **TechCrunch**, Ivan Mehta: "Creator of Gas and tbh makes an app for disappearing photos via
    iMessage", 15 Jan 2025. https://techcrunch.com/2025/01/15/creator-of-gas-and-tbh-makes-an-app-for-disappearing-photos-via-imessage/
12. **TechCrunch**, Amanda Silberling: "Nikita Bier joins X as head of product: 'I've officially posted
    my way to the top'", 1 Jul 2025. https://techcrunch.com/2025/07/01/nikita-bier-joins-x-as-head-of-product-ive-officially-posted-my-way-to-the-top/
13. **Sources** (Alex Heath): "X wants its haters back", 11 Dec 2025 (free intro only).
    https://sources.news/p/x-wants-its-haters-back
14. **MediaPost**, Colin Kirkland: "X Head Of Product Steps Down, Becomes Advisor", 6 Aug 2026.
    https://www.mediapost.com/publications/article/417079/x-head-of-product-steps-down-becomes-advisor.html

### Founders he advised, in their own words

15. **Top Founders with Nathan Latka**: Sid Bendre of Oleve, 15 Jul 2025 (second-hand account of
    Nikita's pricing advice). https://www.youtube.com/watch?v=6b33IBE50Mo

### Reference

16. **Wikipedia**: "Tbh" (dates only). https://en.wikipedia.org/wiki/Tbh
17. **Wikipedia**: "Gas (app)" (dates and co-founders only). https://en.wikipedia.org/wiki/Gas_(app)
18. **Intro**: Nikita Bier's advisory listing. https://intro.co/NikitaBier

### Nikita's posts on X (@nikitabier), 72 posts, oldest first

- 2018-05-30 · https://x.com/nikitabier/status/1001666968917757952
- 2019-03-19 · https://x.com/nikitabier/status/1107871174413803520
- 2019-04-02 · https://x.com/nikitabier/status/1112886629910241280
- 2020-06-18 · https://x.com/nikitabier/status/1273437328866832384
- 2021-06-11 · https://x.com/nikitabier/status/1403498766737444865
- 2021-07-09 · https://x.com/nikitabier/status/1413392823630680071
- 2021-08-13 · https://x.com/nikitabier/status/1426229686175027201
- 2022-04-16 · https://x.com/nikitabier/status/1515118303420682240
- 2022-08-09 · https://x.com/nikitabier/status/1557132295714222080
- 2023-02-01 · https://x.com/nikitabier/status/1620821649888264195
- 2023-04-18 · https://x.com/nikitabier/status/1648324047111847936
- 2023-05-25 · https://x.com/nikitabier/status/1661733445163417601
- 2023-05-26 · https://x.com/nikitabier/status/1662100378500866049
- 2023-07-15 · https://x.com/nikitabier/status/1680336066325393408
- 2023-08-07 · https://x.com/nikitabier/status/1688538948514021376
- 2023-10-01 · https://x.com/nikitabier/status/1708513023990645011
- 2023-11-29 · https://x.com/nikitabier/status/1729676931858153501
- 2023-12-23 · https://x.com/nikitabier/status/1738688024253493290
- 2023-12-25 · https://x.com/nikitabier/status/1739083277053620418
- 2024-01-15 · https://x.com/nikitabier/status/1746756081194619066
- 2024-01-25 · https://x.com/nikitabier/status/1750592825060921353
- 2024-02-06 · https://x.com/nikitabier/status/1754896706880127185
- 2024-04-05 · https://x.com/nikitabier/status/1776045211220615193
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
- 2025-07-06 · https://x.com/nikitabier/status/1941655319198958039
- 2025-09-04 · https://x.com/nikitabier/status/1963498520805007470
- 2025-09-09 · https://x.com/nikitabier/status/1965421715732759000
- 2025-10-12 · https://x.com/nikitabier/status/1977446408136650785
- 2025-10-14 · https://x.com/nikitabier/status/1978132382868988310
- 2025-10-16 · https://x.com/nikitabier/status/1978930409296601166
- 2025-10-19 · https://x.com/nikitabier/status/1979994223224209709
- 2025-11-19 · https://x.com/nikitabier/status/1991016787543035907
- 2025-11-22 · https://x.com/nikitabier/status/1992335925322613127
- 2025-12-02 · https://x.com/nikitabier/status/1995990576391749850
- 2026-01-07 · https://x.com/nikitabier/status/2008805057849082018
- 2026-01-15 · https://x.com/nikitabier/status/2011825522817270230
- 2026-01-20 · https://x.com/nikitabier/status/2013410692444102793
- 2026-01-21 · https://x.com/nikitabier/status/2014079005025247240
- 2026-02-14 · https://x.com/nikitabier/status/2022496540275937525
- 2026-02-21 · https://x.com/nikitabier/status/2025092951014301841
- 2026-02-24 · https://x.com/nikitabier/status/2026107397044109347
- 2026-03-25 · https://x.com/nikitabier/status/2036603028619534564
- 2026-04-22 · https://x.com/nikitabier/status/2047041338106159484
- 2026-04-24 · https://x.com/nikitabier/status/2047747631624183889
- 2026-04-25 · https://x.com/nikitabier/status/2047909972990927255
- 2026-06-07 · https://x.com/nikitabier/status/2063767110736908757
- 2026-07-01 · https://x.com/nikitabier/status/2072203879479910490
- 2026-07-07 · https://x.com/nikitabier/status/2074341886333157582
- 2026-07-15 · https://x.com/nikitabier/status/2077479511202152728
- 2026-07-16 · https://x.com/nikitabier/status/2077774853650944028
- 2026-07-24 · https://x.com/nikitabier/status/2080747924380856519
- 2026-07-28 · https://x.com/nikitabier/status/2082140254237241588
- 2026-08-05 · https://x.com/nikitabier/status/2085105586966827343
- 2026-09-20 · https://x.com/nikitabier/status/2101763620954894647
- 2026-10-03 · https://x.com/nikitabier/status/2106208271778668930

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
