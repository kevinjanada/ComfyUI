# JuggernautXL Character Generation Validation Guide

**Purpose:** Active validation rules I follow when helping you generate characters with JuggernautXL

---

## Pre-Generation Validation Checklist

### 1. Character Identity Verification

**Required Elements (Must Be Present):**

- [ ] **Unique character token** with weight: `(TOKEN:1.2)`
- [ ] **Role/profession** clearly stated
- [ ] **Hair description** with weight: `([hair]:1.1)`
- [ ] **Eye description** with weight: `([eyes]:1.1)`
- [ ] **Signature accessory** with weight: `([accessory]:1.1)`
- [ ] **Outfit description**
- [ ] **BREAK keyword** separating identity from action
- [ ] **Pose/action** after BREAK
- [ ] **Art style** keyword: `stylized 3D fintech character`
- [ ] **Quality boosters:** `highly detailed, sharp focus, professional 3D render`

**Validation:** I will check each element and warn if any are missing

---

### 2. Prompt Structure Validation

**Correct Order (Identity → Action):**

```
✅ GOOD:
(novatraderAI:1.2), female AI trading analyst, (short silver hair:1.1), (glowing teal eyes:1.1), (circular holographic halo:1.1), black fintech bodysuit BREAK
portrait shot, teal lighting, stylized 3D fintech character, highly detailed, sharp focus

❌ BAD:
portrait shot, novatraderAI, female AI trading analyst...  # Pose before identity!
```

**Validation:** I verify the character token appears in the first 10 words

---

### 3. Weighting Validation

**Correct Weighting Pattern:**

- **Character token:** `(TOKEN:1.2)` - Required
- **Critical identity traits:** `(trait:1.1)` - Recommended for hair, eyes, accessories
- **Other elements:** No weighting - Normal importance

**Validation:**
- [ ] Character token has `:1.2` weight
- [ ] No element has weight > 1.3 (over-weighting)
- [ ] No more than 4 weighted elements per prompt

**Warnings I will issue:**
- "Missing weight on character token - recommend (TOKEN:1.2)"
- "Too many weighted elements - may cause inconsistency"
- "Over-weighted element (>1.3) - suggest reducing to 1.1-1.2"

---

### 4. Negative Prompt Validation

**Required Negative Prompt Elements:**

Must include ALL of these categories:

**Quality exclusions:**
- `low quality`, `blurry`, `distorted face`, `deformed`

**Anatomy exclusions:**
- `bad anatomy`, `bad hands`, `extra fingers`, `duplicate body parts`

**Style drift prevention (CRITICAL for JuggernautXL):**
- `realistic`, `photorealistic`, `2d`, `flat`, `painting`, `drawing`, `sketch`
- `oil painting`, `watercolor`, `illustration`, `anime style`, `manga`

**Other exclusions:**
- `multiple characters`, `text`, `watermark`, `logo`

**Complete Required Negative Prompt:**
```
low quality, blurry, distorted face, bad anatomy, bad hands, extra fingers, deformed, ugly, duplicate body parts, multiple characters, 2d, flat, painting, drawing, sketch, photorealistic, realistic, oil painting, watercolor, illustration, anime style, manga, cel shaded, inconsistent lighting, asymmetric eyes, disfigured, mutated, poorly drawn face, poorly drawn hands, missing fingers, extra limbs, fused fingers, too many fingers, long neck, cross-eyed, text, watermark, logo, signature
```

**Validation:** I will verify the negative prompt contains at minimum:
- Quality exclusions ✓
- Anatomy exclusions ✓
- `realistic` or `photorealistic` ✓ (CRITICAL)
- `2d` or `flat` or `painting` ✓ (style protection)

---

### 5. Settings Validation

**Required Settings for JuggernautXL:**

| Setting | Correct Value | Validation |
|---------|---------------|------------|
| **Model** | Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors | Check checkpoint node |
| **Resolution** | 1024×1024 | Verify EmptyLatentImage node |
| **Sampler** | dpmpp_2m | Check KSampler node |
| **Scheduler** | karras | Check KSampler node |
| **Steps** | 35 | Check KSampler (not 30) |
| **CFG** | 7 | Check KSampler (not 6) |
| **Seed** | -1 or "randomize" | Check KSampler node |
| **Batch Size** | 2-4 | Check EmptyLatentImage |

**Validation:** I will verify each setting matches the skill requirements

---

### 6. Style Consistency Validation

**Required Style Keywords (Must Appear):**
- `stylized 3D fintech character`
- `highly detailed`
- `sharp focus`
- `professional 3D render`

**Prohibited Style Keywords (Must NOT Appear in Positive Prompt):**
- `realistic`, `photorealistic` (belongs in negative!)
- `oil painting`, `watercolor`
- `anime`, `manga`, `cel shaded`
- `2d`, `flat`, `sketch`, `drawing`

**Validation:** I check that style keywords are appropriate

---

## Post-Generation Quality Checklist

### Image Review Criteria

When you show me generated images, I will validate:

**Identity Consistency:**
- [ ] **Hair color correct** (silver for Nova, platinum for Athena)
- [ ] **Eye color correct** (teal for Nova, gold for Athena)
- [ ] **Outfit matches description** (bodysuit vs robe)
- [ ] **Signature accessory present** (halo for Nova, crown for Athena)

**Style Consistency:**
- [ ] **3D stylized look** (not realistic, not 2D/anime)
- [ ] **Consistent lighting** (teal for Nova, gold for Athena)
- [ ] **No style drift** across images

**Technical Quality:**
- [ ] **Clean face** (no distortions)
- [ ] **Proper anatomy** (especially hands if visible)
- [ ] **Single character** (no duplicates)
- [ ] **1024×1024 resolution** maintained
- [ ] **Not blurry or low quality**

