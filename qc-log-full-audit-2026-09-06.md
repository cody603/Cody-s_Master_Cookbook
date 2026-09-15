# Full Cookbook QC Log — 2026-09-06

**Companion to [`qc-log-pictures-2026-09-06.md`](qc-log-pictures-2026-09-06.md).** That log covers the 14 pictures. This one covers the master file itself — every entry, every index, every rule in [CLAUDE.md](CLAUDE.md).

**Status: LOG ONLY — nothing in `codys-cookbook.md` was changed.** Another session is live on the master; these are staged for later.

---

## First: the batch photos and PDFs are not on this machine

Cody asked for the batch photos and PDFs to be checked. **They cannot be reached from this session.** This was established by exhaustive search, not assumption:

| Search | Result |
|---|---|
| Every PDF on the filesystem | **0** |
| Every image outside the repo | 0 (only my own audit crops in scratch) |
| Images in the repo | the same **14 JPEGs** already audited |
| Every file ever added in git history | those 14 JPEGs, `.DS_Store`, `.gitattributes`, and `.md` files — **nothing else, ever** |
| Files ever deleted from git history | **none** |
| Git LFS pointers | not in use |
| Total `.git` size | 6.2 MB — far too small to have held a 55-page scan |

The five named batch scans (11-, 21-, 50-, 54-, and 55-page) and every other photographed page lived on earlier sessions' disks. They were never committed. **To QC them I need them uploaded to a session** — then I can do the same pixel-level pass that caught the omelette page rotation.

Everything below is what *could* be checked, checked exhaustively.

---

## What was audited

**All 649 entries** — 522 numbered recipes, 105 technique entries, 22 reference sections — against every structural rule in CLAUDE.md, by script rather than by eye, so coverage is 100% rather than a sample.

Checks run: link integrity · TOC coverage · recipe and technique numbering · required-section presence and order · difficulty badges · Difficulty & Time Index coverage, sort order, and agreement with every badge · Nutrition presence, serving descriptions, and arithmetic · keto tagging across all four required places · Family Ratings Index membership and counts · grocery-list store conventions · placeholder compliance · changelog ordering · duplicate titles.

**Headline: 14 findings. The structural spine is in excellent shape — 6,737 internal links and not one broken, zero numbering gaps, zero section-order violations. The defects are in the indexes, which have drifted behind the content.**

---

## Verdict summary

| ID | Sev | Where | What |
|---|---|---|---|
| **S-01** | **HIGH** | TOC L198–224 | **79 of 105 technique entries missing from the TOC** — the list stops at T28 |
| S-02 | MED | §14.26 L39781 | No difficulty badge on the entry, though the index says 🟢 |
| S-03 | MED | Index L1269, L1282 | Two rows out of sort order |
| S-04 | MED | Family Ratings Index | Stale — missing 4 ❤️ and 3 👍; declared counts too low |
| S-05 | MED | Index prose | Four stale counts, one off by a factor of ~7 |
| S-06 | MED | §4.36 L3929 | Nutrition rows disagree by ~2× |
| S-07 | MED | CLAUDE.md §3 | Documents a grocery convention the cookbook abandoned entirely |
| S-08 | LOW-MED | 4 entries | Incomplete recipes marked as placeholders, treated inconsistently |
| S-09 | LOW | 4 entries | Nutrition block with no "What a serving is" line |
| S-10 | LOW | 6 entries | Badge times disagree with index row times |
| S-11 | LOW | §T25 L13995 | Per-serving low end divided by 1.5, not 2 |
| S-12 | LOW | §7.69 L26180 | Whole-dish and per-serving rows measure different things |
| S-13 | LOW | §4.22 / §4.38 | Two recipes named "Mustard Sauce", no cross-reference |
| S-14 | LOW | grocery headings | Two spellings of the Hong Kong heading; 15 "Specific store" variants |

---

## S-01 — HIGH: 79 technique entries are missing from the Table of Contents

The TOC's **"T. Cooking Techniques & Tips"** block runs from **L198 to L224** and lists **26 entries: T1–T8 and T11–T28.** It then stops. The next line is `- [12. Recipes To Document]`.

