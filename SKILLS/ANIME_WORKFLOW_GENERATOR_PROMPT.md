# Anime Workflow Generator Prompt for LLM

**Copy and paste this entire prompt into ChatGPT, Claude, or any LLM to generate proper Animagine XL 4.0 anime character workflows.**

---

## ⚡ TL;DR - QUICK REFERENCE

When reviewing generated workflows, verify these 5 critical items:

| Check | What to Look For | Why It Matters |
|-------|------------------|----------------|
| **Gender Tag** | `1girl` or `1boy` at start | REQUIRED by Animagine XL 4.0 |
| **Quality Tags** | `masterpiece, high score, great score, absurdres` at END | Ensures high quality output |
| **No Weights** | No `:1.1` or `:1.2` syntax | Animagine uses tag ordering, not weights |
| **Settings** | Steps=28, CFG=5, Euler Ancestral | Anime-optimized settings |
| **Model** | `animagine-xl-4.0-opt.safetensors` | Correct anime model |

**All 5 must pass or the workflow is invalid.**

---

## YOUR TASK

Generate complete ComfyUI workflow JSON files for anime character image generation using Animagine XL 4.0.

Create **one workflow file per pose** (simple approach - separate files for each pose).

The workflows must follow Animagine XL 4.0 best practices for consistent anime character generation and LoRA training dataset creation.

**CRITICAL:** This is for ANIME style, NOT 3D stylized. Use tag-based prompting, NOT natural language.

---

## INTERACTIVE MODE - HOW TO HANDLE USER INPUT

### Decision Tree

**IF user provides COMPLETE filled ANIME_CHARACTER_SPEC_TEMPLATE.md:**
→ Generate all 7 workflows immediately

**ELIF user provides PARTIAL information:**
→ Ask specific clarifying questions (concise bullet format)
→ Offer examples from Aika/hikariAI after each question
→ Validate answers in real-time with ✓/✗/⚠ feedback
→ Cannot proceed until all required fields complete

**ELSE (minimal/no information provided):**
→ Offer guided character creation wizard
→ Walk through template section-by-section
→ Provide examples at each step

### Required Information Checklist

Before generating workflows, confirm:

- [ ] **Gender** - `1girl` or `1boy` (REQUIRED for Animagine XL 4.0)
- [ ] **Token** - Format: nameAI (e.g., aikaAI, yukiAI)
- [ ] **Role** - Profession/job (e.g., crypto analyst, AI researcher)
- [ ] **Hair** - Color, style, anime features
- [ ] **Eyes** - Color, highlights, anime style (most critical!)
- [ ] **Face** - Anime proportions, expression
- [ ] **Outfit** - Type, colors, tech details
- [ ] **Accessory** - Unique signature item
- [ ] **Environment** - 2-4 contextual anime elements

### Question Templates (Use These Exactly)

**Missing Gender:**
```
Gender tag needed (REQUIRED for Animagine XL 4.0):
• 1girl - for female characters
• 1boy - for male characters

Which for your character?
```

**Missing Token:**
```
Token needed. Format: nameAI
Example: aikaAI, yukiAI, hikariAI
What token for your character?
```

**Missing Role:**
```
Role needed. Examples:
• Aika: AI crypto analyst
• hikariAI: AI crypto market scout
• Custom: [your profession]

What's your character's profession?
```

**Missing Visual Anchors (Anime Style):**
```
Need visual anchors for anime character:

1. HAIR - Anime style description
   Example (Aika): short silver white hair with blue gradient tips
   Example (hikariAI): short neon blue hair with dynamic style

2. EYES - Most critical in anime!
   Example (Aika): deep purple eyes with star highlights
   Example (hikariAI): electric yellow eyes with star highlights

3. ACCESSORY - Unique anime tech item
   Example (Aika): holographic data tablet
   Example (hikariAI): glowing cyber visor over one eye

Define these for your character:
```

**Missing Anime Style Elements:**
```
Anime-specific details needed:

• Face shape: [soft round, sharp angular, etc.]
• Expression: [energetic, cool, serious, etc.]
• Outfit type: [futuristic uniform, tech bodysuit, etc.]
• Special effects: [glowing elements, holographic displays, etc.]

Examples:
• Aika: soft facial features, analytical expression, futuristic school uniform with tech accents
• hikariAI: soft anime features, energetic expression, futuristic trading jacket

Your character's details?
```

