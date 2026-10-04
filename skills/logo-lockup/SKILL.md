---
name: logo-lockup
description: "Use when the user needs a brand logo built from a symbol plus wordmark — 图形+字标组合、横版/竖版/图标版/反白版 lockups, clear-space and minimum-size rules — often derived from an existing IP character. Triggers: logo 设计, 标志组合, 字标, lockup, 品牌 logo, wordmark, app icon."
---

# Logo 组合 · Symbol + Wordmark Lockup

一个品牌至少需要 4 种 logo 用法：横版、竖版、纯图标、单色反白。这个 skill 从 IP 或品牌关键词出发，先简化出**图形**，再配**字标**，最后输出一整张 lockup 规范图。

> 属于 [brand-ip-kit-skills](https://github.com/xianyu110/brand-ip-kit-skills) · 默认 Sunburst（字标必须逐字正确）

## 需要的输入
- 品牌名（中文 / 英文，精确拼写、大小写）、可选副标（如"茶研""Studio"）
- 图形来源：`brand/ref/ip-sheet.png`，或 2–3 个品牌关键词
- 字标气质：圆润可爱 / 几何现代 / 书法国潮 / 衬线高级（选一）
- 已有色板（`brand/brand.md`），没有就先跑 `brand-color-type-system` 或临时给 2 个 HEX

## 步骤
1. **图形简化**：IP 全身图做不了 logo。只保留"头部 + 记忆钩子"，限制 ≤3 色 + 描边，去掉阴影和高光细节。先出 4 个简化方向（模板 A），选一个。
2. **字标**：字标是 logo 里最容易翻车的部分。品牌名 ≤ 8 个字符时让模型直接渲染（Sunburst）；更长或含生僻字时，模型只出图形，字标用真实字体后期排（见"后期替换"）。
3. **组合**：模板 B 一次出整张 lockup 规范板：横版主标、竖版、图标（圆/圆角方）、单色反白。
4. **缩小测试**：把图标缩到 32px / 16px 看还能否识别；不行就继续简化（去掉腮红、条纹）。
5. **矢量化**（交付前必做）：AI 生成的是位图。用 Illustrator 图像描摹 / Inkscape Trace Bitmap / vectorizer 类工具转 SVG，再手动修节点；字标用真实字体重打。在交付说明里写清这一步。
6. 保存：`brand/logo/` 下 `logo-horizontal.png`、`logo-stacked.png`、`logo-icon.png`、`logo-mono.png` 以及源提示词。

## 提示词模板

**A · 图形简化**
```text
Use image 1 as the character reference. Design 4 logo symbol options derived from its head only, in a 2x2 grid:
flat vector, maximum {3} colours ({HEX list}) plus {outline HEX} outline, no gradients, no shading, bold simple shapes,
must stay recognisable at 32 px. Keep the hook: {hook}. White background, no text.
```

**B · Lockup 规范板**
```text
Use image 1 as the symbol reference. Logo lockup sheet for "{brand}" on {off-white HEX}:
top: primary horizontal lockup — symbol left, wordmark reading exactly "{WORDMARK}" in {wordmark style}, colour {HEX},
{optional: small second line reading exactly "{subline}"}.
bottom row: (1) stacked version, symbol above wordmark (2) symbol alone inside a {circle / rounded square} app badge in {HEX}
(3) one-colour reversed version, white on {HEX}. Thin dashed clear-space guides. Clean vector presentation, no other text.
```

**C · 字标单独探索（不含图形）**
```text
Wordmark exploration for "{WORDMARK}": 6 variations in a 3x2 grid, {style keywords}, {HEX} on white,
consistent letter spacing, each spelled exactly "{WORDMARK}", no symbols, no extra words.
```

## 规范（写进品牌手册）
- 安全空间：四周 ≥ 图标高度的 1/4（或字标 x 高度）
- 最小尺寸：印刷横版 ≥ 25 mm 宽；屏幕图标 ≥ 24 px
- 反白：深色底只用单色白版，不要把彩色版直接放深色底上

## 质检清单
- [ ] 字标逐字正确（中文笔画、英文大小写、无多余字母）
- [ ] 图形 16/32 px 可识别
- [ ] 单色版不依赖颜色也成立
- [ ] 图形和字标视觉重量平衡（字标高度 ≈ 图形高度的 40–60%）
- [ ] 已提醒用户矢量化 + 商标检索（在当地商标数据库查近似）

## 常见翻车 & 修复
| 现象 | 修复 |
|---|---|
| 字标多一个字母 / 中文错字 | 切 Sunburst；字标写在引号里并加 "spelled exactly"；仍错就留空，后期用真实字体排 |
| 图形太复杂像插画 | 加 "flat vector, no shading, max 3 colours, icon style"；明确去掉的细节（条纹、腮红） |
| 每个版本图形长得不一样 | 先定图形 → 把选中图形作为参考图再出 lockup，而不是一次全部生成 |
| 看着像某个知名 logo | 换图形结构（轮廓/负形），并做商标近似检索 |

## 后期替换字标
模型只出图形 + 预留空白位置，再用 Figma / AI 排字：中文推荐开源可商用字体（思源黑体、阿里巴巴普惠体、站酷系列等，以各自授权为准），英文可用 Google Fonts。

## 出图方式 · How to render

| 路线 | 条件 | 做法 |
|---|---|---|
| ① 内置工具 | agent 自带生图（Codex imagegen、ChatGPT 等） | 直接调用，把 `brand/ref/` 里的参考图作为输入图 |
| ② API Key | 设置 `GPTIMAGE_API_KEY`，可选 `GPTIMAGE_BASE_URL`（任意 OpenAI 兼容网关；没有官方 key 可用 `https://tryallapi.com/v1`） | `python scripts/generate.py --model flare --image brand/ref/ip-sheet.png --size 1024x1024 --prompt-file p.txt --out out/x.png` |
| ③ 都没有 | — | 输出最终提示词 + 需要上传的参考图清单，让用户粘贴到任何支持参考图的生图工具 |

**模型路由**：默认 GPT Image 2.5 **Flare**（`gpt-image-2.5-flare`，快、适合草稿与场景）；画面里有必须逐字正确的字标/中文标题、或做"只改一处"的局部编辑时切 **Sunburst**（`gpt-image-2.5-sunburst`）。提示词本身是模型无关的：换 Gemini / Seedream / Midjourney 等也能用，但文字渲染能力弱的模型请把文字留空、后期排版。
