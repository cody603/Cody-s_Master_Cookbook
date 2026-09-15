#!/usr/bin/env python3
"""Manage family cookbook photos.

  python3 tools/photos.py scan      # find new photos, add stubs to images/photos.json
  python3 tools/photos.py check     # report anything missing a caption or people
  python3 tools/photos.py index     # regenerate photo-index.md
  python3 tools/photos.py strip     # remove GPS/location data from every photo

Layout:  images/family/<recipe>-<slug>/<YYYY-MM-DD>-<nn>-<what-it-shows>.jpg
"""
import json, os, re, sys, subprocess
from collections import defaultdict

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
FAM  = os.path.join(ROOT, 'images', 'family')
MAN  = os.path.join(ROOT, 'images', 'photos.json')
IDX  = os.path.join(ROOT, 'photo-index.md')
EXT  = ('.jpg', '.jpeg', '.png', '.heic', '.webp')

FNAME = re.compile(r'^(?P<date>\d{4}-\d{2}-\d{2})-(?P<seq>\d{2})-(?P<slug>[a-z0-9-]+)\.\w+$', re.I)
DIR   = re.compile(r'^(?P<num>T?\d+(?:\.\d+)?)-(?P<slug>[a-z0-9-]+)$', re.I)


def load():
    if os.path.exists(MAN):
        return json.load(open(MAN, encoding='utf-8'))
    return {'_readme': 'Photo manifest for the family cookbook. See photo-guide.md.',
            'photos': []}


def save(m):
    m['photos'].sort(key=lambda p: (p['recipe'], p['date'], p['file']))
    json.dump(m, open(MAN, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    print(f'{len(m["photos"])} photos in manifest')


def walk():
    for d in sorted(os.listdir(FAM)) if os.path.isdir(FAM) else []:
        p = os.path.join(FAM, d)
        if not os.path.isdir(p):
            continue
        for f in sorted(os.listdir(p)):
            if f.lower().endswith(EXT):
                yield d, f


def cmd_scan():
    m = load()
    known = {p['file'] for p in m['photos']}
    added = 0
    for d, f in walk():
        rel = f'images/family/{d}/{f}'
        if rel in known:
            continue
        dm, fm = DIR.match(d), FNAME.match(f)
        m['photos'].append({
            'file': rel,
            'recipe': dm.group('num') if dm else '?',
            'date': fm.group('date') if fm else '',
            'seq': int(fm.group('seq')) if fm else 0,
            'caption': '',                     # <- fill these in
            'people': None,                    # <- and these ([] once you've checked and nobody's in it)
            'hero': False,
            'alt': '',
        })
        added += 1
    print(f'found {added} new photo(s)')
    if added:
        print('   -> fill in caption + people in images/photos.json, then: photos.py index')
    save(m)


def cmd_check():
    m = load()
    bad = 0
    for p in m['photos']:
        miss = [k for k in ('caption', 'date') if not p.get(k)]
        if p.get('people') is None:
            miss.append('people (use [] if nobody is in the shot)')
        if p['recipe'] == '?':
            miss.append('recipe (folder name must start with the section number)')
        if not os.path.exists(os.path.join(ROOT, p['file'])):
            miss.append('FILE MISSING')
        if miss:
            bad += 1
            print(f'  {p["file"]}  needs: {", ".join(miss)}')
    heroes = defaultdict(int)
    for p in m['photos']:
        if p.get('hero'):
            heroes[p['recipe']] += 1
    for r, n in heroes.items():
        if n > 1:
            print(f'  §{r}: {n} photos marked hero — pick one')
    print('all good' if not bad else f'{bad} photo(s) need attention')
    return 1 if bad else 0


def cmd_index():
    m = load()
    by = defaultdict(list)
    for p in m['photos']:
        by[p['recipe']].append(p)
    everyone = sorted({n for p in m['photos'] for n in (p.get('people') or [])})
    o = ['# Photo Index', '',
         f'**{len(m["photos"])} photo{"s" if len(m["photos"])!=1 else ""} across {len(by)} recipe{"s" if len(by)!=1 else ""}.** Generated — run `python3 tools/photos.py index` after adding any.',
         '', 'See [photo-guide.md](photo-guide.md) for how to add them.', '']
    if everyone:
        o += ['## Who\'s in the book', '']
        for n in everyone:
            shots = [p for p in m['photos'] if n in (p.get('people') or [])]
            rec = sorted({p['recipe'] for p in shots})
            o.append(f'- **{n}** — {len(shots)} photo(s), across §{", §".join(rec)}')
        o.append('')
    o += ['---', '', '## By recipe', '']
    for r in sorted(by, key=lambda x: [int(t) if t.isdigit() else 0 for t in re.split(r'\D+', x) if t]):
        ps = sorted(by[r], key=lambda p: (p['date'], p['seq']))
        o.append(f'### §{r}')
        o.append('')
        for p in ps:
            star = ' ⭐' if p.get('hero') else ''
            who = f' — *{", ".join(p["people"])}*' if p.get('people') else ''
            o.append(f'- `{os.path.basename(p["file"])}`{star} — {p.get("caption") or "*(no caption yet)*"}{who}  <small>{p.get("date","")}</small>')
        o.append('')
    open(IDX, 'w', encoding='utf-8').write('\n'.join(o) + '\n')
    print(f'wrote photo-index.md ({len(m["photos"])} photos)')


def cmd_strip():
    """Drop GPS/location tags. Faces are a choice; broadcasting your address isn't."""
    try:
        subprocess.run(['exiftool', '-ver'], capture_output=True, check=True)
    except Exception:
        print('exiftool not installed — skipping (install it before publishing photos)')
        return
    files = [os.path.join(FAM, d, f) for d, f in walk()]
    if not files:
        print('no photos yet')
        return
    subprocess.run(['exiftool', '-gps:all=', '-overwrite_original', *files], check=False)
    print(f'stripped location data from {len(files)} photo(s)')


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'check'
    fn = {'scan': cmd_scan, 'check': cmd_check, 'index': cmd_index, 'strip': cmd_strip}.get(cmd)
    if not fn:
        print(__doc__); sys.exit(2)
    sys.exit(fn() or 0)
