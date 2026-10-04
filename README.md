<div align="center">

# 🎨 Brand IP Kit Skills

**12 个品牌 / IP 全套视觉 Agent Skills · GPT Image 2.5（Flare / Sunburst）**<br>
**12 Agent Skills for a complete brand & mascot visual kit — character sheet → logo → VI → packaging → stickers → merch → brand book**

[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-12-8b5cf6)](#-skills--技能列表)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-ready-d97757)](#-安装)
[![Codex](https://img.shields.io/badge/Codex-ready-111111)](#-安装)
[![Cursor](https://img.shields.io/badge/Cursor-ready-2563eb)](#-安装)
[![GPT Image 2.5](https://img.shields.io/badge/GPT%20Image%202.5-Flare%20%2F%20Sunburst-0d9488)](#-出图方式--rendering)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/xianyu110/brand-ip-kit-skills?style=social)](https://github.com/xianyu110/brand-ip-kit-skills)

[中文](#-中文) · [English](#-english) · [效果展示](#-效果展示--showcase) · [Skills](#-skills--技能列表) · [没有 Claude / API？](#-没有-claude--api)

<table>
<tr>
<td width="64%"><img src="https://upload.maynor1024.live/file/1791116767212_bipk-gallery-wall.jpg" alt="Brand IP Kit gallery wall — 12 outputs from one character sheet"></td>
<td width="36%"><img src="https://upload.maynor1024.live/file/1791116713589_bipk-demo.gif" alt="demo gif"></td>
</tr>
</table>

<sub>↑ 一张设定板 → 12 类品牌物料，全部由 GPT Image 2.5 真实生成（虚构品牌「MIKAN TEA 橘咪茶研」），未经 PS。提示词全文见 <a href="docs/showcase-prompts.md">docs/showcase-prompts.md</a><br>
One character sheet → 12 brand deliverables, real GPT Image 2.5 outputs for a fictional brand, no retouching.</sub>

</div>

---

## 🇨🇳 中文

做一个品牌 IP，真正难的不是"画出一只可爱的猫"，而是**让这只猫在 logo、名片、包装、表情包、海报、周边上都是同一只猫**，并且每样东西都符合它的用途（能缩到 16px、能印珐琅徽章、能被头像裁成圆）。

Brand IP Kit Skills 把这件事拆成 12 个可单独安装的 Agent Skill。对 Claude Code / Codex / Cursor 说一句"给我的茶饮品牌做一个橘子猫 IP 和整套物料"，它会先定角色、再定规范、最后批量出物料，并在每一步做质检。

**和一堆 prompt 的区别：**

- 🧬 **一次设定，处处复用**：`ip-character-sheet` 产出设定板 + 文字版 IP 身份卡，`ip-consistency-lock` 把它变成一段 LOCK，原样贴进后面每一条提示词，并用 7 项漂移打分决定"通过 / 局部修 / 重抽"。
- 📁 **共用 `brand/` 目录**：`brand.md` 是色值、字体、标语的唯一来源；所有 skill 读同一份，告别"每张图的橙色都不一样"。
- 🏭 **按用途出图，而不是按好看出图**：logo 要过 16px 测试并提醒矢量化；徽章限 ≤6 色闭合线；表情包按微信 240×240 切片；横幅按平台安全区排版；包装不编造成分和认证。
- 🛠 **脚本只做确定性的事**：抽色 + WCAG 对比度矩阵（`palette.py`）、整版切片/抠底/尺寸检查（`slice_grid.py`）、物料拼板与 PDF 品牌手册（`make_board.py`）、零依赖出图客户端（`generate.py`）。
- 🌏 **中文优先，提示词可移植**：流程与说明中文，提示词英文骨架 + 中文文案位，换 Gemini / Seedream / Midjourney 也能用。

### 📦 安装

```bash
# 方式 1：skills CLI（推荐）
npx skills add xianyu110/brand-ip-kit-skills

# 方式 2：手动复制
git clone https://github.com/xianyu110/brand-ip-kit-skills.git
cd brand-ip-kit-skills
mkdir -p ~/.claude/skills && cp -r skills/* ~/.claude/skills/     # Claude Code（全局）
mkdir -p ~/.codex/skills  && cp -r skills/* ~/.codex/skills/      # Codex
mkdir -p .cursor/skills   && cp -r skills/* .cursor/skills/       # Cursor（项目内）
```

只要其中几个？复制对应文件夹即可，例如 `cp -r skills/sticker-pack ~/.claude/skills/`。每个 skill 文件夹自带所需脚本，互不依赖。<br>
Claude Code 插件市场：`/plugin marketplace add xianyu110/brand-ip-kit-skills`。

### 🚀 使用

```text
用 brand-guidelines 给我的茶饮品牌「MIKAN TEA」做全套 IP 视觉，吉祥物是橘子猫，先给我物料计划和预算
用 ip-character-sheet 把 ./sketch.jpg 这只小熊定型成设定板，并写 IP 身份卡
用 sticker-pack 给橘咪做 16 个微信表情，语气网感一点，切成 240×240
用 holiday-campaign 做中秋 KV，标题「橘满月圆」，再延展一个小红书封面和限定礼盒
```

### 🔑 出图方式 / Rendering

| 方式 | 条件 | 做法 |
|---|---|---|
| ① 内置工具 | agent 自带生图（Codex imagegen 等） | 自动使用 |
| ② API Key | 设置 `GPTIMAGE_API_KEY`，可选 `GPTIMAGE_BASE_URL`（默认 `https://api.openai.com`；任何 OpenAI 兼容网关都行，没有的话见下方「方法二」） | `python scripts/generate.py --model sunburst --image brand/ref/ip-sheet.png --prompt-file p.txt --out out/logo.png` |
| ③ 都没有 | — | 输出最终提示词 + 需要上传的参考图清单，粘贴到任意支持参考图的生图工具 |

| 默认 **Flare** `gpt-image-2.5-flare` | 切 **Sunburst** `gpt-image-2.5-sunburst` |
|---|---|
| 概念草稿、场景、海报构图、批量变体 | 字标 / 中文标题 / HEX 标注必须逐字正确 |
| 样机、包装、周边效果图 | "只改一处"的局部修复（修漂移、改错字） |

---

## 🖼 效果展示 / Showcase

先用文生图出第 1 张设定板，再把**它作为唯一参考图**生成其余 11 张——就是 `ip-consistency-lock` 的标准用法。每张都是一次出图（没有挑选重抽），点击看大图。<br>
Image 1 is text-to-image; images 2–12 all use image 1 as the only identity reference. Single takes, no cherry-picking.

<table>
<tr>
<td align="center" width="33%"><a href="https://upload.maynor1024.live/file/1791116755589_bipk-01-ip-character-sheet.jpg"><img src="https://upload.maynor1024.live/file/1791116755589_bipk-01-ip-character-sheet.jpg" alt="ip-character-sheet" width="260"></a><br><sub><b>IP 形象设定</b> · <a href="skills/ip-character-sheet/SKILL.md"><code>ip-character-sheet</code></a></sub></td>
<td align="center" width="33%"><a href="https://upload.maynor1024.live/file/1791116756228_bipk-02-logo-lockup.jpg"><img src="https://upload.maynor1024.live/file/1791116756228_bipk-02-logo-lockup.jpg" alt="logo-lockup" width="260"></a><br><sub><b>Logo 组合</b> · <a href="skills/logo-lockup/SKILL.md"><code>logo-lockup</code></a></sub></td>
<td align="center" width="33%"><a href="https://upload.maynor1024.live/file/1791116753321_bipk-03-color-type-system.jpg"><img src="https://upload.maynor1024.live/file/1791116753321_bipk-03-color-type-system.jpg" alt="brand-color-type-system" width="260"></a><br><sub><b>品牌色彩与字体系统</b> · <a href="skills/brand-color-type-system/SKILL.md"><code>brand-color-type-system</code></a></sub></td>
</tr>
<tr>
<td align="center" width="33%"><a href="https://upload.maynor1024.live/file/1791116754061_bipk-04-vi-mockup.jpg"><img src="https://upload.maynor1024.live/file/1791116754061_bipk-04-vi-mockup.jpg" alt="vi-mockup" width="260"></a><br><sub><b>VI 样机</b> · <a href="skills/vi-mockup/SKILL.md"><code>vi-mockup</code></a></sub></td>
<td align="center" width="33%"><a href="https://upload.maynor1024.live/file/1791116753401_bipk-05-packaging-design.jpg"><img src="https://upload.maynor1024.live/file/1791116753401_bipk-05-packaging-design.jpg" alt="packaging-design" width="260"></a><br><sub><b>包装设计</b> · <a href="skills/packaging-design/SKILL.md"><code>packaging-design</code></a></sub></td>
<td align="center" width="33%"><a href="https://upload.maynor1024.live/file/1791116756360_bipk-06-sticker-pack.jpg"><img src="https://upload.maynor1024.live/file/1791116756360_bipk-06-sticker-pack.jpg" alt="sticker-pack" width="260"></a><br><sub><b>表情包 / 贴纸套组</b> · <a href="skills/sticker-pack/SKILL.md"><code>sticker-pack</code></a></sub></td>
</tr>
<tr>
<td align="center" width="33%"><a href="https://upload.maynor1024.live/file/1791116755376_bipk-07-social-avatar-cover.jpg"><img src="https://upload.maynor1024.live/file/1791116755376_bipk-07-social-avatar-cover.jpg" alt="social-avatar-cover" width="260"></a><br><sub><b>社媒头像与封面套件</b> · <a href="skills/social-avatar-cover/SKILL.md"><code>social-avatar-cover</code></a></sub></td>
<td align="center" width="33%"><a href="https://upload.maynor1024.live/file/1791116755121_bipk-08-ip-scene-poster.jpg"><img src="https://upload.maynor1024.live/file/1791116755121_bipk-08-ip-scene-poster.jpg" alt="ip-scene-poster" width="260"></a><br><sub><b>IP 场景海报</b> · <a href="skills/ip-scene-poster/SKILL.md"><code>ip-scene-poster</code></a></sub></td>
<td align="center" width="33%"><a href="https://upload.maynor1024.live/file/1791116764112_bipk-09-merch-design.jpg"><img src="https://upload.maynor1024.live/file/1791116764112_bipk-09-merch-design.jpg" alt="merch-design" width="260"></a><br><sub><b>周边文创</b> · <a href="skills/merch-design/SKILL.md"><code>merch-design</code></a></sub></td>
</tr>
<tr>
<td align="center" width="33%"><a href="https://upload.maynor1024.live/file/1791116761139_bipk-10-brand-guidelines.jpg"><img src="https://upload.maynor1024.live/file/1791116761139_bipk-10-brand-guidelines.jpg" alt="brand-guidelines" width="260"></a><br><sub><b>品牌手册汇总</b> · <a href="skills/brand-guidelines/SKILL.md"><code>brand-guidelines</code></a></sub></td>
<td align="center" width="33%"><a href="https://upload.maynor1024.live/file/1791116767052_bipk-11-ip-consistency-lock.jpg"><img src="https://upload.maynor1024.live/file/1791116767052_bipk-11-ip-consistency-lock.jpg" alt="ip-consistency-lock" width="260"></a><br><sub><b>IP 一致性锁定</b> · <a href="skills/ip-consistency-lock/SKILL.md"><code>ip-consistency-lock</code></a></sub></td>
<td align="center" width="33%"><a href="https://upload.maynor1024.live/file/1791116764153_bipk-12-holiday-campaign.jpg"><img src="https://upload.maynor1024.live/file/1791116764153_bipk-12-holiday-campaign.jpg" alt="holiday-campaign" width="260"></a><br><sub><b>品牌节日营销物料</b> · <a href="skills/holiday-campaign/SKILL.md"><code>holiday-campaign</code></a></sub></td>
</tr>
</table>

> 「MIKAN TEA 橘咪茶研」与 IP「橘咪」均为演示虚构，如与现实品牌雷同纯属巧合。生成图用于提案与方向确认；logo 交付前请矢量化并做商标检索，印刷品请打样。

---

## 🧩 Skills / 技能列表

| # | Skill | 做什么 | 默认模型 |
|---|---|---|---|
| 1 | [`ip-character-sheet`](skills/ip-character-sheet/SKILL.md) | **IP 形象设定** — 三视图 / 表情 / 色板 / 比例的设定板 + 文字版 IP 身份卡，后续所有 skill 的基准 | Flare |
| 2 | [`logo-lockup`](skills/logo-lockup/SKILL.md) | **Logo 组合** — 从 IP 简化图形 + 字标，输出横版/竖版/图标/反白四件套与安全空间 | Sunburst |
| 3 | [`brand-color-type-system`](skills/brand-color-type-system/SKILL.md) | **品牌色彩与字体系统** — 抽色、5 色结构与比例、WCAG 对比度检查（脚本）、中英字体层级、展示板 | Sunburst |
| 4 | [`vi-mockup`](skills/vi-mockup/SKILL.md) | **VI 样机** — 名片 / 工牌 / 手提袋 / 信封 / 门头，附常用物件尺寸与版面 | Flare |
| 5 | [`packaging-design`](skills/packaging-design/SKILL.md) | **包装设计** — 信息层级 → 系列 SKU 规则 → 平面稿 → 系列合照 / packshot，不编造成分认证 | Flare |
| 6 | [`sticker-pack`](skills/sticker-pack/SKILL.md) | **表情包 / 贴纸套组** — 情绪清单、整版 3×3 出图保证一致、切片到 240×240（脚本）、动态帧 | Sunburst |
| 7 | [`social-avatar-cover`](skills/social-avatar-cover/SKILL.md) | **社媒头像与封面套件** — 按平台画布与安全区出头像、横幅、帖子模板（小红书/公众号/B站/X/YouTube） | Flare |
| 8 | [`ip-scene-poster`](skills/ip-scene-poster/SKILL.md) | **IP 场景海报** — 一句话故事 + 4 种构图 + 标题留白，KV / 上新 / 开屏 | Flare → Sunburst |
| 9 | [`merch-design`](skills/merch-design/SKILL.md) | **周边文创** — 按工艺约束出图案（珐琅徽章/丝印 T 恤/热转印杯/亚克力/毛绒）+ 效果图 | Sunburst / Flare |
| 10 | [`brand-guidelines`](skills/brand-guidelines/SKILL.md) | **品牌手册汇总** — 总控：规划 → 调用其它 11 个 skill → 总验收 → 合成 PDF 手册（脚本） | Auto |
| 11 | [`ip-consistency-lock`](skills/ip-consistency-lock/SKILL.md) | **IP 一致性锁定** — 参考包 + LOCK 锁定段 + 7 项漂移打分 + 局部修复，多图保持同一角色 | Flare / Sunburst |
| 12 | [`holiday-campaign`](skills/holiday-campaign/SKILL.md) | **品牌节日营销物料** — 节日符号库 × 品牌钩子，KV 先行再延展封面/限定包装/表情/周边 | Sunburst / Flare |

**推荐顺序**：`ip-character-sheet` → `ip-consistency-lock` → `brand-color-type-system` → `logo-lockup` → 各类物料 → `brand-guidelines` 汇总。或者直接用 `brand-guidelines` 让它按顺序帮你跑完。

每个 `SKILL.md` 都包含：什么时候用 · 需要的输入 · 分步流程 · 带变量的提示词模板 · 质检清单 · 常见翻车与修复 · 出图方式。

---

## 💡 没有 Claude / API？

skill 里的出图脚本只认 `GPTIMAGE_API_KEY` + `GPTIMAGE_BASE_URL`，任何 OpenAI 兼容接口都能接。手上没有的话：

- **方法一**：`https://claude-opus.top/` — Claude 国内镜像站，打开网页就能用 Claude，把 `SKILL.md` 内容贴进去即可按流程出提示词。
- **方法二**：`https://tryallapi.com/register?aff=5A6A` — 一站式 API，GPT Image 2.5 / Claude / Gemini 一个 key 全部可用。可直接作为 `BASE_URL` 兜底：

```bash
export GPTIMAGE_API_KEY=sk-...                     # 在 tryallapi 后台创建
export GPTIMAGE_BASE_URL=https://tryallapi.com/v1  # 兜底网关，OpenAI 兼容
python skills/ip-character-sheet/scripts/generate.py --model flare --size 1536x1024 \
  --prompt-file prompt.txt --out out/ip-sheet.png
```

做电商？姊妹仓库 👉 [**xianyu110/ecommerce-image-skills**](https://github.com/xianyu110/ecommerce-image-skills)：12 个电商出图 skill（白底主图、场景图、A+、详情长图、小红书封面……），和本仓库共用同一套出图方式，IP 做好后可以直接拿去做商品图。

---

## 🇬🇧 English

A Chinese-first collection of **12 agent skills** that turn one mascot idea into a complete, consistent brand kit with image models — primarily **GPT Image 2.5** (Flare for drafts, Sunburst for exact text and local edits). Prompts are model-agnostic.

**Why not just a prompt pack?** One character sheet + a written identity card become a `LOCK` block that is pasted into every prompt; a 7-point drift score decides pass / repair / regenerate. All skills share a `brand/` folder where `brand.md` is the single source of truth for colours, fonts and copy. Outputs are fit for purpose (16 px logo test, enamel-pin colour limits, 240×240 sticker slicing, platform safe zones), and small scripts handle the deterministic parts.

### Install

```bash
npx skills add xianyu110/brand-ip-kit-skills
# or
git clone https://github.com/xianyu110/brand-ip-kit-skills.git && cp -r brand-ip-kit-skills/skills/* ~/.claude/skills/
```

Codex: `~/.codex/skills/` · Cursor: `.cursor/skills/` · Claude Code plugin: `/plugin marketplace add xianyu110/brand-ip-kit-skills`

### Use

```text
Use brand-guidelines to plan a full mascot brand kit for my tea brand "MIKAN TEA" — show the plan and budget first.
Use sticker-pack to make 16 WeChat stickers for the mascot and slice them to 240×240.
```

### Optional API key

```bash
export GPTIMAGE_API_KEY=sk-...
export GPTIMAGE_BASE_URL=https://api.openai.com   # or any OpenAI-compatible gateway, e.g. https://tryallapi.com/v1
```

### Skills

| Skill | What it does | Default model |
|---|---|---|
| [`ip-character-sheet`](skills/ip-character-sheet/SKILL.md) | Character sheet: turnaround, expressions, palette + an IP identity card | Flare |
| [`logo-lockup`](skills/logo-lockup/SKILL.md) | Symbol + wordmark lockups: horizontal, stacked, icon, mono | Sunburst |
| [`brand-color-type-system`](skills/brand-color-type-system/SKILL.md) | Palette extraction, ratios, WCAG contrast script, type scale, board | Sunburst |
| [`vi-mockup`](skills/vi-mockup/SKILL.md) | Business card, badge, tote, envelope, storefront mockups | Flare |
| [`packaging-design`](skills/packaging-design/SKILL.md) | Hierarchy → SKU system → flat art → packshots | Flare |
| [`sticker-pack`](skills/sticker-pack/SKILL.md) | Emotion list, 3×3 sheets, slicing to platform sizes, GIF frames | Sunburst |
| [`social-avatar-cover`](skills/social-avatar-cover/SKILL.md) | Avatars, banners, post templates with platform safe zones | Flare |
| [`ip-scene-poster`](skills/ip-scene-poster/SKILL.md) | Story-first posters & key visuals with headline space | Flare → Sunburst |
| [`merch-design`](skills/merch-design/SKILL.md) | Process-aware merch art + mockups: pins, tees, mugs, plush | Sunburst / Flare |
| [`brand-guidelines`](skills/brand-guidelines/SKILL.md) | Orchestrator: plan, run all skills, QA, compile a PDF brand book | Auto |
| [`ip-consistency-lock`](skills/ip-consistency-lock/SKILL.md) | Reference pack, LOCK block, 7-point drift score, repair | Flare / Sunburst |
| [`holiday-campaign`](skills/holiday-campaign/SKILL.md) | Festival symbols × brand hook: KV first, then extensions | Sunburst / Flare |

### Scripts

| Script | Purpose |
|---|---|
| `scripts/generate.py` | Zero-dependency GPT Image client (generations + edits) for any OpenAI-compatible endpoint |
| `scripts/palette.py` | Extract dominant colours from an image; WCAG contrast matrix for a palette |
| `scripts/slice_grid.py` | Slice sticker / expression / test grids, trim, optional transparency, resize, size-limit check |
| `scripts/make_board.py` | Assemble outputs into presentation boards or a multi-page PDF brand book |

`scripts/` is the source of truth; each skill bundles the copies it needs so a single folder works on its own.

---

## ⭐ Star History

<a href="https://star-history.com/#xianyu110/brand-ip-kit-skills&Date">
  <img src="https://api.star-history.com/svg?repos=xianyu110/brand-ip-kit-skills&type=Date" alt="Star History Chart" width="600">
</a>

## 🤝 Contributing

更好的模板、更多平台规格、更多工艺约束都欢迎 PR。请保持每个 skill 自包含（`skills/<name>/SKILL.md` + `scripts/`），平台规格请附可查证的来源。

## Related

- [ecommerce-image-skills](https://github.com/xianyu110/ecommerce-image-skills) — 12 个电商出图 Agent Skills（GPT Image 2.5）
- [awesome-gpt-image2.5](https://github.com/xianyu110/awesome-gpt-image2.5) — GPT Image 2.5 提示词案例库

## License

MIT © xianyu110

---

<div align="center">

我是 MaynorAI 团队，分享 AI 编程、AI SaaS 工具出海、一人团队搭建经验。

</div>
