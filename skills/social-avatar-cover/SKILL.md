---
name: social-avatar-cover
description: "Use when the brand needs a matching social media kit — 头像、主页封面/横幅、帖子模板、视频封面 — for 小红书、抖音、视频号、公众号、B站、微博、X、YouTube etc., with safe zones for circular crops and platform UI overlays. Triggers: 社媒头像, 主页封面, 横幅, 公众号封面, 小红书封面, social media kit, profile banner, avatar."
---

# 社媒头像与封面套件 · Social Kit

同一套视觉在不同平台的**裁切方式完全不同**：头像会被裁成圆，横幅两侧会被 UI 盖住，手机端只显示中间一条。这个 skill 先按平台确定画布与安全区，再生成一整套风格统一的头像、封面和帖子模板。

> 属于 [brand-ip-kit-skills](https://github.com/xianyu110/brand-ip-kit-skills) · 默认 Flare，封面上有标语时切 Sunburst

## 需要的输入
- 平台清单（例：小红书 + 公众号 + X）
- 标语 / 账号名（逐字）；`brand/` 下 logo、IP、色板
- 头像类型：IP 头像（亲和）还是 logo 头像（官方）

## 步骤
1. **列画布**：根据平台查下表，生成"画布清单"（平台 / 用途 / 尺寸 / 安全区）。规格变化快，交付前提醒用户到平台后台确认。
2. **头像**：只用 IP 头部或图标，主体占圆形安全区 70–80%；纯色或极简背景。出 3 个底色备选（模板 A）。
3. **封面 / 横幅**：主体与文字全部放进中央安全区，两侧只放可被裁掉的延展图案（模板 B）。超宽比例先用 1536×1024 生成，再用"扩图/调整尺寸"延展两侧，不要直接拉伸。
4. **帖子模板**：3 张同系列（模板 C）：内容卡、上新卡、互动卡，留出文字区，便于后续在 Canva/稿定 里替换文字。
5. **裁切预览**：把头像缩到 40px，放到圆形遮罩里看；横幅叠一层平台 UI 截图检查遮挡。

## 平台画布速查（常见值，以平台最新规定为准）
| 平台 | 头像 | 封面 / 横幅 | 内容封面 |
|---|---|---|---|
| 小红书 | 1:1，圆形裁切 | — | 3:4（1080×1440） |
| 微信公众号 | 1:1，圆形裁切 | — | 头条 2.35:1（900×383），次条 1:1 |
| 抖音 / 视频号 | 1:1，圆形 | 主页背景较宽，主体放中间 | 视频封面 9:16 / 3:4 |
| B 站 | 1:1，圆形 | 空间头图超宽，只有中间区域稳定可见 | 视频封面 16:10 / 16:9 |
| X (Twitter) | 400×400 圆形 | 1500×500，左下会被头像遮挡 | 16:9 |
| YouTube | 800×800 圆形 | 2560×1440，所有设备安全区约 1546×423 居中 | 1280×720 |

## 提示词模板

**A · 头像**
```text
{LOCK}
Profile avatar: {IP name} head only, {expression}, centred, filling 75% of a circle-safe area, solid {HEX} background,
flat and bold so it reads at 40 px. Square 1:1, no text.
```

**B · 横幅（中央安全区）**
```text
{LOCK}
Wide social banner for "{brand}", aspect {ratio}. All important content inside the central {safe %} area:
{IP name} {pose} on the {left/right} third, headline "{slogan}" in {font feel} {HEX}. Outer edges: only a seamless {pattern} that can be cropped.
{Avoid the bottom-left corner (profile photo overlay).} Background {HEX}.
```

**C · 帖子模板三联**
```text
{LOCK}
Three matching square social post templates for "{brand}" side by side: (1) {content card: IP holding a blank sign, empty text area}
(2) {"NEW" launch card with product placeholder} (3) {Q&A / poll card}. Shared border style, {HEX list}, generous empty space for text. No text except "NEW".
```

**D · 套件展示板（给老板/客户看）**
```text
{LOCK}
Social media kit presentation board on white: circular avatar left, wide banner right, three post templates below; small labels "AVATAR", "COVER", "POSTS". Clean, flat.
```

## 质检清单
- [ ] 头像 40px 仍能认出 IP；圆形裁切后不缺耳朵/配件
- [ ] 封面文字和主体在安全区内；被 UI 遮挡后仍成立
- [ ] 全套颜色和描边一致，像同一个设计师做的
- [ ] 标语逐字正确
- [ ] 导出尺寸正确（不要把 1024 方图直接当横幅拉伸）

## 常见翻车 & 修复
| 现象 | 修复 |
|---|---|
| 超宽横幅里 IP 被拉扁 | 先生成常规比例，再用 outpaint/调整尺寸向两侧扩展 |
| 头像主体太小 | 写明"head only, fills 75%"；或切图后手动放大裁切 |
| 文字靠边被头像挡住 | 提示词写出要避开的角落；交付时附遮挡预览 |
| 三张模板风格不一 | 一次生成三联图再切开（`slice_grid.py --rows 1 --cols 3`） |

## 出图方式 · How to render

| 路线 | 条件 | 做法 |
|---|---|---|
| ① 内置工具 | agent 自带生图（Codex imagegen、ChatGPT 等） | 直接调用，把 `brand/ref/` 里的参考图作为输入图 |
| ② API Key | 设置 `GPTIMAGE_API_KEY`，可选 `GPTIMAGE_BASE_URL`（任意 OpenAI 兼容网关；没有官方 key 可用 `https://tryallapi.com/v1`） | `python scripts/generate.py --model flare --image brand/ref/ip-sheet.png --size 1024x1024 --prompt-file p.txt --out out/x.png` |
| ③ 都没有 | — | 输出最终提示词 + 需要上传的参考图清单，让用户粘贴到任何支持参考图的生图工具 |

**模型路由**：默认 GPT Image 2.5 **Flare**（`gpt-image-2.5-flare`，快、适合草稿与场景）；画面里有必须逐字正确的字标/中文标题、或做"只改一处"的局部编辑时切 **Sunburst**（`gpt-image-2.5-sunburst`）。提示词本身是模型无关的：换 Gemini / Seedream / Midjourney 等也能用，但文字渲染能力弱的模型请把文字留空、后期排版。
