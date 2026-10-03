# Template 01 · Instrumentation checklist

Fill this in **before** trusting any growth number. Based on chapter 08
(`references/08-measurement-and-diagnosis.md`).

> "It starts with just instrumentation and uh knowing knowing what's happening through the whole
> thing." Nikita Bier [OOO 1:07:29]

App: ______________________  Analytics tool: ______________  Date: __________

## A. Is the data clean? (the three traps he sees "almost everyday" [X 2025-02-25])

| # | Check | Yes / No | Notes |
|---|---|---|---|
| A1 | Internal, team and test devices are filtered out of every funnel | | |
| A2 | Debug and staging builds send no events to production analytics | | |
| A3 | Logged-out users are tracked (anonymous ID before sign-up, merged after) | | |
| A4 | "Shared" and "invited" are counted at the **final send event**, not the tap on the button | | |
| A5 | Someone has watched at least 10 individual sessions at the biggest drop-off this week | | |

## B. Can you answer "how is it growing today?" [OOO 1:08:12]

| # | Check | Yes / No | Answer |
|---|---|---|---|
| B1 | Every install is attributed to a source (invite, share, organic search, ads, press, unknown) | | |
| B2 | Top 3 sources of downloads this month, by share | | 1. ___ 2. ___ 3. ___ |
| B3 | % of installs that are "unknown" source | | ___ % |

## C. The funnel, step by step (every step instrumented)

Write each screen a new user sees, in order. Predict conversion **before** looking at the data
(product sense, per [X 2025-05-11]), then fill in the actual number.

| Step | Screen / event | Predicted % | Actual % | Biggest surprise |
|---|---|---|---|---|
| 1 | Store page view → install | | | |
| 2 | First open | | | |
| 3 | Sign-up started | | | |
| 4 | Sign-up completed | | | |
| 5 | Permission (contacts / notifications) granted | | | |
| 6 | First moment of value ("aha") | | | |
| 7 | First invite or share **sent** | | | |
| 8 | Day-1 return | | | |

## D. The two growth channels [OOO 1:05:46]

| Channel | Event tracked end to end? | Rate |
|---|---|---|
| One-to-one invites (referrals) | | invites sent per new user: ___ · accepted: ___ % |
| One-to-many sharing (stories, posts, links) | | shares per new user: ___ · installs per share: ___ |

## E. Guardrail for the next change [OOO 38:05]

The metric that must stay flat or better for the next change to ship: ____________________

**Done when** every row in A is "Yes" and B2 is filled in from data, not from memory.
