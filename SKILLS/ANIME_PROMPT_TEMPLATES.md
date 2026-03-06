# Anime Pose Prompt Templates (Animagine XL 4.0)

**Version:** 1.0  
**Purpose:** Pre-built anime pose variations for consistent character generation

---

## How to Use These Templates

1. **Copy the template** for your desired pose
2. **Replace placeholders** with your character's details:
   - `[GENDER]` → `1girl` or `1boy`
   - `[TOKEN]` → Your character token (e.g., `hikariAI`)
   - `[ROLE]` → Character's profession
   - `[HAIR]` → Hair description
   - `[EYES]` → Eyes description
   - `[FACE]` → Face features
   - `[OUTFIT]` → Outfit description
   - `[ACCESSORY]` → Signature accessory
   - `[ENVIRONMENT]` → Background elements
3. **Add quality tags at END:** `masterpiece, high score, great score, absurdres`
4. **Use exact anime negative prompt**

---

## 7 Standard Anime Poses

### 1. PORTRAIT (Priority: HIGHEST - 40% of dataset)

**Use case:** Profile pictures, avatar consistency, face training

**Prompt Template:**
```
[GENDER], [TOKEN], [ROLE], [HAIR], [EYES], [FACE], [OUTFIT], [ACCESSORY], portrait, upper body, looking at viewer, minimal background, modern anime style, digital art, masterpiece, high score, great score, absurdres
```

**Example (hikariAI):**
```
1girl, hikariAI, AI crypto market scout, short neon blue hair, electric yellow eyes with star highlights, soft anime facial features, analytical and energetic expression, futuristic trading jacket with electric blue and neon purple colors, glowing cyber visor over one eye, portrait, upper body, looking at viewer, minimal background, modern anime style, digital art, masterpiece, high score, great score, absurdres
```

**Variations:**
- **Expression variations:** `smile`, `serious expression`, `determined look`
- **Angle variations:** `slight smile`, `neutral expression`, `confident gaze`
- **Background:** `minimal background`, `gradient background`, `soft bokeh`

**Target:** 12-16 images (40% of dataset)

---

### 2. STANDING CONFIDENT (Priority: HIGH - 20% of dataset)

**Use case:** Hero shots, professional presence, outfit display

**Prompt Template:**
```
[GENDER], [TOKEN], [ROLE], [HAIR], [EYES], [FACE], [OUTFIT], [ACCESSORY], standing, confident pose, waist up, professional stance, hands on hips or at sides, [ENVIRONMENT], modern anime style, digital art, masterpiece, high score, great score, absurdres
```

**Example (hikariAI):**
```
1girl, hikariAI, AI crypto market scout, short neon blue hair, electric yellow eyes with star highlights, soft anime facial features, analytical and energetic expression, futuristic trading jacket with electric blue and neon purple colors, glowing cyber visor over one eye, standing, confident pose, waist up, professional stance, holographic trading tablet, small AI drone assistant, modern anime style, digital art, masterpiece, high score, great score, absurdres
```

**Variations:**
- **Pose:** `arms crossed`, `hand on hip`, `relaxed stance`
- **Expression:** `confident smile`, `professional look`, `determined`
- **Props:** `holding tablet`, `arms at sides`, `adjusting visor`

**Target:** 12-16 images (40% of dataset)

---

### 3. ACTION/PROFESSIONAL (Priority: HIGH - 20% of dataset)

**Use case:** Context shots, storytelling, showing profession

**Prompt Template:**
```
[GENDER], [TOKEN], [ROLE], [HAIR], [EYES], [FACE], [OUTFIT], [ACCESSORY], analyzing data, dynamic pose, interacting with holographic interface, [ENVIRONMENT], professional action, focused expression, modern anime style, digital art, masterpiece, high score, great score, absurdres
```

**Example (hikariAI):**
```
1girl, hikariAI, AI crypto market scout, short neon blue hair, electric yellow eyes with star highlights, soft anime facial features, analytical and energetic expression, futuristic trading jacket with electric blue and neon purple colors, glowing cyber visor over one eye, analyzing crypto data, dynamic pose, interacting with holographic interface, floating candlestick charts, small AI drone assistant, price tickers, futuristic trading floor, focused expression, modern anime style, digital art, masterpiece, high score, great score, absurdres
```