### Real-Time Validation Rules

When user provides information, validate immediately:

**Gender Tag:**
- ✓ Valid: `1girl` or `1boy` exactly
- ✗ Invalid: Anything else (female, male, girl, etc.)

**Token Format:**
- ✓ Valid: Ends with "AI", no spaces (aikaAI, yukiAI)
- ✗ Invalid: Contains spaces, missing AI suffix

**No Weight Syntax:**
- ✓ Correct: `aikaAI, short silver hair`
- ✗ Wrong: `(aikaAI:1.2), (short silver hair:1.1)`
- ⚠ Warning: Animagine XL 4.0 doesn't use weight syntax!

**Quality Tags Position:**
- ✓ Correct: At END of prompt
- ✗ Wrong: At beginning or middle

**Settings:**
- ✓ Steps: 28 (correct)
- ✗ Steps: 35 (wrong - too high for anime)
- ✓ CFG: 5 (correct)
- ✗ CFG: 7 (wrong - too high)
- ✓ Sampler: euler_ancestral (correct)
- ✗ Sampler: dpmpp_2m (wrong - not optimal for anime)

### Example Interaction

**User:** "Make anime workflow for Sakura"

**You:**
```
Missing required information for anime character. Need:

□ Gender: 1girl or 1boy?
□ Token: sakuraAI? (or other)
□ Role: Profession/job?
□ Visual anchors (anime style):
  - Hair: color/style?
  - Eyes: color/highlights? (most critical in anime!)
  - Accessory: unique item?

Example from Aika (AI crypto analyst):
□ Gender: 1girl
□ Token: aikaAI
□ Role: AI crypto analyst
□ Hair: short silver white with blue gradient tips
□ Eyes: deep purple with star highlights
□ Accessory: holographic data tablet
□ Outfit: futuristic school uniform with tech accents

Example from hikariAI (AI crypto market scout):
□ Gender: 1girl
□ Token: hikariAI
□ Role: AI crypto market scout
□ Hair: short neon blue
□ Eyes: electric yellow with star highlights
□ Accessory: glowing cyber visor over one eye
□ Outfit: futuristic trading jacket

Provide Sakura's anime-style details:
```

---

## CHARACTER SPECIFICATION

**[PASTE YOUR FILLED ANIME CHARACTER SPEC FROM ANIME_CHARACTER_SPEC_TEMPLATE.md HERE]**

---

## MANDATORY RULES - HARD CONSTRAINTS

These rules are **non-negotiable**. Violation = invalid workflow.

### ✅ MUST (Required)

| Rule | Value | Why Critical |
|------|-------|--------------|
| **Gender Tag** | `1girl` or `1boy` FIRST | Required by Animagine XL 4.0 architecture |
| **Token** | Included after gender | Character identifier |
| **No Weights** | NEVER use `:1.1` or `:1.2` | Animagine uses tag ordering, not weights |
| **Tag-Based** | Comma-separated tags only | Model trained on tags, not natural language |
| **Quality Tags** | `masterpiece, high score, great score, absurdres` at END | Ensures high quality |
| **Anime Style** | Include `modern anime style, digital art` | Prevents style drift |
| **Model** | animagine-xl-4.0-opt.safetensors | Correct anime model |
| **Steps** | Exactly `28` | Optimal for anime (not 35!) |
| **CFG** | Exactly `5` | Sweet spot for anime (not 7!) |
| **Sampler** | `euler_ancestral` | Recommended for anime |
| **Seed** | `-1` | True randomization |
| **Resolution** | `1024×1024` | Native SDXL |

### ❌ NEVER (Prohibited)

| Rule | Wrong Value | Why Broken |
|------|-------------|------------|
| **Missing Gender** | No `1girl`/`1boy` | Model won't generate correctly |
| **Weight Syntax** | `(token:1.2)` | Doesn't work with Animagine XL 4.0 |
| **Natural Language** | `A girl with blue hair` | Model trained on tags only |
| **Quality Tags First** | Tags at beginning | Reduces effectiveness |
| **Steps** | `35` | Wastes time, no improvement |
| **CFG** | `7` | Too high, causes artifacts |
| **Sampler** | `dpmpp_2m` | Not optimal for anime |
| **Wrong Model** | JuggernautXL | Completely different style |
| **Wrong Negative** | Juggernaut negative | Missing anime exclusions |

