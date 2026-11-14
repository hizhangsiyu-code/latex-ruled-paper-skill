#!/usr/bin/env python3
"""Merge section PDFs into one combined PDF, in the order listed.

Usage:
  python3 merge_sections.py <out.pdf> <section1.pdf> <section2.pdf> ...

Each input is one section's finished PDF. The combined file keeps
every page as-is (no page numbers are added, the dashed line stays).
Verify the result with verify_pdf.py afterwards.
"""
import sys
import fitz

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(2)
    out_path, inputs = sys.argv[1], sys.argv[2:]
    out = fitz.open()
    total = 0
    for path in inputs:
        doc = fitz.open(path)
        out.insert_pdf(doc)
        total += len(doc)
        print(f"{path}: {len(doc)} pages")
    out.save(out_path)
    print(f"Combined: {total} pages -> {out_path}")