**Variations:**
- **Action:** `typing on holographic keyboard`, `pointing at data`, `monitoring screens`
- **Expression:** `focused`, `concentrated`, `analytical`
- **Dynamic:** `leaning forward`, `slight movement`, `engaged posture`

**Target:** 6-8 images (20% of dataset)

---

### 4. SIDE PROFILE (Priority: MEDIUM - 10% of dataset)

**Use case:** Face consistency from angles, variety

**Prompt Template:**
```
[GENDER], [TOKEN], [ROLE], [HAIR], [EYES], [FACE], [OUTFIT], [ACCESSORY], profile, looking to side, side view, [ENVIRONMENT], modern anime style, digital art, masterpiece, high score, great score, absurdres
```

**Example (hikariAI):**
```
1girl, hikariAI, AI crypto market scout, short neon blue hair, electric yellow eyes with star highlights, soft anime facial features, analytical expression, futuristic trading jacket with electric blue and neon purple colors, glowing cyber visor over one eye, profile, looking to side, side view, monitoring data displays, modern anime style, digital art, masterpiece, high score, great score, absurdres
```

**Variations:**
- **Direction:** `looking left`, `looking right`
- **Expression:** `focused profile`, `calm profile`, `observant`
- **Background:** `minimal background`, `tech displays in background`

**Target:** 3-4 images (10% of dataset)

---

### 5. THREE-QUARTER VIEW (Priority: MEDIUM - 5% of dataset)

**Use case:** Dynamic portraits, artistic variety

**Prompt Template:**
```
[GENDER], [TOKEN], [ROLE], [HAIR], [EYES], [FACE], [OUTFIT], [ACCESSORY], three-quarter view, turned slightly, dynamic angle, [ENVIRONMENT], modern anime style, digital art, masterpiece, high score, great score, absurdres
```

**Example (hikariAI):**
```
1girl, hikariAI, AI crypto market scout, short neon blue hair, electric yellow eyes with star highlights, soft anime facial features, energetic expression, futuristic trading jacket with electric blue and neon purple colors, glowing cyber visor over one eye, three-quarter view, turned slightly, dynamic angle, standing in trading environment, modern anime style, digital art, masterpiece, high score, great score, absurdres
```

**Variations:**
- **Angle:** `45 degree angle`, `slightly turned`, `three-quarter portrait`
- **Expression:** `engaging look`, `welcoming`, `professional`
- **Background:** `soft gradient`, `tech ambient`

**Target:** 2-3 images (5% of dataset)

---

### 6. ENVIRONMENTAL/FULL BODY (Priority: LOW - 5% of dataset)

**Use case:** Establishing shots, world-building, complete character

**Prompt Template:**
```
[GENDER], [TOKEN], [ROLE], [HAIR], [EYES], [FACE], [OUTFIT], [ACCESSORY], full body, standing, complete outfit visible, [ENVIRONMENT], wide shot, modern anime style, digital art, masterpiece, high score, great score, absurdres
```

**Example (hikariAI):**
```
1girl, hikariAI, AI crypto market scout, short neon blue hair, electric yellow eyes with star highlights, soft anime facial features, analytical and energetic expression, futuristic trading jacket with electric blue and neon purple colors, glowing cyber visor over one eye, full body, standing, complete outfit visible, futuristic trading floor, floating candlestick charts, small AI drone assistant, price tickers, holographic displays, wide shot, modern anime style, digital art, masterpiece, high score, great score, absurdres
```

**Variations:**
- **Pose:** `standing confidently`, `walking`, `casual stance`
- **Environment:** `trading floor`, `tech office`, `data center`
- **Scale:** `wide shot`, `establishing shot`, `full scene`

**Target:** 2-3 images (5% of dataset)

**Note:** Use sparingly - full body most prone to anatomy issues

---

### 7. DETAIL FOCUS (Priority: LOW - 0-5% of dataset)

**Use case:** Accessory consistency, eye detail, emphasis