---

## COMMON MISTAKES - LEARN FROM EXAMPLES

### Mistake #1: Missing Gender Tag

**❌ WRONG:**
```
hikariAI, AI crypto market scout, short neon blue hair...
```
**Problem:** No gender tag - Animagine XL 4.0 requires `1girl` or `1boy`

**✅ CORRECT:**
```
1girl, hikariAI, AI crypto market scout, short neon blue hair...
```
**Fixed:** Gender tag first

---

### Mistake #2: Using Weight Syntax

**❌ WRONG:**
```
1girl, (hikariAI:1.2), (short neon blue hair:1.1)...
```
**Problem:** Animagine XL 4.0 doesn't use weight syntax

**✅ CORRECT:**
```
1girl, hikariAI, short neon blue hair...
```
**Fixed:** Plain tags only

---

### Mistake #3: Natural Language

**❌ WRONG:**
```
1girl, hikariAI who is an AI crypto market scout with short blue hair...
```
**Problem:** Model trained on tags, not sentences

**✅ CORRECT:**
```
1girl, hikariAI, AI crypto market scout, short neon blue hair...
```
**Fixed:** Tag-based only

---

### Mistake #4: Wrong Settings

**❌ WRONG:**
```json
"widgets_values": [-1, "randomize", 35, 7, "dpmpp_2m", "normal", 1]
```
**Problem:** Steps=35, CFG=7, wrong sampler - these are JuggernautXL settings!

**✅ CORRECT:**
```json
"widgets_values": [-1, "randomize", 28, 5, "euler_ancestral", "normal", 1]
```
**Fixed:** Steps=28, CFG=5, euler_ancestral (anime settings)

---

### Mistake #5: Quality Tags in Wrong Position

**❌ WRONG:**
```
masterpiece, high score, 1girl, hikariAI, short neon blue hair...
```
**Problem:** Quality tags at beginning dilute character tags

**✅ CORRECT:**
```
1girl, hikariAI, short neon blue hair... masterpiece, high score, great score, absurdres
```
**Fixed:** Quality tags at END

---

### Mistake #6: Wrong Model

**❌ WRONG:**
```json
"widgets_values": ["Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors"]
```
**Problem:** Wrong model - JuggernautXL is for 3D stylized, not anime

**✅ CORRECT:**
```json
"widgets_values": ["animagine-xl-4.0-opt.safetensors"]
```
**Fixed:** Use anime model

---

### Mistake #7: Missing Anime Keywords

**❌ WRONG:**
```
1girl, hikariAI, short neon blue hair...
```
**Problem:** Missing anime style keywords

**✅ CORRECT:**
```
1girl, hikariAI, short neon blue hair... modern anime style, digital art
```
**Fixed:** Include style lock

---

### Quick Reference: Common Errors

| Error | Detection | Fix |
|-------|-----------|-----|
| Missing gender | Check prompt start | Add `1girl` or `1boy` first |
| Weight syntax | Search for `(` and `:` | Remove all `:1.x` weights |
| Natural language | Look for `with`, `who`, `and` | Convert to comma-separated tags |
| Wrong steps | Check KSampler widget_values[2] | Set to 28, not 35 |
| Wrong CFG | Check widget_values[3] | Set to 5, not 7 |
| Wrong sampler | Check widget_values[4] | Use `euler_ancestral` |
| Quality tags first | Check position in prompt | Move to END |
| Wrong model | Check checkpoint name | Use `animagine-xl-4.0-opt` |

---

## STOP & VERIFY CHECKPOINTS

You MUST complete these 3 checkpoints before outputting any workflow. Do not skip.

### 🛑 CHECKPOINT 1: Prompt Verification

**After constructing the positive prompt, STOP and verify:**

```
PROMPT VERIFICATION:
□ Gender tag first? (1girl or 1boy at start)
□ No weight syntax? (no :1.1 or :1.2)
□ Tag-based only? (no natural language words like "with", "who")
□ Character token included?
□ Visual traits (hair, eyes) described?
□ Style tags present? (modern anime style, digital art)
□ Quality tags at END? (masterpiece, high score, great score, absurdres)
□ No BREAK keyword? (not used in anime workflows)
```

