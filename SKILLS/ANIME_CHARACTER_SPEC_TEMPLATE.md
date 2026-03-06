# Anime Character Specification Template (Animagine XL 4.0)

Use this template to define a new anime-style character for Animagine XL 4.0 workflow generation.

Fill out all sections completely for best results.

---

## Basic Information

- **Token:** [Use format: nameAI, e.g., lunaAI, aikaAI, yukiAI]
- **Gender:** [1girl or 1boy - REQUIRED for Animagine XL 4.0]
- **Name:** [Character name]
- **Role/Profession:** [e.g., AI researcher, blockchain developer, crypto trader]

---

## Visual Identity (Anime Style)

### Hair (Anime Style)
- **Color:** [e.g., neon blue, silver white, pastel pink]
- **Style/Length:** [e.g., short spiky, long flowing, twin tails, bob cut]
- **Special Features:** [e.g., gradient tips, glowing strands, ahoge (cowlick)]
- **Anime Notes:** Consider dynamic hair movement for action poses

### Eyes (Most Critical in Anime!)
- **Color:** [e.g., electric yellow, deep purple, crystal blue]
- **Style:** [e.g., large expressive, half-lidded cool, starry excited]
- **Highlights:** [e.g., star-shaped highlights, multiple light reflections, gradient]
- **Anime Notes:** Eyes are the window to anime character soul - be detailed!

### Face Structure (Anime Proportions)
- **Face Shape:** [e.g., soft round, sharp angular, heart-shaped]
- **Expression Type:** [e.g., energetic smile, cool confident, serious focused]
- **Features:** [e.g., small anime nose, defined jawline, soft cheeks]
- **Anime Notes:** Typical anime proportions - larger eyes, smaller nose than realistic

### Outfit (Anime + Tech Fusion)
- **Type:** [e.g., futuristic school uniform, tech bodysuit, modern casual]
- **Primary Color:** [main outfit color]
- **Secondary Color:** [accents, trim]
- **Details:** [e.g., glowing circuits, holographic elements, tech accessories]
- **Anime Notes:** Balance anime aesthetics with futuristic tech elements

### Signature Accessory (Unique Identifier)
- **Item:** [e.g., cyber visor, holographic halo, data tablet]
- **Description:** [what makes it distinctive]
- **Color/Effect:** [e.g., pulsing neon light, holographic display]
- **Anime Notes:** Should be visually striking and memorable

---

## Color Palette (Anime Style)

Use vibrant anime colors:

- **Primary:** #HEXCODE [main character color]
- **Secondary:** #HEXCODE [accent color]
- **Tertiary:** #HEXCODE [background/dark color]
- **Lighting:** [e.g., "cool neon glow", "warm sunset lighting", "cyberpunk ambient"]

**Anime Color Tips:**
- Use saturated colors for impact
- Consider color psychology (blue=trust, purple=mystery, yellow=energy)
- Gradients work well in anime style

**Example:**
- Primary: #00BFFF (electric blue)
- Secondary: #9B59FF (neon purple)
- Tertiary: #0B0F1A (dark navy)
- Lighting: Cool electric blue and neon purple ambient glow

---

## Signature Elements (Environment)

List 2-4 environmental elements for professional context:

- [ ] Element 1: [e.g., floating holographic displays]
- [ ] Element 2: [e.g., data visualization screens]
- [ ] Element 3: [optional - e.g., AI assistant drone]
- [ ] Element 4: [optional - e.g., crypto price charts]

**Anime Notes:** These add context while keeping anime aesthetic

---

## Anime Style Tags

Select the anime style for consistency:

- [x] **Modern Anime 2020s** - Clean, sharp, detailed (RECOMMENDED)
- [ ] **Late 2010s** - Slightly softer, vibrant colors
- [ ] **Mid 2010s** - Classic moe style
- [ ] **Early 2010s** - More detailed shading

**Recommended:** `newest` tag for modern anime style

---

## Dataset Targets

Recommended distribution for LoRA training:

- **Total Images Needed:** 30-40
- **Portrait (40%):** 12-16 images
  - Focus on face and eye consistency (critical in anime!)
  - Various expressions, same identity
  
- **Waist-Up (40%):** 12-16 images
  - Shows outfit and tech details
  - Professional and dynamic poses
  
- **Full Body/Environmental (20%):** 6-8 images
  - Complete character in anime tech environment
  - Use sparingly (anatomy challenges)

**Why this ratio:** Anime faces are most critical for recognition, waist-up shows tech outfit details without hand issues.

---

## Pose Checklist (7 Standard Poses)

Select which poses you need. All 7 recommended for complete diversity.

### Standard Poses

- [ ] **1. Portrait**
  - **Description:** Face close-up, looking at viewer
  - **Use:** Profile pictures, avatar consistency
  - **Priority:** HIGHEST (40% of dataset)
  - **Tags:** `portrait, upper body, looking at viewer`

- [ ] **2. Standing Confident**
  - **Description:** Waist-up, professional stance
  - **Use:** Hero shots, professional presence
  - **Priority:** HIGH (20% of dataset)
  - **Tags:** `standing, confident pose, waist up`

- [ ] **3. Action/Professional**
  - **Description:** Character performing their role
  - **Use:** Context shots, storytelling
  - **Priority:** HIGH (20% of dataset)
  - **Tags:** `analyzing data, dynamic pose, tech interface`