**Option A: Eye Focus**
```
[GENDER], [TOKEN], [ROLE], [HAIR], [EYES], close-up, eye focus, detailed eyes, anime eye highlights, sparkling eyes, [ACCESSORY] visible, modern anime style, digital art, masterpiece, high score, great score, absurdres
```

**Option B: Accessory Focus**
```
[GENDER], [TOKEN], [ROLE], [HAIR], [ACCESSORY], close-up, accessory focus, detailed [ACCESSORY], [ENVIRONMENT] blurred, modern anime style, digital art, masterpiece, high score, great score, absurdres
```

**Example (hikariAI - Eye Focus):**
```
1girl, hikariAI, AI crypto market scout, short neon blue hair, electric yellow eyes with star highlights, close-up, eye focus, detailed eyes, anime eye highlights, sparkling eyes, glowing cyber visor visible, modern anime style, digital art, masterpiece, high score, great score, absurdres
```

**Example (hikariAI - Accessory Focus):**
```
1girl, hikariAI, AI crypto market scout, short neon blue hair, glowing cyber visor over one eye, close-up, accessory focus, detailed cyber visor, holographic interface display, trading floor blurred background, modern anime style, digital art, masterpiece, high score, great score, absurdres
```

**Variations:**
- **Focus:** `extreme close-up`, `detail shot`, `macro`
- **Subject:** `eyes`, `accessory`, `face details`
- **Effect:** `soft bokeh background`, `sharp focus`

**Target:** 0-2 images (optional, 0-5% of dataset)

---

## Complete Example: All 7 Poses for hikariAI

### 1. Portrait
```
1girl, hikariAI, AI crypto market scout, short neon blue hair, electric yellow eyes with star highlights, soft anime facial features, analytical and energetic expression, futuristic trading jacket with electric blue and neon purple colors, glowing cyber visor over one eye, portrait, upper body, looking at viewer, minimal background, modern anime style, digital art, masterpiece, high score, great score, absurdres
```

### 2. Standing
```
1girl, hikariAI, AI crypto market scout, short neon blue hair, electric yellow eyes with star highlights, soft anime facial features, analytical and energetic expression, futuristic trading jacket with electric blue and neon purple colors, glowing cyber visor over one eye, standing, confident pose, waist up, professional stance, holographic trading tablet, small AI drone assistant, modern anime style, digital art, masterpiece, high score, great score, absurdres
```

### 3. Action
```
1girl, hikariAI, AI crypto market scout, short neon blue hair, electric yellow eyes with star highlights, soft anime facial features, analytical and energetic expression, futuristic trading jacket with electric blue and neon purple colors, glowing cyber visor over one eye, analyzing crypto data, dynamic pose, interacting with holographic interface, floating candlestick charts, small AI drone assistant, price tickers, futuristic trading floor, focused expression, modern anime style, digital art, masterpiece, high score, great score, absurdres
```

### 4. Profile
```
1girl, hikariAI, AI crypto market scout, short neon blue hair, electric yellow eyes with star highlights, soft anime facial features, analytical expression, futuristic trading jacket with electric blue and neon purple colors, glowing cyber visor over one eye, profile, looking to side, side view, monitoring data displays, modern anime style, digital art, masterpiece, high score, great score, absurdres
```

### 5. Three-Quarter
```
1girl, hikariAI, AI crypto market scout, short neon blue hair, electric yellow eyes with star highlights, soft anime facial features, energetic expression, futuristic trading jacket with electric blue and neon purple colors, glowing cyber visor over one eye, three-quarter view, turned slightly, dynamic angle, standing in trading environment, modern anime style, digital art, masterpiece, high score, great score, absurdres
```

### 6. Full Body
```
1girl, hikariAI, AI crypto market scout, short neon blue hair, electric yellow eyes with star highlights, soft anime facial features, analytical and energetic expression, futuristic trading jacket with electric blue and neon purple colors, glowing cyber visor over one eye, full body, standing, complete outfit visible, futuristic trading floor, floating candlestick charts, small AI drone assistant, price tickers, holographic displays, wide shot, modern anime style, digital art, masterpiece, high score, great score, absurdres
```

