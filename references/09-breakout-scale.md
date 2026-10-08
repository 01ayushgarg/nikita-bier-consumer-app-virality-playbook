# 09 · When it works: breakout scale

## Product-market fit is binary

Nikita relays a line from founder Roger Dickey: "if your product's working, you'll know. and if
there's any uncertainty, it's not working." [LP 36:12] His own addition: "it really is a binary when
it comes to consumer products." People fight to get in, and you invent new metrics; tbh's was
"hourly actives per day" [LP 36:29 to 36:36].

## What breakout looked like on tbh

- One school sent 450,000 messages in its first seven days [LP 28:35].
- On a messaging app's first day "you're lucky if people send three or four"; tbh users sent 60
  [LP 28:43].
- At its peak tbh got 360,000 installs per day [LP 24:43].
- Cash: an Amazon bill of about $120,000 against $150,000 in the bank. He quickly put together a
  funding round and told the team: "i think i could probably sell this thing." [LP 21:55 to 22:15]

## Geofence to control growth

They rolled out region by region and geofenced the rest so the servers could keep up. It was
controversial inside the team ("why would you turn off something that's working?"), but his view was
that if it worked at so many schools "we could just relaunch it any time" [LP 28:43 to 29:08].

> "if we didn't geofence the app, there would be no way we would've been able to keep that thing
> online because that gave us some slack to control growth." [LP 35:40]

## Everything breaks

> "everything that you built needs to be substituted almost every three days." [LP 34:45]

Their support system broke after three days and its replacement seven days later [LP 34:59]. "you
have to be ruthless with prioritization as something scales up and put out the largest fires
first" [LP 35:18]. During Gas he was "sleeping three hours a day for three months" [LP 1:08:13].

## Expect a crisis every few hours

"there's a crisis every 3 hours when it's starting to work", and a breakout needs, in his words, a
miracle every week [SOL 1:42].

Experience is what makes it survivable: after 14 failures, "when it hit we knew exactly what to do"
[WIH 8:26].

## Spend nothing you don't have to

Gas "ran almost entirely on startup credits" (AWS, Mixpanel). Once early data came in, his rule was
to "negotiate every bill down to the last cent of margin for every vendor", and the company stayed
"pure cashflow for the team. we had no investors." [LP 1:10:13 to 1:10:38]

---

## How to apply it (our reading)

**A breakout runbook, prepared before you need it.**

1. **Gate.** Build a regional or invite gate you can switch on in minutes (by school, city, country).
2. **Rank the breakers.** List the systems that fail at 10x: servers and database, support, moderation
   and abuse, payments, SMS or push providers. For each, write the first sign of failure and the
   replacement.
3. **Daily fire list.** Each morning, rank open problems by users affected. Fix from the top only.
4. **Cash check.** Write cost per thousand daily users. Ask every vendor for credits and a better rate
   before you are big, not after.
5. **Decide early what *too fast* means**: the error rate or support backlog that triggers the gate.

**Worked numbers (invented).** Servers cost $0.04 per daily user per day. At 50,000 daily users that
is $2,000 a day; at 500,000 it is $20,000 a day, or $600,000 a month, before revenue. With $250,000 in
the bank, the gate is not optional. Open one region at a time while the database work lands, as tbh
did with geofencing.

**Failure modes.**
- No gate, so the first viral day takes the app down for everyone.
- Rebuilding everything at once instead of the one system on fire.
- Hiring through a spike that may last weeks (chapter 00: viral apps “basically are like uh films” [OOO 54:39]).
- Letting moderation and safety fall behind growth. With teens, that is the first fire, not the last
  (chapter 12).

**Limits.** These are his accounts of two breakouts with very small teams. Bigger teams will hit
different bottlenecks, but the gate and the fire list still apply.
