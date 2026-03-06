# hikariAI - Anime Style Character Specification

**Model:** Animagine XL 4.0 Opt  
**Style:** Modern Anime 2020s  
**Purpose:** AI crypto market scout character for LoRA training

---

## Basic Information

- **Token:** hikariAI
- **Gender:** 1girl
- **Role:** AI crypto market scout who detects trading opportunities early
- **Style Tags:** modern anime style, digital art, illustration

---

## Visual Identity

### Hair
- Short neon blue hair
- Dynamic, slightly spiky anime style
- Subtle glow effect

### Eyes
- Large electric yellow anime eyes (anime proportions)
- Star highlights for sparkle effect
- One eye visible, one covered by cyber visor
- Expressive and energetic

### Face
- Soft anime facial features
- Analytical and energetic expression
- Small anime nose
- Youthful appearance

### Outfit
- Futuristic trading jacket
- Electric blue (#00BFFF) primary
- Neon purple (#9B59FF) accents
- High-tech details with circuit patterns

### Signature Accessory
- Glowing cyber visor over one eye
- Translucent with holographic interface display
- Anime-style tech aesthetic

---

## Color Palette

- **Primary:** Electric blue (#00BFFF)
- **Secondary:** Neon purple (#9B59FF)
- **Tertiary:** Black (#0B0F1A)
- **Lighting:** Cool electric blue and neon purple ambient glow

---

## Environment Elements

- Floating candlestick charts
- Small AI drone assistant hovering nearby
- Price tickers in background
- Holographic trading tablet
- Cyber trading floor atmosphere

---

## Tag-Based Prompt Construction

### Base Character Tags
```
1girl, hikariAI, AI crypto market scout, short neon blue hair, electric yellow eyes, star eye highlights, glowing cyber visor over one eye, soft facial features, analytical expression, energetic, futuristic trading jacket, electric blue and neon purple colors, high-tech outfit
```

### Quality Tags (Always at END)
```
masterpiece, high score, great score, absurdres
```

### Full Positive Prompt Example
```
1girl, hikariAI, AI crypto market scout, short neon blue hair, electric yellow eyes with star highlights, glowing cyber visor over one eye, soft anime facial features, analytical and energetic expression, futuristic trading jacket with electric blue and neon purple colors, high-tech details, holographic trading tablet, small AI drone assistant, floating candlestick charts, price tickers, modern anime style, digital art, masterpiece, high score, great score, absurdres
```

### Negative Prompt
```
lowres, bad anatomy, bad hands, text, error, missing finger, extra digits, fewer digits, cropped, worst quality, low quality, low score, bad score, average score, signature, watermark, username, blurry, 3d render, realistic, photorealistic, western cartoon
```

---

## Dataset Targets

- **Total Images:** 30-40
- **Portrait (40%):** 12-16 images - Focus on face and eye consistency
- **Waist-Up (40%):** 12-16 images - Show outfit and upper body
- **Full Body (20%):** 6-8 images - Include environment elements

---

## Caption Format

**Simple Format (Recommended):**
```
hikariAI, AI crypto market scout
```

**With Pose (Optional):**
```
hikariAI, AI crypto market scout, portrait
```

---

## Settings for Animagine XL 4.0

| Setting | Value |
|---------|-------|
| Model | animagine-xl-4.0-opt.safetensors |
| Resolution | 1024×1024 |
| Sampler | euler_ancestral |
| Steps | 28 |
| CFG Scale | 5 |
| Seed | 0 |
| Batch Size | 2 |

---

## Notes

- **No weight syntax:** Animagine XL 4.0 uses tag ordering, not weighted prompts
- **Tag-based:** Use comma-separated tags, not natural language
- **Quality tags at end:** Always end with `masterpiece, high score, great score, absurdres`
- **Gender tag first:** Always start with `1girl` or `1boy`
- **Modern anime:** Aim for clean, sharp 2020s anime aesthetic
- **Tech fusion:** Balance anime style with futuristic fintech elements

---

## References

- **Anime Skill:** `SKILLS/ANIME_CHARACTER_SKILL.md`
- **Validation:** `SKILLS/ANIME_VALIDATION_GUIDE.md`
- **Templates:** `SKILLS/ANIME_PROMPT_TEMPLATES.md`
