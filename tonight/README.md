# tonight/ — the night's cooking sequence, one file per night

**This is where the live-cooking chat reads from.** Stage 2 (the Opus build — `CHAT.md` §5) does the thinking once and writes the result here; the live walkthrough (`CHAT.md` §7) fetches the file and reads it one step at a time. Nothing gets re-derived in the kitchen.

Cody, 2026-09-14: *"When you're doing the chat, you don't have to do much thinking, because all of the logic was already predetermined, and all you're doing is referencing things very quickly… it just needs to be easily accessible. With the Word doc I have to actually manually share this thing."* This folder is the fix: the file is fetched by URL like everything else in the system, so there is nothing to share.

## Naming

One file per night, named by the date of the dinner: **`tonight/2026-09-14.md`**. A week planned on Sunday writes seven files at once. The live chat fetches `tonight/<today>.md` from `https://raw.githubusercontent.com/cody603/Cody-s_Master_Cookbook/main/tonight/<today>.md`; if it isn't there, no plan was built for that night, and the chat says so and offers to build one.

## What's in the file

The merged sequence exactly as [§T112 §3](../codys-cookbook.md#t112-cooking-the-whole-meal--sequencing-several-dishes-and-the-spoken-walkthrough) specifies — the same content as the Word doc, in markdown:

1. **Title line** — the night, the dishes, the dinner time, who's cooking if known.
2. **Substitution line** — *if a dish changed, skip every step tagged for it.*
3. **Ingredients per dish**, verbatim from each recipe, grouped by dish.
4. **One numbered sequence** in cooking order: every step tagged *(for the X)*, simultaneous steps as an *"At the same time:"* block, precision stages marked *full attention*. **Each step that has a technique names its §T file in brackets** — `[t2-hot-pan-first-then-oil.md]` — so the chat fetches it without a tag lookup.
5. **Swaps made tonight** — a short list at the bottom, added *during* cooking: *coriander → cumin + a squeeze of lime (looked up: Nosrat)*. Empty until something changes.

## Who writes here

- **Stage 2 writes the file** when the night's document is built. If a Word doc or an email is wanted too, that's on request — this file is the one that has to exist.
- **The live chat edits the file** for a mid-cook swap (appending to *Swaps made tonight* and adjusting that dish's remaining steps), so *"where were we?"* survives a dropped connection and the swap is on record for the cooking log.
- **Nobody else.** Code sessions don't hand-write these; they're generated from the planner files by the chat.

## What this folder is not

Not the cookbook, not the printed book, not the log. Files here are working papers for one night. They can stay for the record — `COOKING-LOG.md` links the night's row to its file — but nothing in them is ever the source of truth for a recipe. A swap that should become permanent is a revision request in `PROPOSED-REVISIONS.md`.
