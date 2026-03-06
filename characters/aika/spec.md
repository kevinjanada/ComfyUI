# Aika - AI Crypto Analyst (Anime Style Example)

**Token:** aikaAI  
**Gender:** 1girl  
**Role:** AI Crypto Analyst  
**Model:** Animagine XL 4.0 Opt  
**Style:** Modern Anime 2020s

---

## Character Overview

Aika is a calm, analytical AI specialist who monitors cryptocurrency markets and provides trading insights. Her design combines futuristic tech elements with a approachable anime aesthetic.

---

## Visual Identity

### Hair
- **Color:** Short silver white
- **Style:** Slightly spiky with dynamic movement
- **Special Features:** Subtle blue gradient tips
- **Anime Notes:** Clean, modern anime hairstyle

### Eyes (Most Critical!)
- **Color:** Deep purple
- **Style:** Large expressive anime eyes
- **Highlights:** Star-shaped light reflections
- **Anime Notes:** Eyes are the focal point - detailed and expressive

### Face
- **Shape:** Soft with gentle jawline
- **Expression:** Analytical and confident
- **Features:** Small anime nose, soft cheeks
- **Anime Notes:** Youthful, approachable appearance

### Outfit
- **Type:** Futuristic school uniform
- **Primary:** Dark navy blue
- **Secondary:** Silver tech accents
- **Details:** Glowing circuit patterns on sleeves
- **Anime Notes:** Blends traditional uniform with futuristic elements

### Signature Accessory
- **Item:** Holographic data tablet
- **Description:** Floating transparent screen displaying crypto charts
- **Effect:** Purple and blue holographic glow
- **Anime Notes:** Visually striking tech element

---

## Color Palette

- **Primary:** #C0C0C0 (silver white)
- **Secondary:** #9B59B6 (deep purple)
- **Tertiary:** #0B0F1A (dark navy)
- **Lighting:** Cool silver and purple ambient glow

---

## Environment Elements

- [x] Floating holographic data screens
- [x] Crypto price ticker displays
- [x] Small AI assistant icon
- [ ] Blockchain network visualizations

---

## Complete Prompt Examples

### Portrait Pose
```
1girl, aikaAI, AI crypto analyst, short silver white hair, deep purple eyes with star highlights, soft facial features, analytical and confident expression, futuristic school uniform with dark navy and silver accents, glowing circuit patterns on sleeves, holographic data tablet, portrait, upper body, looking at viewer, minimal background, modern anime style, digital art, masterpiece, high score, great score, absurdres
```

### Standing Pose
```
1girl, aikaAI, AI crypto analyst, short silver white hair, deep purple eyes with star highlights, soft facial features, analytical and confident expression, futuristic school uniform with dark navy and silver accents, glowing circuit patterns on sleeves, holographic data tablet, standing, confident pose, waist up, professional stance, floating holographic data screens, crypto price tickers, modern anime style, digital art, masterpiece, high score, great score, absurdres
```

### Action Pose
```
1girl, aikaAI, AI crypto analyst, short silver white hair, deep purple eyes with star highlights, soft facial features, focused expression, futuristic school uniform with dark navy and silver accents, glowing circuit patterns on sleeves, holographic data tablet, analyzing crypto charts, dynamic pose, interacting with holographic interface, floating data screens, crypto market data, small AI assistant icon, modern anime style, digital art, masterpiece, high score, great score, absurdres
```

---

## Negative Prompt

```
lowres, bad anatomy, bad hands, text, error, missing finger, extra digits, fewer digits, cropped, worst quality, low quality, low score, bad score, average score, signature, watermark, username, blurry, 3d render, realistic, photorealistic, western cartoon
```

---

## Settings

| Setting | Value |
|---------|-------|
| Model | animagine-xl-4.0-opt.safetensors |
| Resolution | 1024×1024 |
| Sampler | euler_ancestral |
| Steps | 28 |
| CFG | 5 |
| Seed | 0 |
| Batch Size | 2 |

---

## Workflow Files

- `aika_portrait_animagine.json` - Portrait workflow
- `aika_standing_animagine.json` - Standing workflow
- `aika_action_animagine.json` - Action workflow

Load these in ComfyUI to generate Aika images.

---

## Dataset Targets

- **Total:** 30-40 images
- **Portrait (40%):** 12-16 images
- **Waist-Up (40%):** 12-16 images
- **Full Body (20%):** 6-8 images

---

## Caption Format

**Simple:**
```
aikaAI, AI crypto analyst
```

**With Pose:**
```
aikaAI, AI crypto analyst, portrait
```

---

## Usage Example

1. Load workflow in ComfyUI
2. Check settings (Steps=28, CFG=5, Euler Ancestral)
3. Generate 2 test images
4. If quality good, generate full dataset
5. Create caption files
6. Train LoRA

---

## References

- **Skill Guide:** `SKILLS/ANIME_CHARACTER_SKILL.md`
- **Prompt Templates:** `SKILLS/ANIME_PROMPT_TEMPLATES.md`
- **Validation:** `SKILLS/ANIME_VALIDATION_GUIDE.md`
