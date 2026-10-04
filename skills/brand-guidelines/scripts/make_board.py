#!/usr/bin/env python3
"""Assemble finished brand assets into presentation boards and a multi-page PDF brand book.

  # one board per section, auto grid, with a caption under each image
  python make_board.py --title "MIKAN TEA 品牌手册" --section "01 IP 形象" brand/out/ip-*.png \
      --section "02 Logo" brand/out/logo-*.png --out brand/handbook.pdf

  # single contact sheet image
  python make_board.py --section "全部物料" brand/out/*.png --out brand/overview.png

Captions use the file name (dashes -> spaces). Pass --font /path/to/NotoSansSC.otf for Chinese titles
(the script tries common Noto/WenQuanYi/PingFang locations automatically). Needs Pillow.
"""
import argparse, glob, math, os, sys
from PIL import Image, ImageDraw, ImageFont

FONT_GUESSES = [
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
    "/usr/share/fonts/noto-cjk/NotoSansCJK-Regular.ttc",
    "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc",
    "/System/Library/Fonts/PingFang.ttc",
    "C:/Windows/Fonts/msyh.ttc",
]


def font(path, size):
    for p in ([path] if path else []) + FONT_GUESSES:
        if p and os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def board(title, section, files, fpath, W=2480, H=1754, bg=(250, 247, 242)):
    page = Image.new("RGB", (W, H), bg)
    d = ImageDraw.Draw(page)
    m = 110
    d.text((m, 70), title, fill=(120, 110, 100), font=font(fpath, 34))
    d.text((m, 120), section, fill=(40, 32, 26), font=font(fpath, 72))
    top = 260
    n = len(files)
    cols = min(n, 4) if n != 4 else 2
    rows = math.ceil(n / cols)
    cw, ch = (W - 2 * m) / cols, (H - top - m) / rows
    cap = font(fpath, 28)
    for i, f in enumerate(files):
        im = Image.open(f).convert("RGB")
        im.thumbnail((int(cw - 40), int(ch - 80)))
        x = int(m + (i % cols) * cw + (cw - im.width) / 2)
        y = int(top + (i // cols) * ch)
        page.paste(im, (x, y))
        name = os.path.splitext(os.path.basename(f))[0].replace("-", " ")
        d.text((x, y + im.height + 14), name, fill=(110, 100, 92), font=cap)
    return page


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--title", default="Brand Kit")
    ap.add_argument("--font")
    ap.add_argument("--out", required=True, help=".pdf for a multi-page book, .png/.jpg for one board")
    ap.add_argument("--section", nargs="+", action="append", metavar=("NAME", "FILES"),
                    help='--section "01 Logo" a.png b.png ...  (repeatable; globs ok)')
    a = ap.parse_args()
    if not a.section:
        ap.error("at least one --section")
    pages = []
    for sec in a.section:
        name, pats = sec[0], sec[1:]
        files = sorted({f for p in pats for f in (glob.glob(p) or [p]) if os.path.isfile(f)})
        if not files:
            print(f"skip empty section: {name}", file=sys.stderr)
            continue
        for i in range(0, len(files), 8):  # max 8 per page
            pages.append(board(a.title, name, files[i:i + 8], a.font))
    if not pages:
        sys.exit("no images found")
    os.makedirs(os.path.dirname(a.out) or ".", exist_ok=True)
    if a.out.lower().endswith(".pdf"):
        pages[0].save(a.out, save_all=True, append_images=pages[1:], resolution=200)
    else:
        pages[0].save(a.out)
    print(f"{a.out}  ({len(pages)} page{'s' if len(pages) > 1 else ''})")


if __name__ == "__main__":
    main()
