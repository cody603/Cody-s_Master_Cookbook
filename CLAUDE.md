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
