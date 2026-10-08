# Template 02 · The 48-hour test plan

One test, one rung, one answer. Based on chapters 03 and 04.

> "usually within 48 hours we'd know if it if it was working. uh and with with tbh uh we knew that
> night" Nikita Bier [OOO 56:46]

> "you never want to walk away from an experiment or test and say" that maybe the execution was
> bad. [LP 32:00]

Test name: ______________________  Owner: __________  Start: __________  Read-out: __________

## 1. Which rung are we testing? (pick ONE) [LP 1:11:50]

- [ ] Core flow: will people use it?
- [ ] Spread inside a group: will they bring their peers?
- [ ] Hop between groups: will it jump to the next group on its own?
- [ ] Pay: will people pay for it?

## 2. The chain of must-be-true conditions [LP 1:12:46]

Write the product as conditions. Aim for four or fewer.

1. If ____________________, then ____________________ must be true.
2. If ____________________, then ____________________ must be true.
3. ...

This test checks link number: ___

## 3. Execute 100% on the rung, half-ass the rest [LP 1:12:02]

| What must be excellent for this test | What can be rough |
|---|---|
| | |

## 4. Remove the confounding variables

| Confounder | How we remove it |
|---|---|
| Not enough friends on the app (density) | Seed one real group all at once: one school, club, team or community [OOO 55:52] |
| Users stuck or confused | Live chat support, staffed for the whole test [LP 32:44] |
| Bad first impression from bugs | Polish the core flow even if nothing else is polished |
| Wrong audience | Ads and invites target exactly the group being tested |

## 5. The seed

- Group: ______________________  Size: ______
- How everyone gets it at the same time: ______________________
- Marketing touches per person (he says people need about three) [LP 29:54]: ______

**Remember his caveat:** "this is not the way we grew the app. this is how we tested apps." [LP 30:46]

## 6. Decide the answer before you start

| Signal | YES at or above | NO below | UNCLEAR band (between) |
|---|---|---|---|
| Primary metric: ____________ | | | |
| Guardrail: ____________ | | | |

Every test needs all three columns. UNCLEAR is not a pass: it means a confounder was probably not
removed (section 4). Our suggested default for a core-flow test: YES at 50%+ doing the core action
3+ times on day 1, NO under 20%, UNCLEAR in between. These numbers are ours, not his.

"if your product's working, you'll know. and if there's any uncertainty, it's not working"
(Roger Dickey, relayed by Nikita) [LP 36:12]

## 7. Read-out (fill in at 48 hours)

- Result: YES / NO / UNCLEAR
- If UNCLEAR, which confounder was not removed? ______________________
- Next: YES, move up one rung. NO, change the idea or the mechanic. UNCLEAR, fix the confounder and
  relaunch once; a second UNCLEAR counts as NO (our rule, following his “any uncertainty” line [LP 36:12]).
