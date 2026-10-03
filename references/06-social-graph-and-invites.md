# 06 · The social graph, invites and naming

> "The thing that I've been exceptionally good at uh when it comes to doing uh social app product
> development is getting the social graph right, which is uh so when when someone signs up, can they
> find everyone that they know?" [OOO 59:19]

## The two questions every social app must answer

[X 2018-05-30](https://x.com/nikitabier/status/1001666968917757952):

> "If you're building a social app but you're not able to answer these two questions...
> 1. What does your friendfinder look like?
> 2. How do you invite people?
> ...then you just like the idea of building a social app. You're not actually building a real one."

## Small things decide K-factor

[X 2022-08-09](https://x.com/nikitabier/status/1557132295714222080):

> "From the outside, a breakout social app seems like it would just work on the concept alone—without
> grinding out optimizations. In practice, the difference between exponential decline vs. growth
> (0.99 vs. 1.01 K-factor) is often an extra invite button or ranking contacts correctly"

## Contacts access is the floor

[X 2021-06-11](https://x.com/nikitabier/status/1403498766737444865):

> "If you're building a social app and less than 70% of your users are granting access to contacts,
> your app is dead on arrival until that's fixed. Network effects will never form if you expect
> users—who have a 5 second attention span—to find their friends by typing in usernames."

He made the same point as satire in [X 2023-11-29](https://x.com/nikitabier/status/1729676931858153501)
("Bro your app doesn't need access to Contacts. People can share usernames... And by the year 2035,
your app's social graph will be competitive with Instagrams.") and on Lenny's Podcast: username
exchange means "10,000 taps versus one." [LP 1:31:35]

## One sign-in method, on the same "protocol" as invites

[X 2023-05-26](https://x.com/nikitabier/status/1662100378500866049):

> "If you truly want to grow & get friend density, you should only allow one method—and have that
> method be on the same "protocol" as your distribution & friending system. For example:
> • Phone Number Auth should be paired with SMS Invitations and Contact-based Friendfinding
> • Twitter Auth should be paired with Share to Twitter and Import Followers
> When you allow multiple methods, it leads to a corrupted social graph where users can't find each
> other and the app won't be able to properly rank people that users should invite."

## Build for the network, not only the user

[X 2025-05-10](https://x.com/nikitabier/status/1921278141122887970):

> "Instead of the user, they need to be squarely focused on building for the benefit of the network.
> And those solutions usually can't be inferred by empathy, but rather numbers. On the surface, some
> decisions can look outright user-hostile. For example, urging users to import contacts or follow
> people. But for the incremental burden it puts on the user, it yields 100x value to the collective
> network."

Pair this with section 12: building for the network never means sending anything a user did not knowingly send.

## The name decides the invite [LP 1:15:52 to 1:16:59]

- Gas went through names including Crush and Melt. Crush had a great domain, but under that
  name "invitations dropped significantly."
- The cause: "Boys invite boys, girls invite girls to apps," and "boys didn't want to invite
  their friends to an app called Crush with a pink icon."
- tbh and Gas indexed about 60 to 65% women. They made the app "more masculine": black icon,
  a flame, named Gas. "The invites rate jumped."
- "You think a name doesn't matter, but right at the moment of sending an invite..."

## Invites the user sends knowingly

- On tbh, you tapped a contact's name, tapped Invite, and the app sent a text via Twilio [LP 58:19].
- "We never did that. That's egregiously illegal to do and also unethical at a user experience
  level", about texting people when they were voted on [LP 58:43]. TechCrunch in 2017: "tbh doesn't
  spam your contacts with unexpected invite messages", and the team said "User trust is really
  important." [TC1]
- For Gas, "we had to rebuild uh invitations" because "the landscape had changed" [OOO 59:07];
  texts had to come from the user's own device [LP 59:00].

## Friend graph vs interest graph

Contact sync only works where the network is people you know. On X, an interest graph:

> "X is an affinity affinity based network. Um so you can't just like sync your contacts and suddenly
> have a relevant feed. You have to ask people on boarding [sic: in onboarding] use the timeline
> recommendations." [OOO 26:21]

His fix at X was **starter packs**: accounts grouped by niche, picked at signup with your country
and interests. "We've doubled time spent uh in the app for new users." [OOO 27:05 to 28:22],
[X 2026-01-20](https://x.com/nikitabier/status/2013410692444102793)

## iOS 18 contact permissions `[2024]`

- About 65% of users approve the contacts permission across apps, higher for teens, lower for adults [LP 1:24:27].
- "If you're betting on contact sync as a company right now, you better start thinking about plan B." [LP 1:26:06]
- A month later, [X 2024-09-19](https://x.com/nikitabier/status/1836612494938509664): "RIP Social
  Apps, 2005-2023. As of iOS 18, friend-based contact sync apps are basically dead on arrival. The
  number of people consenting to the new permission has nose-dived—so there is no way to get density
  in a meaningful way... For better or for worse, LLMs might be the new Contact Sync. If we can't find
  our friends on apps anymore, people will find something else to talk to."

**Re-check current iOS behaviour before relying on any of this.**

**Checks to run:**
- What % of new users grant contacts (or the equivalent)? Under 70% is his "dead on arrival" line [2021].
- Does sign-in use the same protocol as invites and friend-finding?
- Are contacts ranked so the best people to invite come first?
- Read the name and icon as the least likely inviter would. Would they send it?
- Friend graph or interest graph? If interest, what replaces contact sync on day one?
