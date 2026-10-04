---
name: holiday-campaign
description: "Use when planning holiday or festival marketing visuals for a brand IP — 春节、元宵、情人节、618、中秋、国庆、双11、圣诞 etc. — producing a matched set (KV poster, social cover, limited packaging, stickers, merch) with festive elements that don't override the brand. Triggers: 节日营销, 节日海报, 春节物料, 中秋海报, 双11, 节日限定, holiday campaign, festive key visual."
---

# 品牌节日营销物料 · Holiday Campaign

节日物料的难点：**节日元素要浓，但还得一眼是你家的 IP**。这个 skill 用"节日符号库 + 品牌化改造"的方法，一次规划出一整套同主题物料。

> 属于 [brand-ip-kit-skills](https://github.com/xianyu110/brand-ip-kit-skills) · KV 用 Sunburst（大字标题），延展物料 Flare

## 需要的输入
- 节日与上线日期；活动形式（限定品 / 折扣 / 纯品牌互动）
- 主标题、副标题、活动信息（逐字，**不编造折扣**）
- 需要的物料清单；`brand/` 参考

## 步骤
1. **节日符号挑 2 个**（见下表），不要堆满全部元素。
2. **品牌化改造**：把节日符号和品牌钩子融合，写一句"创意钩子"。例：中秋 × 橘子 → 月饼表面印橘瓣纹、"橘满月圆"。谐音梗只在品牌语气允许时使用。
3. **节日配色**：品牌主色保持 ≥30% 画面，节日色作为辅助（如春节红金、中秋藏青金、圣诞红绿），避免整张变成节日通用模板。
4. **先 KV**（模板 A），确认后用 KV 作为风格参考延展：社媒封面、限定包装、表情包 3–4 张、周边 1–2 件（模板 B）。
5. **合规检查**：不使用国旗/国徽等受限元素做商业装饰；宗教节日注意文化敏感；折扣信息由用户确认。

## 节日符号库（挑 2 个）
| 节日 | 符号 | 节日色 |
|---|---|---|
| 春节 | 灯笼、春联、福字、烟花、生肖、红包 | 中国红、金 |
| 元宵 | 汤圆、花灯、灯谜 | 暖橙、金 |
| 情人节 / 七夕 | 爱心、玫瑰、鹊桥、星河 | 粉、酒红 / 夜空蓝 |
| 618 / 双 11 | 购物袋、礼盒、倒计时数字、红包雨 | 品牌色 + 亮红 |
| 中秋 | 满月、月饼、玉兔、桂花、灯笼 | 藏青、金、暖黄 |
| 国庆 | 烟花、出游、城市地标 | 红、金（不用国旗国徽做装饰） |
| 圣诞 / 新年 | 圣诞树、雪花、礼物、毛线帽 | 红、绿、白 |

## 提示词模板

**A · 节日 KV**
```text
{LOCK}
{Festival} campaign key visual for "{brand}", {vertical 2:3 | horizontal 16:9}.
Creative hook: {hook}. {IP name} {action with festival symbol 1}, {festival symbol 2} around, {optional companion character}.
Palette: brand {HEX primary} stays dominant (≥30%), festive accents {festival colours}. Mood {warm / lively / elegant}, premium illustration.
Headline "{headline}" in {font feel} at {position}; small line "{campaign info}". All text spelled exactly, no other text.
```

**B · 延展物料（以 KV 为风格参考）**
```text
Use image 1 as the character reference and image 2 (approved festival KV) as the style, palette and symbol reference.
Create a {social cover 3:1 | limited packaging front | 3x3 festival sticker sheet | enamel pin} for the same campaign.
Keep the same festival symbols ({s1}, {s2}) and headline font feel. {Text: "..." | no text}.
```

**C · 节日倒计时系列（3/2/1）**
```text
{LOCK}
Countdown poster "{N}" for {festival}: big number "{N}" occupies 40% of the frame, {IP name} {interaction with the number}, same layout as image 2, only number and pose change.
```

## 质检清单
- [ ] 去掉 logo 后仍能认出是你家的 IP（品牌色 ≥30%）
- [ ] 节日符号 ≤2–3 个，主次清楚
- [ ] 标题与活动信息逐字正确，折扣与日期经用户确认
- [ ] 延展物料与 KV 同一套符号、字体气质、配色
- [ ] 无受限元素、无文化冒犯

## 常见翻车 & 修复
| 现象 | 修复 |
|---|---|
| 整张都是红金，品牌色没了 | 写 "brand orange dominant, red only as accents"；减少灯笼/烟花数量 |
| IP 被节日服装盖住特征 | 服装只加小配件（围巾、小帽），不遮挡记忆钩子 |
| 节日元素出现错误文化细节（如日式灯笼混入春节） | 在提示词写明 "Chinese {festival}"，并列出要的具体元素 |
| 延展物料风格和 KV 不像一家 | 把 KV 作为第二参考图，并写 "same style, palette and symbols as image 2" |

## 出图方式 · How to render

| 路线 | 条件 | 做法 |
|---|---|---|
| ① 内置工具 | agent 自带生图（Codex imagegen、ChatGPT 等） | 直接调用，把 `brand/ref/` 里的参考图作为输入图 |
| ② API Key | 设置 `GPTIMAGE_API_KEY`，可选 `GPTIMAGE_BASE_URL`（任意 OpenAI 兼容网关；没有官方 key 可用 `https://tryallapi.com/v1`） | `python scripts/generate.py --model flare --image brand/ref/ip-sheet.png --size 1024x1024 --prompt-file p.txt --out out/x.png` |
| ③ 都没有 | — | 输出最终提示词 + 需要上传的参考图清单，让用户粘贴到任何支持参考图的生图工具 |

**模型路由**：默认 GPT Image 2.5 **Flare**（`gpt-image-2.5-flare`，快、适合草稿与场景）；画面里有必须逐字正确的字标/中文标题、或做"只改一处"的局部编辑时切 **Sunburst**（`gpt-image-2.5-sunburst`）。提示词本身是模型无关的：换 Gemini / Seedream / Midjourney 等也能用，但文字渲染能力弱的模型请把文字留空、后期排版。
