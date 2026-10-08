# 11 · Monetization and economics

## Charge for the most-requested thing

On tbh, "the number one support message we received was can i pay to reveal who sent me polls?" He
still asks whether monetizing "made even more than the acquisition" [LP 56:26]. In 2026:
"i always wondered, you know, like if we monetized it, would we have had to have sold?" [OOO 58:20]

Gas answered it with **God Mode**, an optional subscription that "gives users hints about who their
secret complimenters are" [TC3]. (We no longer give a price: the only source we had for it was
Wikipedia, which this repo uses for dates only.)

⚠️ **Conflict, how much Gas made:**
- Lenny: "$11 million in sales through the app"; Nikita: “yeah” [LP 1:09:57]
- Nikita: "it made $10 million in 90 days" [OOO 1:00:57]
- Sensor Tower, via TechCrunch: "almost $7 million in consumer spending" since launch [TC3]

## A founder's account of his pricing advice

Oleve co-founder Sid Bendre, on Nathan Latka's show, says Nikita told his co-founder to "switch to
weekly subscriptions and charge more or something like that." [NL 12:57] Second-hand and hedged by
the founder himself: an anecdote, not a rule.

## Know which kind of app you are building

In a 2024 post he splits apps into **durable apps**, built on repeat engagement, and **paywall-ad
arbitrage apps**, where the business model is "primarily people forgetting to cancel
subscriptions" and retention is close to nil. Either can make “life-changing money”, but he says the
last thing you should do is raise outside funding for the second type.
[X 2024-10-24](https://x.com/nikitabier/status/1849291216166289772)

## Run lean

- tbh: the team "purposefully kept its burn rate low to maximize its runway" (TechCrunch) and had
  “maybe 60 days left” before launch (the team) [TC1]. Office rent: $1,800 a month [LP 37:48].
- Gas: "the entire company was run on free startup credits too... there were no salaries."
  [OOO 1:00:57 to 1:01:08] He self-financed it for about $25,000 [OOO 1:01:19].
- His 2023 benchmark: when tbh hit what he calls 4 million daily users, burn excluding AWS was about
  $32,000 a month, and he asked every vendor for a 30% cut.
  [X 2023-12-23](https://x.com/nikitabier/status/1738688024253493290) ⚠️ TechCrunch reported 2.5
  million daily users and corrected its own “4 million” figure [TC2].

## Raising money for a social app `[2023]`

Valuation ranges he published in April 2023 for consumer social apps
[X 2023-04-18](https://x.com/nikitabier/status/1648324047111847936):

| Stage | His figure |
|---|---|
| No product, 1 to 2 engineers | $6M |
| Prototype | $12M |
| Launched, no traction | $8M |
| Launched and topping the charts | $80M to $150M |

How he pitched, from a 2024 post: hand investors a prototype, leave the room, have the team interact
with them in the app, then come back and talk vision. His point is that consumer products should
"speak for themselves".
[X 2024-07-03](https://x.com/nikitabier/status/1808546435836883032)

## Platform fees change the math `[2024]`

In January 2024 he worked through Apple's then-new EU fee terms and concluded he would never launch
an app in Europe. [X 2024-01-25](https://x.com/nikitabier/status/1750592825060921353) That was his
reading of the terms as announced then; re-check current terms before using it.

## Venture capital is optional

After an IPO and "seven rounds of dilution", many founders end up with amounts "pretty comparable to
what we get from our apps for 90 days of work." [LP 1:22:13] **His comparison.**

---

## How to apply it (our reading)

1. **Rank support requests** for the last 30 days. Is the top one something people would pay for?
2. **Tie the paid feature to a curiosity the free product creates** (*who picked me?*).
3. **Only test pay after rungs 1 to 3 hold** (chapter 04). Payment tests on a non-spreading app
   measure nothing useful.
4. **Decide which type you are**, durable or arbitrage, and fund accordingly.
5. **Write the burn per thousand daily users** and the vendor list you will renegotiate.

**Worked numbers (invented).** 200,000 weekly active users; 4% try a weekly $3.99 plan; 40% of those
keep it for 4 weeks. Month one revenue: 8,000 × $3.99 × (1 + 3 × 0.4) ≈ $70,000 gross, before store
fees. If retention is the thing paying for it, this is a durable app; if most revenue comes from
people who forget to cancel, it is his type B, and you should not raise venture money on it.

**Failure modes.**
- Charging before the app spreads.
- A paywall on the core action, which kills the loop that brings new users.
- Revenue that depends on forgotten cancellations, presented to investors as retention.

**Guardrails.** For minors: no paid *reveal* of who said what, no pressure to pay to see something
about yourself, and follow the app store and local rules on purchases by children. The God Mode
model only gave hints, and even that needs care with a teen audience (chapter 12).
