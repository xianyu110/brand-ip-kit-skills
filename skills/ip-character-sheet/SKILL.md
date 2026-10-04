---
name: ip-character-sheet
description: "Use when the user wants to create or formalise a brand mascot / IP character — 三视图、设定板、表情、配色、比例 — from a text idea, a sketch or an existing drawing. Produces the reference sheet and an IP identity card that every other brand-ip-kit skill reuses. Triggers: IP形象设计, 吉祥物, 角色设定, 三视图, character sheet, turnaround, mascot design."
---

# IP 形象设定 · Character Sheet

把一句"我想要一只橘子猫当吉祥物"变成**可复用的角色资产**：三视图 + 表情 + 色板 + 比例标尺的设定板，以及一份文字版「IP 身份卡」。后面 11 个 skill 都靠这两样东西保持同一个角色。

> 属于 [brand-ip-kit-skills](https://github.com/xianyu110/brand-ip-kit-skills) · 默认模型 GPT Image 2.5 Flare（终稿可切 Sunburst）

## 什么时候用
- 品牌还没有 IP，需要从 0 设计；或者有一张手绘/AI 草图，要"定型"。
- 已有 IP 但没有正式设定板，导致每次出图都长得不一样。

## 需要的输入
| 必填 | 选填 |
|---|---|
| 品牌名 + 一句话定位（卖什么、给谁） | 现有草图 / 参考图（最多 3 张） |
| 角色原型（动物/物件/人物/抽象） | 指定主色 HEX、禁用元素 |
| 性格 3 个关键词（如：元气、嘴硬、爱睡） | 目标场景：表情包为主？包装为主？（影响线条粗细） |

缺必填项时先问，不要自行脑补品牌定位。

## 步骤
1. **原型 × 品牌钩子**：列 3 个方向，每个方向 = 原型 + 一个和品牌有关的"记忆钩子"（例：橘子猫 = 猫 + 头顶橘子叶芽）。钩子必须在剪影里就能认出来。让用户选一个。
2. **写 IP 身份卡**（见下方模板），保存为 `brand/ip-card.md`。所有数值都要具体：头身比、主色 HEX、描边颜色和粗细、固定配件。
3. **出概念草稿**：用模板 A 跑 3–4 张 Flare，只看造型，不看排版。用户选定后，把选中的图存为 `brand/ref/ip-concept.png`。
4. **出设定板**：模板 B，以概念图为参考图（有参考图走 edits 接口）。横版 1536×1024。
5. **验收**：按质检清单逐项打勾；不合格的局部用 Sunburst 局部修（"只把背面的尾巴改成和正面一致，其它不动"）。
6. **定稿**：设定板存 `brand/ref/ip-sheet.png`；用 `scripts/palette.py extract brand/ref/ip-sheet.png` 核对实际色值，偏差大就回写身份卡或修图。

## IP 身份卡模板（brand/ip-card.md）
```text
IP 名：{中文名} / {English name}
原型：{例：圆滚滚的橘猫幼崽}
记忆钩子：{例：头部轮廓是橘子，头顶两片绿叶芽}
头身比：{2.5} 头身；体型 {圆/方/水滴}
五官：{眼睛形状与高光，嘴，腮红}
配色：主色 {#F28C28}；辅色 {#FFE9C7}；点缀 {#6BAA4B}；描边 {#3B2A20 粗描边}
固定配件：{只有叶芽，不戴帽子、不穿衣服}
画风：{扁平 + 柔和赛璐璐阴影 / 3D 软胶 / 手绘蜡笔 …}
性格：{元气 / 嘴硬 / 爱睡}
禁止：{写实毛发、人类手指、第二种主色}
```

## 提示词模板

**A · 概念草稿（文生图）**
```text
Original brand mascot concept for "{brand}", {one-line positioning}.
Character: {archetype}, memorable hook: {hook}. Personality: {k1}, {k2}, {k3}.
Proportions {ratio} heads tall, {body shape}. Palette: {primary HEX}, {secondary HEX}, {accent HEX}, outline {outline HEX}.
Style: {style}. Single character, full body, front 3/4 view, plain light background, no text.
```

**B · 设定板（带参考图）**
```text
Use image 1 as the identity reference. Character design reference sheet for "{IP name}".
{paste the whole IP identity card}
Layout on an off-white board with faint grid: top row = turnaround front / side / back at identical scale on one baseline,
with a height ruler marked "{ratio} HEADS"; bottom-left = {4} expression busts ({e1}, {e2}, {e3}, {e4});
bottom-right = colour swatches labelled with hex codes; title block reading exactly "{IP name} · CHARACTER SHEET".
Same proportions and markings in every view. No other text.
```

## 质检清单
- [ ] 三个视图头顶、脚底在同一水平线，体型大小一致
- [ ] 侧面/背面的花纹、配件位置与正面逻辑一致（背面没长出正面的五官）
- [ ] 剪影测试：涂黑后仍能认出（钩子在轮廓里）
- [ ] 色块 HEX 与身份卡一致（用 `palette.py` 抽色核对）
- [ ] 缩到 64px 仍能看清五官 → 能做头像和图标
- [ ] 标题文字逐字正确；没有多余乱码字

## 常见翻车 & 修复
| 现象 | 修复 |
|---|---|
| 三视图大小不一、站不齐 | 提示词加 "identical scale, all standing on one baseline"；或拆成三张单图后用 `make_board.py` 拼 |
| 背面凭空多出图案 / 侧面不对 | 在身份卡写清"背面：纯色 + 3 道条纹"；用 Sunburst 局部修背面 |
| 表情一变脸型就变 | 只出"头部胸像"表情，并写 "same head shape, only eyes and mouth change" |
| 撞脸知名 IP | 换钩子而不是换颜色；避免"像 XX 一样"的描述，不在提示词里写任何已有 IP 名 |
| 文字乱码 | 标题改 Sunburst 或留白后期加字 |

## 出图方式 · How to render

| 路线 | 条件 | 做法 |
|---|---|---|
| ① 内置工具 | agent 自带生图（Codex imagegen、ChatGPT 等） | 直接调用，把 `brand/ref/` 里的参考图作为输入图 |
| ② API Key | 设置 `GPTIMAGE_API_KEY`，可选 `GPTIMAGE_BASE_URL`（任意 OpenAI 兼容网关；没有官方 key 可用 `https://tryallapi.com/v1`） | `python scripts/generate.py --model flare --image brand/ref/ip-sheet.png --size 1024x1024 --prompt-file p.txt --out out/x.png` |
| ③ 都没有 | — | 输出最终提示词 + 需要上传的参考图清单，让用户粘贴到任何支持参考图的生图工具 |

**模型路由**：默认 GPT Image 2.5 **Flare**（`gpt-image-2.5-flare`，快、适合草稿与场景）；画面里有必须逐字正确的字标/中文标题、或做"只改一处"的局部编辑时切 **Sunburst**（`gpt-image-2.5-sunburst`）。提示词本身是模型无关的：换 Gemini / Seedream / Midjourney 等也能用，但文字渲染能力弱的模型请把文字留空、后期排版。
