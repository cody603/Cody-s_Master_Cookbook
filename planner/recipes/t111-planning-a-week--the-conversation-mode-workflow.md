<!-- GENERATED from codys-cookbook.md#t111-planning-a-week--the-conversation-mode-workflow — do not edit here; edit the master file and rerun tools/build_planner.py -->
[↑ Meal Planning Sheet](../meal-planning-sheet.md) · [Index](../index.md)

### T111. Planning a Week — the Conversation-Mode Workflow

<!-- TECHNIQUE-TAGS: cody, meal-planning-sheet, planning, weekly-plan, grocery-list, calendar, countdown, leftovers, conversation-mode -->
**Tags:** `cody` · `meal-planning-sheet` · `planning` · `weekly-plan` · `grocery-list` · `calendar` · `countdown` · `leftovers` · `conversation-mode`
**Source:** Cody's own description of how he wants to use the cookbook, dictated 2026-09-09. Not a cooking technique; the procedure a chat session follows when he plans a week off the [Meal Planning Sheet](../meal-planning-sheet.md).
**Used by:** the *master-cookbook* skill in regular Claude chat (voice or text). Code sessions keep the book; chat sessions run the week — see [CLAUDE.md §7](../../CLAUDE.md).

**What he asked for, in his words:** *"I'll trigger the cookbook skill, and then I'll speak into it and say, Monday, we're having dinner at seven. I would like to have pulled pork. Tuesday, we're having street tacos — I'd have the leftover pulled pork with the street tacos. Wednesday, we're having X Y Z. And then, in the calendar, I'd like you to put events: when I need to start prepping, when I need to start sous vide-ing, and when I need to dry brine the day before. All of those things need to be taken into consideration, and I want it happening exactly like that."* The four deliverables he named, in the order he named them: **the grocery list to his phone, the calendar events, one document with every cooking instruction for the week, and then live questions while he cooks.**

#### 0. Where the chat reads from — and why it is not the master file

The master file is over 4 MB. A chat session fetching it from GitHub gets the front matter and nothing else — the [Meal Planning Sheet](../meal-planning-sheet.md) starts 180 KB in and the first recipe 230 KB in. **So the chat never fetches `codys-cookbook.md` directly.** It reads the generated `planner/` folder in the same repo, which is the master split one entry per file and rebuilt after every change (it is a derived view, never edited by hand — the master stays the single source of truth per [CLAUDE.md §1–§2](../../CLAUDE.md)):

- `planner/meal-planning-sheet.md` — the fridge sheet. **Fetch this first, every time.**
- `planner/staples.md` — every ⭐ Staple with its badge and its **⏰ Countdown to dinner** line.
- `planner/index.md` — every entry on one line, for looking a dish up by name.
- `planner/recipes/<anchor>.md` — the full entry. The anchor is the one the sheet links to.

Raw URL pattern: `https://raw.githubusercontent.com/cody603/Cody-s_Master_Cookbook/main/planner/<path>`. Always the live copy; never memory, never an old paste.

#### 1. Take the week down

He gives it by voice, loosely: a day, a dinner time, a dish — sometimes a side, sometimes "leftovers." Write it back as a table before doing anything else, so a misheard dish is caught first:

