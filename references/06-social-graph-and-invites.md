# 06 · The social graph, invites and naming

> "the thing that i've been exceptionally good at uh when it comes to doing uh social app product
> development is getting the social graph right, which is uh so when when someone signs up, can they
> find everyone that they know?" [OOO 59:19 to 59:30]

## The two questions every social app must answer

His 2018 test: if you can't say what your friendfinder looks like and how people invite others, you
“just like the idea” of building a social app, rather than building one.
[X 2018-05-30](https://x.com/nikitabier/status/1001666968917757952)

## Small things decide K-factor

In 2022 he wrote that the gap between exponential decline and growth, a K-factor of 0.99 versus
1.01, is often “an extra invite button” or better contact ranking.
[X 2022-08-09](https://x.com/nikitabier/status/1557132295714222080)

## Contacts access is the floor `[2021]`

His 2021 line: if less than 70% of users grant contacts access, the app is “dead on arrival” until
that is fixed. [X 2021-06-11](https://x.com/nikitabier/status/1403498766737444865) Two years later
he mocked the alternative in a satire post about sharing usernames
[X 2023-11-29](https://x.com/nikitabier/status/1729676931858153501), and on Lenny's Podcast called
username exchange "10,000 taps versus one" [LP 1:31:38].

## One sign-in method, on the same protocol as invites

His 2023 rule: allow one sign-in method and pair it with the matching invite and friend-finding
system, for example phone number sign-in with SMS invites and contact-based friend finding. Multiple
methods lead to "a corrupted social graph where users can't find each other".
[X 2023-05-26](https://x.com/nikitabier/status/1662100378500866049)

## Build for the network, not only the user

In 2025 he argued that social products serve the network more than the individual user, so some
choices look user-hostile, such as urging people to import contacts, yet the small burden "yields
100x value to the collective network."
[X 2025-05-10](https://x.com/nikitabier/status/1921278141122887970)

Pair this with chapter 12: building for the network never means sending anything a user did not
knowingly send, or taking contact data the user did not agree to share.

## The name decides the invite [LP 1:15:55 to 1:16:55]

- Gas went through names including Crush and Melt. Under Crush, "invitations dropped
  significantly".
- The cause: "boys invite boys, girls invite girls to apps. and boys didn't want to invite their
  friends to an app called crush with a pink icon." [LP 1:16:18]
- tbh and Gas indexed "about 60 to 65% women", so they made the icon black with a flame, called it
  Gas, "and the invites rate jumped." [LP 1:16:28 to 1:16:48]

## Invites the user sends knowingly

- On tbh, you tapped a contact, tapped Invite, and the app sent a text via Twilio [LP 58:15].
- Texting people without their knowledge: "we never did that. that's egregiously illegal to do and
  also unethical at a user experience level" [LP 58:47]. TechCrunch in 2017: tbh "doesn't spam your
  contacts with unexpected invite messages" [TC1].
- For Gas, the landscape had changed, "so we had to rebuild uh invitations" [OOO 59:19]; texts had to
  come from the user's own device [LP 58:31].

## Friend graph vs interest graph

> "x is an affinity affinity based network. um so you can't just like sync your contacts and suddenly
> have a relevant feed." [OOO 26:29]

His fix at X was **Starterpacks**, accounts grouped by niche and picked at sign-up. Result he
claims: "doubled time spent uh in the app for new users" [OOO 27:33].
[X 2026-01-20](https://x.com/nikitabier/status/2013410692444102793)

## iOS 18 contact permissions `[2024]`

- Across apps you "average about 65% approval rate", higher for teens and lower for adults
  [LP 1:24:25].
- "you better start thinking about plan b" if your company depends on contact sync [LP 1:26:06].
- A month later, he wrote that since iOS 18 friend-based contact-sync apps are “basically dead on
  arrival”, because far fewer people consent to the new permission.
  [X 2024-09-19](https://x.com/nikitabier/status/1836612494938509664)

**Re-check current iOS and Android behaviour before relying on any of this.**

---

## How to apply it (our reading)

1. **Measure the permission funnel**: contacts prompt shown, granted, then (iOS 18+) how many
   contacts shared. His 70% line is from 2021 and pre-dates the iOS 18 change.
2. **Ask at the moment of obvious value** (*see which friends are already here*), never as screen
   one.
3. **Rank the list**: friends on the app first, then non-members with the most friends on the app.
4. **Match the protocol**: one sign-in method, the same identity used for invites.
5. **Read the name and icon as your least likely inviter would.**
6. **Interest graph?** Replace contact sync with picked interests or curated starter accounts.

**Worked numbers (invented).** 1,000 sign-ups, 55% grant contacts, each sharing 40 contacts. If
ranking puts 6 likely joiners at the top and 30% of grantors invite 2 each, that is 330 invites.
Raising the grant rate to 70% (better timing of the prompt) gives 420 invites from the same traffic.
Neither number is his; the levers are.

**Failure modes.**
- Several sign-in methods *to reduce friction*, which breaks friend finding.
- An unranked contact list, so users invite the wrong people or nobody.
- Pre-checked *invite all* boxes. Out of bounds (chapter 12).
- Planning on contact sync after iOS 18 without measuring what users actually share.

**Limits.** The 70% and 65% figures are his, dated 2021 and 2024, from his apps and the dashboards he
has seen. They are not platform statistics.