**T29 through T107 — 79 entries — were never added.** There is no separate technique index anywhere in the file, so from the TOC these are simply unreachable.

That's the entire body of reference material added by the *Salt, Fat, Acid, Heat* and both *Meathead* projects: all the BBQ science, meat and fish buying, rib and brisket anatomy, rubs, the Warp heat scale, the ingredient notes. They *are* linked from inside individual recipes — every one of those links resolves — but a reader browsing the TOC cannot find them, and neither can Cody.

For scale, the missing block is three times the size of the listed one:

| | Listed | Missing |
|---|---|---|
| Technique entries | 26 (T1–T8, T11–T28) | **79 (T29–T107)** |

*(T9 and T10 are a documented, deliberate gap — they became §8.0 and §10.0 in the 2026-08-12 reorganization, and the numbers were left vacant on purpose rather than renumbering T11–T28. Correctly handled; not a defect.)*

> **Fix:** extend the TOC block to T107. Given the size, consider sub-grouping it by source or subject the way the chapter listings are grouped — 105 flat entries is a lot to scan.

---

## S-02 — MED: §14.26 Classic Pumpkin Pie has no badge

**L39781.** Every other written-up recipe in the cookbook carries a difficulty/time badge — this is the only exception in 483.

The rating exists everywhere *except* the entry: the Difficulty & Time Index row (L1295) reads `🟢 | 25 min | 55 min | — | 2 hr 20 min`, and the 2026-09-06 changelog says it was "rated 🟢 Easy, a direct-bake custard."

> **Fix:** add the badge line to the entry, matching the index row:
> `**🟢 Easy** · **Prep ~25 min** · **Cook ~55 min** · **Start to finish ~2 hr 20 min** *(includes a 15 min freeze and a 1 hr cooling rest)*`

---

## S-03 — MED: two rows out of sort order

CLAUDE.md §3a: *"Sort the index by prep + cook."* I tested all 498 rows under three conventions for reading ranges — the index sorts by the **midpoint** (5 breaks under low-end, 4 under high-end, **2 under midpoint**), so midpoint is the working convention and these two are genuine strays:

| Row | Entry | prep+cook | Sits after | which is |
|---|---|---|---|---|
| L1269 | §7.99 Kermit's Second-Favorite Pork Chops | **58 min** | §7.49 "Brunette" de Veau | 65 min |
| L1282 | §7.108 Santa Maria Tri-Tip | **72 min** | §7.145 60-Minute Ribs, Dreamland Style | 90 min |

Both are *Meathead* additions, inserted without re-sorting.

---

## S-04 — MED: the Family Ratings Index is stale

Seven rated recipes are marked in the TOC but appear nowhere in the Family Ratings Index — verified absent, not merely under a different anchor:

| Mark | Missing from the index |
|---|---|
| ❤️ | §4.99 Tomatillo Avocado Salsa · §5.37 Mamma's Spinach · §8.34 Shrimp and Corn Chowder · §8.35 Tomato Basil Soup |
| 👍 | §4.98 Herdez Street Taco Sauce · §5.36 Lemon Green Beans · §8.33 Mamma's Deer/Beef Stew |

The group headings' declared counts are correspondingly low, and the arithmetic confirms the diagnosis exactly:

| Group | Heading says | Links in the group | TOC marks | Shortfall |
|---|---|---|---|---|
| ❤️ Family favorites | 56 | 56 | **60** | 4 |
| 👍 Tried and liked | 14 | 14 | **17** | 3 |
| 🔖 Want to try | 19 | 19 | 19 | ✅ none |

> **Fix:** add the seven, and update the two headings to 60 and 17.

---

## S-05 — MED: four stale counts in the index prose

| Claim | Where | Actual |
|---|---|---|
| *"The **fifteen** 🔴 Hard ones come down to five problems"* | Difficulty index, Reading this table | **22** 🔴 rows |
| *"Still unrated: **58** written-up entries"* | Family Ratings Index | **387** (483 written-up − 96 rated) |
| *"**11 of the 17** techniques"* | Family Ratings Index | there are now **105** technique entries |
| *"**44** of §4's sauces, rubs, and seasonings"* | Family Ratings Index | §4 now holds **176** entries |

