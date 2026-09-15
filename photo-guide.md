# The Photo Guide

**For the family cookbook.** Many photos per recipe, faces included — this is how they get filed so they're still
usable when we sit down to lay out the printed book.

---

## The two kinds of pictures, kept apart

They are not the same thing and shouldn't share a folder.

| | **Source scans** | **Family photos** |
|---|---|---|
| What | Photographed pages from cookbooks — technique diagrams | Our own photos: people, hands, the pot, the plate |
| Where | `images/omelette/`, `images/french-bread/`, `images/ratatouille/` | `images/family/` |
| Purpose | Teaching a technique | The book itself |
| How many | One per page spread | **As many as you want per recipe** |

The 14 existing scans stay exactly where they are — the cookbook links to them by path, and moving them would break
those links. Everything new goes under `images/family/`.

---

## Where a photo goes

```
images/family/<recipe-number>-<short-name>/<date>-<##>-<what-it-shows>.jpg
```

```
images/family/7.15-pauls-jambalaya/
    2026-09-14-01-kids-stirring-the-pot.jpg
    2026-09-14-02-andouille-going-in.jpg
    2026-09-14-03-the-pot-finished.jpg
```

**The date in the filename is doing real work.** Cook the jambalaya again next year and those photos drop into the same
folder without colliding, and the two sessions stay tellable apart. The `##` keeps them in the order they happened.

Folder name **must** start with the recipe's section number — that's how a photo gets tied back to its recipe.

---

## Adding a batch

```bash
python3 tools/photos.py scan     # finds new files, adds a stub for each
#   ... fill in caption + people in images/photos.json ...
python3 tools/photos.py check    # tells you what's still blank
python3 tools/photos.py index    # regenerates photo-index.md
```

Or just drop them in and say *"I added photos from tonight"* — the captions can be written conversationally and
filled in for you.

### What each photo records

```json
{
  "file": "images/family/7.15-pauls-jambalaya/2026-09-14-01-kids-stirring-the-pot.jpg",
  "recipe": "7.15",
  "date": "2026-09-14",
  "seq": 1,
  "caption": "Taking turns on the pot while the trinity cooks down.",
  "people": ["..."],
  "hero": true,
  "alt": "Two kids stirring a big pot at the stove"
}
```

- **`caption`** — what's happening, in a sentence. This is what prints under the photo.
- **`people`** — who's in it. Empty list `[]` means you checked and nobody is. This is the field that will matter most
  in ten years, and it's the one nobody remembers to fill in later.
- **`hero`** — the one shot that leads the recipe's page. One per recipe.
- **`alt`** — plain description for anyone who can't see the image.

---

## Shooting so it's usable later

Not art direction — just the things that make a photo unusable at print size.

- **Shoot in landscape for the wide shots, portrait for a person at the stove.** A printed page wants both; phones
  default to portrait and you end up with none of the first kind.
- **Get in closer than feels natural.** Hands doing the thing, not the whole kitchen.
- **Faces work best mid-task, not posed.** Someone looking down at what they're doing beats someone smiling at you.
- **Turn the overhead light on and get a window behind you, not in front.** Backlit faces go dark and can't be saved.
- **Take the plate shot before anyone eats.** Every single time, this is the one that gets forgotten.
- **Three to six per recipe is plenty** — a start, a couple of middles, a finish. More than that and nobody sorts them.
- **Don't delete the ugly ones on the spot.** The out-of-focus one of somebody laughing is usually the keeper.

**Keep the originals somewhere off this repo.** What's here is the working set for the book, not the archive.

---

## Two mechanical notes

**Location data gets stripped.** `python3 tools/photos.py strip` clears GPS tags before photos go up. Phones stamp
coordinates into every shot, and there's no reason for the repo to carry your address. Run it before committing a batch.

**Watch the repo size.** Photos are a few MB each; a few hundred and the repo gets slow to clone. If it starts to bite,
the fix is to resize the working copies down to something print-sized (~2000px on the long edge) and keep full-resolution
originals elsewhere.

---

## Later: the printed book

The manifest is built so the printed cookbook can be generated from it — `hero` picks each recipe's lead photo,
`caption` prints beneath, and `people` drives a "who cooked what" section at the back. Nothing else needs deciding now;
just get the captions and the names written down while you still remember them.

---

*Conventions live here for now. They belong in [CLAUDE.md](CLAUDE.md) eventually — noted so it doesn't get lost.*