**If ANY check fails:**
- State which check failed
- Explain why it's wrong for anime
- Show corrected version
- Re-verify

**Only proceed to Checkpoint 2 when ALL checks pass.**

---

### 🛑 CHECKPOINT 2: Settings Verification

**After configuring KSampler and model, STOP and verify:**

```
SETTINGS VERIFICATION:
□ Model: animagine-xl-4.0-opt.safetensors
□ Steps: 28 (NOT 35)
□ CFG: 5 (NOT 7)
□ Sampler: euler_ancestral (NOT dpmpp_2m)
□ Resolution: 1024×1024
□ Seed: -1
□ Batch Size: 2
```

**Show your work:**
```
Current values:
- Model: animagine-xl-4.0-opt ✅
- Steps: 28 ✅
- CFG: 5 ✅
- Sampler: euler_ancestral ✅
- Seed: -1 ✅
```

**If ANY value is wrong:**
- Identify incorrect value
- Explain correct anime value
- Fix it
- Re-verify

**Only proceed to Checkpoint 3 when ALL values correct.**

---

### 🛑 CHECKPOINT 3: Final Validation

**Before outputting JSON, STOP and run 10-point checklist:**

```
FINAL VALIDATION (MANDATORY):
□ 1. Gender Tag: 1girl or 1boy first
□ 2. Token: Included in prompt
□ 3. No Weights: No :1.x syntax anywhere
□ 4. Tag-Based: Only comma-separated tags
□ 5. Quality Tags: At END (masterpiece, high score, great score, absurdres)
□ 6. Model: animagine-xl-4.0-opt.safetensors
□ 7. Steps: Exactly 28
□ 8. CFG: Exactly 5
□ 9. Sampler: euler_ancestral
□ 10. Valid JSON: No syntax errors
```

**Display results:**
```
Validation Results:
✅ 1. Gender Tag - PASS
✅ 2. Token - PASS
✅ 3. No Weights - PASS
✅ 4. Tag-Based - PASS
✅ 5. Quality Tags - PASS
✅ 6. Model - PASS
✅ 7. Steps - PASS
✅ 8. CFG - PASS
✅ 9. Sampler - PASS
✅ 10. Valid JSON - PASS

✅ ALL CHECKS PASSED - Ready to output
```

**If ANY check fails:**
```
Validation Results:
✅ 1. Gender Tag - PASS
❌ 2. Token - PASS
✅ 3. No Weights - FAIL (found :1.2 in prompt)
✅ 4. Tag-Based - PASS
...

❌ CHECKPOINT 3 FAILED
Fix: Remove weight syntax from prompt
Re-run validation after fix.
```

**DO NOT OUTPUT WORKFLOW until all 10 checks show ✅**

---

## CRITICAL REQUIREMENTS

### 1. Model & Settings (Non-Negotiable)

| Setting | Value | Notes |
|---------|-------|-------|
| **Checkpoint** | animagine-xl-4.0-opt.safetensors | ~6.5GB download |
| **Resolution** | 1024×1024 | SDXL native |
| **Sampler** | euler_ancestral | Recommended for anime |
| **Scheduler** | normal | Standard |
| **Steps** | 28 | Optimal for anime (not 35!) |
| **CFG Scale** | 5 | Anime sweet spot (not 7!) |
| **Seed** | -1 | True randomization |
| **Batch Size** | 2 | Memory safe |

**Validation:** Check these exact values appear in the JSON.

### 2. Prompt Structure (STRICT - Follow Exactly)

Use this exact tag-based structure:

```
1girl/1boy, TOKEN, ROLE, HAIR, EYES, FACE, OUTFIT, ACCESSORY, POSE_ENVIRONMENT, STYLE_TAGS, QUALITY_TAGS
```

**Breakdown:**
1. **Gender tag FIRST** - `1girl` or `1boy` (REQUIRED)
2. **Token** - Character identifier
3. **Role** - Profession
4. **Visual traits** - Hair, eyes, face, outfit, accessory
5. **Pose/Environment** - Action and setting
6. **Style tags** - `modern anime style, digital art`
7. **Quality tags at END** - `masterpiece, high score, great score, absurdres`

