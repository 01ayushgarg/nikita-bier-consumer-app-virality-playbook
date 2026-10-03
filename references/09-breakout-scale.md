# 09 · When it works: breakout scale

## Product-market fit is binary

Nikita relays a line from founder Roger Dickey: "If your product's working, you'll know. And if
there's any uncertainty, it's not working." [LP 36:15] "It really is a binary when it comes to
consumer products." Signs: people fight to get in, and you invent new metrics. tbh's was
"hourly actives", not daily actives [LP 36:40].

## What breakout looked like on tbh

- On a messaging app's first day "you're lucky if people send three or four" messages. tbh users
  sent 60 [LP 28:47].
- One school sent 450,000 messages in its first seven days [LP 28:30].
- At its peak tbh got 360,000 installs per day [LP 24:43].
- `[2024]` Reaching #1 in the US App Store "used to be like 80 to 100,000 installs," and with
  heavy ad spenders, "some days it's up to 300,000" per day [LP 24:16].
- Cash: an AWS bill around $120,000 against $150,000 in the bank. Nikita quickly put together a funding
  round and asked the team to focus for two months: "I think I could probably sell this thing." [LP 21:58 to 22:16]

## Geofence to control growth

They rolled out state by state, geofencing each state, to scale servers. It was controversial
internally ("why would you turn off something that's working?"), but "if it's working at this
many individual schools, we could just relaunch it any time." [LP 28:52 to 29:19]

> "If we didn't geofence the app, there would be no way we would've been able to keep that
> thing online because that gave us some slack to control growth." [LP 35:35]

## Everything breaks

> "Everything that you built needs to be substituted almost every three days." [LP 34:43]

Their support system broke after three days, its replacement after seven more. "You have to be
ruthless with prioritization as something scales up and put out the largest fires first." [LP 35:17]
Gas: Nikita slept three hours a day for three months; the team worked 9am to midnight, seven
days a week [LP 1:08:12].

## Expect a crisis every few hours

> "There's a crisis every 3 hours when it's starting to work. To really have a consumer product break
> out, you essentially need a miracle every single week." [SOL 1:42]

Experience is what makes it survivable: after 14 failures, "when it hit we knew exactly what to do we knew
exactly how to scale it." [WIH 8:24]

## Spend nothing you don't have to

Gas "ran almost entirely on startup credits" (AWS, Mixpanel). When early data came in: "now
it's time for me to negotiate every bill down to the last cent of margin for every vendor."
They had no investors; it was "pure cashflow for the team." [LP 1:10:11 to 1:10:41]

**Checks to run:**
- Is there a kill switch or regional gate to slow growth if infrastructure fails?
- Which systems will break first at 10x (support, servers, moderation, payments)? Rank by blast radius.
- Has every vendor been asked for startup credits and a better rate?
