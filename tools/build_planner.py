#!/usr/bin/env python3
"""Build planner/ from codys-cookbook.md.

planner/ is a DERIVED, machine-generated view of the master file, made so a chat
session can fetch one recipe at a time from GitHub (the master is 4 MB and a web
fetch never reaches past its front matter). Nothing here is edited by hand; every
file is overwritten on each run. The master file stays the single source of truth
(CLAUDE.md §1–§2).

Outputs:
  planner/README.md                   what this folder is + the weekly-planning workflow pointer
  planner/meal-planning-sheet.md      the Meal Planning Sheet, links rewritten to recipe files
  planner/index.md                    one row per recipe: §, title, badge, ⏰ countdown, file
  planner/recipes/<anchor>.md         one file per recipe / technique entry
"""
import os, re, sys, shutil, collections

ROOT = '/home/user/Cody-s_Master_Cookbook'
BOOK = os.path.join(ROOT, 'codys-cookbook.md')
OUT = os.environ.get('PLANNER_OUT', os.path.join(ROOT, 'planner'))
REC = os.path.join(OUT, 'recipes')

def slug(t):
    t = re.sub(r'[^\w\s-]', '', t.strip().lower())
    return t.replace(' ', '-')

src = open(BOOK, encoding='utf-8').read()
lines = src.split('\n')

# ---- 1. entry boundaries -------------------------------------------------
ENTRY = re.compile(r'^(##|###) ((\d+)\. |(\d+\.\d+) |(T\d+)\. )(.*)$')
entries = []          # (start_line, end_line, number, title, anchor)
seen = collections.Counter()
anchor_of_line = {}   # line -> anchor (all headings, GitHub-style dedupe)
for i, ln in enumerate(lines):
    m = re.match(r'^(#{1,6}) (.+?)\s*$', ln)
    if not m:
        continue
    a = slug(m.group(2))
    a2 = a if not seen[a] else f'{a}-{seen[a]}'
    seen[a] += 1
    anchor_of_line[i] = a2

starts = []
for i, ln in enumerate(lines):
    m = ENTRY.match(ln)
    if m:
        num = m.group(3) or m.group(4) or m.group(5)
        starts.append((i, num, m.group(6).strip(), anchor_of_line[i]))
# an entry ends at the next entry start, or at the next ## / # heading
for k, (i, num, title, anchor) in enumerate(starts):
    end = len(lines)
    if k + 1 < len(starts):
        end = starts[k + 1][0]
    for j in range(i + 1, end):
        if re.match(r'^#{1,2} ', lines[j]):
            end = j
            break
    entries.append((i, end, num, title, anchor))

# ---- 2. anchor -> file map ----------------------------------------------
anchor_file = {}      # anchor -> (file, sub-anchor or None)
for (i, end, num, title, anchor) in entries:
    fname = anchor + '.md'
    for j in range(i, end):
        if j in anchor_of_line:
            anchor_file[anchor_of_line[j]] = (fname, None if j == i else anchor_of_line[j])

sheet_s = lines.index('## Meal Planning Sheet')
sheet_e = next(j for j in range(sheet_s + 1, len(lines)) if re.match(r'^## ', lines[j]))
for j in range(sheet_s, sheet_e):
    if j in anchor_of_line:
        anchor_file[anchor_of_line[j]] = ('../meal-planning-sheet.md', None if j == sheet_s else anchor_of_line[j])

LINK = re.compile(r'\]\(#([^)]+)\)')
def rewrite(text, base):
    """base: 'recipes' when the file lives in planner/recipes, 'planner' when in planner/."""
    def sub(m):
        a = m.group(1)
        if a in anchor_file:
            f, suba = anchor_file[a]
            if f.startswith('../'):                # the sheet
                path = f[3:] if base == 'planner' else f
            else:
                path = f if base == 'recipes' else 'recipes/' + f
            return '](' + path + ('#' + suba if suba else '') + ')'
        # anything else (TOC, indexes, changelog) -> the index
        return '](' + ('index.md' if base == 'planner' else '../index.md') + ')'
    text = LINK.sub(sub, text)
    text = text.replace('](images/', '](../../images/' if base == 'recipes' else '](../images/')
    up = '../../' if base == 'recipes' else '../'
    text = text.replace('](CLAUDE.md', '](' + up + 'CLAUDE.md').replace('](CHANGELOG.md', '](' + up + 'CHANGELOG.md')
    return text