**Rules:**
1. **NEVER use weight syntax** - No `:1.1` or `:1.2`
2. **NEVER use natural language** - No sentences, only tags
3. **Gender tag MUST be first** - Required by model architecture
4. **Quality tags MUST be at end** - Reduces dilution
5. **NEVER use BREAK** - Not needed in anime workflows
6. **Always include style tags** - Prevents drift

### 3. Negative Prompt (EXACT - Copy Verbatim)

**Use this COMPLETE anime negative prompt (DO NOT MODIFY):**

```
lowres, bad anatomy, bad hands, text, error, missing finger, extra digits, fewer digits, cropped, worst quality, low quality, low score, bad score, average score, signature, watermark, username, blurry, 3d render, realistic, photorealistic, western cartoon
```

**CRITICAL:** Must exclude `3d render, realistic, photorealistic, western cartoon` - Animagine XL 4.0 is for anime only.

### 4. Standard Poses (Generate One Workflow Per Pose)

**Generate workflows for these poses (or user-specified subset):**

**Required (Priority Order):**

1. **Portrait** - Face close-up, looking at viewer
   - Priority: HIGHEST (40% of dataset)
   - Tags: `portrait, upper body, looking at viewer`

2. **Standing Confident** - Waist-up, professional stance
   - Priority: HIGH (20% of dataset)
   - Tags: `standing, confident pose, waist up`

3. **Action/Professional** - Character performing their role
   - Priority: HIGH (20% of dataset)
   - Tags: `analyzing data, dynamic pose, tech interface`

4. **Side Profile** - Looking left or right
   - Priority: MEDIUM (10% of dataset)
   - Tags: `profile, looking to side`

5. **Three-Quarter View** - 45-degree angle
   - Priority: MEDIUM (5% of dataset)
   - Tags: `three-quarter view`

6. **Environmental/Full Body** - Full body with context
   - Priority: LOW (5% of dataset)
   - Tags: `full body, standing`

7. **Detail Focus** - Close-up eyes or accessory
   - Priority: LOW (0-5% of dataset)
   - Tags: `close-up, eye focus`

**Note:** Generate workflows for ALL 7 poses, or ask user which ones they want.

---

## WORKFLOW JSON STRUCTURE

Create valid JSON with these exact nodes:

