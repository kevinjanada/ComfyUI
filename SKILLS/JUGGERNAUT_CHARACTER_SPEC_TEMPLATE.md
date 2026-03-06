# Character Specification Template

Use this template to define a new character for JuggernautXL workflow generation.

Fill out all sections completely for best results.

---

## Basic Information

- **Token:** [Use format: nameAI, e.g., lunaAI, victorAI, auroraAI]
- **Name:** [Character name]
- **Role/Profession:** [e.g., blockchain developer, DeFi analyst, crypto trader, AI strategist]

---

## Visual Identity (Visual Anchors - Most Important!)

These three elements are the most critical for character consistency. Weight them at 1.1 in prompts.

### Hair (Visual Anchor #1)
- **Color:** [e.g., long dark blue, short silver, platinum blonde]
- **Style/Length:** [e.g., flowing, pixie cut, braided, spiky]
- **Special Features:** [e.g., glowing tips, holographic strands, neon highlights]
- **Prompt Weight:** 1.1 (critical for consistency)

### Eyes (Visual Anchor #2)
- **Color:** [e.g., electric purple, glowing teal, vibrant amber]
- **Effect:** [e.g., luminescent glow, digital patterns, subtle shimmer]
- **Prompt Weight:** 1.1 (critical for consistency)

### Face Structure
- **General Shape:** [e.g., angular, soft, youthful, mature, oval]
- **Expression:** [e.g., confident, analytical, friendly, serious]
- **Features:** [e.g., high cheekbones, sharp jawline, soft features]

### Outfit
- **Type:** [e.g., futuristic bodysuit, tech robe, armored jacket, formal suit]
- **Primary Color:** [main outfit color]
- **Secondary Color:** [accents, trim]
- **Details:** [e.g., glowing circuits, LED panels, holographic trim, metallic accents]

### Signature Accessory (Visual Anchor #3 - Unique Identifier)
- **Item:** [e.g., data visor, neural crown, holographic halo, energy wings, tech mask]
- **Description:** [what makes it distinctive and recognizable]
- **Color/Effect:** [e.g., pulsing purple light, holographic cyan display, glowing gold edges]
- **Prompt Weight:** 1.1 (ensures consistent presence)

**Why these matter:** Hair, eyes, and signature accessory are the three visual anchors that make your character instantly recognizable. Weighting them ensures they appear consistently across all generated images.

---

## Color Palette

Use specific hex codes to prevent color drift:

- **Primary:** #HEXCODE [main character color, used in outfit/accessories]
- **Secondary:** #HEXCODE [accent color, used in lighting/effects]
- **Tertiary:** #HEXCODE [background/dark color]
- **Lighting:** [warm/cool, e.g., "cool cyan neon lighting" or "warm golden ambient light"]

**Example:**
- Primary: #8B5CF6 (vivid purple)
- Secondary: #06B6D4 (bright cyan)
- Tertiary: #1E293B (dark navy)
- Lighting: Cool purple and cyan neon lighting

---

## Signature Elements (Environment)

List 2-4 environmental elements that define this character's professional context:

- [ ] Element 1: [e.g., floating holographic code blocks]
- [ ] Element 2: [e.g., blockchain network visualizations]
- [ ] Element 3: [e.g., cryptocurrency price tickers]
- [ ] Element 4: [optional - e.g., smart contract diagrams]

These appear in the BREAK section of prompts to establish context.

---

## Dataset Targets

Recommended distribution for LoRA training:

- **Total Images Needed:** 30-40
- **Portrait (40%):** 12-16 images
  - Head and shoulders only
  - Face consistency is most important
  - Various expressions, same identity
  
- **Waist-Up (40%):** 12-16 images
  - Shows outfit details
  - Professional poses
  - Avoids hand generation issues
  
- **Full Body/Environmental (20%):** 6-8 images
  - Complete character in context
  - Environmental storytelling
  - Use sparingly (harder to get perfect)

**Why this ratio:** Portraits ensure face consistency (most critical), waist-up shows outfits without hand problems, full-body adds context but is most prone to artifacts.

---

## Pose Checklist (7 Standard Poses)

Select which poses you need. All 7 are recommended for complete dataset diversity.

### Standard Poses (Industry Best Practice)

- [ ] **1. Portrait**
  - **Description:** Head and shoulders, facing camera
  - **Use:** Profile pictures, avatar consistency
  - **Priority:** HIGHEST (40% of dataset)
  - **Prompt:** `portrait shot, looking at camera, minimal background`

- [ ] **2. Standing Confident**
  - **Description:** Waist-up, professional stance, arms at sides or crossed
  - **Use:** Hero shots, professional presence
  - **Priority:** HIGH (20% of dataset)
  - **Prompt:** `standing confidently, waist-up shot, professional pose`

- [ ] **3. Action/Professional**
  - **Description:** Character performing their professional role
  - **Use:** Context shots, storytelling
  - **Priority:** HIGH (20% of dataset)
  - **Prompt:** `[professional action], futuristic interface, dynamic pose`

