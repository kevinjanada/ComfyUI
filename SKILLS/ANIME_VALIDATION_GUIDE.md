# Anime Character Validation Guide (Animagine XL 4.0)

**Version:** 1.0  
**Purpose:** 10-point validation checklist for anime character workflows

---

## Quick Validation

**Run this before generating ANY images:**

```bash
# Check 5 critical items in 30 seconds:

1. Gender tag first? (1girl/1boy) ✓
2. No weight syntax? (no :1.x) ✓
3. Quality tags at END? ✓
4. Settings: Steps=28, CFG=5? ✓
5. Model: animagine-xl-4.0-opt? ✓

All 5 must pass or workflow is invalid.
```

---

## Full 10-Point Validation Checklist

### Before Generating Images

**Check each item and mark ✓ or ✗:**

#### 1. ✓ Gender Tag Present
- [ ] Prompt starts with `1girl` or `1boy`
- [ ] No other text before gender tag
- [ ] Correct format (not "female", "girl", etc.)

**Why:** Animagine XL 4.0 requires gender tag for proper generation

**Check:** Look at start of positive prompt in CLIPTextEncode node

---

#### 2. ✓ Character Token Included
- [ ] Token appears after gender tag
- [ ] Format: `nameAI` (ends with AI)
- [ ] Consistent across all workflows

**Why:** Token ensures character consistency for LoRA training

**Check:** Verify token in positive prompt (e.g., `hikariAI`, `aikaAI`)

---

#### 3. ✓ No Weight Syntax
- [ ] No `(token:1.x)` anywhere in prompt
- [ ] No `(hair:1.x)` or similar
- [ ] Plain tags only

**Why:** Animagine XL 4.0 uses tag ordering, not weighted syntax

**Check:** Search prompt for `:` and `(` characters - should be none except in tags

**Common mistake:** Copying JuggernautXL workflows with `(token:1.2)`

---

#### 4. ✓ Tag-Based Prompting
- [ ] Comma-separated tags only
- [ ] No natural language (no "with", "who", "and", "wearing")
- [ ] No sentences or phrases

**Why:** Model trained on tag datasets, not natural language

**Check:** Prompt should read like: `1girl, token, hair, eyes, outfit`

**❌ Wrong:** `1girl, hikariAI who has blue hair and wears a jacket`  
**✅ Right:** `1girl, hikariAI, blue hair, jacket`

---

#### 5. ✓ Quality Tags at End
- [ ] `masterpiece` at end
- [ ] `high score` at end
- [ ] `great score` at end
- [ ] `absurdres` at end
- [ ] No quality tags at beginning or middle

**Why:** Quality tags at end maximize impact without diluting character tags

**Check:** Look at end of positive prompt - should end with quality tags

**Order matters:** Character first, quality last

---

#### 6. ✓ Correct Model
- [ ] CheckpointLoaderSimple shows `animagine-xl-4.0-opt.safetensors`
- [ ] Not `Juggernaut-XL_v9` or other model
- [ ] Model file exists in `models/checkpoints/`

**Why:** Wrong model = completely different style

**Check:** Verify `widgets_values` in CheckpointLoaderSimple node

**File size:** Should be ~6.5GB

---

#### 7. ✓ Correct Steps
- [ ] KSampler shows `28` in steps field
- [ ] Not 25, 30, or 35
- [ ] Exactly 28

**Why:** 28 steps optimal for Animagine XL 4.0 (converges faster than 3D models)

**Check:** Verify `widgets_values[2]` in KSampler node

**Common mistake:** Using JuggernautXL setting of 35 steps

---

#### 8. ✓ Correct CFG Scale
- [ ] KSampler shows `5` in CFG field
- [ ] Not 4, 6, or 7
- [ ] Exactly 5

**Why:** CFG 5 is sweet spot for anime (higher causes artifacts)

**Check:** Verify `widgets_values[3]` in KSampler node

