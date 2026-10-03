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

### The agent skill

`SKILL.md` turns the playbook into a growth audit. Give your agent your app, your numbers and your
first 60 seconds of onboarding. It checks your instrumentation, finds the first unproven rung of the
validation ladder, runs the checks for that rung, and returns table stakes, 2 to 3 step-function
changes and one clean test, each tied to a principle and a source.

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

### Long-form interviews (Nikita in his own words)

1. **Lenny's Podcast**: "How to consistently go viral: Nikita Bier's playbook for winning at consumer
   apps", with Lenny Rachitsky, 25 Aug 2024. https://www.youtube.com/watch?v=bhnfZhJWCWY
2. **Out of Office (Lightspeed)**: "Nikita Bier Is Out Of Office", with Michael Mignano, 10 Feb 2026.
   https://www.youtube.com/watch?v=tF4j4LB-2rk

### Reporting

3. **TechCrunch**, Josh Constine: "How tbh hit #1 by turning anonymity positive", 22 Sep 2017.
   https://techcrunch.com/2017/09/22/tbh-app/
4. **TechCrunch**, Josh Constine: "Facebook acquires anonymous teen compliment app tbh, will let it run",
   16 Oct 2017. https://techcrunch.com/2017/10/16/facebook-acquires-anonymous-teen-compliment-app-tbh-will-let-it-run/
5. **TechCrunch**, Amanda Silberling: "Discord acquires Gas, a compliments-based social media app for
   teens", 17 Jan 2023. https://techcrunch.com/2023/01/17/discord-acquires-gas-a-compliments-based-social-media-app-for-teens/
6. **TechCrunch**, Ivan Mehta: "Creator of Gas and tbh makes an app for disappearing photos via
   iMessage", 15 Jan 2025. https://techcrunch.com/2025/01/15/creator-of-gas-and-tbh-makes-an-app-for-disappearing-photos-via-imessage/
7. **TechCrunch**, Amanda Silberling: "Nikita Bier joins X as head of product: 'I've officially posted
   my way to the top'", 1 Jul 2025. https://techcrunch.com/2025/07/01/nikita-bier-joins-x-as-head-of-product-ive-officially-posted-my-way-to-the-top/
8. **Sources** (Alex Heath): "X wants its haters back", 11 Dec 2025 (free intro only).
   https://sources.news/p/x-wants-its-haters-back
9. **MediaPost**, Colin Kirkland: "X Head Of Product Steps Down, Becomes Advisor", 6 Aug 2026.
   https://www.mediapost.com/publications/article/417079/x-head-of-product-steps-down-becomes-advisor.html

### Reference

10. **Wikipedia**: "Tbh" (dates only). https://en.wikipedia.org/wiki/Tbh
11. **Wikipedia**: "Gas (app)" (dates and co-founders only). https://en.wikipedia.org/wiki/Gas_(app)
12. **Intro**: Nikita Bier's advisory listing. https://intro.co/NikitaBier

### Nikita's posts on X (34 posts, @nikitabier)

13. 2018-05-30 · the two questions every social app must answer · https://x.com/nikitabier/status/1001666968917757952
14. 2019-03-19 · why "meet up with friends" apps fail · https://x.com/nikitabier/status/1107871174413803520
15. 2019-04-02 · invites depend on age and social inflection points · https://x.com/nikitabier/status/1112886629910241280
16. 2021-06-11 · under 70% contacts access is "dead on arrival" · https://x.com/nikitabier/status/1403498766737444865
17. 2021-07-09 · assume you're wrong, build a pivot map · https://x.com/nikitabier/status/1413392823630680071
18. 2021-08-13 · dumb PM vs smart PM on funnels · https://x.com/nikitabier/status/1426229686175027201
19. 2022-08-09 · 0.99 vs 1.01 K-factor · https://x.com/nikitabier/status/1557132295714222080
20. 2023-05-25 · de-risk by changing only the interaction model · https://x.com/nikitabier/status/1661733445163417601
21. 2023-05-26 · one sign-in method on the same protocol as invites · https://x.com/nikitabier/status/1662100378500866049
22. 2023-08-07 · two types of growth people · https://x.com/nikitabier/status/1688538948514021376
23. 2023-10-01 · the 4-month viral app team · https://x.com/nikitabier/status/1708513023990645011
24. 2023-11-29 · satire on skipping contacts access · https://x.com/nikitabier/status/1729676931858153501
25. 2023-12-25 · don't apologise into a pile-on · https://x.com/nikitabier/status/1739083277053620418
26. 2024-01-25 · App Store fees in Europe · https://x.com/nikitabier/status/1750592825060921353
27. 2024-04-16 · rebuilding Flip's friendfinder · https://x.com/nikitabier/status/1780307682475549154
28. 2024-04-18 · don't dismiss taboo ideas · https://x.com/nikitabier/status/1780967619199467685
29. 2024-07-21 · what his $10k/month advisory covers · https://x.com/nikitabier/status/1815130311963168831
30. 2024-09-19 · "RIP Social Apps" after iOS 18; LLMs as the new contact sync · https://x.com/nikitabier/status/1836612494938509664
31. 2024-11-16 · against "minimum viable products" · https://x.com/nikitabier/status/1857896428317630893
32. 2025-02-08 · "adults have no friends" · https://x.com/nikitabier/status/1888375654850453743
33. 2025-02-18 · advising Protectors · https://x.com/nikitabier/status/1891685562412675284
34. 2025-02-25 · founders must own Mixpanel · https://x.com/nikitabier/status/1894468176584610053
35. 2025-05-10 · build for the network · https://x.com/nikitabier/status/1921278141122887970
36. 2025-05-11 · predicting push opt-in; product sense · https://x.com/nikitabier/status/1921708920181055975
37. 2025-05-15 · interest graphs are hard to activate · https://x.com/nikitabier/status/1922864090277392756
38. 2025-05-21 · the "60% tax" of sound-on sign-up · https://x.com/nikitabier/status/1925179335180197902
39. 2025-09-04 · one insight a day for 6 months · https://x.com/nikitabier/status/1963498520805007470
40. 2025-09-09 · App Store rank counts first-time downloads only · https://x.com/nikitabier/status/1965421715732759000
41. 2026-01-20 · new-user ramp is X's key growth lever · https://x.com/nikitabier/status/2013410692444102793
42. 2026-02-21 · "I really quit the viral app business just in time" · https://x.com/nikitabier/status/2025092951014301841
43. 2026-07-07 · original content as the arbitrage on X · https://x.com/nikitabier/status/2074341886333157582
44. 2026-07-28 · software as self-expression · https://x.com/nikitabier/status/2082140254237241588
45. 2026-08-05 · stepping back from leading product at X · https://x.com/nikitabier/status/2085105586966827343
46. 2026-09-20 · deterministic vs probabilistic products · https://x.com/nikitabier/status/2101763620954894647

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
