#!/usr/bin/env python3
"""Build a meal-plan spec (JSON) for tools/mealplan.js.

Usage: python3 tools/build_week.py "Week of Sept 8" Mon=7.15 Tue=7.16 ... > week.json
"""
import sys, json, re, os, subprocess
sys.path.insert(0, os.path.dirname(__file__))
from extract_recipes import main as extract, load

# where an item is bought -> which list it lands on, in shopping order
ORDER = ['General grocery', 'Hong Kong / Chinese market', 'Butcher / meat counter',
         'Fish market / seafood counter', 'Specific store', 'Order online / Amazon']

def bucket(store):
    s = store.lower()
    if 'hong kong' in s or 'chinese' in s or 'asian' in s: return 'Hong Kong / Chinese market'
    if 'butcher' in s or 'deli' in s or 'meat' in s:       return 'Butcher / meat counter'
    if 'fish' in s or 'seafood' in s:                      return 'Fish market / seafood counter'
    if 'online' in s or 'amazon' in s or 'mail' in s:      return 'Order online / Amazon'
    if 'general' in s or not s.strip():                    return 'General grocery'
    return 'Specific store'

OVR = json.load(open(os.path.join(os.path.dirname(__file__), 'ratings.json')))['overrides']

BADGE = re.compile('^\\*\\*(?:\U0001F951 Keto\\*\\* \u00b7 \\*\\*)?(\U0001F7E2 Easy|\U0001F7E1 Medium|\U0001F534 Hard)\\*\\*.*$', re.M)
LEVEL = {'\U0001F7E2 Easy': 'Easy', '\U0001F7E1 Medium': 'Moderate', '\U0001F534 Hard': 'Hard'}

def timeline(num, ents):
    """Return (level, hands-on). Level honours the overrides in tools/ratings.json."""
    for e in ents:
        t = e['title']
        if t.startswith(num + ' ') or t.startswith(num + '.'):
            m = BADGE.search(e['body'])
            level, bl = (LEVEL.get(m.group(1), ''), m.group(0)) if m else ('', '')
            prep = re.search(r'\*\*Prep\s*([^*]+)\*\*', bl)
            cook = re.search(r'\*\*Cook\s*([^*]+)\*\*', bl)
            parts = [x.group(1).strip() for x in (prep, cook) if x]
            hands = ' + '.join(p for p in parts if p.lower().strip() not in ('none', 'none on its own'))
            if num in OVR:
                level = OVR[num]['level']
            return level, hands
    return OVR.get(num, {}).get('level', ''), ''

def main():
    title_week = sys.argv[1]
    pairs = [a.split('=', 1) for a in sys.argv[2:]]
    nums = [n for _, n in pairs]
    recipes = extract(nums)
    ents = load()

    days, groc = [], {k: [] for k in ORDER}
    seen = set()
    for (day, num), r in zip(pairs, recipes):
        r['day'] = day
        lvl, hands = timeline(num, ents)
        days.append({'day': day, 'name': r['title'], 'level': lvl, 'time': hands})
        for g in r['grocery']:
            b = bucket(g['store'])
            key = (b, g['item'].lower())
            if key in seen: continue
            seen.add(key)
            groc[b].append(g['item'])
    spec = {
        'title': 'Dinner This Week',
        'week': title_week,
        'note': 'Times are hands-on. Anything with a long unattended stretch — a smoker, a slow cooker, a soak — is called out in the recipe itself.',
        'days': days,
        'grocery': {k: v for k, v in groc.items() if v},
        'recipes': recipes,
    }
    json.dump(spec, sys.stdout, indent=1, ensure_ascii=False)

if __name__ == '__main__':
    main()