**Common mistake:** Using JuggernautXL setting of CFG 7

---

#### 9. ✓ Correct Sampler
- [ ] KSampler shows `euler_ancestral` (or `euler a`)
- [ ] Not `dpmpp_2m` or other sampler
- [ ] Euler Ancestral recommended for anime

**Why:** Euler a produces smoother anime aesthetics

**Check:** Verify `widgets_values[4]` in KSampler node

**Alternative:** `euler` also acceptable, but `euler_ancestral` preferred

---

#### 10. ✓ Valid JSON
- [ ] No syntax errors in workflow file
- [ ] Proper JSON formatting
- [ ] Can load in ComfyUI without errors

**Why:** Invalid JSON = workflow won't load

**Check:** Try loading workflow in ComfyUI - should load without errors

---

## Validation Results

### If ALL checks pass:
```
✅✅✅ VALIDATION PASSED ✅✅✅

All 10 checks passed. Workflow is ready for generation.

Generate 30-40 images following dataset targets:
- Portrait (40%): 12-16 images
- Waist-up (40%): 12-16 images  
- Full body (20%): 6-8 images
```

### If ANY check fails:
```
❌❌❌ VALIDATION FAILED ❌❌❌

Failed checks:
- Check #3: Weight syntax found (remove all :1.x)
- Check #7: Steps = 35 (change to 28)

Fix these issues before generating.
```

---

## Common Validation Failures

### Failure #1: Weight Syntax Present
**Problem:** Using `(token:1.2)` from JuggernautXL  
**Fix:** Remove all `:1.x` weights, use plain tags  
**Example:** `(hikariAI:1.2)` → `hikariAI`

### Failure #2: Wrong Settings
**Problem:** Steps=35, CFG=7 (JuggernautXL settings)  
**Fix:** Change to Steps=28, CFG=5  
**Also check:** Sampler should be `euler_ancestral`

### Failure #3: Missing Gender Tag
**Problem:** Prompt starts with token, not gender  
**Fix:** Add `1girl` or `1boy` at very beginning  
**Example:** `hikariAI, blue hair` → `1girl, hikariAI, blue hair`

### Failure #4: Quality Tags in Wrong Position
**Problem:** `masterpiece` at start of prompt  
**Fix:** Move quality tags to END of prompt  
**Example:** `masterpiece, 1girl, hikariAI...` → `1girl, hikariAI... masterpiece`

### Failure #5: Natural Language
**Problem:** Using sentences instead of tags  
**Fix:** Convert to comma-separated tags  
**Example:** `girl with blue hair wearing a jacket` → `1girl, blue hair, jacket`

### Failure #6: Wrong Model
**Problem:** Using JuggernautXL or other model  
**Fix:** Change to `animagine-xl-4.0-opt.safetensors`  
**Download:** From HuggingFace if not present

---

## Pre-Flight Checklist

**Before running first generation:**

- [ ] Model downloaded (~6.5GB)
- [ ] Workflow loaded in ComfyUI
- [ ] All 10 validation checks pass
- [ ] Negative prompt is anime version
- [ ] Output folder ready
- [ ] Sufficient disk space (~2GB for 40 images)
- [ ] ComfyUI running with ROCm

**Settings confirmation:**
- [ ] Steps: 28
- [ ] CFG: 5
- [ ] Sampler: euler_ancestral
- [ ] Resolution: 1024×1024
- [ ] Batch: 2

---

## Batch Generation Validation

**When generating multiple poses:**

For EACH workflow file:
1. Load workflow in ComfyUI
2. Run through 10-point checklist
3. Generate test batch (2 images)
4. Verify output looks like anime (not 3D, not realistic)
5. If good, proceed with full generation

**Red flags to stop generation:**
- Images look photorealistic → Check negative prompt
- Images look 3D rendered → Check model and style tags
- Character inconsistent → Check token and prompts
- Poor quality → Check quality tags and steps

