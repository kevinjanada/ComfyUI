# Workflow Generator Prompt for LLM

**Copy and paste this entire prompt into ChatGPT, Claude, or any LLM to generate proper JuggernautXL character workflows.**

---

## ⚡ TL;DR - QUICK REFERENCE

When reviewing generated workflows, verify these 5 critical items:

| Check | What to Look For | Why It Matters |
|-------|------------------|----------------|
| **Seed** | `-1` in KSampler widget | `0` = identical images, `-1` = true random |
| **BREAK** | `...outfit BREAK pose...` | Separates identity from action |
| **Token Weight** | `(character:1.2)` first | Character consistency anchor |
| **Max Weight** | No weight > 1.2 | Prevents over-emphasis distortion |
| **Negative** | Contains "realistic, photorealistic" | Prevents JuggernautXL realism drift |

**All 5 must pass or the workflow is invalid.**

---

## YOUR TASK

Generate complete ComfyUI workflow JSON files for character image generation using JuggernautXL v9.

Create **one workflow file per pose** (simple approach - separate files for each pose).

The workflows must follow JuggernautXL best practices for consistent character generation and LoRA training dataset creation.

---

## INTERACTIVE MODE - HOW TO HANDLE USER INPUT

### Decision Tree

**IF user provides COMPLETE filled CHARACTER_SPEC_TEMPLATE.md:**
→ Generate all 7 workflows immediately

**ELIF user provides PARTIAL information:**
→ Ask specific clarifying questions (concise bullet format)
→ Offer examples from Luna/Nova/Athena after each question
→ Validate answers in real-time with ✓/✗/⚠ feedback
→ Cannot proceed until all required fields complete

**ELSE (minimal/no information provided):**
→ Offer guided character creation wizard
→ Walk through template section-by-section
→ Provide examples at each step

### Required Information Checklist

Before generating workflows, confirm:

- [ ] **Token** - Format: nameAI (e.g., lunaAI, novaAI)
- [ ] **Role** - Profession/job (e.g., blockchain developer)
- [ ] **Visual Anchor #1: Hair** - Color, style, special features
- [ ] **Visual Anchor #2: Eyes** - Color, effect, glow
- [ ] **Visual Anchor #3: Signature Accessory** - Unique identifier item
- [ ] **Face Structure** - General shape, expression
- [ ] **Outfit** - Type, colors, details
- [ ] **Color Palette** - Primary, secondary, tertiary hex codes
- [ ] **Environment Elements** - 2-4 contextual items

### Question Templates (Use These Exactly)

**Missing Token:**
```
Token needed. Format: nameAI
Example: lunaAI, novaAI, athenaAI
What token for your character?
```

**Missing Role:**
```
Role needed. Examples:
• Luna: blockchain developer
• Nova: AI safety researcher  
• Athena: DeFi strategist
What's your character's profession?
```

**Missing Visual Anchors:**
```
Need 3 visual anchors (define identity):

1. HAIR - Color, style, special features
   Example (Luna): long dark blue hair with glowing cyan tips

2. EYES - Color, effect
   Example (Nova): deep purple eyes with neural pattern overlay

3. ACCESSORY - Unique signature item
   Example (Athena): golden data crown with holographic interface

Define these for your character:
```

**Missing Color Palette:**
```
Color palette prevents drift. Need:
• Primary (main outfit): #HEX + description
• Secondary (accents): #HEX + description
• Tertiary (background): #HEX + description

Example (Luna):
• Primary: #8B5CF6 vivid purple
• Secondary: #06B6D4 bright cyan
• Tertiary: #1E293B dark navy

Your palette?
```

### Real-Time Validation Rules

When user provides information, validate immediately:

**Token Format:**
- ✓ Valid: Ends with "AI", no spaces (lunaAI, victorAI)
- ✗ Invalid: Contains spaces, missing AI suffix
- ⚠ Warning: Suggest shorter token (2-3 syllables ideal)

**Weight Values:**
- ✓ Token: 1.2 (correct)
- ✓ Visual anchors: 1.1 (correct)
- ✗ Any value > 1.2 (rejected - explain max is 1.2)

