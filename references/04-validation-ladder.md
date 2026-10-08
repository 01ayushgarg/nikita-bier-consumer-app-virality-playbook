# 04 · The validation ladder

This is the chapter the agent skill is built around: find the first rung that is not yet proven,
and aim everything at it.

## The rungs, in his words

From the Gas rebuild [LP 1:00:13 to 1:02:27] and his lasting lesson [LP 1:11:50]:

1. **Will people use the core flow?** For Gas: do people send a lot of messages?
2. **Will they spread it within their peer group?** Within a school.
3. **Will it hop peer groups?** School to school.
4. **Will people pay for it?**

He calls each of these "a very, very challenging problem in light of the new climate that we were
operating in" [LP 1:00:25].

> "execute at 100% for the thing you're trying to validate at that specific stage of the product
> development cycle. and then you can kind of half-ass the rest" [LP 1:12:02]

For Gas that meant: "we made the polling experience just perfect. the questions were great. push
notifications, everything worked. and then the next stage was getting sharing and virality
working." [LP 1:12:25]

## Conditional layers

> "if this is true, then what next needs to be true for this thing to work out? and these layers of
> conditional statements. and the more layers you have, the higher risk your product is, so you
> should try to condense it to about like four things" [LP 1:12:46 to 1:12:54]

## Same idea, new climate

Gas was the tbh concept five years later and still took "about i think like nine launches including
renaming the app" [LP 59:15]. tbh had sent invite texts from a server via Twilio; by then "you
really can't send texts from a server anymore" [LP 58:31], users had to send from their own phone,
and fewer invites went out [LP 58:57]. **A rung proven in the past is not proven now.**

---

## How to apply it (our reading)

The procedure, thresholds and scoring below are ours, built on the rungs above. Use
`templates/05-validation-ladder-scorecard.md` to fill it in.

### Step 1: write the chain

Write the product as at most four *if, then* links, one per rung. Example for a study-group app:

1. If a student joins, they use the group chat on day 1 (core flow).
2. If they use it, they bring classmates from the same course (within group).
3. If one course fills up, students in other courses hear about it and join (hop).
4. If they rely on it, some pay for a premium feature (pay).

More than four links is itself a finding: the plan carries too much risk.

### Step 2: pick the evidence for each rung

| Rung | What counts as proof (our suggestion) | What does not count |
|---|---|---|
| 1. Core flow | Most people in a seeded, dense group do the core action repeatedly on day 1, and come back on day 2 | Sign-ups; a TestFlight beta of fans |
| 2. Within group | Invites or shares per active user rising, and a growing share of the group joins without new ads | A spike from a creator video |
| 3. Hop groups | New groups starting with zero seeding from you | Groups you seeded yourself |
| 4. Pay | A share of active users pay for the thing support keeps asking for (chapter 11) | Pre-orders from friends |

### Step 3: find the first rung that is not proven

Start at rung 1 and stop at the first rung without proof. That is the only thing the next test
measures. Everything for later rungs can be rough, as long as it does not confound the test.

### Step 4: run one clean test on that rung

Use chapter 03 and `templates/02-48-hour-test-plan.md`. Set YES, NO and UNCLEAR lines in advance.

### Step 5: re-check the rungs below when the climate changes

A new platform rule, a new OS permission, a rename or a new audience can knock out a rung you
thought was proven (his Twilio example above, iOS 18 in chapter 06).

## Worked example (invented numbers)

A photo-challenge app seeded in one school of 900 students.

| Rung | Evidence so far | Verdict |
|---|---|---|
| 1. Core flow | 520 sign-ups; 61% posted at least 3 times on day 1; 48% back on day 2 | Proven for this group |
| 2. Within group | Invites per active user 1.4 in week 1, 0.6 in week 2; 70% of new joins came from the paid ads | **Not proven** |
| 3. Hop groups | Two other schools have users, both reached by the same ads | Not tested |
| 4. Pay | Team is designing a subscription | Premature |

Audit finding: stop the subscription work. Rung 2 is the target. The next test changes only the
invite flow (chapter 06), with ads switched off after day 1 so in-group spread can be seen.

## Failure modes

- **Skipping to pay.** Building monetisation before anyone spreads the app.
- **Counting seeded growth as hopping.** If you seeded it, it did not hop.
- **Polishing everything.** Effort spread across all rungs leaves the test rung under-built.
- **Never re-testing.** Treating last year's proof as this year's.
- **A chain of eight links.** Too many things must go right; cut scope until there are about four.

## Limits

The four rungs describe a social app with a peer group. For a utility, rungs 2 and 3 become *people
share the result* and *strangers arrive from those shares* (chapter 16). The ladder tells you what
to test next, not whether the product will last; durability stays a black swan (chapter 01).
