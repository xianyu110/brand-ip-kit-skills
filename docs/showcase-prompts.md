# Showcase prompts · 示例图提示词

README 里 12 张示例图的**完整原始提示词**。全部由 GPT Image 2.5 通过 OpenAI 兼容接口（`/v1/images/generations` 与 `/v1/images/edits`，quality=high）一次生成，未经 PS 修图；仅为 README 缩放与转码为 JPG。

虚构品牌：**MIKAN TEA 橘咪茶研**，IP：**橘咪 MIKAN**。先用文生图出设定板，再把设定板作为唯一参考图生成其余 11 张——这就是 `ip-consistency-lock` 的用法。

复现：`python scripts/generate.py --model <model> --size <size> --quality high [--image out/01-ip-sheet.png] --prompt-file NN.txt`

## 01 · IP 形象设定 · ip-character-sheet

模型 `gpt-image-2.5-flare` · 尺寸 `1536x1024` · 参考图：无（文生图）

```text
Character design reference sheet (设定板) for an original brand mascot IP named "MIKAN 橘咪": a chubby round orange tabby kitten whose head is shaped like a mandarin orange, with a small green two-leaf sprout on top of the head, big glossy dark eyes, tiny pink blush cheeks, cream-white belly and paws, short stubby legs, a little curled tail with a cream tip. Flat vector-like illustration with soft cel shading, clean thick outlines, kawaii but premium.
Layout on a clean off-white #FAF6EF board with thin grid lines: top row = turnaround three views (front / side / back) at identical scale standing on a baseline; bottom-left = 4 facial expressions (happy, surprised, sleepy, proud) as head busts; bottom-right = colour palette swatches with hex labels: #F28C28 orange, #FFE9C7 cream, #6BAA4B leaf green, #3B2A20 outline brown, #F7A6A0 blush; a small title block top-left reading exactly "MIKAN 橘咪 · CHARACTER SHEET". Consistent proportions across all views, 2.5 heads tall. No other text.
```

## 02 · Logo 组合 · logo-lockup

模型 `gpt-image-2.5-sunburst` · 尺寸 `1536x1024` · 参考图：图 1 = 第 1 张设定板

```text
Use image 1 as the ONLY identity reference for the mascot "MIKAN 橘咪": keep the exact same character — round mandarin-shaped orange tabby kitten head, green two-leaf sprout on top, big glossy dark eyes, pink blush, cream belly and paws, cream-tipped curled tail, thick dark-brown outline, flat soft cel shading, same proportions. Brand colours: orange #F28C28, cream #FFE9C7, leaf green #6BAA4B, brown #3B2A20.
Create a brand logo lockup sheet for a fictional citrus tea shop brand "MIKAN TEA". On off-white #FAF6EF: top = primary horizontal lockup: simplified flat MIKAN head icon (front view, minimal, 2 colours + outline) left of a rounded bold geometric wordmark reading exactly "MIKAN TEA" in brown #3B2A20 with small Chinese line "橘咪茶研" below it. Bottom row: stacked vertical lockup, icon-only app badge in orange circle, and a one-colour white-on-orange reversed version. Clear space guides as thin dashed lines. Clean vector logo presentation, no other text.
```

## 03 · 色彩与字体 · brand-color-type-system

模型 `gpt-image-2.5-sunburst` · 尺寸 `1536x1024` · 参考图：图 1 = 第 1 张设定板

```text
Use image 1 as the ONLY identity reference for the mascot "MIKAN 橘咪": keep the exact same character — round mandarin-shaped orange tabby kitten head, green two-leaf sprout on top, big glossy dark eyes, pink blush, cream belly and paws, cream-tipped curled tail, thick dark-brown outline, flat soft cel shading, same proportions. Brand colours: orange #F28C28, cream #FFE9C7, leaf green #6BAA4B, brown #3B2A20.
Brand colour & typography system board for "MIKAN TEA". Left half: five large rounded colour swatch cards labelled with names and hex: "Mikan Orange #F28C28", "Cream #FFE9C7", "Sprout Green #6BAA4B", "Bark Brown #3B2A20", "Blush #F7A6A0", with proportion bar showing 60/20/10/5/5. Right half: typography specimen — big "Aa" in rounded bold sans, line "MIKAN TEA" headline, line "橘咪茶研 · 一口清甜" in rounded Chinese heiti, small body text lines as grey bars. Small MIKAN mascot peeking from bottom-right corner. Clean Swiss-grid design board, off-white background.
```

## 04 · VI 样机 · vi-mockup

模型 `gpt-image-2.5-flare` · 尺寸 `1024x1024` · 参考图：图 1 = 第 1 张设定板

