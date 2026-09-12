<!-- GENERATED from codys-cookbook.md#t112-cooking-the-whole-meal--sequencing-several-dishes-and-the-spoken-walkthrough — do not edit here; edit the master file and rerun tools/build_planner.py -->
[↑ Meal Planning Sheet](../meal-planning-sheet.md) · [Index](../index.md)

### T112. Cooking the Whole Meal — Sequencing Several Dishes, and the Spoken Walkthrough

<!-- TECHNIQUE-TAGS: cody, conversation-mode, cooking-live, sequencing, timing, multitasking, walkthrough, tonight-document, attention -->
**Tags:** `cody` · `conversation-mode` · `cooking-live` · `sequencing` · `timing` · `multitasking` · `walkthrough` · `tonight-document` · `attention`
**Source:** Cody's own description, dictated 2026-09-12, of how a night's cooking should be talked through and written up. Not a single technique; the rules for stringing several dishes together and for how the chat speaks them.
**Used by:** the chat side (`CHAT.md` §6) whenever someone is cooking; the *tonight's instructions* document; [§T111](t111-planning-a-week--the-conversation-mode-workflow.md) for the week-ahead version.

**Why this exists.** A recipe is one dish. Dinner is three, and they don't cook in a line — they overlap, and the overlap is where a night goes wrong. Cody: *"There needs to be unique instructions based on the sides every time… if there's something delicate like steak or shrimp or fish that really gets ruined… the way Darcy cooks her steak is she cooks two steaks at a time in a pan very slowly and brings it up to one twenty-eight and continues to put an internal thermometer on it over and over again. It's a very high-maintenance issue. And so those high-maintenance issues — a sauce, a roux, whatever it is — take your time. And so you have to write customized instructions for that particular meal at that particular time."* And on how it is spoken: *"Giving them one step at a time… if you just give them steps one through thirty-five, that's worthless, because they're busy doing a step for a minute or two. They wanna concentrate on that one step."*

#### 1. The attention scale — every stage of every dish is one of three

- **Precision — full attention, nothing else at the same time.** A stage that goes from perfect to ruined in a minute, or that you have to stand over with a thermometer or your eyes. Bringing a steak up to temperature in a pan and probing it over and over ([§3](3-darcys-steak.md)); a sear; a roux ([§T1](t1-how-to-make-a-roux.md)); an emulsion ([§4.9](49-hollandaise-sauce.md), beurre blanc); frying shrimp or fish; a full-blast wok ([§2](2-geoffs-pork-belly-thai-basil.md)). In this book these are the stages that earn a 🟡 or 🔴 — [CLAUDE.md §3a](../../CLAUDE.md)'s test, *can it go from perfect to ruined?*, is the same test.
- **Check-in — a look every few minutes, a stir, a flip.** Sautéing a side, boiling pasta, a simmer, mashing, reheating chili. You can run two of these at once, or one beside a hands-off stage. Cody's own examples: the Brussels sprouts and the caulimash — *"that requires less thinking, and it needs to be less precise."*
- **Hands-off — set it and wait for the timer or the thermometer alarm.** Roasted vegetables in the oven (*"that goes on, and then you just check it — you don't have to flip it"*), a bake, a crock pot, a sous vide bath, a smoker, and **a rest or a hold**. Nothing to do until it beeps.

#### 2. The sequencing rules

1. **Never two precision stages at once.** One cook, one delicate thing. If the meal has two precision dishes, one finishes and holds before the other starts.
2. **Hands-off stages start first**, so their clocks run while you work on something else. Roasted vegetables go in before you touch the steak.
3. **Check-in stages pair with each other, or ride beside a hands-off stage — never beside a precision stage.**
4. **Precision comes at the points where nothing else needs you — and a hold or a rest is what creates those points.** Darcy's steak is the model, in Cody's words: *"She's going to cook the internal temperature of the steaks first to one twenty-eight. Then after that she's going to cook the Brussels sprouts and caulimash simultaneously… and then she's going to sear the steak."* That works because the reverse sear has a rest between the bring-up and the sear: **precision** (bring-up) → **hands-off** (steaks hold) → **check-in + check-in** (both sides at once) → **precision** (sear) → plate.
5. **A dish that is precision end to end** — a dark-roux gumbo, a wok stir-fry — **goes last, with everything else done or holding before it starts.**
6. **Time it backward from dinner** with each recipe's ⏰ Countdown line, then interleave. Whatever finishes last sets the clock; the rest is placed into its gaps.

