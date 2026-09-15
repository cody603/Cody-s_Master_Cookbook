# CHAT.md — read this, then go

A *master-cookbook* skill sent you here. This is the whole manual. It is short on purpose so a small, fast model can run it in voice. Base URL for every file named below: `https://raw.githubusercontent.com/cody603/Cody-s_Master_Cookbook/main/`

## 1. Fast path — do this first, every time

1. **Fetch `planner/quick.md`.** That is the fridge sheet: every ⭐ staple main and side with its hands-on minutes, how many it serves, and **how its name sounds when spoken**. Answer planning questions from it. **Do not fetch anything else until you actually need it.**
2. **Speak short.** Rules in §3.
3. **Plan first, build later.** Stage 1 is fast conversation. Stage 2 is the real work, and it may take a minute. Stage 3 comes back later — the pantry check, then the cart. Never mix them, and never run ahead to the next one.

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

**Usually Sunday or Monday: the whole week in one conversation, ending with the list on the phone.** Take the week down: day, dinner time, main, sides.

**Questions are the bottleneck — keep them to the fewest that change the outcome.** Cody: *"it's designed for the utmost accuracy while maintaining speed."* Assume the small things and **say the assumption in the read-back**, where one yes confirms all of it and one word corrects any of it. Ask only these, one at a time:

- Dinner time, if not given — then assume 7:00 and say so.
- **Leftovers?** "Leftover meat" = subtract that meat only, keep everything else (still chop the cilantro, still buy the buns). "Leftover street tacos" = the whole meal, nothing to shop or make. **Frozen?** If not said, ask — frozen earns a thaw event (pulled pork: a full day in the fridge; a whole chuck roast: two days). Leftovers from earlier the same week are already thawed.
- **How many people?** quick.md has each dish's serving count; say when a dish is short for the table.
- **Anything extra this week?** — fruit, snacks, sandwich fixings from `HOUSEHOLD-STAPLES.md`. Something new they want on there every week is a revision request (§9).
- **Anything due on the repeat-buy log?** Fetch `CONSUMABLES.md` and ask about **everything** past its interval **in one sentence** — *"trash bags, paper towels and the Zevia are all about due — want any of those?"* One question, one answer. Never add silently, never one item at a time. Drinks, milk, paper goods and cleaning supplies all count as groceries here.

Read the whole plan back in one breath. Get the yes. **Then, and only then, Stage 2.**

**Log what's for tonight.** When someone says a dish is for *tonight*, write it into `COOKING-LOG.md` as *provisional* (§9) — no question asked. The next conversation that mentions that night confirms it or marks it skipped.

## 5. Stage 2 — Build (the real work; say "give me a minute")

**Model: Opus for this stage.** Cody's call, 2026-09-14 — the merged, timed sequence in step 5 is where all the logic lives: which steps start together, what waits, what gets full attention. *"The word document is where all the logic is… I need you to learn and look at things, especially the first couple of times we're doing it with Opus, so we can set some principles up."* Stage 1 runs fine on Haiku; live cooking (§7) only *follows* this document, so it doesn't need Opus. If the conversation is on a smaller model when it's time to build, say so once and offer to hand off.

Now fetch what you need: `planner/recipes/<anchor>.md` for each chosen dish (the anchor is in quick.md), `planner/staples.md` for the ⏰ countdowns, `HOUSEHOLD-STAPLES.md` for extras. Then produce, in this order:

1. **Grocery list**, merged from each recipe's own list. Group: **Hong Kong Market · Walmart or any grocery · a named store · order online.** Sum like items. Subtract leftover meat. **Memphis Dust is never on it** (standing stash). Staple rubs are *check the pantry*. **Siete maíz chips are bought in store at Walmart, never online.** Briquettes and wood whenever a grill or smoker dish is in the week; eggs for the soak whenever fresh seafood is.
2. **Push it to their phone** — whatever reminders connector *this person's* Claude has (Apple Reminders on iPhone, Google Tasks on Android). One item per line, store name first. No connector? Say so, offer email.
3. **Email it on request** through Gmail: the grouped list, plus a plain paste-ready block for a Walmart order — one item per line, quantity first, no symbols, Walmart items only.
4. **Calendar events** from each staple's countdown, subtracted from the dinner time: thaw, dry brine, sous vide start, light the smoker, start prep, dinner. One spoken summary, one yes, then write.
5. **Tonight's instructions — one per night**, and for the whole week when planning the week: **one merged, numbered sequence per meal, not the recipes stapled together** — every step tagged *(for the X)*, simultaneous steps as an *"at the same time"* block, precision stages marked *full attention*, a substitution line at the top (*if a dish changed, skip its tagged steps*), each dish's Ingredients verbatim and grouped. Steps are the recipes' own words. Rules and example: §T112 (§7). **Write each night's sequence to `tonight/<date-of-dinner>.md` in the repo** (format in `tonight/README.md`; each technique step names its §T file in brackets) — that file is what live cooking reads, so it must exist. Word doc and email are copies on request; grocery list on top of those.

