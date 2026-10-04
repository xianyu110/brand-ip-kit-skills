---
name: sticker-pack
description: "Use when making an emoji / sticker set for a brand IP — 微信表情包、贴纸、聊天表情、实体贴纸 — with a planned emotion list, consistent character, short captions and slicing to platform sizes. Triggers: 表情包, 贴纸, 微信表情, 聊天表情, emoji pack, sticker set, LINE stickers, die-cut stickers."
---

# 表情包 / 贴纸套组 · Sticker Pack

一套好表情包 = **一张情绪清单 + 稳定的角色 + 能一眼读懂的动作**。这个 skill 用"整版出图 → 切片"的方式保证同一套里角色一致，再按平台尺寸导出。

> 属于 [brand-ip-kit-skills](https://github.com/xianyu110/brand-ip-kit-skills) · 默认 Sunburst（每格都有中文短句）

## 需要的输入
- `brand/ref/ip-sheet.png` + `brand/ip-card.md`
- 数量（建议 8 / 16 / 24）与用途：微信表情 / 社群贴纸 / 实体贴纸
- 语气：品牌官方（礼貌）还是网感（梗）；需避开的词

## 步骤
1. **情绪清单**：按"高频聊天场景"排，而不是按"喜怒哀乐"。默认 16 个：早安、晚安、收到、好的、谢谢、哈哈、委屈、生气、震惊、加油、在吗、摸鱼、比心、拜托、再见、品牌专属（如"喝茶吗"）。让用户增删。
2. **每格写一行**：`文字 | 动作 | 表情 | 小道具`。动作要夸张、能剪影识别；文字 ≤4 个字。
3. **整版生成**：每张 3×3（9 格）。16 张 = 2 版。整版生成比单张逐个生成一致性高得多。
4. **切片**：`python scripts/slice_grid.py out/sheet-1.png --rows 3 --cols 3 --size 240 --thumb 120 --out out/stickers/`（`--transparent` 可把纯色底抠成透明，适合扁平背景）。
5. **逐张检查**：文字、手指数量、是否越格；不合格的单格用 Sunburst 局部修，或单独重出一张再替换。
6. **按平台导出**：见下表。动态表情（GIF）可先出 3–4 帧关键动作网格再合成。

## 平台规格速查（以平台当前规则为准）
| 平台 | 数量 | 主图 | 其它 |
|---|---|---|---|
| 微信表情开放平台 | 8 / 16 / 24 | 240×240，PNG/GIF，单张 ≤500 KB | 缩略图 120×120；封面 240×240；聊天页图标 50×50；详情横幅 750×400 |
| LINE Creators | 8 / 16 / 24 / 32 / 40 | 最大 370×320 PNG | 主图 240×240，tab 96×74 |
| 实体贴纸 | 任意 | 300 dpi，白边 ≥2 mm | 交付带刀线的 PDF |

## 提示词模板

**整版 3×3**
```text
{LOCK from ip-consistency-lock}
A sticker sheet of 9 die-cut stickers of {IP name}, 3x3 grid with even spacing, thick white sticker border, light grey background.
1 "{t1}" — {action1}; 2 "{t2}" — {action2}; 3 "{t3}" — {action3}; 4 "{t4}" — {action4}; 5 "{t5}" — {action5};
6 "{t6}" — {action6}; 7 "{t7}" — {action7}; 8 "{t8}" — {action8}; 9 "{t9}" — {action9}.
Captions in bold rounded Chinese, spelled exactly, placed beside the character, never covering the face. Same character in every sticker.
```

**单张补图**
```text
{LOCK}
One die-cut sticker of {IP name}: {action}, expression {expression}, caption "{text}" in bold rounded Chinese spelled exactly, white border, light grey background, centred, generous margin.
```

**动态帧（GIF）**
```text
{LOCK}
4 animation key frames of {IP name} {action} in a 2x2 grid, identical framing and size in every frame, plain {HEX} background, no text.
```
切片后用任意 GIF 工具（如 `ffmpeg` / ezgif）按 1→2→3→4 合成，每帧 120–200 ms。

## 质检清单
- [ ] 每张不看文字也能猜到意思
- [ ] 文字 ≤4 字，逐字正确，不压脸
- [ ] 16 张放在一起是同一个角色（用 ip-consistency-lock 的打分）
- [ ] 240px 下线条不糊；PNG ≤500 KB（脚本会提示）
- [ ] 没有使用他人 IP、明星肖像或未授权梗图元素

## 常见翻车 & 修复
| 现象 | 修复 |
|---|---|
| 格子里的角色大小不一 | 加 "same character size in every cell"；切片脚本会裁边并居中，统一外观 |
| 某一格文字错 | 该格单独 Sunburst 局部修："只把右下角文字改成「晚安」" |
| 手指多了 / 爪子变人手 | 身份卡写 "round paws, no fingers"；动作选不需要手指的 |
| 透明抠图有白边 | 生成时用与角色反差大的纯色底（如浅灰），切片时 `--transparent` |

## 出图方式 · How to render

| 路线 | 条件 | 做法 |
|---|---|---|
| ① 内置工具 | agent 自带生图（Codex imagegen、ChatGPT 等） | 直接调用，把 `brand/ref/` 里的参考图作为输入图 |
| ② API Key | 设置 `GPTIMAGE_API_KEY`，可选 `GPTIMAGE_BASE_URL`（任意 OpenAI 兼容网关；没有官方 key 可用 `https://tryallapi.com/v1`） | `python scripts/generate.py --model flare --image brand/ref/ip-sheet.png --size 1024x1024 --prompt-file p.txt --out out/x.png` |
| ③ 都没有 | — | 输出最终提示词 + 需要上传的参考图清单，让用户粘贴到任何支持参考图的生图工具 |

**模型路由**：默认 GPT Image 2.5 **Flare**（`gpt-image-2.5-flare`，快、适合草稿与场景）；画面里有必须逐字正确的字标/中文标题、或做"只改一处"的局部编辑时切 **Sunburst**（`gpt-image-2.5-sunburst`）。提示词本身是模型无关的：换 Gemini / Seedream / Midjourney 等也能用，但文字渲染能力弱的模型请把文字留空、后期排版。