The "unrated: 58" figure is the one to watch — it is off by a factor of nearly seven and makes the collection look far more thoroughly rated than it is.

*(A fifth claim, "30 minutes of work or less — 114 recipes", already carries its own inline caveat that it predates the recent batches. Left as-is, but it should be recounted in the same pass.)*

---

## S-06 — MED: §4.36's nutrition rows disagree by about 2×

**L3929, North Carolina Vinegar Sauce.**

| Row | Calories | Carbs |
|---|---|---|
| **Whole batch** | ~130 | 30 g |
| **Per serving** *(2 Tbsp, of 18)* | ~15 | 3 g |

130 ÷ 18 = **7 calories**, not 15. 30 g ÷ 18 = **1.7 g** carbs, not 3.

**The divisor is right** — I checked the yield rather than assuming: "about 2¼ cups" = 36 Tbsp = exactly 18 servings of 2 Tbsp. So one of the two rows is wrong.

**An independent estimate from the ingredient list says the whole-batch row is the low one.** 2 cups cider vinegar (~50 cal) + 3 Tbsp ketchup (~45 cal, ~11 g carbs) + 2 Tbsp brown sugar (~105 cal, ~27 g carbs) ≈ **200 cal and ~40 g carbs** for the batch — which puts a 2 Tbsp serving at about **11 cal and 2.2 g carbs**.

> **Fix:** recompute both rows from the ingredients. Neither currently printed figure is right.

---

## S-07 — MED: CLAUDE.md documents a grocery convention the cookbook no longer uses

**[CLAUDE.md §3C](CLAUDE.md)** specifies:

> Split by store, using these prefixes: **HK** — Hong Kong Market · **GEN** — general grocery · `GEN Fig jam (Trader Joe's)`

**That convention appears zero times in the cookbook.** It was replaced by an icon system that the cookbook documents in its own **Store Icon Key** section (L820): ☯️ Hong Kong / Chinese market · 🛒 general grocery · 🏪 a specific store, named in parentheses — with the deliberate rule that *"a named store never carries the cart."*

That system is in use across **496+** grocery lists. The cookbook is right and the project instructions are stale.

> **Fix: this one is CLAUDE.md's, not the cookbook's.** Update §3C to describe the icon key, and point it at the Store Icon Key section. Worth doing before the next batch, so a future session doesn't "correct" 496 recipes back to a convention Cody abandoned.

---

## S-08 — LOW-MED: incomplete recipes are filed as placeholders, and treated inconsistently

Four recipes are partial transcriptions — the source page ran out mid-recipe. The cookbook knows this and says so at L1361: *"not stubs, but genuinely incomplete transcriptions."* But the TOC marks them **○**, the same symbol as a true placeholder, and CLAUDE.md §3a says *"Placeholders don't get one"* — yet all four carry badges. They also get handled three different ways:

| Entry | TOC | Badge | Nutrition | Index times |
|---|---|---|---|---|
| §7.56 Coq au Vin | ○ | ✅ | ❌ | `?` |
| §10.8 Quiche aux Fruits de Mer | ○ | ✅ | **✅** | `?` |
| §14.3 Classic Tuiles | ○ | ✅ | ❌ | `?` |
| §15.3 Basic Biscuits | ○ | ✅ | ❌ | `?` |

Only §10.8 has a Nutrition block; the other three don't, for no stated reason.

> **Fix:** give incomplete transcriptions their own TOC status marker (◐ would read clearly against ✅ and ○), add it to the TOC legend, name the case in CLAUDE.md §3a so the badge isn't a rule violation, and settle whether a partial recipe gets a Nutrition block — then apply that to all four.

---

## S-09 — LOW: four Nutrition blocks with no serving description

CLAUDE.md §3b: *"**Always** describe what a serving actually is, in plain language. A number without a portion is useless."*

Missing the **What a serving is** line: **§T27** Sous Vide "Not-So-Premium" Steak Cuts (L14243) · **§T28** Sous Vide Chicken (L14364) · **§5.27** Smothered Eggplant, Onion & Bell Pepper (L18299) · **§10.8** Quiche aux Fruits de Mer (L37443).

