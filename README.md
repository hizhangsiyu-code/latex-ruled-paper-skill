# LaTeX Ruled-Paper Typesetting / 横线纸排版

![Showcase](showcase.png)

[English](#english) | [中文](#中文)

---

## English

Turn a scanned maths workbook into clean, printable PDFs on the child's own ruled paper, with a correction zone, room to work, and every figure taken from the original.

### About

This skill was created to solve a very concrete problem: a parent has a maths workbook as a scan, and a child who does their homework on ruled loose-leaf paper. Printing the scan wastes the paper, and retyping the whole book by hand takes forever. OCR looks like a shortcut until it meets a fraction or a diagram, and then it invents numbers.

**LaTeX Ruled-Paper Typesetting** bridges that gap by:

- Measuring the actual paper first, then setting the PDF page to exactly that size, so the printed lines land on the ruled lines instead of drifting down the page
- Typesetting each section from a 300 DPI render of the scan, checking every number, formula and option against the original
- Taking every figure from the original at native resolution and enlarging it, never redrawing it
- Leaving a correction zone on the right and answer space in whole lines, so the child can work on the page and correct on the side
- Verifying every finished PDF (dashed line, no text over it, no page numbers, baselines on the grid) before it is delivered

Perfect for:

- **Parents** turning a scanned workbook into printable homework pages
- **Teachers** preparing a class set from a textbook scan
- **Tutors** who need clean, editable `.tex` sources to revise from
- **Anyone** whose paper is not A4 and whose printer must not scale the page

The skill was built by typesetting two real books end to end, and every number in it comes from those two books.

### Real results

- **A 397-type maths book** (types, knowledge boxes, worked examples, variants, a separate answer book): 167 pages, 63 types in the first three chapters, delivered as a questions-only PDF, an answers-only PDF and a combined PDF, all on 204 by 291mm ruled paper.
- **A Grade 6 workbook** (23 sections, 17 weeks plus unit exercises, mid-term and final): 129 pages, 618 problems, delivered as one combined questions-only PDF, because the scan had no answers in it.

Both books were checked page by page: baselines on the grid, the dashed line on every page, no text crossing it, no page numbers, figures intact.

### Features

- **Paper-first layout**: the PDF page is the paper size, no bleed, so a home printer at 100 percent actual size does not shrink the lines
- **Ruled grid**: an 8mm baseline grid with the first baseline 19mm from the top, matching the paper
- **Correction zone**: a 50mm zone on the right, separated by a thin dashed line at x=154mm on every page
- **Answer space**: whole multiples of the line spacing only, so the baselines after it stay on the ruled lines (1 line after a choice or fill-in problem, 2 lines after a worked problem)
- **Faithful figures**: every diagram cropped from the source at 300 DPI and enlarged, never redrawn, with a centred caption
- **Correct symbols**: problem numbers with `\textcircled`, inline fractions with `\tfrac`, because Unicode circled numbers render blank in the CJK font and `\dfrac` breaks the grid
- **Verification script**: checks the dashed line, the text clearance, page numbers and baselines on every finished PDF
- **Editable sources**: a `.tex` file for every PDF, so a revision starts from the source

### Installation

#### Method 1: Automatic Installation (Recommended)

```bash
npx skills add https://github.com/hizhangsiyu-code/latex-ruled-paper-skill.git
```

This will automatically install the skill to the correct directory.

#### Method 2: Git Clone

```bash
git clone https://github.com/hizhangsiyu-code/latex-ruled-paper-skill.git ~/.claude/skills/latex-ruled-paper-typesetting
```

#### Method 3: Manual Installation

1. Download this repository
2. Copy the `latex-ruled-paper-skill` folder to your skills directory:
   - **Muse**: `~/workspace/custom-skills/`
   - **Claude Code**: `~/.claude/skills/`
3. Ensure the folder contains `SKILL.md` and `README.md`

#### Post-Installation Setup

Install the required tools:

```bash
# TeX Live with XeLaTeX and Chinese support (Debian/Ubuntu)
sudo apt-get install texlive-xetex texlive-lang-chinese fonts-noto-cjk

# Python helpers
pip install PyMuPDF Pillow
```

Confirm the toolchain before you compile:

```bash
which xelatex
```

Restart your agent and verify by asking it to typeset a sample section.

### Usage

#### Basic Workflow

1. **Hand over the scan**:
   ```
   Typeset this maths workbook onto my ruled paper.
   ```
   Attach the PDF, or give a link to it.

2. **Confirm the paper** (the agent will ask):
   - The actual paper size, measured from a photo or by hand
   - The line spacing and the distance from the top of the page to the first line
   - Whether there is an answer book, and whether you want answers included

3. **Review one sample section**: the agent typesets one section first, and you check the layout and the answer space before the rest is batched.

4. **Batch the rest**: the remaining sections are typeset the same way, each verified, and merged into one combined PDF.

#### Example Prompts

```
Typeset this workbook on my 204x291mm ruled paper, questions only.

Split it by week, leave 1 line after choice and fill-in problems
and 2 lines after worked problems.

Make a combined PDF of all 23 sections, no page numbers.
```

### Workflow Phases

**Phase 1: Measure the paper**
Measure the paper size, the line spacing and the first baseline from a photo or by hand, and set the PDF page to exactly that size with no bleed.

**Phase 2: Read the source**
Find how the book is organised (by type, by week, by unit), check whether it has answers, and render the source pages at 300 DPI for transcription.

**Phase 3: Sample one section**
Typeset one section from the template, compile it twice, verify it and show it to the user, and only batch the rest once the layout and the answer space are approved.

**Phase 4: Typeset every section**
Transcribe each section from its 300 DPI renders, crop each figure from the original, keep an editable `.tex` source, and record anything doubtful in the section notes instead of changing it silently.

**Phase 5: Verify and deliver**
Run the verification script on every PDF, read the rendered pages by eye, merge the sections in order, and deliver the combined PDF with the per-section PDFs beside it.

### Format Principles

1. **Measure the paper, never assume A4** - the page is the paper, and a change of paper is a fresh setup.
2. **No bleed for home printing** - bleed makes the printer scale the page down and the lines drift.
3. **Baselines on the ruled lines** - every baseline lands on an 8mm grid, and answer space is always a whole multiple of the grid.
4. **A correction zone, not a margin** - the right 50mm stays empty behind a dashed line, with room for punctuation that hangs past the text edge.
5. **Figures from the original, never redrawn** - crop at 300 DPI, enlarge only, check every crop by eye.
6. **Check the answers against the questions** - when a question and its answer disagree, fix the side that is wrong; when there is no answer book, do not invent answers.
7. **Verify the rendered page, not the source** - open the exact PDF the user will see, and say plainly what remains unchecked.

### File Structure

```
latex-ruled-paper-skill/
├── SKILL.md                    # Skill definition and workflow
├── README.md                   # This file
├── LICENSE                     # MIT License
├── skill.yaml                  # Skill metadata
├── requirements.txt            # Python dependencies
├── templates/
│   └── ruled-paper-template.tex # Copy-pasteable LaTeX template
├── scripts/
│   ├── verify_pdf.py           # Check a finished PDF
│   ├── crop_figure.py          # Crop a figure from a 300 DPI render
│   └── merge_sections.py       # Merge section PDFs in order
├── references/
│   └── format-decisions.md     # Settled numbers and the lessons behind them
└── assets/
    └── showcase.png            # Before and after: scan vs typeset page
```

### Requirements

- TeX Live with `xelatex` and Chinese support (`texlive-xetex`, `texlive-lang-chinese`)
- Noto Serif CJK SC font (`fonts-noto-cjk`)
- Python 3 with `PyMuPDF` and `Pillow` (for the helper scripts)

### License

MIT License - feel free to use for personal or commercial projects.

### Contributing

Contributions welcome! Please feel free to submit issues or pull requests. If you typeset a book with this skill, a note about the paper size and the page count helps the next person calibrate it.

---

## 中文

把一本扫描版数学练习册，排成孩子自己那张横线纸上能直接打印、直接做的 PDF，带订正区、留好答题空、图全部取自原书。

### 关于本项目

这个技能源于一个很具体的需求：手里有一本数学练习册的扫描件，孩子做作业用的是横线活页纸。直接打印扫描件浪费纸，整本手打重排又太费事。OCR 看着像捷径，一碰到分数和图形就开始编数字。

**横线纸排版** 通过以下方式解决这个问题：

- 先量纸，再定版：PDF 页就是纸的实际尺寸，打印出来的行正好压在横线上，越往下也不漂
- 按 300 DPI 的渲染图逐字录入，每个数字、公式、选项都对照原书核对过
- 每张图都从原书按原生分辨率抠出来放大，绝不重画
- 右边留 50mm 订正区，答题空按整行留，孩子能在页上做题、在边上订正
- 每份 PDF 交付前都校验过（虚线、越线、页码、基线），再交到你手里

适用场景：

- **家长** 把扫描版练习册变成能打印的作业页
- **老师** 按课本扫描件备一整套班级练习
- **家教** 需要能改的 `.tex` 源文件，随时修订
- **任何人** 纸不是 A4、打印机又不能缩放页面的情况

这个技能是靠实打实排完两本书做出来的，里面的每个数都来自那两本书。

### 实际成果

- **一本 397 种题型的数学书**（题型、知识框、例题、变式，另有答案册）：167 页，前三章 63 型，交付了题目版、答案版、题目加答案合订版三个版本，全部是 204×291mm 横线纸。
- **一本六年级练习册**（23 节，17 周加单元练习、期中、期末）：129 页、618 道题，交付了一个题目版合订 PDF，因为那份扫描件里本来就没有答案。

两本书都逐页检查过：基线压线、虚线每页都在、文字不越线、无页码、图完整。

### 功能特性

- **先量纸再定版**：PDF 页就是纸的尺寸，无出血，家用打印机按 100% 实际大小打印，行距不会被压小
- **横线网格**：8mm 基线网格，首行基线距页顶 19mm，跟纸上的横线对得上
- **订正区**：右侧 50mm 订正区，每页一条细虚线隔开，虚线在距左 154mm 处
- **答题空间**：只按整行留空，留完基线还压线（选择题、填空题后留 1 行，解答题后留 2 行）
- **图取自原书**：每张图从 300 DPI 渲染图上裁切放大，绝不重画，图下有居中图注
- **符号不出错**：题号用 `\textcircled`，行内分数用 `\tfrac`，因为 Unicode 圈号在中文字体下渲染为空白，`\dfrac` 会撑破网格
- **校验脚本**：每份成品 PDF 都跑一遍校验（虚线、越线、页码、基线）
- **源文件可改**：每份 PDF 都有对应的 `.tex` 源文件，改起来从源文件改

### 安装方式

#### 方法 1：自动安装（推荐）

```bash
npx skills add https://github.com/hizhangsiyu-code/latex-ruled-paper-skill.git
```

这将自动把技能安装到正确的目录。

#### 方法 2：Git 克隆

```bash
git clone https://github.com/hizhangsiyu-code/latex-ruled-paper-skill.git ~/.claude/skills/latex-ruled-paper-typesetting
```

#### 方法 3：手动安装

1. 下载本仓库
2. 把 `latex-ruled-paper-skill` 文件夹复制到技能目录：
   - **Muse**：`~/workspace/custom-skills/`
   - **Claude Code**：`~/.claude/skills/`
3. 确保文件夹里有 `SKILL.md` 和 `README.md`

#### 安装后配置

安装所需工具：

```bash
# TeX Live（含 XeLaTeX 与中文支持，Debian/Ubuntu）
sudo apt-get install texlive-xetex texlive-lang-chinese fonts-noto-cjk

# Python 辅助脚本
pip install PyMuPDF Pillow
```

编译前先确认工具链：

```bash
which xelatex
```

重启你的 agent，找它排一节样张验证安装成功。

### 使用方法

#### 基本工作流

1. **交出扫描件**：
   ```
   把这本数学练习册排到我的横线纸上。
   ```
   附上 PDF，或者给一个链接。

2. **确认纸张**（agent 会问你）：
   - 纸的实际尺寸，拍照量或者上手量
   - 横线间距、第一条横线距页顶多远
   - 有没有答案册，要不要把答案排进去

3. **先看一节样张**：agent 先排一节给你看，版式和留白都合意了，再批量排剩下的。

4. **批量排完**：剩下的节按同一套做法排，每节都校验过，最后合成一个合订 PDF。

#### 示例指令

```
把这本练习册排到 204x291mm 横线纸上，只要题目版。

按周分节，选择题、填空题后留 1 行，解答题后留 2 行。

23 节合成一个合订 PDF，不要页码。
```

### 工作流程阶段

**阶段 1：量纸**
拍照或上手量纸的尺寸、横线间距、首行位置，PDF 页就按纸的实际尺寸定，无出血。

**阶段 2：读源文件**
看清书的结构（按题型、按周、按单元），确认有没有答案，把源页按 300 DPI 渲染出来备着录入。

**阶段 3：先做一节样张**
按模板排一节，编两次、校验过、拿给用户看，版式和留白都点了头再批量。

**阶段 4：逐节排版**
每节按 300 DPI 渲染图逐字录入，图从原书裁切，留一份能改的 `.tex` 源文件，拿不准的地方记进本节 NOTES 里，不悄悄改掉。

**阶段 5：校验交付**
每份 PDF 跑校验脚本，渲染页肉眼看一遍，按顺序合成合订版，连同各节单节 PDF 一起交付。

### 版式原则

1. **量纸，不假设 A4** —— 页就是纸，换纸就是重新定版。
2. **家用打印不要出血** —— 出血逼打印机整页缩印，行距被压小，越往下越不压线。
3. **基线压线** —— 每行基线都落在 8mm 网格上，答题空只按整行留。
4. **订正区不是边距** —— 右侧 50mm 空出来留给订正，虚线隔开，还给行末悬挂的标点留了余地。
5. **图取自原书，绝不重画** —— 300 DPI 裁切、只放大，每张裁切都肉眼检查过。
6. **拿答案核题目** —— 题目和答案对不上的，改错的那一边；没有答案册的，不编答案。
7. **验渲染页，不验源文件** —— 打开用户将要看到的那份 PDF 本身再说通过，没打开的就直说没验过。

### 文件结构

```
latex-ruled-paper-skill/
├── SKILL.md                    # 技能定义与工作流程
├── README.md                   # 本文件
├── LICENSE                     # MIT 开源协议
├── skill.yaml                  # 技能元数据
├── requirements.txt            # Python 依赖
├── templates/
│   └── ruled-paper-template.tex # 能直接用的 LaTeX 模板
├── scripts/
│   ├── verify_pdf.py           # 校验一份成品 PDF
│   ├── crop_figure.py          # 从 300 DPI 渲染图上裁图
│   └── merge_sections.py       # 按顺序合成各节 PDF
├── references/
│   └── format-decisions.md     # 定下来的那些数和踩过的坑
└── assets/
    └── showcase.png            # 前后对比：扫描件 vs 排版后
```

### 系统要求

- TeX Live（含 `xelatex` 与中文支持，`texlive-xetex`、`texlive-lang-chinese`）
- Noto Serif CJK SC 字体（`fonts-noto-cjk`）
- Python 3 与 `PyMuPDF`、`Pillow`（辅助脚本用）

### 开源协议

MIT License - 可自由用于个人或商业项目。

### 贡献

欢迎贡献！请随时提交 issue 或 pull request。如果你用这个技能排过一本书，留个言说一下纸的尺寸和页数，能帮下一个人更快定版。
