#!/usr/bin/env python3
"""Slice a generated grid sheet (sticker sheet, expression sheet, 2x2 consistency test, avatar set)
into individual files, trim the background, pad to square and resize to platform sizes.

  # 3x3 sticker sheet -> 9 PNGs at 240x240 (WeChat sticker main image size) + a 120px thumbnail of #1
  python slice_grid.py out/stickers.png --rows 3 --cols 3 --size 240 --thumb 120 --out out/stickers/
  # 2x2 test grid, keep original resolution
  python slice_grid.py out/grid.png --rows 2 --cols 2 --out out/tiles/

--transparent turns the near-uniform background into alpha (good for flat backgrounds, not for photos).
Prints each file with its byte size and warns when a PNG is above --max-kb (default 500).
Needs Pillow.
"""
import argparse, os
from PIL import Image, ImageChops


def bg_colour(im):
    w, h = im.size
    pts = [(2, 2), (w - 3, 2), (2, h - 3), (w - 3, h - 3)]
    px = [im.getpixel(p)[:3] for p in pts]
    return tuple(sum(c[i] for c in px) // 4 for i in range(3))


def trim(im, bg, tol=18):
    diff = ImageChops.difference(im.convert("RGB"), Image.new("RGB", im.size, bg)).convert("L")
    box = diff.point(lambda v: 255 if v > tol else 0).getbbox()
    return im.crop(box) if box else im


def to_alpha(im, bg, tol=22):
    im = im.convert("RGBA")
    data = [(r, g, b, 0) if abs(r - bg[0]) + abs(g - bg[1]) + abs(b - bg[2]) < tol * 3 else (r, g, b, a)
            for r, g, b, a in im.getdata()]
    im.putdata(data)
    return im


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("sheet")
    ap.add_argument("--rows", type=int, required=True)
    ap.add_argument("--cols", type=int, required=True)
    ap.add_argument("--gutter", type=int, default=0, help="px to shave off each tile edge (grid lines)")
    ap.add_argument("--size", type=int, help="square output size, e.g. 240")
    ap.add_argument("--thumb", type=int, help="also save a thumbnail of tile 1 at this size")
    ap.add_argument("--pad", type=float, default=0.06, help="padding ratio around the trimmed subject")
    ap.add_argument("--transparent", action="store_true")
    ap.add_argument("--max-kb", type=int, default=500)
    ap.add_argument("--out", default="out/tiles")
    a = ap.parse_args()

    sheet = Image.open(a.sheet).convert("RGB")
    bg = bg_colour(sheet)
    W, H = sheet.size
    tw, th = W / a.cols, H / a.rows
    os.makedirs(a.out, exist_ok=True)
    n = 0
    for r in range(a.rows):
        for c in range(a.cols):
            n += 1
            box = (int(c * tw) + a.gutter, int(r * th) + a.gutter, int((c + 1) * tw) - a.gutter, int((r + 1) * th) - a.gutter)
            tile = trim(sheet.crop(box), bg)
            side = int(max(tile.size) * (1 + 2 * a.pad))
            canvas = Image.new("RGB", (side, side), bg)
            canvas.paste(tile, ((side - tile.width) // 2, (side - tile.height) // 2))
            out = to_alpha(canvas, bg) if a.transparent else canvas
            if a.size:
                out = out.resize((a.size, a.size), Image.LANCZOS)
            path = os.path.join(a.out, f"{n:02d}.png")
            out.save(path, optimize=True)
            kb = os.path.getsize(path) / 1024
            print(f"{path}  {out.size[0]}x{out.size[1]}  {kb:.0f}KB" + ("  ⚠ over limit" if kb > a.max_kb else ""))
            if a.thumb and n == 1:
                t = out.resize((a.thumb, a.thumb), Image.LANCZOS)
                tp = os.path.join(a.out, f"thumb-{a.thumb}.png")
                t.save(tp, optimize=True)
                print(tp)


if __name__ == "__main__":
    main()