**Required Keywords:**
- ✓ BREAK present (correct)
- ✗ Missing BREAK (reject - ask to add)
- ✓ "stylized 3D fintech character" included (correct)
- ✗ Missing style lock (reject - must include)

**Settings:**
- ✓ seed=-1 (correct)
- ✗ seed=0 (reject - explain identical image problem)
- ✓ steps=35, cfg=7 (correct)
- ✗ steps≠35 or cfg≠7 (reject - use exact values)

### Example Interaction

**User:** "Make workflow for Alex"

**You:**
```
Missing required information. Need:

• Token (format: nameAI) → alexAI?
• Role → profession/job?
• Visual anchors:
  - Hair: color/style?
  - Eyes: color/effect?
  - Accessory: unique item?

Example from Luna:
• Token: lunaAI
• Role: blockchain developer
• Hair: long dark blue with glowing cyan tips
• Eyes: electric purple with digital patterns
• Accessory: data visor with holographic interface

Provide Alex's details:
```

**User:** "alexAI, crypto trader, blonde hair, blue eyes, watch"

**You:**
```
Partial info received. Need more detail:

✓ Token: alexAI
✓ Role: crypto trader
⚠ Hair: Need style/length + special features
  Example: short platinum blonde with data strands
✗ Eyes: Need color + effect
  Example: amber eyes with golden calculations
⚠ Accessory: Need description
  Example: smartwatch with holographic charts

Complete these:
```

---

## CHARACTER SPECIFICATION

**[PASTE YOUR FILLED CHARACTER SPEC FROM CHARACTER_SPEC_TEMPLATE.md HERE]**

---

## MANDATORY RULES - HARD CONSTRAINTS

These rules are **non-negotiable**. Violation = invalid workflow.

### ✅ MUST (Required)

| Rule | Value | Why Critical |
|------|-------|--------------|
| **Seed** | `-1` | `0` creates identical images every time |
| **BREAK** | Exactly 1 | Separates identity from action/pose |
| **Token Position** | First in prompt | `(TOKEN:1.2), role, hair...` |
| **Token Weight** | Exactly `1.2` | Character consistency anchor |
| **Visual Anchor Weights** | Exactly `1.1` | Hair, eyes, accessory consistency |
| **Max Weight** | Never exceed `1.2` | Prevents over-emphasis artifacts |
| **Style Lock** | Include "stylized 3D fintech character" | Prevents JuggernautXL realism drift |
| **Model** | Juggernaut-XL_v9 | SDXL base produces inferior results |
| **Steps** | Exactly `35` | Optimal quality/speed balance |
| **CFG** | Exactly `7` | Character consistency sweet spot |
| **Negative Keywords** | Include "realistic, photorealistic" | Counteracts model photorealism bias |

### ❌ NEVER (Prohibited)

| Rule | Wrong Value | Why Broken |
|------|-------------|------------|
| **Seed** | `0` | Generates identical images |
| **Weight** | `>1.2` on any element | Causes distortion/artifacts |
| **Prompt** | "realistic" or "photorealistic" | Conflicts with stylized 3D goal |
| **Model** | SDXL base | Wrong model for this workflow |
| **Steps** | `<35` or `>35` | Suboptimal quality |
| **CFG** | `<7` or `>7` | Loses consistency or adds noise |
| **BREAK** | Missing or multiple | Breaks prompt structure |
| **Style** | Missing "stylized 3D fintech character" | Results drift to photorealism |

---

## CRITICAL REQUIREMENTS

### 1. Model & Settings (Non-Negotiable)

| Setting | Value | Notes |
|---------|-------|-------|
| **Checkpoint** | Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors | Built-in VAE |
| **Resolution** | 1024×1024 | SDXL native |
| **Sampler** | dpmpp_2m | Best balance |
| **Scheduler** | karras | Standard |
| **Steps** | 35 | Optimal quality |
| **CFG Scale** | 7 | Character consistency |
| **Seed** | -1 | True randomization |
| **Batch Size** | 2 | Memory safe |

**Validation:** Check these exact values appear in the JSON.

### 2. Prompt Structure (STRICT - Follow Exactly)

Use this exact structure for the positive prompt:

