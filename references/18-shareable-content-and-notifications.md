# 18 · Shareable content and notification loops

Chapter 06 covers one-to-one invites. This chapter covers the other product channel, one-to-many
sharing, and the notification loop that brings people back. Both are thinner in his first-party
record than invites, so more of this chapter is our reading, labelled as such.

## Sharing is the second product channel

> "the other is uh sharing one to many. so like you know posting on your story" [OOO 1:05:50]

## Spotify Wrapped syndrome

His December 2023 post: true viral growth comes only when users share your app's content "at a high
frequency to other networks". Founders who add a one-off shareable moment, which he calls "Spotify
Wrapped syndrome", may top the charts for a day, but that creates “phantom validation”. What you need
is for the main content of the feed to be shareable; he gives TikTok and Instagram as examples of apps
that did not grow from a hack bolted on later.
[X 2023-12-16](https://x.com/nikitabier/status/1736067506442326102)

## What it looked like on Gas

Per TechCrunch, in October 2022 he said 23% of Snapchat's US users had viewed a Gas story, and
"sharing a gas poll with snapchat was placed as a primary button in the app"; when Snap removed Gas
from its developer platform, the app broke for seven days [TC4]. The share was the main surface, not a
campaign, and it sat on a platform he did not own (chapter 07).

## Notifications as the core loop

- On tbh, as TechCrunch described it, "you get notified when you're selected" in a poll, while who
  chose you stays anonymous [TC1]. A 2018 write-up of his Berkeley talk describes the same loop: the
  chosen friend "is notified that an anonymous person selected them in the poll" [SCETW]. The
  notification is the payoff of someone else's action, which is what brings the picked person back.
- Getting the core flow perfect on Gas included the notifications: "the questions were great. push
  notifications, everything worked." [LP 1:12:25]
- He treats the push permission as a funnel step like any other: he once guessed an app's push
  opt-in rate from its onboarding almost exactly
  [X 2025-05-11](https://x.com/nikitabier/status/1921708920181055975).
- During the hoax, a push notification to every user about safety was one of their tools, per the
  Washington Post [WP].
- The competition is fierce: "we are spread thin through so many notifications, products,
  everything" [LP 1:27:31].
- And a limit he set at X for AI: "a machine should not be talking to a human unprompted" [TBS 25:26].

---

## How to apply it (our reading)

**Sharing.**
1. **Find the unit of content** your app produces every session (a poll result, a photo, a score, a
   price found).
2. **Make that unit shareable by default**, with one tap, in the format of the destination (a story
   card, a link preview).
3. **Measure frequency**: shares per active user per week, not total shares in launch week.
4. **Attribute installs from shares** separately (`templates/01`).

**Notifications.**
1. **Tie every push to another person's real action** or a result the user asked for. No filler.
2. **Ask for the permission at the moment of value** (*get told when a friend picks you*).
3. **Track opt-in, open rate and day-2 return** for users who opt in versus those who don't.
4. **Cap the volume**, as tbh capped answering at 12 per hour [TC1]. Scarcity keeps the signal.

**Worked numbers (invented).** Launch week: a year-in-review card gets 30,000 shares, then 400 a week.
That is the syndrome. Compare a feed where 5% of 50,000 weekly users share one item a week: 2,500 shares
every week, compounding. If each share brings 0.2 installs, that is 500 installs a week that keep coming.

**Failure modes.**
- A one-off shareable campaign read as product-market fit.
- Shares that land on a platform that can switch you off overnight.
- Pushes about the app rather than about people (*We miss you!*).
- Notifications engineered to pull teens back late at night. Out of bounds (chapter 12).

**Limits.** He has said less in public about notifications than about invites. The notification
steps above are our synthesis, anchored to the loop tbh used.
