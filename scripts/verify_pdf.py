#!/usr/bin/env python3
"""Verify a typeset ruled-paper PDF before delivery.

Checks every page for:
  - the dashed correction-zone line at x=154mm on every page
  - no text crossing x=153.3mm (the dashed line is at 154mm)
  - no page numbers (a lone digit near the bottom of a page)
  - baseline deviation from the 8mm grid (first baseline 19mm from
    the top of the page); lines more than 0.6mm off are listed

Lines containing \\tfrac, superscripts or subscripts, and \\small
figure captions are expected to read up to about 1.7mm off; treat
those as measurement artefacts, not drift, unless a line with at
least 10 Chinese characters is more than 1.6mm off.

Usage:
  python3 verify_pdf.py <pdf> [--dash 154] [--pitch 8] [--first 19]

Requires: PyMuPDF (pip install PyMuPDF).
"""
import sys
import fitz

MM = 72 / 25.4


def check(path, dash_x=154.0, pitch=8.0, first=19.0):
    doc = fitz.open(path)
    bad_dash = []
    maxx = 0.0
    pgnums = []
    off = []
    for pno in range(len(doc)):
        page = doc[pno]
        if not any(abs(dr["rect"].x0 - dash_x * MM) < 2 for dr in page.get_drawings()):
            bad_dash.append(pno + 1)
        for block in page.get_text("dict")["blocks"]:
            if block["type"] != 0:
                continue
            for line in block["lines"]:
                text = "".join(s["text"] for s in line["spans"])
                y0 = line["spans"][0]["origin"][1]
                if y0 > page.rect.height - 20:
                    continue
                k = round((y0 - first * MM) / (pitch * MM))
                dev = (y0 - (first + pitch * k) * MM) / MM
                if abs(dev) > 0.6:
                    off.append((pno + 1, round(dev, 2), text[:40]))
                x1 = max(s["bbox"][2] for s in line["spans"])
                maxx = max(maxx, x1)
                if text.strip().isdigit() and y0 > page.rect.height - 30:
                    pgnums.append((pno + 1, text.strip()))
    print(f"{path}: {len(doc)} pages")
    print(f"  pages missing dashed line at x={dash_x}mm: {bad_dash or 'none'}")
    print(f"  furthest text from the left edge: {maxx / MM:.1f}mm (limit 153.3mm)")
    print(f"  page numbers found: {pgnums or 'none'}")
    print(f"  lines more than 0.6mm off the grid: {len(off)}")
    for pno, dev, text in off[:20]:
        print(f"    p{pno} {dev:+.2f}mm  {text}")
    ok = not bad_dash and maxx / MM <= 153.3 and not pgnums
    print("  RESULT:", "PASS" if ok else "CHECK ABOVE")
    return ok


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(0 if check(sys.argv[1]) else 1)
