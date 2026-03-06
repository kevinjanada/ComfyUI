# Animagine XL 4.0 Anime Character Generation Skill

**Version:** 1.0  
**Last Updated:** March 6, 2026  
**Purpose:** Generate consistent anime-style character datasets for LoRA training using Animagine XL 4.0

---

## ⚡ Quick Reference Card

| Setting | Value | Notes |
|---------|-------|-------|
| **Model** | animagine-xl-4.0-opt.safetensors | Optimized version, ~6.5GB |
| **Download** | https://huggingface.co/cagliostrolab/animagine-xl-4.0 | Place in `models/checkpoints/` |
| **Resolution** | 1024×1024 | Native SDXL (supports multiple aspects) |
| **Sampler** | Euler Ancestral (Euler a) | Recommended for anime |
| **Steps** | 28 | Optimal (25-28 range) |
| **CFG Scale** | 5 | Sweet spot (4-7 range) |
| **Seed** | 0 | Start at 0, increment manually |
| **Batch Size** | 2 | Memory safe with 16GB RAM |

---

## Model Installation

### Download Animagine XL 4.0 Opt

```bash
# Navigate to ComfyUI checkpoints directory
cd /home/kevin/ComfyUI/models/checkpoints

# Download the model (~6.5GB)
wget -c "https://huggingface.co/cagliostrolab/animagine-xl-4.0/resolve/main/animagine-xl-4.0.safetensors" -O animagine-xl-4.0-opt.safetensors
```