```
(TOKEN:1.2), [ROLE], ([HAIR]:1.1), ([EYES]:1.1), [FACE_STRUCTURE], ([SIGNATURE_ACCESSORY]:1.1), [OUTFIT] BREAK
[POSE/ACTION], [ENVIRONMENT], stylized 3D fintech character, highly detailed, sharp focus, professional 3D render
```

**Rules:**
1. **Character token MUST be first** with `(TOKEN:1.2)` weight
2. **Use BREAK** to separate identity from action
3. **Weight critical traits** at 1.1 (hair, eyes, signature accessory)
4. **Never exceed 1.2** weight on any element
5. **Always include** "stylized 3D fintech character" (prevents realism drift)
6. **Always include** quality boosters: "highly detailed, sharp focus, professional 3D render"

### 3. Negative Prompt (EXACT - Copy Verbatim)

**Use this COMPLETE negative prompt (DO NOT MODIFY):**

```
low quality, blurry, distorted face, bad anatomy, bad hands, extra fingers, deformed, ugly, duplicate body parts, multiple characters, 2d, flat, painting, drawing, sketch, photorealistic, realistic, oil painting, watercolor, illustration, anime style, manga, cel shaded, inconsistent lighting, asymmetric eyes, disfigured, mutated, poorly drawn face, poorly drawn hands, missing fingers, extra limbs, fused fingers, too many fingers, long neck, cross-eyed, text, watermark, logo, signature
```

**CRITICAL:** Must include "realistic, photorealistic" - JuggernautXL defaults to photorealistic, we need stylized 3D.

---

## COMMON MISTAKES - LEARN FROM EXAMPLES

These are real mistakes seen in workflow generation. Study these to avoid them.

### Mistake #1: Wrong Seed Value

**❌ WRONG:**
```json
"widgets_values": [0, "randomize", 35, 7, "dpmpp_2m", "karras", 1]
```
**Problem:** `seed: 0` generates the SAME image every time

**✅ CORRECT:**
```json
"widgets_values": [-1, "randomize", 35, 7, "dpmpp_2m", "karras", 1]
```
**Fixed:** `seed: -1` enables true randomization

---

### Mistake #2: Token Not First

**❌ WRONG:**
```
ai researcher, (novaAI:1.2), long purple hair...
```
**Problem:** Token weight diluted by preceding text

**✅ CORRECT:**
```
(novaAI:1.2), ai researcher, long purple hair...
```
**Fixed:** Token weighted and positioned first for maximum impact

---

### Mistake #3: Missing BREAK

**❌ WRONG:**
```
(novaAI:1.2), ai researcher, (long purple hair:1.1) standing confidently
```
**Problem:** Identity and pose mixed together - inconsistent results

**✅ CORRECT:**
```
(novaAI:1.2), ai researcher, (long purple hair:1.1) BREAK
standing confidently, stylized 3D fintech character...
```
**Fixed:** BREAK clearly separates identity (before) from action (after)

---

### Mistake #4: Wrong CFG Scale

**❌ WRONG:**
```json
"widgets_values": [-1, "randomize", 35, 6, "dpmpp_2m", "karras", 1]
```
**Problem:** `CFG: 6` too low - character features drift between images

**✅ CORRECT:**
```json
"widgets_values": [-1, "randomize", 35, 7, "dpmpp_2m", "karras", 1]
```
**Fixed:** `CFG: 7` maintains character consistency

---

### Mistake #5: Missing Style Lock

**❌ WRONG:**
```
BREAK
standing confidently, futuristic interface, highly detailed...
```
**Problem:** Missing "stylized 3D fintech character" - results drift to photorealism

**✅ CORRECT:**
```
BREAK
standing confidently, futuristic interface, stylized 3D fintech character, highly detailed...
```
**Fixed:** Style lock keyword keeps consistent stylized 3D aesthetic

---

### Mistake #6: Weight Too High

**❌ WRONG:**
```
(novaAI:1.5), ai researcher...
```
**Problem:** Weight `1.5` causes distortion and artifacts

**✅ CORRECT:**
```
(novaAI:1.2), ai researcher...
```
**Fixed:** Max weight `1.2` prevents over-emphasis

---

### Mistake #7: Wrong Model

**❌ WRONG:**
```json
"widgets_values": ["sd_xl_base_1.0.safetensors"]
```
**Problem:** SDXL base model not optimized for character consistency