### 7. Detail
```
1girl, hikariAI, AI crypto market scout, short neon blue hair, electric yellow eyes with star highlights, close-up, eye focus, detailed eyes, anime eye highlights, sparkling eyes, glowing cyber visor visible, modern anime style, digital art, masterpiece, high score, great score, absurdres
```

---

## Dataset Distribution Summary

| Pose | Priority | Target Count | Percentage |
|------|----------|--------------|------------|
| **Portrait** | HIGHEST | 12-16 | 40% |
| **Standing** | HIGH | 12-16 | 40% |
| **Action** | HIGH | 6-8 | 20% |
| **Profile** | MEDIUM | 3-4 | 10% |
| **Three-Quarter** | MEDIUM | 2-3 | 5% |
| **Full Body** | LOW | 2-3 | 5% |
| **Detail** | LOW | 0-2 | 0-5% |
| **TOTAL** | - | **30-40** | **100%** |

**Note:** The 7 poses above add up to >100% because Detail is optional. Adjust based on your needs, but maintain 40% portrait minimum.

---

## Tips for Best Results

### 1. Start with Portrait
- Generate portrait images first
- Establish consistent face and eyes
- Use as reference for other poses

### 2. Vary Expressions
- Same pose, different expressions
- Portrait: `smile`, `serious`, `determined`
- Standing: `confident`, `professional`, `focused`

### 3. Vary Backgrounds
- Portrait: `minimal background`, `gradient`, `soft bokeh`
- Environmental: Include tech elements
- Keep backgrounds simple for character focus

### 4. Maintain Consistency
- Same hair color in all prompts
- Same eye color in all prompts
- Same outfit description in all prompts
- Same accessory in all prompts

### 5. Use Style Tags
- Always include: `modern anime style, digital art`
- Optional: `newest` (for modern 2020s look)
- Optional: `year 2023` (for specific era)

---

## Anime Expression Tags

Add these to vary character expressions:

**Positive/Active:**
- `smile`, `happy`, `excited`, `energetic`
- `confident`, `determined`, `motivated`
- `laughing`, `cheerful`, `bright expression`

**Neutral/Professional:**
- `neutral expression`, `calm`, `composed`
- `focused`, `concentrated`, `analytical`
- `professional`, `serious`, `business-like`

**Cool/Stoic:**
- `cool expression`, `stoic`, `collected`
- `slight smile`, `mysterious`, `intriguing`

**Avoid for Consistency:**
- Extreme expressions (`crying`, `shouting`, `angry`)
- These can make character unrecognizable

---

## Anime Background Tags

**Minimal:**
- `minimal background`, `simple background`, `gradient background`
- `white background`, `solid color background`

**Tech/Professional:**
- `futuristic office`, `tech environment`, `data center`
- `holographic displays`, `digital screens`, `neon lights`

**Abstract:**
- `soft bokeh`, `abstract background`, `colorful gradient`
- `glowing particles`, `digital rain`, `cyber atmosphere`

**Specific:**
- `trading floor`, `control room`, `server room`
- `futuristic city`, `cyberpunk setting`

---

## Negative Prompt (Use for ALL Poses)

```
lowres, bad anatomy, bad hands, text, error, missing finger, extra digits, fewer digits, cropped, worst quality, low quality, low score, bad score, average score, signature, watermark, username, blurry, 3d render, realistic, photorealistic, western cartoon
```

---

## Settings (Use for ALL Poses)

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

## Caption Format

**Simple (Recommended):**
```
TOKEN, role
```

**With Pose (Optional):**
```
TOKEN, role, pose_keyword
```

**Example:**
```
hikariAI, AI crypto market scout
hikariAI, AI crypto market scout, portrait
```

---

## References

- **Anime Skill:** `SKILLS/ANIME_CHARACTER_SKILL.md`
- **Workflow Generator:** `SKILLS/ANIME_WORKFLOW_GENERATOR_PROMPT.md`
- **Validation Guide:** `SKILLS/ANIME_VALIDATION_GUIDE.md`
- **Spec Template:** `SKILLS/ANIME_CHARACTER_SPEC_TEMPLATE.md`
- **Example Characters:** `characters/hikariAI/`, `characters/aika/`, `SKILLS/examples/anime/aika/`

---

**Ready to generate?** Pick a pose template, customize it for your character, and start generating!
