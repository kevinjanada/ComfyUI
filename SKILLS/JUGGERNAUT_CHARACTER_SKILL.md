# JuggernautXL Character Generation Skill

**Version:** 1.0  
**Last Updated:** March 6, 2026  
**Purpose:** Generate consistent character datasets for LoRA training using JuggernautXL v9

---

## Quick Reference Card

| Setting | Value | Notes |
|---------|-------|-------|
| **Model** | Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors | Built-in VAE, no separate VAE needed |
| **Resolution** | 1024×1024 | SDXL native resolution |
| **Sampler** | DPM++ 2M Karras | Best balance of speed/quality |
| **Steps** | 35 | Optimal for JuggernautXL (not 30) |
| **CFG Scale** | 7 | Sweet spot for character consistency |
| **Seed** | -1 | True randomization every run |
| **Batch Size** | 2-4 | Start with 2 for memory safety |

---

## Core Principles

### 1. Identity Token Priority
Always start prompts with your unique character token using light weighting:

```
(CHARACTER_TOKEN:1.2), [role], [physical traits], [outfit], [signature elements]
```

**Why 1.2 weight?** JuggernautXL defaults to photorealistic styles. The weight forces 20% more attention on your character, preventing style drift.

### 2. Token Placement Order (Most → Least Important)

```
1. Unique character token (weighted 1.2)
2. Role/profession
3. Face/hair (weighted 1.1)
4. Outfit/body
5. Signature accessories (weighted 1.1)
6. Art style (stylized 3D fintech character)
7. Pose/action
8. Environment/lighting
```

**Critical:** Never put pose/action before character identity traits!

### 3. The BREAK Technique

Separate **WHO** from **WHAT THEY'RE DOING**:

```
(novatraderAI:1.2), female AI trading analyst, (short silver hair:1.1), (glowing teal eyes:1.1), (circular holographic halo:1.1), black fintech bodysuit BREAK
analyzing holographic candlestick charts, teal lighting, stylized 3D fintech character
```

- **Before BREAK:** Character definition (never changes)
- **After BREAK:** Pose, action, environment (varies per image)

### 4. Style Lock

JuggernautXL will drift toward photorealism unless you explicitly prevent it. Always include:

```
stylized 3D fintech character, highly detailed, sharp focus, professional 3D render
```

And use the enhanced negative prompt (see below) to exclude realistic styles.

---

## Character Identity Template

### Structure

```
(TOKEN:1.2), [ROLE], ([HAIR]:1.1), ([EYES]:1.1), [FACE_STRUCTURE], ([SIGNATURE_ACCESSORY]:1.1), [OUTFIT], BREAK
[ACTION/Pose], [ENVIRONMENT], stylized 3D fintech character, [QUALITY_BOOSTERS]
```

### Example: Nova (Complete)

```
(novatraderAI:1.2), female AI trading analyst, (short silver hair:1.1), (glowing teal eyes:1.1), (circular holographic halo behind head:1.1), black fintech bodysuit with glowing circuit patterns BREAK
portrait shot, minimal background, teal lighting, stylized 3D fintech character, highly detailed, sharp focus, professional 3D render
```

### Example: Athena (Complete)

```
(athenaquantAI:1.2), AI quant strategist, (long platinum hair:1.1), (glowing gold eyes:1.1), (neural crown interface:1.1), white strategist robe with gold accents BREAK
portrait shot, minimal background, gold lighting, stylized 3D fintech character, highly detailed, sharp focus, professional 3D render
```

---

## Negative Prompt (Enhanced - REQUIRED)

**Use this EXACT negative prompt for all JuggernautXL character generation:**

```
low quality, blurry, distorted face, bad anatomy, bad hands, extra fingers, deformed, ugly, duplicate body parts, multiple characters, 2d, flat, painting, drawing, sketch, photorealistic, realistic, oil painting, watercolor, illustration, anime style, manga, cel shaded, inconsistent lighting, asymmetric eyes, disfigured, mutated, poorly drawn face, poorly drawn hands, missing fingers, extra limbs, fused fingers, too many fingers, long neck, cross-eyed, text, watermark, logo, signature
```

**Why this matters:**
- JuggernautXL is trained on photorealistic images
- Without excluding "realistic, photorealistic," you'll get realistic humans instead of stylized 3D characters
- The style exclusions prevent drift toward anime, oil painting, etc.

---

## Dataset Generation Strategy

### Target Composition

| Shot Type | Count | Percentage |
|-----------|-------|------------|
| Portrait | 15 | 37.5% |
| Waist-up | 15 | 37.5% |
| Full-body | 10 | 25% |
| **Total** | **40** | **100%** |

### Generation Workflow

1. **Load workflow** (Nova-Juggernaut or Athena-Juggernaut)
2. **Select pose** from Prompt Templates
3. **Generate 4-6 images** (batch size 2, run 2-3 times)
4. **Review immediately** - delete bad ones
5. **Repeat** for next pose
6. **Stop at 40-50 images** per character
7. **Curate down to 30-40 best**

### Seed Management

- **Workflow seed: -1** (automatic random)
- **Never reuse seeds** for dataset generation
- **Document exceptional seeds** if you find a perfect image (for reference, not reuse)

---

## Common Mistakes & Fixes

### ❌ Mistake: Missing style keywords
```
novatraderAI, female AI trading analyst...  # Wrong - will be realistic
```

