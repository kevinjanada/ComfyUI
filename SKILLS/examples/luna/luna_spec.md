# Luna Character Specification

**Example character demonstrating proper spec format.**

Use this as a reference when filling out CHARACTER_SPEC_TEMPLATE.md for your own characters.

---

## Basic Information

- **Token:** lunaAI
- **Name:** Luna
- **Role/Profession:** Blockchain Developer

---

## Visual Identity (Visual Anchors - Most Important!)

### Hair (Visual Anchor #1)
- **Color:** Long dark blue
- **Style/Length:** Flowing, waist-length
- **Special Features:** Glowing cyan tips that pulse with data flow
- **Prompt Weight:** 1.1 (critical for consistency)

### Eyes (Visual Anchor #2)
- **Color:** Electric purple
- **Effect:** Digital pattern overlay with subtle luminescent glow
- **Prompt Weight:** 1.1 (critical for consistency)

### Face Structure
- **General Shape:** Angular with sharp features
- **Expression:** Focused, analytical, determined

### Outfit
- **Type:** High-tech jacket with holographic panels
- **Primary Color:** Dark navy (#1E293B)
- **Secondary Color:** Cyan LED accents (#06B6D4)
- **Details:** Circuit patterns that pulse with data flow across the fabric

### Signature Accessory (Visual Anchor #3 - Unique Identifier)
- **Item:** Data Visor
- **Description:** Translucent AR glasses displaying real-time code and blockchain data
- **Color/Effect:** Holographic cyan interface with scrolling data
- **Prompt Weight:** 1.1 (ensures consistent presence)

---

## Color Palette

- **Primary:** #8B5CF6 (vivid purple)
- **Secondary:** #06B6D4 (bright cyan)
- **Tertiary:** #1E293B (dark navy)
- **Lighting:** Cool purple and cyan neon lighting with holographic glow effects

---

## Signature Elements (Environment)

- [x] Floating holographic code blocks
- [x] Blockchain network node visualizations
- [x] Cryptocurrency price tickers in holographic displays
- [ ] Smart contract flow diagrams (optional)

---

## Dataset Targets

- **Total Images Needed:** 30-40
- **Portrait (40%):** 12-16 images
- **Waist-Up (40%):** 12-16 images
- **Full Body/Environmental (20%):** 6-8 images

---

## Pose Checklist

### Standard Poses

- [x] **1. Portrait** - Head and shoulders, camera facing
- [x] **2. Standing Confident** - Waist-up, professional stance
- [x] **3. Action/Professional** - Coding, debugging, analyzing blockchain
- [ ] **4. Side Profile** - Left/right view
- [ ] **5. Three-Quarter View** - 45-degree angle
- [ ] **6. Environmental/Full Body** - Full body with context
- [ ] **7. Detail Focus** - Close-up data visor or face

**Workflows Generated:** 3 (Portrait, Standing, Action)

---

## Caption Format

**Simple:** `lunaAI, blockchain developer`

**Detailed (optional):** `lunaAI, blockchain developer, portrait shot`

---

## Prompt Examples

### Portrait
```
(lunaAI:1.2), blockchain developer, (long dark blue hair with glowing cyan tips:1.1), (electric purple eyes with digital patterns:1.1), angular focused face, (data visor with holographic cyan interface:1.1), high-tech jacket with LED panels BREAK
portrait shot, minimal background, looking at camera, cool purple and cyan neon lighting, stylized 3D fintech character, highly detailed, sharp focus, professional 3D render
```

### Standing Confident
```
(lunaAI:1.2), blockchain developer, (long dark blue hair with glowing cyan tips:1.1), (electric purple eyes with digital patterns:1.1), angular focused face, (data visor with holographic cyan interface:1.1), high-tech jacket with LED panels BREAK
standing confidently, arms crossed, waist-up shot, surrounded by floating holographic code blocks, cool purple and cyan neon lighting, stylized 3D fintech character, highly detailed, sharp focus, professional 3D render
```

### Action/Professional
```
(lunaAI:1.2), blockchain developer, (long dark blue hair with glowing cyan tips:1.1), (electric purple eyes with digital patterns:1.1), angular focused face, (data visor with holographic cyan interface:1.1), high-tech jacket with LED panels BREAK
analyzing blockchain network visualizations, pointing at floating code blocks, futuristic development environment, cool purple and cyan neon lighting, stylized 3D fintech character, highly detailed, sharp focus, professional 3D render
```

---

## Negative Prompt (Standard for All)

```
low quality, blurry, distorted face, bad anatomy, bad hands, extra fingers, deformed, ugly, duplicate body parts, multiple characters, 2d, flat, painting, drawing, sketch, photorealistic, realistic, oil painting, watercolor, illustration, anime style, manga, cel shaded, inconsistent lighting, asymmetric eyes, disfigured, mutated, poorly drawn face, poorly drawn hands, missing fingers, extra limbs, fused fingers, too many fingers, long neck, cross-eyed, text, watermark, logo, signature
```

---

## Workflow Files

See accompanying JSON files:
- `luna_portrait_juggernaut.json`
- `luna_standing_juggernaut.json`
- `luna_action_juggernaut.json`

---

## References

- **Character Template:** `SKILLS/CHARACTER_SPEC_TEMPLATE.md`
- **Workflow Generator:** `SKILLS/WORKFLOW_GENERATOR_PROMPT.md`
- **Skill Guide:** `SKILLS/JUGGERNAUT_CHARACTER_SKILL.md`
- **Validation:** `SKILLS/VALIDATION_GUIDE.md`