# ---- 3. write ------------------------------------------------------------
if os.path.isdir(OUT):
    shutil.rmtree(OUT)
os.makedirs(REC)

BADGE = re.compile(r'^\*\*(🥑 Keto\*\* · \*\*)?(🟢 Easy|🟡 Medium|🔴 Hard)\*\*')
COUNT = re.compile(r'^\*\*⏰ Countdown to dinner:\*\*\s*(.*)$')
rows = []
for (i, end, num, title, anchor) in entries:
    body = '\n'.join(lines[i:end]).rstrip() + '\n'
    head = (f'<!-- GENERATED from codys-cookbook.md#{anchor} — do not edit here; edit the master file and rerun tools/build_planner.py -->\n'
            f'[↑ Meal Planning Sheet](../meal-planning-sheet.md) · [Index](../index.md)\n\n')
    open(os.path.join(REC, anchor + '.md'), 'w', encoding='utf-8').write(head + rewrite(body, 'recipes'))
    badge = countdown = ''
    for ln in lines[i:end]:
        if not badge and BADGE.match(ln):
            badge = re.sub(r'\s*\*\([^)]*\)\*', '', ln).replace('**', '')
        m = COUNT.match(ln)
        if m and not countdown:
            countdown = m.group(1).strip()
        if badge and countdown:
            break
    rows.append((num, title, anchor, badge, countdown))

# index.md — compact (kept small enough for a chat fetch); staples.md carries badge + countdown
def numkey(n):
    if n.startswith('T'):
        return (1, int(n[1:]), 0)
    a, _, b = n.partition('.')
    return (0, int(a), int(b or 0))
rows.sort(key=lambda r: numkey(r[0]))
t111 = next((a for (_, _, a, _, _) in rows if a.startswith('t111-')), 't111')
def circle(badge):
    m = re.search(r'(🟢|🟡|🔴)', badge)
    return (('🥑 ' if '🥑' in badge else '') + m.group(1)) if m else '—'
with open(os.path.join(OUT, 'index.md'), 'w', encoding='utf-8') as f:
    f.write('# Planner index — every entry in the cookbook, one line each\n\n')
    f.write('<!-- GENERATED from codys-cookbook.md — do not edit here -->\n\n')
    f.write('Start from the [Meal Planning Sheet](meal-planning-sheet.md); the ⭐ Staples with their badges and ⏰ countdowns are in '
            '[staples.md](staples.md); the weekly-planning workflow is [§T111](recipes/' + t111 + '.md). '
            'Circle = difficulty (🟢 easy · 🟡 medium · 🔴 hard); — = placeholder or store-bought product, nothing to cook.\n\n')
    f.write('| § | Recipe | | File |\n|---|---|---|---|\n')
    for num, title, anchor, badge, countdown in rows:
        t = re.sub(r'\s*\*\*.*$', '', title)
        f.write(f'| {num} | {t} | {circle(badge)} | [open](recipes/{anchor}.md) |\n')

with open(os.path.join(OUT, 'staples.md'), 'w', encoding='utf-8') as f:
    f.write('# ⭐ Staples — badge and ⏰ countdown to dinner\n\n')
    f.write('<!-- GENERATED from codys-cookbook.md — do not edit here -->\n\n')
    f.write('Every entry that carries a **⏰ Countdown to dinner** line (the ⭐ Staples on the [Meal Planning Sheet](meal-planning-sheet.md)). '
            'Offsets count back from the moment food hits the table; the weekly-planning workflow in [§T111](recipes/' + t111 + '.md) '
            'turns them into calendar events by subtracting each T− from the dinner time Cody gives.\n\n')
    f.write('| § | Recipe | Badge | ⏰ Countdown to dinner | File |\n|---|---|---|---|---|\n')
    for num, title, anchor, badge, countdown in rows:
        if not countdown:
            continue
        t = re.sub(r'\s*\*\*.*$', '', title)
        f.write(f'| {num} | {t} | {rewrite(badge, "planner")} | {rewrite(countdown, "planner")} | [{anchor}.md](recipes/{anchor}.md) |\n')

