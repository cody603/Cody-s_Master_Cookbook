# CLAUDE.md — Cody's Master Cookbook

These are the permanent rules for this repo — referred to as the **project instructions** (or **cookbook instructions**). They change only when Cody explicitly asks to revise them; when he does, edit this file.

## 1. Purpose

This repo maintains **Cody's Cookbook**: one living markdown file, `codys-cookbook.md`, at the root of this repo. It is the single source of truth. Claude Code's job here is **cookbook editor** — keep the master file organized, complete, and current.

The cooking style is hands-on and conversational: Cody talks through methods in plain language, and Claude organizes and formalizes them into the cookbook.

## 2. The Master File Workflow

Every time a recipe is added or changed:

1. **Read the parts of `codys-cookbook.md` you are about to touch, in full, before touching them.** Never edit from memory. The file has passed 4 MB and can no longer be read end to end in a single pass, so the working method is: grep for the section heading, read that entry with offset/limit, and read every entry that cross-references it. Never edit an entry you have not just read.
2. **Edit the file in place.** No copies and no versioned filenames — git history is the backup system. **One exception, added 2026-09-08 at Cody's direction: the changelog lives in its own file, `CHANGELOG.md`.** It grew past the point where it could ride along in the master file. Nothing else may be split out without Cody saying so.
3. **Commit directly to `main`.** No branches, no pull requests — just commit straight to main with a clear message. (Git keeps every version, so any bad edit can be rolled back.)
4. **Use scripting for bulk edits** rather than manual string replacement when many sections change at once.

The cookbook keeps a **table of contents** at the top plus one section per recipe. **The changelog is `CHANGELOG.md`, newest entry first.** Every change gets a changelog line there with the date and what changed — that requirement has not relaxed, only moved.

Default format is markdown. Do **not** produce a Word document or any other format unless Cody explicitly asks.

## 3. Recipe Structure

Every recipe has **exactly three sections, always in this order**:

### A. Ingredients

Full list with quantities. This is the authoritative list — it must always match what the instructions actually call for.

### B. Cooking Instructions

Two-layer format:

- **Numbered main steps in bold.** The skeleton — what to do, in order, readable at a glance.
- *Unbolded detail paragraphs beneath each step.* The "why and how" — technique, doneness cues, timing, warnings, sensory checkpoints.

Example of the intended feel:

> **3. Make the roux.**
> Equal parts fat and flour over low heat. Keep stirring — constantly, not occasionally. A roux will go from perfect to burnt in under a minute if you walk away or push the heat. You're looking for a color just shy of chocolate brown. If you see black flecks, throw it out and start over; scorched roux will ruin the whole pot.

Include timers in the step text wherever there's a duration ("stir 8 minutes, then add the broth").

### C. Grocery Shopping List

Split by store, using these prefixes:

- **HK** — Hong Kong Market / Chinese market items
- **GEN** — general grocery store (anywhere works)
- For a specific store, GEN plus the store name in parentheses: `GEN Fig jam (Trader Joe's)`, `GEN Harissa paste (Whole Foods)`

## 3a. Difficulty & Time Badge

Every written-up recipe carries a one-line badge above its Ingredients, and a matching row in the **Difficulty & Time Index** near the top of the cookbook. Placeholders don't get one — there's no method to time yet.

**Difficulty is technique risk, not effort.** 🟢 Easy · 🟡 Medium · 🔴 Hard. Hard is reserved for things that can genuinely fail on you — roux above all. An 8-hour crock pot is Easy, because none of those hours can go wrong. A 15-minute roux is Hard.

**Roux comes in three tiers, and only the darkest earns a 🔴** *(Cody, 2026-09-07: "use your judgment on the roux, because some is dark and some is light — I think a bisque is a light version, which is less hard")*:

- **Dark roux** — chocolate, mahogany, "dark brown," "dark red-brown to black" → **🔴 Hard.** This is the one that goes from perfect to burnt in under a minute.
- **Brown / medium roux** — peanut-butter colored, copper, "brown," "medium brown" → **🟡 Medium.** It can still scorch, but the window is wider and the target more forgiving.
- **Blond / light / white roux** — pale, a couple of minutes, never colored; the base of a béchamel, a velouté, or a butter-thickened cream sauce → **earns nothing on its own.** Rate the recipe on whatever else it does.

**The color target sets the tier, not the quantity.** A two-tablespoon roux taken to dark is 🔴; a cup of blond roux is not. And a roux never *lowers* a rating that another technique has already earned — emulsions, caramel, and meringue folds keep their own difficulty regardless.

