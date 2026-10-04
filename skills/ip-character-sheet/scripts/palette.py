#!/usr/bin/env python3
"""Brand palette helper: extract dominant colours from an image and/or check WCAG contrast.

  # 1) pull 6 dominant colours from a character sheet / logo (ignores near-white background)
  python palette.py extract brand/ref/ip-sheet.png -k 6
  # 2) contrast matrix for a palette (which text colour can sit on which background)
  python palette.py contrast "#F28C28" "#FFE9C7" "#6BAA4B" "#3B2A20" "#FFFFFF"

Needs Pillow (pip install pillow). Output is Markdown so it can be pasted straight into brand.md.
"""
import argparse, sys


def hex2rgb(h):
    h = h.strip().lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def rgb2hex(c):
    return "#{:02X}{:02X}{:02X}".format(*c)


def luminance(c):
    def ch(v):
        v /= 255
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = (ch(v) for v in c)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(a, b):
    la, lb = sorted((luminance(a), luminance(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def extract(path, k, keep_bg):
    from PIL import Image
    im = Image.open(path).convert("RGB")
    im.thumbnail((400, 400))
    q = im.quantize(colors=32, method=Image.Quantize.MEDIANCUT)
    pal = q.getpalette()
    counts = sorted(q.getcolors(), reverse=True)
    rows = []  # [rgb, pixel_count]
    for n, idx in counts:
        c = tuple(pal[idx * 3: idx * 3 + 3])
        if not keep_bg and min(c) > 232:  # skip paper / white background
            continue
        for r in rows:  # merge near-duplicates into the bigger cluster
            if sum(abs(x - y) for x, y in zip(c, r[0])) < 60:
                r[1] += n
                break
        else:
            rows.append([c, n])
    rows.sort(key=lambda r: -r[1])
    rows = rows[:k]
    total = sum(n for _, n in rows)
    print("| HEX | RGB | 占比（不含背景） |\n|---|---|---|")
    for c, n in rows:
        print(f"| `{rgb2hex(c)}` | {c} | {n / total:.0%} |")


def matrix(hexes):
    cols = [hex2rgb(h) for h in hexes]
    print("| 文字 \\ 底色 | " + " | ".join(f"`{h.upper()}`" for h in hexes) + " |")
    print("|---" * (len(hexes) + 1) + "|")
    for h, fg in zip(hexes, cols):
        cells = []
        for bg in cols:
            r = contrast(fg, bg)
            tag = "AAA" if r >= 7 else "AA" if r >= 4.5 else "大字" if r >= 3 else "✗"
            cells.append(f"{r:.1f} {tag}")
        print(f"| `{h.upper()}` | " + " | ".join(cells) + " |")
    print("\nAA ≥ 4.5（正文） · 大字 ≥ 3（≥24px 标题/图标） · ✗ 不要用来放文字")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    e = sub.add_parser("extract")
    e.add_argument("image")
    e.add_argument("-k", type=int, default=6)
    e.add_argument("--keep-bg", action="store_true", help="keep near-white colours")
    c = sub.add_parser("contrast")
    c.add_argument("hex", nargs="+")
    a = ap.parse_args()
    if a.cmd == "extract":
        extract(a.image, a.k, a.keep_bg)
    else:
        if len(a.hex) < 2:
            sys.exit("give at least two colours")
        matrix(a.hex)


if __name__ == "__main__":
    main()
