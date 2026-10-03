# Template 02 · The 48-hour test plan

One test, one rung, one answer. Based on chapters 03 and 04.

> "Usually within 48 hours we'd know if it if it was working. Uh and with with TBH uh we knew that
> night." Nikita Bier [OOO 56:29]

> "You never want to walk away from an experiment or test and say, 'Well, maybe the execution was
> bad.'" [LP 31:58]

Test name: ______________________  Owner: __________  Start: __________  Read-out: __________

## 1. Which rung are we testing? (pick ONE) [LP 1:11:50]

- [ ] Core flow: will people use it?
- [ ] Spread inside a group: will they bring their peers?
- [ ] Hop between groups: will it jump to the next group on its own?
- [ ] Pay: will people pay for it?

## 2. The chain of "must be true" [LP 1:12:48]

Write the product as conditions. Aim for four or fewer.

1. If ____________________, then ____________________ must be true.
2. If ____________________, then ____________________ must be true.
3. ...

This test checks link number: ___

## 3. Execute 100% on the rung, half-ass the rest [LP 1:12:07]

| What must be excellent for this test | What can be rough |
|---|---|
| | |

## 4. Remove the confounding variables

| Confounder | How we remove it |
|---|---|
| Not enough friends on the app (density) | Seed one real group all at once: one school, club, team or community [OOO 55:34] |
| Users stuck or confused | Live chat support, staffed for the whole test [LP 32:46] |
| Bad first impression from bugs | Polish the core flow even if nothing else is polished |
| Wrong audience | Ads and invites target exactly the group being tested |

## 5. The seed

- Group: ______________________  Size: ______
- How everyone gets it at the same time: ______________________
- Marketing touches per person (he says people need about three) [LP 29:44]: ______

**Remember his caveat:** "This is not the way we grew the app. This is how we tested apps." [LP 30:43]

## 6. Decide the answer before you start

| Signal | Threshold for YES | Threshold for NO |
|---|---|---|
| Primary metric: ____________ | | |
| Guardrail: ____________ | | |

"If your product's working, you'll know. And if there's any uncertainty, it's not working."
(Roger Dickey, relayed by Nikita) [LP 36:15]

## 7. Read-out (fill in at 48 hours)

- Result: YES / NO / UNCLEAR
- If UNCLEAR, which confounder was not removed? ______________________
- Next: relaunch the same rung with a change, or move up one rung.