### ✅ Fix: Lock the style
```
(novatraderAI:1.2), female AI trading analyst..., stylized 3D fintech character  # Right
```

---

### ❌ Mistake: Short negative prompt
```
bad anatomy, blurry...  # Wrong - Juggernaut will drift to realistic
```

### ✅ Fix: Use full enhanced negative
```
low quality, blurry, ... realistic, photorealistic, ...  # Right - see full version above
```

---

### ❌ Mistake: Wrong token order
```
portrait shot, novatraderAI, female AI trading analyst...  # Wrong - pose before identity
```

### ✅ Fix: Identity first
```
(novatraderAI:1.2), female AI trading analyst..., portrait shot...  # Right
```

---

### ❌ Mistake: Too many weights
```
(novatraderAI:1.5), (female:1.4), (AI:1.3), (trading:1.2)...  # Wrong - over-weighted
```

### ✅ Fix: Light weights only on critical identity
```
(novatraderAI:1.2), female AI trading analyst, (short silver hair:1.1)...  # Right
```

---

## Quality Checklist

Before accepting an image into your dataset, verify:

- [ ] **Identity correct:** Right hair color, eye color, accessories
- [ ] **Style consistent:** Stylized 3D look, not realistic or 2D
- [ ] **No artifacts:** Clean hands, proper face, no deformities
- [ ] **Colors match:** Teal/purple/black for Nova, gold/white/navy for Athena
- [ ] **Signature elements present:** Halo for Nova, crown for Athena
- [ ] **Lighting appropriate:** Teal for Nova, gold for Athena
- [ ] **Single character:** No duplicates or multiple figures
- [ ] **Resolution good:** 1024×1024, not blurry or pixelated

---

## Caption Format for LoRA Training

Each image needs a `.txt` caption file with the same name:

### Simple Caption (Recommended)
```
novatraderAI, female AI trading analyst
```

### Detailed Caption (Optional)
```
novatraderAI, female AI trading analyst, portrait shot, teal lighting
```

**Rules:**
- Keep captions short (under 20 words)
- Always include the character token
- Optional: include pose/action keywords
- Never include quality keywords (masterpiece, highly detailed, etc.)

---

## File Naming Convention

### Generated Images (ComfyUI handles this)
```
nova_juggernaut_00001.png
nova_juggernaut_00002.png
...
```

### Dataset Images (after curation)
```
nova_dataset/
  0001.png
  0001.txt
  0002.png
  0002.txt
  ...
```

---

## Workflow Files

| Workflow | Character | Model | Use Case |
|----------|-----------|-------|----------|
| `01_nova_juggernaut.json` | Nova | JuggernautXL | Primary generation |
| `02_athena_juggernaut.json` | Athena | JuggernautXL | Primary generation |
| `03_nova_sdxl.json` | Nova | SDXL Base | Comparison/testing |
| `04_athena_sdxl.json` | Athena | SDXL Base | Comparison/testing |

**Note:** All workflows pre-configured with optimal settings (Steps: 35, CFG: 7, Seed: -1)

---

## Advanced Tips

### Memory Management (16GB RAM)

If you get OOM errors:
1. Reduce batch size from 2 to 1
2. Restart ComfyUI between character switches
3. Use `--normalvram` flag on startup
4. Close browser tabs during generation

### Iterative Refinement

Don't expect perfect images on first try:
1. Generate 4-6 images per pose
2. Keep 1-2 best, delete rest
3. Adjust prompt slightly if results drift
4. Generate more until you have 30-40 quality images

### Backup Exceptional Seeds

If you generate a "perfect" image, note the seed:
```
# In ComfyUI, check the image metadata or console output
# Document it in a text file for reference
Seed: 12345 - Perfect Nova portrait
```

**Never reuse seeds for dataset** (defeats randomization purpose), but useful for testing.

---

## Troubleshooting

### Problem: Images look realistic instead of stylized 3D
**Solution:** Check negative prompt includes "realistic, photorealistic" and positive includes "stylized 3D fintech character"

### Problem: Character looks different across images
**Solution:** Ensure unique token weight is (TOKEN:1.2) and identity traits are weighted (1.1)

### Problem: Halo/crown missing
**Solution:** Weight the accessory: `(circular holographic halo:1.1)` or `(neural crown interface:1.1)`

### Problem: Wrong colors (purple instead of teal)
**Solution:** Specify color in prompt: `teal lighting (#00F0FF)` and weight if needed: `(teal lighting:1.1)`

### Problem: Hands look bad
**Solution:** Normal for AI. Use waist-up or portrait shots for 70% of dataset. Full-body only when necessary.

---

## Next Steps

1. **Read** `PROMPT_TEMPLATES.md` for ready-to-use pose variations
2. **Reference** `VALIDATION_GUIDE.md` when I validate your prompts
3. **Generate** 40-50 images per character using workflows
4. **Curate** down to 30-40 best images
5. **Create** caption files for each selected image
6. **Organize** into dataset folders
7. **Train** LoRAs using Kohya_ss

---

## Version History

- **v1.0** (2026-03-06) - Initial skill documentation

---

## References

- Prompt Templates: `SKILLS/PROMPT_TEMPLATES.md`
- Validation Guide: `SKILLS/VALIDATION_GUIDE.md`
- Character Specs: `CHARACTERS.md`
- Workflows: `user/default/workflows/`
