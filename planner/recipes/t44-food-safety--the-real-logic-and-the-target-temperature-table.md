<!-- GENERATED from codys-cookbook.md#t44-food-safety--the-real-logic-and-the-target-temperature-table — do not edit here; edit the master file and rerun tools/build_planner.py -->
[↑ Meal Planning Sheet](../meal-planning-sheet.md) · [Index](../index.md)

### T44. Food Safety — The Real Logic (and the Target Temperature Table)

<!-- TECHNIQUE-TAGS: meathead, food-safety, pasteurization, 7d, internal-temp, myth, ground-meat -->
**Tags:** `meathead` · `food-safety` · `pasteurization` · `7d` · `internal-temp` · `myth` · `ground-meat`
**Source:** **Meathead Goldwyn**, ***Meathead: The Science of Great Barbecue and Grilling*** (p. 42–57), dictated by Cody.
**Standing override, now applied:** per [§13 Meathead Cookbook](13-meathead-cookbook.md)'s recorded rule, **this entry's target temperature table now supersedes [§T32 How to Use Heat](t32-how-to-use-heat.md)'s Nosrat-sourced meat-doneness figures wherever the two touch the same ground.** §T32's own table has been annotated to point here rather than silently left to disagree.
**Used in:** the doneness temperature behind every meat and poultry entry in this cookbook — [§6.2 Pulled Pork](62-pulled-pork.md)'s 195°F is actually on the low side of the 203°F this entry recommends, [§7.76 Hamburgers with Herb Butter](776-hamburgers-with-herb-butter.md)'s 160°F ground-beef floor is confirmed exactly, and [§T27](t27-sous-vide-not-so-premium-steak-cuts-codys-method.md)/[§T28](t28-sous-vide-chicken-codys-method.md)'s sous vide temperatures sit inside the "chef temp" band below.

#### The actual standard: pasteurization, not sterilization

You can't sterilize meat and have it still be food — so the real standard is **pasteurization**: reducing pathogens until getting sick is extremely unlikely, not reducing them to zero. The USDA's benchmark is the **7D kill rate** — one cell surviving out of 10,000,000. Concretely: take 10,000 steaks with 1,000 bacteria each, and a true 7D reduction leaves a single surviving cell on just one of those 10,000 steaks.

**Pathogens don't die at one magic number — it's temperature *and* time together:**

| Temp | Time to 7D kill |
|---|---|
| 130°F | ~2 hours |
| 140°F | ~12 minutes |
| 160°F | ~8 seconds |
| 165°F | essentially instant |

**Carryover keeps killing microbes even after the meat is off the heat** — pull a turkey breast at 155°F and it keeps working toward safe the whole time it rests.

#### Whole muscle vs. ground meat — the distinction that actually matters

Microbes on a steak live **only on the surface**, and that surface hits well past 165°F almost instantly once it touches heat — so a 145°F *center* reading is genuinely fine on a whole cut. **Grinding changes everything:** it mixes surface contamination all the way through the meat, which is exactly why burgers need a full 160°F at the center, with no exceptions. Cattle and pigs are penned closely, fecal matter gets onto hides, knives cut through it during processing, and intestines occasionally get nicked — E. coli sitting harmlessly on a steak's surface becomes dangerous the instant it's ground into the center of a patty.

**The steakhouse math, as an illustration, not a recommendation:** chefs know beef tastes best at 130°F and would go out of business cooking every steak to the USDA's 145°F recommendation — and go out of business faster if a customer got sick. Accepting a 6D reduction (10 surviving cells among 10,000 steaks) or even 5D (100 cells) is how a rare steak stays on a menu at all — a real, if small, elevated risk, and this cookbook's own [§T27 Sous Vide Steak](t27-sous-vide-not-so-premium-steak-cuts-codys-method.md) already operates in exactly this band. **Ground beef and poultry are a different case: contamination rates there run high enough that this cookbook sticks close to the USDA figures**, per [§7.76](776-hamburgers-with-herb-butter.md)'s existing 160°F callout, unless the meat is irradiated.

#### Myths this section busts

> ⚠️ **"Pink pork means trichinosis."** True historically, when hogs ate garbage — today the parasite is essentially eradicated in developed countries, with fewer than a dozen U.S. cases a year, mostly from wild game like bear rather than farmed pork. The parasite itself dies at 138°F, and the USDA's own pork minimum is now 145°F, well above that. (Cooking bear specifically: at least 138°F.)

> ⚠️ **"Cook chicken until the juices run clear."** Indisputably false, and following it will over- or under-cook the bird. The pink color is myoglobin, and cooking does change its structure so it absorbs light differently — but **there's no single fixed temperature where that change happens.** pH is a major factor: high-pH, low-acid muscle can need 170–180°F before the juices run fully clear, and thighs/drumsticks (more myoglobin than breast) need even more. **165°F is safe regardless of what color the juices are.**

> ⚠️ **"Meat is safe once it's no longer pink."** Color is never a reliable guide in either direction. Red or purple-tinted bones are just marrow, where blood is made — modern chickens are slaughtered at only 6–8 weeks, before their bones fully calcify, so that color shows through the shell and can tint nearby meat even at 180°F, fully safe. Pink meat can also come from nitric oxide or carbon monoxide in the cooker locking in myoglobin's color (the same chemistry behind [§T35's smoke ring](t35-smoke-science--combustion-the-smoke-ring-and-getting-blue-smoke.md)). And ground beef can turn brown from plain oxidation long before it's actually safe at 160°F. **Use a thermometer — never color.**

#### Target temperatures

| Food | Target |
|---|---|
| Beef, lamb, venison, duck breast | 130–135°F medium-rare (chef temp); USDA minimum 145°F |
| Pork chops/roasts | 130–135°F (chef temp); USDA minimum 145°F |
| Ribs, pork shoulder, brisket | **203°F** — deliberately well past well-done, for the connective tissue, not the doneness |
| Chicken & turkey | 165°F USDA; most chefs pull at 160°F to let carryover finish the job |
| Ground meat, burgers, sausage | **160°F, no exceptions** |
| Fish | 145°F (parasite safety) |
| Precooked ham & hot dogs | 140°F — already cured and cooked, this is just reheating |

*Why 203°F for the big smoked cuts specifically:* past that point you're no longer cooking for doneness at all — you're melting connective tissue and rendering fat, which is a completely different goal than "safely cooked."

#### Other useful benchmarks, in one place

34–39°F ideal fridge temp · 41–130°F the food-safety danger zone · 95–130°F animal fats begin to soften and melt · 130°F+ the kill zone begins · 135°F connective tissue starts contracting and squeezing out juice · 150–165°F the stall zone (see [§T33](t33-how-meat-actually-cooks--conduction-carryover-and-why-resting-is-a-myth.md)) · 160–205°F collagen actively melts into gelatin · 160–165°F the instant-kill zone for pathogens · 212°F boiling point at sea level, dropping ~2°F per 1,000 ft of elevation · 225°F the recommended low-and-slow air temperature · 310°F Maillard really accelerates · 325°F the recommended poultry temperature, hot enough to render fat and crisp skin · 425°F where Teflon-coated thermometer cables start to melt · 500–700°F hardwood smokes · 700–1,000°F hardwood actively flames.

**To temp a whole bird:** push the probe through the thickest part of the breast all the way to the ribs, then slowly withdraw it, reading continuously as it comes back out — the lowest reading along that path is the one that matters.

[↑ Table of Contents](../index.md)

---
