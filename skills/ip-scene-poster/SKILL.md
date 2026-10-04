---
name: ip-scene-poster
description: "Use when the user wants a story-driven poster or key visual starring the brand IP — 新品海报、活动 KV、品牌故事插画、门店海报、开屏图 — with a clear headline area and the character kept on-model. Triggers: IP 海报, 场景海报, 主视觉, KV, 品牌插画, key visual, campaign poster, splash screen."
---

# IP 场景海报 · Scene Poster

海报不是"角色 + 背景"。这个 skill 先用一句话定**故事**，再定**构图与标题区**，最后出图——让 IP 在做一件和品牌信息有关的事。

> 属于 [brand-ip-kit-skills](https://github.com/xianyu110/brand-ip-kit-skills) · 草稿 Flare，定稿/大字标题用 Sunburst

## 需要的输入
- 海报目的：上新 / 活动 / 品牌形象 / 招聘 …；主标题与副标题（逐字）
- 投放位置与尺寸（见下表）；是否需要放产品
- `brand/` 参考：IP 设定板、色板、logo

## 步骤
1. **一句话故事**：`{IP} 在 {地点} 正在 {动作}，因为 {和卖点有关的理由}`。例："橘咪乘着橘子热气球飞过果园——因为新品是当季鲜橘"。给 3 个故事选 1。
2. **构图**：从下面 4 种里选——
   - **中心英雄**：IP 居中大，标题在上 1/4；适合品牌形象。
   - **三分对角**：IP 在一角，产品在另一角，视线连接；适合上新。
   - **大字压图**：标题占 40% 画面，IP 与文字互动（坐在字上 / 推着字）；适合活动。
   - **窗口叙事**：前景框（窗户、门、杯口）+ 远处场景；适合故事感。
3. **标题区留白**：在提示词里写清标题位置和"留空区域"，避免主体压字。
4. **草稿 → 定稿**：Flare 出 3–4 张选构图；选中的一张再用 Sunburst 修文字 / 细节，必要时"调整尺寸"出其它投放比例。
5. **检查一致性**：用 ip-consistency-lock 打分；海报场景复杂时最容易漂移。

## 常用投放尺寸
| 位置 | 比例 | 生成画布建议 |
|---|---|---|
| 手机海报 / 朋友圈 / 小红书 | 3:4 或 9:16 | 1024×1536 |
| 门店海报 / 易拉宝 | 2:3、1:2.5 | 1024×1536 后扩图 |
| 电商 Banner / 公众号头图 | 16:9、2.35:1 | 1536×1024 后扩图 |
| 开屏图 | 9:19.5 | 1024×1536，主体放中上，底部留 logo 区 |

## 提示词模板
```text
{LOCK}
{Vertical | Horizontal} poster, aspect {ratio}. Story: {IP name} {action} in {place}, because {reason}.
Composition: {hero centre | diagonal thirds | big type | window frame}. Mood: {mood}, {lighting}, {palette HEX list} dominant.
Background detail {rich | medium | minimal}, with clear depth; character stays flat cel-shaded exactly as reference.
Headline at {top / left}: "{headline}" in {font feel}; small line at bottom: "{brand / date}". Leave {area} empty for {logo / QR code}.
All text spelled exactly, no other text.
```

**带产品的版本**：在 LOCK 后追加
```text
Use image 2 as the exact product (shape, colour, label must not change). The product sits {position}, {IP name} interacts with it by {interaction}.
```

**系列海报（同一活动 3 张）**
```text
Same layout grid, typography and palette as image 2 (the approved first poster). Only change: story beat {2/3} — {action}, headline "{headline}".
```

## 质检清单
- [ ] 3 秒内看懂"谁在做什么"
- [ ] 标题区干净，标题逐字正确，与主体不重叠
- [ ] IP 风格没被场景风格"同化"（例如变成写实毛发）
- [ ] 产品（如有）与真实产品一致
- [ ] 预留了 logo / 二维码位置

## 常见翻车 & 修复
| 现象 | 修复 |
|---|---|
| 背景比角色抢眼 | 降低背景细节 "minimal background, soft focus"；用色彩对比把 IP 提出来 |
| 场景很美但 IP 变成写实 | 加 "character stays flat cel-shaded exactly as image 1, only background is painterly" |
| 标题被主体挡住 | 明确"top 25% empty for headline"；或先出无字图再排版 |
| 换比例后构图崩 | 用"调整尺寸 / outpaint"重排而不是裁切；重要比例分别生成 |

## 出图方式 · How to render

| 路线 | 条件 | 做法 |
|---|---|---|
| ① 内置工具 | agent 自带生图（Codex imagegen、ChatGPT 等） | 直接调用，把 `brand/ref/` 里的参考图作为输入图 |
| ② API Key | 设置 `GPTIMAGE_API_KEY`，可选 `GPTIMAGE_BASE_URL`（任意 OpenAI 兼容网关；没有官方 key 可用 `https://tryallapi.com/v1`） | `python scripts/generate.py --model flare --image brand/ref/ip-sheet.png --size 1024x1024 --prompt-file p.txt --out out/x.png` |
| ③ 都没有 | — | 输出最终提示词 + 需要上传的参考图清单，让用户粘贴到任何支持参考图的生图工具 |

**模型路由**：默认 GPT Image 2.5 **Flare**（`gpt-image-2.5-flare`，快、适合草稿与场景）；画面里有必须逐字正确的字标/中文标题、或做"只改一处"的局部编辑时切 **Sunburst**（`gpt-image-2.5-sunburst`）。提示词本身是模型无关的：换 Gemini / Seedream / Midjourney 等也能用，但文字渲染能力弱的模型请把文字留空、后期排版。