# ---- quick.md + aliases.md — the voice fast path (CHAT.md §1–§2) --------------
# tools/aliases.txt is hand-maintained: "anchor | alias; alias". Unknown anchors are reported, not silently dropped.
aliases = {}
alias_problems = []
try:
    for raw in open(os.path.join(ROOT, 'tools', 'aliases.txt'), encoding='utf-8'):
        raw = raw.strip()
        if not raw or raw.startswith('#') or '|' not in raw:
            continue
        a, _, rest = raw.partition('|')
        a = a.strip()
        names = [x.strip() for x in rest.split(';') if x.strip()]
        if a not in anchor_file:
            alias_problems.append(a)
            continue
        aliases.setdefault(a, [])
        for n in names:
            if n.lower() not in [x.lower() for x in aliases[a]]:
                aliases[a].append(n)
except FileNotFoundError:
    alias_problems.append('(tools/aliases.txt missing)')

title_of = {}
serves_of = {}
for (i, end, num, title, anchor) in entries:
    title_of[anchor] = re.sub(r'\s*\*\*.*$', '', title).strip()
    m = re.search(r'\*\*Per serving\*\* \*\(serves (\d+)', '\n'.join(lines[i:end]))
    if m:
        serves_of[anchor] = m.group(1)

CIRCLE = {'🟢': 'easy', '🟡': 'medium', '🔴': 'hard'}
def describe_cell(cell):
    """Turn one sheet cell into a plain-words line for quick.md, or None for headers/blank."""
    c = cell.strip()
    if not c:
        return None
    m = re.search(r'\[([^\]]+)\]\(#([^)]+)\)', c)
    if not m:
        if c.startswith('**'):
            return None
        return ('nocook', c.replace('*', '').strip())        # a No-Cook item: plain text, no link
    name, anchor = m.group(1), m.group(2)
    diff = next((w for e, w in CIRCLE.items() if e in c), '')
    mins = re.search(r'[🟩🟨🟥]\(([^)]*)\)', c)
    mins = mins.group(1).replace('†', '').replace(' min', ' min').strip() if mins else ''
    tags = []
    if '❤️' in c: tags.append('favorite')
    if '👍' in c: tags.append('liked')
    if '🍽️' in c: tags.append('whole meal, no side needed')
    if '♨' in c: tags.append('grill or smoker')
    if '🥑' in c: tags.append('keto')
    parts = [name]
    if diff: parts.append(diff)
    if mins: parts.append(mins + ' hands-on')
    if anchor in serves_of: parts.append('serves ' + serves_of[anchor])
    parts += tags
    line = ' — '.join(parts)
    if aliases.get(anchor):
        line += ' — sounds like: ' + ', '.join(aliases[anchor][:6])
    line += f' — file: recipes/{anchor}.md'
    return ('dish', line)

# walk the sheet's main table: the ⭐ Staple pair leads both columns
mains, sides, nocook = [], [], []
in_staples = False
col_open = [False, False]
for ln in lines[sheet_s:sheet_e]:
    if not ln.startswith('|'):
        continue
    cells = ln.split('|')[1:-1]
    if any('⭐ Staple Mains' in x for x in cells):
        in_staples = True; col_open = [True, True]; continue
    if not in_staples:
        continue
    for k, cell in enumerate(cells[:2]):
        if not col_open[k]:
            continue
        cs = cell.strip()
        if cs.startswith('**') and '](#' not in cs:
            col_open[k] = False          # next group header closes this column's staple run
            continue
        d = describe_cell(cell)
        if not d:
            continue
        kind, text = d
        if kind == 'nocook':
            nocook.append(text)
        elif k == 0:
            mains.append(text)
        else:
            sides.append(text)
    if not any(col_open):
        break

with open(os.path.join(OUT, 'quick.md'), 'w', encoding='utf-8') as f:
    f.write('# Quick sheet — the fridge list, for fast conversation\n\n')
    f.write('<!-- GENERATED from codys-cookbook.md (Meal Planning Sheet staples + tools/aliases.txt) — do not edit here -->\n\n')
    f.write('Read this first and answer from it. One line per dish: name — difficulty — hands-on minutes — serves — notes — how the name sounds when spoken — the recipe file. '
            'Speak the words, not the symbols. For everything else in the book, fetch meal-planning-sheet.md; for the calendar countdowns, staples.md.\n\n')
    f.write('## Staple mains\n\n')
    for x in mains: f.write('- ' + x + '\n')
    f.write('\n## Staple sides\n\n')
    for x in sides: f.write('- ' + x + '\n')
    f.write('\n## No-cook sides (no recipe, just buy them)\n\n')
    for x in nocook: f.write('- ' + x + '\n')
    f.write('\n## Household extras\n\nFruit, snacks, sandwich fixings and the like are in `../HOUSEHOLD-STAPLES.md` — ask "anything extra this week?" once.\n')
    f.write('\n## Not on this page\n\nEvery other cookable dish is on `meal-planning-sheet.md`. The chili is Cody\'s Chili (`recipes/848-codys-chili.md`); chili mac and Frito pie are one dish built on it.\n')