**Alternative:** Download via browser from [HuggingFace](https://huggingface.co/cagliostrolab/animagine-xl-4.0) and place in `models/checkpoints/`

### Why Animagine XL 4.0?

**Key Improvements over 3.0:**
- **8.4M training images** (vs 1.2M in 3.0)
- **Better stability** with Opt version
- **Enhanced anatomy accuracy**
- **Fixed color saturation** (richer colors)
- **Reduced noise and artifacts**
- **Superior anime + tech fusion** (perfect for fintech characters!)

---

## Core Principles

### 1. Tag-Based Prompting (NOT Natural Language)

Animagine XL 4.0 was trained with **tag-based captions**, not natural language. Use comma-separated tags:

**❌ WRONG (Natural Language):**
```
A girl with short blue hair wearing a futuristic jacket
```

**✅ CORRECT (Tag-Based):**
```
1girl, short blue hair, futuristic jacket
```

### 2. Prompt Structure (Exact Order)

```
1girl/1boy, character_token, role, visual_traits, pose_environment, style_tags, quality_tags
```

**Breakdown:**
1. **Gender tag first:** `1girl` or `1boy` (REQUIRED)
2. **Character token:** Your unique identifier
3. **Role:** Profession/job
4. **Visual traits:** Hair, eyes, outfit, accessories
5. **Pose/Environment:** Action and setting
6. **Style tags:** `modern anime style, digital art`
7. **Quality tags at END:** `masterpiece, high score, great score, absurdres`

### 3. NO Weight Syntax

**❌ WRONG:**
```
1girl, (hikariAI:1.2), short blue hair
```

**✅ CORRECT:**
```
1girl, hikariAI, short blue hair
```

Animagine XL 4.0 uses **tag ordering** for emphasis, not weighted syntax.

### 4. Quality Tags (Always at End)

Add these quality enhancement tags at the END of every prompt:

```
masterpiece, high score, great score, absurdres
```

**What they do:**
- `masterpiece` - Highest quality tier (>150 score)
- `high score` - High aesthetic quality (100-150)
- `great score` - Great quality (75-100)
- `absurdres` - High resolution

### 5. Style Lock

Prevent style drift with explicit anime style tags:

```
modern anime style, digital art, illustration
```

---

## Character Identity Template

### Basic Structure

```
1girl, TOKEN, ROLE, HAIR, EYES, FACE, OUTFIT, ACCESSORY, POSE, ENVIRONMENT, STYLE, QUALITY
```

### Example: hikariAI (Complete)

**Character Definition:**
```
1girl, hikariAI, AI crypto market scout, short neon blue hair, electric yellow eyes with star highlights, glowing cyber visor over one eye, soft anime facial features, analytical and energetic expression, futuristic trading jacket with electric blue and neon purple colors
```

**Full Portrait Prompt:**
```
1girl, hikariAI, AI crypto market scout, short neon blue hair, electric yellow eyes with star highlights, glowing cyber visor over one eye, soft anime facial features, analytical and energetic expression, futuristic trading jacket with electric blue and neon purple colors, high-tech details, portrait, upper body, looking at viewer, minimal background, modern anime style, digital art, masterpiece, high score, great score, absurdres
```

---

## Negative Prompt (REQUIRED)

Use this **exact** negative prompt for all generations:

```
lowres, bad anatomy, bad hands, text, error, missing finger, extra digits, fewer digits, cropped, worst quality, low quality, low score, bad score, average score, signature, watermark, username, blurry, 3d render, realistic, photorealistic, western cartoon
```

**Key exclusions:**
- `3d render` - Prevents 3D CG look
- `realistic, photorealistic` - Keeps anime style
- `western cartoon` - Avoids Disney/Pixar style

---

## Recommended Settings

### Optimal Configuration

| Parameter | Value | Range | Notes |
|-----------|-------|-------|-------|
| **Model** | animagine-xl-4.0-opt.safetensors | - | Optimized version |
| **Resolution** | 1024×1024 | 640×1536 to 1536×640 | Native is 1:1 |
| **Sampler** | euler_ancestral | euler, dpm++ 2M | Euler a recommended |
| **Steps** | 28 | 25-28 | Higher doesn't improve quality |
| **CFG Scale** | 5 | 4-7 | Lower = more artistic freedom |
| **Seed** | 0 | 0-999999 | Start at 0, manually increment |
| **Batch Size** | 2 | 1-4 | Start with 2 for memory |

### Resolution Options

Animagine XL 4.0 supports multiple aspect ratios:

| Orientation | Dimensions | Aspect | Use Case |
|-------------|------------|--------|----------|
| Square | 1024×1024 | 1:1 | Standard portraits |
| Landscape | 1152×896 | 9:7 | Wide shots |
| Landscape | 1216×832 | 3:2 | Cinematic |
| Portrait | 896×1152 | 7:9 | Tall characters |
| Portrait | 832×1216 | 2:3 | Full body |

**Recommendation:** Use 1024×1024 for consistency training.

---

## Dataset Generation Strategy

### Image Distribution for LoRA Training

**Total Target:** 30-40 images per character

| Pose Type | Percentage | Count | Priority |
|-----------|-----------|-------|----------|
| **Portrait** | 40% | 12-16 | HIGHEST - Face consistency |
| **Waist-Up** | 40% | 12-16 | HIGH - Show outfit details |
| **Full Body** | 20% | 6-8 | MEDIUM - Environmental context |

### Why This Ratio?

1. **Portrait (40%):** Face consistency is most critical for character recognition
2. **Waist-Up (40%):** Shows outfit without hand generation issues
3. **Full Body (20%):** Context shots but prone to anatomy errors

### Generation Order

1. **Start with Portrait** - Establish face consistency first
2. **Standing poses** - Build outfit recognition
3. **Action poses** - Add variety
4. **Full body last** - When settings are dialed in

---

## Caption Format for LoRA Training

### Simple Format (Recommended)

```
TOKEN, role
```

**Example:**
```
hikariAI, AI crypto market scout
```

### With Pose (Optional)

```
TOKEN, role, pose_keyword
```

**Example:**
```
hikariAI, AI crypto market scout, portrait
```

**Rules:**
- Always include TOKEN first
- Keep under 10 words
- Don't include quality tags (masterpiece, etc.)
- Don't include style tags (anime style, etc.)

---

## Workflow Structure

### Required ComfyUI Nodes

1. **CheckpointLoaderSimple** - Load animagine-xl-4.0-opt
2. **CLIPTextEncode (Positive)** - Tag-based character prompt
3. **CLIPTextEncode (Negative)** - Anime negative prompt
4. **EmptyLatentImage** - 1024×1024, batch 2
5. **KSampler** - Euler a, 28 steps, CFG 5, seed -1
6. **VAEDecode** - Decode latent to image
7. **SaveImage** - Save with naming convention

### Example Workflow JSON

See: `/user/default/workflows/hikariAI_portrait_animagine.json`

---

## Special Features

### Score Tags

Control quality more precisely with score tags:

| Tag | Score Range | Effect |
|-----|-------------|---------|
| `masterpiece` | >150 | Highest quality |
| `high score` | 100-150 | High quality |
| `great score` | 75-100 | Great quality |
| `average score` | 0-75 | Average |
| `low score` | -5-0 | Low quality |
| `bad score` | <-5 | Poor quality |

**Usage:** Add to positive prompt for quality boost, or negative to exclude.

### Year/Temporal Tags

Control anime art style era:

| Tag | Year Range | Style |
|-----|------------|-------|
| `newest` | 2022-2025 | Modern clean style |
| `late` | 2019-2021 | Recent style |
| `mid` | 2015-2018 | Mid-2010s |
| `early` | 2011-2014 | Early 2010s |
| `oldest` | 2005-2010 | 2000s style |

**Recommendation:** Use `newest` for modern 2020s anime look.

---

## Common Mistakes to Avoid

### 1. Using Weight Syntax
**❌** `1girl, (hikariAI:1.2), blue hair`  
**✅** `1girl, hikariAI, blue hair`

### 2. Natural Language
**❌** `A girl with blue hair`  
**✅** `1girl, blue hair`

### 3. Missing Quality Tags
**❌** `1girl, hikariAI, blue hair`  
**✅** `1girl, hikariAI, blue hair, masterpiece, high score, great score, absurdres`

### 4. Wrong Negative Prompt
**❌** Using JuggernautXL negative (includes photorealistic exclusions)  
**✅** Use anime-specific negative (provided above)

### 5. Too Many Steps
**❌** 35+ steps (wastes time, no improvement)  
**✅** 25-28 steps (optimal)

### 6. CFG Too High
**❌** CFG 7+ (can cause artifacts)  
**✅** CFG 4-5 (recommended)

---

## Limitations

1. **Tag-based only** - Natural language prompts don't work well
2. **Hand anatomy** - May struggle with complex hand poses (common in all models)
3. **Text rendering** - Cannot generate readable text in images
4. **Multiple characters** - Single character per image works best
5. **Recent characters** - Very new anime characters may not be recognized
6. **Style consistency** - Focuses more on identity than specific art styles

---

## Troubleshooting

### Images Look Too Realistic
- Check negative prompt includes `realistic, photorealistic, 3d render`
- Add `anime style, illustration` to positive prompt
- Ensure CFG isn't too high (try 4-5)

### Inconsistent Character Faces
- Generate more portrait shots first (40% of dataset)
- Ensure token is consistent across all prompts
- Use same quality tags every time

### Poor Image Quality
- Verify quality tags at end of prompt
- Check steps (should be 25-28, not lower)
- Ensure using Euler Ancestral sampler

### Memory Issues
- Reduce batch size to 1
- Use `--normalvram --cache-ram 4 --disable-smart-memory` flags
- Close other applications

---

## File References

- **Character Spec Template:** `SKILLS/ANIME_CHARACTER_SPEC_TEMPLATE.md`
- **Workflow Generator:** `SKILLS/ANIME_WORKFLOW_GENERATOR_PROMPT.md`
- **Validation Guide:** `SKILLS/ANIME_VALIDATION_GUIDE.md`
- **Pose Templates:** `SKILLS/ANIME_PROMPT_TEMPLATES.md`
- **Example Characters:** `characters/hikariAI/`, `characters/aika/`, `SKILLS/examples/anime/aika/`

---

## Comparison: Anime vs JuggernautXL

| Feature | Animagine XL 4.0 | JuggernautXL v9 |
|---------|------------------|-----------------|
| **Style** | Anime/Manga | Stylized 3D |
| **Prompt Type** | Tag-based | Natural language |
| **Weight Syntax** | ❌ Not used | ✅ `(token:1.2)` |
| **BREAK** | ❌ Not used | ✅ Required |
| **Steps** | 25-28 | 35 |
| **CFG** | 4-5 | 7 |
| **Sampler** | Euler Ancestral | DPM++ 2M |
| **Quality Tags** | End of prompt | Throughout |
| **Best For** | Anime characters | 3D stylized characters |

---

## Ready to Generate?

1. **Download model** (if not done)
2. **Fill character spec** using `ANIME_CHARACTER_SPEC_TEMPLATE.md`
3. **Generate workflows** using `ANIME_WORKFLOW_GENERATOR_PROMPT.md`
4. **Validate** using `ANIME_VALIDATION_GUIDE.md`
5. **Generate 30-40 images** following dataset targets
6. **Create captions** and train LoRA

**Example characters ready to use:**
- `hikariAI` - AI crypto market scout (see `characters/hikariAI/`)
- `aika` - Crypto analyst (see `characters/aika/`)
- `luna` - 3D stylized example (see `characters/luna/`)
- Also see: `SKILLS/examples/anime/aika/` (reference examples)

**Let's create your anime character!**