**✅ CORRECT:**
```json
"widgets_values": ["Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors"]
```
**Fixed:** JuggernautXL v9 produces superior character results

---

### Quick Reference: Common Errors

| Error | Detection | Fix |
|-------|-----------|-----|
| Seed=0 | Check KSampler widget_values[0] | Change to -1 |
| Missing BREAK | Search prompt text | Add BREAK between outfit and pose |
| Token not first | Check prompt start | Move (TOKEN:1.2) to beginning |
| CFG≠7 | Check widget_values[3] | Set to exactly 7 |
| Weight>1.2 | Regex search for \(.*?\:1\.[3-9]\) | Reduce to max 1.2 |
| Missing style lock | Check for "stylized 3D" | Add "stylized 3D fintech character" |
| Wrong model | Check checkpoint name | Use Juggernaut-XL_v9 |

---

### 4. Standard Poses (Generate One Workflow Per Pose)

**Generate workflows for these poses (or user-specified subset):**

**Required (Priority Order):**

1. **Portrait** - Head and shoulders, looking at camera
   - Priority: HIGHEST (40% of dataset)
   - Prompt suffix: `portrait shot, minimal background, looking at camera`

2. **Standing Confident** - Waist-up, professional stance
   - Priority: HIGH (20% of dataset)
   - Prompt suffix: `standing confidently, waist-up shot, professional pose`

3. **Action/Professional** - Character doing their job
   - Priority: HIGH (20% of dataset)
   - Prompt suffix: `[professional action], futuristic interface, dynamic pose`

4. **Side Profile** - Looking left or right
   - Priority: MEDIUM (10% of dataset)
   - Prompt suffix: `side profile view, looking to the right, analyzing data`

5. **Three-Quarter View** - 45-degree angle
   - Priority: MEDIUM (5% of dataset)
   - Prompt suffix: `three-quarter view, turned slightly to the side`

6. **Environmental/Full Body** - Full body with context
   - Priority: LOW (5% of dataset)
   - Prompt suffix: `full body shot, standing in futuristic [environment]`

