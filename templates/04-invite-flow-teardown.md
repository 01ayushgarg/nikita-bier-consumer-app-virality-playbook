# Template 04 · Invite flow teardown

Walk the invite flow screen by screen, as a new user, with a stopwatch and a tap counter.
Based on chapters 05 and 06.

> "If you're building a social app but you're not able to answer these two questions... 1. What does
> your friendfinder look like? 2. How do you invite people?" Nikita Bier [X 2018-05-30]

App: ______________________  Device: __________  Tester: __________

## 1. Taps and time

| Moment | Taps from first open | Seconds from first open |
|---|---|---|
| First moment of value | | |
| First friend found | | |
| 10 friends found | | |
| First invite sent | | |

Benchmarks from the playbook: value in about 3 seconds [LP 1:27:37]; username-based friend finding
is "10,000 taps versus one" [LP 1:31:35].

## 2. Score the flow

| # | Question | Score 0 / 1 / 2 | Evidence |
|---|---|---|---|
| 1 | Does sign-in use the same "protocol" as invites and friend-finding (e.g. phone + SMS + contacts)? [X 2023-05-26] | | |
| 2 | Is the contacts (or equivalent) permission asked at a moment that makes the value obvious? | | |
| 3 | Is the permission grant rate 70% or more? [X 2021-06-11] | | |
| 4 | Are contacts ranked so the most likely joiners come first? ("ranking contacts correctly") [X 2022-08-09] | | |
| 5 | Are people not yet on the app ranked by how many friends they have on it? [LP 1:30:59] | | |
| 6 | Is there more than one well-placed invite entry point? [X 2022-08-09] | | |
| 7 | Does the user always see and approve exactly what gets sent, and to whom? [LP 58:43] | | |
| 8 | Would the least likely inviter in your audience be happy to send this name and icon? [LP 1:16:29] | | |
| 9 | Does the invite message name the shared community or reason? [LP 1:33:24] | | |
| 10 | Does the person invited reach value fast, ideally seeing their friends already there? [LP 1:27:46] | | |
| 11 | Can sign-up be done silently, one-handed, with no sound or voice? [X 2025-05-21] | | |
| 12 | Interest graph? If yes, what replaces contacts on day one (interests, starter packs)? [OOO 26:21] | | |

**Total: ___ / 24.** Every 0 is a table-stakes fix. Pick the two biggest gaps and test them with
template 02.

## 3. Guardrail check (always)

- [ ] Nothing is sent that the user didn't knowingly send.
- [ ] Contact data is used only for what the user agreed to.
- [ ] Nothing in the flow pressures, shames or deceives a minor.

See `references/12-positive-design-and-guardrails.md`.