#### 3. The written version — "tonight's instructions"

When someone asks for the night's instructions — *"make me a Word doc for tonight," "write up dinner,"* or at the start of the week for every night — the document is **one merged sequence for that meal, not three recipes stapled together**:

- **Title line:** the night, the dishes, the dinner time.
- **Ingredients per dish**, verbatim from each recipe, grouped by dish so pans and bowls can be set up separately.
- **One numbered sequence**, in cooking order, **every step tagged with the dish it belongs to in parentheses** — *(for the caulimash)*, *(for the Brussels sprouts)*, *(for the steak)*. Cody: *"If you're saying, put some milk in the pan, you need to put in parenthesis what it's for, just in case we make some last-minute substitution… so they can keep their pans separate as well."*
- **Simultaneous steps written as a block** — *"At the same time:"* — with each pan's step carrying its own tag.
- **Precision stages marked plainly** — *full attention, nothing else now* — so nobody starts a side while the steak is coming up.
- **Technique pointers inline**, one or two sentences where a step needs one, taken from the relevant §T entry — hot pan then oil ([§T2](t2-hot-pan-first-then-oil.md)), don't crowd the pan ([§T39](t39-maillard-vs-caramelization--gbd.md)), the roux never leaves your hand ([§T1](t1-how-to-make-a-roux.md)). Not the whole entry.
- **The substitution line at the top:** *if a dish changed, skip every step tagged for it.* Cody: *"They didn't have Brussels sprouts, we did asparagus instead — then she knows to skip that step."* The tags are what make that possible.
- **Format:** Word when asked for Word; otherwise markdown. The steps themselves are the recipes' own steps, never paraphrased.

#### 4. The spoken version — one step, then stop

- **Build the merged sequence first**, or fetch tonight's document if one was made. Keep a private pointer the whole time — *tonight: these dishes; we are on this dish, this step* — and never say the step number out loud.
- **Say one step.** What to do, what it's for, and the one technique pointer if that step has one. **Then stop and wait.** *"Done," "next," "okay," "what now"* means move to the next step.
- **A simultaneous block is spoken as one turn:** the first pan's step, *"and at the same time,"* the second pan's step. Then stop.
- **Precision stages are spoken slowly, one sentence at a time, with the doneness cue** — the thermometer number, the color, the smell. Say plainly that nothing else starts until this is done.
- **A question in the middle of a step:** answer it from the recipe or the technique entry, then bring them back — *"Back to the steak: you're bringing it up to 129."*
- **"Where were we?"** — name the dish and the step, then continue.
- **Timers:** say the minutes and tell them to set a timer; the chat can't set one on the phone.
- **A substitution mid-cook** (*"we're doing asparagus instead"*): swap that dish's remaining steps, say which tagged steps to skip, and carry on. If it's meant to be permanent, it's a revision request too.
- **Doneness and safety:** the entry's own figure; USDA where it's silent; Fahrenheit always ([CLAUDE.md §6](../../CLAUDE.md)).

#### 5. The worked example — Darcy's steak, Brussels sprouts, caulimash, dinner at 7:00

The stages come from [§3](3-darcys-steak.md) (reverse sear: pat dry, season, into the pan on low, bring up by thermometer, rest, sear), [§5.7](57-brussels-sprouts.md) (trim and halve, a 12-minute attended sauté), and [§11.5](115-easy-caulimash-keto-mashed-potatoes.md) (steam, mash, season); the exact steps are theirs and are quoted from them in the document, not restated here. The order is the point:

1. *(for the steak)* Pat dry, season, rub. **Precision starts.**
2. *(for the steak)* Into the pan on low; bring the whole batch up by thermometer to **129°F**, probing over and over. **Full attention, nothing else now.**
3. *(for the steak)* Off the heat to rest. **Hands-off — and this rest is the window.**
4. **At the same time —** *(for the Brussels sprouts)* into the hot fat, 12 minutes, turning now and then · *(for the caulimash)* cauliflower steaming, then mashed and seasoned. **Two check-in stages, side by side.**
5. *(for the steak)* Pan ripping hot, sear, pull. **Precision again.** Sides are done or holding.
6. Plate.

Swap the Brussels sprouts for asparagus and only the step tagged for them changes — [§5.2 Sautéed Asparagus](52-sautéed-asparagus.md)'s sauté drops into the same slot.

[↑ Table of Contents](../index.md)

---
