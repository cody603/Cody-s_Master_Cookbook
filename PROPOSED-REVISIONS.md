# Revision Requests

**Anyone with the master-cookbook skill can write here. Nobody but Cody approves.** This file is the one place a chat session writes to. It is not the cookbook; it is the queue of things people want changed. Cody, 2026-09-12: *"I wanna make it one hundred percent open to writing from people who have my master cookbook skill… they can say, well, we're buying Nutella a lot and it's not one of our staple grocery list items, can we add that? — and it says, I have put that down as a revision request. When Cody approves it, it will be implemented."*

## What goes here — anything at all

If someone wants something in the cookbook, the fridge sheet, or the grocery lists to be different, it's a revision request. There is no wrong kind. Examples Cody gave:

- **A household grocery item** — *"we're buying Nutella a lot, can we add it as a staple grocery item?"*
- **A taste note** — *"there needs to be less salt in this."*
- **A specific quantity** — *"you said less rice, but there should be exactly this much rice in the lemon chicken soup."*
- **The fridge sheet's contents** — a dish that should be on it, or off it, or in a different group.
- **The fridge sheet's look** — *"even the font size of the refrigerator sheet."*
- **A shopping problem** — *"Walmart didn't have serrano peppers, I used a jalapeño."*
- **A new recipe** — a card, a photo, a phone call from a relative, *"write this up."*
- **A rating** — *"we loved it,"* *"the kids wouldn't eat it."*

## Who

Anyone using the skill. **The chat asks the person's name once and puts it on the entry.** The family, as Cody named them *(spellings transcribed from voice — Cody, correct any that are wrong)*: **Cody** (owner — approves everything, and his own requests are applied without waiting), **Vicky**, **Calter**, **Mabel**, **Craig**, **Joeta**, **Darcy**. Someone not on this list can still file; the chat just writes the name they give.

## How a chat session writes here — exact procedure

1. **Read this file** from the repo (GitHub connector: get the file's contents; you need its current `sha` to write it back).
2. **Insert the new entry directly below the line that says `<!-- NEW ENTRIES GO DIRECTLY BELOW THIS LINE -->`**, in the format shown. Newest first. **Never change or delete anything already in the file.**
3. **Write the whole file back** (create-or-update, with the `sha` from step 1), commit message: `Revision request: <dish or topic> — <name>`.
4. **Say this to the person, in these words:** *"I've put that down as a revision request. When Cody approves it, it'll be implemented."*
5. **If you can't write to the repo** — no GitHub connector, or no permission — **email the entry to Cody instead** through Gmail, subject *"Cookbook revision request: <dish or topic>"*, and say: *"I've sent that to Cody as a revision request. When he approves it, it'll be implemented."* Never let a request go unrecorded.

**Entry format** — copy it exactly; keep it to these four lines:

```
### 2026-09-12 · Vicky · Lemon Chicken Soup (§8.4) · quantity
**Request:** There should be 1 cup of rice in the lemon chicken soup, not "less rice."
**Why:** That's how much we actually use and it comes out right.
**Suggested by chat:** update the ingredient line and the step that adds the rice; note it as Vicky's figure.
```

The fourth field on the heading line is the kind of request: `recipe` · `quantity` · `taste` · `fridge sheet` · `sheet look` · `household grocery` · `shopping problem` · `new recipe` · `rating` · `other`.

## How it gets done

Every Claude Code session reads this file first, reviews the **Open** entries with Cody, applies the ones he approves to the master file (or the fridge sheet, or `HOUSEHOLD-STAPLES.md`), and moves each entry to **Done** or **Declined** with the date and a one-line outcome. **Cody's own entries are applied without waiting.**

---

## Open

<!-- NEW ENTRIES GO DIRECTLY BELOW THIS LINE -->

*(nothing open)*

## Done

*(nothing yet)*

## Declined

*(nothing yet)*