```json
{
  "last_node_id": 20,
  "last_link_id": 25,
  "nodes": [
    {
      "id": 1,
      "type": "CheckpointLoaderSimple",
      "pos": [50, 200],
      "size": [350, 100],
      "inputs": [],
      "outputs": [
        {"name": "MODEL", "type": "MODEL", "links": [1], "slot_index": 0},
        {"name": "CLIP", "type": "CLIP", "links": [2, 3], "slot_index": 1},
        {"name": "VAE", "type": "VAE", "links": [9], "slot_index": 2}
      ],
      "widgets_values": ["animagine-xl-4.0-opt.safetensors"],
      "title": "Animagine XL 4.0 Opt"
    },
    {
      "id": 2,
      "type": "CLIPTextEncode",
      "pos": [450, 150],
      "size": [450, 200],
      "inputs": [{"name": "clip", "type": "CLIP", "link": 2}],
      "outputs": [{"name": "CONDITIONING", "type": "CONDITIONING", "links": [4], "slot_index": 0}],
      "widgets_values": ["POSITIVE_PROMPT_HERE"],
      "title": "[CHARACTER] - [POSE] Prompt"
    },
    {
      "id": 3,
      "type": "CLIPTextEncode",
      "pos": [450, 400],
      "size": [450, 200],
      "inputs": [{"name": "clip", "type": "CLIP", "link": 3}],
      "outputs": [{"name": "CONDITIONING", "type": "CONDITIONING", "links": [5], "slot_index": 0}],
      "widgets_values": ["NEGATIVE_PROMPT_HERE"],
      "title": "Negative Prompt (Anime)"
    },
    {
      "id": 4,
      "type": "EmptyLatentImage",
      "pos": [50, 450],
      "size": [350, 110],
      "inputs": [],
      "outputs": [{"name": "LATENT", "type": "LATENT", "links": [6], "slot_index": 0}],
      "widgets_values": [1024, 1024, 2],
      "title": "Batch Size: 2 Images"
    },
    {
      "id": 5,
      "type": "KSampler",
      "pos": [950, 250],
      "size": [320, 470],
      "inputs": [
        {"name": "model", "type": "MODEL", "link": 1},
        {"name": "positive", "type": "CONDITIONING", "link": 4},
        {"name": "negative", "type": "CONDITIONING", "link": 5},
        {"name": "latent_image", "type": "LATENT", "link": 6}
      ],
      "outputs": [{"name": "LATENT", "type": "LATENT", "links": [7], "slot_index": 0}],
      "widgets_values": [-1, "randomize", 28, 5, "euler_ancestral", "normal", 1],
      "title": "Generate (Steps:28, CFG:5, Seed:-1)"
    },
    {
      "id": 6,
      "type": "VAEDecode",
      "pos": [1350, 250],
      "size": [210, 50],
      "inputs": [
        {"name": "samples", "type": "LATENT", "link": 7},
        {"name": "vae", "type": "VAE", "link": 9}
      ],
      "outputs": [{"name": "IMAGE", "type": "IMAGE", "links": [8], "slot_index": 0}],
      "title": "VAE Decode"
    },
    {
      "id": 7,
      "type": "SaveImage",
      "pos": [1650, 250],
      "size": [350, 300],
      "inputs": [{"name": "images", "type": "IMAGE", "link": 8}],
      "widgets_values": ["[token]_[pose]_animagine"],
      "title": "Save Images"
    },
    {
      "id": 10,
      "type": "Note",
      "pos": [50, 50],
      "size": [400, 140],
      "inputs": [],
      "outputs": [],
      "widgets_values": ["[CHARACTER] - [POSE] - Animagine XL 4.0\\n\\nSettings: Steps:28 | CFG:5 | Seed:-1 | Euler Ancestral\\nBatch: 2 images\\n\\nReferences:\\n- Skill: SKILLS/ANIME_CHARACTER_SKILL.md\\n- Templates: SKILLS/ANIME_PROMPT_TEMPLATES.md\\n- Validation: SKILLS/ANIME_VALIDATION_GUIDE.md\\n- Spec: SKILLS/ANIME_CHARACTER_SPEC_TEMPLATE.md"],
      "title": "Workflow Info"
    }
  ],
  "links": [
    [1, 1, 0, 5, 0, "MODEL"],
    [2, 1, 1, 2, 0, "CLIP"],
    [3, 1, 1, 3, 0, "CLIP"],
    [4, 2, 0, 5, 1, "CONDITIONING"],
    [5, 3, 0, 5, 2, "CONDITIONING"],
    [6, 4, 0, 5, 3, "LATENT"],
    [7, 5, 0, 6, 0, "LATENT"],
    [8, 6, 0, 7, 0, "IMAGE"],
    [9, 1, 2, 6, 1, "VAE"]
  ],
  "groups": [],
  "config": {},
  "extra": {},
  "version": 0.4
}
```

**Important:**
- Replace `POSITIVE_PROMPT_HERE` with tag-based character prompt
- Replace `NEGATIVE_PROMPT_HERE` with exact anime negative from section 3
- Replace `[CHARACTER]`, `[POSE]`, `[token]` with actual values
- Ensure valid JSON (no trailing commas, proper quotes)

---

## VALIDATION CHECKLIST (10-Point Verification)

Before outputting each workflow, verify:

- [ ] **1. Gender Tag:** `1girl` or `1boy` at prompt start
- [ ] **2. Token:** Character token included
- [ ] **3. No Weights:** No `:1.x` syntax anywhere
- [ ] **4. Tag-Based:** Only comma-separated tags, no natural language
- [ ] **5. Quality Tags:** `masterpiece, high score, great score, absurdres` at END
- [ ] **6. Model:** `animagine-xl-4.0-opt.safetensors`
- [ ] **7. Steps:** Exactly 28
- [ ] **8. CFG:** Exactly 5
- [ ] **9. Sampler:** `euler_ancestral`
- [ ] **10. Valid JSON:** No syntax errors

**If any check fails, fix it before outputting.**

**Remember:** You already passed Checkpoint 3 to get here. These are the same 10 checks - just the final confirmation.

---

## OUTPUT FORMAT

For each pose workflow, provide:

### 1. Character & Pose Summary
```
Character: [TOKEN] - [Role]
Gender: [1girl/1boy]
Pose: [Pose Name]
Priority: [High/Medium/Low]
Target Images: [X] (from dataset targets)
```

