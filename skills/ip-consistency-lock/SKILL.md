---
name: ip-consistency-lock
description: "Use when the same mascot / IP character must look identical across many images — new poses, scenes, outfits, series content — or when generated images keep drifting (变脸、配色跑偏、配件丢失). Provides a reference pack, a lock block to paste into every prompt, drift scoring and repair steps. Triggers: IP 一致性, 角色一致, 保持同一个角色, character consistency, same character multiple images."
---

# IP 一致性锁定 · Consistency Lock

图像模型没有"记忆"，每一张都是重新画。这个 skill 用 **参考包 + 锁定段 + 漂移打分** 三件事，把"看着像"变成"可检查"。其它 10 个物料 skill 都会先调用它。

> 属于 [brand-ip-kit-skills](https://github.com/xianyu110/brand-ip-kit-skills) · 草稿 Flare，修漂移用 Sunburst

## 需要的输入
- `brand/ip-card.md`（没有就先跑 `ip-character-sheet`）
- `brand/ref/ip-sheet.png` 设定板；可选：2–3 张已被认可的成品图
- 本次要出的图：数量、场景、动作

## 步骤
1. **组参考包**（最多 3 张，越少越干净）：设定板（必带） + 与本次动作最接近的一张认可成品 + （有道具时）道具参考。不要塞 5 张风格各异的图——模型会取平均。
2. **生成锁定段**：从身份卡提炼 5–7 条"不可变"特征，写成下方 LOCK 模板，**原样**贴进每一条提示词的开头。
3. **把可变项和不可变项分开写**：可变 = 动作、表情、服装/道具、场景、镜头；不可变 = LOCK。一次只改 1–2 个可变项。
4. **小批量出图**：每个场景先出 2 张 Flare，挑最像的。
5. **漂移打分**（每项 0/1，满分 7）：轮廓钩子、头身比、眼睛样式、主色、描边、固定配件、花纹位置。≥6 分通过；4–5 分进入修复；≤3 分重抽。
6. **修复**：用 Sunburst 局部编辑，只点名出问题的部位（"把叶芽改回两片、颜色 #6BAA4B，其它都不动"）。
7. **入库**：通过的图放进 `brand/ref/approved/`，后续可作为第二参考。

## 锁定段模板（LOCK）
```text
Use image 1 as the ONLY identity reference for "{IP name}". Keep exactly:
- silhouette & hook: {e.g. mandarin-shaped round head with a two-leaf green sprout}
- proportions: {2.5} heads tall, {chubby round body, short legs}
- face: {big glossy dark eyes with one highlight, tiny mouth, pink blush}
- colours: body {#F28C28}, belly/paws {#FFE9C7}, accent {#6BAA4B}, outline {#3B2A20}
- markings & accessories: {3 forehead stripes, cream tail tip; no clothes unless stated}
- rendering: {flat colour, soft cel shading, thick even outline}
Only the pose, expression, props and background below may change.
```

## 场景提示词模板
```text
{LOCK}
Scene: {IP name} {action} in {place}, {time/light}. Expression: {expression}. Props: {props}.
Camera: {full body / medium / close-up}, {eye-level / low angle}. Background {detail level} so the character stays dominant.
Aspect {ratio}. {No text | Text exactly: "..."}
```

**一致性测试格（推荐首次使用时跑一次）**
```text
{LOCK}
A 2x2 grid of the SAME character in four situations: (1) {s1} (2) {s2} (3) {s3} (4) {s4}.
Identical head shape, markings, colours and proportions in all panels; only pose, props and background change. Thin white gutters.
```
用 `python scripts/slice_grid.py grid.png --rows 2 --cols 2 --out out/tiles/` 切开后单独评分。

## 质检清单
- [ ] 漂移打分 ≥ 6/7
- [ ] 同一批图并排放，配色明暗一致（没有一张偏粉/偏黄）
- [ ] 服装/道具没有盖住记忆钩子
- [ ] 镜头远近变化时描边粗细观感一致

## 常见翻车 & 修复
| 现象 | 原因 | 修复 |
|---|---|---|
| 越改越不像 | 在上一张成品上连续多轮修改，误差累积 | 每次都回到设定板做参考，而不是用上一张 |
| 换画风后变成另一个角色 | 风格词压过了身份 | LOCK 放最前；风格词只写"lighting/material"，不写"in the style of" |
| 多角色同框时互换特征 | 特征描述没有绑定到具体角色 | 每个角色单独 LOCK，用"the cat (left) / the rabbit (right)"绑定位置 |
| 穿衣服后体型变瘦 | 服装词带入人体比例 | 写 "outfit sized for a {2.5}-head chubby body" |
| 同会话里模型去改"最近一张"而不是你指的那张 | 多图会话的引用混乱 | 一张图一个会话，或在 API 里只传需要的那张 |

## 出图方式 · How to render

| 路线 | 条件 | 做法 |
|---|---|---|
| ① 内置工具 | agent 自带生图（Codex imagegen、ChatGPT 等） | 直接调用，把 `brand/ref/` 里的参考图作为输入图 |
| ② API Key | 设置 `GPTIMAGE_API_KEY`，可选 `GPTIMAGE_BASE_URL`（任意 OpenAI 兼容网关；没有官方 key 可用 `https://tryallapi.com/v1`） | `python scripts/generate.py --model flare --image brand/ref/ip-sheet.png --size 1024x1024 --prompt-file p.txt --out out/x.png` |
| ③ 都没有 | — | 输出最终提示词 + 需要上传的参考图清单，让用户粘贴到任何支持参考图的生图工具 |

**模型路由**：默认 GPT Image 2.5 **Flare**（`gpt-image-2.5-flare`，快、适合草稿与场景）；画面里有必须逐字正确的字标/中文标题、或做"只改一处"的局部编辑时切 **Sunburst**（`gpt-image-2.5-sunburst`）。提示词本身是模型无关的：换 Gemini / Seedream / Midjourney 等也能用，但文字渲染能力弱的模型请把文字留空、后期排版。