```text
Use image 1 as the ONLY identity reference for the mascot "MIKAN 橘咪": keep the exact same character — round mandarin-shaped orange tabby kitten head, green two-leaf sprout on top, big glossy dark eyes, pink blush, cream belly and paws, cream-tipped curled tail, thick dark-brown outline, flat soft cel shading, same proportions. Brand colours: orange #F28C28, cream #FFE9C7, leaf green #6BAA4B, brown #3B2A20.
Photorealistic VI stationery mockup flat-lay on warm beige paper background, soft daylight shadows: a business card (front shows the MIKAN head icon + "MIKAN TEA", back is solid orange with small mascot), an employee ID badge on a green lanyard with a mascot illustration and text "STAFF", and a cream kraft paper shopping bag printed with the full-body MIKAN mascot waving and the wordmark "MIKAN TEA". Consistent brand colours, premium print texture, top-down 3/4 view.
```

## 05 · 包装设计 · packaging-design

模型 `gpt-image-2.5-flare` · 尺寸 `1024x1024` · 参考图：图 1 = 第 1 张设定板

```text
Use image 1 as the ONLY identity reference for the mascot "MIKAN 橘咪": keep the exact same character — round mandarin-shaped orange tabby kitten head, green two-leaf sprout on top, big glossy dark eyes, pink blush, cream belly and paws, cream-tipped curled tail, thick dark-brown outline, flat soft cel shading, same proportions. Brand colours: orange #F28C28, cream #FFE9C7, leaf green #6BAA4B, brown #3B2A20.
Photorealistic packaging design product shot: a family of three items for "MIKAN TEA" — a frosted plastic cold-brew tea cup with orange lid and the mascot printed on the side, a square paper tea gift box in cream with orange band and mascot holding a mandarin, and a stand-up pouch of tea bags in leaf green. Each package shows the wordmark "MIKAN TEA". Studio set on soft orange gradient, gentle reflections, commercial packaging photography.
```

## 06 · 表情包 · sticker-pack

模型 `gpt-image-2.5-sunburst` · 尺寸 `1024x1024` · 参考图：图 1 = 第 1 张设定板

```text
Use image 1 as the ONLY identity reference for the mascot "MIKAN 橘咪": keep the exact same character — round mandarin-shaped orange tabby kitten head, green two-leaf sprout on top, big glossy dark eyes, pink blush, cream belly and paws, cream-tipped curled tail, thick dark-brown outline, flat soft cel shading, same proportions. Brand colours: orange #F28C28, cream #FFE9C7, leaf green #6BAA4B, brown #3B2A20.
A sticker sheet of 9 die-cut stickers of the MIKAN mascot (3x3 grid, white sticker borders, subtle drop shadow) on light grey background. Each sticker a different emotion/pose with a short Chinese caption in bold rounded font: "早安", "收到", "冲鸭", "哈哈哈", "委屈", "谢谢老板", "摸鱼中", "晚安", "爱你". Same character in every sticker, flat cartoon style, captions spelled exactly.
```

## 07 · 社媒套件 · social-avatar-cover

模型 `gpt-image-2.5-sunburst` · 尺寸 `1536x1024` · 参考图：图 1 = 第 1 张设定板

```text
Use image 1 as the ONLY identity reference for the mascot "MIKAN 橘咪": keep the exact same character — round mandarin-shaped orange tabby kitten head, green two-leaf sprout on top, big glossy dark eyes, pink blush, cream belly and paws, cream-tipped curled tail, thick dark-brown outline, flat soft cel shading, same proportions. Brand colours: orange #F28C28, cream #FFE9C7, leaf green #6BAA4B, brown #3B2A20.
Social media kit layout on white canvas: left = a circular profile avatar of MIKAN head on solid orange background; right = a wide 3:1 banner cover with the mascot lying on a big mandarin slice, tagline text "MIKAN TEA · 一口清甜" on cream background with leaf patterns; bottom = three square post templates showing the mascot holding a tea cup, a "NEW" badge, and a mandarin. Presented as a clean design kit board with labels "AVATAR", "COVER", "POSTS".
```

## 08 · IP 场景海报 · ip-scene-poster

模型 `gpt-image-2.5-flare` · 尺寸 `1024x1536` · 参考图：图 1 = 第 1 张设定板