### 2. Complete Positive Prompt (Tag-Based)
```
1girl/1boy, TOKEN, ROLE, HAIR, EYES, FACE, OUTFIT, ACCESSORY, POSE, ENVIRONMENT, STYLE_TAGS, QUALITY_TAGS
```

### 3. Complete Negative Prompt
```
[Exact anime negative prompt from section 3]
```

### 4. Filename
```
[token]_[pose]_animagine.json
```
Example: `hikariAI_portrait_animagine.json`

### 5. Complete Workflow JSON
```json
[Valid JSON workflow]
```

### 6. Validation Confirmation
```
✅ All 10 validation checks passed
✅ All 3 checkpoints passed
```

---

## EXAMPLE OUTPUT (hikariAI Portrait)

### Character & Pose Summary
```
Character: hikariAI - AI crypto market scout
Gender: 1girl
Pose: Portrait
Priority: HIGHEST
Target Images: 12-16 (40% of dataset)
```

### Complete Positive Prompt
```
1girl, hikariAI, AI crypto market scout, short neon blue hair, electric yellow eyes with star highlights, glowing cyber visor over one eye, soft anime facial features, analytical and energetic expression, futuristic trading jacket with electric blue and neon purple colors, high-tech details, portrait, upper body, looking at viewer, minimal background, modern anime style, digital art, masterpiece, high score, great score, absurdres
```

### Complete Negative Prompt
```
lowres, bad anatomy, bad hands, text, error, missing finger, extra digits, fewer digits, cropped, worst quality, low quality, low score, bad score, average score, signature, watermark, username, blurry, 3d render, realistic, photorealistic, western cartoon
```

### Filename
```
hikariAI_portrait_animagine.json
```

### Complete Workflow JSON
```json
[JSON would go here with above prompts inserted]
```

### Validation Confirmation
```
✅ All 10 validation checks passed
✅ All 3 checkpoints passed
```

---

## GENERATION INSTRUCTIONS

**Generate workflows for ALL 7 poses, or ask user which specific poses they want.**

**For each pose:**
1. **Construct tag-based prompt** using character spec + pose template
2. **CHECKPOINT 1:** Verify prompt structure (STOP - no weights, gender first, tags only)
3. **Configure anime settings** in KSampler (28 steps, CFG 5, euler_ancestral)
4. **CHECKPOINT 2:** Verify settings (STOP - confirm anime values)
5. **Use exact anime negative prompt** from section 3
6. **Create valid JSON workflow** with all nodes properly connected
7. **CHECKPOINT 3:** Run 10-point final validation (STOP - all must pass)
8. **Output in format above** only after all checkpoints cleared

**Critical:** DO NOT skip checkpoints. DO NOT output if any checkpoint fails.

**Final output should include:**
- Summary of all generated workflows
- Total workflows: [7 or user-specified count]
- Recommended generation order (Portrait → Standing → Action → etc.)
- Confirmation: "All checkpoints passed for each workflow"

---

## REFERENCES

- **Anime Skill Documentation:** `SKILLS/ANIME_CHARACTER_SKILL.md`
- **Pose Templates:** `SKILLS/ANIME_PROMPT_TEMPLATES.md`
- **Validation Rules:** `SKILLS/ANIME_VALIDATION_GUIDE.md`
- **Character Spec Format:** `SKILLS/ANIME_CHARACTER_SPEC_TEMPLATE.md`
- **Example Characters:** `characters/hikariAI/spec.md`, `characters/aika/spec.md`, `SKILLS/examples/anime/aika/`

---

## READY TO GENERATE?

**Paste your anime character spec above, then generate the workflows!**

**Don't have a complete spec?** No problem - I'll ask clarifying questions and guide you through creating one using anime-style examples from Aika and hikariAI.

**Generation Process:**
1. **Interactive Mode** - I'll check if your spec is complete
2. **Ask questions** if anything is missing (with anime examples)
3. **Validate in real-time** as you provide information
4. **Complete all 3 checkpoints** for each workflow
5. **Output only after validation** passes

**Remember:**
- One workflow per pose
- 7 workflows total (or specify which poses you want)
- All 3 checkpoints must pass for each workflow
- Use STOP & VERIFY checkpoints - don't skip them
- NO weight syntax, NO natural language - tag-based only!

**Let's build your anime character workflows! Paste your spec or tell me about your character:**