---

## Post-Generation Validation

**After generating images:**

### Visual Quality Check
- [ ] Anime style (not realistic, not 3D)
- [ ] Consistent character face across images
- [ ] Proper anime proportions (large eyes, small nose)
- [ ] No obvious anatomy errors
- [ ] Color scheme matches character spec

### Character Consistency Check
- [ ] Same hair color in all images
- [ ] Same eye color in all images
- [ ] Same outfit in all images
- [ ] Signature accessory present
- [ ] Character recognizable in different poses

### Dataset Balance Check
- [ ] Portrait: 12-16 images (40%)
- [ ] Waist-up: 12-16 images (40%)
- [ ] Full body: 6-8 images (20%)
- [ ] Total: 30-40 images

### Caption Check
- [ ] All images have caption files
- [ ] Format: `TOKEN, role` (under 10 words)
- [ ] No quality tags in captions
- [ ] Consistent naming

---

## Validation Tools

### Quick Command-Line Checks

**Check JSON validity:**
```bash
python -m json.tool workflow.json > /dev/null && echo "Valid JSON" || echo "Invalid JSON"
```

**Check for weight syntax:**
```bash
grep -o ':[0-9]\.[0-9]' workflow.json && echo "Found weights!" || echo "No weights found"
```

**Check model name:**
```bash
grep "animagine-xl-4.0-opt" workflow.json && echo "Correct model" || echo "Wrong model!"
```

---

## Troubleshooting Failed Validations

### "Check #3: Weight syntax found"
**Solution:** Remove all instances of `:1.x` from prompts
- Open workflow in text editor
- Find and replace all `:1.1` and `:1.2` with nothing
- Remove parentheses around weighted terms

### "Check #6: Wrong model"
**Solution:** 
1. Download animagine-xl-4.0-opt if not present
2. Edit workflow JSON, replace model name
3. Or reload workflow in ComfyUI and select correct model

### "Check #7-9: Wrong settings"
**Solution:** Edit KSampler node in ComfyUI
- Steps: change to 28
- CFG: change to 5
- Sampler: change to euler_ancestral

### "Check #10: Invalid JSON"
**Solution:**
1. Check for trailing commas in JSON
2. Ensure all quotes are properly closed
3. Validate JSON online or with python tool
4. Recreate workflow if corrupted

---

## Best Practices

### Always Validate
- Run 10-point checklist before first generation
- Validate each new pose workflow
- Validate after any edits

### Test First
- Generate 2 test images before full batch
- Check quality before generating 30-40 images
- Fix issues early

### Document Changes
- Keep notes on what works
- Save successful workflow variations
- Track which settings produce best results

### Iterate
- First generation rarely perfect
- Adjust prompts based on results
- Fine-tune over multiple attempts

---

## Summary

**Critical 5 checks (do these first):**
1. ✓ Gender tag first
2. ✓ No weight syntax
3. ✓ Quality tags at end
4. ✓ Settings: Steps=28, CFG=5
5. ✓ Model: animagine-xl-4.0-opt

**Full 10 checks (before generation):**
1. ✓ Gender tag
2. ✓ Character token
3. ✓ No weights
4. ✓ Tag-based
5. ✓ Quality tags position
6. ✓ Correct model
7. ✓ Steps = 28
8. ✓ CFG = 5
9. ✓ Sampler = euler_ancestral
10. ✓ Valid JSON

**Remember:** Validation catches errors BEFORE wasting time on bad generations. Always validate!

---

## References

- **Anime Skill:** `SKILLS/ANIME_CHARACTER_SKILL.md`
- **Workflow Generator:** `SKILLS/ANIME_WORKFLOW_GENERATOR_PROMPT.md`
- **Prompt Templates:** `SKILLS/ANIME_PROMPT_TEMPLATES.md`
- **Spec Template:** `SKILLS/ANIME_CHARACTER_SPEC_TEMPLATE.md`
