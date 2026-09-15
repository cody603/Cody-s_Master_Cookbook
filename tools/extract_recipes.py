#!/usr/bin/env python3
"""Pull full recipes out of codys-cookbook.md into JSON for the meal-plan generator.

Usage:  python3 tools/extract_recipes.py 7.15 7.16 5.13 ...   > week.json
"""
import re, sys, json, os

BOOK = os.path.join(os.path.dirname(__file__), '..', 'codys-cookbook.md')

def load():
    lines = open(BOOK, encoding='utf-8').read().split('\n')
    ents, cur = [], None
    for i, l in enumerate(lines):
        if l.startswith('### '):
            if cur: cur['end'] = i; ents.append(cur)
            cur = {'title': l[4:].strip(), 'start': i}
        elif l.startswith('## ') and cur:
            cur['end'] = i; ents.append(cur); cur = None
    if cur: cur['end'] = len(lines); ents.append(cur)
    for e in ents:
        e['body'] = '\n'.join(lines[e['start']:e['end']])
    return ents

def section(body, name):
    m = re.search(r'^#### [A-Z]?\.? ?' + name + r'.*?$(.*?)(?=^#### |\Z)', body, re.M | re.S)
    return m.group(1).strip() if m else ''

def bullets(text):
    out = []
    for l in text.split('\n'):
        l = l.strip()
        if l.startswith('- '):
            out.append(clean(l[2:]))
    return out

def steps(text):
    """Numbered bold steps plus the detail paragraph under each."""
    out, cur = [], None
    for l in text.split('\n'):
        s = l.strip()
        m = re.match(r'^\*\*(\d+)\.\s*(.+?)\*\*\s*$', s)
        if m:
            if cur: out.append(cur)
            cur = {'n': int(m.group(1)), 'head': clean(m.group(2)), 'detail': []}
        elif cur is not None and s and not s.startswith('#') and not s.startswith('|'):
            if s.startswith('!['): continue
            cur['detail'].append(clean(s))
    if cur: out.append(cur)
    for s in out:
        s['detail'] = ' '.join(s['detail']).strip()
    return out

def clean(s):
    s = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', s)
    s = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', s)      # links -> text
    s = re.sub(r'<!--.*?-->', '', s)
    s = s.replace('**', '').replace('*', '').replace('`', '')
    s = re.sub(r'\s+', ' ', s)
    return s.strip()

STORE = {'🛒': 'General grocery', '☯️': 'Hong Kong / Chinese market', '🏪': 'Specific store'}

def grocery(text):
    """Split the grocery list into (store, item) pairs, keeping any (Store Name) hint."""
    out, cur = [], 'General grocery'
    for l in text.split('\n'):
        s = l.strip()
        h = re.match(r'^\*\*(.+?)\*\*\s*$', s)
        if h:
            lab = clean(h.group(1))
            for icon, name in STORE.items():
                if icon in lab:
                    cur = lab.replace(icon, '').strip(' —-') or name
            continue
        if s.startswith('- '):
            item = s[2:]
            store = cur
            for icon, name in STORE.items():
                if item.strip().startswith(icon):
                    item = item.strip()[len(icon):]
                    break
            out.append({'store': store, 'item': clean(item)})
    return out

def badge(body):
    m = re.search(r'^\*\*(?:🥑 Keto\*\* · \*\*)?(🟢 Easy|🟡 Medium|🔴 Hard)\*\*(.*)$', body, re.M)
    if not m: return {'level': '', 'line': ''}
    return {'level': m.group(1), 'line': clean(m.group(0))}

def yield_(body):
    m = re.search(r'^\*\*Yield:\*\*\s*(.+)$', body, re.M)
    return clean(m.group(1)) if m else ''

def main(nums):
    ents = load()
    idx = {}
    for e in ents:
        m = re.match(r'^(T\d+|\d+\.\d+)[.\s]', e['title'])
        if m: idx[m.group(1)] = e
    out = []
    for n in nums:
        e = idx.get(n)
        if not e:
            print(f'!! no recipe {n}', file=sys.stderr); continue
        b = e['body']
        out.append({
            'num': n,
            'title': re.sub(r'^(T?\d+\.?\d*)\.?\s+', '', e['title']),
            'yield': yield_(b),
            'badge': badge(b),
            'ingredients': bullets(section(b, 'Ingredients')),
            'steps': steps(section(b, 'Cooking Instructions')),
            'grocery': grocery(section(b, 'Grocery Shopping List')),
        })
    return out

if __name__ == '__main__':
    json.dump(main(sys.argv[1:]), sys.stdout, indent=1, ensure_ascii=False)