with open(os.path.join(OUT, 'aliases.md'), 'w', encoding='utf-8') as f:
    f.write('# Sounds like — spoken names for every dish that has them\n\n')
    f.write('<!-- GENERATED from tools/aliases.txt — add new mangles there, not here -->\n\n')
    f.write('Voice transcription mangles names. Match what you heard against the left side, by sound; the right side is the dish and its file. If nothing matches, take the closest and confirm in one word.\n\n')
    for a in sorted(aliases, key=lambda x: title_of.get(x, x).lower()):
        f.write(f'- {"; ".join(aliases[a])} → **{title_of.get(a, a)}** — recipes/{a}.md\n')

print(f'quick.md: {len(mains)} staple mains, {len(sides)} staple sides, {len(nocook)} no-cook; aliases for {len(aliases)} dishes')
if alias_problems:
    print('ALIAS ANCHORS NOT FOUND (fix tools/aliases.txt):', alias_problems)

# meal-planning-sheet.md
sheet = '\n'.join(lines[sheet_s:sheet_e]).rstrip() + '\n'
sheet = ('<!-- GENERATED from codys-cookbook.md#meal-planning-sheet — do not edit here -->\n\n' +
         rewrite(sheet, 'planner').replace('[↑ Table of Contents](index.md)', '[Index](index.md)'))
open(os.path.join(OUT, 'meal-planning-sheet.md'), 'w', encoding='utf-8').write(sheet)

# README.md — carries the build stamp a chat session compares against CHANGELOG.md (CHAT.md §4)
import datetime, subprocess
try:
    built_from = subprocess.run(['git', '-C', ROOT, 'rev-parse', '--short', 'HEAD'], capture_output=True, text=True).stdout.strip() or 'unknown'
except Exception:
    built_from = 'unknown'
built_at = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
open(os.path.join(OUT, 'README.md'), 'w', encoding='utf-8').write(f'''# planner/ — the cookbook, one recipe per file

**Built {built_at}, on top of commit `{built_from}`.** *(A chat session compares this against the top of `CHANGELOG.md` — if a changelog row is newer than this stamp, the planner hasn't caught up with it yet. See `CHAT.md` §4.)*

**This folder is generated from [`codys-cookbook.md`](../codys-cookbook.md) and is never edited by hand.** The master
file is the single source of truth (CLAUDE.md §1–§2); this is a derived view of it, rebuilt by
`python3 tools/build_planner.py` after every change to the master, so a chat session can fetch one recipe at a time
from GitHub. The master is over 4 MB, and a web fetch never gets past its front matter — that is the only reason this
folder exists.

**A chat session should start from [`../CHAT.md`](../CHAT.md)** — the operating manual — which sends it here.

- [`meal-planning-sheet.md`](meal-planning-sheet.md) — the fridge sheet. **Start here** when planning a week.
- [`staples.md`](staples.md) — the ⭐ Staples with badge and ⏰ countdown to dinner, one line each.
- [`index.md`](index.md) — every entry on one line: § number, title, difficulty, file.
- [`recipes/`](recipes/) — one file per recipe and technique entry, named by the entry's anchor.
- The weekly-planning workflow (what to produce, in what order, and how the calendar events are placed) is
  [§T111](recipes/{t111}.md) in the cookbook.
- Things a chat session may write to live outside this folder: [`../PROPOSED-REVISIONS.md`](../PROPOSED-REVISIONS.md)
  (the intake queue) and [`../HOUSEHOLD-STAPLES.md`](../HOUSEHOLD-STAPLES.md) (groceries that aren't recipes).

Raw-file URL pattern for a chat session: `https://raw.githubusercontent.com/cody603/Cody-s_Master_Cookbook/main/planner/<path>`.
''')

print(f'{len(entries)} entries → planner/recipes; sheet {len(sheet)} bytes; index rows {len(rows)}')
missing = [r[0] for r in rows if not r[3] and not r[0].startswith('T')]
print('entries with no badge (placeholders/products):', len(missing))
