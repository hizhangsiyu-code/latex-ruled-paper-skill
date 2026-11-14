# Typeset a Scanned Maths Workbook on Ruled Paper

## Measure the paper first

- Ask the user for the actual paper size and measure it from a photo or a physical measurement before you set any page size, and never assume A4.

- Set the PDF page to the exact paper size with no bleed, because bleed makes a home printer scale the whole page down and the text drifts off the ruled lines further down the page.

- Take the line spacing, the first baseline and the margins from that paper, and keep every page in the same format once it is settled.

- Read `references/format-decisions.md` for the numbers settled on 204 by 291mm paper, and re-measure them when the paper changes.

## Read the source book

- Find how the book is organised before you typeset anything, whether it is by problem type, by week or lesson, or by unit, and split the output the same way the book does.

- Check whether the book has answers, and whether they sit in a separate answer book or in an appendix at the back of the same file.

- Render the source pages at 300 DPI and transcribe from those renders, because a scanned book has no text layer and OCR text on maths is unreliable.

- Check every label, number, formula and option against the render, and never invent a value from garbled text.

- When the book has answers, use them to check the questions, and fix the side that is wrong when a question and its answer disagree.

- When there is no answer book, deliver a questions-only version and record anything that looks wrong in the section notes without changing it.

## Build one section as a sample

- Copy `templates/ruled-paper-template.tex` for the first section and fill in its title and problems, then compile it twice with xelatex and check it before you scale up.

- Show the sample to the user and wait for their verdict on the layout and the answer space before you batch the rest.

- Keep the template preamble and its `\gridblock` macro unchanged across sections, and only change the title, the problems and the figures.

## Typeset each section

- Keep an editable .tex source for every PDF, so later revisions start from the source rather than from a rendered copy.

- Put each section in its own folder with a PDF, a same-named .tex, a same-named notes file and a figures folder, and name them the way the template does.

- Use `\textcircled{N}` for every problem number, because Unicode circled numbers render as blank in Noto Serif CJK SC.

- Use `\tfrac` for every inline fraction, because `\dfrac` stretches the line and breaks the grid.

- Keep the layout compact with no blank line after a heading and no empty line between paragraphs.

- Give answer space only in whole multiples of the 8mm line spacing, so the baselines after it still fall on ruled lines, and never compress it to fit a section onto one page.

- Leave 1 line after a choice or fill-in problem and 2 lines after a worked problem, or follow the per-type rule in `references/format-decisions.md` when the book is organised by problem type.

- Drop the cover, copyright page, author bio and preface, and start directly from the first chapter or lesson in the contents.

- Use no page numbers anywhere, unless the user asks for them, and then apply the decision to every section at once.

## Handle figures

- Crop each figure from a 300 DPI render of the source page with `scripts/crop_figure.py`, or take the native image object when the PDF has one, and enlarge it as needed.

- Never redraw a figure, even when it looks simple.

- View every crop before you use it, and reject any crop with stray text from a neighbouring problem, cut-off digits or a caption left inside it.

- Put each figure inside the `\gridblock` macro so the text after it returns to the grid, and add a centred caption naming it.

- Keep every figure clear of the correction zone line, and re-measure the macro offset for each new figure size instead of copying a value from another block.

## Compile and verify

- Confirm `which xelatex` before you compile on a fresh machine, because a system reinstall can leave TeX Live absent.

- Compile twice with xelatex, because the TikZ dashed line needs two passes, and check for "Output written" plus the PDF timestamp so you do not mistake a stale PDF for a fresh one.

- Run `scripts/verify_pdf.py` on every finished PDF, and read the rendered pages by eye at the size the user will print them.

- Check that the dashed line is on every page, that no text crosses it, that there are no page numbers, and that the problem numbers run continuously from 1.

- Treat lines with `\tfrac`, superscripts or subscripts and `\small` captions as measurement artefacts when they read up to about 1.7mm off the grid, and investigate any other line more than 0.6mm off.

- Measure the clearance from the bottom of each box, table and figure to the next line of text, and require a positive gap on every page.

- Count every non-ASCII marker in the written .tex file and compare the count with the source, because writing the file can drop them silently, and repair a missing marker by its unique following anchor, then recompile and count again.

- Remove build files such as .aux, .log and texput.log from the delivery folders.

## Combine and deliver

- Merge the finished sections in order with `scripts/merge_sections.py`, then run `scripts/verify_pdf.py` on the combined file as well.

- Deliver the combined PDF and keep each section PDF beside it, so the user can print the whole book or one section at a time.

- Record the page count, the problem count, the figure count and anything that looked wrong in the original book, and tell the user about the doubtful items instead of silently changing them.

- Ask the user to print one sample page at 100 percent actual size before they print the whole book, because a printed page can reveal drift that a screen render hides.
