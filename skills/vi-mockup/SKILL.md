---
name: vi-mockup
description: "Use when the user wants realistic VI / stationery mockups of a brand — 名片、工牌、手提袋、信纸、信封、门头、工服 — to present or test a visual identity. Triggers: VI 样机, 名片设计, 工牌, 手提袋, stationery mockup, brand identity mockup, 办公事务用品."
---

# VI 样机 · Stationery & Office Mockups

把 logo 和 IP 放到真实物件上看效果。这个 skill 先**确定每个物件上放什么**（版面），再生成摄影级样机；尺寸与印刷常识写在里面，避免"图很美但印不出来"。

> 属于 [brand-ip-kit-skills](https://github.com/xianyu110/brand-ip-kit-skills) · 默认 Flare，名片小字多时切 Sunburst

## 需要的输入
- `brand/logo/`（至少横版 + 图标）、`brand/brand.md` 色板、可选 IP 设定板
- 物件清单（默认：名片正反、工牌 + 挂绳、手提袋）；名片上的姓名职位联系方式（**用占位信息**，不要用真人信息）
- 呈现风格：平铺俯拍 / 45° 桌面 / 场景摆拍

## 步骤
1. **版面先行**：为每个物件写一行版面说明（见下表），用户确认后再出图。
2. **参考图**：logo 横版 + IP 图（≤2 张）。物件多时宁可分批出（每次 2–3 件），一张塞 8 件会让 logo 变形。
3. **生成**：模板 A（组合平铺）或模板 B（单件特写）。
4. **检查 logo**：放大看 logo 是否被"重画"了。变形 → Sunburst 局部编辑"把名片上的 logo 替换为图 2，保持透视"。
5. **交付**：样机图只是效果展示；真实印刷稿需按下方尺寸在设计软件里排版。

## 常用物件版面与尺寸
| 物件 | 尺寸（常见） | 版面建议 |
|---|---|---|
| 名片 | 中国 90×54 mm；欧美 85×55 mm；出血 3 mm | 正面 logo + 姓名职位；背面满版主色 + 小 IP |
| 工牌 | CR80 卡 85.6×54 mm（竖用） | 上 1/3 主色带 + logo，中间照片位，底部姓名 |
| 手提袋 | 常见 32×25×11 cm | 正面大 IP，侧面 logo，牛皮纸或白卡 |
| 信封 | DL 220×110 mm | 左上 logo，右下 IP 小角标 |
| 工服 / 围裙 | — | 左胸 logo 7–9 cm 宽，背后大字标 |

## 提示词模板

**A · 组合平铺**
```text
Photorealistic brand stationery flat-lay on {surface, e.g. warm beige paper}, soft daylight, gentle shadows, top-down {or 3/4} view.
Items: (1) business card front — {front layout}, (2) business card back — {back layout}, (3) {item 3 + layout}, (4) {item 4 + layout}.
Use image 1 as the exact logo (do not redraw it) and image 2 as the mascot reference. Brand colours {HEX list}.
Text on items limited to: "{brand}", "{placeholder name}", "{placeholder title}". Premium {matte / uncoated / kraft} print texture.
```

**B · 单件特写**
```text
Close-up product mockup of a {item} for "{brand}", {material and finish: e.g. 600gsm cotton card with orange edge painting / foil-stamped logo}.
Layout: {layout}. Use image 1 as the exact logo. Shallow depth of field, {background}, studio light.
```

**C · 空间延展（门头 / 前台）**
```text
Photorealistic {shop front / reception wall} for "{brand}": {sign material, e.g. backlit acrylic letters} showing the logo from image 1,
{IP name} {wall illustration / 3D figure} using image 2, brand colours {HEX}, {city / time of day}, architectural photography.
```

## 质检清单
- [ ] logo 没被重画（形状、字标拼写与原图一致）
- [ ] 透视正确：logo 贴合物件曲面、阴影方向一致
- [ ] 名片信息是占位信息，不含真实电话
- [ ] 主色在纸张材质上的表现合理（牛皮纸上不会出现纯白印刷除非注明白墨）
- [ ] 一组样机光线、色温统一

## 常见翻车 & 修复
| 现象 | 修复 |
|---|---|
| logo 被改成"差不多" | 减少同图物件数；Sunburst 局部替换；或生成空白样机后在 PS 里智能对象贴图 |
| 名片小字乱码 | 小字只保留 2–3 行；其余用 "fine grey placeholder lines" |
| 物件比例失真（名片比手提袋还大） | 写明 "realistic real-world scale"，并给出参照物（笔、咖啡杯） |
| 太像模板网站的样机 | 换真实环境道具（门店桌面、工作台），加入使用痕迹 |

## 出图方式 · How to render

| 路线 | 条件 | 做法 |
|---|---|---|
| ① 内置工具 | agent 自带生图（Codex imagegen、ChatGPT 等） | 直接调用，把 `brand/ref/` 里的参考图作为输入图 |
| ② API Key | 设置 `GPTIMAGE_API_KEY`，可选 `GPTIMAGE_BASE_URL`（任意 OpenAI 兼容网关；没有官方 key 可用 `https://tryallapi.com/v1`） | `python scripts/generate.py --model flare --image brand/ref/ip-sheet.png --size 1024x1024 --prompt-file p.txt --out out/x.png` |
| ③ 都没有 | — | 输出最终提示词 + 需要上传的参考图清单，让用户粘贴到任何支持参考图的生图工具 |

**模型路由**：默认 GPT Image 2.5 **Flare**（`gpt-image-2.5-flare`，快、适合草稿与场景）；画面里有必须逐字正确的字标/中文标题、或做"只改一处"的局部编辑时切 **Sunburst**（`gpt-image-2.5-sunburst`）。提示词本身是模型无关的：换 Gemini / Seedream / Midjourney 等也能用，但文字渲染能力弱的模型请把文字留空、后期排版。
