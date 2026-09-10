# planner/ — the cookbook, one recipe per file

**This folder is generated from [`codys-cookbook.md`](../codys-cookbook.md) and is never edited by hand.** The master
file is the single source of truth (CLAUDE.md §1–§2); this is a derived view of it, rebuilt by
`python3 tools/build_planner.py` after every change to the master, so a chat session can fetch one recipe at a time
from GitHub. The master is over 4 MB, and a web fetch never gets past its front matter — that is the only reason this
folder exists.

- [`meal-planning-sheet.md`](meal-planning-sheet.md) — the fridge sheet. **Start here** when planning a week.
- [`staples.md`](staples.md) — the ⭐ Staples with badge and ⏰ countdown to dinner, one line each.
- [`index.md`](index.md) — every entry on one line: § number, title, difficulty, file.
- [`recipes/`](recipes/) — one file per recipe and technique entry, named by the entry's anchor.
- The weekly-planning workflow (what to produce, in what order, and how the calendar events are placed) is
  [§T111](recipes/t111-planning-a-week--the-conversation-mode-workflow.md) in the cookbook.

Raw-file URL pattern for a chat session: `https://raw.githubusercontent.com/cody603/Cody-s_Master_Cookbook/main/planner/<path>`.
