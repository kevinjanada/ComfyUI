# Aika Example - Anime Character

This directory contains a complete example anime character using Animagine XL 4.0.

## Character

**Aika** - AI Crypto Analyst
- **Token:** aikaAI
- **Gender:** 1girl
- **Style:** Modern Anime 2020s

## Files

- `aika_spec.md` - Complete character specification
- `aika_portrait_animagine.json` - Portrait workflow
- `aika_standing_animagine.json` - Standing workflow
- `aika_action_animagine.json` - Action workflow

## How to Use

1. **Load a workflow** in ComfyUI
2. **Check settings:**
   - Model: animagine-xl-4.0-opt.safetensors
   - Steps: 28
   - CFG: 5
   - Sampler: euler_ancestral
3. **Generate test images** (batch of 2)
4. **If quality good**, generate full dataset:
   - Portrait: 12-16 images
   - Standing: 12-16 images
   - Action: 6-8 images
5. **Create caption files:** `aikaAI, AI crypto analyst`
6. **Train LoRA**

## Key Features

- **Tag-based prompting** (no weights)
- **Gender tag first** (1girl)
- **Quality tags at end** (masterpiece, high score, great score, absurdres)
- **Anime negative prompt** (excludes 3D/realistic)
- **Modern anime style** with tech elements

## References

- **Anime Skill:** `SKILLS/ANIME_CHARACTER_SKILL.md`
- **Templates:** `SKILLS/ANIME_PROMPT_TEMPLATES.md`
- **Validation:** `SKILLS/ANIME_VALIDATION_GUIDE.md`