```text
Use image 1 as the ONLY identity reference for the mascot "MIKAN 橘咪": keep the exact same character — round mandarin-shaped orange tabby kitten head, green two-leaf sprout on top, big glossy dark eyes, pink blush, cream belly and paws, cream-tipped curled tail, thick dark-brown outline, flat soft cel shading, same proportions. Brand colours: orange #F28C28, cream #FFE9C7, leaf green #6BAA4B, brown #3B2A20.
Vertical scene poster (illustration) : MIKAN mascot riding a giant mandarin orange like a hot-air balloon above a sunny orchard with tiny tea cups as clouds, warm golden light, depth and atmosphere, storybook-quality illustration while keeping the flat cel-shaded character exactly the same. Big headline at top in bold rounded Chinese: "夏日橘子季", small subline "MIKAN TEA" at bottom. Poster composition with clear title area.
```

## 09 · 周边文创 · merch-design

模型 `gpt-image-2.5-flare` · 尺寸 `1024x1024` · 参考图：图 1 = 第 1 张设定板

```text
Use image 1 as the ONLY identity reference for the mascot "MIKAN 橘咪": keep the exact same character — round mandarin-shaped orange tabby kitten head, green two-leaf sprout on top, big glossy dark eyes, pink blush, cream belly and paws, cream-tipped curled tail, thick dark-brown outline, flat soft cel shading, same proportions. Brand colours: orange #F28C28, cream #FFE9C7, leaf green #6BAA4B, brown #3B2A20.
Photorealistic merchandise product photo set on a cream tabletop: a round enamel pin badge of the MIKAN head, a white cotton T-shirt with the mascot waving printed on the chest and "MIKAN" under it, a white ceramic mug with the mascot wrapped around it, and an acrylic keychain of the sitting mascot. Soft natural window light, lifestyle merch catalogue style.
```

## 10 · 品牌手册 · brand-guidelines

模型 `gpt-image-2.5-sunburst` · 尺寸 `1024x1024` · 参考图：图 1 = 第 1 张设定板

```text
Use image 1 as the ONLY identity reference for the mascot "MIKAN 橘咪": keep the exact same character — round mandarin-shaped orange tabby kitten head, green two-leaf sprout on top, big glossy dark eyes, pink blush, cream belly and paws, cream-tipped curled tail, thick dark-brown outline, flat soft cel shading, same proportions. Brand colours: orange #F28C28, cream #FFE9C7, leaf green #6BAA4B, brown #3B2A20.
Brand guideline book spread mockup, photorealistic: an open A4 landscape brand manual lying on a desk. Left page: section title "01 品牌标志 LOGO" with the MIKAN TEA logo lockup and clear space diagram; right page: "02 吉祥物 MASCOT" showing the mascot front/side/back and do/don’t examples with small green check and red cross marks. Closed cover of the manual (solid orange with mascot) visible at the corner. Clean editorial layout, soft shadows.
```

## 11 · 一致性锁定 · ip-consistency-lock

模型 `gpt-image-2.5-flare` · 尺寸 `1024x1024` · 参考图：图 1 = 第 1 张设定板

```text
Use image 1 as the ONLY identity reference for the mascot "MIKAN 橘咪": keep the exact same character — round mandarin-shaped orange tabby kitten head, green two-leaf sprout on top, big glossy dark eyes, pink blush, cream belly and paws, cream-tipped curled tail, thick dark-brown outline, flat soft cel shading, same proportions. Brand colours: orange #F28C28, cream #FFE9C7, leaf green #6BAA4B, brown #3B2A20.
Consistency test grid: 2x2 panels of the SAME MIKAN mascot in four different situations — (1) sitting reading a book in a cafe, (2) wearing a tiny yellow raincoat jumping in a puddle, (3) sleeping on a cloud at night, (4) waving at the beach with sunglasses pushed up. Identical head shape, sprout, stripes, colours and proportions in all panels; only pose, props and background change. Flat illustration, thin white gutters.
```

## 12 · 节日营销 · holiday-campaign

模型 `gpt-image-2.5-flare` · 尺寸 `1024x1536` · 参考图：图 1 = 第 1 张设定板

```text
Use image 1 as the ONLY identity reference for the mascot "MIKAN 橘咪": keep the exact same character — round mandarin-shaped orange tabby kitten head, green two-leaf sprout on top, big glossy dark eyes, pink blush, cream belly and paws, cream-tipped curled tail, thick dark-brown outline, flat soft cel shading, same proportions. Brand colours: orange #F28C28, cream #FFE9C7, leaf green #6BAA4B, brown #3B2A20.
Mid-Autumn Festival (中秋) holiday marketing poster, vertical: MIKAN mascot holding a mooncake with an orange-shaped pattern, sitting on a crescent moon above a night sky with lanterns and osmanthus flowers, a jade rabbit friend beside. Headline in elegant bold Chinese at top: "中秋 · 橘满月圆", small text bottom "MIKAN TEA 限定礼盒". Warm gold, deep navy and brand orange palette, festive premium illustration.
```
