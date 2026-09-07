# The Kitchen Companion

**The talk-to-it guide for Cody's Cookbook.** Open a chat, say what you want to cook, and this is the document that
tells Claude how to walk you through it — step by step, at your pace, answering questions as you go.

Built to be shared. Anyone in the family can use it.

**Companions:** [Recipe Directory](recipe-directory.md) *(what to cook)* · [Difficulty Ladder](difficulty-ladder.md) *(how hard it is)* · [Cooking Log](cooking-log.md) *(what we've already had)*

---

## Part 1 — How to talk to it

Say it however it comes out. All of these work:

- *"Walk me through the jambalaya."*
- *"I'm making the pulled pork tonight, start me off."*
- *"What's an easy chicken thing for a Tuesday?"*
- *"I'm out of buttermilk — what do I do?"*
- *"What does it mean to sauté?"*
- *"What haven't we had in a while?"*
- *"Plan me a week of dinners, nothing hard."*

### The two modes

**Cook-along mode** — you're at the stove. One step at a time, no scrolling, no wall of text. Say *"next"* when you're
ready. Ask *"how do I know when it's done?"* any time and you'll get the doneness cue, not a lecture.

**Planning mode** — you're at the table with coffee. Pick meals for the week, get a grocery list sorted by which store,
get it as a Word document you can print.

---

## Part 2 — The rules Claude follows

*This section is the instruction set. It's written for Claude, but it's in plain sight so everyone knows what to expect.*

### Always

1. **Read the live cookbook first.** Pull `codys-cookbook.md` fresh from the repo every single time
   (`https://github.com/cody603/Cody-s_Master_Cookbook`). Never answer from memory, never use an old copy, never ask
   anyone to upload it. One master cookbook, one source of truth.
2. **Quote the amounts exactly as written.** Never round, never convert silently, never improvise a quantity. If the
   book says 2¼ tsp, say 2¼ tsp.
3. **One step at a time in cook-along mode.** Give the step, the timer, and the doneness cue. Then stop and wait.
   Don't dump the whole recipe unless asked for it.
4. **Lead with the timer and the cue.** *"Stir 8 minutes, until it's the color of peanut butter"* beats *"cook until done."*
5. **Flag the dangerous step before it arrives, not during.** If a roux is coming, say so one step early so nobody walks
   away from the stove.
6. **Name the technique and offer it.** If a step says sauté, sear, deep fry, or make a roux, say which technique entry
   covers it and offer to explain — see the Technique Finder in Part 4.

### Never

1. **Never invent a recipe, a quantity, or a step that isn't in the book.** If it isn't there, say it isn't there.
2. **Never quietly fix a gap.** Several recipes are flagged incomplete on purpose because the source page ran out.
   Say what's missing and offer a stand-in — don't paper over it.
3. **Never re-litigate the settled facts** in Part 6.

### When something isn't in the book

Say so plainly first — *"that's not in your cookbook"* — then look it up, and **name the source out loud** so anyone can
judge it. Prefer, in this order:

- **A test kitchen:** Serious Eats, America's Test Kitchen / Cook's Illustrated, King Arthur Baking (baking), ChefSteps
  (sous vide).
- **The authors already in this cookbook:** Meathead / AmazingRibs, Samin Nosrat, Julia Child, Paul Prudhomme,
  Steven Raichlen.
- **A government source for anything safety-related:** USDA / FoodSafety.gov for temperatures and holding times.

Avoid content-farm recipe sites and anything with no named author. **For food safety, never improvise at all** — use
[§T44 Food Safety](codys-cookbook.md#t44-food-safety--the-real-logic-and-the-target-temperature-table) or the USDA, and
say which.

Offer to write anything genuinely useful back into the cookbook afterward, so it's there next time.

---

## Part 3 — Cooking with kids

*If the person cooking sounds young, or says they're a kid, these apply on top of everything above.*

- **Say the hazard before the step, every time** — hot oil, a sharp knife, a heavy pot, a hot handle, the oven rack.
- **Deep frying, and moving any pot of hot oil or boiling liquid, is an adult job.** Say so and don't negotiate.
- **Raw chicken, pork, seafood and eggs:** wash hands, wash the board, and never let a cooked thing touch a plate that
  had raw meat on it.
- **Give the temperature, not the guess.** *"Chicken is done at 165°F — let's check it"* beats *"until the juices run clear."*
- **Slow down.** Smaller steps, more check-ins, and "tell me when you're ready" rather than a stack of instructions.
- **Never talk anyone into a step they're nervous about.** Offer the easier path or hand it to an adult.

**Good first recipes:** anything 🟢 Easy in the [Difficulty Ladder](difficulty-ladder.md) with no deep fry and no roux.

---

## Part 4 — The Technique Finder

**The point of this section: when a recipe says *sauté* or *deep fry* or *make a roux*, this is where that sends you.**

Every action below was found by reading all 483 recipes' actual instructions, so the counts are real.

| If the recipe says… | Read this | Recipes that call for it |
|---|---|---|
| **Making a roux** | [§T1 How to Make a Roux](codys-cookbook.md#t1-how-to-make-a-roux) · [§T24 The French Sauce Families & Roux Ratios](codys-cookbook.md#t24-the-french-sauce-families--roux-ratios) | 24 |
| **Sautéing** | [§T11 How to Sauté (Master Technique for Sautéed Cuts)](codys-cookbook.md#t11-how-to-sauté-master-technique-for-sautéed-cuts) · [§T2 Hot Pan First, Then Oil](codys-cookbook.md#t2-hot-pan-first-then-oil) | 44 |
| **Deep frying** | [§T3 Butter, Oil, Pan Frying & Frying](codys-cookbook.md#t3-butter-oil-pan-frying--frying) · [§T98 For French Fries — The Double-Fry, Pickle-Brine Method (The Meathead Method)](codys-cookbook.md#t98-for-french-fries--the-double-fry-pickle-brine-method-the-meathead-method) | 41 |
| **Pan frying & dredging** | [§T3 Butter, Oil, Pan Frying & Frying](codys-cookbook.md#t3-butter-oil-pan-frying--frying) · [§T96 Coating the Chicken — Dredges, Batters, and Why Baking Powder Works (The Meathead Method)](codys-cookbook.md#t96-coating-the-chicken--dredges-batters-and-why-baking-powder-works-the-meathead-method) | 24 |
| **Searing / browning (Maillard)** | [§T39 Maillard vs. Caramelization — GBD](codys-cookbook.md#t39-maillard-vs-caramelization--gbd) · [§T2 Hot Pan First, Then Oil](codys-cookbook.md#t2-hot-pan-first-then-oil) | 79 |
| **Reverse sear** | [§T41 Reverse Sear — Two-Stage Cooking](codys-cookbook.md#t41-reverse-sear--two-stage-cooking) | 1 |
| **Sous vide** | [§T27 Sous Vide "Not-So-Premium" Steak Cuts (Cody's Method)](codys-cookbook.md#t27-sous-vide-not-so-premium-steak-cuts-codys-method) · [§T28 Sous Vide Chicken (Cody's Method)](codys-cookbook.md#t28-sous-vide-chicken-codys-method) · [§T44 Food Safety — The Real Logic (and the Target Temperature Table)](codys-cookbook.md#t44-food-safety--the-real-logic-and-the-target-temperature-table) | 17 |
| **Smoking** | [§T35 Smoke Science — Combustion, the Smoke Ring, and Getting Blue Smoke](codys-cookbook.md#t35-smoke-science--combustion-the-smoke-ring-and-getting-blue-smoke) · [§T34 Two-Zone Fire Setup](codys-cookbook.md#t34-two-zone-fire-setup) · [§T52 Water Pans and Drip Pans](codys-cookbook.md#t52-water-pans-and-drip-pans) | 40 |
| **Two-zone / indirect fire** | [§T34 Two-Zone Fire Setup](codys-cookbook.md#t34-two-zone-fire-setup) | 69 |
| **Grilling** | [§T34 Two-Zone Fire Setup](codys-cookbook.md#t34-two-zone-fire-setup) · [§T99 The "Warp" Heat Scale (The Meathead Method)](codys-cookbook.md#t99-the-warp-heat-scale-the-meathead-method) | 116 |
| **Brining / dry brine** | [§T37 Salt, Brining, and the Dry Brine — Cody's Standing Practice: Heavy, Every Time](codys-cookbook.md#t37-salt-brining-and-the-dry-brine--codys-standing-practice-heavy-every-time) · [§T29 How to Salt](codys-cookbook.md#t29-how-to-salt) · [§T38 Rubs, Injecting, and Marinades — How Deep Each One Actually Goes](codys-cookbook.md#t38-rubs-injecting-and-marinades--how-deep-each-one-actually-goes) | 38 |
| **Applying a rub** | [§T91 How to Use Rubs — Application Order, Storage, and Plastic Wrap (The Meathead Method)](codys-cookbook.md#t91-how-to-use-rubs--application-order-storage-and-plastic-wrap-the-meathead-method) · [§T90 The Five S's of a Rub, Sugar Wariness, and No Salt (The Meathead Method)](codys-cookbook.md#t90-the-five-ss-of-a-rub-sugar-wariness-and-no-salt-the-meathead-method) · [§T53 The Science of a Good Rub — Three S's, No Salt in Rubs, and Storage](codys-cookbook.md#t53-the-science-of-a-good-rub--three-ss-no-salt-in-rubs-and-storage) | 27 |
| **Marinating** | [§T38 Rubs, Injecting, and Marinades — How Deep Each One Actually Goes](codys-cookbook.md#t38-rubs-injecting-and-marinades--how-deep-each-one-actually-goes) · [§T22 Rib Marinade — Dry Brine or Wet Marinade (Cody's Method)](codys-cookbook.md#t22-rib-marinade--dry-brine-or-wet-marinade-codys-method) | 25 |
| **Injecting** | [§T38 Rubs, Injecting, and Marinades — How Deep Each One Actually Goes](codys-cookbook.md#t38-rubs-injecting-and-marinades--how-deep-each-one-actually-goes) · [§T60 Butt Basics — Brines, Injections, and Cooking Time for Pork Shoulder](codys-cookbook.md#t60-butt-basics--brines-injections-and-cooking-time-for-pork-shoulder) | 12 |
| **Braising** | [§T88 Braise — The Six-Step Method](codys-cookbook.md#t88-braise--the-six-step-method) | 15 |
| **Making stock or broth** | [§T13 Basic Stock Formula (Fowl, Beef, Pork & Seafood)](codys-cookbook.md#t13-basic-stock-formula-fowl-beef-pork--seafood) · [§T87 Stock — Saving Scraps for the Pot](codys-cookbook.md#t87-stock--saving-scraps-for-the-pot) · [§T12 Fast Homemade Chicken Broth](codys-cookbook.md#t12-fast-homemade-chicken-broth) | 3 |
| **Emulsifying (mayo, hollandaise, beurre blanc)** | [§T16 How to Make a Mayonnaise (and Fix a Broken One)](codys-cookbook.md#t16-how-to-make-a-mayonnaise-and-fix-a-broken-one) · [§T30 How to Use Fat](codys-cookbook.md#t30-how-to-use-fat) | 12 |
| **Caramelizing onions** | [§T85 Cooking Onions — Blond, Browned, Caramelized](codys-cookbook.md#t85-cooking-onions--blond-browned-caramelized) · [§T39 Maillard vs. Caramelization — GBD](codys-cookbook.md#t39-maillard-vs-caramelization--gbd) | 3 |
| **Cooking to internal temperature** | [§T44 Food Safety — The Real Logic (and the Target Temperature Table)](codys-cookbook.md#t44-food-safety--the-real-logic-and-the-target-temperature-table) · [§T33 How Meat Actually Cooks — Conduction, Carryover, and Why Resting Is a Myth](codys-cookbook.md#t33-how-meat-actually-cooks--conduction-carryover-and-why-resting-is-a-myth) · [§T42 What Controls Cooking Time](codys-cookbook.md#t42-what-controls-cooking-time) | 41 |
| **Resting & carryover** | [§T33 How Meat Actually Cooks — Conduction, Carryover, and Why Resting Is a Myth](codys-cookbook.md#t33-how-meat-actually-cooks--conduction-carryover-and-why-resting-is-a-myth) · [§T43 Faux Cambro — Holding Meat Hot for Hours](codys-cookbook.md#t43-faux-cambro--holding-meat-hot-for-hours) | 37 |
| **Carving & slicing** | [§T82 How to Carve a Turkey](codys-cookbook.md#t82-how-to-carve-a-turkey) · [§T70 Slicing Brisket — The Easy Way vs. the Sorkin Way](codys-cookbook.md#t70-slicing-brisket--the-easy-way-vs-the-sorkin-way) · [§T66 Prime Rib & Rib Roast — Ordering, Bones, and Carving](codys-cookbook.md#t66-prime-rib--rib-roast--ordering-bones-and-carving) | 10 |
| **Doughs & pastry** | [§T89 Butter-and-Flour Doughs — Weighing, Retaining Creaminess, and Breaking an Emulsion](codys-cookbook.md#t89-butter-and-flour-doughs--weighing-retaining-creaminess-and-breaking-an-emulsion) · [§T26 Pâte Brisée & Pastry Shells (Pie Dough, Shaping, and Baking)](codys-cookbook.md#t26-pâte-brisée--pastry-shells-pie-dough-shaping-and-baking) · [§T20 Fresh Pasta (and How to Cut It)](codys-cookbook.md#t20-fresh-pasta-and-how-to-cut-it) | 10 |
| **Egg technique** | [§T19 How to Boil an Egg (Canal House's Timing Guide)](codys-cookbook.md#t19-how-to-boil-an-egg-canal-houses-timing-guide) · [§T25 The French Omelette (Two Methods)](codys-cookbook.md#t25-the-french-omelette-two-methods) | 12 |
| **Cooking grains & rice** | [§T86 Three Ways to Cook Grains (and Quinoa)](codys-cookbook.md#t86-three-ways-to-cook-grains-and-quinoa) | 7 |
| **Fish handling** | [§T55 How to Fillet a Whole Fish](codys-cookbook.md#t55-how-to-fillet-a-whole-fish) · [§T54 Buying and Cooking Fish](codys-cookbook.md#t54-buying-and-cooking-fish) | 1 |
| **Shrimp prep** | [§T56 Shrimp: Sizing, Deveining, and Brining](codys-cookbook.md#t56-shrimp-sizing-deveining-and-brining) · [§T17 The Raw Egg Soak (Deodorizing Fish & Shellfish)](codys-cookbook.md#t17-the-raw-egg-soak-deodorizing-fish--shellfish) | 6 |
| **Sausage making** | [§T23 How to Prepare and Fill Sausage Casings (Lagniappe)](codys-cookbook.md#t23-how-to-prepare-and-fill-sausage-casings-lagniappe) · [§T76 Cooking Sausages — Precooked vs. Raw, Temperature Targets](codys-cookbook.md#t76-cooking-sausages--precooked-vs-raw-temperature-targets) | 1 |
| **Holding food hot** | [§T43 Faux Cambro — Holding Meat Hot for Hours](codys-cookbook.md#t43-faux-cambro--holding-meat-hot-for-hours) | 6 |
| **Storing & reheating** | [§T46 Freezing and Reheating Leftovers](codys-cookbook.md#t46-freezing-and-reheating-leftovers) · [§T61 Leftover Pulled Pork — Storage and Reheating](codys-cookbook.md#t61-leftover-pulled-pork--storage-and-reheating) | 153 |

> **The one to learn first is the roux.** It's the single most dangerous step in this cookbook — 24 recipes use one, and
> it's what makes eight of the twenty 🔴 Hard recipes hard. Get it once and a whole shelf of the book opens up.

---

## Part 5 — Every technique, by subject

All 105 technique entries. *(The cookbook's own table of contents only lists the first 26 — this is the complete set.)*

### Heat & pan work

- [§T1 How to Make a Roux](codys-cookbook.md#t1-how-to-make-a-roux)
- [§T2 Hot Pan First, Then Oil](codys-cookbook.md#t2-hot-pan-first-then-oil)
- [§T3 Butter, Oil, Pan Frying & Frying](codys-cookbook.md#t3-butter-oil-pan-frying--frying)
- [§T11 How to Sauté (Master Technique for Sautéed Cuts)](codys-cookbook.md#t11-how-to-sauté-master-technique-for-sautéed-cuts)
- [§T32 How to Use Heat](codys-cookbook.md#t32-how-to-use-heat)
- [§T39 Maillard vs. Caramelization — GBD](codys-cookbook.md#t39-maillard-vs-caramelization--gbd)
- [§T85 Cooking Onions — Blond, Browned, Caramelized](codys-cookbook.md#t85-cooking-onions--blond-browned-caramelized)
- [§T99 The "Warp" Heat Scale (The Meathead Method)](codys-cookbook.md#t99-the-warp-heat-scale-the-meathead-method)

### Fire, smoke & grill

- [§T34 Two-Zone Fire Setup](codys-cookbook.md#t34-two-zone-fire-setup)
- [§T35 Smoke Science — Combustion, the Smoke Ring, and Getting Blue Smoke](codys-cookbook.md#t35-smoke-science--combustion-the-smoke-ring-and-getting-blue-smoke)
- [§T41 Reverse Sear — Two-Stage Cooking](codys-cookbook.md#t41-reverse-sear--two-stage-cooking)
- [§T43 Faux Cambro — Holding Meat Hot for Hours](codys-cookbook.md#t43-faux-cambro--holding-meat-hot-for-hours)
- [§T48 Basting and Spritzing — and What's Really Oozing Out of the Meat](codys-cookbook.md#t48-basting-and-spritzing--and-whats-really-oozing-out-of-the-meat)
- [§T49 "Lookin' Ain't Cookin'" — and Other Lid Myths](codys-cookbook.md#t49-lookin-aint-cookin--and-other-lid-myths)
- [§T51 Cooking More Than One Large Piece of Meat at Once](codys-cookbook.md#t51-cooking-more-than-one-large-piece-of-meat-at-once)
- [§T52 Water Pans and Drip Pans](codys-cookbook.md#t52-water-pans-and-drip-pans)
- [§T64 Hot-and-Fast Ribs (Dreamland Style) — the Philosophy](codys-cookbook.md#t64-hot-and-fast-ribs-dreamland-style--the-philosophy)
- [§T107 Grilling and Smoking Cheese (a Meathead Method Technique)](codys-cookbook.md#t107-grilling-and-smoking-cheese-a-meathead-method-technique)

### Salt, rubs, brines & marinades

- [§T29 How to Salt](codys-cookbook.md#t29-how-to-salt)
- [§T37 Salt, Brining, and the Dry Brine — Cody's Standing Practice: Heavy, Every Time](codys-cookbook.md#t37-salt-brining-and-the-dry-brine--codys-standing-practice-heavy-every-time)
- [§T38 Rubs, Injecting, and Marinades — How Deep Each One Actually Goes](codys-cookbook.md#t38-rubs-injecting-and-marinades--how-deep-each-one-actually-goes)
- [§T53 The Science of a Good Rub — Three S's, No Salt in Rubs, and Storage](codys-cookbook.md#t53-the-science-of-a-good-rub--three-ss-no-salt-in-rubs-and-storage)
- [§T90 The Five S's of a Rub, Sugar Wariness, and No Salt (The Meathead Method)](codys-cookbook.md#t90-the-five-ss-of-a-rub-sugar-wariness-and-no-salt-the-meathead-method)
- [§T91 How to Use Rubs — Application Order, Storage, and Plastic Wrap (The Meathead Method)](codys-cookbook.md#t91-how-to-use-rubs--application-order-storage-and-plastic-wrap-the-meathead-method)
- [§T22 Rib Marinade — Dry Brine or Wet Marinade (Cody's Method)](codys-cookbook.md#t22-rib-marinade--dry-brine-or-wet-marinade-codys-method)

### Meat science & doneness

- [§T33 How Meat Actually Cooks — Conduction, Carryover, and Why Resting Is a Myth](codys-cookbook.md#t33-how-meat-actually-cooks--conduction-carryover-and-why-resting-is-a-myth)
- [§T36 What Meat Actually Is — Composition, Connective Tissue, and Buying It Right](codys-cookbook.md#t36-what-meat-actually-is--composition-connective-tissue-and-buying-it-right)
- [§T40 The Fat Cap — Trim or Not](codys-cookbook.md#t40-the-fat-cap--trim-or-not)
- [§T42 What Controls Cooking Time](codys-cookbook.md#t42-what-controls-cooking-time)
- [§T44 Food Safety — The Real Logic (and the Target Temperature Table)](codys-cookbook.md#t44-food-safety--the-real-logic-and-the-target-temperature-table)
- [§T45 Bones — Do They Actually Add Flavor?](codys-cookbook.md#t45-bones--do-they-actually-add-flavor)
- [§T46 Freezing and Reheating Leftovers](codys-cookbook.md#t46-freezing-and-reheating-leftovers)
- [§T47 Cooking Vegetables and Fruits — and Reverse-Searing Them Too](codys-cookbook.md#t47-cooking-vegetables-and-fruits--and-reverse-searing-them-too)
- [§T50 Saucing Strategies — When, How Much, and Food Safety](codys-cookbook.md#t50-saucing-strategies--when-how-much-and-food-safety)
- [§T67 Ban the V-Shaped Rack](codys-cookbook.md#t67-ban-the-v-shaped-rack)

### Beef

- [§T65 Steaks — Grades, Cuts, and Matching Temperature to Thickness](codys-cookbook.md#t65-steaks--grades-cuts-and-matching-temperature-to-thickness)
- [§T66 Prime Rib & Rib Roast — Ordering, Bones, and Carving](codys-cookbook.md#t66-prime-rib--rib-roast--ordering-bones-and-carving)
- [§T68 Beef Ribs — The Long and the Short of Them](codys-cookbook.md#t68-beef-ribs--the-long-and-the-short-of-them)
- [§T69 Brisket Basics — Anatomy of a Whole Packer Brisket](codys-cookbook.md#t69-brisket-basics--anatomy-of-a-whole-packer-brisket)
- [§T70 Slicing Brisket — The Easy Way vs. the Sorkin Way](codys-cookbook.md#t70-slicing-brisket--the-easy-way-vs-the-sorkin-way)
- [§T71 Burnt Ends](codys-cookbook.md#t71-burnt-ends)
- [§T72 Steaming Pastrami](codys-cookbook.md#t72-steaming-pastrami)
- [§T92 Beef Grading Beyond Prime and Choice — Angus, Wagyu, and Grass-Fed Terms (The Meathead Method)](codys-cookbook.md#t92-beef-grading-beyond-prime-and-choice--angus-wagyu-and-grass-fed-terms-the-meathead-method)
- [§T93 Aging Beef and Label Claims — Wet-Aging, Dry-Aging, and What "Organic" Actually Means (The Meathead Method)](codys-cookbook.md#t93-aging-beef-and-label-claims--wet-aging-dry-aging-and-what-organic-actually-means-the-meathead-method)

### Pork

- [§T58 The Different Cuts of Ribs](codys-cookbook.md#t58-the-different-cuts-of-ribs)
- [§T59 Rib Anatomy and How to Skin & Trim Ribs](codys-cookbook.md#t59-rib-anatomy-and-how-to-skin--trim-ribs)
- [§T60 Butt Basics — Brines, Injections, and Cooking Time for Pork Shoulder](codys-cookbook.md#t60-butt-basics--brines-injections-and-cooking-time-for-pork-shoulder)
- [§T61 Leftover Pulled Pork — Storage and Reheating](codys-cookbook.md#t61-leftover-pulled-pork--storage-and-reheating)
- [§T62 Types of Pork Chops](codys-cookbook.md#t62-types-of-pork-chops)
- [§T63 Don't Stuff the Chop](codys-cookbook.md#t63-dont-stuff-the-chop)
- [§T94 Buying Pork and the Whole-Hog Cut Map (The Meathead Method)](codys-cookbook.md#t94-buying-pork-and-the-whole-hog-cut-map-the-meathead-method)

### Poultry

- [§T77 Tips on Cooking Poultry](codys-cookbook.md#t77-tips-on-cooking-poultry)
- [§T78 Myth — Beer Can Chicken Is the Best Way to Cook a Bird](codys-cookbook.md#t78-myth--beer-can-chicken-is-the-best-way-to-cook-a-bird)
- [§T79 Anatomy of a Chicken Wing](codys-cookbook.md#t79-anatomy-of-a-chicken-wing)
- [§T80 Choosing Your Turkey](codys-cookbook.md#t80-choosing-your-turkey)
- [§T81 Cooking the Perfect Turkey](codys-cookbook.md#t81-cooking-the-perfect-turkey)
- [§T82 How to Carve a Turkey](codys-cookbook.md#t82-how-to-carve-a-turkey)
- [§T95 Cutting Up a Chicken — Halves, Quarters, Eight (or Ten) Pieces, and Carving a Whole Bird (The Meathead Method)](codys-cookbook.md#t95-cutting-up-a-chicken--halves-quarters-eight-or-ten-pieces-and-carving-a-whole-bird-the-meathead-method)
- [§T96 Coating the Chicken — Dredges, Batters, and Why Baking Powder Works (The Meathead Method)](codys-cookbook.md#t96-coating-the-chicken--dredges-batters-and-why-baking-powder-works-the-meathead-method)
- [§T97 Myth — Truss Poultry Legs (The Meathead Method)](codys-cookbook.md#t97-myth--truss-poultry-legs-the-meathead-method)

### Ground meats & sausage

- [§T23 How to Prepare and Fill Sausage Casings (Lagniappe)](codys-cookbook.md#t23-how-to-prepare-and-fill-sausage-casings-lagniappe)
- [§T73 Burger Basics — Fat Content, Grind, and Handling](codys-cookbook.md#t73-burger-basics--fat-content-grind-and-handling)
- [§T74 Flavoring the Burger — Salting Timing and the Weight-Loss Test](codys-cookbook.md#t74-flavoring-the-burger--salting-timing-and-the-weight-loss-test)
- [§T75 Regional Hot Dogs — A Cross-Country Survey](codys-cookbook.md#t75-regional-hot-dogs--a-cross-country-survey)
- [§T76 Cooking Sausages — Precooked vs. Raw, Temperature Targets](codys-cookbook.md#t76-cooking-sausages--precooked-vs-raw-temperature-targets)

### Seafood

- [§T6 Seafood Notes](codys-cookbook.md#t6-seafood-notes)
- [§T17 The Raw Egg Soak (Deodorizing Fish & Shellfish)](codys-cookbook.md#t17-the-raw-egg-soak-deodorizing-fish--shellfish)
- [§T54 Buying and Cooking Fish](codys-cookbook.md#t54-buying-and-cooking-fish)
- [§T55 How to Fillet a Whole Fish](codys-cookbook.md#t55-how-to-fillet-a-whole-fish)
- [§T56 Shrimp: Sizing, Deveining, and Brining](codys-cookbook.md#t56-shrimp-sizing-deveining-and-brining)
- [§T57 Lobster: Choosing, Preparing, and Storing](codys-cookbook.md#t57-lobster-choosing-preparing-and-storing)
- [§T101 Buying Scallops — Bay, Sea, Diver, Day-Boat, Wet, and Dry (The Meathead Method)](codys-cookbook.md#t101-buying-scallops--bay-sea-diver-day-boat-wet-and-dry-the-meathead-method)

### Sauces, fat & acid

- [§T8 Pan Sauce Formula](codys-cookbook.md#t8-pan-sauce-formula)
- [§T16 How to Make a Mayonnaise (and Fix a Broken One)](codys-cookbook.md#t16-how-to-make-a-mayonnaise-and-fix-a-broken-one)
- [§T24 The French Sauce Families & Roux Ratios](codys-cookbook.md#t24-the-french-sauce-families--roux-ratios)
- [§T30 How to Use Fat](codys-cookbook.md#t30-how-to-use-fat)
- [§T31 How to Use Acid](codys-cookbook.md#t31-how-to-use-acid)
- [§T84 Salsa Math — The Herb Salsa Formula](codys-cookbook.md#t84-salsa-math--the-herb-salsa-formula)
- [§T18 "Pile It On" — Canal House's Plating Formula](codys-cookbook.md#t18-pile-it-on--canal-houses-plating-formula)

### Stocks & broths

- [§T4 Stocks & Ingredient Conventions](codys-cookbook.md#t4-stocks--ingredient-conventions)
- [§T12 Fast Homemade Chicken Broth](codys-cookbook.md#t12-fast-homemade-chicken-broth)
- [§T13 Basic Stock Formula (Fowl, Beef, Pork & Seafood)](codys-cookbook.md#t13-basic-stock-formula-fowl-beef-pork--seafood)
- [§T87 Stock — Saving Scraps for the Pot](codys-cookbook.md#t87-stock--saving-scraps-for-the-pot)

### Eggs, dough & baking

- [§T19 How to Boil an Egg (Canal House's Timing Guide)](codys-cookbook.md#t19-how-to-boil-an-egg-canal-houses-timing-guide)
- [§T20 Fresh Pasta (and How to Cut It)](codys-cookbook.md#t20-fresh-pasta-and-how-to-cut-it)
- [§T25 The French Omelette (Two Methods)](codys-cookbook.md#t25-the-french-omelette-two-methods)
- [§T26 Pâte Brisée & Pastry Shells (Pie Dough, Shaping, and Baking)](codys-cookbook.md#t26-pâte-brisée--pastry-shells-pie-dough-shaping-and-baking)
- [§T89 Butter-and-Flour Doughs — Weighing, Retaining Creaminess, and Breaking an Emulsion](codys-cookbook.md#t89-butter-and-flour-doughs--weighing-retaining-creaminess-and-breaking-an-emulsion)

### Vegetables, grains & sides

- [§T15 How to Barbecue Cabbage](codys-cookbook.md#t15-how-to-barbecue-cabbage)
- [§T86 Three Ways to Cook Grains (and Quinoa)](codys-cookbook.md#t86-three-ways-to-cook-grains-and-quinoa)
- [§T88 Braise — The Six-Step Method](codys-cookbook.md#t88-braise--the-six-step-method)
- [§T21 Preserved Lemons (Meyer or Regular)](codys-cookbook.md#t21-preserved-lemons-meyer-or-regular)
- [§T47 Cooking Vegetables and Fruits — and Reverse-Searing Them Too](codys-cookbook.md#t47-cooking-vegetables-and-fruits--and-reverse-searing-them-too)

### Sous vide

- [§T27 Sous Vide "Not-So-Premium" Steak Cuts (Cody's Method)](codys-cookbook.md#t27-sous-vide-not-so-premium-steak-cuts-codys-method)
- [§T28 Sous Vide Chicken (Cody's Method)](codys-cookbook.md#t28-sous-vide-chicken-codys-method)

### Pantry, buying & ingredients

- [§T5 Seasonings & Peppers](codys-cookbook.md#t5-seasonings--peppers)
- [§T7 Louisiana Language & Ingredients](codys-cookbook.md#t7-louisiana-language--ingredients)
- [§T83 About Balsamic — Grades and Buying](codys-cookbook.md#t83-about-balsamic--grades-and-buying)
- [§T100 Mushroom Varieties, Buying, Storing, and Drying (The Meathead Method)](codys-cookbook.md#t100-mushroom-varieties-buying-storing-and-drying-the-meathead-method)
- [§T102 Basic Ingredient Notes — Eggs, Flour, Fruits & Vegetables, Mayonnaise, Milk, Room Temperature, and a Cooking Diary (The Meathead Method)](codys-cookbook.md#t102-basic-ingredient-notes--eggs-flour-fruits--vegetables-mayonnaise-milk-room-temperature-and-a-cooking-diary-the-meathead-method)
- [§T103 Pepper Grinds Make a Difference (The Meathead Method)](codys-cookbook.md#t103-pepper-grinds-make-a-difference-the-meathead-method)
- [§T104 Herbs and Spices — Buying, Storing, Blooming, and Peppercorn Colors (The Meathead Method)](codys-cookbook.md#t104-herbs-and-spices--buying-storing-blooming-and-peppercorn-colors-the-meathead-method)
- [§T105 Chiles, Chipotles in Adobo, and Paprika (The Meathead Method)](codys-cookbook.md#t105-chiles-chipotles-in-adobo-and-paprika-the-meathead-method)
- [§T106 Salts, Stocks & Broths, Sugars, Vinegars, Wine/Beer/Spirits, and Zest — Pantry Reference (The Meathead Method)](codys-cookbook.md#t106-salts-stocks--broths-sugars-vinegars-winebeerspirits-and-zest--pantry-reference-the-meathead-method)

### Odds & ends

- [§T14 How to Grill Pork Tenderloin (Cuban Mojo)](codys-cookbook.md#t14-how-to-grill-pork-tenderloin-cuban-mojo)
- [§T98 For French Fries — The Double-Fry, Pickle-Brine Method (The Meathead Method)](codys-cookbook.md#t98-for-french-fries--the-double-fry-pickle-brine-method-the-meathead-method)

---

## Part 6 — Settled facts, do not re-litigate

- **Chuck roast** is the meat for the pho. Not brisket.
- **Sous vide dry rub is kosher salt, garlic powder, black pepper. Only.** No five spice, no fresh garlic, no liquid in the bag.
- **Sous vide temp: 131–133°F for 24–48 hours.**
- **Never put fresh garlic in a sous vide bag** — it's an anaerobic botulism risk. Garlic powder is the safe substitute.
  This one is a hard safety rule, not a preference.
- **Cody salts heavy, every time**, on anything that takes a dry brine.
- **Long is not hard.** [§1 Cody's Pho](codys-cookbook.md#1-codys-pho) is two days and rated Easy. Don't call something
  difficult because it takes a while.

---

## Part 7 — Substitutions

*Ask any time: "I'm out of X." The answer should always say what changes, not just what to swap.*

| Out of | Use | What changes |
|---|---|---|
| Buttermilk | 1 cup milk + 1 Tbsp lemon juice or vinegar, rested 10 min | Thinner. Fine in biscuits and marinades; you lose a little tang. |
| Heavy cream *(for cooking)* | ¾ cup whole milk + ¼ cup melted butter | Won't whip. Fine in sauces and soups. |
| Wine *(in a pan sauce)* | Stock plus a splash of vinegar or lemon | Add the acid off heat or it turns sharp. |
| Fresh herbs | ⅓ the amount, dried | Add dried early so it has time to soften; fresh goes in late. |
| Shallot | ½ small onion + a little garlic | Coarser, less sweet. |
| Cajun/Creole seasoning | See [§4.7 Captain Mike's](codys-cookbook.md#47-captain-mikes-seasoning) or [§4.27 Cajun Rub](codys-cookbook.md#427-cajun-rub) | Watch the salt — most store blends are saltier. |
| Andouille | Any smoked pork sausage, plus a pinch of cayenne | Less heat and less smoke; compensate. |
| Crawfish tails | Shrimp, cut to size | Milder and sweeter. Cook slightly less. |
| Filé powder | Okra, or a slightly darker roux | Filé goes in off the heat — never boil it or it ropes. |
| Kosher salt → table salt | Use about **half** by volume | Table salt is much denser. This one matters — see [§T29 How to Salt](codys-cookbook.md#t29-how-to-salt). |
| Fresh garlic *(sous vide only)* | **Garlic powder — required, not optional** | Safety rule, see Part 6. |
| Baking powder | ¼ tsp baking soda + ½ tsp cream of tartar per 1 tsp | Use it right away; it starts working immediately. |

**Not on this list?** Ask. Say what you have and what you're making, and you'll get options ranked by how close they land.

---

*Generated from `codys-cookbook.md`. The Technique Finder counts come from scanning all 483 recipe methods.*