- [ ] **4. Side Profile**
  - **Description:** Looking left or right, profile view
  - **Use:** Face consistency from angles
  - **Priority:** MEDIUM (10% of dataset)
  - **Tags:** `profile, looking to side`

- [ ] **5. Three-Quarter View**
  - **Description:** 45-degree angle, dynamic
  - **Use:** Dynamic portraits, variety
  - **Priority:** MEDIUM (5% of dataset)
  - **Tags:** `three-quarter view`

- [ ] **6. Environmental/Full Body**
  - **Description:** Full body with background
  - **Use:** Establishing shots, world-building
  - **Priority:** LOW (5% of dataset)
  - **Tags:** `full body, standing`

- [ ] **7. Detail Focus**
  - **Description:** Close-up of eyes or accessory
  - **Use:** Detail emphasis
  - **Priority:** LOW (optional, 0-5%)
  - **Tags:** `close-up, eye focus` or `close-up, accessory focus`

### Custom Poses (Add Your Own)

- [ ] **Custom 1:** [Name] - [Description]

---

## Tag-Based Prompt Construction

### Base Character Tags
```
1girl/1boy, TOKEN, ROLE, HAIR, EYES, FACE, OUTFIT, ACCESSORY
```

### Quality Tags (Always at END)
```
masterpiece, high score, great score, absurdres
```

### Style Tags
```
modern anime style, digital art, newest
```

### Full Example
```
1girl, aikaAI, AI crypto analyst, short silver hair, deep purple eyes, soft facial features, futuristic school uniform with tech accents, holographic data tablet, portrait, looking at viewer, modern anime style, digital art, newest, masterpiece, high score, great score, absurdres
```

---

## Negative Prompt (Use This Exactly)

```
lowres, bad anatomy, bad hands, text, error, missing finger, extra digits, fewer digits, cropped, worst quality, low quality, low score, bad score, average score, signature, watermark, username, blurry, 3d render, realistic, photorealistic, western cartoon
```

---

## Settings for Animagine XL 4.0

| Setting | Value |
|---------|-------|
| Model | animagine-xl-4.0-opt.safetensors |
| Resolution | 1024×1024 |
| Sampler | euler_ancestral |
| Steps | 28 |
| CFG Scale | 5 |
| Seed | 0 |
| Batch Size | 2 |

---

## Caption Format

**Simple Format (Recommended):**
```
TOKEN, role
```

**Example:**
```
aikaAI, AI crypto analyst
```

**With Pose (Optional):**
```
TOKEN, role, pose_keyword
```

**Example:**
```
aikaAI, AI crypto analyst, portrait
```

---

## Example: Completed Spec (Aika - AI Crypto Analyst)

### Basic Information
- **Token:** aikaAI
- **Gender:** 1girl
- **Name:** Aika
- **Role/Profession:** AI Crypto Analyst

### Visual Identity

**Hair:**
- Color: Short silver white
- Style: Slightly spiky with dynamic movement
- Special Features: Subtle blue gradient tips

**Eyes:**
- Color: Deep purple
- Style: Large expressive anime eyes
- Highlights: Star-shaped light reflections

**Face:**
- Shape: Soft with gentle jawline
- Expression: Analytical and confident

**Outfit:**
- Type: Futuristic school uniform
- Primary: Dark navy blue
- Secondary: Silver tech accents
- Details: Glowing circuit patterns on sleeves

**Signature Accessory:**
- Item: Holographic data tablet
- Description: Floating transparent screen with crypto charts
- Effect: Purple and blue holographic glow

### Color Palette
- **Primary:** #C0C0C0 (silver white)
- **Secondary:** #9B59B6 (deep purple)
- **Tertiary:** #0B0F1A (dark navy)
- **Lighting:** Cool silver and purple ambient glow

### Signature Elements
- [x] Floating holographic data screens
- [x] Crypto price ticker displays
- [x] Small AI assistant icon
- [ ] Blockchain network visualizations

### Anime Style
- [x] Modern Anime 2020s (newest)

### Dataset Targets
- **Total:** 30-40 images
- **Portrait (40%):** 12-16 images
- **Waist-Up (40%):** 12-16 images
- **Full Body (20%):** 6-8 images

### Poses
- [x] 1. Portrait
- [x] 2. Standing Confident
- [x] 3. Action/Professional
- [ ] 4. Side Profile
- [ ] 5. Three-Quarter View
- [ ] 6. Environmental/Full Body
- [ ] 7. Detail Focus

### Caption Format
**Simple:** `aikaAI, AI crypto analyst`

---

## Next Steps

1. Fill out this template for your character
2. Review the example (Aika) for guidance
3. Use the Anime Workflow Generator to create workflows
4. Generate 30-40 images following the dataset targets
5. Curate the best images for LoRA training

**Ready? Start filling out the sections above!**

---

## References

- **Anime Skill Guide:** `SKILLS/ANIME_CHARACTER_SKILL.md`
- **Workflow Generator:** `SKILLS/ANIME_WORKFLOW_GENERATOR_PROMPT.md`
- **Validation Guide:** `SKILLS/ANIME_VALIDATION_GUIDE.md`
- **Pose Templates:** `SKILLS/ANIME_PROMPT_TEMPLATES.md`
- **Example Characters:** `characters/hikariAI/`, `characters/aika/`, `SKILLS/examples/anime/aika/`
