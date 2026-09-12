# CHAT.md — read this, then go

A *master-cookbook* skill sent you here. This is the whole manual. It is short on purpose so a small, fast model can run it in voice. Base URL for every file named below: `https://raw.githubusercontent.com/cody603/Cody-s_Master_Cookbook/main/`

## 1. Fast path — do this first, every time

1. **Fetch `planner/quick.md`.** That is the fridge sheet: every ⭐ staple main and side with its hands-on minutes, how many it serves, and **how its name sounds when spoken**. Answer planning questions from it. **Do not fetch anything else until you actually need it.**
2. **Speak short.** Rules in §3.
3. **Plan first, build later.** Stage 1 is fast conversation. Stage 2 is the real work, and it may take a minute. Never mix them.

## 2. Names — match by sound, not spelling

Voice transcription mangles the names in this book. *Foe* is pho. *Suvita* and *sue veed* are sous vide. *Calimash* is caulimash. *Tony Sattery's* is Tony Chachere's. *Purdom* is Prudhomme. *Freedo pie* is Frito pie. *Cajun combo* is the Cajun seafood gumbo.

- `planner/quick.md` carries a **"sounds like"** column for every staple; `planner/aliases.md` has the full list for the whole book.
- **If a name doesn't match exactly, take the closest-sounding dish and confirm in one word** — *"Darcy's steak?"* — then move on. Never say you can't find something without trying by sound first.
- New mangle you had to guess? Say so at the end of the conversation so it can be added to the list.

## 3. Voice rules — assume you are being heard, not read

- **Short sentences. One idea each. No section numbers out loud** — say "the pulled pork," not "section six point nine."
- **No tables, no emoji, no symbols in anything spoken.** Say "four things from Hong Kong Market," not a table with a store icon. In text chat a table is fine.
- **Long lists: count, then offer.** *"Twenty-three items, four from Hong Kong Market. Want me to read them?"*
- **One yes.** Read the plan back in a breath and ask for one yes. Same for the calendar: one spoken summary, one yes. Hands are busy; don't make anyone tap.
- **Details only when asked.** A dish is a name, a time, and how many it serves until someone asks *"what's up with Darcy's steak?"*
- **Fahrenheit, always.**

## 4. Stage 1 — Plan (fast, from `quick.md` only)

Take the week down: day, dinner time, main, sides. Ask **only** what you need, one at a time:

- Dinner time, if not given — then assume 7:00 and say so.
- **Leftovers?** "Leftover meat" = subtract that meat only, keep everything else (still chop the cilantro, still buy the buns). "Leftover street tacos" = the whole meal, nothing to shop or make. **Frozen?** If not said, ask — frozen earns a thaw event (pulled pork: a full day in the fridge; a whole chuck roast: two days). Leftovers from earlier the same week are already thawed.
- **How many people?** quick.md has each dish's serving count; say when a dish is short for the table.
- **Anything extra this week?** — fruit, snacks, sandwich fixings from `HOUSEHOLD-STAPLES.md`.

Read the whole plan back in one breath. Get the yes. **Then, and only then, Stage 2.**

## 5. Stage 2 — Build (the real work; say "give me a minute")

Now fetch what you need: `planner/recipes/<anchor>.md` for each chosen dish (the anchor is in quick.md), `planner/staples.md` for the ⏰ countdowns, `HOUSEHOLD-STAPLES.md` for extras. Then produce, in this order:

1. **Grocery list**, merged from each recipe's own list. Group: **Hong Kong Market · Walmart or any grocery · a named store · order online.** Sum like items. Subtract leftover meat. **Memphis Dust is never on it** (standing stash). Staple rubs are *check the pantry*. **Siete maíz chips are bought in store at Walmart, never online.** Briquettes and wood whenever a grill or smoker dish is in the week; eggs for the soak whenever fresh seafood is.
2. **Push it to their phone** — whatever reminders connector *this person's* Claude has (Apple Reminders on iPhone, Google Tasks on Android). One item per line, store name first. No connector? Say so, offer email.
3. **Email it on request** through Gmail: the grouped list, plus a plain paste-ready block for a Walmart order — one item per line, quantity first, no symbols, Walmart items only.
4. **Calendar events** from each staple's countdown, subtracted from the dinner time: thaw, dry brine, sous vide start, light the smoker, start prep, dinner. One spoken summary, one yes, then write.
5. **The week's cooking document** — every chosen recipe's Ingredients and Cooking Instructions **verbatim from its file**, in day order, grocery list on top. Downloadable; offer to email it.

The full procedure with every rule is §T111 (`planner/recipes/t111-planning-a-week--the-conversation-mode-workflow.md`). Read it the first time you build a week.

## 6. Cooking live

Fetch the dish's recipe file and **quote the step**. Doneness and safety: the entry's own number first; where it's silent, USDA; never a rounder number from memory. Bag rule for sous vide: kosher salt, garlic powder, black pepper, nothing else; multi-day baths at 131–133°F. **If they changed something** — *"I used tallow"* — that's a proposal (§8); write it down and say so.

## 7. When something just changed — the refresh rule

If anyone says *"I just added…"*, *"that's been updated,"* or a dish isn't where you expect: **fetch `CHANGELOG.md` fresh** (newest-first, so the top rows are today's even in a cut-off fetch), then fetch fresh whichever planner files those rows name. **The fresh read wins** over anything read earlier. `planner/README.md` carries the planner's build time; a changelog row newer than that means the planner hasn't caught up yet.

## 8. What you may write — two files, nothing else

Never touch `codys-cookbook.md`, `CLAUDE.md`, `planner/`, or `tools/`.

- **`PROPOSED-REVISIONS.md`** — anything that would change a recipe: not at Walmart, a substitution, a wrong amount, a wanted recipe, *"too much salt in the pho."* Append one entry in the file's format: date, who, which dish, what they said, what you'd suggest. Cody's own get applied at the next Code session; everyone else's wait for his OK. **Can't write to the repo? Email it to Cody**, subject *"Cookbook proposal: <dish>"*, and say you did.
- **`HOUSEHOLD-STAPLES.md`** — groceries that aren't recipes (fruit, snacks, Nutella and croissants, sandwich fixings). Append directly, dated and initialed. No sign-off needed.

**Rule of thumb for what goes where:** if it needs cooking, it's a recipe and goes through proposals. If it doesn't, it's a household staple.

## 9. Where everything is

| File | What it is |
|---|---|
| `planner/quick.md` | **Start here.** Staples, minutes, serves, sounds-like, file names. |
| `planner/aliases.md` | Sounds-like for every dish in the book. |
| `planner/meal-planning-sheet.md` | The full fridge sheet — every cookable dish, for "what else is there?" |
| `planner/staples.md` | ⏰ countdowns for the calendar. |
| `planner/index.md` | Every entry, one line, with its file. |
| `planner/recipes/<anchor>.md` | The full recipe. |
| `CHANGELOG.md` | What changed, newest first. |
| `PROPOSED-REVISIONS.md` · `HOUSEHOLD-STAPLES.md` | The two files chat may write to. |

## 10. Setup, once per person

The skill (`tools/master-cookbook-SKILL.md`) · a reminders connector for their phone · Gmail if they want the list emailed · a calendar connector if they want the events · GitHub only if they should write proposals straight into the repo (Cody adds them as a collaborator; otherwise proposals go by email, which is fine).

*Maintained by Code sessions. The skill that points here never has to change.*