479 of 483 have it, so this is four stragglers rather than a systemic gap.

---

## S-10 — LOW: badge times that disagree with the index

Every badge was compared field by field against its index row. **483 entries, 6 real disagreements** (the rest matched, once equivalent spellings like "1¾ hr"/"1 hr 45 min" and "60 min"/"1 hr" are treated as equal — which they are).

**Genuine conflicts — the two sources give different numbers:**

| Entry | Field | Badge | Index row |
|---|---|---|---|
| §7.86 Carpaccio of Sous Vide Octopus (L27530) | Prep | **35 min** | 40 min (L1184) |
| §9.22 Tailgate Muffuletta (L36361) | Slow cook | **3–5 hr** | 3–4 hr (L1047) |
| §4.53 Simple Tomato Sauce (L4871) | Cook | **1–3 hr** | 1 hr (L1277) |

**Range truncations — the index keeps only one end of the badge's range:**

| Entry | Field | Badge | Index row |
|---|---|---|---|
| §5.38 Roasted Veggies (L18989) | Cook | 20–25 min | 20 min |
| §14.1 Mixed Berry Cobbler (L38052) | Cook | 40–45 min | 45 min |
| §10.12 Grilled Grits (L37623) | Slow cook | 4 hr minimum | 4 hr – 2 days |

§4.53's is the one worth a look — a cook time of "1 hour" versus "1 to 3 hours" is a real planning difference, and it also affects where the row sorts.

---

## S-11 — LOW: §T25's per-serving low end is divided by 1.5

**L13995, The French Omelette.**

| Row | Calories | Fat | Protein |
|---|---|---|---|
| **Whole omelette** *(3 eggs + butter)* | ~370 | 30 g | 19 g |
| **Per serving** *(1 to 2 servings)* | ~250–370 | 20–30 g | 13–19 g |

The high ends are right (1 serving = the whole omelette). The low ends are all the whole divided by **1.5**: 370/1.5 = 247, 30/1.5 = 20, 19/1.5 = 12.7. But the row says *2* servings, and 2 servings means **÷2**: 185 cal, 15 g fat, 9.5 g protein.

Consistent across all three numbers, so it's one arithmetic habit rather than three slips.

> **Fix:** low ends become ~185 cal, 15 g fat, 9.5 g protein.

---

## S-12 — LOW: §7.69's rows measure different dishes

**L26180, Bengali Shish Kebabs.** The whole-dish row is the kebabs alone; both per-serving rows are *"with bread and toppings"*. So the columns don't reconcile — 1,500 ÷ 8 = 187 cal, but the appetizer serving reads ~280, and carbs go from 15 g whole to 14 g *per serving*, which is impossible for the same food.

The two per-serving rows are internally consistent with each other (main = exactly 2× appetizer), so only the whole-dish row is out of step.

> **Fix:** either include bread and toppings in the whole-dish row, or label it *(kebabs only, before bread and toppings)* so the mismatch is deliberate and visible.

---

## S-13 — LOW: two recipes called "Mustard Sauce", not cross-referenced

**§4.22** (L3186, *Louisiana Kitchen* — a thickened mustard-cream dip, 20 min cook) and **§4.38** (L4032, *How to Grill* — a no-cook grilling sauce, 3 min). Different sources, different techniques, same name, and **neither mentions the other**.

This is the only same-name pair in the cookbook left undisambiguated. Everywhere else the pattern is explicit — §4.35/§4.92 carry "distinct from" notes, §4.36/§4.91/§4.93 get a three-way comparison table, the three pestos all cross-link.

> **Fix:** a "distinct from" note in each direction, matching the existing pattern.

---

## S-14 — LOW: grocery heading variants

- **Two spellings of the same heading:** `☯️ Hong Kong / Chinese market` (11 uses) and `☯️ Hong Kong Market / Chinese market` (7). The Store Icon Key calls it "Hong Kong Market / Chinese market".
- **`🏪 Specific store` has ~15 suffix variants** — butcher, butcher counter, butcher/deli, fish market, fishmonger, seafood counter, fish market or seafood counter, deli, Asian market, specialty/online, gourmet/Mediterranean, Middle Eastern/spice shop, and bare. Not wrong, and arguably useful, but worth settling on a shortlist.

