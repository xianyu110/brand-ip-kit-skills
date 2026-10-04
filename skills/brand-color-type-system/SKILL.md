---
name: brand-color-type-system
description: "Use when defining or documenting a brand's colour palette and typography — 主辅色、色彩比例、对比度、中英文字体搭配、字号层级 — and rendering it as a presentation board. Triggers: 品牌色彩, 配色方案, 字体系统, 色板, colour system, typography, brand palette, design tokens."
---

# 品牌色彩与字体系统 · Colour & Type

把"橘色、可爱一点"变成**可执行的规范**：5 个带 HEX 的颜色、使用比例、可读性对比、中英文字体与字号层级，再出一张展示板。生成图只负责"展示"，数值由脚本和规范决定。

> 属于 [brand-ip-kit-skills](https://github.com/xianyu110/brand-ip-kit-skills) · 展示板用 Sunburst（大量 HEX 文字）

## 需要的输入
- 品牌定位 + 3 个气质词；已有 logo / IP 图（可选，用于抽色）
- 主要使用场景：屏幕为主 / 印刷为主 / 门店空间（影响色彩空间与字体选择）
- 禁忌色（行业或竞品已占用的颜色）

## 步骤
1. **抽色**（有图时）：`python scripts/palette.py extract brand/ref/ip-sheet.png -k 6`，得到实际像素色。AI 图的颜色常偏饱和，取值后人工微调。
2. **搭 5 色结构**：主色 1 + 浅底色 1 + 点缀色 1 + 深色文字 1 + 情绪色 1。给每个颜色起名字（"橘咪橙"比 `#F28C28` 好记）。
3. **比例**：默认 60 / 20 / 10 / 5 / 5（底色 / 主色 / 文字 / 点缀 / 情绪），写进规范。
4. **对比度检查**：`python scripts/palette.py contrast "#F28C28" "#FFE9C7" "#3B2A20" "#FFFFFF"`。正文组合必须 ≥ 4.5（AA），大标题 ≥ 3。不合格的组合在规范里明确"禁止放文字"。
5. **字体**：每种语言最多 2 款（标题 / 正文）。中文优先开源可商用字体（思源黑体/宋体、阿里巴巴普惠体、OPPO Sans、站酷快乐体等，交付前请核实各自授权）；英文配同气质的无衬线或衬线。定 5 级字号：H1/H2/H3/Body/Caption（例：48/32/24/16/12 px）。
6. **写入 `brand/brand.md`** 的「色彩」「字体」两节（模板见下）。
7. **展示板**：模板 A 生成；数值以 `brand.md` 为准，图上如有错字，用 Sunburst 局部改或后期修。

## brand.md 片段模板
```markdown
## 色彩
| 名称 | HEX | RGB | 用途 | 比例 |
|---|---|---|---|---|
| {橘咪橙} | #F28C28 | 242,140,40 | 主色、按钮、IP 身体 | 20% |
| {奶油白} | #FFE9C7 | 255,233,199 | 大面积底色 | 60% |
| {树皮棕} | #3B2A20 | 59,42,32 | 正文、描边 | 10% |
| {叶芽绿} | #6BAA4B | 107,170,75 | 点缀、新品标签 | 5% |
| {腮红粉} | #F7A6A0 | 247,166,160 | 情绪、节日 | 5% |
允许的文字组合：棕字/奶油底（11.5）、白字/棕底；禁止：白字/橙底（对比不足）

## 字体
标题：{中文字体} / {English font} · 正文：{…} · 字号 48/32/24/16/12 · 行高 1.5
```

## 提示词模板

**A · 色彩 + 字体展示板**
```text
Brand colour and typography system board for "{brand}", clean Swiss grid, {off-white HEX} background.
Left: five large rounded swatch cards, each labelled with name and hex exactly: "{name1} {HEX1}", "{name2} {HEX2}", "{name3} {HEX3}", "{name4} {HEX4}", "{name5} {HEX5}";
under them a horizontal proportion bar {60/20/10/5/5}.
Right: typography specimen — a large "Aa" in {headline font feel}, the line "{brand}" as a headline, the line "{Chinese slogan}" in {Chinese font feel}, body text shown as grey bars.
{Optional: small {IP name} peeking from the bottom-right corner, use image 1 as reference.} No other text.
```

**B · 配色应用预览（检验配色是否好用）**
```text
Three UI cards side by side using only these colours: {HEX list}. Card 1 a product card with a {primary} button,
card 2 a {accent} "NEW" tag on {background}, card 3 dark mode using {dark} background with {light} text. Flat, no other colours.
```

## 质检清单
- [ ] 所有 HEX 在 brand.md、展示板、logo 中完全一致
- [ ] 正文颜色组合对比度 ≥ 4.5
- [ ] 主色在白底和深色底都成立
- [ ] 字体为可商用授权，并写明来源
- [ ] 色盲友好：重要信息不只靠红/绿区分

## 常见翻车 & 修复
| 现象 | 修复 |
|---|---|
| 展示板上的 HEX 写错一位 | 规范以 brand.md 为准；图用 Sunburst 改或直接后期替换文字 |
| 生成图颜色比规定更艳 | 正常现象，提示词加 "flat, exact colours, no colour grading"；最终色值不以图为准 |
| 主色印刷后发灰 | 屏幕 RGB 转 CMYK 会掉饱和，提前让印厂打样，并在规范里补 CMYK / Pantone 近似值 |
| 字体有中文但图上中文乱 | 展示板只放少量中文；长文用灰条代替 |

## 出图方式 · How to render

| 路线 | 条件 | 做法 |
|---|---|---|
| ① 内置工具 | agent 自带生图（Codex imagegen、ChatGPT 等） | 直接调用，把 `brand/ref/` 里的参考图作为输入图 |
| ② API Key | 设置 `GPTIMAGE_API_KEY`，可选 `GPTIMAGE_BASE_URL`（任意 OpenAI 兼容网关；没有官方 key 可用 `https://tryallapi.com/v1`） | `python scripts/generate.py --model flare --image brand/ref/ip-sheet.png --size 1024x1024 --prompt-file p.txt --out out/x.png` |
| ③ 都没有 | — | 输出最终提示词 + 需要上传的参考图清单，让用户粘贴到任何支持参考图的生图工具 |

**模型路由**：默认 GPT Image 2.5 **Flare**（`gpt-image-2.5-flare`，快、适合草稿与场景）；画面里有必须逐字正确的字标/中文标题、或做"只改一处"的局部编辑时切 **Sunburst**（`gpt-image-2.5-sunburst`）。提示词本身是模型无关的：换 Gemini / Seedream / Midjourney 等也能用，但文字渲染能力弱的模型请把文字留空、后期排版。
