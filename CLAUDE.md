# CLAUDE.md — Cody's Master Cookbook

These are the permanent rules for this repo — referred to as the **project instructions** (or **cookbook instructions**). They change only when Cody explicitly asks to revise them; when he does, edit this file.

## 1. Purpose

This repo maintains **Cody's Cookbook**: one living markdown file, `codys-cookbook.md`, at the root of this repo. It is the single source of truth. Claude Code's job here is **cookbook editor** — keep the master file organized, complete, and current.

The cooking style is hands-on and conversational: Cody talks through methods in plain language, and Claude organizes and formalizes them into the cookbook.

## 2. The Master File Workflow

Every time a recipe is added or changed:

1. **Read the entire `codys-cookbook.md` first.** Never edit from memory or a partial view.
2. **Edit the file in place.** No copies, versioned filenames, or side files — git history is the backup system.
3. **Commit directly to `main`.** No branches, no pull requests — just commit straight to main with a clear message. (Git keeps every version, so any bad edit can be rolled back.)
4. **Use scripting for bulk edits** rather than manual string replacement when many sections change at once.

The cookbook keeps a **table of contents** and a **changelog** at the top, plus one section per recipe. Every change gets a changelog line with the date and what changed.

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

Low-carb recipes may also carry **net carbs** when the source gives them, since that's the number that matters for the §11 keto entries.

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

- **Cody's Pho** is the first documented recipe.
- Chuck roast is the meat for the pho — not brisket.
- Sous vide dry rub is kosher salt, garlic powder, black pepper only. No five spice, no fresh garlic, no liquid in the bag.
- Sous vide temp: 131–133°F for 24–48 hours.
- Fresh garlic in a sous vide bag is an anaerobic botulism risk; garlic powder is the safe substitute.

## 7. Out of Scope for Code Sessions

Two jobs from the old setup live in regular Claude chat, not here:

- **Grocery pushes to Reminders** — the Reminders integration isn't available in Code sessions. The grocery list in each recipe stays current here; pushing items to phones happens in a normal chat.
- **Live cooking tutor mode** — walking someone through a recipe step by step happens in regular chat/voice, not in a Code session.
