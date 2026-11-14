#!/usr/bin/env python3
"""Crop a figure from a 300 DPI render of a source page.

Render the source page first (PyMuPDF at 300 DPI), then crop a
rectangle given in pixels and save it. View the crop and adjust the
box until it holds exactly the figure: no stray text from a
neighbouring problem, no cut-off digits, no caption left in the crop
(the caption is added in LaTeX).

Usage:
  python3 crop_figure.py <render.png> <x0> <y0> <x1> <y1> <out.png>

Coordinates are pixels in the 300 DPI render. A 204x291mm page at
300 DPI is about 2410x3437 pixels; a book page of the same size is
similar. Start wide, view the crop, then tighten.
"""
import sys
from PIL import Image

if __name__ == "__main__":
    if len(sys.argv) != 7:
        print(__doc__)
        sys.exit(2)
    src, x0, y0, x1, y1, out = sys.argv[1], *map(int, sys.argv[2:6]), sys.argv[6]
    im = Image.open(src)
    crop = im.crop((x0, y0, x1, y1))
    crop.save(out)
    print(f"{out}: {crop.size[0]}x{crop.size[1]}px, "
          f"{crop.size[0] / 300 * 25.4:.0f}mm x {crop.size[1] / 300 * 25.4:.0f}mm at 300 DPI")