*(Checked and benign: 24 grocery bullets carry no store icon, but every one is a "Plus everything for §X" cross-reference line rather than a shoppable item.)*

---

## Verified clean

Recorded so the next audit doesn't re-plough it.

**Link integrity — perfect.** All **6,737** internal links resolve to a real heading. Zero broken. The 90-link repair in the 2026-09-06 QC pass has held, and nothing has regressed since.

**Structure — perfect.**
- **Section order:** 503 entries carry the A/B/C sections; **zero** order violations. Ingredients → Cooking Instructions → Grocery Shopping List holds everywhere.
- **Recipe numbering:** zero gaps and zero duplicates across all 11 numbered chapters (§4 1–176, §5 1–59, §6 1–8, §7 1–145, §8 0–40, §9 1–31, §10 0–12, §11 1–6, §14 1–34, §15 1–8, §16 1).
- **Technique numbering:** T1–T107 with no duplicates and no out-of-order entries; the only gap, T9–T10, is the documented 2026-08-12 move to §8.0/§10.0.
- The 23 entries without a full A/B/C are all technique or formula entries, which correctly don't have one. **No numbered recipe is missing a required section.**

**Difficulty & Time Index — near perfect.** 498 rows. Every one of the 483 written-up entries has a row (**zero missing**), no anchor is listed twice, and no row points at a non-existent entry. Difficulty agreement between badge and row is **482/483** — §14.26 (S-02) is the only exception.

**Nutrition — strong.** 480 of 483 written-up entries carry a block; the 3 without are incomplete transcriptions (S-08). 479 carry a serving description (S-09 covers the 4 that don't). **392 nutrition tables were arithmetic-checked** against their own stated serving counts; the only genuine problems are S-06, S-11 and S-12. Several tables that looked wrong on a first pass were re-checked and are correct — §9.30 Muffelatta (a "serves 2 to 4" range against a "~725–1,450" range, exactly right), §5.58 Smoked Tomato Raisins, §4.139 Balsamic Vinaigrette, §7.136 Championship Pork Ribs.

**Keto tagging — fully consistent.** All 5 keto recipes carry 🥑 on the badge line, 🥑 in the TOC, and net carbs in the Nutrition block. §7.30 Basil-Grilled Tuna surfaced as a candidate and turns out to be **correctly** untagged — the entry explains that its source doesn't print net carbs, and cites CLAUDE.md §3c for why the tag is withheld. Exactly the right call, documented in place.

**Changelog — clean.** 196 dated rows spanning 2026-08-08 to 2026-09-06, in perfect newest-first order. Zero out-of-sequence dates.

**Grocery conventions.** Zero legacy `HK`/`GEN` prefixes remain — the icon migration was complete, not partial (which is what makes S-07 a CLAUDE.md problem rather than a cookbook one).

**Duplicate titles.** Only one pair in 649 entries (S-13).

---

## Suggested order of application

1. **S-01** — the TOC technique block. Biggest reader-facing gap, self-contained, touches one region.
2. **S-02, S-06, S-10, S-11, S-12** — the numeric corrections. One pass.
3. **S-03, S-04, S-05** — index maintenance: re-sort two rows, add seven ratings, recount four figures. Best done together since they all live in the two index sections.
4. **S-07** — the CLAUDE.md fix. Do this early regardless of the rest, so the next batch session doesn't work from the stale spec.
5. **S-08** — the incomplete-vs-placeholder decision. Needs Cody's call on the marker and on whether partials get Nutrition.
6. **S-09, S-13, S-14** — small consistency cleanups.

Every applied item needs its changelog line, per [CLAUDE.md §2](CLAUDE.md).

---

## Still outstanding

**The batch photos and PDFs remain unaudited** — see the top of this log. Upload them to a session and the same treatment applies: page-by-page identity checks, transcription against the pixels, and the re-shoot ledger extended with anything new. The omelette rotation in the picture log is the kind of defect only that pass finds.
