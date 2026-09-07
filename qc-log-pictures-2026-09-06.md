# Picture QC Log — 2026-09-06

**Scope:** 100% QC of every picture in the cookbook. Three rigorous passes.
**Status: LOG ONLY — nothing in `codys-cookbook.md` or `images/` was changed by this pass.** Another session is live; these corrections are staged here to be applied to the master later.

---

## What was checked, and what could not be

**Checked at the pixel level: all 14 pictures in the repo.** Every one was opened at full resolution, its page numbers read from the printed footers, and every word, number, and illustration visible in it compared against the cookbook text it supports.

| Set | Files | Cookbook entry |
|---|---|---|
| Omelette | 4 | [§T25 The French Omelette](codys-cookbook.md#t25-the-french-omelette-two-methods) |
| Ratatouille | 2 | [§5.22 Ratatouille](codys-cookbook.md#522-ratatouille-eggplant-casserole) |
| French bread | 8 | [§15.1 Plain French Bread](codys-cookbook.md#151-plain-french-bread-pain-français) |

**Not checkable here: every other photograph in the project.** The cookbook is built almost entirely from photographed pages — 649 entries in all (522 numbered recipes, 105 technique entries, 22 reference sections), and five named batch scans alone (11-, 21-, 50-, 54-, and 55-page). Those photographs were supplied in earlier sessions and live nowhere in this repo or on this machine. For everything outside the 14 files above, Pass 3 audits **what the cookbook itself records about the pictures** — coverage, gaps, and contradictions — which is as far as the evidence goes. Where a finding rests on the record rather than on pixels, it says so.

**Method:**

- **Pass 1** — read every picture at full resolution; compared it line by line against the cookbook text, alt text, caption, and placement.
- **Pass 2** — independent re-verification. Page numbers re-read from cropped-and-magnified footer corners *without* reference to Pass 1, so the page identity of every file rests on a second, separate reading. Plus mechanical checks: full pixel decode, reference/file reconciliation, orphan and duplicate detection.
- **Pass 3** — whole-cookbook sweep of every claim made *about* the pictures: source page ranges, "not photographed" flags, embedding claims, stale cross-references, and a complete re-shoot ledger.

**Headline: one critical defect (4 files), one meaning-reversing omission, 18 smaller items, and 1 question only Cody can settle. The French bread set is clean on page identity; the omelette set is not.**

---

## Verdict summary

| ID | Sev | Where | What |
|---|---|---|---|
| **P-01** | **CRITICAL** | §T25, 4 files | Every omelette picture shows the wrong pages — filenames are rotated |
| **P-02** | **FLAG** | §15.1 L40574 | Plywood thickness — the photo cannot resolve the numerator; needs Cody's eyes on the book |
| P-03 | MED | §15.1 L40554 | Freezer limit drops "probably more" — reverses the source's meaning |
| P-04 | MED | §15.1 Step 5 | Missing step: prepare the canvas during the 5-minute rest |
| P-05 | MED | §15.1 Step 6 | Missing technique: start each roll seal-side down, twist to straighten |
| P-06 | MED | §15.1 §E | Baker's-oven kit needs **two** boards; only one is specced |
| P-13 | MED | §T25 L14001, §15.1 L40466 | "Straight crops" — 12 of the 14 are uncropped full-spread photos |
| P-07 | LOW | §15.1 Step 6 | Missing rationale + the seal-and-tear warning + hand position |
| P-08 | LOW | §15.1 Step 6 | Heading drops the source's *la tourne* |
| P-09 | LOW | §15.1 Yield | Source contradicts itself on ficelle width; only one figure recorded |
| P-10 | LOW | §15.1 §D | Round loaves: missing "flour lightly, cover, rise to almost triple" |
| P-11 | LOW | §T25 §D | Quotation not verbatim — "you're" for the source's "you are" |
| P-12 | LOW | §T25 L14053 | Caption: Method II begins on the *same* page, not the facing one |
| P-14 | LOW | §T24 L13986 | Stale: p. 505 listed as "still open", but it's transcribed at §5.22 |
| P-15 | LOW | §5.22 | Embeds two source illustrations but carries no embedding note |
| P-16 | LOW | 3 files | Alt text under-describes what's actually in the picture |
| P-17 | LOW | 12 files | Shadows, thumbs in the text block, skew, low contrast |
| P-18 | LOW | ratatouille ×2 | Page attribution corroborated but not directly verifiable |
| P-19 | LOW | repo | `.gitattributes` treats binaries as text; `.DS_Store` committed |
| P-20 | INFO | repo | Only 14 of the project's photographs survive anywhere |
| P-21 | INFO | cookbook-wide | Re-shoot ledger — 30+ pictures that came through incomplete |

---

## P-01 — CRITICAL: all four omelette pictures show the wrong pages

**Every one of the four pictures embedded in §T25 is a photograph of pages other than the ones its filename and caption claim.** The filenames are rotated by one position against their contents. A reader following the recipe is shown, at each of the four steps, an illustration of a different step.

Verified twice, independently: once by reading each spread whole, and again in Pass 2 by cropping and magnifying only the printed page-number corners, with no reference to the first reading. Both agree exactly.

| File | Filename claims | **Actually contains** | What the picture actually shows |
|---|---|---|---|
| `omelette-p128-129.jpg` | 128–129 | **134–135** | Jerking the pan; increasing the tilt; browning the shaped omelette; Garnishings and Fillings |
| `omelette-p130-131.jpg` | 130–131 | **128–129** | Pan-to-plate transfer; start of Method I |
| `omelette-p132-133.jpg` | 132–133 | **130–131** | Butter to the point of coloring; sliding and stirring; tilt and gather at the far lip |
| `omelette-p134-135.jpg` | 134–135 | **132–133** | The 4–5 sharp blows; Method II begins; letting the eggs settle |

The *intent* was right — the four captions describe exactly the four things the 2026-08-10 changelog says were meant to be embedded, and each is placed at the correct step. Only the file-to-page mapping is wrong.

**Fix — rotate the filenames to match their contents. No markdown edit is needed at all:** each reference in §T25 already names the page it wants, so once the filenames tell the truth, all four references resolve correctly. This also makes it the safest possible fix to land while another session has the master file open, since it touches zero lines of `codys-cookbook.md`.

```bash
cd images/omelette
git mv omelette-p128-129.jpg _tmp.jpg          # holds pp.134-135
git mv omelette-p130-131.jpg omelette-p128-129.jpg
git mv omelette-p132-133.jpg omelette-p130-131.jpg
git mv omelette-p134-135.jpg omelette-p132-133.jpg
git mv _tmp.jpg              omelette-p134-135.jpg
```

**Verification after the rename** — each caption should then match its file:

| Reference in §T25 | Step it illustrates | Correct after rename |
|---|---|---|
| `omelette-p130-131.jpg` (L14040) | Method I, Steps 2–4 | ✅ butter, sliding, tilt-and-gather |
| `omelette-p132-133.jpg` (L14052) | Method I, Step 5 | ✅ sharp blows, Method II begins |
| `omelette-p134-135.jpg` (L14082) | Method II, Steps 4–6 | ✅ jerking, rolling, browning |
| `omelette-p128-129.jpg` (L14094) | Section E, transfer | ✅ pan-to-plate |

---

## P-02 — FLAG: plywood thickness cannot be confirmed from the photograph

**§15.1 §E, line 40574** — "a piece of **5/16-inch** plywood".

**This does not resolve.** The source prints the thickness as a typographic fraction whose numerator is a superscript numeral only a few pixels tall in these photographs. It appears twice — page 70 (the unmolding board) and page 71 (the sliding board) — and both were magnified to the limit and contrast-stretched. The denominator is unmistakably **16** in both. **The numerator is not legible with confidence: it is either 3 or 5.**

Compared side by side with known digits set in the same face on the same page ("6 by 3 inches" two paragraphs above, "Step 5" and "10 to 12 pieces" at the top), the glyph reads closer to a flat-topped **5** than to that page's clearly double-bowled **3** — but at this resolution that is an impression, not a reading, and I am not willing to record it as one.

**My first pass through this called it a definite 3/16-inch error. That was overconfident and is withdrawn.** The cookbook's 5/16-inch may well be correct as transcribed.

> **Action: not a correction — a question for Cody.** One look at the physical book settles it. If it *is* 3/16-inch, it needs changing in two places once P-06 adds the unmolding board. If it's 5/16-inch, nothing changes and this closes.
>
> A re-photograph of pages 70–71 straight-on, without the shadow, would also settle it and would serve P-17 at the same time.

---

## P-03 — MED: the freezer limit is a floor, not a ceiling

**§15.1 §C, line 40554** currently reads: *"Limit: a week to 10 days for plain French bread dough (and risky past 10 days for doughs with butter and eggs)."*

Source page 68 prints: *"Limit: A week to 10 days, **probably more** for plain French bread dough, and risky after 10 days for doughs with butter and eggs."*

The dropped two words invert the sense. The source is saying plain French bread dough will likely keep **longer** than 10 days; the cookbook reads as though 10 days is its outer limit.

> **Fix:** *"Limit: a week to 10 days — **probably more** — for plain French bread dough…"*

---

## P-04 — MED: a missing step in the master recipe

**§15.1 Step 5.** Source page 62 gives an instruction for the 5-minute rest that the cookbook does not carry anywhere:

> *"While the dough is resting, prepare the rising surface: smooth the canvas or linen toweling on a large tray or baking sheet, and rub flour thoroughly into the entire surface of the cloth to prevent the dough from sticking."*

Step 6 later says to place the shaped loaf "at one side of a flour-rubbed canvas," but never says to prepare it — and the rest is the only window in which to do it. Confirmed absent: neither "rising surface" nor "linen toweling" appears anywhere in the cookbook.

> **Fix:** add a closing sentence to Step 5.

---

## P-05 — MED: the seal-management technique is missing

**§15.1 Step 6.** Source page 64:

> *"During the extension rolls, keep circumference of dough as even as possible and try to **start each roll with sealed side of dough down, twisting the rope of dough to straighten the line of seal as necessary**. If seal disappears, **as it sometimes does with all-purpose flour**, do not worry."*

The cookbook keeps "keeping the circumference as even as possible and the line of seal straight — if the seal disappears, don't worry," but drops *how* you keep it straight, and drops the reassurance that all-purpose flour is the reason it vanishes. Since §15.1's own headnote insists on all-purpose flour, that second clause is the one that tells the baker nothing has gone wrong.

---

## P-06 — MED: the simulated baker's oven needs two boards

**§15.1 §E** lists one board:

> *"**The sliding board:** a piece of 5/16-inch plywood slightly longer but 2 inches narrower than your oven rack…"*

The source specifies two different boards under two separate headings:

| Board | Source | Spec |
|---|---|---|
| **Unmolding board** — canvas to board | p. 70 | plywood *(thickness per P-02)*, about **20 inches long and 8 inches wide** |
| **Sliding board** — board to tiles, replaces *la pelle* | p. 71 | plywood *(thickness per P-02)*, slightly longer but **2 inches narrower than your oven rack** |

§E's own "Using it" paragraph then uses both ("sprinkle *fleurage* on the unmolding board **and** the sliding board") without §E ever having specced the first. The master recipe's equipment list (L40484) does name an unmolding board — "cardboard or plywood 18 to 20 inches long and 6 to 8 inches wide" — but that is a general-purpose stand-in, and the ranges differ from p. 70's figures. (Those ranges most likely come from the source's own equipment paragraph on p. 57, which is not among the pictures held here, so they are not contradicted — just unverifiable from the evidence available.)

> **Fix:** add the unmolding board as its own bullet in §E with p. 70's dimensions. Both boards are the same thickness, whatever P-02 resolves it to — so write that figure once and use it for both.

---

## P-07 — LOW: forming-the-loaf detail dropped

Three items visible in the pictures and absent from §15.1 Step 6:

1. **Why the shaping works** (p. 62): *"Because French bread stands free in the oven and is not baked in a pan, it has to be formed in such a way that the tension of the coagulated gluten cloak on the surface will hold the dough in shape."* The cookbook gives this rationale only for round loaves in §D, never for the bâtard the recipe actually walks through.
2. **The tear warning** (p. 63): the working surface must be *very* lightly floured "so the dough will not stick and tear, **which would break the lightly coagulated gluten cloak that is being formed**."
3. **The hand position for sealing** (p. 63): *"your hands extended, thumbs out at right angles and touching."*

Also worth capturing from p. 62, since §15.1's Yield offers baguettes as an option without qualification: *"**Baguettes are much too long for home ovens.**"*

---

## P-08 — LOW: the step heading drops a term

Source p. 62 heads the step *"Forming loaves—**la tourne**; la mise en forme des pâtons."* §15.1 keeps only the second phrase. "*la tourne*" appears nowhere in the cookbook.

---

## P-09 — LOW: the source contradicts itself on ficelle width

Both figures were magnified and read directly:

| Source page | Ficelle dimensions |
|---|---|
| p. 58 (Yield list) | 12 to 16 by **2** inches |
| p. 68 (Variations) | 12 to 16 by **1½** inches |

§15.1 §D records 1½ inches; the Yield line omits ficelle dimensions entirely, so the discrepancy is currently invisible. This is the source's error, not the cookbook's — but it should be on the record rather than silently resolved.

> **Fix:** a parenthetical at §D — *(the source's own Yield list on p. 58 says 2 inches; the Variations page says 1½ — the book contradicts itself)*.

---

## P-10 — LOW: round loaves, missing rise instruction

**§15.1 §D.** Source p. 69: *"Place the dough pucker side up on flour-rubbed canvas; seal the pucker by pinching with your fingers. **Flour lightly, cover loosely, and let rise to almost triple its size.** After unmolding upside down on the baking sheet, slash it as follows…"* The cookbook goes straight from sealing the pucker to unmolding, skipping the rise.

---

## P-11 — LOW: a quotation that isn't verbatim

**§T25 §D** presents this inside quotation marks:

> *"…As soon as **you're** able to make them flip over themselves in a group…"*

Source p. 133 prints **"you are"**. Everything else in the quotation matches exactly. The other two direct quotations checked against the pixels — the "complete control" line (p. 67) and the "queerly deformed shapes" line (p. 72) — are both verbatim.

---

## P-12 — LOW: caption error

**§T25, line 14053** — *"…sits just above where Method II begins **on the facing page**."*

Method II begins at the **bottom of page 132**, directly below the end of Method I, on the same page. Page 133 carries its continuation — the dried-beans practice note, the ingredient list, and the eggs-settling illustration.

> **Fix:** *"…sits just above where Method II begins on the same page, with Method II's own eggs-settling moment — its Step 3 below — on the facing page."*

---

## P-13 — MED: "straight crops" is not what these are

Both entries claim it:

- **§T25, line 14001** — *"They're straight crops of the photographed pages."*
- **§15.1, line 40466** — *"They're straight crops of the photographed pages…"*

Twelve of the fourteen are **uncropped photographs of an open book**: two-page spreads, with the reader's thumb in frame, a bookmark protruding from the top of every French bread shot, ambient shadow across the page, and the surrounding room visible around the edges. The 2026-08-10 changelog repeats the same word ("cropped and embedded").

The only genuine crops in the repo are the two ratatouille images, which *are* tight single-illustration crops.

> **Fix:** reword both to something honest — *"They're the photographed pages themselves, embedded whole."* Either that, or actually crop them (see P-17).

---

## P-14 — LOW: stale "still open" cross-reference

**§T24 §J, line 13986** lists among the chapter's open items:

> *"…and **peeling/seeding tomatoes (p. 505)** — supporting techniques the recipes cite."*

That technique is not open. It is transcribed in full at **§5.22 Ratatouille, Step 2**, with **both** of the source's illustrations (p. 505 and p. 506) embedded at the exact moments they teach.

> **Fix:** strike it from the open list and point to §5.22 Step 2 instead.

---

## P-15 — LOW: §5.22 embeds pictures but doesn't say so

§T25 and §15.1 each carry an "illustrations are embedded below" note and cross-reference each other. §5.22 Ratatouille embeds two source illustrations with no such note, and is named by neither. The three picture-carrying entries should form one set.

---

## P-16 — LOW: alt text under-describes three pictures

| File (post-P-01 naming) | Issue |
|---|---|
| `omelette-p130-131.jpg` | Alt covers only p. 130 (butter, sliding). P. 131's tilt-and-gather-at-the-far-lip illustration — Step 4 — isn't mentioned. |
| `p58-59-fraisage-kneading-shapes.jpg` | Alt names four shapes and says "and more". The chart labels nine: *pain de campagne, joko, pain boulot, ficelle, champignon, pistolet, tire-bouchon, baguette, bâtard.* |
| `p70-71-simulated-bakers-oven.jpg` | Alt is "The banneton and the bakers' lames"; the spread also carries the round-roll one-hand rolling illustration. |

---

## P-17 — LOW: picture quality

No re-shoot is required — **every word in all 14 files is legible**, and every value in them was read successfully for this audit. But the pictures are raw phone shots of a book held open, and it shows:

- **Hard diagonal shadow** falling across the lower-left text block: p58-59, p60-61, p62-63, p70-71, p72-73 (worst on p58-59 and p62-63).
- **A thumb inside the frame**, in two cases overlapping the text block: p58-59, p60-61, p62-63, and all four omelette spreads.
- **A bookmark** protruding into the top of every French bread spread.
- **Page skew and gutter curvature**, worst on the left-hand page of p64-65 and p70-71.
- **Ratatouille pair**: low contrast and washed out (measured tonal spread of only ~57 and ~85 levels between the 5th and 95th percentiles, against ~230 for the others), with heavy show-through from the reverse of the page, and visible rotation on `p505`.

Since these render inline in the cookbook, a crop-deskew-and-level pass on all 14 would materially improve the finished document. Purely cosmetic; no information is lost.

**Integrity is clean:** all 14 decode fully with no truncation — 8 French bread at 1700 px wide, 4 omelette at 1600, 2 ratatouille at 1600.

---

## P-18 — LOW: the ratatouille pages can't be verified from the pixels

Both ratatouille files are cropped past the page number, so their p. 505 / p. 506 attribution cannot be confirmed the way all twelve other files were. The attribution is *consistent* with two independent pieces of evidence:

1. The first picture ends on the printed heading **"TO SEED AND JUICE TOMATOES (for illustration, see next page)"** — so the second picture is the page immediately following the first.
2. §T24 independently cites p. 505 for peeling/seeding tomatoes.

Recorded as corroborated, not verified. If Cody still has the original photos, an uncropped version of either would settle it.

---

## P-19 — LOW: repo hygiene

- **`.gitattributes` is `* text=auto`** — line-ending normalization applied to every file, binaries included. Git's binary detection is protecting the JPEGs today (all 14 decode perfectly), but that's a safety net, not a policy. Add `*.jpg -text` (or `*.jpg binary`).
- **`.DS_Store` is committed at the repo root** — macOS Finder metadata, no purpose in the repo. Delete it and add to `.gitignore`.

---

## P-20 — INFO: only 14 photographs survive anywhere

The cookbook holds 649 entries — 522 numbered recipes plus 105 technique and 22 reference sections — essentially all of them transcribed from photographed pages, including five named batch scans (11-, 21-, 50-, 54-, and 55-page). **Fourteen source photographs exist in this repo. Every other picture in the project is gone** — they lived on session disks, not in git.

Two consequences worth naming:

- The 2026-09-06 page-order audits (Champions of Sous Vide, Meathead ×2, Salt Fat Acid Heat, Brines/Rubs/Sauces) were only possible because those sessions still had the files. **They cannot be repeated from this repo.** Any future re-check needs Cody to re-supply the originals.
- The changelog records that the omelette scan also included pp. 126–127 and the bread scan all twenty pages of pp. 55–74. Those were deliberately not embedded, correctly — **they carry no illustrations** — so this is not a coverage gap in the cookbook. But those files no longer exist anywhere.

If picture durability matters, committing the batch scans to `images/` (or an `images/source-scans/` tree) is the only thing that would fix it. Worth a decision, not an action to take unasked — it would be a large addition.

---

## P-21 — INFO: re-shoot ledger

The pictures Cody has already supplied that came through **incomplete** — cut off, obscured, or never shot. This is the standing "photograph these again" list, pulled from the cookbook's own flags. Each is already honestly flagged in place; none was guessed at.

### Pages that would complete a recipe

| Where | What's missing |
|---|---|
| [§14.3 Classic Tuiles](codys-cookbook.md#143-classic-tuiles) | Source says "continued on page 118" — that page never photographed. Missing the shaping step, bake time, and doneness cue. |
| [§7.56 Coq au Vin](codys-cookbook.md#756-coq-au-vin-chicken-in-red-wine-with-onions-mushrooms-and-bacon) | Finishing steps not photographed (source p. 263) |
| [§10.8 Quiche aux Fruits de Mer](codys-cookbook.md#108-quiche-aux-fruits-de-mer-shrimp-crab-or-lobster-quiche) | Most of the page not photographed |
| [§15.3 Basic Biscuits](codys-cookbook.md#153-basic-biscuits-cheese-or-bacon-variation) | Title and most of the ingredients not photographed |
| [§5.27 Smothered Eggplant](codys-cookbook.md#527-smothered-eggplant-onion--bell-pepper) | Source title not photographed |
| [§14.27 Buttermilk Biscuits](codys-cookbook.md#1427-light-and-flaky-buttermilk-biscuits) — Fruit Cobbler variation | Runs off the bottom of book p. 393 |
| [§14.21](codys-cookbook.md#1421-loris-chocolate-midnight-cake) / [§14.23](codys-cookbook.md#1423-fresh-ginger-and-molasses-cake) | Vanilla Cream filling, source p. 423 |
| [§14.26 Classic Pumpkin Pie](codys-cookbook.md#1426-classic-pumpkin-pie) | All-Butter Pie Dough, book p. 386; toppings ~pp. 423–425 |
| [§14.34 Poach It in Wine](codys-cookbook.md#1434-poach-it-in-wine) | Scented Cream, source p. 422 |
| [§14.25 Marshmallowy Meringues](codys-cookbook.md#1425-marshmallowy-meringues) | Rose Scented Berries and Cardamom Cream |
| [§4.174 Poblano-Basil Cream Sauce](codys-cookbook.md#4174-poblano-basil-cream-sauce) | Duxelles / Mushroom Cream Sauce: Step 1 and the shared ingredient list, book p. 192 |
| [§4.117 Kansas City Classic BBQ Sauce](codys-cookbook.md#4117-kansas-city-classic-barbecue-sauce) | Title and headnote, book pp. 174–175 — confirmed absent from the 21-page scan; also its mixing method, which [§7.136](codys-cookbook.md#7136-championship-pork-ribs) and [§7.141](codys-cookbook.md#7141-championship-chicken) both need |
| [§7.47 Shrimp Roast](codys-cookbook.md#747-shrimp-roast) | Curd Rice — name visible, method on an unphotographed page |
| [§7.55 Boeuf à la Mode](codys-cookbook.md#755-braised-beef-pot-roast--boeuf-à-la-mode-beef-braised-in-red-wine) | Cold Braised Beef variation, on the following page |
| [§10.11 Garlic Cheese Grits](codys-cookbook.md#1011-garlic-cheese-grits) | "Fried Grits" — cut off at the bottom of the photo |
| [§15.8 Skillet Cornbread](codys-cookbook.md#158-old-fashioned-skillet-cornbread-and-hush-puppies) | "PANKO PERFECT" callout — title only, no body text anywhere in the scan |
| [§T27](codys-cookbook.md#t27-sous-vide-not-so-premium-steak-cuts-codys-method) / [§T24](codys-cookbook.md#t24-the-french-sauce-families--roux-ratios) | Sauce Bordelaise — printed in another chapter, never photographed |
| §13 Meathead — Sweet and Sour Coleslaw (p. 362) | Dressing and slaw amounts cut off at the right margin |
| §13 Meathead — untitled polenta (p. 360) | Mid-recipe fragment only; no title, headnote, or ingredients |
| §13 Meathead Method — Pineapple Foster (p. 382) | Headnote only, cut off mid-sentence |
| §13 Meathead Method — fried-chicken derivative recipe | Fragment only, no title or ingredients |

### Pages where the photo is legible but marginal

| Where | Problem |
|---|---|
| [§4.31 Mediterranean Herb Rub](codys-cookbook.md#431-mediterranean-herb-rub) | Recipe box partly obscured; **ingredient proportions are reconstructed and may not match the source.** Entry itself asks for a clean re-photo of pp. 442–443. Highest-value re-shoot on this list. |
| [§5.18 Pickled Beets with Horseradish Cream](codys-cookbook.md#518-pickled-beets-with-horseradish-cream) | Horseradish cream step at a steep angle, partly obscured; method reconstructed from the ingredient list |
| [§4.9 Hollandaise](codys-cookbook.md#49-hollandaise-sauce) | Roasted-goose stuffing name obscured (a cross-reference only) |
| [§5.39 Fennel Fondant](codys-cookbook.md#539-fennel-fondant), [§7.85 Hanger Steak](codys-cookbook.md#785-hanger-steak-with-duck-fat-wild-mushrooms) | Page footers cropped past the bottom edge — page numbers verified absent, recipe text whole |

### Adjacent recipes glimpsed but not captured

Not gaps in any existing entry — pages that would each add a new recipe: a second unnamed soup at [§8.17](codys-cookbook.md#817-minted-sweet-pea-and-spinach-soup) (a photo of p. 56 would resolve it); "Greek Lemon Soup" at [§8.18](codys-cookbook.md#818-gazpacho); a vegetable-and-rice soup and a "Malcolm and Versie's" title at [§8.19](codys-cookbook.md#819-crawfish-bisque-bisque-décrevisses); a raspberry-butter fish fillet at [§8.20](codys-cookbook.md#820-six-onion-soup).

---

## Verified clean

Recorded so the next audit knows what has already been settled.

**Page identity — all 8 French bread files correct.** Each footer cropped and magnified independently in Pass 2: 58/59, 60/61, 62/63, 64/65, 66/67, 68/69, 70/71, 72/73. Every filename matches its contents. The rotation defect is confined to the omelette set.

**File integrity and wiring.** All 14 files decode fully, no truncation. 14 image references, 14 files on disk: zero broken paths, zero orphans, zero duplicates, no case mismatches, no images referenced from outside `images/`.

**§15.1 ingredients — every value checked against page 58 and correct:** 1 cake (0.6 oz) fresh yeast or 1 package dry-active; ⅓ cup warm water, not over 100°F; 3½ cups (about 1 lb) all-purpose flour, scooped and swept; 2¼ tsp salt; 1¼ cups tepid water at 70–74°F.

**§15.1 — also verified correct against the pictures:**

- Delayed-action chart, including the row mapping the source prints as two loose columns (65°F → 5–6 hr, 55°F → 7–8 hr, refrigerator → 9–10 hr) — the cookbook's table pairs them correctly.
- Rise targets: 3 cups of dough to 10½ cups on the first rise, "not quite triple" on the second, "almost triple" on the final.
- The deflating sequence and its order — near-to-far, left, right, then near tucked under.
- The slash pattern: three slashes, far cut first then middle then third, blade almost parallel, less than half an inch deep.
- Baking: 450°F, sprayed at 3-minute intervals ×3, ~25 minutes, hollow thump; cooling 2–3 hours; storing and thawing at 400°F for ~20 minutes; canvas housekeeping.
- Self-criticism table — 5 of 7 rows verified word-for-word against p. 73. The remaining two rows (both flavor rows) are on p. 74, which isn't among the pictures held here; nothing contradicts them.
- Machine note correctly attributed to p. 74, per the pointer printed on p. 58.

**§T25 — verified correct against the pictures:** both methods' step content across pp. 128–135; the 30–40 beating strokes; 6 Tbsp for two eggs and 9 for three; the ¼-inch depth rule and the 10–11-inch pan for 8 eggs; the 3-or-4-second broken custard; the fillings. **And the fix recorded in the 2026-08-10 changelog is confirmed correct:** the "4 or 5 short, sharp blows" step does belong to Method I, and page 132 shows it exactly where the cookbook now places it.

**§5.22 — verified correct against the pictures:** both printed illustration captions, the 10-second blanch, and the strainer-over-a-measuring-cup method.

**Changelog consistency.** The 2026-08-10 entry saying the omelette illustrations "can't be embedded in this text-only cookbook" is properly superseded by a later same-day entry recording that Cody pushed back and they were embedded. No contradiction left standing.

---

## Suggested order of application

1. **P-01** — the rename. Touches no markdown, so it can land immediately regardless of what the other session is doing.
2. **P-03** — the one confirmed factual correction. Small, surgical.
3. **P-04, P-05, P-06, P-07, P-10** — the §15.1 content restorations. One editing pass.
4. **P-08, P-09, P-11, P-12, P-13, P-14, P-15, P-16** — wording, captions, cross-references. One editing pass.
5. **P-17, P-19** — cosmetic and hygiene, whenever.
6. **P-02, P-20, P-21** — questions and decisions for Cody, not edits.

Every applied item needs its changelog line, per [CLAUDE.md §2](CLAUDE.md).