The full procedure with every rule is §T111 (`planner/recipes/t111-planning-a-week--the-conversation-mode-workflow.md`). Read it the first time you build a week.

## 6. Stage 3 — the pantry check, then the cart

**The list you pushed in Stage 2 is the *need* list, not the *buy* list.** Two more rounds turn it into a buy list and then into a filled cart. They happen later, in their own turns — don't run ahead to them.

**Round 1 — the pantry check.** Say it when you push the list: *"Go check your cabinets and fridge, tick off whatever you already have, and tell me when you're done."* They walk the kitchen and check items off in Reminders. When they come back — *"I've updated the grocery list"* — **re-read the actual list from the reminders connector. Do not work from the copy you wrote.** Then give back the **revised buy list**: only what is still unchecked, regrouped by store, counted. *"Nineteen left. Four Hong Kong Market, fifteen Walmart."* If the connector can't show you what's checked, say so plainly and ask them to read off what they've got instead — never guess.

**Round 2 — the cart.** This one needs a computer, because it drives a browser. Someone opens this same chat on a desktop and says *"add all of this to my Walmart cart."* Work from the **revised** list, Walmart items only, and add them to the cart at walmart.com through the Chrome extension.

- **Report every miss.** Anything Walmart doesn't carry, doesn't have in store, or substitutes on its own — **say which items and why**, item by item. Don't quietly accept a substitution.
- **Misses have somewhere to go:** an Amazon list for anything orderable, Hong Kong Market for the Asian-aisle items, a named store for the rest. Offer it; don't do it unasked.
- **The Siete maíz chips never go in an online cart** — those are picked up in the store at Walmart, standing rule.
- **On a phone, this round can't run.** Say so in one sentence — *"this part needs a computer"* — hand them the paste-ready list instead, and stop.
- **When the cart is filled or the list is handed off, stamp the date in `CONSUMABLES.md`** for everything on that log that was bought (§9). Two or three stamps teach the interval for anything marked *learn it*.

## 7. Cooking live — one step, then stop

**This stage follows the document; it doesn't think up the order.** Cody: *"the live cooking in chat is really just following the logic of the word document. The word document is where all the logic is."* So any model that can read a list and fetch a file can run it — Sonnet is fine. The rules and a worked example are **§T112** (`planner/recipes/t112-cooking-the-whole-meal--sequencing-several-dishes-and-the-spoken-walkthrough.md`). Fetch it the first time someone starts cooking in a conversation. The short form:

1. **Fetch `tonight/<today>.md` and walk its steps in order.** *Let's cook, what's first, walk me through dinner* — that's the trigger; the file is the plan. It already decided what starts together, what waits, and what gets full attention. **If the file isn't there**, say so, then build the sequence yourself from §T112 — every stage of every dish is *precision* (steak coming up to temp, a sear, a roux, frying, a wok — full attention, nothing else at once), *check-in* (a side in a pan, pasta, mashing — two can run together), or *hands-off* (oven, rest, bath — start these first); precision stages in the rest windows; a dish that is precision end to end goes last.
1a. **Techniques come from the tags, not from memory.** When a step has a technique in it — *sauté the sprouts*, *bring the steak to 129*, *make the roux* — the recipe file's **Techniques used** line names the §T entry; fetch that `planner/recipes/t…` file and answer from it.
2. **Keep a private pointer** — which dish, which step. Never say the number aloud.
3. **Say one step:** what to do, **what it's for** (*"for the caulimash"*), and the one technique pointer if the step has one. **Then stop and wait** for *done / next / okay / what now*.
4. **Simultaneous steps are one turn:** the first pan's step, *"and at the same time,"* the second pan's. Then stop.
5. **Precision stages: slow, one sentence at a time, with the doneness cue.** Say that nothing else starts until this is done.
6. **A question mid-step:** answer from the recipe or technique file, then bring them back — *"Back to the steak: you're bringing it up to 129."* **"Where were we?"** — name the dish and the step.
7. **Timers:** say the minutes, tell them to set one. **Substitution mid-cook:** swap that dish's remaining steps, say which tagged steps to skip; if permanent, it's a revision request (§9).
8. **Out of coriander? Only half-and-half?** Expected — answer in the next sentence, on any model. Cookbook first (the pantry reference is `planner/recipes/t106-…`), then one quick lookup from a real chef or test kitchen, source named in a breath. **Write the swap into tonight's file** under *Swaps made tonight*, adjust that dish's remaining steps, and keep going. Never stall a kitchen on a lookup.
8. **Doneness and safety:** the entry's own number; USDA where it's silent; Fahrenheit always. Sous vide bag: kosher salt, garlic powder, black pepper, nothing else; multi-day baths at 131–133°F.

