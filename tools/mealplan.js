// Weekly meal plan -> Word. Big fonts, readable across the kitchen.
// Usage: node tools/mealplan.js week.json out.docx
const fs = require('fs');
const { Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType, PageBreak,
        Table, TableRow, TableCell, WidthType, ShadingType, BorderStyle, PageOrientation } = require('docx');

const spec = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const OUT  = process.argv[3] || 'meal-plan.docx';

// ---- type scale (half-points: 32 = 16pt) -------------------------
// half-points: 36 = 18pt. Sized to be read standing back from the counter.
const T = { title: 72, sub: 32, day: 30, recipe: 56, h2: 40, body: 36, step: 38, detail: 34, meta: 26, cell: 30 };
const INK = '1A1A1A', MUTED = '555555', RULE = 'B08968', ACCENT = '7B3F00';

const P = (text, o = {}) => new Paragraph({
  alignment: o.align, spacing: { before: o.before ?? 0, after: o.after ?? 120, line: o.line ?? 300 },
  border: o.rule ? { bottom: { style: BorderStyle.SINGLE, size: 12, color: RULE, space: 6 } } : undefined,
  indent: o.indent,
  children: [new TextRun({ text, bold: o.bold, italics: o.italics, size: o.size ?? T.body,
                           color: o.color ?? INK, font: o.font ?? 'Calibri' })],
});
const cell = (text, o = {}) => new TableCell({
  width: { size: o.w, type: WidthType.DXA },
  shading: o.shade ? { type: ShadingType.CLEAR, fill: o.shade, color: 'auto' } : undefined,
  margins: { top: 90, bottom: 90, left: 130, right: 130 },
  children: [P(text, { size: o.size ?? T.cell, bold: o.bold, after: 0, line: 260, color: o.color })],
});

const kids = [];
const dif = { '🟢 Easy': 'Easy', '🟡 Medium': 'Moderate', '🔴 Hard': 'Hard', '⚫ Expert': 'Expert' };

// ---- cover -------------------------------------------------------
kids.push(P(spec.title || 'Dinner This Week', { size: T.title, bold: true, align: AlignmentType.CENTER, after: 60 }));
kids.push(P(spec.week || '', { size: T.sub, italics: true, align: AlignmentType.CENTER, color: MUTED, after: 300, rule: true }));

const W = [2100, 4700, 1500, 1500];
kids.push(new Table({
  columnWidths: W, width: { size: 9800, type: WidthType.DXA },
  rows: [new TableRow({ tableHeader: true, children: [
      cell('Day', { w: W[0], bold: true, shade: 'F2E8DC' }), cell('What we’re making', { w: W[1], bold: true, shade: 'F2E8DC' }),
      cell('Level', { w: W[2], bold: true, shade: 'F2E8DC' }), cell('Hands-on', { w: W[3], bold: true, shade: 'F2E8DC' })] }),
    ...spec.days.map(d => new TableRow({ children: [
      cell(d.day, { w: W[0], bold: true }), cell(d.name, { w: W[1] }),
      cell(d.level || '', { w: W[2] }), cell(d.time || '', { w: W[3] })] }))],
}));
kids.push(P('', { after: 260 }));
if (spec.note) kids.push(P(spec.note, { italics: true, size: T.meta, color: MUTED }));

// ---- grocery list ------------------------------------------------
kids.push(new Paragraph({ children: [new PageBreak()] }));
kids.push(P('Grocery List', { size: T.title, bold: true, after: 60 }));
kids.push(P('Everything for the week, sorted by where you buy it.', { size: T.meta, italics: true, color: MUTED, after: 240, rule: true }));

for (const [store, items] of Object.entries(spec.grocery)) {
  if (!items.length) continue;
  kids.push(P(store, { size: T.h2, bold: true, color: ACCENT, before: 240, after: 100 }));
  for (const it of items) kids.push(P('❑  ' + it, { size: T.body, after: 70, line: 290, indent: { left: 200 } }));
}

// ---- recipes -----------------------------------------------------
for (const r of spec.recipes) {
  kids.push(new Paragraph({ children: [new PageBreak()] }));
  if (r.day) kids.push(P(r.day.toUpperCase(), { size: T.meta, bold: true, color: ACCENT, after: 40 }));
  kids.push(P(r.title, { size: T.recipe, bold: true, after: 60 }));
  const meta = [`§${r.num}`, dif[r.badge?.level] || '', r.yield].filter(Boolean).join('  ·  ');
  kids.push(P(meta, { size: T.meta, italics: true, color: MUTED, after: 40 }));
  if (r.badge?.line) kids.push(P(r.badge.line.replace(/^\S+\s\S+\s·\s/, ''), { size: T.meta, color: MUTED, after: 200, rule: true }));

  kids.push(P('Ingredients', { size: T.h2, bold: true, color: ACCENT, before: 200, after: 110 }));
  for (const i of r.ingredients) kids.push(P('❑  ' + i, { size: T.body, after: 70, line: 290, indent: { left: 200 } }));

  kids.push(P('Instructions', { size: T.h2, bold: true, color: ACCENT, before: 280, after: 130 }));
  for (const s of r.steps) {
    kids.push(P(`${s.n}.  ${s.head}`, { size: T.step, bold: true, before: 180, after: 60, line: 300 }));
    if (s.detail) kids.push(P(s.detail, { size: T.detail, after: 60, line: 330, indent: { left: 340 } }));
  }
}

const doc = new Document({
  creator: "Cody's Cookbook", title: spec.title || 'Meal Plan',
  styles: { default: { document: { run: { font: 'Calibri', size: T.body, color: INK } } } },
  sections: [{
    properties: { page: { size: { width: 12240, height: 15840, orientation: PageOrientation.PORTRAIT },
                          margin: { top: 900, right: 900, bottom: 900, left: 900 } } },
    children: kids,
  }],
});
Packer.toBuffer(doc).then(b => { fs.writeFileSync(OUT, b); console.log('wrote ' + OUT + ' (' + b.length + ' bytes)'); });
