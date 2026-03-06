# JuggernautXL Character Prompt Templates

**Use these templates as starting points for generating character datasets.**

Copy the template, replace `[PLACEHOLDERS]` with your character's details, and paste into the workflow.

---

## Template Structure Explained

```
(CHARACTER_TOKEN:1.2), [ROLE], ([HAIR]:1.1), ([EYES]:1.1), [FACE], ([ACCESSORY]:1.1), [OUTFIT] BREAK
[POSE/ACTION], [ENVIRONMENT], stylized 3D fintech character, highly detailed, sharp focus, professional 3D render
```

**Legend:**
- `()` with `:1.2` or `:1.1` = Weighted (emphasized)
- `BREAK` = Separator between identity and action
- Text without weights = Standard importance

---

## NOVA Templates (AI Market Analyst)

### Base Identity (Never Changes)

```
(novatraderAI:1.2), female AI trading analyst, (short silver hair:1.1), (glowing teal eyes:1.1), (circular holographic halo behind head:1.1), black fintech bodysuit with glowing circuit patterns
```

**Color Palette:** Teal (#00F0FF), Purple (#6B4DFF), Black (#0B0F1A)  
**Signature Elements:** Holographic candlestick charts, teal lighting, fintech interfaces

---

### Template 1: Portrait (Most Important - 40% of dataset)

```
(novatraderAI:1.2), female AI trading analyst, (short silver hair:1.1), (glowing teal eyes:1.1), (circular holographic halo behind head:1.1), black fintech bodysuit with glowing circuit patterns BREAK
portrait shot, minimal background, teal lighting, stylized 3D fintech character, highly detailed, sharp focus, professional 3D render, looking at camera
```

**Use for:** 15-16 images (head and shoulders only)

**Variations to try:**
- Change "looking at camera" → "looking to the side", "slight smile", "confident expression"
- Change "minimal background" → "dark background", "gradient background", "fintech interface background"

---

### Template 2: Standing Confident (20% of dataset)

```
(novatraderAI:1.2), female AI trading analyst, (short silver hair:1.1), (glowing teal eyes:1.1), (circular holographic halo:1.1), black fintech bodysuit with glowing circuit patterns BREAK
standing confidently, arms at sides, waist-up shot, teal and purple lighting, stylized 3D fintech character, highly detailed, sharp focus, professional 3D render
```

**Use for:** 8 images (waist-up, showing bodysuit details)

**Variations to try:**
- "arms crossed" instead of "arms at sides"
- "hands on hips" for more confidence
- Change "waist-up" → "full body" for some variety

---

### Template 3: Chart Analysis (20% of dataset)

```
(novatraderAI:1.2), female AI trading analyst, (short silver hair:1.1), (glowing teal eyes:1.1), (circular holographic halo:1.1), black fintech bodysuit with circuit patterns BREAK
analyzing holographic candlestick charts, pointing at resistance level, futuristic trading interface, teal neon lighting, stylized 3D fintech character, highly detailed, sharp focus
```

**Use for:** 8 images (action pose, showing professional activity)

**Variations to try:**
- "pointing at support level" instead of resistance
- "observing floating crypto data"
- "reviewing market trends on holographic display"

---

### Template 4: Side Profile (10% of dataset)

```
(novatraderAI:1.2), female AI trading analyst, (short silver hair:1.1), (glowing teal eyes:1.1), (circular holographic halo:1.1), black fintech bodysuit with circuit patterns BREAK
side profile view, looking to the right, analyzing financial data streams, teal lighting, stylized 3D fintech character, highly detailed, sharp focus, professional 3D render
```

**Use for:** 4 images (profile view for face consistency)

**Variations to try:**
- "looking to the left" (mirror view)
- "three-quarter view" instead of full profile
- "observing market data" instead of "analyzing"

---

### Template 5: Trading Desk Scene (10% of dataset)

```
(novatraderAI:1.2), female AI trading analyst, (short silver hair:1.1), (glowing teal eyes:1.1), (circular holographic halo:1.1), black fintech bodysuit with circuit patterns BREAK
sitting at futuristic trading desk, surrounded by holographic charts, full body shot, teal neon lighting, stylized 3D fintech character, highly detailed, sharp focus, professional 3D render
```

**Use for:** 4 images (full body, environmental context)

**Note:** Hands may be problematic in desk shots. If hands look bad, crop to waist-up or use portrait instead.

---

### Template 6: Market Scan (Bonus - Optional)

```
(novatraderAI:1.2), female AI trading analyst, (short silver hair:1.1), (glowing teal eyes:1.1), (circular holographic halo:1.1), black fintech bodysuit with circuit patterns BREAK
observing floating crypto market data streams, holographic candlestick charts around her, waist-up shot, teal neon lighting, stylized 3D fintech character, highly detailed, sharp focus
```

**Use for:** 2-4 images (dynamic, data-rich scene)

---

### Template 7: Explaining Trade (Bonus - Optional)

```
(novatraderAI:1.2), female AI trading analyst, (short silver hair:1.1), (glowing teal eyes:1.1), (circular holographic halo:1.1), black fintech bodysuit with circuit patterns BREAK
explaining bitcoin breakout, gesturing toward holographic trading chart, confident pose, teal lighting, stylized 3D fintech character, highly detailed, sharp focus
```

**Use for:** 2-4 images (teaching/explaining pose)

---

## ATHENA Templates (AI Quant Strategist)

### Base Identity (Never Changes)

```
(athenaquantAI:1.2), AI quant strategist, (long platinum hair:1.1), (glowing gold eyes:1.1), (neural crown interface:1.1), white strategist robe with gold accents
```

**Color Palette:** Gold (#FFD700), White (#F4F6F8), Navy (#0A1A33)  
**Signature Elements:** Neural crown interface, quant data streams, neural analysis interface

---

### Template 1: Portrait (Most Important - 40% of dataset)

```
(athenaquantAI:1.2), AI quant strategist, (long platinum hair:1.1), (glowing gold eyes:1.1), (neural crown interface:1.1), white strategist robe with gold accents BREAK
portrait shot, minimal background, gold lighting, stylized 3D fintech character, highly detailed, sharp focus, professional 3D render, looking at camera
```

**Use for:** 15-16 images

**Variations to try:**
- "slight smile", "thoughtful expression", "confident gaze"
- "minimal background" → "dark navy background", "gold gradient background"

---

### Template 2: Strategic Analysis (20% of dataset)

```
(athenaquantAI:1.2), AI quant strategist, (long platinum hair:1.1), (glowing gold eyes:1.1), (neural crown interface:1.1), white strategist robe with gold accents BREAK
analyzing advanced market data streams, gold quant interface floating around her, waist-up shot, gold lighting, stylized 3D fintech character, highly detailed, sharp focus
```

**Use for:** 8 images

**Variations to try:**
- "macro market analysis", "volatility modeling", "risk assessment"

---

### Template 3: Confident Pose (20% of dataset)

```
(athenaquantAI:1.2), AI quant strategist, (long platinum hair:1.1), (glowing gold eyes:1.1), (neural crown interface:1.1), white strategist robe with gold accents BREAK
standing with arms crossed, analyzing market volatility data streams, waist-up shot, gold lighting, stylized 3D fintech character, highly detailed, sharp focus, professional 3D render
```

**Use for:** 8 images

**Variations to try:**
- "hands clasped in front", "one hand raised in explanation"
- Change "waist-up" → "full body" for some

---

### Template 4: Side Profile (10% of dataset)

```
(athenaquantAI:1.2), AI quant strategist, (long platinum hair:1.1), (glowing gold eyes:1.1), (neural crown interface:1.1), white strategist robe with gold accents BREAK
side profile view, looking to the right, reviewing financial data interface, gold lighting, stylized 3D fintech character, highly detailed, sharp focus, professional 3D render
```

**Use for:** 4 images

**Variations:** Same as Nova side profile template

---

### Template 5: Strategy Console (10% of dataset)

```
(athenaquantAI:1.2), AI quant strategist, (long platinum hair:1.1), (glowing gold eyes:1.1), (neural crown interface:1.1), white strategist robe with gold accents BREAK
operating advanced quant analysis console, neural data streams, full body shot, gold lighting, stylized 3D fintech character, highly detailed, sharp focus, professional 3D render
```

**Use for:** 4 images (full body)

---

### Template 6: Macro Market View (Bonus - Optional)

```
(athenaquantAI:1.2), AI quant strategist, (long platinum hair:1.1), (glowing gold eyes:1.1), (neural crown interface:1.1), white strategist robe with gold accents BREAK
observing global market data holograms, multiple data streams, waist-up shot, gold lighting, stylized 3D fintech character, highly detailed, sharp focus
```

**Use for:** 2-4 images

---

### Template 7: Quant Calculation (Bonus - Optional)

```
(athenaquantAI:1.2), AI quant strategist, (long platinum hair:1.1), (glowing gold eyes:1.1), (neural crown interface:1.1), white strategist robe with gold accents BREAK
surrounded by floating quant analysis equations and market indicators, calculating probabilities, waist-up shot, gold lighting, stylized 3D fintech character, highly detailed, sharp focus
```

**Use for:** 2-4 images

---

## Generic Character Template (For Future Characters)

Use this template to create new characters following the same structure:

### Step 1: Define Character Identity

```
(TOKEN:1.2), [ROLE/PROFESSION], ([HAIR_COLOR STYLE]:1.1), ([EYE_COLOR]:1.1), [FACE_STRUCTURE], ([SIGNATURE_ACCESSORY]:1.1), [OUTFIT_DESCRIPTION] BREAK
[POSE], [ENVIRONMENT], stylized 3D fintech character, highly detailed, sharp focus, professional 3D render
```

### Step 2: Fill in the Blanks

| Placeholder | Example (Nova) | Example (Athena) |
|-------------|----------------|------------------|
| TOKEN | novatraderAI | athenaquantAI |
| ROLE | female AI trading analyst | AI quant strategist |
| HAIR | short silver hair | long platinum hair |
| EYES | glowing teal eyes | glowing gold eyes |
| ACCESSORY | circular holographic halo | neural crown interface |
| OUTFIT | black fintech bodysuit | white strategist robe |
| COLOR | teal | gold |

### Step 3: Create Pose Variations

Copy the identity line, then add different BREAK sections:

**Portrait:**
```
...BREAK
portrait shot, minimal background, [COLOR] lighting, stylized 3D fintech character, highly detailed, sharp focus, professional 3D render
```

**Standing:**
```
...BREAK
standing confidently, waist-up shot, [COLOR] lighting, stylized 3D fintech character, highly detailed, sharp focus, professional 3D render
```

**Action:**
```
...BREAK
[PROFESSIONAL_ACTION], [COLOR] lighting, stylized 3D fintech character, highly detailed, sharp focus, professional 3D render
```

---

## Quick Reference: Prompt Building Checklist

Before generating, verify your prompt has:

- [ ] Unique character token weighted (TOKEN:1.2)
- [ ] Role/profession specified
- [ ] Hair described and weighted (1.1)
- [ ] Eyes described and weighted (1.1)
- [ ] Face structure mentioned
- [ ] Signature accessory weighted (1.1)
- [ ] Outfit described
- [ ] BREAK keyword present
- [ ] Pose/action after BREAK
- [ ] Color lighting specified
- [ ] "stylized 3D fintech character" included
- [ ] Quality boosters (highly detailed, sharp focus, professional 3D render)
- [ ] Enhanced negative prompt used

---

## Copy-Paste Ready: Full Negative Prompt

**Use this for ALL generations:**

```
low quality, blurry, distorted face, bad anatomy, bad hands, extra fingers, deformed, ugly, duplicate body parts, multiple characters, 2d, flat, painting, drawing, sketch, photorealistic, realistic, oil painting, watercolor, illustration, anime style, manga, cel shaded, inconsistent lighting, asymmetric eyes, disfigured, mutated, poorly drawn face, poorly drawn hands, missing fingers, extra limbs, fused fingers, too many fingers, long neck, cross-eyed, text, watermark, logo, signature
```

---

## Next Steps

1. **Choose a template** from above (start with Portrait)
2. **Copy the prompt** (select all, Ctrl+C)
3. **Open ComfyUI** and load the appropriate workflow
4. **Paste into the prompt node**
5. **Click "Queue Prompt"**
6. **Generate 4-6 images**, keep the best 1-2
7. **Repeat** with next template/pose
8. **Continue until you have 30-40 images**

**Reference:** `SKILLS/JUGGERNAUT_CHARACTER_SKILL.md` for full skill documentation