## 8. When something just changed — the refresh rule

If anyone says *"I just added…"*, *"that's been updated,"* or a dish isn't where you expect: **fetch `CHANGELOG.md` fresh** (newest-first, so the top rows are today's even in a cut-off fetch), then fetch fresh whichever planner files those rows name. **The fresh read wins** over anything read earlier. `planner/README.md` carries the planner's build time; a changelog row newer than that means the planner hasn't caught up yet.

## 9. Writing things down — three files, open to everyone

**`PROPOSED-REVISIONS.md` is the file a chat session writes to for anything about the book.** Never touch `codys-cookbook.md`, `CLAUDE.md`, `HOUSEHOLD-STAPLES.md`, `planner/`, `photos/`, or `tools/`.

**Two logs and the night files are writable without approval** — they're diaries, not the book. Same read-insert-write-back procedure as below, commit message `Log: <what> — <name>`:

- **`CONSUMABLES.md`** — add a purchase date (newest first) when a run actually happens; add an item when someone says they buy it on a rhythm; write a *learned* interval once there are two or three dates to average.
- **`COOKING-LOG.md`** — a row the moment a dish is named for *tonight*, marked *provisional*; flip it to *confirmed* or *skipped* the next time that night comes up. A one-line verdict if one was given. Anything that would change a **recipe** goes below instead.
- **`tonight/<date>.md`** — written by Stage 2, edited by live cooking for swaps. Working papers for one night; never the source of a recipe.

**Anything anyone wants changed is a revision request** — a taste note (*"less salt in the pho"*), a specific quantity, a dish on or off the fridge sheet, even the sheet's font size, a household grocery item (*"we buy Nutella all the time — add it"*), a substitution, a new recipe, a rating. **Every time, without exception.** Ask the person's name once if you don't have it.

**The procedure, exactly:**

1. Read `PROPOSED-REVISIONS.md` from the repo with the GitHub connector (you need its `sha` to write it back).
2. Insert one entry — the four-line format in that file — **directly below the line `<!-- NEW ENTRIES GO DIRECTLY BELOW THIS LINE -->`**. Never alter anything already there.
3. Write the file back (create-or-update with the `sha`), commit message `Revision request: <topic> — <name>`.
4. Say, in these words: **"I've put that down as a revision request. When Cody approves it, it'll be implemented."**
5. **No GitHub connector, or no permission?** Email the same entry to Cody through Gmail, subject *"Cookbook revision request: <topic>"*, and say: **"I've sent that to Cody as a revision request. When he approves it, it'll be implemented."** A request is never left unrecorded.

Cody's own requests get applied at the next Code session without waiting; everyone else's wait for his OK.

## 10. Where everything is

| File | What it is |
|---|---|
| `planner/quick.md` | **Start here.** Staples, minutes, serves, sounds-like, file names. |
| `planner/aliases.md` | Sounds-like for every dish in the book. |
| `planner/meal-planning-sheet.md` | The full fridge sheet — every cookable dish, for "what else is there?" |
| `planner/staples.md` | ⏰ countdowns for the calendar. |
| `planner/index.md` | Every entry, one line, with its file. |
| `planner/recipes/<anchor>.md` | The full recipe. |
| `CHANGELOG.md` | What changed, newest first. |
| `PROPOSED-REVISIONS.md` | **Chat writes here.** Every request about the book, from anyone. |
| `HOUSEHOLD-STAPLES.md` | Groceries that aren't recipes — read it for the week's extras; additions go through requests. |
| `CONSUMABLES.md` | Drinks, milk, paper goods, cleaning supplies — repeat buys with their purchase dates. **Chat writes here**, no approval needed. |
| `COOKING-LOG.md` | What got cooked, which night, how it went. **Chat writes here**, no approval needed. |
| `tonight/<date>.md` | The night's merged sequence — what live cooking reads. **Stage 2 writes it; live cooking edits it for swaps.** |

## 11. Setup, once per person

The skill (`tools/master-cookbook-SKILL.md`) · a reminders connector for their phone · Gmail if they want the list emailed · a calendar connector if they want the events · GitHub only if they should write proposals straight into the repo (Cody adds them as a collaborator; otherwise proposals go by email, which is fine) · the Claude Chrome extension **on a computer** if they want §6's cart run.

*Maintained by Code sessions. The skill that points here never has to change.*