- [ ] **4. Side Profile**
  - **Description:** Looking left or right, full profile view
  - **Use:** Face consistency from angles, variety
  - **Priority:** MEDIUM (10% of dataset)
  - **Prompt:** `side profile view, looking to the right, analyzing data`

- [ ] **5. Three-Quarter View**
  - **Description:** 45-degree angle, dynamic but still recognizable
  - **Use:** Dynamic portraits, artistic variety
  - **Priority:** MEDIUM (5% of dataset)
  - **Prompt:** `three-quarter view, turned slightly to the side`

- [ ] **6. Environmental/Full Body**
  - **Description:** Full body with background context
  - **Use:** Establishing shots, world-building
  - **Priority:** LOW (5% of dataset)
  - **Prompt:** `full body shot, standing in futuristic [environment]`

- [ ] **7. Detail Focus**
  - **Description:** Close-up of face or signature accessory
  - **Use:** Accessory consistency, detail emphasis
  - **Priority:** LOW (optional, 0-5%)
  - **Prompt:** `close-up detail shot, focus on [accessory/face]`

### Custom Poses (Add Your Own)

- [ ] **Custom 1:** [Name] - [Description]
- [ ] **Custom 2:** [Name] - [Description]

---

## Caption Format for LoRA Training

Captions should be SHORT. Long captions confuse the model.

### Simple Format (Recommended)
```
TOKEN, role
```
**Example:** `lunaAI, blockchain developer`

### Detailed Format (Optional - Use Sparingly)
```
TOKEN, role, pose_keyword
```
**Example:** `lunaAI, blockchain developer, portrait shot`

**Rules:**
- Always include the character token first
- Keep under 10 words
- Don't include quality keywords (masterpiece, best quality, etc.)
- Don't include style keywords (stylized 3D, etc.)
- Pose keywords are optional

---

## Workflow Generation

Once this spec is complete:

1. Copy your filled spec
2. Open `SKILLS/WORKFLOW_GENERATOR_PROMPT.md`
3. Paste your spec at the designated section
4. Give the complete prompt to an LLM (ChatGPT, Claude, etc.)
5. LLM will generate workflow JSON files
6. Save each workflow as: `[character]_[pose]_juggernaut.json`

---

## References

- **Skill Guide:** `SKILLS/JUGGERNAUT_CHARACTER_SKILL.md` - Complete best practices
- **Pose Templates:** `SKILLS/PROMPT_TEMPLATES.md` - Ready-to-use pose variations
- **Validation:** `SKILLS/VALIDATION_GUIDE.md` - What to check before generating
- **Workflow Generator:** `SKILLS/WORKFLOW_GENERATOR_PROMPT.md` - LLM prompt template

---

## Example: Completed Spec (Luna - Blockchain Developer)

### Basic Information
- **Token:** lunaAI
- **Name:** Luna
- **Role/Profession:** Blockchain Developer

### Visual Identity

**Hair:**
- Color: Long dark blue
- Style/Length: Flowing, waist-length
- Special Features: Glowing cyan tips
- Weight: 1.1

**Eyes:**
- Color: Electric purple
- Effect: Digital pattern overlay, subtle glow
- Weight: 1.1

**Face:**
- Structure: Angular, sharp features
- Expression: Focused, analytical

**Outfit:**
- Type: High-tech jacket with holographic panels
- Primary: Dark navy (#1E293B)
- Secondary: Cyan LED accents (#06B6D4)
- Details: Circuit patterns that pulse with data flow

**Signature Accessory:**
- Item: Data Visor
- Description: Translucent AR glasses displaying code
- Color/Effect: Holographic cyan interface
- Weight: 1.1

### Color Palette
- **Primary:** #8B5CF6 (vivid purple)
- **Secondary:** #06B6D4 (bright cyan)
- **Tertiary:** #1E293B (dark navy)
- **Lighting:** Cool purple and cyan neon lighting

### Signature Elements
- [x] Floating holographic code blocks
- [x] Blockchain network node visualizations
- [x] Cryptocurrency price tickers
- [ ] Smart contract flow diagrams

### Dataset Targets
- **Total:** 30-40 images
- **Portrait (40%):** 12-16 images
- **Waist-Up (40%):** 12-16 images
- **Full Body (20%):** 6-8 images

### Poses
- [x] 1. Portrait
- [x] 2. Standing Confident
- [x] 3. Action/Professional
- [x] 4. Side Profile
- [ ] 5. Three-Quarter View
- [ ] 6. Environmental/Full Body
- [ ] 7. Detail Focus

### Caption Format
**Simple:** `lunaAI, blockchain developer`

---

## Next Steps

1. Fill out this template for your character
2. Review the example (Luna) for guidance
3. Use the Workflow Generator to create workflows
4. Generate 30-40 images following the dataset targets
5. Curate the best images for LoRA training

**Ready? Start filling out the sections above!**
