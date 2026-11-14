# Settled format decisions

These numbers were settled by measuring the user's actual paper and
by two full books (a 397-type maths book and a 23-section Grade 6
workbook). Re-measure them when the paper changes; do not copy them
blindly onto different paper.

## Paper and page

- Paper is 204mm by 291mm (A4 with 3mm trimmed off every side).
The PDF page is exactly the paper size, with no bleed and no crop
marks. Bleed makes a home printer scale the whole page down, which
shrinks the line spacing and makes the text drift off the ruled
lines further down the page.
- Print at 100 percent actual size. Never use fit to page or shrink
to fit.
- Margins: left 35mm, right 54mm, top 11mm, bottom 12mm. Text width
is 115mm, so the right edge of the text is at 150mm from the left
edge of the page.

## Ruled lines

- Line spacing is 8mm, matching the ruled paper. The first text
baseline sits 19mm from the top of the page.
- In LaTeX: `\baselineskip=8mm`, `parskip=0`, `topskip=8mm`,
`parindent=0`, `lineskip=0`, `lineskiplimit=0`.
- Measure the paper from a photo before you set these numbers.
The ruled spacing was 8.0mm and the first line was about 19mm
from the top. If the first line is off, change the top margin.
If the drift grows down the page, change the line spacing.

## Correction zone

- The right 50mm of the page is a correction zone, separated from
the text by a thin dashed black line at x=154mm from the left
edge, running the full height of every page.
- The text right edge (150mm) sits 4mm left of the line on purpose:
a Chinese full stop at the end of a line hangs about 2.6mm past
the text edge, so it reaches about 152.6mm and stays clear of the
line.
- Draw the line with TikZ `remember picture, overlay` and
`\AddToHook{shipout/background}`. Compile twice; a single pass
draws the line off the page. When you move the line, change both
endpoints of the `\draw` or it draws slanted.
- No text or figure may touch or cross x=154mm. The furthest text
measured in production was 153.3mm.

## Page numbers

- None. The whole book uses `\pagestyle{empty}`. If the user
changes their mind, apply the decision to every section at once.

## Answer space

- Answer space is always a whole multiple of the 8mm line spacing,
so the baselines after it still fall on ruled lines. Never
compress it to fit a section onto one page.
- For a workbook of numbered problems: 1 line (8mm) after a choice
or fill-in problem, 2 lines (16mm) after a worked problem.
- For a book organised by problem type with variants: 1 line
between variants, and extra space only after the last variant of
a type: 3 lines for calculation, simplification, evaluation or
equation work, 2 lines for application or proof, 1 line for
choice, true or false or fill-in. Apply the rule once per type,
uniformly; do not multiply it per item.

## Type and symbols

- Problem numbers use `\textcircled{N}`. Unicode circled numbers
(U+2460 and friends) render as blank in Noto Serif CJK SC, so
never type them directly. The same applies to circled numbers
inside the text, such as "as shown in figure 1"; use a small
macro (for example `\qcirc`) that draws the circle.
- Inline fractions use `\tfrac`. `\dfrac` stretches the line and
breaks the grid, and it also breaks brackets and numerators.
- Keep the layout compact: no blank line after a heading, no empty
line between paragraphs, no meaningless vertical skips.

## Figures

- Never redraw a figure. Crop it from the source page at 300 DPI
(or take the native image object when the PDF has one, at about
600 DPI) and enlarge it as needed.
- Check every crop by eye: no stray text from a neighbouring
problem, no cut-off digits, no caption left inside the crop.
Add the caption in LaTeX, centred under the figure, naming it
(for example "Figure 2").
- Put each figure inside the `\gridblock` macro so the text after
it returns to the grid. Re-measure the macro offset for each new
figure size; do not copy a calibration value from another block.
A figure caption in `\small` reads up to about 1.7mm off the
grid; that is a measurement artefact of the smaller font, not
drift.

## Sources and checking

- A scanned book has no text layer, so transcribe from a 300 DPI
render and check every label, number, formula and option against
that render. Never invent a value from garbled OCR text.
- When the book has a separate answer book, use the answers to
check the questions: if a question and its answer disagree, fix
the side that is wrong (a wrong question gets a corrected
question, a wrong answer gets a corrected answer) instead of
copying the error. When there is no answer book, do not invent
answers; deliver a questions-only version and record anything
that looks wrong in the section notes without changing it.
- Keep an editable.tex source for every PDF. Writing a.tex file
can silently drop non-ASCII markers such as, so count them
in the written file and compare the count with the source. Repair
a missing marker by its unique following anchor, recompile, and
count again.
- Compile twice with xelatex and check for "Output written" plus
the PDF timestamp; a stale PDF is easy to mistake for a fresh
one. Confirm `which xelatex` before compiling on a fresh machine,
because a system reinstall can leave TeX Live absent.
- Verify every finished PDF with `scripts/verify_pdf.py` and read
the rendered pages by eye before delivery. Record the label
count, the baseline deviation and the clearance you measured.