**Long is not hard. A big recipe is not automatically a 🔴.** The test is always the same: *can a step go from perfect to ruined?* If nothing can, it's Easy no matter how many hours or components it involves. **[§1 Cody's Pho](codys-cookbook.md#1-codys-pho) is the reference case** — two days, two hours of prep, more moving parts than anything else in the book, and rated 🟢 Easy, because not one of its steps can fail on you. In Cody's words, *it's a long distance run.* Length, component count, and lead time belong in the **time** fields; they must never inflate the difficulty rating.

**Time is split three ways, and the third one matters most:**

- **Prep** — hands-on work before and between cooking. Chopping, mixing, dredging, skewering, breaking down a chicken.
- **Cook** — actual cooking you're engaged with, plus short unattended stretches (a 20-minute bake, a 40-minute simmer). Annotate the unattended portion when it's a big share of the number.
- **Slow cook** — its own separate category. **Long, mostly hands-off cooking where the waiting *is* the method**: smoking meats, a roast or turkey in the oven, a crock pot, a long braise or bean pot, stock and pho broth, sous vide, dehydrating.

**Why slow cook is separate:** a 4-to-8-hour smoke or crock pot does *not* take long to make — it takes ten minutes to make and then it cooks itself. Rolling that into "cook time" makes the easiest recipes in the book look like the most demanding ones, which is backwards. Never put a multi-hour hands-off stretch in the Cook field.

**Rule of thumb:** roughly 2 hours or more of hands-off cooking is Slow cook. So are smoker, crock pot, sous vide, and dehydrator work at *any* length, since those are slow-cook methods by nature. Everything shorter stays in Cook.

Lead time that isn't cooking — marinating, chilling, an overnight bean soak — is noted too, since it changes when you start rather than how hard you work.

Format:

> **🟢 Easy** · **Prep ~15 min** · **Cook ~10 min** · **Slow cook 4 hr** *(crock pot)* · **Start to finish ~4 hr 25 min**

Omit any field that doesn't apply. **Sort the index by prep + cook** — the time that actually costs you — not by start-to-finish.

## 3b. Nutrition

Every written-up recipe carries a **Nutrition** block after its Grocery Shopping List. Placeholders don't get one.

**Report five numbers, two ways:** calories, fat, protein, carbs, and fiber — once for the **whole dish** and once **per serving**, with the serving count stated. Pure reference sections (§T2–§T7) are skipped; they aren't dishes.

**Where the numbers come from:**

- **If the source page prints them, use those and say so** — mark the block *(per serving, as printed on the source page)* and calculate the whole-dish figures from them. Never overwrite a publisher's numbers with an estimate.
- **Otherwise estimate from the ingredient list** and mark the block *(estimated)*. Add up the actual ingredients and divide by a sensible serving count. These are working estimates for planning, not lab figures — say so rather than implying false precision.
- **When the recipe has no quantities** (some handwritten cards don't), say that plainly in the block and flag it in Open Questions. An estimate built on assumed amounts must be labeled as such.

**Always describe what a serving actually is, in plain language.** A number without a portion is useless — "420 calories per serving" means nothing until you know whether that's half a cup or a full plate. Describe it the way a person would: *"about 1½ cups — a normal dinner bowl,"* *"one 6 oz cutlet,"* *"¼ cup, a few scoops with crackers,"* *"½ cup rice with a ladle of beans over it."* Where the source states its own portion, use that.

**Account for what's actually eaten.** Marinade left in the bag, oil that stays in the fry pot, a dredge that half falls off, oxtail pulled out and discarded, brine poured off — none of that lands on the plate. Estimate the eaten portion, not the shopping list.

Format:

> #### Nutrition *(estimated)*
>
> | | Calories | Fat | Protein | Carbs | Fiber |
> |---|---|---|---|---|---|
> | **Whole dish** | ~1,350 | 63 g | 112 g | 86 g | 13 g |
> | **Per serving** *(serves 4)* | ~340 | 16 g | 28 g | 21 g | 3 g |
>
> **What a serving is:** a generous 1½-cup bowl.

## 3c. Keto / Low-Carb Tagging

**If a source prints net carbs, the recipe is keto — tag it.** That's the reliable signal: net carbs is a low-carb metric, and no ordinary recipe bothers to print it.

Keto recipes carry:

- **🥑 Keto** as the first item on the difficulty/time badge line
- **🥑** after the ✅ in the Table of Contents
- **Net carbs per serving**, stated in the Nutrition block
- A row in the keto callout under the Difficulty & Time Index

Tag by the recipe's own content, not by which section it sits in. Keto recipes turn up outside §11 — the fried chicken lives in §7 Mains — so the tag is what makes them findable as a group.

**The recurring substitutions** across these are worth recognizing when a new one arrives: cauliflower for potatoes, almond flour and oat fiber for wheat flour, erythritol for sugar, whey protein powder for breading. When a new keto recipe uses one of these, cross-reference the others that already do.

## 3d. "Use Your Judgment" — What That Actually Requires

**Added 2026-09-08 at Cody's direction.** When Cody says **"use your judgment," "figure it out," "you decide,"** or anything of that shape, that is not permission to guess. It is an instruction to go research it properly and then write it down with its basis.

**In his words:**

> *"If I say I'd like you to figure it out — from now on, if I say something like that or use your judgment — I'd like you to look at a really credible cooking source. Professional chefs, tried-and-true websites that aren't just a Pinterest or Facebook flare. These are real chefs with real credentials, and I'd like you to look through what they have to say."*

**What counts as a source:**

- **This cookbook first.** If something already here answers it, that beats anything external — it's already sourced, and it keeps the book internally consistent. *(Example: "3 mild hot peppers" was answered from [§T105](codys-cookbook.md#t105-chiles-chipotles-in-adobo-and-paprika-the-meathead-method)'s own Scoville table, not from a web search.)*
- **Named cookbook authors already in this book** — Prudhomme, Raichlen, Meathead, Julia Child, Nosrat, Canal House.
- **Professional test kitchens and chefs with real credentials** — the kind of place that tests a recipe before publishing it.
- **Government food-safety sources** for anything about temperature or safety — USDA FSIS above all.

**What does not count, and must never be used:**

- **Pinterest, Facebook, and social recipe reposts.** Cody named these specifically.
- **SEO content farms and recipe aggregators** — the sites that rank well and cook nothing.
- **User-submitted recipe archives and anonymous copycat pages.** A copycat recipe posted by an unnamed user is not a source; it's a guess with formatting. *(This rule exists because one was used, on 2026-09-08, for [§4.7 Captain Mike's](codys-cookbook.md#47-captain-mikes-seasoning) — Cody rejected the result outright.)*

**How to write it up, every time:**

1. **Label the fill as cookbook judgment** — plainly, where a reader will see it, not buried in a footnote.
2. **Name the source you reasoned from.** Publication and author or recipe name is enough. **Do not attach a URL you cannot verify from this environment** — a wrong link is worse than no link.
3. **State what is Cody's and what is the cookbook's.** The ingredients, the order, the technique may be his; if the numbers are yours, say so in that sentence.
4. **Say plainly that his own figures supersede yours** the day he gives them. They always do.
5. **Log it in `CHANGELOG.md`** like any other change.

**And judgment has a limit: it fills gaps, it does not invent facts.** If the honest answer is that the source never says and no credible reference covers it, that stays an Open Question. Never dress a guess up as research.

## 4. Handling Recipe Revisions

Cody will frequently come back after cooking and ask for a tweak — e.g., "Add another teaspoon of hot sauce to Crawfish Elegante."

When that happens, propagate the change **everywhere**, not just where he mentioned it:

1. Update the **Ingredients** list (quantity or new line item).
2. Update the **Cooking Instructions** wherever that ingredient appears.
3. Update the **Grocery Shopping List** if it's a new item or a quantity that affects buying.
4. Add a **changelog** line with the date and what changed.

If a tweak conflicts with something already documented, flag it clearly in the commit message rather than silently overwriting.

## 5. Protection Rules

- **Never delete a complete recipe** (e.g., Cody's Pho) unless specifically requested. Add and revise, don't remove.
- When Cody says "add to" or "update" the master file, that means edit `codys-cookbook.md` — always the master file, never a new file.
- Deletions Cody explicitly requests are fine — git history preserves everything, so no manual backup copies are needed. Just note the deletion in the changelog and commit message.

## 6. Established Kitchen Facts (do not re-litigate)

- **Every temperature in this cookbook is Fahrenheit unless it explicitly says otherwise.** *(Cody, 2026-09-08: "when I say 150 degrees, I'm always talking in Fahrenheit — that should be throughout the cookbook.")* When he dictates a bare number, read it as °F. Where a transcribed source prints Celsius, keep the source's figure and give the °F conversion alongside it.
- **Cody's Pho** is the first documented recipe.
- Chuck roast is the meat for the pho — not brisket.
- Sous vide dry rub is kosher salt, garlic powder, black pepper only. No five spice, no fresh garlic, no liquid in the bag.
- Sous vide temp: 131–133°F for 24–48 hours.
- Fresh garlic in a sous vide bag is an anaerobic botulism risk; garlic powder is the safe substitute.

## 7. Out of Scope for Code Sessions

Two jobs from the old setup live in regular Claude chat, not here:

- **Grocery pushes to Reminders** — the Reminders integration isn't available in Code sessions. The grocery list in each recipe stays current here; pushing items to phones happens in a normal chat.
- **Live cooking tutor mode** — walking someone through a recipe step by step happens in regular chat/voice, not in a Code session.
