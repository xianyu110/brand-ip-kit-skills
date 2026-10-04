---
name: brand-guidelines
description: "Use when the user wants a complete brand / IP visual kit planned end-to-end or compiled into a brand manual — 品牌手册、VI 手册、品牌规范、全套物料汇总 — orchestrating the other brand-ip-kit skills, checking consistency and exporting a PDF/board. Triggers: 品牌手册, VI 手册, 品牌规范, 全套品牌视觉, brand guidelines, brand book, brand kit."
---

# 品牌手册汇总 · Brand Guidelines (Orchestrator)

这是总控 skill：从一句品牌描述出发，**规划 → 依次调用其它 11 个 skill → 统一验收 → 汇总成手册 PDF**。也可以只用最后一步，把已有物料整理成手册。

> 属于 [brand-ip-kit-skills](https://github.com/xianyu110/brand-ip-kit-skills) · 模型按各子 skill 路由

## 需要的输入
- 品牌名、定位、目标人群、3 个气质词
- 范围：完整套件 / 指定几项；预算（大约多少张图）
- 已有资产：logo、IP、色板、字体（有则跳过对应步骤）

## brand/ 目录约定（所有 skill 共用）
```text
brand/
├── brand.md          # 品牌名、标语、色彩、字体、语气（唯一数值来源）
├── ip-card.md        # IP 身份卡（ip-character-sheet 产出）
├── ref/              # 参考图：ip-sheet.png、ip-concept.png、approved/
├── logo/             # logo-horizontal / stacked / icon / mono
├── out/<skill>/      # 每个 skill 的成品
└── prompts/          # 每张成品的最终提示词（可复现）
```

## 步骤
1. **立项单**：把输入整理成 brand.md 的「基础信息」一节，并给出物料计划表（skill / 张数 / 模型 / 是否需要用户提供文字），让用户确认预算。默认完整套件约 25–35 张生成。
2. **按依赖顺序执行**：
   1. `ip-character-sheet` → 身份卡 + 设定板
   2. `ip-consistency-lock` → LOCK 段（后面全部复用）
   3. `brand-color-type-system` → 色彩字体
   4. `logo-lockup` → logo 四件套
   5. 物料并行：`vi-mockup` · `packaging-design` · `sticker-pack` · `social-avatar-cover` · `ip-scene-poster` · `merch-design` · `holiday-campaign`
3. **每步存档**：成品放 `brand/out/<skill>/`，提示词放 `brand/prompts/`，文件名含版本号。
4. **总验收**：把所有成品拼一张总览图 `python scripts/make_board.py --section "总览" "brand/out/*/*.png" --out brand/overview.png`，统一检查颜色、描边、logo 一致性；不合格的回到对应 skill 修。
5. **编手册**：按下方目录生成章节页（可用模板 A 生成章节封面/跨页样机），再用脚本合成 PDF：
   ```bash
   python scripts/make_board.py --title "{brand} 品牌手册" \
     --section "01 品牌标志" "brand/logo/*.png" \
     --section "02 色彩与字体" "brand/out/brand-color-type-system/*.png" \
     --section "03 IP 形象" brand/ref/ip-sheet.png "brand/out/ip-consistency-lock/*.png" \
     --section "04 应用物料" "brand/out/vi-mockup/*.png" "brand/out/packaging-design/*.png" \
     --section "05 社媒与表情" "brand/out/social-avatar-cover/*.png" "brand/out/sticker-pack/*.png" \
     --section "06 周边与营销" "brand/out/merch-design/*.png" "brand/out/holiday-campaign/*.png" \
     --out brand/handbook.pdf
   ```
6. **交付说明**：哪些是可直接用的、哪些需要矢量化 / 打样 / 法务检索（商标、字体授权）。

## 手册目录模板
```text
00 封面 · 品牌故事一句话
01 品牌标志：组合规范、安全空间、最小尺寸、错误用法
02 色彩：主辅色 HEX/RGB/CMYK、比例、可用文字组合
03 字体：中英文字体、字号层级
04 IP 形象：设定板、性格、表情、禁止事项（变形、换色、加配件）
05 应用：VI、包装、社媒、周边、节日
06 资源：文件清单与命名、联系人
```

## 提示词模板

**A · 手册跨页样机（用于展示/封面）**
```text
Photorealistic open brand guideline book on a desk, A4 landscape. Left page: section title "{01 品牌标志 LOGO}" with the logo from image 1 and a clear-space diagram;
right page: "{02 吉祥物 MASCOT}" with the character from image 2 in front/side/back and do / don't examples marked with small check and cross icons.
Closed cover in {HEX} with the mascot at the corner. Clean editorial layout, soft shadows, all headings spelled exactly.
```

**B · 错误用法页**
```text
{LOCK}
"Don't" examples grid for the {IP name} / logo, 2x3: stretched, recoloured, rotated, added outline glow, busy background, cropped face. Each with a small red cross, flat diagram style, no other text.
```

## 质检清单
- [ ] brand.md 是唯一数值来源，所有图与之一致
- [ ] 每个成品都有对应提示词，可复现
- [ ] 总览图里没有"异类"（色调、描边、风格）
- [ ] 手册包含错误用法和最小尺寸
- [ ] 交付说明列清需人工完成的事项

## 常见翻车 & 修复
| 现象 | 修复 |
|---|---|
| 物料越做越偏离初版 | 所有 skill 都以设定板为参考，不用上一张成品"接力" |
| 预算超支 | 先每项出 1 张定方向，用户确认后再补全 |
| 手册文字被 AI 写错 | 章节页正文用 make_board 或排版软件排，不交给图像模型 |

## 出图方式 · How to render

| 路线 | 条件 | 做法 |
|---|---|---|
| ① 内置工具 | agent 自带生图（Codex imagegen、ChatGPT 等） | 直接调用，把 `brand/ref/` 里的参考图作为输入图 |
| ② API Key | 设置 `GPTIMAGE_API_KEY`，可选 `GPTIMAGE_BASE_URL`（任意 OpenAI 兼容网关；没有官方 key 可用 `https://tryallapi.com/v1`） | `python scripts/generate.py --model flare --image brand/ref/ip-sheet.png --size 1024x1024 --prompt-file p.txt --out out/x.png` |
| ③ 都没有 | — | 输出最终提示词 + 需要上传的参考图清单，让用户粘贴到任何支持参考图的生图工具 |

**模型路由**：默认 GPT Image 2.5 **Flare**（`gpt-image-2.5-flare`，快、适合草稿与场景）；画面里有必须逐字正确的字标/中文标题、或做"只改一处"的局部编辑时切 **Sunburst**（`gpt-image-2.5-sunburst`）。提示词本身是模型无关的：换 Gemini / Seedream / Midjourney 等也能用，但文字渲染能力弱的模型请把文字留空、后期排版。