**Accept/Reject Decision:**
- ✅ **Accept** if 7+ criteria met
- ❌ **Reject** if <5 criteria met OR identity is wrong
- 🤔 **Borderline** if 5-6 criteria met (your call)

---

## Common Validation Failures & Fixes

### Failure 1: Missing Character Token Weight

**Detection:**
```
novatraderAI, female AI trading analyst...  # No weight!
```

**Warning:**
> ⚠️ Character token should be weighted: `(novatraderAI:1.2)` - This helps maintain consistency across images

**Fix:**
```
(novatraderAI:1.2), female AI trading analyst...
```

---

### Failure 2: Pose Before Identity

**Detection:**
```
portrait shot, novatraderAI, female AI trading analyst...  # Wrong order!
```

**Warning:**
> ⚠️ Pose appears before character identity. Move pose after BREAK: `(novatraderAI:1.2), ... BREAK portrait shot`

**Fix:**
```
(novatraderAI:1.2), female AI trading analyst... BREAK
portrait shot...
```

---

### Failure 3: Missing Style Lock

**Detection:**
```
(novatraderAI:1.2), female AI trading analyst, portrait shot  # No style!
```

**Warning:**
> ⚠️ Missing style specification. Add: `stylized 3D fintech character, highly detailed, sharp focus, professional 3D render`

**Fix:**
```
(novatraderAI:1.2), female AI trading analyst... BREAK
portrait shot, stylized 3D fintech character, highly detailed, sharp focus, professional 3D render
```

---

### Failure 4: Short Negative Prompt

**Detection:**
```
bad anatomy, blurry...  # Missing critical exclusions
```

**Warning:**
> ⚠️ Negative prompt missing critical exclusions. MUST include: `realistic, photorealistic, 2d, flat, painting` to prevent style drift

**Fix:**
Use the full enhanced negative prompt (see below)

---

### Failure 5: Wrong Settings

**Detection:**
- Steps: 30 (should be 35)
- CFG: 6 (should be 7)
- Seed: Fixed number (should be -1)

**Warning:**
> ⚠️ Settings not optimal for JuggernautXL:
> - Steps: 30 → 35 (better quality)
> - CFG: 6 → 7 (character consistency)
> - Seed: [number] → -1 (true randomization)

---

### Failure 6: Wrong Model

**Detection:**
```
sd_xl_base_1.0.safetensors  # Wrong model!
```

**Warning:**
> ⚠️ Using SDXL Base instead of JuggernautXL. Switch checkpoint to: `Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors`

---

### Failure 7: Style Drift in Generated Image

**Detection:** Image looks realistic instead of stylized 3D

**Warning:**
> ⚠️ Image shows style drift toward realism. Check:
> 1. Negative prompt includes `realistic, photorealistic`
> 2. Positive prompt includes `stylized 3D fintech character`
> 3. CFG scale is 7 (not lower)

---

### Failure 8: Missing Signature Accessory

**Detection:** Nova without halo, Athena without crown

**Warning:**
> ⚠️ Character missing signature accessory. Weight the accessory higher: `(circular holographic halo:1.1)` or `(neural crown interface:1.1)`

---

## Complete Reference: Copy-Paste Elements

### Enhanced Negative Prompt (Required)

```
low quality, blurry, distorted face, bad anatomy, bad hands, extra fingers, deformed, ugly, duplicate body parts, multiple characters, 2d, flat, painting, drawing, sketch, photorealistic, realistic, oil painting, watercolor, illustration, anime style, manga, cel shaded, inconsistent lighting, asymmetric eyes, disfigured, mutated, poorly drawn face, poorly drawn hands, missing fingers, extra limbs, fused fingers, too many fingers, long neck, cross-eyed, text, watermark, logo, signature
```

### Style Lock (Required in Positive)

```
stylized 3D fintech character, highly detailed, sharp focus, professional 3D render
```

### Quality Boosters (Recommended)

```
unreal engine 5, octane render, 8k, masterpiece, best quality
```

---

## My Validation Process

When you ask me to help with prompts or workflows, I will:

1. **Check character token** - Must be weighted 1.2
2. **Verify prompt order** - Identity before BREAK, pose after
3. **Validate weights** - Light weights only (1.1-1.2), not excessive
4. **Inspect negative prompt** - Must include realistic/photorealistic exclusions
5. **Verify settings** - Steps 35, CFG 7, Seed -1
6. **Check model** - Must be Juggernaut-XL_v9
7. **Confirm style keywords** - 3D stylized, not realistic
8. **Validate dataset composition** - 40% portrait, proper variety

If any check fails, I will:
- ⚠️ **Warn** you about the issue
- 💡 **Suggest** the specific fix
- 📝 **Provide** corrected prompt/settings

---

## Quick Validation Command

When I review your work, I'll use this format:

```
✅ VALIDATION PASSED
   All checks passed! Ready to generate.

or

⚠️ VALIDATION WARNINGS (X issues):
   1. [Issue description] → [Fix suggestion]
   2. [Issue description] → [Fix suggestion]
   
   💡 Corrected prompt:
   [Fixed prompt here]
```

---

## References

- **Full Skill Docs:** `SKILLS/JUGGERNAUT_CHARACTER_SKILL.md`
- **Prompt Templates:** `SKILLS/PROMPT_TEMPLATES.md`
- **Character Specs:** `CHARACTERS.md`
- **Workflows:** `user/default/workflows/`

---

## Version History

- **v1.0** (2026-03-06) - Initial validation guide

---

## Usage Note

**This guide is for me (the AI assistant) to follow when helping you.** It ensures consistency with the JuggernautXL skill standards.

You don't need to memorize this - just know that I'll be checking your prompts against these rules and offering corrections when needed!
