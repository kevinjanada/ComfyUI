# Luna Example Character

This folder contains a complete example character specification and workflows to demonstrate the proper format.

## What's Included

### Character Specification
- **`luna_spec.md`** - Complete filled-out character spec template
  - Visual identity (hair, eyes, outfit, accessory)
  - Color palette with hex codes
  - Dataset targets (30-40 images)
  - Pose checklist
  - Prompt examples

### Workflow Files
Three example workflows generated from the spec:

1. **`luna_portrait_juggernaut.json`**
   - Pose: Portrait (head and shoulders)
   - Priority: HIGHEST (40% of dataset)
   - Target: 12-16 images

2. **`luna_standing_juggernaut.json`**
   - Pose: Standing Confident (waist-up)
   - Priority: HIGH (20% of dataset)
   - Target: 8-12 images

3. **`luna_action_juggernaut.json`**
   - Pose: Action/Professional (character working)
   - Priority: HIGH (20% of dataset)
   - Target: 8-12 images

## How to Use These Examples

### 1. Study the Spec
Open `luna_spec.md` and see how a complete character is defined:
- Token format: `lunaAI`
- Visual anchors weighted at 1.1
- Color palette with specific hex codes
- Dataset distribution (40/40/20 split)

### 2. Examine the Workflows
Each JSON file shows:
- Proper JuggernautXL settings (Steps:35, CFG:7, Seed:-1)
- Prompt structure with BREAK keyword
- Weighted tokens: `(lunaAI:1.2)`, `(hair:1.1)`, etc.
- Enhanced negative prompt
- Style lock: "stylized 3D fintech character"

### 3. Create Your Own Character

**Step 1:** Copy the template
```bash
cp SKILLS/CHARACTER_SPEC_TEMPLATE.md my_character_spec.md
```

**Step 2:** Fill it out following Luna's example
- Use the same structure
- Define your visual anchors
- Specify color palette
- Select your poses

**Step 3:** Generate workflows
1. Open `SKILLS/WORKFLOW_GENERATOR_PROMPT.md`
2. Copy the entire prompt
3. Paste into ChatGPT, Claude, or similar LLM
4. At "[PASTE YOUR CHARACTER SPEC HERE]", paste your filled spec
5. LLM will generate workflow JSON files
6. Save them as `[character]_[pose]_juggernaut.json`

**Step 4:** Generate images
1. Load a workflow in ComfyUI
2. Click "Queue Prompt"
3. Generate 4-6 images per pose
4. Keep the best 1-2
5. Repeat for all poses
6. Aim for 30-40 total images

## Character Summary: Luna

**Token:** lunaAI  
**Role:** Blockchain Developer  
**Visual Style:** High-tech, holographic, neon

**Key Visual Anchors:**
- Hair: Long dark blue with glowing cyan tips (1.1)
- Eyes: Electric purple with digital patterns (1.1)
- Accessory: Data visor with holographic cyan interface (1.1)

**Color Palette:**
- Primary: #8B5CF6 (vivid purple)
- Secondary: #06B6D4 (bright cyan)
- Tertiary: #1E293B (dark navy)

**Signature Elements:**
- Floating holographic code blocks
- Blockchain network visualizations
- Cryptocurrency price tickers

## Validation

Each workflow has been validated against:
- ✅ `SKILLS/JUGGERNAUT_CHARACTER_SKILL.md` - Best practices
- ✅ `SKILLS/PROMPT_TEMPLATES.md` - Pose structure
- ✅ `SKILLS/VALIDATION_GUIDE.md` - 10-point checklist

## References

- **Character Template:** `SKILLS/CHARACTER_SPEC_TEMPLATE.md`
- **Generator Prompt:** `SKILLS/WORKFLOW_GENERATOR_PROMPT.md`
- **Skill Guide:** `SKILLS/JUGGERNAUT_CHARACTER_SKILL.md`
- **Validation:** `SKILLS/VALIDATION_GUIDE.md`

---

**Ready to create your own character?** Start by copying the spec template and following Luna's example!
