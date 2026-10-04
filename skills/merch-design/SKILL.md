---
name: merch-design
description: "Use when turning a brand IP into merchandise / 周边文创 — 徽章、T恤、马克杯、帆布袋、钥匙扣、贴纸、毛绒公仔、冰箱贴 — producing print-ready artwork direction plus photoreal merch mockups. Triggers: 周边设计, 文创, 徽章, T恤图案, 马克杯, 帆布袋, 钥匙扣, merch design, swag, enamel pin."
---

# 周边文创 · Merchandise

周边不是"把 IP 印上去"。不同工艺有不同限制：徽章要少色、T 恤要考虑印花工艺、杯子是曲面。这个 skill 先按**工艺**出适配图案，再出商品效果图。

> 属于 [brand-ip-kit-skills](https://github.com/xianyu110/brand-ip-kit-skills) · 图案 Sunburst（线稿干净）/ 效果图 Flare

## 需要的输入
- 品类清单与预算级别（打样小批量 / 量产）
- `brand/` 参考；是否需要文字（口号、年份、活动名）
- 风格：品牌常规 / 限定（节日、联名、城市）

## 步骤
1. **工艺 → 图案约束**（见下表），每个品类写一行约束，再写图案内容。
2. **先出平面图案**（模板 A），白底或透明底，便于后续矢量化与打样。
3. **再出效果图**（模板 B / C），把平面图案作为参考图贴到商品上。
4. **一组周边统一**：同一系列用同一个"系列主题"（例：橘子季、打工人、城市限定），姿势不同但道具/配色统一。
5. **生产交付**：平面图需矢量化或 300 dpi 位图；徽章要给工厂 Pantone 色号与描边金属线说明。

## 工艺约束速查
| 品类 | 工艺 | 图案要求 |
|---|---|---|
| 金属徽章 | 软/硬珐琅 | ≤6 色，每块颜色被金属线围合，最小线宽 ≈0.3 mm，尺寸常见 25–40 mm |
| T 恤 | 丝印 / 数码直喷 DTG / 烫画 | 丝印按色数计费（建议 ≤4 色）；DTG 可渐变；胸前小标 8–10 cm，正背大图 25–30 cm |
| 马克杯 | 热转印 | 印刷区约 20×8 cm 环绕，把手两侧各留 1–2 cm |
| 帆布袋 | 丝印 | 单色或双色最划算，避开大面积满版 |
| 亚克力钥匙扣 | UV 印 + 切割 | 外轮廓加 2–3 mm 白边，留挂孔 |
| 毛绒公仔 | 缝制 | 去掉细线条，五官改刺绣块面，比例更 Q |

## 提示词模板

**A · 平面图案（按工艺）**
```text
{LOCK}
Merch artwork for a {item} made with {process}: {IP name} {pose} {+ props}, {text: "{text}" spelled exactly | no text}.
Constraints: max {n} flat colours from {HEX list}, {closed outlines for enamel | no gradients | thick outlines}, centred on pure white, print-ready look, no mockup.
```

**B · 单品效果图**
```text
Photorealistic product photo of a {colour} {item} printed with the artwork from image 1 ({placement and size, e.g. 9 cm wide on left chest}).
Correct {fabric folds / mug curvature / enamel shine}, {setting}, soft natural light, lifestyle catalogue style.
```

**C · 周边全家福**
```text
{LOCK}
Photorealistic merch collection flat-lay on {surface}: {item list with designs}. Same series theme "{theme}", consistent palette {HEX}, natural window light, top-down.
```

**D · 毛绒 / 软胶手办打样图**
```text
{LOCK}
Product design render of a {plush toy | vinyl figure} of {IP name}, {height} cm, {material}, simplified for {sewing | moulding}: embroidered eyes, no thin lines.
Front and 3/4 view side by side, white studio background.
```

## 质检清单
- [ ] 图案满足工艺约束（色数、线宽、留白）
- [ ] 文字逐字正确；小尺寸（徽章）没有放长句
- [ ] 效果图里图案没变形、位置符合真实印刷区
- [ ] 一组周边属于同一系列主题
- [ ] 已提醒：量产前打样，色差以实物为准

## 常见翻车 & 修复
| 现象 | 修复 |
|---|---|
| 徽章图案有渐变/阴影，工厂做不了 | 加 "flat colours only, closed outlines, enamel pin artwork" |
| T 恤效果图图案浮在衣服上 | 写 "printed into the fabric, follows folds"；或用 PS 置换贴图 |
| 杯子图案被把手切断 | 写清 "design centred on the side opposite the handle" |
| 毛绒打样图太像插画 | 强调材质 "fuzzy fabric texture, visible seams" |

## 出图方式 · How to render

| 路线 | 条件 | 做法 |
|---|---|---|
| ① 内置工具 | agent 自带生图（Codex imagegen、ChatGPT 等） | 直接调用，把 `brand/ref/` 里的参考图作为输入图 |
| ② API Key | 设置 `GPTIMAGE_API_KEY`，可选 `GPTIMAGE_BASE_URL`（任意 OpenAI 兼容网关；没有官方 key 可用 `https://tryallapi.com/v1`） | `python scripts/generate.py --model flare --image brand/ref/ip-sheet.png --size 1024x1024 --prompt-file p.txt --out out/x.png` |
| ③ 都没有 | — | 输出最终提示词 + 需要上传的参考图清单，让用户粘贴到任何支持参考图的生图工具 |

**模型路由**：默认 GPT Image 2.5 **Flare**（`gpt-image-2.5-flare`，快、适合草稿与场景）；画面里有必须逐字正确的字标/中文标题、或做"只改一处"的局部编辑时切 **Sunburst**（`gpt-image-2.5-sunburst`）。提示词本身是模型无关的：换 Gemini / Seedream / Midjourney 等也能用，但文字渲染能力弱的模型请把文字留空、后期排版。