7. **Detail Focus** - Close-up accessory/face
   - Priority: LOW (0-5% of dataset)
   - Prompt suffix: `close-up detail shot, focus on [accessory]`

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
      "widgets_values": ["Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors"],
      "title": "Juggernaut XL v9 Model"
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
      "title": "Negative Prompt (Enhanced)"
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
      "widgets_values": [-1, "randomize", 35, 7, "dpmpp_2m", "karras", 1],
      "title": "Generate (Steps:35, CFG:7, Seed:-1)"
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
      "title": "VAE Decode (Built-in)"
    },
    {
      "id": 7,
      "type": "SaveImage",
      "pos": [1650, 250],
      "size": [350, 300],
      "inputs": [{"name": "images", "type": "IMAGE", "link": 8}],
      "widgets_values": ["[token]_[pose]_juggernaut"],
      "title": "Save Images"
    },
    {
      "id": 10,
      "type": "Note",
      "pos": [50, 50],
      "size": [400, 140],
      "inputs": [],
      "outputs": [],
      "widgets_values": ["[CHARACTER] - [POSE] - Juggernaut XL v9\\n\\nSettings: Steps:35 | CFG:7 | Seed:-1\\nBatch: 2 images\\n\\nReferences:\\n- Skill: SKILLS/JUGGERNAUT_CHARACTER_SKILL.md\\n- Templates: SKILLS/PROMPT_TEMPLATES.md\\n- Validation: SKILLS/VALIDATION_GUIDE.md\\n- Spec: SKILLS/CHARACTER_SPEC_TEMPLATE.md"],
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
- Replace `POSITIVE_PROMPT_HERE` with the actual constructed prompt
- Replace `NEGATIVE_PROMPT_HERE` with the exact negative prompt from section 3
- Replace `[CHARACTER]`, `[POSE]`, `[token]` with actual values
- Ensure valid JSON (no trailing commas, proper quotes)

---

## STOP & VERIFY CHECKPOINTS

You MUST complete these 3 checkpoints before outputting any workflow. Do not skip.

### 🛑 CHECKPOINT 1: Positive Prompt Verification

**After constructing the positive prompt, STOP and verify:**

```
POSITIVE PROMPT VERIFICATION:
□ Token first? (character:1.2) at start
□ BREAK present? Exactly one occurrence
□ Visual anchors weighted? Hair, eyes, accessory at 1.1
□ Max weight ≤1.2? No element exceeds limit
□ Style lock included? "stylized 3D fintech character"
□ Quality boosters? "highly detailed, sharp focus, professional 3D render"
```

**If ANY check fails:**
- State which check failed
- Explain why it's wrong
- Show corrected version
- Re-verify

**Only proceed to Checkpoint 2 when ALL checks pass.**

---

### 🛑 CHECKPOINT 2: Settings Verification

**After configuring KSampler and model, STOP and verify:**

```
SETTINGS VERIFICATION:
□ Seed: -1 (NOT 0)
□ Steps: 35
□ CFG: 7
□ Sampler: dpmpp_2m
□ Scheduler: karras
□ Model: Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors
□ Resolution: 1024×1024
□ Batch Size: 2
```

**Show your work:**
```
Current values:
- Seed: -1 ✅
- Steps: 35 ✅
- CFG: 7 ✅
- Model: Juggernaut-XL_v9 ✅
```

**If ANY value is wrong:**
- Identify incorrect value
- Explain correct value
- Fix it
- Re-verify

**Only proceed to Checkpoint 3 when ALL values correct.**

---

### 🛑 CHECKPOINT 3: Final Validation

**Before outputting JSON, STOP and run 10-point checklist:**

```
FINAL VALIDATION (MANDATORY):
□ 1. Token Weight: (TOKEN:1.2) format, first position
□ 2. Trait Weights: Hair, eyes, accessory at (trait:1.1)
□ 3. BREAK Present: Exactly one BREAK keyword
□ 4. Pose Position: Pose/action AFTER BREAK
□ 5. Weight Limits: No element exceeds 1.2
□ 6. Negative Complete: Full enhanced negative used verbatim
□ 7. Settings Correct: Steps=35, CFG=7, Seed=-1
□ 8. Style Lock: "stylized 3D fintech character" included
□ 9. Quality Boosters: All quality keywords present
□ 10. Valid JSON: No syntax errors, proper formatting
```

**Display results:**
```
Validation Results:
✅ 1. Token Weight - PASS
✅ 2. Trait Weights - PASS
✅ 3. BREAK Present - PASS
✅ 4. Pose Position - PASS
✅ 5. Weight Limits - PASS
✅ 6. Negative Complete - PASS
✅ 7. Settings Correct - PASS
✅ 8. Style Lock - PASS
✅ 9. Quality Boosters - PASS
✅ 10. Valid JSON - PASS

✅ ALL CHECKS PASSED - Ready to output
```

**If ANY check fails:**
```
Validation Results:
✅ 1. Token Weight - PASS
❌ 2. Trait Weights - FAIL (eyes at 1.2, should be 1.1)
✅ 3. BREAK Present - PASS
...

❌ CHECKPOINT 3 FAILED
Fix: Change eye weight from 1.2 to 1.1
Re-run validation after fix.
```

**DO NOT OUTPUT WORKFLOW until all 10 checks show ✅**

---

## VALIDATION CHECKLIST (10-Point Verification)

Before outputting each workflow, verify:

- [ ] **1. Token Weight:** Character token is first with `(TOKEN:1.2)` format
- [ ] **2. Trait Weights:** Hair, eyes, accessory use `(trait:1.1)` format
- [ ] **3. BREAK Present:** BREAK keyword separates identity from action
- [ ] **4. Pose Position:** Pose/action appears AFTER BREAK
- [ ] **5. Weight Limits:** No element exceeds 1.2 weight
- [ ] **6. Negative Complete:** Full enhanced negative prompt used verbatim
- [ ] **7. Settings Correct:** Steps=35, CFG=7, Seed=-1, Model=Juggernaut-XL_v9
- [ ] **8. Style Lock:** "stylized 3D fintech character" in positive prompt
- [ ] **9. Quality Boosters:** "highly detailed, sharp focus, professional 3D render" included
- [ ] **10. Valid JSON:** No syntax errors, proper formatting

**If any check fails, fix it before outputting.**

**Remember:** You already passed Checkpoint 3 to get here. These are the same 10 checks - just the final confirmation.

---

## OUTPUT FORMAT

For each pose workflow, provide:

### 1. Character & Pose Summary
```
Character: [TOKEN] - [Role]
Pose: [Pose Name]
Priority: [High/Medium/Low]
Target Images: [X] (from dataset targets)
```

### 2. Complete Positive Prompt
```
(TOKEN:1.2), [ROLE], ([HAIR]:1.1), ([EYES]:1.1), [FACE], ([ACCESSORY]:1.1), [OUTFIT] BREAK
[POSE], [ENVIRONMENT], stylized 3D fintech character, highly detailed, sharp focus, professional 3D render
```

### 3. Complete Negative Prompt
```
[Exact negative prompt from section 3]
```

### 4. Filename
```
[token]_[pose]_juggernaut.json
```
Example: `luna_portrait_juggernaut.json`

### 5. Complete Workflow JSON
```json
[Valid JSON workflow]
```

### 6. Validation Confirmation
```
✅ All 10 validation checks passed
```

---

## EXAMPLE OUTPUT (Luna Portrait)

### Character & Pose Summary
```
Character: lunaAI - Blockchain Developer
Pose: Portrait
Priority: HIGHEST
Target Images: 12-16 (40% of dataset)
```

### Complete Positive Prompt
```
(lunaAI:1.2), blockchain developer, (long dark blue hair with glowing cyan tips:1.1), (electric purple eyes with digital patterns:1.1), angular focused face, (data visor with holographic cyan interface:1.1), high-tech jacket with LED panels BREAK
portrait shot, minimal background, looking at camera, cool purple and cyan neon lighting, stylized 3D fintech character, highly detailed, sharp focus, professional 3D render
```

### Complete Negative Prompt
```
low quality, blurry, distorted face, bad anatomy, bad hands, extra fingers, deformed, ugly, duplicate body parts, multiple characters, 2d, flat, painting, drawing, sketch, photorealistic, realistic, oil painting, watercolor, illustration, anime style, manga, cel shaded, inconsistent lighting, asymmetric eyes, disfigured, mutated, poorly drawn face, poorly drawn hands, missing fingers, extra limbs, fused fingers, too many fingers, long neck, cross-eyed, text, watermark, logo, signature
```

### Filename
```
luna_portrait_juggernaut.json
```

### Complete Workflow JSON
```json
[JSON would go here with above prompts inserted]
```

### Validation Confirmation
```
✅ All 10 validation checks passed
```

---

## GENERATION INSTRUCTIONS

**Generate workflows for ALL 7 poses, or ask user which specific poses they want.**

**For each pose:**
1. **Construct positive prompt** using character spec + pose template
2. **CHECKPOINT 1:** Verify positive prompt (STOP - run checklist)
3. **Configure settings** in KSampler and model nodes
4. **CHECKPOINT 2:** Verify settings (STOP - confirm all values)
5. **Use exact negative prompt** from section 3
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

- **Full Skill Documentation:** `SKILLS/JUGGERNAUT_CHARACTER_SKILL.md`
- **Pose Templates:** `SKILLS/PROMPT_TEMPLATES.md`
- **Validation Rules:** `SKILLS/VALIDATION_GUIDE.md`
- **Character Spec Format:** `SKILLS/CHARACTER_SPEC_TEMPLATE.md`
- **Existing Characters:** `CHARACTERS.md` (Nova & Athena examples)

---

## READY TO GENERATE?

**Paste your character spec above, then generate the workflows!**

**Don't have a complete spec?** No problem - I'll ask clarifying questions and guide you through creating one.

**Generation Process:**
1. **Interactive Mode** - I'll check if your spec is complete
2. **Ask questions** if anything is missing (with examples from Luna/Nova/Athena)
3. **Validate in real-time** as you provide information
4. **Complete all 3 checkpoints** for each workflow
5. **Output only after validation** passes

**Remember:**
- One workflow per pose
- 7 workflows total (or specify which poses you want)
- All 3 checkpoints must pass for each workflow
- Use STOP & VERIFY checkpoints - don't skip them

**Let's build your character workflows! Paste your spec or tell me about your character:**
