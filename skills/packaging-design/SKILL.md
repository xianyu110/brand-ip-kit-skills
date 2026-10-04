---
name: packaging-design
description: "Use when designing product packaging that carries a brand / IP — 杯子、盒子、袋子、瓶标、礼盒、系列化 SKU 包装 — including dielines-aware layout, SKU colour coding and photoreal packshots. Triggers: 包装设计, 包装盒, 瓶标, 礼盒, 系列包装, packaging design, label design, packshot."
---

# 包装设计 · Packaging

包装是 IP 出现频率最高的地方。这个 skill 先做**信息层级与系列规则**，再出包装效果图；生成图用于提案与选方向，真实生产稿需在刀版上排。

> 属于 [brand-ip-kit-skills](https://github.com/xianyu110/brand-ip-kit-skills) · 默认 Flare，包装正面文字多时切 Sunburst

## 需要的输入
- 产品与容器类型（杯 / 方盒 / 立袋 / 瓶 / 罐 / 管），规格（如 500 ml）
- 正面必须出现的文字（品牌、品名、规格），**由用户提供**；不编造成分、认证、功效
- SKU 数量与口味/型号名（做系列时）
- `brand/` 下 logo、色板、IP 参考

## 步骤
1. **信息层级**：按 1 秒（品牌/IP）→ 3 秒（品名/口味）→ 10 秒（规格/卖点）排序，写成一张表让用户确认。
2. **系列规则**（多 SKU）：固定元素（logo 位置、IP 姿势框架、字体）+ 变化元素（底色、IP 手里的道具、口味插画）。每个 SKU 一个色，色值从品牌辅助色延伸。
3. **主视觉**：先出一个 SKU 的正面平面稿（模板 A），确定版式。
4. **系列与立体效果**：把平面稿作为参考图出系列合照（模板 B）或单品 packshot（模板 C）。
5. **校对**：放大检查文字；任何法规信息（配料表、生产许可、条码）不要靠 AI 生成，在设计稿里用真实资料排。
6. **交付**：效果图 + 信息层级表 + 系列规则 + 提示词；提醒用户向印厂索要刀版图。

## 提示词模板

**A · 正面平面稿**
```text
Flat front-panel packaging artwork for a {container} of "{product name}" by "{brand}", {size}.
Hierarchy: 1) {IP name} {pose} large in the centre (image 1 is the reference) 2) wordmark "{brand}" top 3) product name "{product name}" 4) small "{size}".
Background {SKU HEX} with {pattern, e.g. subtle mandarin-slice pattern}. Flat print-ready look, no 3D, no mockup, all text spelled exactly.
```

**B · 系列合照**
```text
Photorealistic packaging family shot: {n} {containers} for "{brand}" lined up, same layout system, each in its own colour:
{SKU1 name — HEX1}, {SKU2 name — HEX2}, {SKU3 name — HEX3}. The mascot from image 1 appears on each with a different prop ({props}).
Studio set on {background}, soft reflections, commercial packshot, labels readable.
```

**C · 单品 packshot / 场景**
```text
Use image 1 as the exact front artwork, wrap it correctly onto a {material} {container}. {Scene: e.g. café counter with morning light / clean studio gradient}.
Keep logo and text unchanged, realistic {frost / foil / matte} material, 3/4 view.
```

**D · 礼盒开箱**
```text
Photorealistic opened gift box for "{brand}": lid off showing {contents}, inner lid printed with {IP name} {message pose}, ribbon {HEX}, tissue paper, top-down 45°.
```

## 质检清单
- [ ] 1 秒能认出品牌 / IP
- [ ] 品名与规格逐字正确；没有模型自己编的成分、功效、认证标志
- [ ] 系列图中固定元素位置一致，变化元素只变一处
- [ ] 包装曲面上 logo 透视合理，不像贴纸浮在表面
- [ ] 已提醒：法规信息、条码、刀版需在设计软件中完成

## 常见翻车 & 修复
| 现象 | 修复 |
|---|---|
| 模型自动加了"有机""0 糖"等字样 | 提示词加 "no extra claims, no badges, no certifications"；用 Sunburst 擦除 |
| 系列里每个盒子版式都不同 | 先定一张平面稿，以它为参考图再出系列，并写 "identical layout, only colour and prop change" |
| 杯身包装图拉伸变形 | 写清 "wrap around a cylinder, correct curvature"；或只出平面稿，用 3D 样机软件包裹 |
| 文字太多全部乱码 | 正面只留 3 段字；背面信息不交给 AI |

## 出图方式 · How to render

| 路线 | 条件 | 做法 |
|---|---|---|
| ① 内置工具 | agent 自带生图（Codex imagegen、ChatGPT 等） | 直接调用，把 `brand/ref/` 里的参考图作为输入图 |
| ② API Key | 设置 `GPTIMAGE_API_KEY`，可选 `GPTIMAGE_BASE_URL`（任意 OpenAI 兼容网关；没有官方 key 可用 `https://tryallapi.com/v1`） | `python scripts/generate.py --model flare --image brand/ref/ip-sheet.png --size 1024x1024 --prompt-file p.txt --out out/x.png` |
| ③ 都没有 | — | 输出最终提示词 + 需要上传的参考图清单，让用户粘贴到任何支持参考图的生图工具 |

**模型路由**：默认 GPT Image 2.5 **Flare**（`gpt-image-2.5-flare`，快、适合草稿与场景）；画面里有必须逐字正确的字标/中文标题、或做"只改一处"的局部编辑时切 **Sunburst**（`gpt-image-2.5-sunburst`）。提示词本身是模型无关的：换 Gemini / Seedream / Midjourney 等也能用，但文字渲染能力弱的模型请把文字留空、后期排版。