| Day | Dinner at | Main | Sides | Notes |
|---|---|---|---|---|
| Mon | 7:00 pm | [§6.9 Cody's Pulled Pork Sandwiches](69-codys-pulled-pork.md) | Southern Fauxtato Salad | make enough pork for Tue |
| Tue | 7:00 pm | [§7.1 Cody's Pulled Pork Street Tacos](71-pulled-pork-tacos.md) *(from leftover pork)* | — | leftover from Mon |

Rules for resolving what he said:
- **Match every dish to a sheet line, and take the link from the sheet.** "Street tacos" is [§7.1](71-pulled-pork-tacos.md); "pulled pork" on its own is [§6.9 Cody's](69-codys-pulled-pork.md) unless he names another; "sous vide chicken" is [§T28](t28-sous-vide-chicken-codys-method.md); "Darcy's steak" is the reverse sear in [§3](3-darcys-steak.md). When a name could be two lines (four pulled porks, three crawfish bisques), ask — one question, with the candidates named.
- **No dinner time given → ask once, then assume 7:00 pm** and say so in the table.
- **A dish with 🍽️ is the whole meal**; do not add a side unless he names one.
- **"Leftovers" is something he says, not something the sheet lists — and the two forms mean different things.** *(The 🍱 Leftovers group was retired from the sheet 2026-09-12 at his own instruction; the standing rule is [CLAUDE.md §3f](../../CLAUDE.md).)* **"Leftover meat"** — also *frozen meat*, *previously cooked meat* — means **subtract that meat and nothing else**: the rest of the dish is still cooked and still shopped. **"Leftover [the dish]"** — *"leftover street tacos"* — means **the whole meal is leftovers**, garnishes included, and nothing is made at all. He will say which; leftover meat is far the more common. Either way the source dish must be on an earlier day — if it is not, say so and offer to add it. **A leftover that isn't meat is an anomaly: ask.**
- **If he didn't say whether the meat is frozen, ask — it decides whether the week needs a thaw event.** Leftovers from earlier in the same week's plan are in the fridge and already thawed; anything else is presumed frozen. See §3 below.
- **Do not add dishes he did not name.** Suggestions are fine when asked; the plan is his.

#### 2. Deliverable one — the grocery list, to his phone

Pull each chosen recipe file and take its **C. Grocery Shopping List** exactly as printed — those lists are kept authoritative per [CLAUDE.md §3](../../CLAUDE.md). Then merge:

- **Group by store prefix** — **HK** first, then **GEN**, with any store named in parentheses kept on the line (`GEN Fig jam (Trader Joe's)`).
- **Combine like items across the week** and sum quantities where the units match; where they do not, list both (`2 lb + 1 bunch`).
- **Leftovers subtract, and how much they subtract depends on which form he said** — [CLAUDE.md §3f](../../CLAUDE.md). **"Leftover meat": drop that meat's own grocery items and keep every other ingredient in the dish.** Tuesday's tacos from Monday's pork put cilantro, onion, lime, and tortillas on the list — not a second pork butt; the pulled pork sandwiches still buy buns, and [§4.5 Pickled Pink Onions](45-pickled-pink-onions.md) still get made for both. Monday's line gets a note: *make enough for Tuesday.* **"Leftover [the dish]" adds nothing at all** — not even the garnishes, because they are left over too.
- **[§4.108 Memphis Dust](4108-meatheads-memphis-dust.md) is skipped** — he keeps a standing stash, per [CLAUDE.md §6](../../CLAUDE.md). The rest of the ⭐ Staple Rubs ([§4.105 Dalmatian](4105-dalmatian-rub.md), [§4.1 Darcy's](41-darcys-steak-rub.md), [§4.7 Captain Mike's](47-captain-mikes-seasoning.md), [§4.87 Cavender's](487-cavenders-all-purpose-greek-seasoning-store-bought.md), [§4.88 Vegeta](488-vegeta-store-bought-croatian-all-purpose-seasoning.md), [§4.197 Lawry's](4197-lawrys-seasoned-salt-store-bought.md)) go on as *check the pantry* lines, not as buys.
- **Insta-light briquettes and wood** go on whenever a ♨︎ dish is in the week — his own rule on [§3](3-darcys-steak.md) and [§T27](t27-sous-vide-not-so-premium-steak-cuts-codys-method.md): *"we've gotta have plenty."*
- **Fresh seafood bought in Missouri gets the [§T17](t17-the-raw-egg-soak-deodorizing-fish--shellfish.md) egg soak** — add the eggs.

Then push it to his phone as a Reminders list (that integration lives in chat, not in a Code session — [CLAUDE.md §7](../../CLAUDE.md)), one item per line, store prefix kept so he can shop it in order.

#### 3. Deliverable two — the calendar events

Every ⭐ Staple recipe carries a **⏰ Countdown to dinner** line under its badge, derived from its own steps: stages in reverse order, each with a **T−** offset back from the moment food hits the table. **The calendar is that line, subtracted from the dinner time he gave.** For a 7:00 pm Monday dinner and a countdown reading `T−1 day dry brine · T−5 hr light the smoker, bird on · T−30 min rest and carve`:

| Event | When | Title |
|---|---|---|
| dry brine | Sun 7:00 pm | **Mon dinner — dry brine the turkey (§6.11)** |
| smoker | Mon 2:00 pm | **Mon dinner — light the smoker, bird on at 225°F (§6.11)** |
| rest | Mon 6:30 pm | **Mon dinner — pull, rest, carve (§6.11)** |
| dinner | Mon 7:00 pm | **Dinner: Tony Chachere's Smoked Turkey + sides** |

Rules:
- **One event per stage, plus the dinner itself.** Title = day, the stage in the recipe's own words, the § number. Put the recipe's raw-file link and the stage's step text in the event body so the event is usable from the phone without the document.
- **A range offset (T−4 to 6 hr) is placed at the early end** — being early costs nothing, being late costs dinner.
- **Multi-day stages land on the earlier day at the same clock time as dinner** (T−2 days for a 7:00 pm Wednesday dinner is 7:00 pm Monday). If that collides with another day's cooking, say so and move it earlier, never later.
- **Sides with a countdown of "T−N min start" fold into the main's last prep event** — one event, *"start the sides,"* not five.
- **A recipe with no countdown line** (anything that is not a ⭐ Staple) gets its events from the badge — Prep + Cook back from dinner, Slow cook before that, any marinating or brining lead time the entry states before that — and the event title says *(from the badge, not a countdown line)* so he knows it is the coarser read.
- **Leftover days get one event: the dinner, with the "warm and build" minutes as the start.** Nothing outdoors — *"all leftovers does not need the grill."* A **"leftover meat"** day still gets the events for everything that *is* being made that night; only the meat's own cooking stages come off.
- **🧊 The thaw event is a stage type, and it ranks with a dry brine or a two-day sous vide** — [CLAUDE.md §3f](../../CLAUDE.md). Cody: *"not thawing the meat is a thing that we do. We forget to thaw the meat sometimes."* **Ask whether the meat is frozen whenever he hasn't said.** Leftovers from earlier in the same week's plan are in the fridge and already thawed — no event. Anything else is presumed frozen and gets one, counted back from dinner on **USDA FSIS refrigerator-thawing figures**: **a vacuum-sealed bag of shredded or pulled pork, a full day (T−24 hr, so start it the morning before); a whole chuck roast out of the [§1 Cody's Pho](1-codys-pho.md) sous vide batch, 2 days (T−48 hr).** Ranges and doubts go **early** — thawing ahead costs nothing, since FSIS keeps thawed red-meat cuts 3 to 5 days in the fridge. Title it like any other stage (*"Tue dinner — thaw the pulled pork, fridge (§6.9)"*). **Default to a calendar event; he is still deciding between an event, a reminder, or both** — *"maybe we should do both, quite frankly."*
- **Ask before writing to the calendar the first time in a session; after that, write and report.** Show the whole event table before creating anything.

#### 4. Deliverable three — the week's cooking document

One document, Monday through Saturday (or whatever days he named), in day order. For each day:

1. **The day header:** day, dinner time, the main and sides, the countdown line(s) for that day.
2. **Each recipe's A. Ingredients and B. Cooking Instructions, verbatim from its `planner/recipes/` file** — bold steps, detail paragraphs, timers, warnings, all of it. No paraphrase, no shortening: the whole point of the document is that it says what the cookbook says.
3. **The leftover day cross-references its source** (*"the pork is Monday's §6.9 — see above"*) instead of repeating the source recipe.
4. **Sauces the line names in parentheses** (the [§7.151](7151-sous-vide-chicken-thighs-for-the-family-seared.md) sauce picks, the [§7.61](761-broiled-fish.md) fish sauces) are included in full for whichever one he chose.

Deliver it as a downloadable document (Word if he asks for Word; otherwise markdown or PDF) **and offer to send it through Gmail** in the same turn. The grocery list from §2 goes at the top of the same document as a backup to the phone list.

#### 5. Deliverable four — cooking with the document open

He will read the document and talk at the same time. The rules for that conversation:

- **Answer from the recipe file, not from memory.** Fetch `planner/recipes/<anchor>.md` for the dish he is on and quote the step. If he asks something the entry does not say, say that, and give the cookbook's nearest reference ([§T44](t44-food-safety--the-real-logic-and-the-target-temperature-table.md) for temperatures, [§T1](t1-how-to-make-a-roux.md) for roux, [§T17](t17-the-raw-egg-soak-deodorizing-fish--shellfish.md) for the soak) rather than a guess.
- **Temperatures are Fahrenheit** unless the entry prints otherwise — [CLAUDE.md §6](../../CLAUDE.md).
- **Doneness and safety answers cite the entry's own figure** and, where the entry is silent, USDA FSIS — never a rounder number from memory.
- **If he changes something while cooking** (*"I added another teaspoon of hot sauce"*), write it down as a revision to make in the master file, with the date, and remind him at the end. Chat does not edit the book; the next Code session does, per [CLAUDE.md §4](../../CLAUDE.md).

#### 6. What can go wrong, and the check for each

| Failure | Check |
|---|---|
| The chat read an old copy of the book | Every fetch is the raw GitHub URL of a `planner/` file; the file's first line says which anchor it was generated from |
| A dish matched the wrong line | The plan table in §1 is read back before anything is built |
| A calendar event lands after dinner | Every offset is subtracted, never added; ranges go early; the event table is shown before it is written |
| The grocery list double-buys a leftover's source | Leftover rows add only their own build ingredients |
| A cook was planned for meat that is already cooked | The leftovers question is asked before the grocery list is built — which meat, and is it frozen ([CLAUDE.md §3f](../../CLAUDE.md)) |
| The meat was still frozen at dinner time | Every presumed-frozen leftover gets a thaw event on FSIS figures, placed early |
| The instructions were paraphrased | Section B is pasted from the file, not retyped |
| `planner/` is stale | It is rebuilt (`python3 tools/build_planner.py`) in the same commit as every master-file change; if a recipe he names is missing there, the next Code session rebuilds it |
