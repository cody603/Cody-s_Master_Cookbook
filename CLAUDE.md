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

## 3e. Rare or Hard-to-Find Ingredients

**Added 2026-09-09, from Cody's own reasoning on [§7.85 Hanger Steak with Duck Fat Wild Mushrooms](codys-cookbook.md#785-hanger-steak-with-duck-fat-wild-mushrooms):** *"we don't have duck fat, can we substitute that with tallow or something else... some of these recipes call for rare ingredients... it's just gonna deter the decision-making process... we can still order it from Amazon or online."*

**When a recipe calls for a genuinely hard-to-find ingredient, note a workable substitute and/or mention that it's orderable online**, right alongside the ingredient — so the ingredient doesn't quietly talk someone out of picking that dish off the [Meal Planning Sheet](codys-cookbook.md#meal-planning-sheet). A substitute suggested this way is cookbook judgment per §3d — label it as such, name what it's reasoned from, and never alter the source's own printed ingredient line to do it; the substitute goes alongside the transcription, not in place of it.

**Scope: this does not mean auditing every rare ingredient in the book at once.** It was applied narrowly to §7.85 on 2026-09-09, one entry at a time as they come up — a full-book pass looking for every hard-to-find ingredient is a separate, larger task, only worth doing if Cody asks for it.

## 3f. Leftovers Are Spoken, Not a Sheet Category

**Added 2026-09-12 at Cody's direction, and it retires a thing this cookbook built for him.** The [Meal Planning Sheet](codys-cookbook.md#meal-planning-sheet) carried a **🍱 Leftovers** group from 2026-09-09 until 2026-09-12. He called it his own mistake and asked for it gone:

> *"I improperly said, made you put in a leftover section, and I think that that's a waste. I think it's silly. What I need you to do instead is, if I have leftovers, I'm just going to verbally tell you that there are leftovers."*

**So: leftovers are something he says out loud while planning a week. They are not a category on the sheet, and the sheet must never grow the group back** — not as a convenience, not as a kindness, not because a leftovers line "would be useful." Every recipe that group held is still on the sheet, in its own regular group. The three lines that lived nowhere else moved there on 2026-09-12: [§8.47 Frito Pie](codys-cookbook.md#847-frito-pie) into 🥣 Soups, Gumbos & Chili, [§7.146 Pho with Leftover Beef](codys-cookbook.md#7146-pho-with-leftover-brisket-and-smoked-bone-broth) into 🍜 Pasta, Rice & Noodle Bowls, and [§7.1 Cody's Pulled Pork Street Tacos](codys-cookbook.md#71-pulled-pork-tacos) into 🐖 Pork. *(Later the same day Cody merged Frito Pie into [§8.1 Chili Mac & Frito Pie](codys-cookbook.md#81-chili-mac--frito-pie), so that moved line is now the merged entry's line — still on the sheet, still in 🥣 Soups, under both names.)*

### The two things he can say, and they do not mean the same thing

**1. "Leftover meat" — subtract the meat, and only the meat.** This also covers *frozen meat*, *previously cooked meat*, and anything of that shape.

> *"If I say specifically leftover meat, we'll still have, for instance, for the street tacos, you'll still have to cut the fresh cilantro, lime, and all of that. However, you won't have to cook the pork. Same with pulled pork sandwiches — we'll have to buy buns, we'll have to likely create pickled pink onions for both, but we won't have to cook the meat, and that's one of the hardest steps sometimes."*

> *"Whenever I say leftover meat… you can subtract all the grocery ingredients for that meat, and you could subtract the cooking instructions for that meat, because we already have it cooked."*

Drop that meat from the grocery list, and drop its cooking stages from the instructions **and from the calendar**. **Everything else in the dish still happens.** Cilantro, lime and onion still get chopped for the street tacos; buns still get bought for the sandwiches; [§4.5 Pickled Pink Onions](codys-cookbook.md#45-pickled-pink-onions) still likely get made for both. Subtracting the meat is not subtracting the meal.

**2. "Leftover [the dish]" — the whole meal is leftovers.** *"Leftover street tacos"* names the dish, not the meat, and it means nothing is shopped and nothing is made.

> *"If I say I've got leftover street tacos, then that's leftover street tacos as a whole, not just leftover meat. I will tell you if we've got leftover meat only."*

This is what happens when the dish was already eaten earlier in the same week — the chopped onion, the cilantro and the lime are left over too.

**He will say which one he means.** Leftover meat is by far the more common of the two. A leftover that isn't meat is a possible anomaly rather than a pattern — **ask when one comes up** rather than assuming which reading applies.

### Frozen or thawed — ask if he didn't say

> *"If it's frozen — if I don't specify if it's frozen or not, you need to ask me, because we're gonna have to create a calendar event that says, hey, you've got to thaw the meat from the freezer."*

Two standing readings:

- **Leftovers from earlier in the same week's plan are in the fridge, already thawed.** No thaw event. His own example: street tacos Monday, pulled pork sandwiches Tuesday, the same pork — *"you can safely assume — and feel free to ask — that the leftover meat will already be thawed, because I'm using the leftover pulled pork from the night before."*
- **Anything else is presumed frozen until he says otherwise, and a frozen item earns a thaw event**, placed back from the meal like any other countdown stage.

**Forgetting to thaw is the exact failure this rule exists to prevent.** In his words: *"Not thawing the meat is a thing that we do. We forget to thaw the meat sometimes. So having those reminders is helpful, just like it would be to sous vide ahead of time, or to salt brine, dry brine in the fridge the night before, two nights before, or a two-day sous vide cook."* **A thaw event ranks with a dry brine or a two-day sous vide** — a real scheduled stage, not a nicety.

**Calendar event, reminder, or both — his open preference.** *"That should be either a reminder or a calendar event… maybe we should do both, quite frankly. I will revise later."* **Default to a calendar event** and say so when you make one; do both if he asks. Revisit when he revises.

### Thaw times — researched, never guessed

**Per §3d, thawing is a food-safety question, so the figures come from USDA FSIS and nowhere else.** Two published FSIS figures do all the work here:

- **"A large frozen item like a turkey requires at least a day (24 hours) for every 5 pounds of weight,"** and **"even small amounts of frozen food — such as a pound of ground meat or boneless chicken breasts — require a full day to thaw."** *(USDA FSIS, "The Big Thaw — Safe Defrosting Methods.")*
- **In the refrigerator, "ground beef, stew meat and steaks may defrost within a day," while "bone-in parts and whole roasts may take 2 days or longer."** *(USDA FSIS, "Beef From Farm to Table.")*

**Applied to the two cases that actually come up in this house — the reading is the cookbook's, the numbers are FSIS's:**

- **A vacuum-sealed bag of shredded or pulled pork — allow a full day, 24 hours, in the fridge.** Even a one-pound package gets a full day under FSIS's rule, and these bags run two to four pounds. **Start it the morning before dinner, not the night before** — *"I'm not sure how long a whole bag of shredded pork takes to thaw"* is his own open question, and this is the safe-side answer to it.
- **A whole chuck roast frozen after the sous vide — allow 2 days.** It is a whole roast, and FSIS puts whole roasts at *2 days or longer*; the 24-hours-per-5-pounds rate agrees for the 3-to-5-pound roasts he batches for [§1 Cody's Pho](codys-cookbook.md#1-codys-pho). Two or three roasts thawing in one fridge are slower still, not faster.

**Thawing early is cheap, so err early.** After refrigerator thawing, FSIS keeps red-meat cuts — beef, pork and lamb roasts, chops and steaks — **3 to 5 days** in the fridge before cooking, and ground meat, stew meat, poultry and seafood **an additional day or two**, so a thaw started a day ahead of schedule costs nothing.

**These are FSIS's raw-item figures read onto already-cooked frozen meat, which is the conservative direction.** They are working planning figures, not lab measurements, and **Cody's own figures supersede them the day he gives them** — he said he would revise.

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
- **The healthy chip is the Siete *maíz* (corn) tortilla chip in 100% avocado oil — that is the default, and it is bought in a store, never ordered.** *(Cody, 2026-09-12: "the healthy way is these Siete maíz corn tortilla chips that use a hundred percent avocado oil… you can default to the corn tortilla chip, the Siete, instead of the almond flour. Those almond flours are rather expensive. And if I specifically specify, then I'll tell you.")* **Xochitl avocado oil tortilla chips** are the named alternative; **Siete almond flour chips** are the keto option and only when he asks for them by name. **On where they come from he was explicit:** *"I want to have those in store, in Walmart. I don't wanna have to order those Walmart Plus, just so you know — those should be from the regular grocery store."* So they are an in-person grocery buy, they never go on an online order, and **§3e's "you can order it online" treatment does not apply to them.** Written up at [§8.1 Chili Mac & Frito Pie](codys-cookbook.md#81-chili-mac--frito-pie).
- **Cody keeps a standing stash of [§4.108 Meathead's Memphis Dust](codys-cookbook.md#4108-meatheads-memphis-dust) on hand at all times.** *(Cody, 2026-09-09: "Memphis Dust, I have a huge amount of it at all times.")* This is guidance for conversational grocery-list building only — it can be skipped there without checking. It does **not** mean stripping Memphis Dust from any recipe's own printed Grocery Shopping List in the master file; those stay complete per §3.

## 7. Out of Scope for Code Sessions

Two jobs from the old setup live in regular Claude chat, not here:

- **Grocery pushes to Reminders** — the Reminders integration isn't available in Code sessions. The grocery list in each recipe stays current here; pushing items to phones happens in a normal chat.
- **Live cooking tutor mode** — walking someone through a recipe step by step happens in regular chat/voice, not in a Code session.

## 8. The Chat Side Lives in the Repo

**Added 2026-09-12 at Cody's direction.** The family uses the cookbook from regular Claude chat through a *master-cookbook* skill, and Cody wants that skill **fixed and minimal** so nobody has to update theirs when a rule changes:

> *"I want the skill to only reference the code, and the code continually gets updated… otherwise, when I give this skill to all the different family members, they're gonna have to rewrite their skill every time I update it."*

**So the skill is one paragraph that points at one file, and everything else is in this repo.** Three hand-maintained files at the root, none of them cookbook content:

- **`CHAT.md`** — **the chat operating manual.** The skill sends every chat session here first. It says where to read (the generated `planner/` folder — never the 4 MB master), how to talk (short by default; details on request), how to plan a week, how to build and push the grocery list, the refresh rule when something changed mid-conversation, what chat may write down, and the one-time setup each family member needs. **When a rule in this file or in the book changes in a way that affects a chat session, update `CHAT.md` in the same commit.** The reference copy of the skill is `tools/master-cookbook-SKILL.md`. **It carries exactly one thing that cannot live in the repo — the trigger**: a skill's description is what decides whether it fires, so the skill spells out when the conversation is about food cooked at home (planning, groceries, a house dish, cooking live, feedback on a meal, leftovers, timing, substitutions, household groceries) and when it isn't (restaurants, eating out, *"what's good in Columbia, Missouri"*). Cody, 2026-09-12: *"I want that trigger to be accurate and thoughtful every time… once the trigger happens, then the GitHub file gets executed."* Everything after the trigger is `CHAT.md`, which mirrors the trigger list in its §0. The skill changes only if the trigger needs to; the logic never requires it. **Two hard constraints on the skill file, learned by tripping them: the description may not contain angle brackets** — a validator reads `<anything>` as an XML tag and rejects the upload, which is what a placeholder like *"what's good in <a town>"* did on 2026-09-12 — **and it must stay a single-line, double-quoted YAML string** with no interior double quotes. Write placeholders in words, never in brackets, and re-check with a grep for `[<>]` before handing the file to anyone.
- **`PROPOSED-REVISIONS.md`** — **the intake queue.** Anyone using the book from chat — Vicky above all — records things that *should* change without changing them: an ingredient that wasn't at Walmart, a substitution, a wrong quantity, a wanted recipe. *(Cody: "I don't want her revising the code completely… I'd like that to be noted in a proposed revisions log that's proposed by somebody else.")* **Every Code session reads this file at the start and reviews the Open entries with Cody.** His own entries can be applied directly; everyone else's are applied only on his OK, then moved to Done or Declined with the date and outcome. A chat session that can't write to the repo emails the entry to Cody in the same format.
- **`HOUSEHOLD-STAPLES.md`** — **groceries that aren't recipes.** Cody's rule for what belongs where: *"quick pickles should go into the family cookbook because… it requires cooking. Cottage cheese and all that stuff… doesn't go in a cookbook, but should be included into the refrigerator list."* So fruit, snacks, Nutella and croissants, sandwich fixings live here, not in the master file, and the weekly grocery list pulls from here after the recipes' own lists. **Chat may append to it directly** (dated, attributed) — it is a shopping list, not the book, and needs no sign-off. The fridge sheet's own No-Cook rows stay Cody's picks and change only at his word.

**What this does not change:** the master file is still the single source of truth, still edited only here, still one file. `planner/` is still generated, never hand-edited, and must be rebuilt (`python3 tools/build_planner.py`) in the same commit as any master-file change — its `README.md` carries a build stamp that chat sessions compare against the top of `CHANGELOG.md`. Nothing in these three files is cookbook content, so §2's rule against splitting the book is not touched.
